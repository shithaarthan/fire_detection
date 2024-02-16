import main
from os import system
from ultralytics import YOLO
import cv2
import time
import gen_message

model = YOLO("path to your model file(yolo v8)")
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
count=0

system('clear')

while True:
    _, frame = cap.read()
    results=model.predict(frame)
    for r in results:
        img=r.plot()
        for box in r.boxes:
            
            class_id = r.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            confidence = round(box.conf[0].item(), 2)
            if class_id=="fire":                   # change your class id here
               main.fireThreatMsg()                #sends a email user
               gen_message.send_text_message()     #sends text message to the user
               time.sleep(300)
                
                
            
    cv2.imshow('Color Image', img)           #shows the output window for camera

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
