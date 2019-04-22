import serial
import time
import pyautogui
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


def get_image():
    ret, img = cap.read()  # reads frames from a camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to gray scale of each frames
    return gray


def detect_face(gray):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)!=0:
        return True
    else:
        return False


while 1:
    img = get_image()
    faces = detect_face(img)
    if faces:
        ArduinoSerial = serial.Serial('com3', 9600)  # Create Serial port object called arduinoSerialData
        time.sleep(2)  # wait for 2 seconds for the communication to get established
        incoming = str(ArduinoSerial.readline())  # read the serial data and print it as line
        print(incoming)
        if 'Play/Pause' in incoming:
            pyautogui.typewrite(['space'], 0.2)
        if 'Rewind' in incoming:
            pyautogui.hotkey('ctrl', 'left')
        if 'Forward' in incoming:
            pyautogui.hotkey('shift', 'right')
        if 'Volume Incresaed' in incoming:
            pyautogui.hotkey('shift', 'down')
        if 'Volume Decreased' in incoming:
            pyautogui.hotkey('shift', ' right')
        incoming = "";
    else:
        print("\r face not detected")
cap.release()





