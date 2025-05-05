import cv2
import numpy as np

def detect_traversable_region(frame):
    """
    Detects dark/rocky terrain using color segmentation.
    Returns a binary mask where white = free space, black = obstacle.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for 'free space' — lighter ground
    lower = np.array([0, 0, 180])
    upper = np.array([179, 70, 255])
    mask = cv2.inRange(hsv, lower, upper)

    return mask
