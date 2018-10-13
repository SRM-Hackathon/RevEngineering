import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf 
from keras.models import model_from_json
import cv2
import matplotlib.pyplot as plt
import numpy as np

with open('D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/model.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/weights.h5')

face_cascade=cv2.CascadeClassifier('D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/webcam/haarcascade_frontalface_default.xml')
def detect(url):
	p = cv2.imread(url,1)
	f= 0
	gray=cv2.cvtColor(p,cv2.COLOR_BGR2GRAY)
	print(gray)
	faces=face_cascade.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
	    f=1
	    cv2.rectangle(p,(x,y),(x+w,y+h),(255,0,0),2)
	    image=p[y:y+h,x:x+w]
	    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	    #cv2.imshow('Press v to click',image)
	    image = cv2.resize(image,(200,200), interpolation = cv2.INTER_CUBIC)

	if f==1:
		print("with haarcascade_frontalface_default")
		image.resize(1,64,64,1)
		pr = model.predict(image)
	else:
		print("without haarcascade_frontalface_default")
		p.resize(1,64,64,1)
		pr = model.predict(p)

	# predict = pr[0]*10000000
	# for i in range(len(predict)):
	#     predict[i]=int(predict[i])


	# #graph
	# n_groups = len(predict)
	# index = np.arange(n_groups)
	# fig, ax = plt.subplots()
	# bar_width = 0.35
	# opacity = 0.4
	# error_config = {'ecolor': '0.3'}
	# rects1 = plt.bar(index, predict, bar_width,
	#                  alpha=opacity,
	#                  color='b',
	#                  error_kw=error_config,
	#                  label='Prediction')
	# plt.xlabel('Group')
	# plt.ylabel('Scores')
	# plt.title('Scores by group and gender')
	# plt.xticks(index + bar_width / 2, ('neutral', 'anger', 'surprise', 'happiness', 'disgust','fear','contempt','sadness'))
	# plt.legend()
	# plt.tight_layout()
	# # plt.show()
	# plt.savefig('graph.png')

	# seeing which is greater
	if pr[0][3]>0.5:
		return 1
	else:
		return 0

# detect("D:/Machine Learning/Dirty/RevEngineering/Django Frontend/frontend/media/webcam/webcam.png")