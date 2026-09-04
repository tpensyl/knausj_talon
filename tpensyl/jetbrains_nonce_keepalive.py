import tempfile
from pathlib import Path

from talon import cron

# macOS purges $TMPDIR entries untouched for 3 days, and APFS does not refresh
# atime on read, so an IDE session outliving that loses the nonce file its
# command server wrote at startup and user.idea() fails until the IDE restarts.
def touch_idea_nonce_files():
    for path in Path(tempfile.gettempdir()).glob("*vcidea_*"):
        try:
            path.touch()
        except OSError as e:
            print(e)


cron.interval("12h", touch_idea_nonce_files)
