from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r") as f:
    requirements = f.readlines()
    
name_ = "readQR"
desc_ = "Read QR code from image using WeChat QR code reader in OpenCV"

setup(
    name=name_,
    version="0.1.0",
    description=desc_,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Collins Wakholi",
    url="https://github.com/CollinsWakholi/readQR_weChat",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'':['wechat_artefacts/*.prototxt', 'wechat_artefacts/*.caffemodel']},
)