import sys
from readQR.readQR import readQR_code


from pkg_resources import get_distribution, DistributionNotFound
try:
    version_ = get_distribution(__name__).version
except DistributionNotFound:
    version_ = "unknown"
    
__version__ = version_
__all__ = ["readQR_code"]

if "pdoc" in sys.modules:
    with open("README.md", "r") as fh:
        _readme = fh.read()
