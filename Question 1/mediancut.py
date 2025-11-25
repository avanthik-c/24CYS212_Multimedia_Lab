from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt

og_img=imread('girl.jpg')

#bucket means a certain range of points grouped together
def split_bucket(img,img_arr,depth):
    if len(img_arr)==0:
        return
    if depth==0:
        quantize(img,img_arr)#assign the mean value to the bucket send,here img_arr is the bucket
        return
    r_len=np.max(img_arr[:,0])-np.min(img_arr[:,0])
    g_len=np.max(img_arr[:,1])-np.min(img_arr[:,1])
    b_len=np.max(img_arr[:,2])-np.min(img_arr[:,2])
    idx=0
    if r_len>=g_len & r_len>=b_len:
        idx=0
    elif g_len>=r_len & g_len>=b_len:
        idx=1
    elif b_len>=g_len & b_len>=r_len:
        idx=2
    img_arr=img_arr[img_arr[:,idx].argsort()]
    median_idx=len(img_arr)//2
    print("median= ",median_idx)
    split_bucket(img,img_arr[0:median_idx],depth-1)
    split_bucket(img,img_arr[median_idx:],depth-1) 

#assign the values to the pixel
def quantize(img,img_arr):
    r_mean=np.mean(img_arr[:,0])
    g_mean=np.mean(img_arr[:,1])
    b_mean=np.mean(img_arr[:,2])
    for data in img_arr:
        og_img[data[3],data[4]]=[r_mean,g_mean,b_mean]


# og_img is 3d array[row][col][channels color]
img_array=[]
for ridx,rows in enumerate(og_img):
    for cidx,colour in enumerate(rows):
        img_array.append([colour[0],colour[1],colour[2],ridx,cidx])
img_arr=np.array(img_array)

#level corresponds to 2^level colours
level=5

split_bucket(og_img,img_arr,level)
plt.imshow(og_img) 
plt.axis('off') 
plt.show()