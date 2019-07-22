from PIL import Image

def load_img(dog):
    return Image.open(dog)

def show_img(img):
     img.show()

def save_img(img,dog):
    return save(dog,"JPEG")

def obamicon(img):
    pixels = img.getdata()
    
    new_pixels = []
    
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    
    for p in pixels:
        intensity = p[0]+p[1]+p[2]
        

        if intensity < 182:
            new_pixels.append(darkBlue)
        elif intensity >=182 and intensity <364:
            new_pixels.append(red)
        elif intensity >=364 and  intensity <= 546:
            new_pixels.append(lightBlue)
        else:
            new_pixels.append(yellow)
            
    newImg = Image.new("RGB", img.size)
    newImg.putdata(new_pixels)
    newImg.show()
    return newImg

         
    

    

   
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
#def load_img():


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
#def show_img():


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
#def save_img():


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
#def obamicon()
