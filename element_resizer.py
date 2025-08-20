import tkinter as tk

def resize_element_linear(width, height, old_count, new_count):
    """Scale width and height linearly with count ratio."""
    if new_count <= 0:
        raise ValueError("New count must be > 0")
    s = old_count / new_count
    return width * s, height * s

def on_resize():
    try:
        w = float(width_entry.get())
        h = float(height_entry.get())
        old_c = float(curr_count_entry.get())
        new_c = float(new_count_entry.get())

        new_w, new_h = resize_element_linear(w, h, old_c, new_c)

        result_label.config(
            text=f"New size: {new_w:.2f} × {new_h:.2f}"
        )
    except ValueError:
        result_label.config(text="⚠ Please enter valid numbers (new count > 0).")

# --- GUI ---
root = tk.Tk()
root.title("Linear Element Resizer")

# Inputs
tk.Label(root, text="Width:").grid(row=0, column=0, padx=6, pady=4, sticky="e")
width_entry = tk.Entry(root, width=14)
width_entry.grid(row=0, column=1, padx=6, pady=4)

tk.Label(root, text="Height:").grid(row=1, column=0, padx=6, pady=4, sticky="e")
height_entry = tk.Entry(root, width=14)
height_entry.grid(row=1, column=1, padx=6, pady=4)

tk.Label(root, text="Current Count:").grid(row=2, column=0, padx=6, pady=4, sticky="e")
curr_count_entry = tk.Entry(root, width=14)
curr_count_entry.grid(row=2, column=1, padx=6, pady=4)

tk.Label(root, text="New Count:").grid(row=3, column=0, padx=6, pady=4, sticky="e")
new_count_entry = tk.Entry(root, width=14)
new_count_entry.grid(row=3, column=1, padx=6, pady=4)

# Button
resize_button = tk.Button(root, text="Resize", command=on_resize)
resize_button.grid(row=4, column=0, columnspan=2, pady=8)

# Result
result_label = tk.Label(root, text="", justify="left", fg="blue")
result_label.grid(row=5, column=0, columnspan=2, padx=6, pady=6)

# Prefill some defaults
# width_entry.insert(0, "100")
# height_entry.insert(0, "80")
# curr_count_entry.insert(0, "6")
# new_count_entry.insert(0, "10")

root.mainloop()
