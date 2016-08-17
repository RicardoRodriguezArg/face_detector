import sys, getopt, os
import uuid
from uuid import uuid4
import cv2
import logging
import time
sys.path.insert(0,'../../../face_detector')
sys.path.insert(0,'../../face_detector')
sys.path.insert(0,'../face_detector')
from flask import Flask, request, redirect, url_for, json
from werkzeug.utils import secure_filename
from detectors.haar_face_detector.detector_haar import FaceDetector
app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app.config['UPLOAD_FOLDER']='/home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/service/temporal'
CONFIG_DATA_DICT = {}
facedetector = None
@app.route("/")
def main():
    return "Face Detector Service"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        full_name = os.path.join(app.config['UPLOAD_FOLDER'], f_name)
        file.save(full_name)
        time.sleep(1)
        facedetector.face_detection_data(cv2.imread(full_name))

        return json.dumps({'Amount Faces: ':str(facedetector.get_face_count())})
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Detect Faces>
    </form>
    '''


def parse_cfg_option(cfg_file):
    with open(cfg_file, 'r') as cfg_file:
        data = cfg_file.read()
    data = data.split('\n')
    for line in data:
    	if len(line)>0:
    		if line.split('=')[0].strip() == 'weigth_path':
    			CONFIG_DATA_DICT['weigth_path']=line.split('=')[1].strip()



if __name__ == "__main__":
    parse_cfg_option(sys.argv[1])
    facedetector = FaceDetector(CONFIG_DATA_DICT['weigth_path']) 
    app.run(debug = True)

