import tkinter as tk

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("500x500")

def clr_txt():
    txt_ar.delete("1.0", tk.END)

txt_ar = tk.Text(root, wrap="word")
txt_ar.pack(expand=True, fill="both", padx=10, pady=10)

clear_button = tk.Button(root, text="Clear Text", command=clr_txt)
clear_button.pack(pady=5)

root.mainloop()
