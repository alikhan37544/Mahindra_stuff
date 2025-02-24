import cv2
import numpy as np

def open_camera(camera_index=0):
    """
    Opens the webcam feed for the given index.
    
    Args:
        camera_index (int): Index of the camera to open (default=0).
    
    Returns:
        cv2.VideoCapture: The open VideoCapture object.
    
    Raises:
        Exception: If the webcam could not be opened.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise Exception("Error: Could not open webcam.")
    return cap

def split_frame(frame, rows, cols):
    """
    Splits a frame into rows x cols parts.
    
    Args:
        frame (np.ndarray): The image frame to split.
        rows (int): Number of rows.
        cols (int): Number of columns.
    
    Returns:
        list: A list of equally split frames.
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive integers.")
    height, width, _ = frame.shape
    part_height = height // rows
    part_width = width // cols
    split_frames = []

    for i in range(rows):
        for j in range(cols):
            sub_frame = frame[
                i * part_height : (i + 1) * part_height,
                j * part_width : (j + 1) * part_width
            ]
            split_frames.append(sub_frame)

    return split_frames

def display_split_feed(parts, rows, cols, window_name="Split Feed"):
    """
    Displays the split feed in a grid layout.
    
    Args:
        parts (list): List of frames to display.
        rows (int): Number of grid rows.
        cols (int): Number of grid columns.
        window_name (str): Name of the display window.
    """
    if not parts:
        return
    if len(parts) < rows * cols:
        raise ValueError("Not enough frames to fill the specified grid.")

    # Ensure consistent size across parts
    first_height, first_width = parts[0].shape[:2]
    resized_parts = [cv2.resize(part, (first_width, first_height)) for part in parts]

    # Build row-wise
    row_frames = [
        np.hstack(resized_parts[i * cols : (i + 1) * cols]) for i in range(rows)
    ]
    grid_feed = np.vstack(row_frames)
    cv2.imshow(window_name, grid_feed)

def close_windows():
    """
    Closes all OpenCV windows.
    """
    cv2.destroyAllWindows()