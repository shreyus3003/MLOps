import os
import requests
import urllib.request
import wget as wget
# from keras.utils.image_utils import load_img
# from tensorflow.keras.models import load_model
# import matplotlib.pyplot as plt
# from tensorflow.keras.utils import img_to_array
from keras.models import load_model
# import numpy as np

urllib.request.urlretrieve("https://raw.githubusercontent.com/shreyus3003/AWS-SageMaker/master/clasify.h5",filename="/content/clasify1.h5")
url = 'https://raw.githubusercontent.com/shreyus3003/AWS-SageMaker/master/clasify.h5'

model = load_model('/content/clasify1.h5')
print(model.summary)

img = load_img('/content/img_1.jpeg', grayscale=True, target_size=(28,28))
print(img.size)
plt.imshow(img)
plt.show()

img = img_to_array(img)
img = img.reshape(1, 28, 28, 1)
img_res = img.astype('float32')
img_res = img_res/255.0

model = load_model('/content/clasify.h5')

pred = model.predict(img)
digit = np.argmax(pred)
print(digit)