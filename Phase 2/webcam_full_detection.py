# webcam_full_detection.py
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import cv2
from common.object_detection import ObjectDetector
from common.video_utils import open_camera, close_windows

def webcam_full_detection():
    """
    Perform object detection on the full webcam feed.
    Press 'q' to quit.
    """
    cap = open_camera()
    detector = ObjectDetector()  # Initialize the object detection model

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame from camera.")
                break

            # Detect objects on the full frame
            results = detector.detect_objects(frame)
            annotated_frame = detector.annotate_frame(frame, results)

            # Display the annotated frame
            cv2.imshow("Full Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        close_windows()

if __name__ == "__main__":
    webcam_full_detection()
