import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from tensorflow import keras


class DrawingInterface:
    def __init__(self):
        self.model = keras.models.load_model('models/handwritten5.keras')
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=280, height=280, bg='white')
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.draw)
        self.button_predict = tk.Button(self.root, text='Predict', command=self.predict)
        self.button_predict.pack(side='left')
        self.button_clear = tk.Button(self.root, text='Clear', command=self.clear)
        self.button_clear.pack(side='right')
        self.label_prediction = tk.Label(self.root, text="Predicted: ")
        self.label_prediction.pack()
        self.image = Image.new("L", (280, 280), 'white')
        self.draw = ImageDraw.Draw(self.image)
        
    def draw(self, event):
        x, y = event.x, event.y
        r = 10
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill="black")

    
    def predict(self):
        
        image = self.image.convert('L')
        image = image.resize((28,28))
        
        pixels = np.array(image)
        pixels = np.invert(pixels)
        pixels = pixels.reshape((1,28,28,1)).astype('float32') / 255
        
        prediction = self.model.predict(pixels)[0]
        digit = np.argmax(prediction)
        confidence = round(prediction[digit] * 100, 2)
        
        self.showprediction(digit)
        #print(f"Prediction: {digit}")
        #print(f"Confidence: {confidence}")
        
    def clear(self):
        self.canvas.delete('all')
        self.image = Image.new("L", (280,280), 'white')
        self.draw = ImageDraw.Draw(self.image)
    
    def showprediction(self, prediction):
        self.label_prediction.config(text=f"Predicted: {prediction}")

