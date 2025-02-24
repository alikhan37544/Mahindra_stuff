import cv2
import numpy as np

class SpeedTracker:
    def __init__(self):
        self.prev_positions = {}  # Stores previous positions of cars

    def calculate_speed(self, car_id, current_position, fps, conversion_factor):
        """
        Calculate the speed of the car between frames.
        
        Args:
            car_id (int): Unique identifier for each detected car.
            current_position (tuple): Current (x, y) position of the car.
            fps (float): Frames per second of the camera feed.
            conversion_factor (float): Conversion from pixels to real-world units (e.g., meters).
        
        Returns:
            float: Speed of the car in real-world units per second.
        
        Raises:
            ValueError: If current_position is not a tuple or does not contain exactly two elements.
        """
        if not isinstance(current_position, tuple) or len(current_position) != 2:
            raise ValueError("current_position must be a tuple with exactly two elements.")
        
        if car_id in self.prev_positions:
            prev_position = self.prev_positions[car_id]
            # Calculate pixel distance between current and previous positions
            pixel_distance = np.linalg.norm(np.array(current_position) - np.array(prev_position))
            
            # Speed in pixels per frame
            speed_in_pixels = pixel_distance / fps
            
            # Convert to real-world speed (e.g., meters/second)
            speed_in_mps = speed_in_pixels * conversion_factor
            
            # Update the previous position
            self.prev_positions[car_id] = current_position
            
            return speed_in_mps
        else:
            # Store the current position as the first position
            self.prev_positions[car_id] = current_position
            return 0  # No speed calculated for the first frame

# Example usage
if __name__ == "__main__":
    tracker = SpeedTracker()
    car_id = 1
    fps = 30.0
    conversion_factor = 0.05  # Example conversion factor from pixels to meters

    # Simulated positions of the car in consecutive frames
    positions = [(100, 200), (105, 210), (110, 220), (115, 230)]

    for pos in positions:
        speed = tracker.calculate_speed(car_id, pos, fps, conversion_factor)
        print(f"Car {car_id} speed: {speed:.2f} m/s")
