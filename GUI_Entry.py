import tkinter as tk
import customtkinter as ctk
import threading
from functions.speech2text import _interact

# system settings.
ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("black")

# out app frame.
app = ctk.CTk()
app.geometry("720x75")
app.title("Artificial Lifeform Intelligent Entity | p-typed Research (Preview)")

# add the main UI elements.
# title = ctk.CTkLabel(app,text="")
# title.pack(side="left",padx=10,pady=10)

speech_engine = "system"

query = tk.StringVar()

query_holder = ctk.CTkEntry(app, width=600, height=35, font=("Arial", 14.5), textvariable=query)
query_holder.pack(side="left",padx=10,pady=10)

# print entered text after user clicks enter.
def print_text(event):
    request = query.get()

    # call the _interact function in a new thread
    threading.Thread(target=_interact, args=(request,)).start()
    query_holder.delete(0, 'end')

# bind the enter key to the print_text function.
query_holder.bind("<Return>", print_text)
# run the app mainloop.
app.mainloop()