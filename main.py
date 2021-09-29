import os
import glob
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_button(cmd=self.getFolder)
        self.create_button(cmd=self.save, TXT='Salvar')
        self.quit = Button(self, text="QUIT", fg="red",
                           command=self.master.destroy)
        self.quit.pack()

        self.folderImgs = ''
        self.imgs = []
        self.folderOutput = ''

        frame1 = Frame(self, width=200, height=200, bd=4, relief="ridge")
        frame2 = Frame(self,  width=200, height=200, bd=4, relief="ridge")
        frame1.pack(side=LEFT, fill=BOTH, expand=1, anchor=N)
        frame2.pack(side=RIGHT, fill=BOTH, expand=1, anchor=N)

        self.x = self.create_entry(main=frame2)
        self.y = self.create_entry(main=frame2)
        self.scrollbar = Scrollbar(frame1)

        self. scrollbar.pack(side=LEFT)
        self. photos = Listbox(
            frame1, yscrollcommand=self.scrollbar.set, height=200)
        self.photos.pack(side=LEFT, fill=BOTH)
        self.scrollbar.config(command=self.photos.yview)

    def create_button(self, TXT="Escolher pasta", cmd=lambda x: (x), side="top"):
        btn = Button(self)
        btn["text"] = TXT
        btn["command"] = cmd
        btn.pack(side=side)

        return btn

    def onX(s):
        print(s)

    def create_entry(self, TXT="100", cmd=lambda x: (x), main=None):
        if main:
            text_fild = Entry(main)
            # text_fild["text"] = TXT
            # text_fild["command"] = cmd
        else:
            text_fild = Entry(self)
            pass
        text_fild.insert(0, TXT)
        text_fild.bind("<Button-1>", cmd)

        text_fild.pack(pady=10)
        text_fild.pack(side=RIGHT, fill=X)

        return text_fild

    def say_hi(self):
        print("hi there, everyone!")

    def getFolder(self):
        self.folderImgs = filedialog.askdirectory(
            title='Pastas onde esta as imgs')
        self.folderOutput = filedialog.askdirectory(
            title='Onde Salvar as Imgs?')
        self.loadFolders()

    def loadFolders(self):

        imgs = os.listdir(self.folderImgs)
        imgslist = []
        extensions = ['jpg', 'jpeg', 'png']
        size = 128, 128

        for img in imgs:
            separete = img.split('.')
            try:
                for ex in extensions:
                    image = Image.open(self.folderImgs+'/'+img)

                    imgslist.append(image)
                    self.imgs.append(image)

            except:
                pass

        self.imgslist = imgslist
        self.draw()

    def displayImg(self, image):
        photo = ImageTk.PhotoImage(image)
        newPhoto_label = Label(image=photo)
        newPhoto_label.pack()

        # keep references!
        self. photos.insert(END,  image.filename.split('/')[-1])

    def draw(self):
        imgs = self.imgslist

        for img in imgs:
            self.displayImg(img)

    def save(self):
        size = int(self.x.get()), int(self.y.get())

        for img in self.imgslist:
            nameImg = (img.filename.split('/')[-1])
            # img = img.resize(size)
            img.thumbnail(size, Image.ANTIALIAS)
            img.save(self.folderOutput+'/'+nameImg)
        # def displayImg(img):
        #     image = Image.open(img)
        #     photo = ImageTk.PhotoImage(image)
        #     photos.append(photo)  # keep references!
        #     newPhoto_label = Label(image=photo)
        #     newPhoto_label.pack()

        # root = Tk()
        # root.withdraw()
        # root.attributes('-topmost', True)

        # # file_path = filedialog.askdirectory()
        # root.geometry("800x600")
        # photos = []
        # # print(file_path)

        # def displayImg(img):
        #     image = Image.open(img)
        #     photo = ImageTk.PhotoImage(image)
        #     photos.append(photo)  # keep references!
        #     newPhoto_label = Label(image=photo)
        #     newPhoto_label.pack()

        # for file in glob.glob("*.jpg"):
        #     displayImg(file)
        #     print(file)

        # root.mainloop()


root = Tk()
root.geometry("500x200")

app = Application(master=root)
app.mainloop()
