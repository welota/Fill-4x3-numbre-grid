import tkinter as tk
from tkinter import messagebox
import os 
import sys

max_characters = 1

user_data = {}
path = "score.txt"

sound_path = "winner.wav"

def about_button():
    messagebox.showinfo("About", f"""
The goal of the game is to fill all the boxes
with numbers from 1 to 8 without them being consecutive,
neither horizontally, vertically, nor diagonally. Imagine it as
a box around your number where you cannot
put the next consecutive number of the one you placed.

Wins: {user_data['wins']}
Losses: {user_data['loses']}

(The score is calculated as the difference between
games won and games lost)
""")

def change_score(did_win: bool):
    if did_win:
        user_data["wins"] += 1
    else:
        user_data["loses"] += 1
    
    score.set(f"Score: {user_data['wins'] - user_data['loses']}")
    save_score()

def save_score():
    with open(path, "w") as file:
        for k,v in user_data.items():
            file.write(f"{k}:{v}\n")

def load_score():
    with open(path, "r") as file:
        for line in file:
            split = line.split(":")
            user_data[split[0]] = int(split[1])

def restart():
    py = sys.executable
    os.execl(py, py, *sys.argv)

def validate(text: str):
    if text == "":
        return True
    return text.isdigit() and int(text) in range(1, 9) and len(text) <= max_characters

def finish():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
    def check_all_finished():
        for string in entry_text_arr:
            if len(string.get()) != 1:
                return False
        return True
        
    def is_grid_valid(grid):
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] is None: continue

                num = int(grid[r][c])

                for b_row, b_col in directions:
                    c_row, c_col = r + b_row, c + b_col

                    if 0 <= c_row < 3 and 0 <= c_col < 4 and grid[c_row][c_col] is not None:
                        neighbor = int(grid[c_row][c_col])

                        if abs(neighbor - num) == 1 or neighbor == num:
                            return False
        return True
    
    if check_all_finished():
        entry1.config(state="disabled")
        entry2.config(state="disabled")
        entry3.config(state="disabled")
        entry4.config(state="disabled")
        entry5.config(state="disabled")
        entry6.config(state="disabled")
        entry7.config(state="disabled")
        entry8.config(state="disabled")

        strm = entry_text_arr
        map = [
            [None, strm[0].get(), strm[1].get(), None],
            [strm[2].get(), strm[3].get(), strm[4].get(), strm[5].get()],
            [None, strm[6].get(), strm[7].get(), None],
        ]

        if is_grid_valid(map):
            change_score(True)
            choice = messagebox.askyesno("You won!", "Congratulations! You have won.\nDo you want to continue?")

            if choice:
                restart()
            else:
                root.quit()
        else:
            change_score(False)
            messagebox.showerror("Incorrect", "One or more numbers are adjacent")
            entry1.config(state="normal")
            entry2.config(state="normal")
            entry3.config(state="normal")
            entry4.config(state="normal")
            entry5.config(state="normal")
            entry6.config(state="normal")
            entry7.config(state="normal")
            entry8.config(state="normal")
    else:
        messagebox.showerror("Error", "All spaces must be filled with a number from 1 to 8")

root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("Game")

score = tk.StringVar()
load_score()
score.set(f"Score: {user_data['ganadas'] - user_data['perdidas']}")

vali = (root.register(validate), "%P")

tk.Label(root, textvariable=score, font=("Helvetica", 24)).pack()
tk.Button(root, text="?", font=("Arial", 16), command=about_button).place(relx=1, rely=0, width=50, height=50, anchor=tk.NE)

main_frame = tk.Frame(root, bg="ivory2", padx=10, pady=10)
main_frame.pack(expand=True, fill="both")

for i in range(4):
    main_frame.columnconfigure(i, weight=1)

for i in range(3):
    main_frame.rowconfigure(i, weight=1)

entry_text_arr = [tk.StringVar() for i in range(8)]

entry1 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[0], justify="center", validatecommand=vali, validate="key")
entry2 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[1], justify="center", validatecommand=vali, validate="key")
entry3 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[2], justify="center", validatecommand=vali, validate="key")
entry4 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[3], justify="center", validatecommand=vali, validate="key")
entry5 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[4], justify="center", validatecommand=vali, validate="key")
entry6 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[5], justify="center", validatecommand=vali, validate="key")
entry7 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[6], justify="center", validatecommand=vali, validate="key")
entry8 = tk.Entry(main_frame, highlightbackground="gray", highlightthickness=2, bg="thistle4", font=("Arial", 24), textvariable=entry_text_arr[7], justify="center", validatecommand=vali, validate="key")

entry1.grid(column=1, row=0, sticky="nswe")
entry2.grid(column=2, row=0, sticky="nswe")
entry3.grid(column=0, row=1, sticky="nswe")
entry4.grid(column=1, row=1, sticky="nswe")
entry5.grid(column=2, row=1, sticky="nswe")
entry6.grid(column=3, row=1, sticky="nswe")
entry7.grid(column=1, row=2, sticky="nswe")
entry8.grid(column=2, row=2, sticky="nswe")

validate_button = tk.Button(root, text="Validate", background="purple", font=("Arial", 16), command=finish)
validate_button.pack(side="bottom")

root.mainloop()
