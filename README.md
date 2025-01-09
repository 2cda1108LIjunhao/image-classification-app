# image-classification-app
AI Image Classifier

This project is a desktop application that allows users to classify images into categories using a pre-trained ResNet50 model. It features a simple graphical user interface (GUI) built with Tkinter and includes AI functionality for image classification.

Features

Image Classification: Uses the ResNet50 model to classify images into three categories: Animal, Human, or Scenery.

User-Friendly Interface: Provides a graphical interface to upload images and view the classified results.

Automatic Folder Organization: Saves classified images into corresponding folders based on their categories.

Installation

Prerequisites

Install Python (3.8 or higher).

Install required libraries:

pip install tensorflow pillow numpy

Steps to Set Up

Clone this repository:

git clone <repository_url>
cd <repository_directory>

Place the ResNet50 pre-trained weights file in the same directory. If not available, you can download the weights using the command:

from tensorflow.keras.applications import ResNet50
model = ResNet50(weights='imagenet')

Run the application:

python main.py

Usage

Launch the application by running the script:

python main.py

Use the "Upload Images" button to select images you want to classify. Supported formats: .jpg, .jpeg, .png, .bmp, .gif.

The application will classify the images and save them into folders named Animal, Human, or Scenery inside the classified_images directory.

Use the "Open Classified Images Folder" button to access the results.


Dependencies

Python 3.8+

TensorFlow 2.0+

Pillow

NumPy

Notes

Ensure you have a stable internet connection for the initial download of the ResNet50 weights if they are not already downloaded.

For better performance, you can manually download the ResNet50 weights and specify the local path in the script.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Developed by 李俊豪
