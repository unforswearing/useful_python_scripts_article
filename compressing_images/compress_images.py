from PIL import Image
file_path =  "image_uncompressed.jpg"
img = PIL.Image.open(file_path)
height, width = img.size
img.resize((height, width), Image.ANTIALIAS)
compressed = img.resize((height, width), Image.ANTIALIAS)
compressed.save("image_compressed.jpg", optimize=True,quality=9)