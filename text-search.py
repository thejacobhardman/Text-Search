# Jacob Hardman
# CS 350
# Professor Christopher Harris
# 8/26/2022

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import sys, ctypes

# This code fixes the blurry text that tkinter has when being used on Windows. I got this solution from Stack Overflow:
# https://stackoverflow.com/questions/36514158/tkinter-output-blurry-for-icon-and-text-python-2-7/43033405
if __name__ == "__main__":   
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

num_of_matches = 0
background_colors = ["Yellow", "Red", "Blue", "Orange", "Green", "Purple"]

def open_file_dialog():
    path = filedialog.askopenfile(initialdir="/documents", title="Select File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    if path:
        file_entry.delete(0, "end")
        file_entry.insert(0, path.name.format())
        file_contents.delete("1.0", "end")
        file_contents.insert("1.0", path.read())

def change_highlight_color(selection):
    highlight_color = selection
    color_picker.config(bg=highlight_color)
    file_contents.tag_config("match", background=highlight_color)

# Had to add this method to trigger the search otherwise tkinter threw a fit and would not load the window.
def trigger_search():
    file_contents.tag_delete("match")
    file_contents.tag_config("match", background=highlight_color.get())
    search(file_contents, search_entry.get(), "match")

# I was completely stuck on how to correctly filter and highlight the text using tkinter so I found and incorporated this solution:
# https://stackoverflow.com/questions/17829713/tkinter-highlight-colour-specific-lines-of-text-based-on-a-keyword
def search(text_widget, keyword, tag):
    global num_of_matches
    num_of_matches = 0
    pos = '1.0'
    while True:
        if match_case.get() == 0:
            idx = text_widget.search(keyword, pos, END, nocase=1)
        else:
            idx = text_widget.search(keyword, pos, END)
        if not idx:
            break
        pos = '{}+{}c'.format(idx, len(keyword))
        text_widget.tag_add(tag, idx, pos)
        num_of_matches += 1
    matches_found_label.config(text=("Matches found: " + str(num_of_matches)))

# Create main window
window = tk.Tk()
window.title("Text Search")

match_case = IntVar()
highlight_color = StringVar()
highlight_color.set(background_colors[0])

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
format_label_one.pack(pady="30")

search_entry = tk.Entry(options_frame, width="20")

search_button = tk.Button(options_frame, text="Search", command=trigger_search)

search_button.pack(pady="20")
search_entry.pack()

match_case_checkbox = tk.Checkbutton(options_frame, text="Match Case?", variable=match_case)
match_case_checkbox.pack()

color_label = tk.Label(options_frame, text="Highlight Color:")
color_label.pack(pady="10")

color_picker = tk.OptionMenu(options_frame, highlight_color, *background_colors, command=change_highlight_color)
color_picker.config(bg=highlight_color.get(), width="10", height="2")
color_picker.pack()

# Extra label to help make the UI clearer
format_label_two = tk.Label(options_frame, text="-------------------------------------------------------")
format_label_two.pack(pady="30")

matches_found_label = tk.Label(options_frame, text=("Matches found: " + str(num_of_matches)))
matches_found_label.pack()

# Run the program
window.mainloop()
