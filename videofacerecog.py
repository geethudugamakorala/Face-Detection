import cv2   #Import opencv library
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #giving the file to define face .thats how computer knows how to identify a face
#video = cv2.VideoCapture('filename.mp4')        # If you want to use a video file instead use this insted of 2nd one and add the video to this file directory

video = cv2.VideoCapture(0)     # set up camera 0 means primary camera ,if there are many cameras you can change it to 1,2,3 ...
video.set(3, 600)               #set the width of video
video.set(4, 300)               #set the hight of video

while True:

    check,frame = video.read()                      #capture frame
    #print(frame)                                   #use this to check how frame is stored
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #converts colour image to gray scale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=10)  #find the location of faces and save them in a list
    for x, y, w, h in faces:        #x and y are starting point of the face rectangle and w ,h are width and hight of the face rectangle
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 0, 255 ), 2)         #draw rectangle where faces are
    cv2.imshow("Capturing", frame)          #show the rectangle added frame in a window
    key=cv2.waitKey(1)                      #how long window displayed
    if key == ord('q'):                     #breaking the while loop if q is presssed
        break

video.release()                     #stop using webcam
cv2.destroyAllWindows()             #close the window

#In the while loop its actually does is processing single frame at a time and displaying them in higher speed.That makes it a video