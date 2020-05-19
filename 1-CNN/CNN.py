import skimage.data
import numpy as np
import cv2
import sys

img = skimage.data.chelsea()

img = skimage.color.rgb2gray(img)

l1_filter = np.zeros((2, 3, 3))
l1_filter[0, :, :] = np.array([[[-1, 0, 1],
								[-1, 0, 1],
								[-1, 0, 1]]])

l1_filter[1, :, :] = np.array([[[1, 1, 1],
								[0, 0, 0],
								[-1, -1, -1]]])


def conv_(img, filter): 
	filter_size = filter.shape[0]
	result = np.zeros((img.shape))
	x = np.uint16(filter_size/2)
	#Looping through the image to apply the convolution operation.
	for r in np.arange(0, img.shape[0]-x-2):
		for c in np.arange(0, img.shape[1]-x-2):
			curr_region = img[r:r+filter_size, c:c+filter_size]
			curr_result = curr_region * filter
			result[r, c] = np.sum(curr_result)

	final_result = result[x:result.shape[0]-x, x:result.shape[1]-x]
	return final_result


def conv(img, conv_filter):
	if len(img.shape) > 2 or len(conv_filter.shape) > 3:
		if img.shape[-1] != conv_filter.shape[-1]:
			print("Error: Number of channels of image and filter must match")
			sys.exit()
	if conv_filter.shape[1] != conv_filter.shape[2]: # Check if filter dimensions are equal.  
		print('Error: Filter must be a square matrix. I.e. number of rows and columns must match.')
		sys.exit()
	if conv_filter.shape[1] % 2 == 0:
		print('Error: Filter must have an odd size. I.e. number of rows and columns must be odd.')
		sys.exit()

	feature_maps = np.zeros((img.shape[0] - conv_filter.shape[1] + 1,
							img.shape[1] - conv_filter.shape[2] + 1,
							conv_filter.shape[0]))

	for filter_num in range(conv_filter.shape[0]):
		print("Filter", filter_num + 1)
		curr_filter = conv_filter[filter_num]
		print(curr_filter)
		feature_maps[:, :, filter_num] = conv_(img, curr_filter)
	return feature_maps

def ReLU(feature_maps):
	relu_out = np.zeros((feature_maps.shape))
	for map_num in range (feature_maps.shape[-1]):
		for r in np.arange(0, feature_maps.shape[0]):
			for c in np.arange(0, feature_maps.shape[1]):
				relu_out[r, c, map_num] = np.max(feature_maps[r, c, map_num], 0)
	return relu_out

def pooling(feature_maps, size=2, stride=2):
	pool_out = np.zeros((np.uint16((feature_maps.shape[0]-size+1)/stride),
						np.uint16((feature_maps.shape[1]-size+1)/stride),
						feature_maps.shape[-1]))
	for map_num in range(feature_maps.shape[-1]):
		r_out = 0
		for r in np.arange(0, feature_maps.shape[0]-size-1, stride):
			c_out = 0
			for c in np.arange(0, feature_maps.shape[1]-size-1, stride):
				pool_out[r_out, c_out, map_num] = np.max(feature_maps[r:r+size, c:c+size])
				c_out = c_out + 1
			r_out = r_out + 1
	return pool_out


feature_maps = conv(img, l1_filter)
relu = ReLU(feature_maps)
pool_map = pooling(relu, 2, 2)

cv2.imshow("map 1", feature_maps[:, :, 0])
cv2.imshow("map 2", feature_maps[:, :, 1])


cv2.imshow("relu 1", relu[:, :, 0])
cv2.imshow("relu 2", relu[:, :, 1])

cv2.imshow("pool 1", pool_map[:, :, 0])
cv2.imshow("pool 2", pool_map[:, :, 1])
cv2.waitKey(0)