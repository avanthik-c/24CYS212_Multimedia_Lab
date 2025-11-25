import numpy as np
from PIL import Image

#frequency sampling
img=Image.open("girl.jpg")

grey = img.convert("L")            
grey = np.array(grey)               
row,col=grey.shape

F=np.fft.fft2(grey)
F_shift = np.fft.fftshift(F)

crow,ccol=row//2,col//2
x=np.arange(row)-crow
y=np.arange(col)-ccol
Y,X=np.meshgrid(y,x)
D=np.sqrt(X**2+Y**2)

print("Rows= ",row)
print("cols= ",col)

max_freq=np.sqrt(row**2+col**2)
print("Max freq= ",max_freq)

#enter the ratio you want to sample at
ratio=1/16
cutoff=max_freq*ratio
mask = (D <= cutoff).astype(float)
F_filtered=F_shift*mask

F_ishift=np.fft.ifftshift(F_filtered)
res_img=np.fft.ifft2(F_ishift)
res_img=np.abs(res_img)
res_img = res_img.astype(np.uint8)
final = Image.fromarray(res_img)
final.show()

#******************************************#
#spatial sampling
#can do both axis if factor has sq root

a=2
# a is sq root of the factor by which we need to downsample
#if factor = 1/4  => a=2

og_img = Image.open('girl.jpg')
og_img=np.array(og_img)

# hor_img = og_img[:, ::2, :]
# vert_img = og_img[::2, :, :]

both_img = og_img[::a, ::a, :]

final=Image.fromarray(og_img)
final.show("original")
Image.fromarray(both_img).show("1/4 spatial")
# final1=Image.fromarray(hor_img)
# final1.show("horizontal")
# final2=Image.fromarray(vert_img)
# final2.show("vertical")


