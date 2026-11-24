"""Sends ONE text message using only the standard library. Use your own number first."""
import os, sys, urllib.parse, urllib.request, urllib.error

base = os.environ.get("WHATS360_BASE_URL", "https://whats360.live/api/v1")
query = urllib.parse.urlencode({
    "token": os.environ["WHATS360_TOKEN"],
    "instance_id": os.environ["WHATS360_INSTANCE_ID"],
    "jid": os.environ["WHATS360_TEST_NUMBER"] + "@s.whatsapp.net",
    "msg": sys.argv[1] if len(sys.argv) > 1 else "Hello from Whats360 API",
})
try:
    with urllib.request.urlopen(f"{base}/send-text?{query}", timeout=30) as r:
        print(r.status, r.read().decode())
except urllib.error.HTTPError as e:
    print(e.code, e.read().decode())
