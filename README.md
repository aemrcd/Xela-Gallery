# Xela-Gallery

Explore 3D Art, Engage Your Imagination Today!

[![Last Commit](https://img.shields.io/github/last-commit/aemrcd/Xela-Gallery)](https://github.com/aemrcd/Xela-Gallery/commits/main) 
[![HTML Percentage](https://img.shields.io/badge/html-60.6%25-blue)](https://github.com/aemrcd/Xela-Gallery) 
[![Python Percentage](https://img.shields.io/badge/python-39.4%25-yellow)](https://github.com/aemrcd/Xela-Gallery) 


## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database-Setup](README.md#database-setup)
  - [Website-View](#testing)

---

## Overview

Xela-Gallery is a powerful Flask-based web application designed to showcase 3D models while ensuring an immersive and interactive user experience. It allows users to explore and engage with 3D art in a modern, intuitive interface.

### Key Features

- **User Authentication (Login / Register)**:  
  Easy-to-use login and sign-up system. Users can create an account or log in quickly with just a few steps.

- **3D Model Viewer**:  
  Uses modelviewer.dev in HTML to display interactive 3D models with no need for extra JavaScript—just a simple module.

- **Secure Database with MySQL**:  
  User data is stored securely using a MySQL database. Passwords are hashed using `werkzeug.security`'s `generate_password_hash` and verified with `check_password_hash`, ensuring strong security practices are followed.

---

## Getting Started

Follow the steps below to set up and run Xela-Gallery locally.

### Prerequisites

Before you begin, ensure you have the following installed:

- **Database Setup in Ubuntu**: [Download Ubuntu](https://ubuntu.com/download/desktop) 
- **Python** (version 3.8 or higher): [Download Python](https://www.python.org/downloads/) 
- **pip**: Python's package installer (comes bundled with Python installations).
- **Virtual Environment** (recommended): To manage project dependencies.


---

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aemrcd/Xela-Gallery.git
   ```

2. **Setup Venv & Activate**:
   - Create a Virtual Environment
     
   ```bash
      python -m venv venv
   ```
   
   - Powershell Activate in Powershell
   ```Powershell
      .\venv\Scripts\Activate     
   ```
   *If the user gets Unauthorised Access Message*
     ```Powershell
     Set-ExecutionPolicy Unrestricted -Scope Process
     ```
3. **Install the Requirements**
    ```bash 
    pip install -r requirements.txt
    ```
    
---
### Database Setup

1. Installing MariaDB to PI/Virtual Machine

  - *Make sure you install Ubuntu on your `PI` & `Virtual Machine`*

  - Press `Windows Key` to open the "Search" menu.
     - Type `Terminal` and press **Enter**. This will open the Terminal Prompt.
     - install MariaDB by typing: 
      ```bash 
      sudo apt install mariadb-server
      ```
      ```bash
      sudo mariadb_secure_installation
      ```
2. Creating and Managing Databases
   
   - Log in to MariaDB as root:
     
     ```bash
     sudo mysql -u root -p
     ```
     
   - Create a new database:
     ```bash
      CREATE DATABASE my_database;
     ```
     
 4. Create a new user and grant privileges:
  ```bash
  CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'password';
  GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost';
  FLUSH PRIVILEGES;
  ```
 4. Exit MariaDB:
  ```bash
  EXIT;
  ```
### 3. Managing Tables in MariaDB:

1. Showing The Database:
- This statement works to show all of your database.
```bash
SHOW DATABASES;
```
2. SELECTING The Database:
- This statement works if you have multiple database.
```bash
USE "yourdatabase";
```
3. Viewing tables in your database
- To see the data inside a table, use the `SELECT` query. Replace `"yourtable"` with the name of the your table  to view.

```bash
SELECT * FROM "yourdatabase";
```
4. Deleting a Row from a Table

- If you want to delete a specific row in a table, use the   `DELETE` statement with a `WHERE` and  Replace `"yourtable"` with the your table name and `"PLACE_YOUR_ID"` with the ID or condition to delete a spesific row.

```bash
SELECT * FROM  "yourdatabase" WHERE Id IN = "PLACE_YOUR_ID";
```
---
### Website View

    
