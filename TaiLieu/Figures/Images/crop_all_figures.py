import cv2
import numpy as np
import os
import glob

def find_caption_and_crop(path):
    img = cv2.imread(path)
    if img is None:
        print(f"Error reading {path}")
        return False
        
    h, w, c = img.shape
    
    # 1. Identify teal pixels (used for lines and "Figure" text)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_teal = np.array([80, 50, 50])
    upper_teal = np.array([100, 255, 255])
    teal_mask = cv2.inRange(hsv, lower_teal, upper_teal)
    
    # Remove long horizontal lines from the teal mask so they don't confuse the text detection
    row_counts = np.sum(teal_mask > 0, axis=1)
    teal_mask_no_lines = teal_mask.copy()
    teal_mask_no_lines[row_counts > w * 0.3, :] = 0
    
    # 2. Identify all non-white content
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # Remove horizontal teal lines from the non-white mask too
    thresh[row_counts > w * 0.3, :] = 0
    
    # Project horizontally to find blocks of content
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
        print(f"No content in {os.path.basename(path)}, skipping.")
        return False
        
    # Merge blocks that are very close (e.g., text lines in a caption)
    # Gap < 20 pixels -> same block
    merged_blocks = [blocks[0]]
    for i in range(1, len(blocks)):
        prev_start, prev_end = merged_blocks[-1]
        curr_start, curr_end = blocks[i]
        if curr_start - prev_end < 20: 
            merged_blocks[-1] = (prev_start, curr_end)
        else:
            merged_blocks.append(blocks[i])
            
    # Look for the caption from the bottom up.
    # The caption should contain teal pixels (the word "Figure").
    caption_start_row = h
    for b in reversed(merged_blocks):
        b_start, b_end = b
        # Check if this block has teal pixels
        if np.sum(teal_mask_no_lines[b_start:b_end, :]) > 10:
            # Found the caption!
            caption_start_row = b_start
            break
            
    # Find the top content to crop out empty space at the top
    content_top = 0
    for b in merged_blocks:
        if b[0] < caption_start_row:
            content_top = b[0]
            break
            
    # Find the bottom of the drawing
    content_bottom = 0
    for b in reversed(merged_blocks):
        if b[1] <= caption_start_row:
            content_bottom = b[1]
            break
            
    # Add a small padding (e.g., 5 pixels) but make sure it doesn't go out of bounds
    crop_top = max(0, content_top - 5)
    crop_bottom = min(h, content_bottom + 5)
    
    # If the script failed to find a separation and wants to crop out everything,
    # or if the image is just a drawing with NO caption (e.g. caption wasn't found),
    # fallback to just keeping everything except the top/bottom horizontal lines.
    if content_bottom <= content_top or caption_start_row == h:
        # Fallback: crop from first to last non-white block
        if len(merged_blocks) > 0:
            crop_top = max(0, merged_blocks[0][0] - 5)
            crop_bottom = min(h, merged_blocks[-1][1] + 5)
        else:
            # Fallback fail
            return False

    cropped_img = img[crop_top:crop_bottom, :]
    
    # Overwrite the original file
    cv2.imwrite(path, cropped_img)
    return True

if __name__ == "__main__":
    files = glob.glob("*.jpg")
    success_count = 0
    fail_count = 0
    for f in files:
        if find_caption_and_crop(f):
            success_count += 1
        else:
            fail_count += 1
            
    print(f"Finished processing {len(files)} images.")
    print(f"Successfully cropped: {success_count}")
    print(f"Failed to crop: {fail_count}")
