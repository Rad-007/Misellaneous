
import cv2
"""
cap=cv2.VideoCapture('sample1.mp4')

frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps=cap.get(cv2.CAP_PROP_FPS)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fourcc=cv2.VideoWriter_fourcc(*'FMP4')
out=cv2.VideoWriter('reversed1.mp4',fourcc,fps,(int(width*0.5),int(height*0.5)))

print("nO OF FRAMES :{}".format(frames))

print("FPS IS :{}".format(fps))

frame_index=frames-1

if(cap.isOpened()):
    while(frame_index!=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame=cap.read()

        frame=cv2.resize(frame,(int(width*0.5),int(height*0.5)))
        out.write(frame)

        frame_index-=1
        if(frame_index%100==0):
            print(frame_index)
        
        cv2.imshow('Frame',frame)

 

    # Press Q on keyboard to  exit

        if cv2.waitKey(25) & 0xFF == ord('q'):

            break

 

  # Break the loop

        else:
            break


out.release()
cap.release()

cv2.destroyAllWindows()
"""

cap = cv2.VideoCapture("sample2.mp4")
 
# read method of video object will return
# a tuple with 1st element denotes whether
# the frame was read successfully or not,
# 2nd element is the actual frame.
 
# Grab the current frame.
check , vid = cap.read()
 
# counter variable for
# counting frames
counter = 0
 
# Initialize the value
# of check variable
check = True
 
frame_list = []
 
# If reached the end of the video
# then we got False value of check.
 
# keep looping until we
# got False value of check.
while(check == True):
     
    # imwrite method of cv2 saves the
    # image to the specified format.
    #cv2.imwrite("frame%d.jpg" %counter , vid)
    check , vid = cap.read()
     
    # Add each frame in the list by
    # using append method of the List
    frame_list.append(vid)
     
    # increment the counter by 1
    counter += 1
 
# last value in the frame_list is None
# because when video reaches to the end
# then false value store in check variable
# and None value is store in vide variable.
 
# removing the last value from the
# frame_list by using pop method of List
frame_list.pop()

# looping in the List of frames.
for frame in frame_list:
     
    # show the frame.
    #cv2.imshow("Frame" , frame)
     
    # waitkey method to stopping the frame
    # for some time. q key is presses,
    # stop the loop
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break
     
# release method of video
# object clean the input video
cap.release()
 
# close any open windows
cv2.destroyAllWindows()
 
# reverse the order of the element
# present in the list by using
# reverse method of the List.
frame_list.reverse()
 
for frame in frame_list:
    cv2.imshow("Reverse" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break
 
cap.release()
cv2.destroyAllWindows()


