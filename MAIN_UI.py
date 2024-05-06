from tkinter import *
import os
from PIL import Image,ImageTk


win=Tk()
win.title("Smart Surveillance for Home Security system")
win.configure(bg="#000000")
win.geometry("1920x1080")
img=Image.open("UI_m1.png")
img=img.resize((1500,750))
bg=ImageTk.PhotoImage(img)

lbl=Label(win,image=bg)
lbl.place(x=0,y=0)

def run_file():
    command = 'python3 detect.py'
    os.system(command)

def photo():
    import tkinter as tk
    from tkinter import filedialog
    import os

    def select_image():
        # Open a file dialog to select an image file
        image_file = filedialog.askopenfilename(
            initialdir="/", title="Select Image", 
            filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("all files", "*.*")))
        # Set the text of the image entry widget to the selected file path
        image_entry.delete(0, tk.END)
        image_entry.insert(0, image_file)

    def save_image():
        # Get the selected image file path from the image entry widget
        image_file = image_entry.get()
        # Open a file dialog to select the destination directory
        dest_directory = filedialog.askdirectory(
            initialdir="/", title="Select Destination Folder")
        if dest_directory:
            # Get the destination file path
            dest_file = os.path.join(dest_directory, os.path.basename(image_file))
            # Save the image to the destination file
            with open(dest_file, "wb") as f:
                with open(image_file, "rb") as src_file:
                    f.write(src_file.read())
            # Display a message to the user
            message_label.config(text="Image saved successfully.")
        else:
            # Display an error message to the user
            message_label.config(text="Error: No destination folder selected.")

    # Create the tkinter window
    window = tk.Tk()

    # Create the widgets for the form
    image_label = tk.Label(window, text="Image:")
    image_entry = tk.Entry(window)
    image_button = tk.Button(window, text="Select Image", command=select_image)
    save_button = tk.Button(window, text="Save Image", command=save_image)
    message_label = tk.Label(window, text="")

    # Layout the widgets using the grid geometry manager
    image_label.grid(row=0, column=0)
    image_entry.grid(row=0, column=1)
    image_button.grid(row=0, column=2)
    save_button.grid(row=1, column=1)
    message_label.grid(row=2, column=0, columnspan=3)

    # Start the tkinter event loop
    window.mainloop()

        
label=Label(win,text=" FACE RECOGNITION USING CNN",bg="black",fg="white",font=("times",25,"bold"))
label.place(x=700,y=25)

label=Label(win,text=" Click below button to run the project",bg="black",fg="white",font=("times",25,"bold"))
label.place(x=700,y=150)

label=Button(win,text="Start",bg="black",fg="white",font=("times",25,"bold"),command=run_file)
label.place(x=900,y=340)


label=Button(win,text="upload a photo",bg="black",fg="white",font=("times",25,"bold"),command=photo)
label.place(x=1200,y=340)


win.mainloop()
