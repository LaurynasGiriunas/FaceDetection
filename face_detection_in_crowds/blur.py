from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

def rounded_rectangle(draw, xy, rad, fill=None):
    x0, y0, x1, y1 = xy
    draw.rectangle([ (x0, y0), (x1, y1) ], fill=fill)

# Open an image
im = Image.open('blur.jpg')

# Create rounded rectangle mask
mask = Image.new('L', im.size, 0)
draw = ImageDraw.Draw(mask)
rounded_rectangle(draw, (0,0, 100, 100), rad=0, fill=255)
mask.save('mask.png')

# Blur image
blurred = im.filter(ImageFilter.GaussianBlur(20))

# Paste blurred region and save result
im.paste(blurred, mask=mask)
im.save('blurer.jpg')
