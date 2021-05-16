# Python programe to illustrate 
# arithmetic operation of 
# bitwise OR of two images 
	
# organizing imports 
import cv2 
import numpy as np
	
def mask(name):

	# path to input images are specified and 
	# images are loaded with imread command 
	nms = name.split("\\")
	curimgpath = nms[len(nms)-1]
	print(curimgpath)
	img1 = cv2.imread('./uploads/'+curimgpath) 
	print("IMG1\n")
	print(img1)

	nms2 = curimgpath.split("\\")
	destimgpath = nms2[len(nms2)-1].split(".")[0] + "." + nms2[len(nms2)-1].split(".")[1]+ ".png"

	print('PATH\n')
	print(destimgpath)
	
	img2 = cv2.imread('./test_data/u2net_results/'+ destimgpath) 

	print("IMG2\n")
	print(img2)

	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)	

	transparent = img1.copy()
	transparent = cv2.cvtColor(transparent, cv2.COLOR_BGR2BGRA)
	transparent[:, :, 3] = img2

	cv2.imwrite('./test_data/masked_images/'+nms[len(nms)-1]+'.png', transparent)

	# De-allocate any associated memory usage 
	if cv2.waitKey(0) & 0xff == 27: 
		cv2.destroyAllWindows() 
