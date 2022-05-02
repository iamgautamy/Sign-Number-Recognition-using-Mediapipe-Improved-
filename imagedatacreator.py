import numpy as np
import pandas as pd
import cv2
from pathlib import Path

def get_images():

    #set the label
    Class = "9"
    Path('ImgDataset/' + Class).mkdir(parents=True, exist_ok=True)

    #open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    i=0
    
    while True:
        ret,frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
     #open frame
        cv2.putText(frame, "Capturing...", (10,10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.rectangle(frame, (100,100), (300,300), (0,255,0), 2)
        cv2.imshow("Frame", frame)
        cv2.imwrite('ImgDataset/' + Class + '/' + Class + str(i) + '.jpg', frame)
        print("Number of images: ", i)
        i+=1
        #to exit
        if(cv2.waitKey(1) == ord('q')) or (i==500):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    get_images()
