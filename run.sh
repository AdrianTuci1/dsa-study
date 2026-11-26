#!/usr/bin/env bash
# Fetch this repository from GitHub, build the image and run it.
#
#   REPO=your-user/dsa-study
#   curl -fsSL "https://raw.githubusercontent.com/$REPO/main/run.sh" \
#     | DSA_STUDY_REPO="$REPO" bash
#
# Optional environment variables:
#   DSA_STUDY_REPO   GitHub slug (owner/repo)        default: OWNER/REPO
#   DSA_STUDY_REF    branch or tag                   default: main
#   DSA_STUDY_PORT   host port                       default: 8765
#   DSA_STUDY_IMAGE  docker image tag                default: dsa-study
#   DSA_STUDY_DIR    download directory              default: ${TMPDIR:-/tmp}/dsa-study

set -euo pipefail

REPO="${DSA_STUDY_REPO:-OWNER/REPO}"
REF="${DSA_STUDY_REF:-main}"
PORT="${DSA_STUDY_PORT:-8765}"
IMAGE="${DSA_STUDY_IMAGE:-dsa-study}"
DIR="${DSA_STUDY_DIR:-${TMPDIR:-/tmp}/dsa-study}"

if ! command -v docker >/dev/null 2>&1; then
  echo "error: docker is required" >&2
  exit 1
fi

if [ "$REPO" = "OWNER/REPO" ]; then
  cat >&2 <<'EOF'
error: set the GitHub repository first.

  REPO=your-user/dsa-study
  curl -fsSL "https://raw.githubusercontent.com/$REPO/main/run.sh" | DSA_STUDY_REPO="$REPO" bash
EOF
  exit 1
fi

case "$DIR" in
  ""|"/"|"$HOME")
    echo "error: refusing DSA_STUDY_DIR=$DIR" >&2
    exit 1
    ;;
esac

echo "Downloading https://github.com/$REPO/archive/refs/heads/$REF.tar.gz ..."
rm -rf "$DIR"
mkdir -p "$DIR"
curl -fsSL "https://github.com/$REPO/archive/refs/heads/$REF.tar.gz" \
  | tar -xz -C "$DIR" --strip-components=1

echo "Building image $IMAGE ..."
docker build -t "$IMAGE" "$DIR"

echo "Starting http://127.0.0.1:$PORT/  (Ctrl+C stops the container)"
exec docker run --rm -p "$PORT:8765" "$IMAGE"
