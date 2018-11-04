import tkinter as tk
from tkinter import *
from tkinter import messagebox
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

        #choices = self.get_gexf_directory_files()
        #choice = tk.StringVar(self)
        #choice.set(choices.pop())
        #choices = {"project1", "project2", "project3"}
        #choice.set("project1")

        #ecosystem_options = tk.OptionMenu(self, choice, *choices)
        #ecosystem_options.grid()

        directory_search_button = tk.Button(self, text="Find", command=self.file_search_button_function)
        directory_search_button.grid()

        self.text_file_location = tk.Text(self, height=2, width=30, )
        self.text_file_location.config(state="disabled")
        self.text_file_location.grid(padx=30)

        show_project_button = tk.Button(self, text="Show my Project's Influencer!")
        show_project_button.grid()

        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(home_frame),
                                    padx=5,
                                    pady=5,
                                    text="Home")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)

    def get_gexf_directory_files(location):
        choices = get_gexf_directory_files_to_vector(location)
        return choices

    def file_search_button_function(self):
        location = filedialog.askopenfile()
        self.text_file_location.config(state="normal")
        self.text_file_location.delete(1.0, "end")
        self.text_file_location.insert("end", location.name)
        self.text_file_location.config(state="disabled")


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
        complete_location = os.path.join(location, "ecosystem_gexf")
        if not verify_directory_existence(location):
            self.path_is_invalid_warning(location)
        else:
            if verify_csv_files_existence_in_path(location):
                if verify_directory_existence(complete_location):
                    if self.analysis_exists_question(complete_location):
                        print("true")
                else:
                    create_directory_structure(location)
                    self.controller.show_frame(results_frame)
            else:
                self.no_csv_file_warning(location)


    def path_is_invalid_warning(self, location):
        messagebox.showwarning("Path is empty", "Select your SECO path before analyzing")

    def analysis_exists_question(self, location):
        answer = tk.messagebox.askyesno("Question", "There is already an analysis on this SECO.\n"
                                                    "Would like to erase it and run the analysis again?")
        if answer:
            remove_directory_structure(location)
            return True
        return False

    def verify_csv_files_existence(self, location):
        if verify_csv_files_existence_in_path(location):
            return True
        return False

    def no_csv_file_warning(self, location):
        messagebox.showwarning("No .csv files found", "No .csv files found at " + location + "\nSelect the "
                                                                        "directory where your .csv files are located")


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

