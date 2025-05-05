import cv2

def get_camera_feed():
    cap = cv2.VideoCapture(0)  # or video file path
    if not cap.isOpened():
        raise RuntimeError("Failed to open camera")
    return cap
