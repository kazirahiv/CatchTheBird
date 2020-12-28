import tkinter.font as tkFont
from tkinter import *
from MoveBirdThread import MoveBirdThread
from TimerThread import TimerThread
from Bird import Bird
from PIL import Image, ImageTk

class HomeView:
    def __init__(self, root):
        self.root = root
        self.root.title('Catch the bird')
        self.root.geometry('860x600')
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.left_frame = Frame(self.root, width=200, height=400)
        self.right_frame = Frame(self.root, width=650, height=580, highlightthickness=1, highlightbackground="black")
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)

        self.timer_thread = TimerThread(end_game=self.close)
        bird = Bird(root=self.right_frame, counter_thread=self.timer_thread, close_game=self.close)
        move_bird_thread = MoveBirdThread(callback=bird.construct_btn, level_up = bird.level_up)

        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        Label(self.left_frame, text="Score Board", font=fontStyle).grid(row=0, column=0, padx=5, pady=5)
        Label(self.left_frame, textvariable=str(bird.kills), font=fontStyle).grid(row=1, column=0, padx=5, pady=5)
        Label(self.left_frame, text="👣 Level", font=fontStyle).grid(row=2, column=0, padx=5, pady=5)
        Label(self.left_frame, textvariable=str(bird.level), font=fontStyle).grid(row=3, column=0, padx=5, pady=5)
        move_bird_thread.start()
        self.timer_thread.start()

    def close(self, won=False):
        if won:
            self.timer_thread.won()
        self.replace_left_frame(won=won)
        self.replace_right_frame(won=won)

    def replace_right_frame(self, won):
        self.right_frame.destroy()
        self.right_frame = Frame(self.root, width=650, height=580, highlightthickness=1, highlightbackground="black")
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)
        dir = 'images/dead_bird.png'
        if won:
            dir = './images/won.png'
        img = Image.open(dir)
        self.dead = self.resize_Image(image=img, maxsize=[400,400])
        self.a = Button(master=self.right_frame,image=self.dead,
                           borderwidth=0,
                           highlightthickness=0,)
        self.a.place(x=150, y=150)

    def replace_left_frame(self, won):
        self.left_frame.destroy()
        self.left_frame = Frame(self.root, width=200, height=400)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        stat = "Game Over"
        if won:
            stat = 'Won !!!!'
        Label(self.left_frame, text=stat, font=fontStyle).grid(row=0, column=0, padx=5, pady=5)

    def resize_Image(self, image, maxsize):
        r1 = image.size[0] / maxsize[0]
        r2 = image.size[1] / maxsize[1]
        ratio = max(r1, r2)
        new_size = (int(image.size[0] / ratio), int(image.size[1] / ratio))
        return ImageTk.PhotoImage(image.resize(new_size, Image.ANTIALIAS))