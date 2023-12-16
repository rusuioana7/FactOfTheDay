import tkinter as tk


def search_result_window():
    user_name = name_entry.get()
    root.destroy()

    new_window = tk.Tk()
    new_window.title("Search Result")
    new_window.config(bg="#525B76")
    new_window.geometry("900x700")


    greeting_label = tk.Label(new_window, text=f"Welcome, {user_name}!", font=("Souvenir", 30, "bold"), bg="#525B76",
                              fg="#c4f1be")
    greeting_label.pack(pady=30)

    about_label = tk.Label(new_window, text="Newest article about ... :", font=("Souvenir", 16), bg="#525B76", fg="#c4f1be")
    about_label.place(relx=0.5, rely=0.5, anchor="center", x=-300, y=-200)

    #search result
    result_frame = tk.Frame(new_window, bg="#c4f1be", bd=5)
    result_frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="center")

    title_label = tk.Label(result_frame, text="Title", font=("Souvenir", 24, "bold"), bg="#c4f1be", fg="#525B76")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    description_label = tk.Label(result_frame, text="Description", font=("Souvenir", 16), bg="#c4f1be",
                                 fg="#525B76")
    description_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    image_path = "C:\\Users\\ioana\\OneDrive\\Pictures\\Capturi de ecran\\Screenshot 2023-03-25 155833.png"
    img = tk.PhotoImage(file=image_path)
    img = img.subsample(4)
    image_label = tk.Label(result_frame, image=img)
    image_label.image = img
    image_label.grid(row=1, column=1, padx=10, pady=10, sticky="e")

    timestamp_label = tk.Label(new_window, text="Time until next article about ... : ...", font=("Souvenir", 16), bg="#525B76",
                            fg="#c4f1be")
    timestamp_label.place(relx=0.5, rely=0.5, anchor="center", x=-250, y=200)

    new_window.mainloop()


def run_app():
    global root
    root = tk.Tk()
    root.title("News App")
    root.config(bg="#525B76")
    root.geometry("900x700")

    title_label = tk.Label(root, text="Fact of the day", font=("Souvenir", 35, "bold"), bg="#525B76", fg="#c4f1be")
    title_label.pack(pady=20)

    name_label = tk.Label(root, text="Your name:", font=("Souvenir", 18), bg="#525B76", fg="#c4f1be")
    name_label.pack(pady=(30, 5))

    global name_entry
    name_entry = tk.Entry(root, font=("Souvenir", 15), bg="#201e50", fg="#c4f1be", width=20, justify="center")
    name_entry.insert(0, "")
    name_entry.pack(pady=5)

    topic_label = tk.Label(root,
                           text="Topic/Topics that your interested in (e.g. astronomy, politics, climate change, ...):",
                           font=("Souvenir", 18), bg="#525B76", fg="#c4f1be")
    topic_label.pack(pady=(20, 5))

    global topic_entry
    topic_entry = tk.Entry(root, font=("Souvenir", 15), bg="#201e50", fg="#c4f1be", width=40, justify="center")
    topic_entry.insert(0, "")
    topic_entry.pack(pady=5)

    additional_label = tk.Label(root, text="Time interval between news (5 minutes default):", font=("Souvenir", 18),
                                bg="#525B76", fg="#c4f1be")
    additional_label.pack(pady=(20, 5))

    global additional_entry
    additional_entry = tk.Entry(root, font=("Souvenir", 15), bg="#201e50", fg="#c4f1be", width=20, justify="center")
    additional_entry.insert(0, "")
    additional_entry.pack(pady=5)

    continue_button = tk.Button(root, text="Submit", bg="#201e50", fg="#c4f1be", command=search_result_window,
                                width=12, height=1)
    continue_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    run_app()
