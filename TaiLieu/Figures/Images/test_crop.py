import cv2
import numpy as np

def analyze_image(path):
    img = cv2.imread(path)
    if img is None:
        print(f"Could not read {path}")
        return
    
    h, w, c = img.shape
    print(f"Image {path}: {w}x{h}")
    
    # Let's find horizontal lines or blue-green pixels
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define a range for blue-green (cyan/teal)
    # OpenCV hue is 0-179. Cyan is around 90.
    lower_teal = np.array([80, 50, 50])
    upper_teal = np.array([100, 255, 255])
    
    mask = cv2.inRange(hsv, lower_teal, upper_teal)
    
    # Find row coordinates where teal pixels exist
    teal_rows = np.where(np.any(mask > 0, axis=1))[0]
    if len(teal_rows) > 0:
        print(f"Teal pixels found at rows spanning from {teal_rows[0]} to {teal_rows[-1]}")
        # Look for horizontal lines (many teal pixels in a row)
        row_counts = np.sum(mask > 0, axis=1)
        line_rows = np.where(row_counts > w * 0.3)[0] # at least 30% of width
        if len(line_rows) > 0:
            print(f"Teal horizontal lines detected at rows: {line_rows}")
        else:
            print("No long teal horizontal lines detected.")
    else:
        print("No teal pixels found.")

if __name__ == "__main__":
    analyze_image("figure_2.2.jpg")
