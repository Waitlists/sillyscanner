import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random
import threading
import time

# Generate random IPs with ports around 25565
def generate_ip():
    ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    port = random.randint(25365, 25765)  # Ports in range 200 below to 200 above 25565
    return f"{ip}:{port}"

# Display new IPs in a scrolling, 'hacker' style
def update_ips():
    while True:
        ip = generate_ip()
        ip_label = tk.Label(root, text=ip, fg="green", bg="black", font=("Courier", 14, "bold"))
        ip_label.pack(anchor="w")
        ip_label.place(x=random.randint(20, 700), y=random.randint(20, 500))  # Randomize placement

        root.update()
        time.sleep(0.2)  # Control speed of IP generation
        ip_label.after(1000, ip_label.destroy)  # IP disappears after 1 second

# Play radar GIF animation
def play_gif():
    for frame in ImageSequence.Iterator(radar_gif):
        frame_image = ImageTk.PhotoImage(frame)
        radar_label.config(image=frame_image)
        radar_label.image = frame_image
        root.update_idletasks()
        time.sleep(0.1)  # Adjust speed of the GIF

# Set up the main window
root = tk.Tk()
root.title("Scanning Radar")
root.configure(bg="black")
root.attributes("-fullscreen", True)

# Load radar GIF
radar_gif = Image.open("radar.gif")
radar_label = tk.Label(root, bg="black")
radar_label.pack(expand=True)

# Start GIF animation and IP updates in separate threads
threading.Thread(target=play_gif, daemon=True).start()
threading.Thread(target=update_ips, daemon=True).start()

# Exit on 'Escape' key
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
