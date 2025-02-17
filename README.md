# LostItemTracker
A Computer Vision Equipped Robot that finds your lost items

- Images were web scraped using BeautifulSoup (bs4) - classes scraped include backpacks, travel baggage, phones, water bottles, wallets, purses, and other commonly forgotten items
- Used Roboflow to annotate (label) the images with the appropriate class and bounding boxes
- Dataset was ~200 images
![image](https://github.com/user-attachments/assets/e2e234f0-6937-4b4e-98d8-f72cec9a62e0)
- Trained on a YOLO11 model for 70 epoches (precision-recall curves, loss curves, and validation/test results shown below)
- Exported model as tflite and ran real-time inference on video scanning for lost items

# To run this project
Clone the repository
<br /><br />
Install dependencies: 
```
pip install -r requirements.txt
```
Run the inference script (provided that you want to use the default camera on your computer to stream inputs): 
```
python run_yolo_detect.py --model best.pt --source cam
```
USB camera option is available as well (source should be usb{index of usb camera})
For example:
```
python run_yolo_detect.py --model best.pt --source usb0
```
Video / images files can be inputted: 
```
python run_yolo_detect.py --model best.pt --source {your_image_name}.jpg
```
Support for PiCamera in script - need testing
Press P for picture, Q to quit

# Training Curves and Validation Predictions
![val_batch1_pred](https://github.com/user-attachments/assets/fad043eb-1b4e-4baa-8bda-5f5f13993e86)
![PR_curve](https://github.com/user-attachments/assets/d481ee73-b48b-48ba-9521-fc44090e5c43)
![confusion_matrix](https://github.com/user-attachments/assets/20b0cdec-bd69-41dd-89a2-86df8743ff54)
![results](https://github.com/user-attachments/assets/ef5de9d0-c28d-4162-b81e-bacdc38aa191)
