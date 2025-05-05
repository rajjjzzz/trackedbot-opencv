import numpy as np
import cv2

def suggest_path(mask):
    """
    Suggests path as the most open vertical slice in the lower part of the frame.
    """
    h, w = mask.shape
    roi = mask[h//2:, :]  # focus only on bottom half of frame
    slice_width = w // 20

    max_clear = 0
    best_col = w // 2

    for i in range(0, w, slice_width):
        slice_area = roi[:, i:i+slice_width]
        white_px = np.sum(slice_area == 255)
        if white_px > max_clear:
            max_clear = white_px
            best_col = i + slice_width // 2

    # Return point at bottom-center of best path
    return (best_col, h - 1)
