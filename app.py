from flask import  Flask, flash, request, redirect, url_for, jsonify
from flask_session import Session
from flask import request
import numpy
import os
from src import testModel
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'data/testingImages'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def hello_world():
    return 'Hello!'
@app.route('/ping')
def pong():
    return 'pong'
@app.route("/test/<string:url>")
def parkinson(url):
    result = testModel.testModel(url)
    return jsonify({'prediction': result.tolist()})

@app.route('/up_image',methods = ['POST'])
def up_image():
    imagefile = request.files.get('image', '')
    file = request.files['image']

    if file.filename=='':
        flash('No selected file')
        return redirect(request.url)
    fil_ex = file.filename.split('.')[1]
    if file and fil_ex in ALLOWED_EXTENSIONS:
        picture_path = os.path.join(app.root_path, UPLOAD_FOLDER, file.filename)
        file.save(picture_path)
        #filename = secure_filename(file.filename)
        #file.save(os.path.join(UPLOAD_FOLDER, filename))
    result = testModel.testModel(file.filename)
    print("res=>>", result)
    return jsonify({'prediction': result.tolist()})
if __name__ == "__main__":

  app.run()