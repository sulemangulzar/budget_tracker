💰 Budget Tracker (Console-Based)
A simple console-based budget tracker in Python that allows users to sign up, log in, and track their personal expenses and budget. User data is stored in .txt files per user, keeping things lightweight and local.

📋 Features
🧾 User Signup
Create a new account with a username, password, and starting budget.

🔐 User Login
Securely log in using your saved credentials.

💵 Add Balance
Add money to your current budget.

🧾 Add Expense
Subtract money from your budget and record the reason and date.

📊 View Balance
Check your current available balance.

📉 View Expenses
View your list of recorded expenses.

🧠 How It Works
Each user gets a text file (username.txt) which stores their credentials, current budget, and expenses.

Example content of user123.txt:

yaml
Copy
Edit
user123
mypassword
Budget: 5000
Expense: 100.00 | Reason: Grocery | Date: 2025-07-30
🚀 How to Run
Make sure you have Python 3 installed.

Save the script to a file, for example: budget_tracker.py.

Run it in your terminal:

bash
Copy
Edit
python budget_tracker.py
🧑‍💻 Usage
Upon running, you will be asked to:

vbnet
Copy
Edit
1 - Signup
2 - Login
Choose option:
Once logged in:

pgsql
Copy
Edit
1 - Add Budget
2 - Add Expense
3 - View Balance
4 - View Expenses
5 - Exit
⚠️ Limitations
No encryption for passwords (stored as plain text).

Single-user local storage via text files.

No multi-threading or concurrent usage support.

Basic input validation.

✅ Improvements You Can Add
Password hashing for better security.

GUI with Tkinter or Flask web version.

Categorize expenses.

Monthly reports or expense charts.

Export data to CSV/Excel.

📂 File Structure
python-repl
Copy
Edit
budget_tracker.py
user1.txt
user2.txt
...
📚 Requirements
Python 3.x

No external libraries needed (only os module)

🧑‍🎓 Author
Developed by: Suleman Gulzar

For learning and personal use.
