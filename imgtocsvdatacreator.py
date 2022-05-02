import numpy as np
import pandas as pd
import mediapipe as mp
import cv2
import os

def process_image(file_path):

    #reading images
    image = cv2.imread(file_path)
    #torgb
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #flip image
    image = cv2.flip(image, 1)
    #media pipe solutions
    mp_hands = mp.solutions.hands
    #initialize media pipe
    hands = mp_hands.Hands(static_image_mode=True,max_num_hands=1,min_detection_confidence=0.7)

    #result
    output = hands.process(image)
    hands.close()


    try:
        #get hand landmarks
        data= output.multi_hand_landmarks[0]
        #print(data)
        data = str(data)
        data = data.strip().split('\n')

        garbage = ['landmark {', '  visibility: 0.0', '  presence: 0.0', '}']

        without_garbage = []

        for i in data:
            if i not in garbage:
                without_garbage.append(i)

        clean = []

        for i in without_garbage:
            i = i.strip()
            clean.append(i[2:])

        for i in range(0, len(clean)):
            clean[i] = float(clean[i])

        return(clean)

    except:
        return(np.zeros([1,63], dtype=int)[0])
#to make csv from mediapipe keypoints    
def make_csv():
    
    mypath = 'ImgDataset'
    file_name = open('dataset.csv', 'a')

    for each_folder in os.listdir(mypath):
        if '._' in each_folder:
            pass

        else:
            for each_number in os.listdir(mypath + '/' + each_folder):
                if '._' in each_number:
                    pass
                
                else:
                    label = each_folder

                    file_loc = mypath + '/' + each_folder + '/' + each_number

                    data = process_image(file_loc)
                    try:
                        for id,i in enumerate(data):
                            if id == 0:
                                print(i)
                            
                            file_name.write(str(i))
                            file_name.write(',')

                        file_name.write(label)
                        file_name.write('\n')
                    
                    except:
                        file_name.write('0')
                        file_name.write(',')

                        file_name.write('None')
                        file_name.write('\n')
       
    file_name.close()
    print('Data Created !!!')

if __name__ == "__main__":
    make_csv()