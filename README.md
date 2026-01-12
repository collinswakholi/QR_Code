# Read QR code

## Description
This is a simple python script that reads a QR code from an image and prints the result.
It uses the WeChat QR code reader API in OpenCV to read the QR code from a CV2 image.

## Requirements
**Important:** This package requires `opencv-contrib-python`, NOT the standard `opencv-python` package.

## Installation

### Option 1: Install from pip (recommended)
```shell
pip install readQR
```

### Option 2: Install from source
```shell
# Clone the repository
git clone https://github.com/CollinsWakholi/QR_Code.git
cd QR_Code

# Uninstall any existing opencv packages to avoid conflicts
pip uninstall opencv-python opencv-contrib-python -y

# Install dependencies (opencv-contrib-python includes all standard OpenCV features)
pip install -r requirements.txt
```

**Note:** If you have `opencv-python` installed, you MUST uninstall it first:
```shell
pip uninstall opencv-python opencv-contrib-python -y
pip install opencv-contrib-python>=4.5.0
```

The WeChat QR code detector is only available in `opencv-contrib-python`, not in the standard `opencv-python` package. Having both installed can cause conflicts.

### Verify Installation
After installation, verify everything is set up correctly:
```shell
python check_installation.py
```

## Usage
```python
from readQR import ReadQR
import readQR.wechat_artefacts as artefacts
import cv2

art_dir = artefacts.__path__[0]
img = cv2.imread('test.png')
reader = ReadQR(artefact_path=art_dir)
show = None # Set to "single" or "continuous" to show the image with the QR code highlighted for single or continuous frames (video)
result = reader.decode(img, show=show)
[print(r) for r in result]
```
##  Sample input and output images

### Input images

<img src="images/single_qr.jpeg" width="400"/> <img src="images/multiple_qr.jpg" width="400"/>

### Output images
<img src="images/single_qr_det.jpg" width="400"/> <img src="images/multiple_qr_det.jpg" width="400"/>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
None

## Acknowledgemnts
I am gratefully acknowledge [Devin Rippner](mailto:devin.rippner@usda.gov), [ORISE](https://orise.orau.gov/index.html), and the [USDA](https://www.usda.gov/) for their invaluable assistance and funding support in the development of this Repo. This project would not have been possible without their guidance and opportunities provided.
