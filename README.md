
# Escapism

Escapism is a Python-based Library Management System that allows users to explore books, manage their personal bookshelf, and share their reading experiences through ratings and reviews.

## Features

- **User Registration & Login** – Create an account and log in to the application.
- **Add Books** – Add books to the library.
- **Personal Bookshelf** – Manage and view your bookshelf.
- **Book Information** – View information about books.
- **Ratings & Reviews** – Rate books and share reviews.

## Technologies Used

- Python
- MySQL
- Pandas
- PrettyTable
- MySQL Connector/Python

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sreeshya-11/escapism.git
cd escapism
```

### 2. Install dependencies

```bash
pip install pandas prettytable mysql-connector-python
```

### 3. Configure MySQL

- Install and start MySQL.
- Create the database named `escapism`.
- Configure the required tables for the application.

### 4. Set the MySQL password

In PowerShell:

```powershell
$env:MYSQL_PASSWORD="your_mysql_password"
```

Replace the placeholder with your MySQL password.

### 5. Run the application

```bash
python esc_1.py
```

## Project

Escapism is a console-based application developed using Python and MySQL, focusing on book management and reading experiences.
