import tkinter as tk
from io import BytesIO

import requests
from PIL import Image, ImageTk
from news_fetcher import fetch_news


def search_result_window():
    user_name = name_entry.get()
    topic = topic_entry.get()
    root.destroy()

    new_window = tk.Tk()
    new_window.title("Search Result")
    new_window.config(bg="#525B76")
    new_window.geometry("1100x700")

    greeting_label = tk.Label(new_window, text=f"Welcome, {user_name}!", font=("Souvenir", 30, "bold"), bg="#525B76", fg="#c4f1be")
    greeting_label.pack(pady=30)

    about_label = tk.Label(new_window, text=f"Newest article about {topic}:", font=("Souvenir", 16), bg="#525B76", fg="#c4f1be")
    about_label.place(relx=0.5, rely=0.5, anchor="center", x=-300, y=-200)

    news_list = fetch_news(topic, max_articles=1)
    for news in news_list:
        result_frame = tk.Frame(new_window, bg="#c4f1be", bd=5)
        result_frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="center")

        title_label = tk.Label(result_frame, text="Title: " + news['title'], font=("Souvenir", 20, "bold"), bg="#c4f1be", fg="#525B76", wraplength=800, justify="center")
        title_label.grid(row=0, column=0, sticky="w", padx=10, pady=0)

        description_label = tk.Label(result_frame, text="Description: " + news['description'], font=("Souvenir", 12), bg="#c4f1be", fg="#525B76", wraplength=400, justify="left")
        description_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        source_label = tk.Label(result_frame, text="Source: " + news['source'], font=("Souvenir", 12), bg="#c4f1be", fg="#525B76")
        source_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        date_label = tk.Label(result_frame, text="Date of publishing: " + news['published_date'], font=("Souvenir", 12), bg="#c4f1be", fg="#525B76")
        date_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Fetch image URL using fetch_image function
        image_url = news['image_url']

        try:
            if image_url and image_url != 'Could not provide image':
                response = requests.get(image_url)
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    img = img.resize((250, 150), resample=Image.BILINEAR)
                    img = ImageTk.PhotoImage(img)

                    image_label = tk.Label(result_frame, image=img)
                    image_label.image = img
                    image_label.grid(row=1, column=0, pady=10, rowspan=2, sticky="e")
                else:
                    raise Exception("Failed to fetch image")
            else:
                raise Exception("Image URL not available or could not be fetched")

        except (requests.exceptions.RequestException, Exception) as e:
            print(f"Error loading image: {e}")
            # Use a default local image when image fetching fails
            default_img = Image.open("img.png")  # Replace with your default image path
            default_img = default_img.resize((250, 150), resample=Image.BILINEAR)
            default_img = ImageTk.PhotoImage(default_img)

            default_img_label = tk.Label(result_frame, image=default_img)
            default_img_label.image = default_img
            default_img_label.grid(row=1, column=0, pady=10, rowspan=2, sticky="e")

    timestamp_label = tk.Label(new_window, text=f"Time until next article about {topic} : ...", font=("Souvenir", 16), bg="#525B76", fg="#c4f1be")
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

    topic_label = tk.Label(root, text="Topic/Topics that your interested in:", font=("Souvenir", 18), bg="#525B76", fg="#c4f1be")
    topic_label.pack(pady=(20, 5))

    global topic_entry
    topic_entry = tk.Entry(root, font=("Souvenir", 15), bg="#201e50", fg="#c4f1be", width=40, justify="center")
    topic_entry.insert(0, "")
    topic_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", bg="#201e50", fg="#c4f1be", command=search_result_window, width=12, height=1)
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_app()
