import gradio as gr
import tensorflow as tf 
import numpy as np
import requests
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model
import torch

model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)

#model = load_model("model.h5")

#function
def example(image):
    image = image.reshape((-1, 224, 224, 3)),
    prediction = model.predict(image).flatten(),
    return {class_names[i]: float(prediction[i]) for i in range(4)}
    
class_names = ['the number of categories in which the model classifies','a','b']

# initializing the input component
image = gr.inputs.Image(shape = (224, 224)) 
# initializing the output component 
label = gr.outputs.Label(num_top_classes = 4)

# launching the interface
gr.Interface(fn = example,inputs = image,outputs = label,capture_session = True, title="Deep N Dense - Empty Problem",description= "").launch(share=True)