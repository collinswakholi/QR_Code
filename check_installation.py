#!/usr/bin/env python3
"""
Installation verification script for readQR package
Run this to check if all dependencies are properly installed
"""
import sys

def main():
    print("=== OpenCV Installation Check ===\n")
    
    all_ok = True

    # Check OpenCV
    try:
        import cv2
        print(f"✓ OpenCV installed: {cv2.__version__}")
    except ImportError as e:
        print(f"✗ OpenCV not installed: {e}")
        all_ok = False

    # Check WeChat QR detector
    try:
        import cv2
        if hasattr(cv2, 'wechat_qrcode_WeChatQRCode'):
            print("✓ WeChat QR detector available")
        else:
            print("✗ WeChat QR detector NOT available")
            print("\n  Please install opencv-contrib-python:")
            print("    pip uninstall opencv-python opencv-contrib-python -y")
            print("    pip install opencv-contrib-python>=4.5.0")
            all_ok = False
    except:
        all_ok = False

    # Check other dependencies
    try:
        import numpy as np
        print(f"✓ NumPy installed: {np.__version__}")
    except ImportError:
        print("✗ NumPy not installed")
        all_ok = False

    try:
        import matplotlib
        print(f"✓ Matplotlib installed: {matplotlib.__version__}")
    except ImportError:
        print("✗ Matplotlib not installed")
        all_ok = False

    # Check readQR package
    try:
        from readQR import ReadQR
        print("✓ readQR package available")
    except ImportError as e:
        print(f"✗ readQR package not available: {e}")
        all_ok = False

    # Check for conflicting packages
    try:
        import pkg_resources
        installed_packages = {pkg.key for pkg in pkg_resources.working_set}
        opencv_packages = [pkg for pkg in installed_packages if 'opencv' in pkg]
        
        if len(opencv_packages) > 1:
            print(f"\n⚠ Warning: Multiple OpenCV packages detected: {opencv_packages}")
            print("  This may cause conflicts. Recommended:")
            print("    pip uninstall " + " ".join(opencv_packages) + " -y")
            print("    pip install opencv-contrib-python>=4.5.0")
    except:
        pass

    print("\n" + "="*50)
    if all_ok:
        print("✓ All dependencies installed correctly!")
        print("\nYou can now use the readQR package.")
        return 0
    else:
        print("✗ Some dependencies are missing or incorrect.")
        print("\nPlease run:")
        print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())
