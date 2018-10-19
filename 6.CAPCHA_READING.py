import cv2
from pytesseract import image_to_string
from PIL import Image

path=raw_input("enter file address:")
image=cv2.imread(path)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
filename=raw_input("enter where to store greyscale image:")
cv.imwrite(filename, gray)  
t=image_to_string(Image.open(filename))

if t[1]=='+':
    print (t[0], t[1], t[2], ' = ', int(t[0])+int(t[2]))
elif t[1]=='-':
    print (t[0], t[1], t[2], ' = ', int(t[0])-int(t[2]))
elif t[1]=='*':
    print (t[0], t[1], t[2], ' = ', int(t[0])*int(t[2]))
elif t[1]=='/':
    print (t[0], t[1], t[2], ' = ', int(int(t[0])/int(t[2])))
