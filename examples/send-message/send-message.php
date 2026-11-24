<?php
// Sends ONE text message. Not executed in the build environment (no PHP). Use your own number first.
$base  = getenv('WHATS360_BASE_URL') ?: 'https://whats360.live/api/v1';
$query = http_build_query([
    'token'       => getenv('WHATS360_TOKEN'),
    'instance_id' => getenv('WHATS360_INSTANCE_ID'),
    'jid'         => getenv('WHATS360_TEST_NUMBER') . '@s.whatsapp.net',
    'msg'         => $argv[1] ?? 'Hello from Whats360 API',
]);
$ch = curl_init("$base/send-text?$query");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 30);
$body = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "HTTP $code\n$body\n";
