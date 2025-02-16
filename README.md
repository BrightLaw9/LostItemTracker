# LostItemTracker
A Computer Vision Equipped Robot that finds your lost items

- Images were web scraped using BeautifulSoup (bs4) - classes scraped include backpacks, travel baggage, phones, water bottles, wallets, purses, and other commonly forgotten items
- Used Roboflow to annotate (label) the images with the appropriate class and bounding boxes
- Dataset was ~200 images
![image](https://github.com/user-attachments/assets/e2e234f0-6937-4b4e-98d8-f72cec9a62e0)
- Trained on a YOLO11 model for 70 epoches (precision-recall curves, loss curves, and validation/test results shown below)
- Exported model as tflite and ran real-time inference on video scanning for lost items
 
