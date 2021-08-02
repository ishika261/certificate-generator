from PIL import ImageFont, ImageDraw, Image  
import cv2  
import numpy as np  
import pandas as pd
import os
import csv

#print(names_list)
print("Initialising script!")

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

f1 = open("coords.txt","r")
coordinates = f1.read().split("\n")

data=pd.read_csv('./Sample.csv')

flag = True

for i,row in data.iterrows():
        name = str(row['Name'])
        name=name.title()

        project=str(row['Project'])
        project=project.title()

        image = cv2.imread("sample_cert.png")  

# Convert the image to RGB (OpenCV uses BGR)  
        cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  

        # Pass the image to PIL  
        pil_im = Image.fromarray(cv2_im_rgb)  

        draw = ImageDraw.Draw(pil_im)  
        # use a truetype font  
        font = ImageFont.truetype("./Roboto-Medium.ttf", 100)      #You can change fonts from list given bottom
        font1 = ImageFont.truetype("./Roboto-Medium.ttf",50) 

        # Draw the text 
        draw.text((int(coordinates[0]), int(coordinates[1])), name, font=font , fill='red')
        draw.text((int(coordinates[2]), int(coordinates[3])), project , font=font1, fill='blue')
        
        # Get back the image to OpenCV  
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
        
        # if flag:
        #     cv2.imshow('Certificate', cv2_im_processed) #Shows sample image
        #     flag=False
        path = ''
        cv2.imwrite('./certificates/'+name+'.png',cv2_im_processed)
    #os.startfile('output.png')
        cv2.waitKey(0)  

        cv2.destroyAllWindows()

# with open('Sample_Data.csv' ,'r') as csv_file:
#     csv_reader =csv.reader(csv_file,delimeter=',')
#     line_count=0
    # for row in csv_reader:
    #     if line_count==0: 
    #         continue
    #     else:
    #         name=str(row[0])
    #         project=str(row[1])



# names=csv.read('Sample_Data.csv')



# flag=True

# for i,row in names.iterrows():
#     name = str(row['Name'])
#     name=name.title()

#     project=str(row['Project'])
#     project=project.title()


    # Load image in OpenCV  
    
    

# '''
# Other vareity of FONTS (Make sure you give proper path)

# MLSJN.TTF
# Lato-Black.ttf
# MATURASC.TTF
# OLDENGL.TTF
# VIVALDII.TTF
# copperplate gothic font.ttf


# '''




# centre 250
# len 125

# start centre -len/2
