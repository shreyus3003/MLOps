from flask import Flask, request, render_template, flash
from pathlib import Path

import os
import model

directory = "uploaded"
home = str(Path.home())
print(home)
path = os.path.join(home, directory)
if not os.path.exists(path):
   os.makedirs(path)

# os.mkdir(path, 755)

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        uploaded_image = request.files['file']
        if uploaded_image.filename != '':
            # image_path = os.path.join('static', uploaded_image.filename)
            # uploaded_image.save(image_path)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'],uploaded_image)
            uploaded_image.save(image_path)
            preprecessed_image = model.preprocessData(image_path)
            predicted_value = model.mnist_model.predict(preprecessed_image)
            result = { 'predicted_image' : predicted_value}
            flash(result)
            flash(uploaded_image)
            return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run( debug = True)

