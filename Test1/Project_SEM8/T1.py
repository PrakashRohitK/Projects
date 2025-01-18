import pygal
from pygal_maps_world.maps import World  # Import World from pygal_maps_world.maps

# Create a world map chart object
world_map = World()
world_map.title = 'Continental Representation'

# Adding continents
world_map.add('Asia', [('asia', 1)])
world_map.add('Europe', [('europe', 1)])
world_map.add('Africa', [('africa', 1)])
world_map.add('North America', [('north_america', 1)])
world_map.add('South America', [('south_america', 1)])
world_map.add('Oceania', [('oceania', 1)])
world_map.add('Antarctica', [('antarctica', 1)])

# Render to file
world_map.render_to_file('world_map.png')
import cv2

# Load the image
image = cv2.imread('C:\\Users\\kpbrb\\PycharmProjects\\Test1\\Project_SEM8\\world_map.png')  # Replace with your image path

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Display the image in a window
    cv2.imshow('Image', image)

    # Wait for a key press and close the image window
    cv2.waitKey(0)  # 0 means wait indefinitely
    cv2.destroyAllWindows()  # Close all OpenCV windows

