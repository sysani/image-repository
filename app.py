import os, os.path
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import secrets

UPLOAD_FOLDER = './static/imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['POST','GET'])
def index():
    #save imgs to display
    imgs = os.listdir('static/imgs/')

    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)

        image = request.files['image']
        if image.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if len(imgs) > 49:
            flash('Max allotment reached: 50 images maximum')
            return redirect(request.url)

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

        else:
            flash('Image could not be uploaded. Please use .jpg, .jpeg, .gif or .png filetypes only!')
        
    return render_template("index.html", imgs=imgs)

if __name__ == "__main__":
    app.run()


# export FLASK_APP=app.py
# flask run

