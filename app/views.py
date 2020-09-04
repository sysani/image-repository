from app import app
import os, os.path
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import secrets

if not os.path.exists('./app/static/imgs'):
    os.makedirs('./app/static/imgs')

UPLOAD_FOLDER = './app/static/imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

secret = secrets.token_urlsafe(32)
app.secret_key = secret
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['POST','GET'])
def home():
    #save imgs to display
    imgs = os.listdir('app/static/imgs/')

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
            return redirect(url_for('home'))

        else:
            flash('Image could not be uploaded. Please use .jpg, .jpeg, .gif or .png filetypes only!')
            
    return render_template("home.html", imgs=imgs)

#delete image
@app.route('/delete/<filename>')
def delete(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.remove(file_path)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)

