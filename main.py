from ultralytics import YOLO
import cv2
model = YOLO(r"C:\Users\SHITHAARTHAN M\Desktop\best.pt")
# results = model(r"C:\Users\SHITHAARTHAN M\Downloads\1000_F_204846264_J8pMn8xTZ5giR83wkMK8A5BnKHdsKCZU.jpg")
# results = model.predict(source=1,classes=6,show=True)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    _, frame = cap.read()
    results=model.predict(frame,classes=6)
    for r in results:
        img=r.plot()
        for box in r.boxes:
            # x, y, w, h, class_id, confidence = result
            class_id = r.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            confidence = round(box.conf[0].item(), 2)
            
    cv2.imshow('Color Image', img)

    # Press 'q' to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

