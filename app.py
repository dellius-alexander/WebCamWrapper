import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)


def get_frame(webcam):
    """
    Get a frame from the webcam.
    :param webcam: The webcam object.
    :return: A frame from the webcam.
    """
    success, frame = webcam.read()
    if not success:
        return None
    # We are using Motion JPEG, but OpenCV defaults to capture raw images,
    # so we must encode it into JPEG in order to correctly display the video stream.
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()


def gen(cam_id: int):
    """
    Generate the video stream.
    :param cam_id: The camera id.
    :return: A frame from the webcam.
    """
    # Set up the webcam by id.
    webcam = cv2.VideoCapture(cam_id)
    while True:
        frame = get_frame(webcam)
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    """
    Render the index page.
    :return: The index page.
    """
    return render_template('index.html')


@app.route('/webcam/<int:cam_id>')
def get_webcam(cam_id: int):
    """
    Get the webcam feed.
    :param cam_id: The camera id.
    :return: The webcam feed.
    """
    return Response(gen(cam_id), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
