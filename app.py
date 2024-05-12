from flask import Flask, render_template, Response, jsonify
import cv2
from deteccion.detection import userChoice 
from AI_generator.PPT3 import jugadaPc 
import time


jugada = None
class Video:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        ret, frame = self.video.read()
        
        return frame


app = Flask(__name__)
output = []

def gen(camera):
    global jugada
    jugada = None
    #while (time.time() - tiempo_inicio) < 5:
    while True:
        
        frame = camera.get_frame()
        
        choice = userChoice(frame)
        
        if choice != None:
            jugada = choice
            
        ret, jpg = cv2.imencode('.jpg', frame)
        
        frame = jpg.tobytes()
        print(choice)
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n'
              b'\r\n' + frame + b'\r\n\r\n')

@app.route('/')
@app.route('/FaceMaskDetection_HomePage')
def homepage():
    return render_template("index2.html")

@app.route('/video')
def video():
     return Response(gen(Video()),
                     mimetype='multipart/x-mixed-replace; boundary=frame')
     
@app.route('/showJugada')     
def showJugada():
    global jugada
    aiChoice = jugadaPc()
    
    # Renderizar la plantilla HTML y pasar las jugadas como parámetros
    return render_template('showResult.html', player_choice=jugada, computer_choice=aiChoice)
       

# --- main ---    

app.run(debug=True)

