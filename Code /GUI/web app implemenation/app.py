import os
from train import draw_image_with_boxes, predict
from keras.preprocessing import image
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../web app implemenation/static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def option():
	return render_template('option.html')

@app.route('/main.html')
def main():
	return render_template('main.html')

@app.route('/result.html',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template("result.html",result = result)

@app.route('/loc1.html')
def loc1():
	return render_template('loc1.html')

@app.route('/loc2.html')
def loc2():
	return render_template('loc2.html')

@app.route('/loc3.html')
def loc3():
	return render_template('loc3.html')

@app.route('/main2.html')
def main2():
	return render_template('main2.html')

@app.route('/ImageResult.html',methods = ['POST', 'GET'])
def ImageResult():
	if request.method == 'POST':
		file = request.files['file']

		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

		upload = '../web app implemenation/static/images/' + filename
		img1 = image.load_img(upload)
		img1 = image.img_to_array(img1)

		model = predict()
		results = model.detect([img1])

		occupied, empty = draw_image_with_boxes(upload,results[0]['rois'],results[0]['class_ids'])

		return render_template("prediction.html", occupied=occupied, empty=empty)

if __name__ == '__main__':
	app.run(debug = True)