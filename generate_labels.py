import cv2
import tkinter as tk
from tkinter import simpledialog
import os

# Function to get the label from the user
def get_label(image_name):
    root = tk.Tk()
    root.withdraw()
    label = simpledialog.askstring("Label", f"Enter a label for {image_name}:", parent=root)
    return label

# Path to the directory containing your images
image_dir = "imgs"
output_file = "labels.txt"

# Get a list of image file names in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Open the output file for writing
with open(output_file, "w") as file:
    for image_name in image_files:
        # Display the image
        image_path = os.path.join(image_dir, image_name)
        image = cv2.imread(image_path)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Get the label from the user
        label = get_label(image_name)

        # Write the image name and label to the output file
        file.write(f"{image_name},{label}\n")

print("Labeling complete. Labels saved to", output_file)
