import cv2

'''
[ASSIGN CAMERA TO VIDEO CAPTURE OBJECT]

    - cv2.VideoCapture(n) where n is the camera device in your PC [! YOU MIGHT WANNA CHANGE THIS PART !]
    - 0 : External Cam
    - 1 : Built-in Camera
'''

cap = cv2.VideoCapture(0)


'''
[INITIATE TRACKER]

    - several Tracker type can be selected, in this program, I used TrackerMOSSE and Tracker CRST
    - CRST Tracker is slow but highly accurate
    - MOSSE Tracker is more suitable for live video for live tracking
    - For those who use OpenCV <4.5, the command is a bit different:
            tracker = cv2.TrackerMOSSE_create(

'''
tracker = cv2.legacy.TrackerMOSSE_create()


# [Frame]
success, img = cap.read()                                                                           # Framing
bbox = cv2.selectROI("Tracking",img,False)


# [Initialise Tracker]
tracker.init(img,bbox)



# [Create Function when Tracking is ongoing]
def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking...", (75, 75), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(img, "Press [q] to exit", (240, 450), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 1)




# [Introduce While Loop to keep draw the box if the tracking is success and output "Object Lost" if failed]
while True:
    timer = cv2.getTickCount()                                                                          # getting pfs
    success, img = cap.read()                                                                           # See Line 28
                                                                                                        # bbox has 4 value (X,Y,width,Height)

    success,bbox = tracker.update(img)                                                                  # update tracker

    if success:
        drawBox(img,bbox)                                                                               # Draw Box at where the tracked object is
    else:
        cv2.putText(img, "Object Lost",(75, 75), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
        cv2.putText(img, "Press [q] to exit", (240, 450), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 1)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)                                         # Display the FPS in the tracking window
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)              # Positioning and Formatting of the text
    cv2.imshow("Object Tracking View",img)                                                              # Caption for the Tracking Window



    if cv2.waitKey(1) & 0xff == ord('q'):                                                               # see if we have press q key, if yes break
        break





