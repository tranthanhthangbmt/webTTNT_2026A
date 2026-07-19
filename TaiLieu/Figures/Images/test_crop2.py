import cv2
import numpy as np

def analyze_image(path):
    img = cv2.imread(path)
    if img is None:
        print(f"Could not read {path}")
        return
    
    h, w, c = img.shape
    
    # Detect the horizontal blue lines. The book style typically has:
    # A top blue-green line
    # The figure content
    # A bottom blue-green line
    # And sometimes the caption is between the figure and bottom line, or below the bottom line.
    # Actually, in the screenshot: 
    # Top line, then drawing, then caption, then bottom line.
    # Let's find the top and bottom horizontal lines.
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_teal = np.array([80, 50, 50])
    upper_teal = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lower_teal, upper_teal)
    
    # horizontal lines usually span a large portion of the width
    row_counts = np.sum(mask > 0, axis=1)
    
    # Let's say a horizontal line has > 50% of the width as teal
    line_rows = np.where(row_counts > w * 0.5)[0]
    
    if len(line_rows) > 0:
        top_line = line_rows[0]
        bottom_line = line_rows[-1]
        print(f"Top line at ~{top_line}, Bottom line at ~{bottom_line}")
    else:
        print("No horizontal teal lines found > 50% width.")
        top_line = 0
        bottom_line = h

    # Now let's find where the text "Figure X.Y" is. We can do OCR or just look for the text bounding box.
    # We can use easyocr or pytesseract, but let's just find the bounding box of non-white pixels 
    # between top_line and bottom_line.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # We want to separate the drawing from the caption. 
    # Usually, the drawing is one big connected component or a set of components, 
    # and the caption is a dense block of small components (text) below the drawing.
    # Let's project horizontal density of non-white pixels.
    proj = np.sum(thresh > 0, axis=1)
    
    for r in range(0, h):
        if r in line_rows:
            proj[r] = 0 # zero out the teal lines
            
    # Find continuous blocks of non-white rows
    blocks = []
    in_block = False
    start = 0
    for r in range(top_line+5, bottom_line):
        if proj[r] > 0 and not in_block:
            in_block = True
            start = r
        elif proj[r] == 0 and in_block:
            in_block = False
            blocks.append((start, r))
    if in_block:
        blocks.append((start, bottom_line))
        
    print(f"Non-white row blocks between {top_line} and {bottom_line}:")
    for b in blocks:
        print(b)
        
    # The caption is likely the last block (or blocks) of text.
    # How to distinguish drawing from caption?
    # Caption is usually at the bottom, left-aligned, starts with "Figure" in teal.
    # Let's check if the teal pixels are in the block. The word "Figure" is teal.
    for b in blocks:
        block_mask = mask[b[0]:b[1], :]
        if np.sum(block_mask > 0) > 0:
            print(f"Block {b} contains teal pixels (could be the caption starting with 'Figure', or part of the drawing).")

if __name__ == "__main__":
    analyze_image("figure_2.2.jpg")
