from PIL import Image, ImageTk
from tkinter import Button, IntVar, StringVar
from random import randrange


class Bird():
    def __init__(self, root, counter_thread, close_game):
        self.close_game = close_game
        self.counter_thread = counter_thread
        self.kills = IntVar()
        self.root = root
        self.window_width, self.window_height = root.winfo_reqheight(), root.winfo_reqwidth()
        self.bug_size_x, self.bug_size_y = 200, 200
        self.level = IntVar(value=1)
        self.turn_level_up = False
        self.construct_btn()

    def construct_btn(self):
        b_position_x = randrange(self.window_height - 200)
        b_position_y = randrange(self.window_width - 200)
        try:
            img = Image.open('images/birdOne.png')
            if self.level.get() == 2:
                img = Image.open('images/birdTwo.png')
            elif self.level.get() == 3:
                img = Image.open('images/birdThree.png')
            elif self.level.get() == 4:
                img = Image.open('./images/Boss.png')
            elif self.level.get() == 5:
                self.close_game(won=True)
            self.bug_img = self.resize_Image(image=img, maxsize=[self.bug_size_x, self.bug_size_y])
        except IOError as err:
            print(err)
        try:
            self.btn0 = Button(master=self.root,
                               image=self.bug_img,
                               borderwidth=0,
                               highlightthickness=0,
                               command=self.bug_click_callback)
            self.btn0.place(x=b_position_x, y=b_position_y)
        except:
            pass

    def level_up(self):
        self.bug_size_x, self.bug_size_y = 200, 200
        self.level.set(self.level.get() + 1)
        self.construct_btn()
        self.turn_level_up = False

    def bug_click_callback(self):
        self.kills.set(self.kills.get() + 1)
        self.bug_size_x, self.bug_size_y = self.bug_size_x - 20, self.bug_size_y - 20
        if self.level.get() < 5:
            self.counter_thread.reset()

    def resize_Image(self, image, maxsize):
        r1 = image.size[0] / maxsize[0]
        r2 = image.size[1] / maxsize[1]
        ratio = max(r1, r2)
        new_size = (int(image.size[0] / ratio), int(image.size[1] / ratio))
        return ImageTk.PhotoImage(image.resize(new_size, Image.ANTIALIAS))
