import customtkinter as ctk

# Initialize the main window
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("dark-blue")  # Default theme

root = ctk.CTk()
root.geometry("1000x500")  # Updated geometry
root.title("CeleryStealer Builder")

# Set background color to #287e29
root.configure(bg="#287e29")

# Adjust column and row weights to center the content
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

# Define the width of 3 inches (approximately 288 pixels)
inch_3_width = 288

# Entry for "App Name" - set to approximately 3 inches
app_name_entry = ctk.CTkEntry(root, placeholder_text="App Name", fg_color="#37ff77", width=inch_3_width)
app_name_entry.grid(row=1, column=0, padx=10, pady=10, sticky="n")  # Centered vertically

# Frame for "App Icon" button and textbox
icon_frame = ctk.CTkFrame(root, fg_color="#287e29")
icon_frame.grid(row=2, column=0, padx=10, pady=10, sticky="n")  # Centered vertically

# Textbox for App Icon Path - set to 3 inches
app_icon_entry = ctk.CTkEntry(icon_frame, placeholder_text="App Icon Path", fg_color="#37ff77", width=inch_3_width)
app_icon_entry.pack(side="right", padx=10, pady=10)

# Button for selecting App Icon - synced with the text box size
app_icon_button = ctk.CTkButton(icon_frame, text="App Icon", fg_color="#37ff77", width=80)  # Standard width for the button
app_icon_button.pack(side="left", padx=10, pady=10)

# Build .EXE Button - set to approximately 3 inches in width
build_exe_button = ctk.CTkButton(root, text="Build .EXE", fg_color="#37ff77", width=inch_3_width)
build_exe_button.grid(row=3, column=0, padx=10, pady=10, sticky="n")

# Project info label (bottom-left corner)
project_label = ctk.CTkLabel(root, text="Project CeleryStealer: 'Githublinkhere'", fg_color="#287e29", text_color="white")
project_label.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")

# Creation date label below the project label
creation_date_label = ctk.CTkLabel(root, text="Creation Date: 10th October 2024", fg_color="#287e29", text_color="white")
creation_date_label.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="w")

# Start the Tkinter event loop
root.mainloop()
