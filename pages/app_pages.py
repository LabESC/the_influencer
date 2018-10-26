import tkinter as tk
from tkinter import filedialog
from assistants.directories import *
import os


class pages(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class home_page(pages):
    def __init__(self, *args, **kwargs):
        pages.__init__(self, *args, **kwargs)
        top_frame = tk.Frame()

        top_frame.pack()
        center_frame = tk.Frame()
        center_frame.config(pady=50)
        center_frame.pack()
        bottom_frame = tk.Frame()
        bottom_frame.pack(side="bottom")
        title_label = tk.Label(top_frame, text="The Influencer")
        title_label.config(font=("Times New Roman", 44))
        title_label.pack()
        instructions_label = tk.Label(center_frame, text="Welcome to The Influencer!\n In order to start your analysis, "
                                                      "browse for your SECO's .csv files location:")
        instructions_label.pack()
        directory_search_button = tk.Button(center_frame, text="Find", command=self.directory_search_button_function)
        directory_search_button.pack()
        confirmation_label = tk.Label(center_frame, text="Confirm that this is your directory location:")
        confirmation_label.pack()
        self.text_directory_location = tk.Text(center_frame, height=2, width=50, )
        self.text_directory_location.config(state="disabled")
        self.text_directory_location.pack()
        analysis_button = tk.Button(center_frame, text="Start Analysis!", command=self.start_analysis)
        analysis_button.pack()

    def directory_search_button_function(self):
        location = filedialog.askdirectory()
        self.text_directory_location.config(state="normal")
        self.text_directory_location.delete(1.0,"end")
        self.text_directory_location.insert("end", location)
        self.text_directory_location.config(state="disabled")


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

class results_page(pages):
    def __init__(self, *args, **kwargs):
        pages.__init__(self, *args, **kwargs)

class main_page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        home_page_frame = home_page(self)
        results_page_frame = results_page(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        home_page_frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        results_page_frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        home_page_frame.show()