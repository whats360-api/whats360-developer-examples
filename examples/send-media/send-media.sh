#!/usr/bin/env bash
# Usage: send-media.sh image|video|audio|doc "https://public.example.com/file" ["caption"]
# Media URLs must be direct, publicly reachable links. Audio has no caption parameter.
set -euo pipefail
kind="$1"; url="$2"; caption="${3:-}"
BASE="${WHATS360_BASE_URL:-https://whats360.live/api/v1}"
case "$kind" in
  image) path=send-image; param=imageurl ;;
  video) path=send-video; param=videourl ;;
  audio) path=send-audio; param=audiourl ;;
  doc)   path=send-doc;   param=docurl ;;
  *) echo "kind must be image, video, audio or doc" >&2; exit 2 ;;
esac
args=(--data-urlencode "token=$WHATS360_TOKEN" --data-urlencode "instance_id=$WHATS360_INSTANCE_ID" \
      --data-urlencode "jid=${WHATS360_TEST_NUMBER}@s.whatsapp.net" --data-urlencode "$param=$url")
if [ -n "$caption" ] && [ "$kind" != audio ]; then args+=(--data-urlencode "caption=$caption"); fi
curl -G "$BASE/$path" "${args[@]}"; echo
