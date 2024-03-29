import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


if os.name=='posix':
    



    def run():
        filepath = asksaveasfilename(
            defaultextension=".c",
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"C interepreter Gui - {filepath}")
        path=(f"python3 __main__.py -f {filepath}")
        
        print(os.system(path))

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Gui C Interpreter - {filepath}")

    def select_file():
        """Open a file for compile."""
        filepath = askopenfilename(
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Gui C Interpreter - {filepath}")
        path=(f"python3 __main__.py -f {filepath}")
        
        print(os.system(path))


    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Gui C Interpreter - {filepath}")

    window = tk.Tk()
    window.title("Gui C Interpreter")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
    btn_run = tk.Button(fr_buttons, text="Run Program",command=run)
    btn_only_run = tk.Button(fr_buttons, text="select_file_to_run",command=select_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    btn_run.grid(row=2, column=0, sticky="ew", padx=5)
    btn_only_run.grid(row=3, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()

elif os.name=='nt':
    def run():
        filepath = asksaveasfilename(
            defaultextension=".c",
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"C interepreter Gui - {filepath}")
        path=(f"python __main__.py -f {filepath}")
        
        print(os.system(path))

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Gui C Interpreter - {filepath}")

    def select_file():
        """Open a file for compile."""
        filepath = askopenfilename(
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Gui C Interpreter - {filepath}")
        path=(f"python __main__.py -f {filepath}")
        
        print(os.system(path))


    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("C Files", "*.c"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Gui C Interpreter - {filepath}")

    window = tk.Tk()
    window.title("Gui C Interpreter")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
    btn_run = tk.Button(fr_buttons, text="Run Program",command=run)
    btn_only_run = tk.Button(fr_buttons, text="select_file_to_run",command=select_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    btn_run.grid(row=2, column=0, sticky="ew", padx=5)
    btn_only_run.grid(row=3, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()
else:
    print("Suitable Operating System Not Found")
    
