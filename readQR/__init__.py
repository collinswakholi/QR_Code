import sys
from readQR.readQR import ReadQR

# Use importlib.metadata instead of deprecated pkg_resources
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # Python < 3.8 fallback
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["ReadQR"]

if "pdoc" in sys.modules:
    with open("README.md", "r", encoding="utf-8") as fh:
        _readme = fh.read()
