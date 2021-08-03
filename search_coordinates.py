
# USe opencv to capture mouse events
import cv2 

#Open Coordinates text file to save the mouse clicks
f = open("coordinates.txt","w")

# Mouse callback function to register and save mouse (double clicks)
def draw_circle(event,x,y):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #img[:] = 0

        #Select location of the text(TRIAL & ERROR)
        #Double click to get the coordinates
        #The coordinates selected will mark the start of the text
        #DOUBLE CLICK TO SELECT
        #The selected coordinates will be displayed in top right corner

        cv2.putText(img,"coordinates (%d,%d)"%(x,y),(60,60),2,1,(0,255,0)) 
        f.write(str(x)+"\n")                                             
        f.write(str(y)+"\n")                                              
                                                                         
# Create a black image, a window and bind the function to window
img = cv2.imread("sample_certificate.png")


#cv2.imshow('image',img)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(10) & 0xFF == 27:   #Press Escape Key to terminate window
        break
cv2.destroyAllWindows()   

f.close()