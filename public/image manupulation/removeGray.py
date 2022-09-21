from PIL import Image
from sympy import limit

originalImageFileName = "threelogo.png"
originalImage = Image.open(originalImageFileName)

originalImage.show()

editedImage = Image.new("RGBA", originalImage.size, "#00000000")


limits = [0, 40, 200]


for x in range(0, editedImage.size[0]):
    for y in range(0, editedImage.size[1]):
        pixel = originalImage.getpixel((x, y))
        if pixel[3] != 0:
            if pixel[0] >= limits[0] and pixel[0] <= limits[1]:
                editedImage.putpixel((x, y), (0, 0, 0, 255))
            if pixel[0] > limits[1] and pixel[0] <= limits[2]:
                editedImage.putpixel((x, y), (0, 0, 0, 0))
            if pixel[0] > limits[2]:
                editedImage.putpixel((x, y), (255, 255, 255, 255))
            
            
editedImage.show()
editedImage.save("threeJSLogo.png", "png")