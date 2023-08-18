import sys
import os
from readQR.readQR import readQR_code
from pkg_resources import get_distribution, DistributionNotFound

try:
    version_ = get_distribution(__name__).version
except DistributionNotFound:
    version_ = "unknown"
    
__version__ = version_
__all__ = []

if "pdoc" in sys.modules:
    with open("README.md", "r") as fh:
        _readme = fh.read()

package_dir = os.path.dirname(__file__)
artefact_dir = os.path.join(package_dir,"wechat_artefacts")

artefacts = os.listdir(artefact_dir)

for file_name in artefacts:
    if file_name.endswith(".prototxt") or file_name.endswith(".caffemodel"):
        file_path = os.path.join(artefact_dir, file_name)
        model_var_name = "model_"+file_name.replace(".","_")
        globals()[model_var_name] = file_path
        __all__.append(model_var_name)

__all__.extend(['readQR_code'])
