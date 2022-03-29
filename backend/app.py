import json
import os
import uuid
from flask import Flask, request
import face_recognition

# UPLOAD_FOLDER = '/home/mtan/src/multi-person-face-identification/backend/known/'
REGISTER_FOLDER = './known/'
MATCH_FOLDER = './unknown/'

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/

app.config['UPLOAD_FOLDER'] = REGISTER_FOLDER
@app.route('/register', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    file = request.files['file']
    extension = os.path.splitext(file.filename)[1]
    f_name = str(uuid.uuid4()) + extension
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
  return json.dumps({'filename':f_name})


app.config['UPLOAD_FOLDER'] = MATCH_FOLDER
@app.route('/match', methods=['GET', 'POST'])
def match():
  if request.method == 'POST':
    file = request.files['file']
    extension = os.path.splitext(file.filename)[1]
    f_name = str(uuid.uuid4()) + extension
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
    
    known_image = face_recognition.load_image_file("known/melvin.jpg")
    unknown_image = face_recognition.load_image_file("unknown/" + f_name)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    if results[0]:
      return "<p>This is a match!</p>"
    else:
      return "<p>Not a match</p>"