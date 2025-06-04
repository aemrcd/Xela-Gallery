# Xela-Gallery

Explore 3D Art, Engage Your Imagination Today!

[![Last Commit](https://img.shields.io/github/last-commit/aemrcd/Xela-Gallery)](https://github.com/aemrcd/Xela-Gallery/commits/main) 
[![HTML Percentage](https://img.shields.io/badge/html-60.6%25-blue)](https://github.com/aemrcd/Xela-Gallery) 
[![Python Percentage](https://img.shields.io/badge/python-39.4%25-yellow)](https://github.com/aemrcd/Xela-Gallery) 


Built with the tools and technologies:
- [Python](https://www.python.org/) 
- [GitHub Actions](https://github.com/features/actions) 

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)

---

## Overview

Xela-Gallery is a powerful Flask-based web application designed to showcase 3D models while ensuring an immersive and interactive user experience. It allows users to explore and engage with 3D art in a modern, intuitive interface.

### Key Features

- **User Authentication (Login / Register)**:  
  Intuitive and user-friendly login and registration system designed for ease of use across all devices — from desktops to mobile phones.

- **3D Model Viewer**:  
  Built-in interactive viewer powered by WebGL/Three.js for seamless display and manipulation of 3D models directly in the browser.

- **User-Friendly Interface**:  
  Clean, modern, and responsive design ensuring smooth navigation and a great experience on any device and modern browser.

- **Secure Database with MySQL**:  
  User data is stored securely using a MySQL database. Passwords are hashed using `werkzeug.security`'s `generate_password_hash` and verified with `check_password_hash`, ensuring strong security practices are followed.

---

## Getting Started

Follow the steps below to set up and run Xela-Gallery locally.

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (version 3.8 or higher): [Download Python](https://www.python.org/downloads/) 
- **pip**: Python's package installer (comes bundled with Python installations).
- **Virtual Environment** (recommended): To manage project dependencies.
- **MySQL Server**: For local database setup.

---

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aemrcd/Xela-Gallery.git 
   cd Xela-Gallery
