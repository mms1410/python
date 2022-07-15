#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:40:16 2022

@author: svenmaurice
"""

from tkinter import filedialog
from tkinter import messagebox
import os
import zipfile
import tkinter as tk
foldername_unzipped = "unzipped"


root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

if os.path.isdir(os.path.join(folder_selected, foldername_unzipped)):
    msg = messagebox.askquestion("Folder 'unziped' already exists.\n Redo?")
    if not msg:
        exit()
    else:
        os.rmdir(os.path.join(folder_selected, foldername_unzipped))

    
files = [file for file in os.listdir(folder_selected)]
zipfiles = [file for file in os.listdir(folder_selected) if zipfile.is_zipfile(os.path.join(folder_selected,file))]
os.mkdir(os.path.join(folder_selected, foldername_unzipped))
folder_extract = os.path.join(folder_selected, foldername_unzipped)

for file in files:
    folder_fullpath = os.path.join(folder_selected, file)
    with zipfile.ZipFile(folder_fullpath, "r") as zfile:
        zfile.extractall(folder_extract)