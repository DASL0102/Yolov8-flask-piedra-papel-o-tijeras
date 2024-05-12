from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors




model = YOLO("deteccion/JUEGO.pt")

def userChoice(frame):
    global model
    names = model.names
    idx = 0
    gesture = None

    im0 = frame
    results = model.predict(im0, conf = 0.8, show=False, verbose=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    annotator = Annotator(im0, line_width=2, example=names)

    if boxes is not None:
        for box, cls in zip(boxes, clss):
            idx += 1
            gesture = names[int(cls)]
            annotator.box_label(box, color=colors(int(cls), True), label=names[int(cls)])

    jugada =  gesture 
    
    
    if jugada == 'Piedra':
        user_choice = 0
    elif jugada == 'Papel':
        user_choice = 1
    elif jugada == 'Tijera':
        user_choice = 2
    else:
        user_choice=None
         
    return user_choice

