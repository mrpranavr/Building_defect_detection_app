from flask import Flask, render_template, request
import cv2
from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
import tensorflow as tf

# Creating the flask application and loading the model
app = Flask(__name__, template_folder="templates")
model = load_model('Building_defect_detection_model.h5')
print('Loaded model from disk')


# Routing to the html pages
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/intro', methods=['GET'])
def about():
    return render_template('intro.html')


@app.route('/upload', methods=['GET', 'POST'])
def predict():
    print("[INFO] starting video stream ....")
    vs = cv2.VideoCapture(0)
    (W,H) = (None, None)

    while True:
        (grabbed, frame) = vs.read()
        if not grabbed:
            break

        if W is None or H is None:
            (H,W) = frame.shape[:2]

        output = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224,224))
        x = image.img_to_array(frame)
        x = np.expand_dims(frame, axis = 0)
        img_data = preprocess_input(x)
        result = np.argmax(model.predict(img_data), axis = -1)
        index = ['roof', 'flakes','crack']
        result = str(index[result[0]])
        
        # display the result
        cv2.putText(output, "activity: {}".format(result), (10,120), cv2.FONT_HERSHEY_PLAIN,
                    1, (0,255,255), 1)
        #play audio
        cv2.imshow("Output", output)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    print("[INFO] cleaning up ...")
    vs.release()
    cv2.destroyAllWindows()
    return render_template("upload.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug=False)