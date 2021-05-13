
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("student.jpg")
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
result = pytesseract.image_to_string(Image.open('temp2.jpg'), lang='eng')

#Modif résultat
arr = result.split('\n')[0:-1]
result = '\n'.join(arr)

print(result)