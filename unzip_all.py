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
import shutil
import tkinter as tk
foldername_unzipped = "unzipped"


root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

if os.path.isdir(os.path.join(folder_selected, foldername_unzipped)):
    msg = messagebox.askquestion(message = "Folder 'unziped' already exists.\n Redo?")
    if not msg:
        exit()
    else:
        msg = messagebox.askyesnocancel(message = "unzipped folder will be deleted.\n Do you want to continue?")
        if msg:
            shutil.rmtree(os.path.join(folder_selected, foldername_unzipped))
        else:
            exit()

    
files = [file for file in os.listdir(folder_selected)]
zipfiles = [file for file in os.listdir(folder_selected) if zipfile.is_zipfile(os.path.join(folder_selected,file))]
os.mkdir(os.path.join(folder_selected, foldername_unzipped))
folder_extract = os.path.join(folder_selected, foldername_unzipped)

for file in files:
    folder_fullpath = os.path.join(folder_selected, file)
    filename_unzipped = os.path.splitext(file)[0]
    filename_unzipped = os.path.join(folder_extract, filename_unzipped)
    os.mkdir(filename_unzipped)
    
    with zipfile.ZipFile(os.path.join(folder_selected, file)) as zfile:
        zfile.extractall(filename_unzipped)