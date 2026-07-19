import cv2
import numpy as np
import os
import glob

def analyze_image(path):
    img = cv2.imread(path)
    if img is None:
        return
    h, w, c = img.shape
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_teal = np.array([80, 50, 50])
    upper_teal = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lower_teal, upper_teal)
    
    row_counts = np.sum(mask > 0, axis=1)
    line_rows = np.where(row_counts > w * 0.3)[0]
    
    lines = []
    # group adjacent line rows
    if len(line_rows) > 0:
        start = line_rows[0]
        for i in range(1, len(line_rows)):
            if line_rows[i] - line_rows[i-1] > 5:
                lines.append((start, line_rows[i-1]))
                start = line_rows[i]
        lines.append((start, line_rows[-1]))
        
    print(f"File {os.path.basename(path)}: size={w}x{h}, horizontal teal lines={lines}")

if __name__ == "__main__":
    files = glob.glob("*.jpg")[:10]
    for f in files:
        analyze_image(f)
