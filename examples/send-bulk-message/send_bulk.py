"""Sends the same text to a short list of numbers, one at a time, with a delay.

This uses the documented send-text endpoint in a loop. It does NOT use the campaign
endpoints because the campaign recipients request body is not documented yet.
Only send to people who agreed to receive messages. Dry run is the default.

Usage: python send_bulk.py numbers.txt "Message text"          (prints what it would send)
       python send_bulk.py numbers.txt "Message text" --send   (really sends)
"""
import os, sys, time, urllib.parse, urllib.request, urllib.error

def build_url(number, msg):
    base = os.environ.get("WHATS360_BASE_URL", "https://whats360.live/api/v1")
    q = urllib.parse.urlencode({"token": os.environ.get("WHATS360_TOKEN", ""),
                                "instance_id": os.environ.get("WHATS360_INSTANCE_ID", ""),
                                "jid": number + "@s.whatsapp.net", "msg": msg})
    return f"{base}/send-text?{q}"

def main(argv):
    path, msg = argv[1], argv[2]
    really = "--send" in argv
    delay = float(os.environ.get("WHATS360_DELAY_SECONDS", "5"))
    numbers = [l.strip() for l in open(path) if l.strip() and not l.startswith("#")]
    for n in numbers:
        if not really:
            print("DRY RUN would send to", n)
            continue
        try:
            with urllib.request.urlopen(build_url(n, msg), timeout=30) as r:
                print(n, r.status)
        except urllib.error.HTTPError as e:
            print(n, "error", e.code)   # see errors.md: 403 limit reached, 463 chat not open
        time.sleep(delay)

if __name__ == "__main__":
    main(sys.argv)
