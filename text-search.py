# Jacob Hardman
# CS 350
# Professor
# 9/1/2021

import tkinter as tk
from tkinter import filedialog
import sys, ctypes

def open_file_dialog():
    path = filedialog.askopenfile(initialdir="/", title="Select File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    
window = tk.Tk()
window.title("Text Search")

content = tk.Frame(window, height="600", width="800")
content.pack(expand="true", fill="both")

text_frame = tk.Frame(content, padx="10", pady="10")
text_frame.place(relwidth="0.5", relheight="1")

file_contents = tk.Text(text_frame, undo="true")
file_contents.place(relwidth="1", relheight="1")

options_frame = tk.Frame(content, padx="10", pady="10", bg="blue")
options_frame.place(anchor="ne", relx="1", relwidth="0.5", relheight="1")

label = tk.Label(options_frame, text="File Path")
label.place(relwidth="0.4", relheight="0.05")

select_file_button = tk.Button(options_frame, text="Select File", command=open_file_dialog)
select_file_button.place(anchor="east", relx="0.5", relwidth="0.4", relheight="0.05")

file_path_entry = tk.Entry(options_frame, width="100")
file_path_entry.place(rely="0.06", relwidth="1", relheight="0.05")

# This code fixes the blurry text that tkinter has when being used on Windows. I got this solution from Stack Overflow:
# https://stackoverflow.com/questions/36514158/tkinter-output-blurry-for-icon-and-text-python-2-7/43033405
if __name__ == "__main__":   
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

window.mainloop()
