from flask import Flask, request


import os
import model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        uploaded_image = request.files['file']
        if uploaded_image.filename != '':
            image_path = os.path.join('static', uploaded_image.filename)
            uploaded_image.save(image_path)
            preprecessed_image = model.preprocessData(image_path)
            predicted_value = model.mnist_model.predict(preprecessed_image)
            result = { 'predicted_image' : predicted_value}
            return render_template('result.html', result=result)
    return reder_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

