from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class Calculator:
    history = []

    def __init__(self):
        # screen set up
        self.root = Tk()
        self.root.geometry("500x800")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=11)
        self.root.rowconfigure(0, weight=1)
        # create a container widget for the keyboard and displays
        self.keyboard = ttk.Frame(self.root, height=531)
        self.keyboard.grid(row=2, column=0, sticky=NSEW, columnspan=2)
        self.display = ttk.Frame(self.root)
        self.display.grid(row=1, column=0, sticky=NE, padx=(0, 15), pady=(30, 0), columnspan=2)
        self.small_display = ttk.Frame(self.root, height=60)
        self.small_display.grid(row=0, column=0, sticky=SE, columnspan=2)
        # create the history button
        history_img = ImageTk.PhotoImage(Image.open("/home/jgruenbaum/Downloads/my-logo.png").resize((20, 20)))
        self.history_number = 0 # if history number == 0 - then we are on the keyboard layout, if its == 1 then we are on the history layout
        self.history_button = Button(image=history_img, command=self.show_history, borderwidth=0)
        self.history_button.grid(row=0, column=1, sticky=E, padx=(0, 15))
        # create the small text display
        self.small_text = ttk.Label(self.small_display, text="", font="Verdana 14")
        self.small_text.grid(row=0, column=0, sticky="NSEW", pady=(30, 0), padx=(0, 5))
        # create the text display
        self.text = ttk.Label(self.display, text="", font="Verdana 36")
        self.text.grid(row=0, column=0, sticky="NSEW", pady=(0, 50))
        self.show_keyboard()

        self.root.mainloop()

    def show_keyboard(self):
        print(self.keyboard.winfo_height()) # HERE IT IS 529
        # create the buttons...
        ttk.Button(self.keyboard, text="%", command=lambda: self.calculate("%")).grid(row=0, column=0, sticky="NSEW")
        ttk.Button(self.keyboard, text="CE", command=lambda: self.add_text(symbol="CE")).grid(row=0, column=1, sticky="NSEW")
        ttk.Button(self.keyboard, text="C", command=lambda: self.add_text(symbol="C")).grid(row=0, column=2, sticky="NSEW")
        ttk.Button(self.keyboard, text="←", command=lambda: self.add_text(symbol="←")).grid(row=0, column=3, sticky="NSEW")
        ttk.Button(self.keyboard, text="1/x", command=lambda: self.fast_calculate("1/x")).grid(row=1, column=0, sticky="NSEW")
        ttk.Button(self.keyboard, text="x²", command=lambda: self.fast_calculate("x²")).grid(row=1, column=1, sticky="NSEW")
        ttk.Button(self.keyboard, text="√x", command=lambda: self.fast_calculate("√x")).grid(row=1, column=2, sticky="NSEW")
        ttk.Button(self.keyboard, text="÷", command=lambda: self.add_text(symbol="÷")).grid(row=1, column=3, sticky="NSEW")
        ttk.Button(self.keyboard, text="7", command=lambda: self.add_text(7)).grid(row=2, column=0, sticky="NSEW")
        ttk.Button(self.keyboard, text="8", command=lambda: self.add_text(8)).grid(row=2, column=1, sticky="NSEW")
        ttk.Button(self.keyboard, text="9", command=lambda: self.add_text(9)).grid(row=2, column=2, sticky="NSEW")
        ttk.Button(self.keyboard, text="X", command=lambda: self.add_text(symbol="X")).grid(row=2, column=3, sticky="NSEW")
        ttk.Button(self.keyboard, text="4", command=lambda: self.add_text(4)).grid(row=3, column=0, sticky="NSEW")
        ttk.Button(self.keyboard, text="5", command=lambda: self.add_text(5)).grid(row=3, column=1, sticky="NSEW")
        ttk.Button(self.keyboard, text="6", command=lambda: self.add_text(6)).grid(row=3, column=2, sticky="NSEW")
        ttk.Button(self.keyboard, text="-", command=lambda: self.add_text(symbol="-")).grid(row=3, column=3, sticky="NSEW")
        ttk.Button(self.keyboard, text="1", command=lambda: self.add_text(1)).grid(row=4, column=0, sticky="NSEW")
        ttk.Button(self.keyboard, text="2", command=lambda: self.add_text(2)).grid(row=4, column=1, sticky="NSEW")
        ttk.Button(self.keyboard, text="3", command=lambda: self.add_text(3)).grid(row=4, column=2, sticky="NSEW")
        ttk.Button(self.keyboard, text="+", command=lambda: self.add_text("+")).grid(row=4, column=3, sticky="NSEW")
        ttk.Button(self.keyboard, text="+/-", command=lambda: self.add_text("+/-")).grid(row=5, column=0, sticky="NSEW")
        ttk.Button(self.keyboard, text="0", command=lambda: self.add_text(0)).grid(row=5, column=1, sticky="NSEW")
        ttk.Button(self.keyboard, text=".", command=lambda: self.add_text(".")).grid(row=5, column=2, sticky="NSEW")
        ttk.Button(self.keyboard, text="=", command=lambda: self.calculate("=")).grid(row=5, column=3, sticky="NSEW")

        for i in range(6):
            self.keyboard.rowconfigure(i, weight=1)
        for i in range(4):
            self.keyboard.columnconfigure(i, weight=1)

    def show_history(self):
        print(self.keyboard.winfo_height()) # HERE IT IS 531
        print(len(self.history))
        
        for child in self.keyboard.winfo_children():
            child.destroy()

        if self.history_number == 0:
            self.t = Text(self.keyboard, font="Verdana 16", height=21)
            self.line_height = self.keyboard.winfo_height() / 21

            if len(self.history) > 0:
                # check if we need to delete the first calculations ( won't add scrollbox )
                if len(self.history) > 21:
                    del self.history[0]
                h = "\n".join(self.history)
                self.t.insert(END, h)

            self.root.rowconfigure(2, weight=0)
            self.t.grid(row=0, column=0) # this is here because I suck at coding :)
            self.history_number += 1
        else:
            self.root.rowconfigure(2, weight=11)
            self.show_keyboard()
            self.history_number -= 1


c = Calculator()

