import tkinter as tk
from tkinter import *
from tkinter import filedialog
from assistants.directories import *
import os


class base_frame(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError


class results_frame(base_frame):
    def create_widgets(self):
        title_label = tk.Label(self, text="The Influencer")
        title_label.config(font=("Times New Roman", 44))
        title_label.grid(padx=100)

        text_message = tk.Label(self, text="Your analysis is done!")
        text_message.grid(pady=20)

        show_ecosystem_button = tk.Button(self, text="Show my Ecosystem's Influencer!")
        show_ecosystem_button.grid()

        suggestion_for_project = tk.Label(self,
                                          text="Or you could see the influencer for a specific project...")
        suggestion_for_project.grid(pady=10)

        choice = tk.StringVar(self)
        choices = {"project1", "project2", "project3"}
        choice.set("project1")

        ecosystem_options = tk.OptionMenu(self, choice, *choices)
        ecosystem_options.grid()

        show_project_button = tk.Button(self, text="Show my Project's Influencer!")
        show_project_button.grid()

        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(home_frame),
                                    padx=5,
                                    pady=5,
                                    text="Home")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)


class home_frame(base_frame):
    def create_widgets(self):
        title_label = tk.Label(self, text="The Influencer")
        title_label.config(font=("Times New Roman", 44))
        title_label.grid(padx=100)

        instructions_label = tk.Label(self,
                                      text="Welcome to The Influencer!\n In order to start your analysis,\n "
                                           "browse for your SECO's .csv files location:", width=30)
        instructions_label.grid(pady=20)

        directory_search_button = tk.Button(self, text="Find", command=self.directory_search_button_function)
        directory_search_button.grid()

        confirmation_label = tk.Label(self, text="Confirm that this is your directory location:")
        confirmation_label.grid()

        self.text_directory_location = tk.Text(self, height=2, width=30, )
        self.text_directory_location.config(state="disabled")
        self.text_directory_location.grid(padx=30)

        analysis_button = tk.Button(self, text="Start Analysis!", command=self.start_analysis)
        analysis_button.grid()

        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(results_frame),
                                    padx=5,
                                    pady=5,
                                    text="Execute")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)

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
                self.controller.show_frame(results_frame)


class python_gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("The Influencer")
        self.wm_geometry("550x350")
        self.create_widgets()
        #self.resizable(0, 0)

    def create_widgets(self):
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.frames = {}
        for f in (home_frame, results_frame):
            frame = f(self.container, self)
            frame.grid(row=2, column=2, sticky=tk.NW+tk.SE)
            self.frames[f] = frame
        self.show_frame(home_frame)

    def show_frame(self, cls):
        self.frames[cls].tkraise()

if __name__ == "__main__":
    app = python_gui()
    app.mainloop()
    exit()

