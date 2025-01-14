import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("3x3 Grid Example")

# Set the size of the window
root.geometry("400x400")  # Width x Height in pixels

# Configure row and column weights for dynamic resizing
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

    

# Add widgets using grid layout
label1 = tk.Label(root, text="Label 1", borderwidth=1, relief="solid")
label1.grid(row=0, column=0, sticky="nsew")

label2 = tk.Label(root, text="Label 2", borderwidth=1, relief="solid")
label2.grid(row=0, column=1, sticky="nsew")

label3 = tk.Label(root, text="Label 3", borderwidth=1, relief="solid")
label3.grid(row=0, column=2, sticky="nsew")

label4 = tk.Label(root, text="Label 4", borderwidth=1, relief="solid")
label4.grid(row=1, column=0, sticky="nsew")

label5 = tk.Label(root, text="Label 5", borderwidth=1, relief="solid")
label5.grid(row=1, column=1, sticky="nsew")

label6 = tk.Label(root, text="Label 6", borderwidth=1, relief="solid")
label6.grid(row=1, column=2, sticky="nsew")

label7 = tk.Label(root, text="Label 7", borderwidth=1, relief="solid")
label7.grid(row=2, column=0, sticky="nsew")

label8 = tk.Label(root, text="Label 8", borderwidth=1, relief="solid")
label8.grid(row=2, column=1, sticky="nsew")

label9 = tk.Label(root, text="Label 9", borderwidth=1, relief="solid")
label9.grid(row=2, column=2, sticky="nsew")


def on_label_click(event):
    label1.config(text="X")
label1.bind("<Button-1>", on_label_click)

def on_label_click2(event):
    label2.config(text="X")    
label2.bind("<Button-1>", on_label_click2)

def on_label_click3(event):
    label3.config(text="X")
label3.bind("<Button-1>", on_label_click3)

def on_label_click4(event):
    label4.config(text="X")    
label4.bind("<Button-1>", on_label_click4)



# Run the main event loop
root.mainloop()
