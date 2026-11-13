"""Keep lv-chordia's installed shared-data resolver valid inside PyInstaller."""

import sys

sys.prefix = sys._MEIPASS
