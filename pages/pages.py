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
        title_label.grid(padx=200)

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

        directory_search_button = tk.Button(self, text="Find project file", command=self.file_search_button_function)
        directory_search_button.grid()

        self.text_file_location = tk.Text(self, height=2, width=30, )
        self.text_file_location.config(state="disabled")
        self.text_file_location.grid(padx=130)

        show_project_button = tk.Button(self, text="Show my Project's Influencer!", command=self.show_project)
        show_project_button.grid()

        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(home_frame),
                                    padx=105,
                                    pady=5,
                                    text="Home")
        #self.new_button.grid(padx=105, pady=5, sticky=tk.W+tk.E)

    def get_gexf_directory_files(location):
        choices = get_gexf_directory_files_to_vector(location)
        return choices

    def file_search_button_function(self):
        location = filedialog.askopenfile(initialdir=os.getcwd(), title="Select the project file",
                                          filetypes = (("gexf files","*.gexf"),("all files","*.*")))
        self.text_file_location.config(state="normal")
        self.text_file_location.delete(1.0, "end")
        try:
            self.text_file_location.insert("end", location.name)
        except:
            pass
        self.text_file_location.config(state="disabled")

    def show_ecosystem(self, ecosystem_file_path):
        gephi_home = os.getenv("GEPHI_HOME")
        gephi_executable = os.path.join(gephi_home)
        gephi_executable = os.path.join(gephi_executable)
        ecosystem_file_path_normalized = os.path.normcase(ecosystem_file_path)
        command = "\"" + gephi_executable + "\" " + ecosystem_file_path_normalized
        os.system(command)

    def show_project(self):
        gephi_home = os.getenv("GEPHI_HOME")
        gephi_executable = os.path.join(gephi_home, "bin")
        gephi_executable = os.path.join(gephi_executable, "gephi")
        file_location = os.path.normcase(self.text_file_location.get(1.0, 'end-1c'))
        if verify_file_existence(file_location):
            command = "\"" + gephi_executable + "\" " + file_location
            os.system(command)
        else:
            messagebox.showwarning("Path is empty", "Select your project file")


class home_frame(base_frame):
    def create_widgets(self):
        title_label = tk.Label(self, text="The Influencer")
        title_label.config(font=("Times New Roman", 44))
        title_label.grid(padx=200)

        instructions_label = tk.Label(self,
                                      text="Welcome to The Influencer!\nStep 1. In order to start your analysis,\n "
                                           "browse for your SECO's .csv files location:", width=30)
        instructions_label.grid(pady=20)

        directory_search_button = tk.Button(self, text="Find", command=self.directory_search_button_function)
        directory_search_button.grid()

        confirmation_label = tk.Label(self, text="Confirm that this is your directory location:")
        confirmation_label.grid()

        self.text_directory_location = tk.Text(self, height=2, width=30, )
        self.text_directory_location.config(state="disabled")
        self.text_directory_location.grid(padx=130)


        filters_label = tk.Label(self, text="Step 2. Choose characteristics to be used while analysing:", width=50)
        filters_label.grid(pady=10)

        self.check_ct = IntVar(value=1)
        self.checkbutton_ct = Checkbutton(self, text="Closeness to GitHub Project Owner", variable=self.check_ct)
        self.checkbutton_ct.grid()
        self.check_lt = IntVar(value=1)
        self.checkbutton_lt = Checkbutton(self, text="Long-time interaction with the Project", variable=self.check_lt)
        self.checkbutton_lt.grid()
        self.check_st = IntVar(value=1)
        self.checkbutton_st = Checkbutton(self, text="Status in GitHub", variable=self.check_st)
        self.checkbutton_st.grid()
        self.check_stp = IntVar(value=1)
        self.checkbutton_stp = Checkbutton(self, text="Status in Project", variable=self.check_stp)
        self.checkbutton_stp.grid()
        self.check_cv = IntVar(value=1)
        self.checkbutton_cv = Checkbutton(self, text="Content Value", variable=self.check_cv)
        self.checkbutton_cv.grid()
        self.check_sl = IntVar(value=1)
        self.checkbutton_sl = Checkbutton(self, text="Source of Learning", variable=self.check_sl)
        self.checkbutton_sl.grid()
        self.check_pcode = IntVar(value=1)
        self.checkbutton_pcode = Checkbutton(self, text="Participation with Code", variable=self.check_pcode)
        self.checkbutton_pcode.grid()
        self.check_pcomm = IntVar(value=1)
        self.checkbutton_pcomm = Checkbutton(self, text="Participation with Comments", variable=self.check_pcomm)
        self.checkbutton_pcomm.grid()


        analysis_button = tk.Button(self, text="Step 3. Start Analysis!", command=self.start_analysis)
        analysis_button.grid()

        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(results_frame),
                                    padx=105,
                                    pady=5,
                                    text="Execute")
        #self.new_button.grid(padx=105, pady=5, sticky=tk.W+tk.E)

    def directory_search_button_function(self):
        location = filedialog.askdirectory()
        self.text_directory_location.config(state="normal")
        self.text_directory_location.delete(1.0,"end")
        self.text_directory_location.insert("end", location)
        self.text_directory_location.config(state="disabled")


    def start_analysis(self):
        print(self.check_pcomm.get())
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
                    self.filter_option()
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

    def filter_option(self):
        pass

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
        self.wm_geometry("750x550")
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

