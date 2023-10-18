import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from ultralytics import YOLO
import shutil

def frameAndLabel(text, width, height, frow, fcol, lrow, lcol, font):
    frame = Frame(master=window, relief="groove", borderwidth=5, width=width, height=height)
    frame.grid(row=frow,column=fcol, padx=(50,10))
    label = tk.Label(text=text, width=30, font=font, bg="#f4f6f3")
    label.grid(row=lrow, column=lcol)

def label(text, font, row, column):
    label = tk.Label(text=text, width=30, font=font, bg="#f4f6f3")
    label.grid(row=row, column=column, sticky="nsew", columnspan=3)

def showImage(img, savedFile, size, row, col):
    img=Image.open(img) 
    img.save(savedFile)
    img=img.resize((size,size))
    img=ImageTk.PhotoImage(img)
    imageLabel =tk.Label(master=window, image=img)
    imageLabel.image = img
    imageLabel.grid(row=row,column=col, padx=(50,10))

def uploadFile():
    f_types = [('PNG Files','*.png'), ('Jpg Files', '*.jpg')]   
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    showImage(filename, "oriImg.png", 350, 1, 0)
    showImage("blank.png", "blank.png", 350, 1, 2)
    buildingFrameLabel.config(text="0")

def detectBuildings():
    global buildingNo
    model = YOLO('best-v13andv16.pt')
    results = model(source="oriImg.png", save=True, conf=0.35, boxes=True)
    buildingNo = len(results[0].boxes)
    predImg = "runs/segment/predict/oriImg.png"
    showImage(predImg, "predImg.png", 350, 1, 2)
    # uploadButton['state'] = DISABLED
    buildingFrameLabel.config(text=f"{buildingNo}")
    shutil.rmtree("runs/segment/predict")

window = tk.Tk()
window.title("Building detection from satellite images")
window.geometry("1200x600")  # Size of the window 
window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)
window['background'] = "#f4f6f3"

buildingNo = 0
labelFont=('times', 16, 'bold')
captionFont=('times', 12, 'italic')

label("Upload satellite image", labelFont, 0, 0)
frameAndLabel("Original image", 450, 450, 1, 0, 2, 0, captionFont)

uploadButton = tk.Button(master=window, text="Choose file", command=uploadFile)
uploadButton.grid(row=0, column=1, columnspan=2)

startImg = Image.open("icon-start.png")
startImg = startImg.resize((80,80))
startImg = ImageTk.PhotoImage(startImg)
startLabel = tk.Label(image=startImg)
algoButton = tk.Button(master=window, image=startImg, borderwidth=0, command=detectBuildings)
algoButton.grid(row=1, column=1)
# algoButton['state'] = DISABLED

frameAndLabel("Image after detection", 450, 450, 1, 2, 2, 2, captionFont)
buildingNoLabel = tk.Label(text="Number of buildings: ", width=30, font=labelFont, bg="#f4f6f3")
buildingNoLabel.grid(row=3, column=1)

buildingNoFrame = Frame(master=window, relief="groove", borderwidth=5, width=100, height=100)
buildingFrameLabel = tk.Label(master=buildingNoFrame, text="0")
buildingFrameLabel.pack()
buildingNoFrame.grid(row=4, column=1)

window.mainloop()
