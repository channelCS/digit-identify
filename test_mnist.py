import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow
import matplotlib.pyplot as plt




json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load woeights into new model
loaded_model.load_weights("model.h5")
print("Loaded Model from disk")

loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])



#img_answer = (img_resized/255.0).astype('float32')
#
#plt.imshow(np.uint8(img_tinted))
#plt.show()

x = imread('output.png',mode='L')
x = np.invert(x)
x = imresize(x,(28,28))
plt.imshow(x)
plt.show()
x = x.reshape(1,28,28,1)

out = loaded_model.predict(x)
print(out)
print(np.argmax(out,axis=1))