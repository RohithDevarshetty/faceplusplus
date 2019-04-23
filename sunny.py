import serial
import time
import pyautogui
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


def get_image():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def detect_face(gray):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)!=0:
        return True
    else:
        return False


ArduinoSerial = serial.Serial('com3', 9600)
time.sleep(2)


while 1:
    img = get_image()
    faces = detect_face(img)
    if faces:
        print('face detected')
        incoming = str(ArduinoSerial.readline())
        print(incoming)
        if 'movedback' in incoming:
            print('Zooming IN')
            pyautogui.hotkey('ctrl', '+')
        if 'movedfront' in incoming:
            print('Zooming OUT')
            pyautogui.hotkey('ctrl', '-')
        if 'Stay' in incoming:
            print('Constant position')
            #  pyautogui.hotkey('shift', 'right')
        incoming = "";
    else:
        print("\r face not detected")

cap.release()





