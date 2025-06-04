# Xela-Gallery

Explore 3D Art, Engage Your Imagination Today!

[![Last Commit](https://img.shields.io/github/last-commit/aemrcd/Xela-Gallery)](https://github.com/aemrcd/Xela-Gallery/commits/main) 
[![HTML Percentage](https://img.shields.io/badge/Html-60.6%25-orange)](https://github.com/aemrcd/Xela-Gallery) 
[![Python Percentage](https://img.shields.io/badge/Python-21.4%25-blue)](https://github.com/aemrcd/Xela-Gallery) 
[![CSS](https://img.shields.io/badge/CSS-18.0%25-purple)](https://github.com/aemrcd/Xela-Gallery) 


## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database-Setup](#database-setup)
  - [Website-View](#website-view)

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

### 1. Install MariaDB

Ensure you're running Ubuntu on your Raspberry Pi or VM. Then:

```bash
sudo apt update
sudo apt install mariadb-server
sudo mariadb-secure-installation
```

---

### 2. Create Database and User

Log into MariaDB:

```bash
sudo mysql -u root -p
```

Then execute the following SQL commands:

```sql
CREATE DATABASE my_database;

CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost';

FLUSH PRIVILEGES;

EXIT;
```

---

## Managing Tables

### 1. Show All Databases

```sql
SHOW DATABASES;
```

### 2. Select a Database

```sql
USE my_database;
```

### 3. View Table Contents

```sql
SELECT * FROM users;
```

### 4. Delete a Row From a Table

To delete a row by its ID:

```sql
DELETE FROM users WHERE id = 1;
```

> 🔍 **Note:** Be sure to replace `users` with your table name and `1` with the actual ID you want to delete.

---

### 5. Example: Creating the `users` Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
---
### Website View

    
