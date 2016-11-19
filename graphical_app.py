import tkinter


class App():
    def __init__(self):
        self.root = tkinter.Tk()
        button = tkinter.Button(self.root,
                                text='root quit',
                                command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()