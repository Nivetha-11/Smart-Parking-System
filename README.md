# Smart-Parking-System using Object-Detection-Technique
Developed a Smart Parking System using MASK-RCNN Object Detection mechanism. GUI - Python and Flask.

# Project Description: 

This project aims to present an Artificial Intelligent system for detecting parking space based on the object detection technique. 
We used transfer learning and trained the Mask-RCNN model to detect occupied/empty parking slots.In this experiment Mask-RCNN, 
object detection & segmentation model is implemented on each input frame of the video to obtain the detection results of cars and
bounding boxes. The bounding boxes obtained from the Mask-RCNN model were used to compute IOU (Intersection Over Union) by comparing
bounding boxes with parking spot coordinates. If the computed IOU value for a particular parking spot is greater than the certain 
threshold value, then we consider the parking slot to be occupied. An automatic car parking system can be used to make the whole process
of parking cars more efficient and less complex for drivers.


# Dataset Details: 

Task Type: Object Detection
Database Link: https://web.inf.ufpr.br/vri/databases/parking-lot-database/ 
1) Training dataset: 833 images
2) Validation dataset: 136 images
3) Test dataset: 136 images
4) The dataset is divided into 70% for training, 15% for testing and 15% for training.


# Sample Input images
<img width="607" alt="Screen Shot 2021-06-28 at 8 47 15 pm" src="https://user-images.githubusercontent.com/57209945/123624552-08b61280-d852-11eb-8534-d92622b3d9cf.png">


# Project Detail along with the python files and GUI:

https://drive.google.com/drive/folders/1KdG9O26TL9mW0G3MStq5d4F_qjENdBxH?usp=sharing


# Basic Workflow Diagram 


<img width="489" alt="Screen Shot 2021-06-28 at 8 48 36 pm" src="https://user-images.githubusercontent.com/57209945/123624693-37cc8400-d852-11eb-88ed-2dffb241ca55.png">

# Experimental Results

<img width="488" alt="Screen Shot 2021-06-28 at 8 51 21 pm" src="https://user-images.githubusercontent.com/57209945/123624984-998cee00-d852-11eb-98a8-a0823091553a.png">


# Sample Images with Predicted Results

<img width="463" alt="Screen Shot 2021-06-28 at 8 50 01 pm" src="https://user-images.githubusercontent.com/57209945/123624826-6a767c80-d852-11eb-9cbc-e8705eda0038.png">




