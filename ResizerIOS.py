from tkinter import *
from tkinter import filedialog
from ttkthemes import ThemedTk, THEMES
import os
from PIL import Image

filePath = ""
fileName = ""
fileExtension = ""
savePath = ""

sizes = [
    40,
    60,
    58,
    87,
    80,
    120,
    180,
    20,
    29,
    76,
    152,
    167,
    1024
]

def resize(width):

    print("FileName", fileName)
    print("FileExtension", fileExtension)
    print("FilePath", filePath)
    print("SavePath", savePath)

    im = Image.open(filePath)

    x, y = im.size
    if x!=y: return

    resizedImage = im.resize((int(width), int(width)))

    resizedImage.save(f"{savePath}/{fileName}{width}{fileExtension}")

def openFile():
    global filePath
    global fileName
    global fileExtension

    filePath = filedialog.askopenfilename(filetypes =[('*.jpg', '*.png')])
    fileName = os.path.basename(filePath)
    fileExtension = os.path.splitext(filePath)[1]
    if filePath: saveFile.configure(state=ACTIVE)
def saveFile():
    global savePath
    savePath = filedialog.askdirectory()

    if savePath == "": return

    for size in sizes:
        resize(size)
    window.destroy()

window = ThemedTk(themebg=True)
window.set_theme('blue')
window.title("Resizer for IOS development")
window.minsize(800, 500)

openFile = Button(text='Open File', height=10, width=50, command=openFile)
openFile.pack(padx=10, pady=10)
saveFile = Button(text='Save File', height=10, width=50, state=DISABLED, command=saveFile)
saveFile.pack(padx=10, pady=10)
window.mainloop()