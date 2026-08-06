#Project - How to Deploy an Image Classification Model using Flask & Tensorflow:

import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

def get_classes(file_path):

    #Model load ho raha hai
    model = ResNet50(weights = "imagenet")

    #Image process karna
    img = image.load_img(file_path,target_size = (224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis= 0)
    x = preprocess_input(x)

    #Prediction

    preds = model.predict(x)
    predictions = decode_predictions(preds, top=3)[0]
    return predictions