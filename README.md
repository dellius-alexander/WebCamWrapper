# WebCamWrapper

WebCamWrapper is a simple Flask-based web application that streams video from a webcam. The application captures frames from the webcam using OpenCV and serves them as a Motion JPEG stream.

## Features

- Stream video from a webcam in real-time.
- Simple and clean web interface.
- Easy to set up and run.

## Requirements

- Python 3.x
- Flask
- OpenCV

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/WebCamWrapper.git
    cd WebCamWrapper
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to view the webcam stream.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `.gitignore`: Git ignore file to exclude unnecessary files from version control.

## Routes

- `/`: Renders the index page.
- `/webcam/<int:cam_id>`: Streams the webcam feed for the specified camera ID.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.