import cv2
import skimage.data
import numpy as np 

img = skimage.data.chelsea()
img = skimage.color.rgb2gray(img)

#fliters
l1_filter = np.zeros((2, 3, 3))
l1_filter[0, :, :] = np.array([[[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]])
l1_filter[1, :, :] = np.array([[[1, 1, 1],[0, 0, 0],[-1, -1, -1]]])


def conv_(img, conv_filter):
	filter_size = conv_filter.shape[0]
	result = np.zeros((img.shape))
	#Lopping through the image ti apply the convolution
	for r in np.uint16(np.arange(filter_size/2, img.shape[0]-filter_size/2-2)):
		for c in np.uint16(np.arange(filter_size/2, img.shape[1]-filter_size/2-2)):
			#getting the current region to get multiplied with the filter
			curr_region = img[r:r+filter_size, c:c+filter_size]
			#Element-wise multiplication between the current region and the filter
			curr_result = curr_region * conv_filter
			conv_sum = np.sum(curr_result)
			result[r, c] = conv_sum
			#Get the final result
	final_result = result[np.uint16(filter_size/2):result.shape[0]-np.uint16(filter_size/2),
							np.uint16(filter_size/2):result.shape[1]-np.uint16(filter_size/2)]
	return final_result


#first convolution layer
def conv(img, conv_filter):
	if (len(img.shape) > 2 or len(conv_filter.shape) > 3) and img.shape[-1] != conv_filter.shape[-1]:
		print("Error: Number of channels in both image and filter must be same.")
		sys.exit()
	if conv_filter.shape[1] != conv_filter.shape[2]:
		print("Error: Filter must be a square martix.")
		sys.exit()
	if conv_filter.shape[1]%2 == 0:
		print("Error: Filter must have odd size")
		sys.exit()
	#Create an empty feature map
	feature_maps = np.zeros((img.shape[0]-conv_filter.shape[1]+1,
							img.shape[1]-conv_filter.shape[1]+1,
							conv_filter.shape[0]))
	for filter_num in range(conv_filter.shape[0]):
		print("Filter", filter_num+1)
		curr_filter = conv_filter[filter_num, :]
		#rgb image
		if len(curr_filter.shape) > 2:
			conv_map = conv_(img[:, :, 0], curr_filter[:, :, 0])
			for ch_num in range(1, curr_filter.shape[-1]):
			 	conv_map = conv_map + conv_(img[:, :, ch_num],   
                                 curr_filter[:, :, ch_num])
		#gray image
		else: 
			conv_map = conv_(img, curr_filter)
		feature_maps[:, :, filter_num] = conv_map
	return feature_maps

l1_feature_maps = conv(img, l1_filter)
cv2.imshow('L1-1', l1_feature_maps[:, :, 0])
cv2.imshow('L1-2', l1_feature_maps[:, :, 1])
cv2.waitKey(0)