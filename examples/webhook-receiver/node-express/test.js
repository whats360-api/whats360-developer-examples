const test = require('node:test');
const assert = require('node:assert');
const { createApp } = require('./server');

test('stores once, dedupes, always 200', async () => {
  const app = createApp(':memory:');
  const server = app.listen(0);
  const url = `http://127.0.0.1:${server.address().port}/whats360/webhook`;
  const body = JSON.stringify({ phone: '201234567890', message: 'hi', message_id: 'm1', instance_id: 'DEVICE_ID' });
  const post = (b) => fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: b });
  assert.strictEqual((await (await post(body)).json()).status, 'stored');
  assert.strictEqual((await (await post(body)).json()).status, 'duplicate');
  assert.strictEqual(app.db.prepare('select count(*) c from events').get().c, 1);
  server.close();
});
