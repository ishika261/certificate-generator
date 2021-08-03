from PIL import ImageFont, ImageDraw, Image  
import cv2  
import numpy as np
import pandas as pd

print("Initialising script!")

#Read Co-ordinates.txt file to use custom coordinates
f1 = open("coordinates.txt","r")
coordinates = f1.read().split("\n")

# use pandas to read the csv file
data=pd.read_csv('./sample_data.csv')

flag = True

# using a for loop iterate through rows in the csv file
for i,row in data.iterrows():
        name = str(row['Name'])
        name=name.title()

        mail=str(row['Mail'])
        mail=mail.title()


        #Open the certificate template you wish to use
        pil_im = Image.open("sample_certificate.png")  

        draw = ImageDraw.Draw(pil_im)  
       

        # use a truetype font  
        font = ImageFont.truetype("./Amsterdam.ttf", 140)      #You can change fonts from list given bottom
        font1 = ImageFont.truetype("./LexendDeca-Regular.ttf",35) 

        #Get the size of the certificate
        W,H = pil_im.size

        #Get the size of the tezt once the font is applied
        wn,hn = font.getsize(name)
        wp, yp = font1.getsize(mail)

        #Co-ordinates x and y mark the start of the text
        #You can hardcode the x,y coordinates or load them from the coordinates.txt file

        #To centre align the text in a particular line
        xName = W/2 - wn/2
        yName = 400

        xMail = W/2 -wp/2
        yMail = 890

        #xname = f1[0] yname=f1[1]
        #xmail =f1[2]  ymail =f1[2]

        # Draw the text 
        draw.text((xName, yName), name, font=font , fill='#03989E')
        draw.text((xMail,yMail ), mail , font=font1, fill='#373737')
        
        
    #Get back the image to OpenCV  
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
        
        #
        path = ''
        cv2.imwrite('./certificates/'+name+'.png',cv2_im_processed)

    #os.startfile('output.png')
        cv2.waitKey(0)  

        cv2.destroyAllWindows()

        #draw.save("{}.png".format(name.replace(" ", "_")))

print("Process Complete!")


    # image = Image.open('part_aaryan.pmg')
    # image = cv2.imread("part_aaryan.png")  

    # Convert the image to RGB (OpenCV uses BGR)  
    # cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  

    # Get back the image to OpenCV  
    #     cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
        
    #     if flag:
    #         cv2.imshow('Certificate', cv2_im_processed) #Shows sample image
    #         flag=False
    #     path = ''
    #     cv2.imwrite('./certificates/'+name+'.png',cv2_im_processed)

    # #os.startfile('output.png')
    #     cv2.waitKey(0)  

    #     cv2.destroyAllWindows()

