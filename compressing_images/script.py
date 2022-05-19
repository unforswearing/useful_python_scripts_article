import PIL
from PIL import Image
file_path =  "uncompressed.jpg"
img = PIL.Image.open(file_path)
img=img.resize(400,600),PIL.Image.ANTI
img.save("compressed.jpg")
