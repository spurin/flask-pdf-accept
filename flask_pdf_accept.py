from io import BytesIO
from flask import Flask, jsonify, send_file
from flask_accept import accept
from reportlab.pdfgen import canvas

# Create an app
app = Flask(__name__)

# Default route
@app.route('/')
@accept('text/html')
def hello_world():
    return 'Hello World!'

# Default route with json accept
@hello_world.support('application/json')
def hello_world_json():
    return jsonify(result="Hello World!")

# Default route with pdf accept
@hello_world.support('application/pdf')
def hello_world_pdf():
    c = canvas.Canvas('hello_world.pdf')
    c.drawString(100,750,"Hello World!")

    # Create a file like object
    file_like = BytesIO(c.getpdfdata())

    # Return pdf file
    return send_file(
                 file_like,
                 attachment_filename='hello_world.pdf',
                 mimetype='application/pdf'
           )

if __name__ == '__main__':
    app.run()
