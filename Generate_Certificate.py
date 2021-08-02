from PIL import Image,ImageFont,ImageDraw
import pandas as pd

def main():
    print("Initialising script!")
    names=pd.read_csv('Sample_Data.csv')
    
    for i,row in names.iterrows():
        name = str(row['Name'])
        name=name.title()

        project=str(row['Project'])
        project=project.title()

        empty_img = Image.open("IITISoc'21.jpg")
        font_size = 150
        font = ImageFont.truetype(r".\Dancing_Script\DancingScript-VariableFont_wght.ttf", 150)
        W,H = empty_img.size 
        w, h = font.getsize(name)
        width = ((W-w)/2)
        height = ((H-h)/2)-50
        if W%w >= 2:
            font_size = 130
            width = ((W-w)/2) +75
            height = ((H-h)/2)-10

        font = ImageFont.truetype(r".\Dancing_Script\DancingScript-VariableFont_wght.ttf", font_size)
        image_editable = ImageDraw.Draw(empty_img)
    
        image_editable.multiline_text((width,height), name, (35, 57, 75), font=font)

        empty_img.save("{}.jpg".format(name.replace(" ", "_")))
        if i % 50 == 0: 
            print('Processed {} Rows'.format(i))
    print("Process Complete!")

if __name__ == "__main__":
    main()


