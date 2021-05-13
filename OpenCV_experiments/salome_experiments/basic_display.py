import pytesseract
from PIL import Image


result = pytesseract.image_to_string(Image.open('student.jpg'))

#Modif résultat
arr = result.split('\n')[0:-1]
result = '\n'.join(arr)

print(result)