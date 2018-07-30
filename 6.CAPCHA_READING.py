mport cv2
import pytesseract
from PIL import Image

path=raw_input("enter file name:")
image=cv2.imread(path)
gray=cv2.wtcolor(image,cv2.COLOR_BGR2GRAY)
filename="image.png"
cv.imwrite(filename, gray)
text=pytesseract.image_to_string(Image.open(filename))
text1=""
text2=""
for i in len(text):
    if text[letter]=='+':
     text1=text[0,letter]
     text2=text[letter+1:]
i=int(text1,[10])
j=int(text2,[10])
k=i+j
print k
