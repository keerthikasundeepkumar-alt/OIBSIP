**OASIS INFOBYTE INTERNSHIP TASKS**

this repository contains my completed tasks for the oasis infobyte virtual internship.
Task 1: Password generator 
Task 2: BMI Calculator 
Task 3: Voice assistant

# 🎙️ Personal Voice Assistant
A simple personal voice assistant built in Python. It can respond to your voice commands, tell the time and date, open websites, and perform Google searches.

## ✨ Features
* Speech Recognition: Uses speech_recognition library.
* Text-to-Speech: Uses pyttsx3.
* Web Integration: Opens Google, YouTube, and LinkedIn.
* Utilities: Provides current time, date, and performs live Google searches.

## 🛠️ Requirements
* Python: 3.10.x
* Packages:
bash
pip install pyttsx3
pip install SpeechRecognition
pip install sounddevice
pip install scipy

## 🚀How to Run:

1.clone the repo:
git clone https://github.com/keerthikasundeepkumar-alt/githubemc1.git

2.folder:
cd githubemc1

3.start the assistant:
python main.py

## Example Commands:
.Greetings: "Hello", "Hi", "Hey"
.Time & Date: "What time is it?", "Today's date"
.Websites: "Open YouTube", "Open Google"
Exit: "Exit", "Stop", "Bye"



# BMI-calculator
📖 Overview

This project is a GUI-based BMI (Body Mass Index) tracking system built using Python. It allows users to calculate BMI, store multiple records, and visualize health data using graphs.

The system integrates user input, database storage, and data analysis to provide a simple yet effective health monitoring tool.
🚀 Features
Calculate BMI using height and weight
Store multiple user records
View historical BMI data
Visualize Height vs Weight using scatter plot
Analyze BMI trend over time using line graph
🛠️ Technologies Used
/Python
/Tkinter
/SQLite
/Matplotlib
🧠 How It Works
1. Database Setup
/Uses SQLite database (bmi.db)
/Stores user details:
>Name
>Height
>weight
>BMI
>date
2. BMI Calculation

The BMI is calculated using the formula:BMI = weight / (height × height)
>Takes input from GUI
>Displays result instantly
>Saves data into database
3. Data Storage
>Each calculation is stored in the database
>Supports multiple users and multiple entries
4. History Viewing
Displays all stored records
Shows:
>Name
>Height
>Weight
>BMI
>Date
5. Data Visualization

Height vs Weight Graph

>Scatter plot
>Shows relationship between height and weight

BMI Trend Graph

>Line chart
>Displays BMI changes over time
▶️ How to Run
>Install Python
>Install required library:pip install matplotlib
>Run the program:python bmi_calc.py
# SMART BMI TRACKER
https://www.linkedin.com/posts/keerthika-sundeepkumar-195ab4316_python-datascience-projects-ugcPost-7447683124962127873--zSx?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFBArwEBn0CQ7bXWiwbuJSsKJ0h7BY8BmYw
[Click here to watch the Video Demo on LinkedIn!](https://www.linkedin.com/posts/keerthika-sundeepkumar-195ab4316_python-datascience-codingproject-activity-7445743320774942720-QaQs?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFBArwEBn0CQ7bXWiwbuJSsKJ0h7BY8BmYw)



# 🔐 Password Generator (Python Tkinter)

A simple desktop application built using Python and Tkinter to generate secure and customizable passwords.

---

## 🚀 Features

- Generate passwords with custom length
- Supports:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (!@#$...)
- Ensures at least one character from each selected category
- Copy generated password to clipboard
- Error handling for invalid selections

---

## 🛠️ Technologies Used

- Python
- Tkinter (GUI)
- Random & String modules

---

## ⚙️ How It Works

1. Enter desired password length
2. Select character types (uppercase, lowercase, numbers, symbols)
3. Click *Generate*
4. Copy the password using the *Copy* button

---

## ⚠️ Limitations

- No password strength indicator yet
- Basic UI design
- Input validation can be improved (e.g., handling non-numeric input)

---

## 📌 Future Improvements

- Add password strength checker (Weak/Medium/Strong)
- Improve UI design
- Add default selections for better user experience
- Handle invalid inputs more robustly

---

## 🧠 What I Learned

- Building GUI applications using Tkinter
- Handling user inputs and validation
- Writing structured Python logic
- Improving problem-solving through project building

---

## 🙌 Acknowledgment

Thanks to Oasis Infobyte for providing this task and learning opportunity.

---

## 📎 Author

keerthika | [View Project Post on LinkedIn](https://www.linkedin.com/posts/keerthika-sundeepkumar-195ab4316_python-tkinter-beginnerprojects-ugcPost-7451500814621147136-3t_i)
