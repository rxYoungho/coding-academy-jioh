import tkinter.ttk as ttk 
import tkinter.messagebox as msgbox

from tkinter import *
from tkinter import filedialog
from PIL import Image 
import os

from click import progressbar

root = Tk()
root.title("Merge Images")

# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="Select image to merge", \
        filetypes=(("PNG File", "*.png"), ("All Files", "*")), \
        initialdir=r"")
    
    for file in files:
        list_file.insert(END, file)
    # 사용자가 선택한 파일 목록

# DELETE
def del_file():
    for i in reversed(list_file.curselection()):
        list_file.delete(i)

# Directory Path 
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

def start():
    print("Width:", cmb_width.get())
    print("Space:", cmb_space.get())
    print("Format:", cmb_format)

    if list_file.size() == 0:
        msgbox.showwarning("WARING!!🔥: Please add at least one image.")
        return
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("WARING!!🔥: Please select the destination directory path.")
    merge()

def merge():
    pass

# file frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # give some sapce

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add Files", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete File", command=del_file)
btn_del_file.pack(side="right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Path Frame
path_frame = LabelFrame(root, text="Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) 

# Directory button
btn_dest_path = Button(path_frame, text="Directory", width=7, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option Frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# Width Option
lbl_width = Label(frame_option, text="Width", width=5)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=8)
cmb_width.current(0) #
cmb_width.pack(side="left", padx=5, pady=5)

# Space Option
lbl_space = Label(frame_option, text="Space", width=5)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["None", "Small", "Medium", "Large"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=8)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# File Format Option
lbl_format = Label(frame_option, text="Format", width=5)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP", "JPEG"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress Bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Merge and Start Button
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_merge = Button(frame_run, padx=5, pady=5, text="Merge", width=12, command=start)
btn_merge.pack(side="right", padx=5, pady=5)

root.resizable(False, False) # x, y 
root.mainloop()