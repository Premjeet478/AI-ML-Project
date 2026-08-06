import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
import face_recognition
from IPython.display import Image




# 1. Load Images & Encodings
def load_images(known_images_dir):
    known_encodings = []
    known_images = []

    for file in os.listdir(known_images_dir):
        filename = os.fsdecode(file)
        image = face_recognition.load_image_file(os.path.join(known_images_dir, filename))

        enc = face_recognition.face_encodings(image)
        if len(enc) > 0:
            known_encodings.append(enc[0])
            known_images.append(filename)

    return (known_encodings, known_images)

# 2. Find Closest Match
def calculate_face_distance(known_encodings, unknown_img_path, cutoff=0.5, num_results=4):
    image_to_test = face_recognition.load_image_file(unknown_img_path)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
    return (unknown_img_path, known_images[face_distances.argmin()])

# 3. Execution & Paths (Apne local path se replace karein)
known_dir = "C:/AIML/AI-ML-Project/Face_Recognization/images"
original_image = "C:/AIML/AI-ML-Project/Face_Recognization/myimage.jpg"

known_encodings, known_images = load_images(known_dir)
matching_image = calculate_face_distance(known_encodings, original_image)[1]

# 4. Display Result
img_1 = mpimg.imread(original_image)
img_2 = mpimg.imread(os.path.join(known_dir, matching_image))

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img_1)
ax[0].set_title("Original")
ax[1].imshow(img_2)
ax[1].set_title("Match")
plt.show()

print('Hey, you look like ' + os.path.splitext(matching_image)[0] + '!')