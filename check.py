import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()  # reads frames from a camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to gray scale of each frames
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detects faces of different sizes in the input image4
    '''print(faces)
    for (x, y, w, h) in faces:
        if x==None and y==None and w==None and h ==None:
            print(' NOT Detected')
        else:
            print('detected')

    k = cv2.waitKey(30) & 0xff  # Wait for Esc key to stop
    if k == 27:
        break
cap.release()  # Close the window
cv2.destroyAllWindows()  # De-allocate any associated memory usage
'''
    if len(faces)!=0:
        print('Detected')
    else:
        print('Not detected')
cap.release()  # Close the window
cv2.destroyAllWindows()