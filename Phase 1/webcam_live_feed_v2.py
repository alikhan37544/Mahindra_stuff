import cv2

def main():
    """
    Opens the default webcam and displays the live feed.
    Press 'q' to quit the feed.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        print("Webcam feed is active.")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to retrieve frame from webcam.")
                break

            cv2.putText(frame, 'Webcam Feed Active', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow('Webcam Feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()