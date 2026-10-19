#!/bin/zsh
cd "${0:A:h}"
if [[ -x "$PWD/.tools/calibre.app/Contents/MacOS/ebook-convert" ]]; then
  export CALIBRE="$PWD/.tools/calibre.app/Contents/MacOS"
elif [[ -x /Applications/calibre.app/Contents/MacOS/ebook-convert ]]; then
  export CALIBRE=/Applications/calibre.app/Contents/MacOS
fi
exec .venv/bin/taguette --browser --bind 127.0.0.1 --database "$PWD/local.sqlite3"
