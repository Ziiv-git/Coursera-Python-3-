import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw
from IPython.display import display

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
#enhancer=ImageEnhance.Brightness(image)
images=[]
#for i in range(1, 10):
 #   images.append(enhancer.enhance(i/10))

width, height = image.size
fonts = ImageFont.truetype('readonly/fanwood-webfont.ttf',70)

images=[]
intensity = [0.1,0.5,0.9]
for i in range(1,4):
    for value in intensity :
        newimage = Image.new(image.mode,(width,height+70))
        capt = ImageDraw.Draw(newimage)
        capt.text((0, newimage.height - 70), 'channel {} intensity {}'
                         .format(i-1, value), font=fonts, fill=(255, 255, 255))
        new = image.copy()
        for x in range(height) :
            for y in range(width) :
                if i == 1 :
                    current = new.getpixel((y,x))
                    r,g,b = current
                    r = int(r*value)
                    newimage.putpixel((y,x),(r,g,b))
                elif i == 2 :
                    current = new.getpixel((y,x))
                    r,g,b = current
                    g = int(g*value)
                    newimage.putpixel((y,x),(r,g,b))
                else :
                    current = new.getpixel((y,x))
                    r,g,b = current
                    b = int(b*value)
                    newimage.putpixel((y,x),(r,g,b))
        images.append(newimage)

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
