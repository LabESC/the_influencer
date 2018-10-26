from pages.pages import pages
from pages.app_pages import main_page
import tkinter as tk


def main():
    #pages()

    root = tk.Tk()
    root.title("The Influencer")
    main = main_page(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("550x350")
    root.mainloop()



if __name__ == "__main__":
    main()


