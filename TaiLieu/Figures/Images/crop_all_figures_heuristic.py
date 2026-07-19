import cv2
import numpy as np
import os
import glob

def find_caption_and_crop(path):
    img = cv2.imread(path)
    if img is None:
        return False
        
    h, w, c = img.shape
    
    # 1. Identify true teal separator lines
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_teal = np.array([80, 50, 50])
    upper_teal = np.array([100, 255, 255])
    teal_mask = cv2.inRange(hsv, lower_teal, upper_teal)
    
    row_counts = np.sum(teal_mask > 0, axis=1)
    
    # We define a separator line as one where >40% of the width is teal
    # BUT its thickness must be small (< 15 pixels)
    is_teal_row = row_counts > w * 0.4
    
    line_blocks = []
    in_line = False
    start = 0
    for r in range(h):
        if is_teal_row[r] and not in_line:
            in_line = True
            start = r
        elif not is_teal_row[r] and in_line:
            in_line = False
            line_blocks.append((start, r))
    if in_line:
        line_blocks.append((start, h))
        
    separator_lines = [b for b in line_blocks if (b[1] - b[0]) < 15]
    
    # Create a mask of all non-white pixels
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # Erase the separator lines from the non-white mask
    for b in separator_lines:
        thresh[b[0]:b[1], :] = 0
        
    # Project horizontally to find content blocks
    proj = np.sum(thresh > 0, axis=1)
    blocks = []
    in_block = False
    start = 0
    for r in range(h):
        if proj[r] > 0 and not in_block:
            in_block = True
            start = r
        elif proj[r] == 0 and in_block:
            in_block = False
            blocks.append((start, r))
    if in_block:
        blocks.append((start, h))
        
    if not blocks:
        return False
        
    # Merge blocks that are very close (gap < 20 pixels)
    merged_blocks = [blocks[0]]
    for i in range(1, len(blocks)):
        prev_start, prev_end = merged_blocks[-1]
        curr_start, curr_end = blocks[i]
        if curr_start - prev_end < 20: 
            merged_blocks[-1] = (prev_start, curr_end)
        else:
            merged_blocks.append(blocks[i])
            
    # Remove lines from teal mask to check for "Figure" text
    teal_mask_no_lines = teal_mask.copy()
    for b in separator_lines:
        teal_mask_no_lines[b[0]:b[1], :] = 0
        
    caption_start_row = h
    # Look for the caption from bottom up
    for b in reversed(merged_blocks):
        b_start, b_end = b
        
        # Calculate the bounding box of teal pixels in this block
        block_teal = teal_mask_no_lines[b_start:b_end, :]
        rows_with_teal = np.where(np.sum(block_teal, axis=1) > 0)[0]
        cols_with_teal = np.where(np.sum(block_teal, axis=0) > 0)[0]
        
        if len(rows_with_teal) > 0 and len(cols_with_teal) > 0:
            teal_h = rows_with_teal[-1] - rows_with_teal[0]
            teal_w = cols_with_teal[-1] - cols_with_teal[0]
            
            # The word "Figure X.Y" is relatively small.
            # E.g. width < 150 pixels, height < 30 pixels.
            # If the teal bounding box is huge, it's a drawing!
            if teal_w < 300 and teal_h < 50:
                # Also, caption is usually at the bottom and left-aligned.
                if cols_with_teal[0] < w * 0.3: # starts in the left 30% of image
                    caption_start_row = b_start
                    break
                    
    # Top of content
    content_top = 0
    for b in merged_blocks:
        if b[0] < caption_start_row:
            content_top = b[0]
            break
            
    # Bottom of drawing
    content_bottom = 0
    for b in reversed(merged_blocks):
        if b[1] <= caption_start_row:
            content_bottom = b[1]
            break
            
    crop_top = max(0, content_top - 5)
    crop_bottom = min(h, content_bottom + 5)
    
    if content_bottom <= content_top or caption_start_row == h:
        # Fallback: keep all non-white blocks
        if len(merged_blocks) > 0:
            crop_top = max(0, merged_blocks[0][0] - 5)
            crop_bottom = min(h, merged_blocks[-1][1] + 5)
        else:
            return False

    cropped_img = img[crop_top:crop_bottom, :]
    cv2.imwrite(path, cropped_img)
    return True

if __name__ == "__main__":
    files = glob.glob("*.jpg")
    print(f"Found {len(files)} images to process.")
    success_count = 0
    for i, f in enumerate(files):
        if find_caption_and_crop(f):
            success_count += 1
        if (i+1) % 50 == 0:
            print(f"Processed {i+1} images...")
            
    print(f"Successfully cropped: {success_count} / {len(files)}")
