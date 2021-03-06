try:
	import os.path
	import tkinter
	from tkinter import *
	from tkinter import filedialog
	from tkinter import messagebox
	from tkinter.filedialog import askopenfilename
except:
	print("package not found")

## ISSUES ##

# shortcuts work but not ctrl+shift+s or save as ;/
# tabs ?!

## vars ##

ide_name = "Simple IDE"
varfile = ""

## themes ##

# plain - 	white bg	black fg
# dark - 	black bg 	white fg
# hacker - 	black bg 	green fg

# Colors

lightgreen = "#43FF00"

## themes functions ##

def plain_theme():
	global textarea
	print("plain_theme used")
	textarea.configure(bg="white", fg="black", insertbackground="black")

def dark_theme():
	global textarea
	print("dark_theme used")
	textarea.configure(bg="black", fg="white", insertbackground="white")

def hacker_theme():
	global textarea
	print("hacker_theme used")
	textarea.configure(bg="black", fg=lightgreen, insertbackground=lightgreen)

## functions ##

def saveasdoc(event=""):
	print("saveas file")
	global textarea, varfile
	text = textarea.get("1.0","end-1c")
	location = filedialog.asksaveasfilename()
	varfile = location
	file = open(location, "w+")
	file.write(text)
	file.close()
	root.title(location + " " + ide_name)

def save(event=""):
	print("save file")
	global textarea, varfile
	text = textarea.get("1.0","end-1c")
	try:
		file = open(varfile, "w+")
	except:
		tkinter.messagebox.showinfo(title="Error",message="Did you save this file?")
	file.write(text)
	file.close()

def openfile(event=""):
	global textarea, varfile
	print("open file")
	file = askopenfilename(parent=root)
	f = open(file)
	f = f.read()

	textarea.delete(1.0, END)
	textarea.insert(END, f)

	varfile = file
	root.title(file + " " + ide_name)

def newfile(event=""):
	print("new file")

def key(event):
	print ("pressed",repr(event.char))

def callback(event):
	root.focus_set()
	print ("clicked at", event.x, event.y)

## gui ##

root = Tk()
root.title("*unsaved %s" % ide_name)

# shortkeys
root.bind("<Key>", key)
root.bind("<Control-Shift-s>", saveasdoc)
root.bind("<Control-s>", save)
root.bind("<Control-o>", openfile)
root.bind("<Control-n>", newfile)

# creating our menu

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=newfile, accelerator="Ctrl+N")
file_menu.add_command(label="Save", command=save, accelerator="Ctrl+S")
file_menu.add_command(label="Open", command=openfile, accelerator="Ctrl+O")
file_menu.add_command(label="SaveAs", command=saveasdoc, accelerator="Ctrl+Shift+S")

theme_menu = Menu(menu)
menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Plain", command=plain_theme)
theme_menu.add_command(label="Dark", command=dark_theme)
theme_menu.add_command(label="Hacker", command=hacker_theme)

## defines the text area

textarea = Text(root)
textarea.pack(fill="both", expand=True)

mainloop()
