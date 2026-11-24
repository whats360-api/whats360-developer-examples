# whats360.live Developer Examples (WhatsApp API code samples)

Code samples for the [whats360.live](https://whats360.live) WhatsApp API in cURL, PHP, Node.js and Python. Every request uses only endpoints and parameters from the [official API reference](https://github.com/whats360-api/whats360-api-docs). Test data is fake. Credentials come from environment variables (see `.env.example`).

| Folder | What it shows | Verification |
|---|---|---|
| examples/send-message | Send a text: cURL, PHP, Node.js, Python | Node and Python: syntax checked. PHP, cURL: PHP not run, shell syntax checked. No live send. |
| examples/send-media | Image, video, audio, document via public URL | shell syntax checked, not sent |
| examples/send-bulk-message | Paced loop over send-text with dry-run default | dry run executed locally |
| examples/webhook-receiver | Outgoing webhook receivers: Flask, Express, PHP, Laravel | Flask 2 tests, Express 1 test pass locally. PHP and Laravel not executed |
| examples/error-handling | Documented error codes mapped to actions | 3 unit tests pass |

**Not live-tested.** No example was run against the whats360.live production API and no real message was sent. Treat all code as examples, not production-ready.

Notes: whats360.live links WhatsApp numbers by QR code. It is not the Meta Cloud API. No account-restriction guarantees are made. Send only to people who agreed to receive messages.

Related: [API docs](https://github.com/whats360-api/whats360-api-docs) · [Webhooks](https://github.com/whats360-api/whats360-webhooks) · [Integration examples](https://github.com/whats360-api/whats360-integration-examples) · Support https://wa.me/201030741766
