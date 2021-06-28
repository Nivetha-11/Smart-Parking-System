# Smart-Parking-System---Object-Detection-Technique-
Developed a Smart Parking System using MASK-RCNN Object Detection mechanism. GUI - Python and Flask.

#Project Description: 

This project aims to present an Artificial Intelligent system for detecting parking space based on the object detection technique. 
We used transfer learning and trained the Mask-RCNN model to detect occupied/empty parking slots.In this experiment Mask-RCNN, 
object detection & segmentation model is implemented on each input frame of the video to obtain the detection results of cars and
bounding boxes. The bounding boxes obtained from the Mask-RCNN model were used to compute IOU (Intersection Over Union) by comparing
bounding boxes with parking spot coordinates. If the computed IOU value for a particular parking spot is greater than the certain 
threshold value, then we consider the parking slot to be occupied. An automatic car parking system can be used to make the whole process
of parking cars more efficient and less complex for drivers.


#Dataset Details: 

Task Type: Object Detection
Database Link: https://web.inf.ufpr.br/vri/databases/parking-lot-database/ 
Training dataset: 833 images
Validation dataset: 136 images
Test dataset: 136 images
The dataset is divided into 70% for training, 15% for testing and 15% for training.

#Project Detail along with the python files and GUI:

https://drive.google.com/drive/folders/1KdG9O26TL9mW0G3MStq5d4F_qjENdBxH?usp=sharing
