import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# DATABASE 
conn = sqlite3.connect("bmi.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    height REAL,
    weight REAL,
    bmi REAL,
    date TEXT
)
""")
conn.commit()

# BMI FUNCTION 
def calculate_bmi():
    try:
        name = entry_name.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")

        date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
        INSERT INTO users (name, height, weight, bmi, date)
        VALUES (?, ?, ?, ?, ?)
        """, (name, height, weight, bmi, date))
        conn.commit()

    except:
        messagebox.showerror("Error", "Invalid input")

#VIEW HISTORY
def view_history():
    records = cursor.execute("SELECT name, height, weight, bmi, date FROM users").fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("History")

    for i, row in enumerate(records):
        text = f"{row[0]} | H:{row[1]} W:{row[2]} BMI:{row[3]:.2f} | {row[4]}"
        tk.Label(history_window, text=text).pack()

# GRAPH (HEIGHT VS WEIGHT)
def show_graph():
    data = cursor.execute("SELECT height, weight FROM users").fetchall()

    if not data:
        messagebox.showinfo("No Data", "No records to plot")
        return

    heights = [d[0] for d in data]
    weights = [d[1] for d in data]

    plt.figure()
    plt.scatter(heights, weights)
    plt.xlabel("Height (m)")
    plt.ylabel("Weight (kg)")
    plt.title("Height vs Weight")
    plt.show()

#BMI TREND 
def bmi_trend():
    data = cursor.execute("SELECT date, bmi FROM users").fetchall()

    if not data:
        messagebox.showinfo("No Data", "No records")
        return

    dates = [d[0] for d in data]
    bmis = [d[1] for d in data]

    plt.figure()
    plt.plot(dates, bmis)
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title("BMI Trend Over Time")
    plt.xticks(rotation=45)
    plt.show()

#GUI
root = tk.Tk()
root.title("Smart BMI Tracker")
root.geometry("350x400")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Height (m)").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Weight (kg)").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

tk.Button(root, text="View History", command=view_history).pack(pady=5)
tk.Button(root, text="Height vs Weight Graph", command=show_graph).pack(pady=5)
tk.Button(root, text="BMI Trend Graph", command=bmi_trend).pack(pady=5)

root.mainloop()
