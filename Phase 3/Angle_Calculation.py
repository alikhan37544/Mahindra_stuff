import numpy as np

def calculate_angle(front_point, rear_point):
    """
    Calculate the angle of the car's orientation based on the front and rear points.
    
    Args:
        front_point (tuple): (x, y) coordinates of the front of the car.
        rear_point (tuple): (x, y) coordinates of the rear of the car.
    
    Returns:
        float: The angle in degrees.
    
    Raises:
        ValueError: If the points are not tuples or do not contain exactly two elements.
    """
    if not (isinstance(front_point, tuple) and isinstance(rear_point, tuple)):
        raise ValueError("Both front_point and rear_point must be tuples.")
    if not (len(front_point) == 2 and len(rear_point) == 2):
        raise ValueError("Both front_point and rear_point must contain exactly two elements.")

    delta_x = front_point[0] - rear_point[0]
    delta_y = front_point[1] - rear_point[1]
    
    # Calculate the angle in radians and convert to degrees
    angle = np.arctan2(delta_y, delta_x) * (180.0 / np.pi)
    
    return angle

# Example usage
if __name__ == "__main__":
    front = (10, 20)
    rear = (5, 5)
    angle = calculate_angle(front, rear)
    print(f"The angle of the car's orientation is {angle:.2f} degrees.")
