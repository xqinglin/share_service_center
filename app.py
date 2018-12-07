import pytesseract
from PIL import Image
from flask import Flask, render_template, url_for, request,redirect,send_from_directory
import os
import translation
def get_text(file):
    img = Image.open(file)
    text = pytesseract.image_to_string(img)
    return text
    print(text)
def m():
    html = url_for('static', filename='bigM.png')
    return '<img src='+html+'/>'


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    target = APP_ROOT+ '/static/image'
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png"):
            print("File supported moving on...")
        else:
            render_template("/", message="Files uploaded are not supported...")
        destination = "/".join([target, 'cur_image.png'])
        print(destination)
        upload.save(destination)
        text_result = get_text(target+'/'+'cur_image.png')
        translation_res = translation.translation(text_result, target='en')
        language = translation_res['detectedSourceLanguage']
        text_translate = translation_res['translatedText']
    return render_template("result.html",text_got = text_result, language=language, text_translate=text_translate)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == '__main__':
    print('start the app', app.name)
    app.run(port=4555, debug=True)