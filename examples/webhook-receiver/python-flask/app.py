"""Receives a Whats360 OUTGOING webhook and stores it in SQLite.

Documented payload fields: phone, sender_name, message, message_id, chat_jid,
timestamp, media_url, instance_id. Event names, signatures and retry policy are
not documented for outgoing webhooks, so none are assumed. Duplicates are ignored
by message_id. Respond 200 quickly.
"""
import os, sqlite3
from flask import Flask, request, jsonify

FIELDS = ("phone", "sender_name", "message", "message_id", "chat_jid", "timestamp", "media_url", "instance_id")

def create_app(db_path=None):
    app = Flask(__name__)
    db_path = db_path or os.environ.get("DB_PATH", "webhooks.sqlite")
    con = sqlite3.connect(db_path, check_same_thread=False)
    con.execute("CREATE TABLE IF NOT EXISTS events (message_id TEXT PRIMARY KEY, " + ", ".join(f + " TEXT" for f in FIELDS if f != "message_id") + ")")
    con.commit()

    @app.post("/whats360/webhook")
    def webhook():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify(status="ignored"), 200      # still 200: do not make the sender retry junk
        row = [str(data.get(f, "")) for f in FIELDS]
        cur = con.execute("INSERT OR IGNORE INTO events (" + ", ".join(FIELDS) + ") VALUES (" + ",".join("?" * len(FIELDS)) + ")", row)
        con.commit()
        return jsonify(status="duplicate" if cur.rowcount == 0 else "stored"), 200

    app.con = con
    return app

if __name__ == "__main__":
    create_app().run(port=int(os.environ.get("PORT", 5000)))
