import pyrebase
from src.pre_process import preProcess
import numpy as np
import tensorflow as tf
import os

def modelImageFetch(imageName, modelName, firstNum, secondNum):
    firebaseConfig = {
  "apiKey": "AIzaSyB87_k14Yeq5nLKEIYxWINagM4NpnAEDq4",
  "authDomain": "elearning-1368a.firebaseapp.com",
  "projectId": "elearning-1368a",
  "storageBucket": "elearning-1368a.appspot.com",
  "messagingSenderId": "77861376796",
  "appId": "1:77861376796:web:b2169efffe48e15db560d9",
  "measurementId": "G-CG8JPTMHC2",
  "databaseURL":"",
    }
    #Firebase initialization
    firebase = pyrebase.initialize_app(firebaseConfig)
    firebase = firebase.storage()

    #Model fetch
    modelPath = f"./data/models/cnn.h5"
    #firebase.child(f"models/{modelName}").download("",modelPath)

    #Fetching of the image to be tested
    imgPath = f"./data/testingImages/{imageName}"
    firebase.child(f"testing/{imageName}").put(f'data/testingImages/{imageName}')
    processedImage = preProcess(imgPath, firstNum, secondNum)
    print(processedImage)
    #Fetching the modal
    loaded_model = tf.keras.models.load_model(modelPath)
    prediction = loaded_model.predict(processedImage)
    classes_x = np.argmax(prediction, axis=1)

    #Remove the downloaded file to prevent server overload on future loads
    #os.remove(modelPath)
    #os.remove(imgPath)

    return classes_x