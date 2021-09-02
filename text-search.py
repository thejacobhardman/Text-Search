# Jacob Hardman
# CS 350
# Professor Christopher Harris
# 9/1/2021

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import sys, ctypes
import re

# This code fixes the blurry text that tkinter has when being used on Windows. I got this solution from Stack Overflow:
# https://stackoverflow.com/questions/36514158/tkinter-output-blurry-for-icon-and-text-python-2-7/43033405
if __name__ == "__main__":   
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

num_of_matches = 0

def open_file_dialog():
    path = filedialog.askopenfile(initialdir="/documents", title="Select File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    if path:
        file_entry.delete(0, "end")
        file_entry.insert(0, path.name.format())
        file_contents.delete("1.0", "end")
        file_contents.insert("1.0", path.read())

def search_for_text():
    global num_of_matches
    num_of_matches = 0
    file_contents.tag_delete("match")
    with open(file_entry.get(), "rt") as file_to_read:
        line_num = 1
        for line in file_to_read:
            if match_case.get() == 0:
                found_object = re.search(search_entry.get(), line, re.IGNORECASE)
            else:
                found_object = re.search(search_entry.get(), line)
            if found_object:
                size = found_object.span()[1] - found_object.span()[0]
                print(str(line_num) + "." + str(found_object.span()[0]))
                j = 0
                while j < size:
                    file_contents.tag_add("match", (str(line_num) + "." + str(found_object.span()[0] + j)))
                    file_contents.tag_config("match", background="yellow")
                    j += 1
                num_of_matches += 1
            line_num += 1
        
        # line_num = 1
        # for line in file_to_read:
        #     letter_num = 0
        #     for letter in line:
        #         if len(search_entry.get()) > 1: # TODO please fix me
        #             print("please fix")
        #         else:
        #             if match_case.get() == 0:
        #                 if letter.upper() in search_entry.get().upper():
        #                     file_contents.tag_add("match", (str(line_num) + "." + str(letter_num)))
        #                     file_contents.tag_config("match", background="yellow")
        #                     num_of_matches += 1
        #             else:
        #                 if letter in search_entry.get():
        #                     file_contents.tag_add("match", (str(line_num) + "." + str(letter_num)))
        #                     file_contents.tag_config("match", background="yellow")
        #                     num_of_matches += 1
        #         letter_num += 1
        #     line_num += 1
        matches_found_label.config(text=("Matches found: " + str(num_of_matches)))

# Create main window
window = tk.Tk()
window.title("Text Search")

match_case = IntVar()

# Master frame to hold two sub frames
content = tk.Frame(window, height="600", width="800")
content.pack(expand="true", fill="both")

# Frame that contains the file's text
text_frame = tk.Frame(content, padx="10", pady="10")
text_frame.place(relwidth="0.5", relheight="1")

file_contents = tk.Text(text_frame, font=("Helvetica", 10))
file_contents.place(relwidth="1", relheight="1")

# Frame that contains the file dialog as well as the search options
options_frame = tk.Frame(content, padx="10", pady="10")
options_frame.place(anchor="ne", relx="1", relwidth="0.5", relheight="1")

file_button = tk.Button(options_frame, text="Open File", command=open_file_dialog)
file_button.pack(pady="20")

file_entry = tk.Entry(options_frame, width="50")
file_entry.pack()

# Extra label to help make the UI clearer
format_label_one = tk.Label(options_frame, text="-------------------------------------------------------")
format_label_one.pack(pady="50")

search_button = tk.Button(options_frame, text="Search", command=search_for_text)
search_button.pack(pady="20")

search_entry = tk.Entry(options_frame, width="20")
search_entry.pack()

match_case_checkbox = tk.Checkbutton(options_frame, text="Match Case?", variable=match_case)
match_case_checkbox.pack()

# Extra label to help make the UI clearer
format_label_two = tk.Label(options_frame, text="-------------------------------------------------------")
format_label_two.pack(pady="50")

matches_found_label = tk.Label(options_frame, text=("Matches found: " + str(num_of_matches)))
matches_found_label.pack(pady="20")

# Run the program
window.mainloop()
