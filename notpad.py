import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    def __init__(self, root):
        self.root = root

        # set the window
        self.width = 600
        self.height = 400
        self.root.title("Astro_Notepad")
        self.text_area = Text(root)
        self.menu_bar = Menu(root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu = Menu(self.menu_bar, tearoff=0)

        # Scrollbar
        self.scrollbar = Scrollbar(self.text_area)
        self.file = None

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # For left alling
        left = (screen_width / 2) - (self.width / 2)

        # For top alling
        top = (screen_height / 2) - (self.height / 2)

        # window geometry
        self.root.geometry("%dx%d+%d+%d" % (self.width,
                                            self.height,
                                            left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.text_area.grid(sticky=N + E + S + W)

        # To open new file
        self.file_menu.add_command(label="New",
                                   command=self.new_file, font=("times to new roman", 10, "italic"))

        # To open a already existing file
        self.file_menu.add_command(label="Open",
                                   command=self.open_file, font=("times to new roman", 10, "italic"))

        # To save current file
        self.file_menu.add_command(label="Save",
                                   command=self.save_file, font=("times to new roman", 10, "italic"))

        # To create a line in the dialog
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",
                                   command=self.exit_application, font=("times to new roman", 10, "italic"))
        self.menu_bar.add_cascade(label="File",
                                  menu=self.file_menu)

        # To give a feature of cut
        self.edit_menu.add_command(label="Cut",
                                   command=self.cut, font=("times to new roman", 10, "italic"))

        # to give a feature of copy
        self.edit_menu.add_command(label="Copy",
                                   command=self.copy, font=("times to new roman", 10, "italic"))

        # To give a feature of paste
        self.edit_menu.add_command(label="Paste",
                                   command=self.paste, font=("times to new roman", 10, "italic"))

        # To give a feature of editing
        self.menu_bar.add_cascade(label="Edit",
                                  menu=self.edit_menu)

        # To create a feature of description of the notepad
        self.help_menu.add_command(label="About Notepad",
                                   command=self.show_about, font=("times to new roman", 10, "italic"))
        self.menu_bar.add_cascade(label="Help",
                                  menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def exit_application(self):
        self.root.destroy()

    def show_about(self):
        showinfo("Astro_Notepad", "Astro_Faruk")

    def open_file(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                               ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file + "Astro_Notepad"))
            self.text_area.delete(1.0, END)

            file = open(self.file, 'r')
            self.text_area.insert(1.0, file.read())
            file.close()

    def new_file(self):
        self.root.title("AStro_Faruk")
        self.file = None
        self.text_area.delete(1.0, END)

    def save_file(self):

        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                          defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, 'w')
                file.write(self.text_area.get(1.0, END))
                file.close()

                # Change the window title
                self.root.title(os.path.basename(self.file) + " - Notepad")

        else:
            file = open(self.file, "w")
            file.write(self.text_area.get(1.0, END))
            file.close()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")


# creating tkinter container
root = Tk()
# pass the root through MusicPlayer class
Notepad(root)
# root window looping
root.mainloop()








