import sys
from readQR.readQR import ReadQR


from pkg_resources import get_distribution, DistributionNotFound
try:
    version_ = get_distribution(__name__).version
except DistributionNotFound:
    version_ = "unknown"
    
__version__ = version_
__all__ = ["ReadQR"]

if "pdoc" not in sys.modules:
    with open("README.md", "r", encoding="utf-8") as fh:
        _readme = fh.read()