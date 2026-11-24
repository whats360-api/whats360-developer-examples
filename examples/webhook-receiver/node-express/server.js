// Express receiver for a Whats360 OUTGOING webhook, stored in SQLite (node:sqlite, Node 22+).
// Documented fields: phone, sender_name, message, message_id, chat_jid, timestamp, media_url, instance_id.
// No signature or retry policy is documented for outgoing webhooks, so none is assumed.
const express = require('express');
const { DatabaseSync } = require('node:sqlite');

const FIELDS = ['phone', 'sender_name', 'message', 'message_id', 'chat_jid', 'timestamp', 'media_url', 'instance_id'];

function createApp(dbPath = process.env.DB_PATH || 'webhooks.sqlite') {
  const db = new DatabaseSync(dbPath);
  db.exec(`CREATE TABLE IF NOT EXISTS events (message_id TEXT PRIMARY KEY, ${FIELDS.filter((f) => f !== 'message_id').map((f) => f + ' TEXT').join(', ')})`);
  const insert = db.prepare(`INSERT OR IGNORE INTO events (${FIELDS.join(',')}) VALUES (${FIELDS.map(() => '?').join(',')})`);
  const app = express();
  app.use(express.json({ limit: '1mb' }));
  app.post('/whats360/webhook', (req, res) => {
    const d = req.body && typeof req.body === 'object' ? req.body : null;
    if (!d) return res.status(200).json({ status: 'ignored' });
    const r = insert.run(...FIELDS.map((f) => String(d[f] ?? '')));
    res.status(200).json({ status: r.changes === 0 ? 'duplicate' : 'stored' });
  });
  app.db = db;
  return app;
}

if (require.main === module) createApp().listen(process.env.PORT || 3000);
module.exports = { createApp };
