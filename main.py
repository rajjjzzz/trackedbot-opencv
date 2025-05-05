import time
import cv2

from input_layer.camera import get_camera_feed
from processing_layer.segmentation import detect_traversable_region
from processing_layer.path_suggestion import suggest_path
from output_layer.overlay import draw_suggested_path

def main():
    cap = get_camera_feed()
    last_processed = time.time()
    latest_point = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()
        if current_time - last_processed >= 1:  # process 1 frame/sec
            mask = detect_traversable_region(frame)
            latest_point = suggest_path(mask)
            last_processed = current_time

        if latest_point:
            frame = draw_suggested_path(frame, latest_point)

        cv2.imshow("Tracked Bot - First Person Path", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
