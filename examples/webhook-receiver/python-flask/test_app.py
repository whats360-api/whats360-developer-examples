import unittest
from app import create_app

PAYLOAD = {"phone": "201234567890", "sender_name": "Test", "message": "hi", "message_id": "m1",
           "chat_jid": "201234567890@s.whatsapp.net", "timestamp": "2026-01-01T00:00:00Z", "media_url": "", "instance_id": "DEVICE_ID"}

class T(unittest.TestCase):
    def setUp(self):
        self.app = create_app(":memory:"); self.c = self.app.test_client()
    def test_store_and_dedupe(self):
        r = self.c.post("/whats360/webhook", json=PAYLOAD)
        self.assertEqual((r.status_code, r.json["status"]), (200, "stored"))
        r = self.c.post("/whats360/webhook", json=PAYLOAD)
        self.assertEqual((r.status_code, r.json["status"]), (200, "duplicate"))
        self.assertEqual(self.app.con.execute("select count(*) from events").fetchone()[0], 1)
    def test_junk_gets_200(self):
        r = self.c.post("/whats360/webhook", data="not json", content_type="text/plain")
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()
