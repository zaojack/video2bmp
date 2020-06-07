import os
import cv2
from tkinter import filedialog
file=filedialog.askopenfilename()
print(file)
video_cap = cv2.VideoCapture(file)
fps=video_cap.get(cv2.CAP_PROP_FPS)
print(fps)
i=0
a=os.path.exists('./out')
if(a==False):
    os.mkdir('./out')
while (True):
    ret, frame = video_cap.read()
    if ret is False:
        print('结束')
        break
    cv2.imshow('frame',frame)
    name='./out/frame'+str(i)+'.bmp'
    cv2.imwrite(name,frame)
    b=cv2.waitKey(1)
    i+=1
    if(b==27):
        break
cv2.waitKey(0)
