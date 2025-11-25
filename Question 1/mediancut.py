from PIL import Image

img = Image.open("girl.jpg").convert("RGB")
q = img.quantize(colors=16, method=Image.MEDIANCUT)
q = q.convert("RGB")
q.show("output_median_cut.jpg")
