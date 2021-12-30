from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from mrcnn.visualize import display_instances
import os
os.chdir("./")
import mrcnn.config
import mrcnn.utils
from mrcnn.model import MaskRCNN

class PredictionConfig(mrcnn.config.Config):
    NAME = 'parking_cfg'
    NUM_CLASSES = 1+2
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

def draw_image_with_boxes(filename, boxes_list, class_list):
	plt.switch_backend('Agg')

	occupied = 0
	empty = 0

	data = plt.imread(filename)
	plt.figure(figsize=(20,14))
	plt.imshow(data)

	ax = plt.gca()

	for box, cls in zip(boxes_list, class_list):
		y1, x1, y2, x2 = box
		width, height = x2 - x1, y2 - y1

		if cls==1:
			rect = mpatches.Rectangle((x1,y1),width,height,fill=False,linewidth=5, color='red')
			occupied = occupied + 1
		elif cls==2:
			rect = mpatches.Rectangle((x1,y1),width,height,fill=False,linewidth=5, color='green')
			empty = empty +1
		ax.add_patch(rect)

	plt.savefig('../web app implemenation/static/images/predict.png', bbox_inches='tight')
	plt.close() 
	return occupied, empty

def predict():
	config = PredictionConfig()
	model_predict = MaskRCNN(mode="inference", model_dir='../web app implemenation/logs/parking_cfg20200617T0142/mask_rcnn_parking_cfg_0005.h5', config=config)
	model_predict.load_weights('../web app implemenation/logs/parking_cfg20200617T0142/mask_rcnn_parking_cfg_0005.h5',by_name= True)
	return model_predict