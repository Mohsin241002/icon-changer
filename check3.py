import os
import tkinter as tk
from tkinter import filedialog
import requests
from googleapiclient.discovery import build
from PIL import Image

# Set your API key and search engine ID
api_key = "AIzaSyAssI1XS2VZ0VHEc74tRe_bAVNST-wVhSg"
search_engine_id = "a5fb584bf85d74aa4"

# Directory to save the downloaded images
output_directory = "images"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Create a custom search service
service = build("customsearch", "v1", developerKey=api_key)

# Initialize the icon path to an empty string
icon_path = ""

# Function to open a folder dialog and set the folder entry
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

# Function to download and convert image to ICO
def download_and_convert_image():
    global icon_path  # Make the icon_path variable global

    # Get the folder path from the entry box
    folder_path = folder_entry.get()

    if not folder_path:
        result_label.config(text="Please select a folder.")
        return

    # Extract folder name from the path
    folder_name = os.path.basename(folder_path)
    search_query = folder_name  # Use the folder name as the search query

    # Perform the Google Custom Search and limit the number of results
    image_urls = []
    response = service.cse().list(q=search_query, num=1, searchType="image", cx=search_engine_id).execute()
    if "items" in response:
        for item in response["items"]:
            image_urls.append(item["link"])

    if not image_urls:
        result_label.config(text="No image found for the folder name.")
        return

    image_url = image_urls[0]  # Use the first image URL
    try:
        print(f"Downloading: {image_url}")
        response = requests.get(image_url)
        if response.status_code == 200:
            image_extension = image_url.split(".")[-1]
            image_filename = os.path.join(output_directory, f"{folder_name}.{image_extension}")
            with open(image_filename, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {image_filename}")
            # Convert the image to ICO format
            icon_filename = os.path.join(output_directory, f"{folder_name}.ico")
            img = Image.open(image_filename)
            img.save(icon_filename, format="ICO")
            icon_path = os.path.abspath(icon_filename)
            icon_entry.delete(0, tk.END)
            icon_entry.insert(0, icon_path)  # Set the complete icon location
            result_label.config(text="Icon downloaded and converted successfully!")
            # Change folder icon
            change_folder_icon(folder_path, icon_path)
        else:
            print(f"Failed to download: {image_url}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to change the folder icon
def change_folder_icon(folder_path, icon_path):
    desktop_ini_path = os.path.join(folder_path, 'desktop.ini')

    # Create or modify the desktop.ini file
    with open(desktop_ini_path, 'w') as desktop_ini:
        desktop_ini.write("[.ShellClassInfo]\n")
        desktop_ini.write(f"IconResource={icon_path},0\n")

    # Set the system and hidden attributes for the folder and desktop.ini
    try:
        os.system(f'attrib +s +h "{desktop_ini_path}"')
        os.system(f'attrib +s "{folder_path}"')
        result_label.config(text="Icon changed successfully!")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Folder Icon Changer")

# Create and arrange widgets
folder_label = tk.Label(root, text="Select Folder:")
folder_label.pack()

folder_entry = tk.Entry(root, width=40)
folder_entry.pack()

select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack()

icon_label = tk.Label(root, text="Icon Location:")
icon_label.pack()

icon_entry = tk.Entry(root, width=40)
icon_entry.pack()

download_button = tk.Button(root, text="Download and Set Icon", command=download_and_convert_image)
download_button.pack()

result_label = tk.Label(root, text="", fg="green")
result_label.pack()

# Start the GUI event loop
root.mainloop()
