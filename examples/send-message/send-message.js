// Node.js 18+. Sends ONE text message. Use your own number first.
const base = process.env.WHATS360_BASE_URL || 'https://whats360.live/api/v1';
const q = new URLSearchParams({
  token: process.env.WHATS360_TOKEN,
  instance_id: process.env.WHATS360_INSTANCE_ID,
  jid: `${process.env.WHATS360_TEST_NUMBER}@s.whatsapp.net`,
  msg: process.argv[2] || 'Hello from Whats360 API',
});
fetch(`${base}/send-text?${q}`).then(async (r) => console.log(r.status, await r.text()));
