# Building Detection from Satellite Images

This project allows you to detect buildings from satellite images using YOLOv8 (You Only Look Once) object detection. Follow the instructions below to run the code successfully.

## Dependencies

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- tkinter library
- PIL (Python Imaging Library)
- ultralytics library
- shutil library

You can install the required libraries using pip:
```
pip install tkinter
pip install pillow
pip install ultralytics
```

## How to Run Inference from One Model

1. Download the entire project files to your local machine.

2. Open the terminal or command prompt and navigate to the project folder.

3. Run the application by executing the following command:

```
python yolov8.py
```

4. The GUI window will open, showing the "Upload satellite image" button.

5. Click on the "Choose file" button to upload a satellite image (in PNG or JPG format) from your local machine.

6. Once the image is uploaded, you will see the "Original image" on the left side of the window.

7. Click the start button (play icon) to initiate the building detection process using YOLO. The application will use the model from `best-v13andv16.pt` to detect buildings in the uploaded image.

8. After the detection process is complete, the "Image after detection" will be displayed on the right side of the window, showing the original image with bounding boxes around detected buildings.

9. The number of detected buildings will be shown below the image as "Number of buildings: X," where X is the count of detected buildings.

10. The application will automatically delete the intermediate files generated during the detection process.


## How to Run Inference from Two Models

1. Download the entire project files to your local machine.

2. Open the terminal or command prompt and navigate to the project folder.

3. Run the application by executing the following command:

```
python yolov8twoModels.py
```

4. The GUI window will open, showing the "Upload satellite image" button.

5. Click on the "Choose file" button to upload a satellite image (in PNG or JPG format) from your local machine.

6. Once the image is uploaded, you will see the "Original image" on the left side of the window.

7. Click the start button (play icon) to initiate the building detection process using YOLOv8. The application will use two different models for detection:

   - Model v13v16: Detects buildings using the 'best-v13andv16.pt' model.
   - Model v13v16v21: Detects buildings using the 'best-v13v16v21.pt' model.

8. After the detection process is complete, the "Image after detection v13v16" and "Image after detection v13v16v21" will be displayed on the right side of the window, showing the original image with bounding boxes around detected buildings.

9. The number of detected buildings for each model will be shown below the respective images as "Number of buildings v13v16: X" and "Number of buildings v13v16v21: Y," where X and Y are the counts of detected buildings for each model.

10. The application will automatically delete the intermediate files generated during the detection process.

That's it! You have successfully run the building detection application from satellite images using YOLOv8. Feel free to upload more images and experiment with the detections.

Note: Ensure you have a working internet connection during the initial run of the application as it may need to download the YOLO model for the first time. Subsequent runs will use the locally cached model.
