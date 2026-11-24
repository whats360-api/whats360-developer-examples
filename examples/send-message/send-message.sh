#!/usr/bin/env bash
# Sends ONE text message. Use your own number first.
set -euo pipefail
: "${WHATS360_TOKEN:?set WHATS360_TOKEN}" "${WHATS360_INSTANCE_ID:?set WHATS360_INSTANCE_ID}" "${WHATS360_TEST_NUMBER:?set WHATS360_TEST_NUMBER}"
BASE="${WHATS360_BASE_URL:-https://whats360.live/api/v1}"
curl -G "$BASE/send-text" \
  --data-urlencode "token=$WHATS360_TOKEN" \
  --data-urlencode "instance_id=$WHATS360_INSTANCE_ID" \
  --data-urlencode "jid=${WHATS360_TEST_NUMBER}@s.whatsapp.net" \
  --data-urlencode "msg=${1:-Hello from Whats360 API}"
echo
