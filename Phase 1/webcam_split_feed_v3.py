import cv2
import numpy as np

def split_frame(frame, rows, cols):
    """
    Splits the frame into rows x cols parts.
    """
    height, width, _ = frame.shape
    part_height = height // rows
    part_width = width // cols
    split_frames = []

    for i in range(rows):
        for j in range(cols):
            sub = frame[i*part_height:(i+1)*part_height, j*part_width:(j+1)*part_width]
            split_frames.append(sub)

    return split_frames

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to retrieve frame.")
                break

            parts = split_frame(frame, 2, 5)
            for idx, part in enumerate(parts):
                cv2.imshow(f'Part {idx + 1}', part)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()