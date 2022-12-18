from flask import Flask, request, render_template


import os
# import model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        uploaded_image = request.files['file']
        if uploaded_image.filename != '':
            image_path = os.path.join('static', uploaded_image.filename)
            uploaded_image.save(image_path)
            # preprecessed_image = model.preprocessData(image_path)
            # predicted_value = model.mnist_model.predict(preprecessed_image)
            result = { 'predicted_image' : 2}
            return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run( debug = True)

