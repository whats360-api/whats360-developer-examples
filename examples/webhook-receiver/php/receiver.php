<?php
// Plain PHP receiver for a Whats360 OUTGOING webhook, stored in SQLite (PDO).
// NOT executed in the build environment (no PHP available). Review before use.
// Documented fields: phone, sender_name, message, message_id, chat_jid, timestamp, media_url, instance_id.
$fields = ['phone','sender_name','message','message_id','chat_jid','timestamp','media_url','instance_id'];
$db = new PDO('sqlite:' . (getenv('DB_PATH') ?: __DIR__ . '/webhooks.sqlite'));
$db->exec('CREATE TABLE IF NOT EXISTS events (message_id TEXT PRIMARY KEY, phone TEXT, sender_name TEXT, message TEXT, chat_jid TEXT, timestamp TEXT, media_url TEXT, instance_id TEXT)');
$data = json_decode(file_get_contents('php://input'), true);
header('Content-Type: application/json');
if (!is_array($data)) { echo json_encode(['status' => 'ignored']); exit; } // still 200
$stmt = $db->prepare('INSERT OR IGNORE INTO events (' . implode(',', $fields) . ') VALUES (' . rtrim(str_repeat('?,', count($fields)), ',') . ')');
$stmt->execute(array_map(fn($f) => (string)($data[$f] ?? ''), $fields));
echo json_encode(['status' => $stmt->rowCount() === 0 ? 'duplicate' : 'stored']);
