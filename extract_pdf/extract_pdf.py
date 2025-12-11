import os
import cv2
import numpy as np
from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

def extract_pdf_to_txt(pdf_path, output_txt, total_pages=88):
    """
    Extracts text and math from a math-heavy PDF to a single .txt file with progress.
    
    Args:
        pdf_path (str): Path to the input PDF file (e.g., 'Lec1 - transformers.pdf').
        output_txt (str): Path to the output .txt file (e.g., 'Lec1 - transformers.txt').
        total_pages (int): Total number of pages in the PDF (default 88).
    """
    # Ensure input file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Input PDF not found: {pdf_path}")

    # Convert PDF to images (high DPI for better OCR)
    images = convert_from_path(pdf_path, dpi=300, output_folder='temp_images', fmt='png')
    if not images:
        raise ValueError("Failed to convert PDF to images. Check Poppler installation.")

    # Configure Tesseract for math and layout (PSM 6 for single block, OEM 3 for LSTM OCR)
    custom_config = r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;()=+-*/<>{}[]|^~!@#$%&_'

    # Extract text and math from images with progress
    extracted_text = []
    for i, img in enumerate(images, 1):
        print(f"Processing page {i} of {total_pages}", end="\r")
        # Convert PIL image to OpenCV format
        open_cv_image = np.array(img)
        open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR

        # OCR with Tesseract
        page_text = pytesseract.image_to_string(open_cv_image, config=custom_config)
        extracted_text.append(f"--- Page {i} ---\n{page_text}\n")

    print(f"Processing page {total_pages} of {total_pages} [Done]")

    # Save to single .txt file
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write("\n".join(extracted_text))
    print(f"Extraction complete! Output saved to: {output_txt}")

    # Clean up temporary images
    for img_path in Path('temp_images').glob('*.png'):
        os.remove(img_path)
    os.rmdir('temp_images')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract math-heavy PDF to TXT with progress using Tesseract.")
    parser.add_argument('pdf_path', type=str, help="Path to the input PDF file.")
    parser.add_argument('output_txt', type=str, help="Path to the output TXT file.")
    args = parser.parse_args()

    try:
        extract_pdf_to_txt(args.pdf_path, args.output_txt)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Ensure all dependencies are installed and Poppler is configured. On Arch Linux, use 'sudo pacman -S poppler'.")
