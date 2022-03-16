from PIL import Image, ImageFilter
image = Image.open(r"city.png")
# requires input image to be of mode = Grayscale (L)
image = image.convert("L")
# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)
image.save("edges.png")