from tkinter import *
from tkinter import filedialog
from assistants.directories import *
import os


class pages():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("550x350")
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
                                                      "browse for your SECO's .csv files location:")
        instructions_label.pack()
        directory_search_button = Button(center_frame, text="Find", command=self.directory_search_button_function)
        directory_search_button.pack()
        confirmation_label = Label(center_frame, text="Confirm that this is your directory location:")
        confirmation_label.pack()
        self.text_directory_location = Text(center_frame, height=2, width=50, )
        self.text_directory_location.config(state=DISABLED)
        self.text_directory_location.pack()
        analysis_button = Button(center_frame, text="Start Analysis!", command=self.start_analysis)
        analysis_button.pack()


    def directory_search_button_function(self):
        location = filedialog.askdirectory()
        self.text_directory_location.config(state=NORMAL)
        self.text_directory_location.delete(1.0,END)
        self.text_directory_location.insert(END, location)
        self.text_directory_location.config(state=DISABLED)


    def start_analysis(self):
        location = self.text_directory_location.get(1.0, 'end-1c')
        if not verify_directory_existence(location):
            print(location)
            print("location invalida")
        else:
            if verify_directory_existence(os.path.join(location, "ecosystem_gexf")):
                remove_directory_structure(location)
            else:
                create_directory_structure(location)


class home_page:
    def __init__(self):
        return 0

class results_page:
    def __init__(self):
        return 0
