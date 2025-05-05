import cv2

def draw_suggested_path(frame, point):
    """
    Draws a green line from bottom center to suggested path point.
    """
    h, w, _ = frame.shape
    bottom_center = (w // 2, h - 10)
    cv2.arrowedLine(frame, bottom_center, point, (0, 255, 0), 4, tipLength=0.3)
    return frame
