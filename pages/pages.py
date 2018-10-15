from tkinter import *
from tkinter import filedialog


class pages:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x300")
        self.window.title("The Influencer")
        self.home_frame = Frame(self.window)
        self.home_frame.pack()
        self.home_page()
        self.window.mainloop()

    def home_page(self):
        top_frame = Frame(self.home_frame)

        top_frame.pack()
        center_frame = Frame(self.window)
        center_frame.config(pady=50)
        center_frame.pack()
        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM)
        title_label = Label(top_frame, text="The Influencer")
        title_label.config(font=("Times New Roman", 44))
        title_label.pack()
        instructions_label = Label(center_frame, text="Welcome to The Influencer!\n In order to start your analysis, "
                                                      "browse for your SECO's .csv directory in your computer:")
        instructions_label.pack()
        directory_search_button = Button(center_frame, text="Directory search", command=self.directory_search_button_function)
        directory_search_button.pack()


    def directory_search_button_function(self):
        name = filedialog.askdirectory()
        print(name)

