from __future__ import absolute_import, division, print_function, unicode_literals
import warnings
with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	import tensorflow as tf
	from tensorflow.keras import datasets, layers, models
	import matplotlib.pyplot as plt

# rest of code from tutorial 
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# this block is importing data and setting and labeling them in categories
# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

#plots the images with each of the class names of the first 25 images

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

#defines the layers and seperating based on color, size etc to label them later
# putting the data into a shape,
#The 6 lines of code below define the convolutional base using a common 
#pattern: a stack of Conv2D and MaxPooling2D layers.

model.summary()

#displays the model of the dataset 
