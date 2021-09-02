# Jacob Hardman
# CS 350
# Professor
# 9/1/2021

import tkinter as tk
from tkinter import filedialog
import sys, ctypes

# This code fixes the blurry text that tkinter has when being used on Windows. I got this solution from Stack Overflow:
# https://stackoverflow.com/questions/36514158/tkinter-output-blurry-for-icon-and-text-python-2-7/43033405
if __name__ == "__main__":   
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

def open_file_dialog():
    path = filedialog.askopenfile(initialdir="/documents", title="Select File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    file_entry.delete(0, "end")
    file_entry.insert(0, path.name.format())
    file_contents.delete("1.0", "end")
    file_contents.insert("1.0", path.read())

# Create main window
window = tk.Tk()
window.title("Text Search")

# Master frame to hold two sub frames
content = tk.Frame(window, height="600", width="800")
content.pack(expand="true", fill="both")

# Frame that contains the file's text
text_frame = tk.Frame(content, padx="10", pady="10")
text_frame.place(relwidth="0.5", relheight="1")

file_contents = tk.Text(text_frame, undo="true")
file_contents.place(relwidth="1", relheight="1")

# Frame that contains the file dialog as well as the search options
options_frame = tk.Frame(content, padx="10", pady="10")
options_frame.place(anchor="ne", relx="1", relwidth="0.5", relheight="1")

file_button = tk.Button(options_frame, text="Open File", command=open_file_dialog)
file_button.pack(pady="20")

file_entry = tk.Entry(options_frame, width="50")
file_entry.pack()

window.mainloop()
