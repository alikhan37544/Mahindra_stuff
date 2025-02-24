# webcam_split_detection.py
import sys
import os

# Ensure project root is accessible
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import cv2
from common.object_detection import ObjectDetector
from common.video_utils import open_camera, split_frame, close_windows

def split_webcam_detection():
    """
    Perform object detection on a split webcam feed (2x5 grid).
    Press 'q' to quit.
    """
    cap = open_camera()
    detector = ObjectDetector()  # Initialize the object detection model

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to retrieve frame from webcam.")
                break

            # Split the frame into 2x5 grid (10 parts)
            parts = split_frame(frame, 2, 5)

            # Detect objects in each part and display them
            for idx, part in enumerate(parts):
                results = detector.detect_objects(part)
                annotated_part = detector.annotate_frame(part, results)
                cv2.imshow(f"Part {idx + 1}", annotated_part)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        close_windows()

if __name__ == "__main__":
    split_webcam_detection()
