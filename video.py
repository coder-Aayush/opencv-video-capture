import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FOR WINDOWS USE ----- *'DIVX' 
# FOR MACOS OR LINUX USE --  *'XVID'

writer = cv2.VideoWriter('videofilename.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

while True:
    ret,frame = cap.read()
    
#    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
writer.release()
cv2.destoryAllWindows()