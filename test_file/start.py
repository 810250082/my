from flask import Flask , request ,render_template , url_for , redirect
from werkzeug import secure_filename
import os
#from app.simple import simple_page
from app import *

app = Flask(__name__)
app.register_blueprint(simple_page)

app.config['UPLOAD_URL'] = './static/upload'
ALLOW_EXT = set(['txt' , 'pdf' , 'png' , 'jpg' , 'jpeg' , 'gif'])

@app.route('/')
def index():
    return "hello world!"


#allow upload
def allowUpload(fileName):
    return '.' in fileName and fileName.rsplit('.' , 1)[1] in ALLOW_EXT



@app.route('/upload' , methods=['GET' , 'POST'])
def uploadFile():
    fileUrl = request.args.get('fileUrl' , '')
    if request.method == "POST":
        file = request.files['myPic']
        if file and allowUpload(file.filename):
            filename = secure_filename(file.filename)
            fileUrl = os.path.join(app.config['UPLOAD_URL'] , filename)
            file.save(fileUrl)
            fileUrl = fileUrl[1:]
    return render_template('upload_file.html' , fileUrl = fileUrl)



if __name__ == "__main__":
    app.run("0.0.0.0" , debug = True)