# Webhook receivers

Receivers for the Whats360 **outgoing** webhook (Whats360 posts message data to your URL). Documented payload fields only: `phone, sender_name, message, message_id, chat_jid, timestamp, media_url, instance_id`.

| Folder | Stack | Test status |
|---|---|---|
| python-flask | Flask + SQLite | 2 unit tests pass (Flask test client, in memory) |
| node-express | Express + node:sqlite (Node 22.5+) | 1 integration test passes against a local server |
| php | Plain PHP + PDO SQLite | not executed |
| laravel | Controller sketch | not executed |

All of them answer 200 quickly, ignore duplicates by `message_id`, and store to a local database. None invents an event name, signature or retry rule: those are not documented for outgoing webhooks. If you add a secret header, define it in your webhook settings and check it yourself.

Security: use HTTPS, keep your webhook URL private, do not log full message bodies in production, do not put customer data in public issues.
