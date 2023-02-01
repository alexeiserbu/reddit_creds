import tkinter as tk

def save_info():
    # get the user input
    name = name_entry.get()
    age = age_entry.get()
    username = username_entry.get()

    # format the output string
    output = "Your name is {}, you are {} years old, and your Reddit username is {}.".format(name, age, username)

    # write the output to a file
    with open("user_info.txt", "w") as f:
        f.write(output)

    # display the output in the result label
    result_label["text"] = output

# create the main window
root = tk.Tk()
root.title("User Information")

# create the labels and entry widgets for the user input
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age:")
age_entry = tk.Entry(root)

username_label = tk.Label(root, text="Reddit username:")
username_entry = tk.Entry(root)

# create the save button
save_button = tk.Button(root, text="Save", command=save_info)

# create the label to display the result
result_label = tk.Label(root, text="")

# arrange the widgets using a grid layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1)

username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1)

save_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, columnspan=2, pady=10)

# start the main event loop
root.mainloop()