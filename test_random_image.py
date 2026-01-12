#!/usr/bin/env python3
"""
Test script to run QR code reader on a random image from the images folder
"""
import os
import random
import cv2
from readQR import ReadQR
import readQR.wechat_artefacts as artefacts

def main():
    # Get the images directory
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    
    # Get all image files in the images directory
    image_files = [f for f in os.listdir(images_dir) 
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    if not image_files:
        print("No image files found in the images directory!")
        return
    
    # Select a random image
    random_image = random.choice(image_files)
    image_path = os.path.join(images_dir, random_image)
    
    print(f"Testing with random image: {random_image}")
    print(f"Full path: {image_path}")
    print("-" * 50)
    
    # Load the image
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return
    
    print(f"Image loaded successfully. Shape: {img.shape}")
    
    # Get the wechat artefacts directory
    art_dir = artefacts.__path__[0]
    
    # Initialize the QR code reader
    print("Initializing QR code reader...")
    reader = ReadQR(artefact_path=art_dir)
    
    # Decode QR codes from the image
    # Set show="single" to display the image with detected QR codes highlighted
    # Set show=None to skip display (recommended for headless environments)
    print("Decoding QR codes from image...")
    result = reader.decode(img, show=None)
    
    # Print the results
    print("-" * 50)
    if result and len(result) > 0:
        print(f"Found {len(result)} QR code(s):")
        for i, data in enumerate(result, 1):
            print(f"  QR Code {i}: {data}")
    else:
        print("No QR codes detected in the image.")
    
    print("-" * 50)
    print("Test completed!")

if __name__ == "__main__":
    main()
