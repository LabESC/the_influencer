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
        top_frame = tk.Frame(self)

        top_frame.pack()
        center_frame = tk.Frame(self)
        center_frame.config(pady=50)
        center_frame.pack()
        bottom_frame = tk.Frame(self)
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


    def start_analysis(self, page):
        location = self.text_directory_location.get(1.0, 'end-1c')
        if not verify_directory_existence(location):
            print(location)
            print("location invalida")
        else:
            if verify_directory_existence(os.path.join(location, "ecosystem_gexf")):
                remove_directory_structure(location)
            else:
                create_directory_structure(location)
                page.show()

class results_page(pages):
    def __init__(self, *args, **kwargs):
        pages.__init__(self, *args, **kwargs)
        top_frame = tk.Frame()
        top_frame.pack()

        title_label = tk.Label(top_frame, text="The Influencer")
        title_label.config(font=("Times New Roman", 44))
        title_label.pack()

        center_frame = tk.Frame()
        center_frame.config(pady=20)
        center_frame.pack()

        text_message = tk.Label(center_frame, text="Your analysis is done!")
        text_message.pack()

        show_ecosystem_button = tk.Button(center_frame, text="Show my Ecosystem's Influencer!")
        show_ecosystem_button.pack()

        bottom_frame = tk.Frame()
        bottom_frame.config(pady=50)
        bottom_frame.pack()

        suggestion_for_project = tk.Label(bottom_frame, text="Or you could see the influencer for a specific project...")
        suggestion_for_project.pack()

        choice = tk.StringVar(self)
        choices = {"project1", "project2", "project3"}
        choice.set("project1")
        ecosystem_options = tk.OptionMenu(bottom_frame, choice, *choices)
        ecosystem_options.pack()

        show_project_button = tk.Button(bottom_frame, text="Show my Project's Influencer!")
        show_project_button.pack()

class main_page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.home_page_frame = home_page(self)
        self.results_page_frame = results_page(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.home_page_frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.results_page_frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.home_page_frame.show()
