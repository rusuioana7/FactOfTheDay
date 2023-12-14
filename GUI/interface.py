import tkinter as tk


def on_name_click(event):
    if name_entry.get() == "Enter your name here":
        name_entry.delete(0, "end")
        name_entry.config(fg="#c4f1be", justify="center")


def on_topic_click(event):
    if topic_entry.get() == "Enter the topic that you're interested in":
        topic_entry.delete(0, "end")
        topic_entry.config(fg="#c4f1be", justify="center")


def on_name_focus_out(event):
    if not name_entry.get():
        name_entry.insert(0, "Enter your name here")
        name_entry.config(fg="#c4f1be", justify="center")


def on_topic_focus_out(event):
    if not topic_entry.get():
        topic_entry.insert(0, "Enter the topic that you're interested in")
        topic_entry.config(fg="#c4f1be", justify="center")


def choose_topic_window():
    user_name = name_entry.get()
    old_width = root.winfo_width()
    old_height = root.winfo_height()

    root.destroy()

    new_window = tk.Tk()
    new_window.title("Welcome")
    new_window.config(bg="#525B76")
    new_window.geometry(f"{old_width}x{old_height}")

    greeting_label = tk.Label(new_window, text=f"Welcome, {user_name}!", font=("Souvenir", 30, "bold"), bg="#525B76",
                              fg="#c4f1be")
    greeting_label.pack(pady=30)

    global topic_entry
    topic_entry = tk.Entry(new_window, font=("Souvenir", 13), bg="#201e50", fg="#c4f1be", width=40, justify="center")
    topic_entry.insert(0, "Enter the topic that you're interested in")
    topic_entry.bind("<FocusIn>", on_topic_click)
    topic_entry.bind("<FocusOut>", on_topic_focus_out)
    topic_entry.pack(pady=15, padx=5, ipady=5)

    submit_button = tk.Button(new_window, text="Submit", bg="#201e50", fg="#c4f1be", command=choose_topic_window,
                              width=12, height=1)
    submit_button.pack(pady=5)

    explore_label_button = tk.Label(new_window, text="Explore more topics", font=("Souvenir", 15, "bold"),
                                  bg="#525B76", fg="#c4f1be")
    explore_label_button.pack(pady=30, padx=50, anchor=tk.W)

    label_frame_list = ["Politics", "Technology", "Health", "Business", "Environment",
                        "Entertainment", "Sports", "Science", "Education", "Lifestyle",
                        "Food", "Fashion", "Art", "Literature", "Tourism"]

    checkbox_texts = [
        ["Politics", ["Elections", "Policies", "Geopolitical issues", "Diplomatic relations"]],
        ["Technology", ["Gadgets", "Software", "Cybersecurity", "AI", "Tech companies"]],
        ["Health", ["Public health issues", "pharmaceuticals", "treatments", "Pandemy", "diseases"]],
        ["Business", ["economy", "stock markets", "entrepreneurship", "Marketing", "Cryptocurrency"]],
        ["Environment", ["climate change", "natural disasters", "Ecology", "Pollution", "Sustainability"]],
        ["Entertainment", ["Music", "Movies", "TV Shows", "awards", "celebrities"]],
        ["Sports", ["Athletes", "Sports Events", "Tennis", "Soccer", "Sports Teams"]],
        ["Science", ["astronomy", "biology", "physics", "chemistry", "discovery"]],
        ["Lifestyle", ["Hobbies", "personal development", "journaling", "fitness", "Relationships"]],
        ["Food", ["restaurant reviews", "culinary trends", "recipies", "nutrition", "calorie deficit"]],
        ["Social", ["human rights", "activism", "ONG", "discrimination", "equality"]],
        ["Art", ["art exhibitions", "art history", "museums"]],
        ["Literature", ["poetry", "bestseller lists", "book releases", "biography", "author interviews"]],
        ["Tourism", ["travel tips", "airline news", "tourist attractions", "travel destinations"]],
    ]

    for label, options in checkbox_texts:
        label_frame = tk.Frame(new_window, bg="#525B76")
        label_frame.pack(pady=5, padx=50, anchor=tk.W)
        tk.Label(label_frame, text=label, font=("Souvenir", 15, "bold"), bg="#525B76", fg="#c4f1be").pack(pady=10,
                                                                                                          padx=20,
                                                                                                          anchor=tk.W)
        label_frame_list.append(label_frame)

        checkbox_frame = tk.Frame(label_frame, bg="#525B76")
        checkbox_frame.pack(anchor=tk.CENTER)

        checkbox_var = [tk.BooleanVar() for _ in range(len(options))]

        column_num = 5
        row = 0
        col = 0
        for i, text in enumerate(options):
            checkbox = tk.Checkbutton(checkbox_frame, text=text, selectcolor="#c4f1be", variable=checkbox_var[i],
                                      bg="#201e50", fg="#c4f1be",
                                      font=("Souvenir", 12), height=1, width=20)
            checkbox.grid(row=row, column=col, padx=10, pady=5)
            col += 1
            if col == column_num:
                col = 0
                row += 1

def run_app():
    global root
    root = tk.Tk()
    root.title("News App")
    root.config(bg="#525B76")
    root.geometry("800x500")

    title_label = tk.Label(root, text="Fact of the day", font=("Souvenir", 30, "bold"), bg="#525B76", fg="#c4f1be")
    title_label.pack(pady=20)

    global name_entry
    name_entry = tk.Entry(root, font=("Souvenir", 13), bg="#201e50", fg="#c4f1be", width=20, justify="center")
    name_entry.insert(0, "Enter your name here")
    name_entry.bind("<FocusIn>", on_name_click)
    name_entry.bind("<FocusOut>", on_name_focus_out)
    name_entry.pack(pady=15, padx=5, ipady=5)

    continue_button = tk.Button(root, text="Continue", bg="#201e50", fg="#c4f1be", command=choose_topic_window, width=12,
                                height=1)
    continue_button.pack(pady=11)

    root.mainloop()

if __name__ == "__main__":
    run_app()