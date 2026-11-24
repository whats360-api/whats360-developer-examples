# Bulk sending

Two routes exist:
1. Campaign endpoints (`campaigns/create`, `recipients`, `start`, ...). The create body is documented only as name plus message_content. The recipients body is not documented, so no example is provided yet. See known gaps.
2. A paced loop over `send-text` ([send_bulk.py](send_bulk.py)). Dry run by default.

Send only to opted-in contacts. This repository makes no promise about WhatsApp account restrictions.
