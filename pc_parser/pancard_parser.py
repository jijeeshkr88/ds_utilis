import cv2
import Image
import pytesseract
import numpy as np


def image_preprocessing(img_path):
	img_rgb = cv2.imread(img_path)
	im_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
	# ret,img_bw = cv2.threshold(im_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	img_bw = np.uint8((im_gray<110)*255)
	kernel = np.ones((1,1),np.uint8)
	opening = cv2.morphologyEx(img_bw, cv2.MORPH_OPEN, kernel)
	# return np.uint8(255-img_bw)
	return opening

def img2text(img_bw):
	text = pytesseract.image_to_string(Image.fromarray(img_bw))
	data = text.split("\n")
	return data

if __name__ == '__main__':
	file_name = "./data/image01.jpg"
	bw_img = image_preprocessing(file_name)
	print(img2text(bw_img))
	



