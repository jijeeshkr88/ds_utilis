import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.ion()



def img_transformation(src_corners,out_corners,image):
	quad_mat, mask = cv2.findHomography(src_corners, out_corners)
	output_ = cv2.warpPerspective(image, quad_mat, (1500,800))
	return output_


#creating test image
def create_test_image(c1,c2):
	mask = np.zeros((500,600, 3), np.uint8)
	cv2.rectangle(mask, c1, c2, (255,0,0), -1)
	return mask



if __name__ == '__main__':
	src_corners = np.float32([[141,276], [503,276], [503,417],[141,417]])
	out_corners = np.float32([[955,198], [1071,506], [847,504], [717,281]])
	x1 = min(src_corners[:,0])
	x2 = max(src_corners[:,0])
	y1 = min(src_corners[:,1])
	y2 = max(src_corners[:,1])
	image_ = create_test_image((x1,y1),(x2,y2))
	img_t = img_transformation(src_corners,out_corners,image_)
	plt.imshow(img_t)



	


