import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import shutil
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import subprocess 

# 加载预训练的 ResNet50 模型
model = ResNet50(weights='imagenet')

# Function to classify a single image
def classify_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Get the top prediction label
    top_prediction = decoded_predictions[0][1].lower()

    # Define categories based on top prediction (still using some keywords)
    if any(keyword in top_prediction for keyword in ['dog', 'cat', 'horse', 'sheep', 'bird']):
        category = "Animal"
    elif any(keyword in top_prediction for keyword in ['person', 'man', 'woman', 'human', 'child']):
        category = "Human"
    else:
        category = "Scenery"

    return category, decoded_predictions

# Function to classify and save images
def classify_and_save_images(file_paths):
    for img_path in file_paths:
        category, predictions = classify_image(img_path)

        # Create folder for category if it doesn't exist
        output_folder = os.path.join('classified_images', category)
        os.makedirs(output_folder, exist_ok=True)

        # Move the image to the category folder
        shutil.copy(img_path, os.path.join(output_folder, os.path.basename(img_path)))

    messagebox.showinfo("Classification Complete", "Images have been classified and saved.")

# Main Application
def create_app():
    def select_images():
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=(
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*")
            )
        )
        if file_paths:
            classify_and_save_images(file_paths)

    def open_folder():
        folder_path = os.path.abspath('classified_images')
        if os.path.exists(folder_path):
            # 判断操作系统并打开文件夹
            if os.name == 'nt':  # Windows
                os.startfile(folder_path)
            elif os.name == 'posix':  # macOS 或 Linux
                subprocess.run(["open", folder_path])  # macOS
                
        else:
            messagebox.showwarning("No Folder Found", "No classified images found. Please classify images first.")

    # Set up the main window
    root = tk.Tk()
    root.title("Image Classifier")
    root.geometry("600x400")
    root.resizable(False, False)

    # Style
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12))

    # Header
    header = tk.Label(root, text="AI Image Classifier", font=("Helvetica", 20), bg="#4CAF50", fg="white")
    header.pack(fill=tk.X, pady=10)

    # Upload Button
    upload_btn = ttk.Button(root, text="Upload Images", command=select_images)
    upload_btn.pack(pady=20)

    # Open Folder Button
    open_btn = ttk.Button(root, text="Open Classified Images Folder", command=open_folder)
    open_btn.pack(pady=10)

    # Instructions
    instructions = tk.Label(
        root,
        text="Instructions:\n1. Click 'Upload Images' to classify images.\n"
             "2. Images will be categorized into Animal, Human, or Scenery.\n"
             "3. Open the folder to view the results.",
        font=("Helvetica", 12),
        justify=tk.LEFT
    )
    instructions.pack(pady=20)

    # Footer
    footer = tk.Label(root, text="Developed by 李俊豪", font=("Helvetica", 10), fg="gray")
    footer.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()
