<p align="center">
  ⭐ <strong>If you found this project helpful, please give it a star!</strong> ⭐
</p>
# 📚 Student Management System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-Export-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  A fully functional <strong>desktop Student Management System</strong> built using <strong>Python</strong>, <strong>Tkinter</strong>, and <strong>MySQL</strong> — featuring a live clock, real-time data table, CSV export, and an in-app database connection manager.
</p>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Screenshots](#-screenshots)
- [Features](#-features)
- [Student Record Fields](#-student-record-fields)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Database Setup](#-database-setup)
- [How to Use](#-how-to-use)
- [Export Feature](#-export-feature)
- [Project Structure](#-project-structure)
- [Known Issues & Future Improvements](#-known-issues--future-improvements)
- [License](#-license)
- [Author](#-author)

---

## 📖 About the Project

The **Student Management System** is a single-file Python desktop application that enables administrators to manage student data through a clean, color-coded GUI. The application connects to a **MySQL** database backend and provides full **CRUD** (Create, Read, Update, Delete) functionality along with **CSV export**.

Key highlights from the codebase:
- The app **automatically creates the database and table** on first connection — no manual SQL setup needed.
- Student records are stored with **auto-captured date and time** of entry.
- The main window features a **live ticking clock**, a **scrolling welcome banner**, and a **real-time Treeview table** that refreshes after every operation.
- A dedicated **"Connect to Database"** button lets users configure and reconnect to any MySQL host at runtime.

---

## 📸 Screenshots

### 🏠 Main Window
> Live date/time clock (top-left), scrolling welcome banner (top-center), Connect to Database button (top-right), menu panel (left), and live data table (right).

![Main Menu](assets/screenshots/main_menu.png)

---

## ✨ Features

| #  | Feature                  | Description                                                                 |
|----|--------------------------|-----------------------------------------------------------------------------|
| 1  | ➕ **Add Student**        | Opens a form to enter student details; auto-saves current date & time       |
| 2  | 🔍 **Search Student**     | Search by any field: ID, Name, Mobile, Email, Address, Gender, D.O.B, Date  |
| 3  | 🗑️ **Delete Student**    | Select a row in the table and delete it with one click                      |
| 4  | ✏️ **Update Student**    | Click any row — form auto-fills with existing data for easy editing         |
| 5  | 📋 **Show All**           | Fetches and displays all student records in the scrollable Treeview table   |
| 6  | 📤 **Export Data**        | Exports currently displayed records to a `.csv` file using Pandas           |
| 7  | 🔌 **Connect to Database**| GUI window to enter host/user/password and connect or reconnect at runtime  |
| 8  | 🕐 **Live Clock**         | Real-time date and time display, updated every 200ms                        |
| 9  | 📜 **Scrollable Table**   | Both horizontal and vertical scrollbars on the data Treeview                |
| 10 | 🚪 **Exit**               | Confirmation dialog before closing the application                          |

---

## 🧾 Student Record Fields

These are the exact fields stored in the `studentdata1` table as defined in the source code:

| Column         | Type          | Description                                  | Example                  |
|----------------|---------------|----------------------------------------------|--------------------------|
| `id`           | INT (PK)      | Unique Student ID (Primary Key)              | `1111`                   |
| `name`         | VARCHAR(20)   | Full name of the student                     | `Niiranjan`              |
| `mobile`       | VARCHAR(12)   | Mobile number                                | `9XXXXXXXX`             |
| `email`        | VARCHAR(30)   | Email address                                | `abc@ex.com`    |
| `address`      | VARCHAR(100)  | Residential address                          | `address`    |
| `gender`       | VARCHAR(50)   | Gender                                       | `Male`                   |
| `dob`          | VARCHAR(50)   | Date of Birth (DD-MM-YYYY)                   | `12-34-5678`             |
| `date`         | VARCHAR(50)   | Date the record was added (auto-captured)    | `25/10/2024`             |
| `time`         | VARCHAR(50)   | Time the record was added (auto-captured)    | `22:50:30`               |

> 📝 **Note:** The `date` and `time` fields are automatically filled by the system using `time.strftime()` — the user does not need to enter them manually when adding a student.

---

## 🛠️ Tech Stack

| Technology               | Purpose                                              |
|--------------------------|------------------------------------------------------|
| **Python 3.x**           | Core programming language                            |
| **Tkinter**              | GUI framework — windows, labels, buttons, entry fields |
| **tkinter.ttk.Treeview** | Tabular data display with scrollbars                 |
| **mysql-connector-python**| Initial MySQL connection at app startup             |
| **PyMySQL**              | Runtime database reconnection via the Connect window |
| **Pandas**               | Exporting table data to `.csv` file                  |
| **time (built-in)**      | Live clock display and auto-timestamping records     |

---

## ✅ Prerequisites

Ensure the following are installed on your system before running:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) (running locally or remotely)
- The following Python packages:

```bash
pip install mysql-connector-python pymysql pandas
```

> **Tkinter** is included with Python by default. If missing, install it via:
> ```bash
> sudo apt-get install python3-tk   # Linux
> ```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/niiranjan-dev/student-management-system.git
cd student-management-system
```

### 2. Install Dependencies

```bash
pip install mysql-connector-python pymysql pandas
```

### 3. Configure Default DB Credentials *(Optional)*

At the top of `Student_Management_System.py`, the default connection is:

```python
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentmanagementsystem1"
)
```

Update this with your MySQL password before running, **or** leave it and use the in-app **"Connect to Database"** button instead.

### 4. Run the Application

```bash
python Student_Management_System.py
```

---

## 🗄️ Database Setup

> ✅ **No manual SQL required!** The app creates the database and table automatically.

When you click **"Connect To Database"** and enter your credentials, the app runs the following automatically:

```sql
CREATE DATABASE studentmanagementsystem1;

USE studentmanagementsystem1;

CREATE TABLE studentdata1 (
    id       INT           NOT NULL PRIMARY KEY,
    name     VARCHAR(20),
    mobile   VARCHAR(12),
    email    VARCHAR(30),
    address  VARCHAR(100),
    gender   VARCHAR(50),
    dob      VARCHAR(50),
    date     VARCHAR(50),
    time     VARCHAR(50)
);
```

If the database already exists, it simply reconnects to it — no data is lost.

---

## 🚀 How to Use

### Step 1 — Connect to the Database
- Click the **"Connect To Database"** button (top-right)
- Enter your MySQL `Host`, `User`, and `Password`
- Click **Submit** — the database and table are created automatically if they don't exist

### Step 2 — Use the Menu

| Button               | What it Does                                                                 |
|----------------------|------------------------------------------------------------------------------|
| **1. Add Student**   | Opens a form → fill in details → click Submit → record saved with timestamp  |
| **2. Search Student**| Enter any known field (ID, name, mobile, etc.) → click Submit to filter table|
| **3. Delete Student**| Click a row in the data table on the right → click this button to delete it  |
| **4. Update Student**| Click a row → this opens a form pre-filled with that student's data → edit → Submit |
| **5. Show All**      | Reloads and displays all student records in the table                        |
| **6. Export Data**   | Saves all currently visible records to a `.csv` file at a location you choose |
| **7. Exit**          | Prompts a confirmation dialog before closing the app                         |

---

## 📤 Export Feature

The **Export Data** feature uses **Pandas** to write all currently displayed records from the Treeview to a CSV file.

- A **Save As dialog** opens for you to choose the file location and name
- The file is saved as `<your_filename>.csv`
- Exported columns: `Id, Name, Mobile, Email, Address, Gender, D.O.B, Added Date, Added Time`

---

## 📁 Project Structure

```
student-management-system/
│
├── Student_Management_System.py   # Complete application (single file)
├── requirements.txt               # Python dependencies
├── assets/
│   └── screenshots/               # Screenshots for README
│       ├── main_menu.png
├── LICENSE                        # MIT License
└── README.md                      # Project documentation
```

> The entire application is self-contained in a **single Python file**.

---

## 🔮 Known Issues & Future Improvements

### ⚠️ Known Limitations
- `name` field is limited to `VARCHAR(20)` — long names may be truncated
- `email` field is limited to `VARCHAR(30)` — may not fit longer email addresses
- No input validation on the form fields (blank entries can be submitted)
- The default DB password is hardcoded at the top of the file

### 🛠️ Planned Improvements
- [ ] Add input validation (empty field checks, mobile number format, email format)
- [ ] Increase VARCHAR sizes for `name` and `email` fields
- [ ] Add admin login / authentication screen
- [ ] Export to PDF in addition to CSV
- [ ] Add student photo upload
- [ ] Dark mode / theme selector
- [ ] Search with multiple filters simultaneously
- [ ] Pagination for large datasets

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for full details.

---

## 🙋‍♂️ Author

**P Niiranjan**

- 🌐 GitHub: [niiranjan-dev](https://github.com/niiranjan-dev)
- 📧 Email: niiranjanprabhakar@gmail.com

## 🤝 Contributors

**Niiranjan P**

- 🌐 GitHub: [niiranjan-exe](https://github.com/niiranjan-exe)

<p align="center">
  ⭐ <strong>If you found this project helpful, please give it a star!</strong> ⭐
</p>
