# 🏦 Banking Service System in Python 🐍

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/maintenance/yes/2025.svg)](https://github.com/your-github-username/your-repository-name) [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## ✨ Introduction

This **Banking Service System** was crafted with 💖 using Python for the Introduction to Programming assignment. It's designed to efficiently manage customer accounts, providing a user-friendly menu-driven interface for both customers and administrative staff.

## 🌟 Key Features

This system is packed with features to make banking operations smooth and secure:

* **🔑 Secure Login:** Separate and secure login for administrators (Super User), staff, and customers.
* **👥 Role-Based Access:**
    * **Super User:** Can create Staff users. (Default: `admin`/`admin1234`)
    * **Staff:** Can add new customers, edit existing customer details (excluding ID/name), and view customer transaction reports.
    * **Customer:** Can change password, deposit/withdraw funds, check balance, and view transaction reports. Log in using the assigned **Account Number**.
* **💸 Customer Transactions:** Customers can easily manage their funds:
    * Deposit money into their accounts 💰.
    * Withdraw funds from their accounts 💳.
* **💼 Administrative Management:** Staff have tools to manage customers:
    * Register new customers 📝.
    * Update customer details (excluding sensitive information like ID and name) ✏️.
* **🔢 Automated Account Numbers:** Unique account numbers are generated automatically upon customer creation.
* **📊 Multiple Account Types:** Supports two popular account types with minimum balance requirements:
    * Savings Account: Minimum balance of RM100 🛡️.
    * Current Account: Minimum balance of RM500 💼.
* **🧾 Account Statements:** Customers can view detailed statements, including deposits, withdrawals, and totals.
* **💾 Data Persistence:** All crucial data (users, customers, accounts, transactions) is stored securely in text files.
* **✅ Robust Input Validation:** Incorporates checks to prevent errors and maintain data integrity.

## 🛠️ Technologies Used

* **🐍 Python:** The backbone of this application.
* **📦 Standard Library:** Leveraging Python's built-in modules for file handling, date/time operations, etc.

## 📂 Project Structure

The project follows a modular design:

* **🧩 Functions:** Encapsulating specific tasks into reusable blocks of code.
* **<0xF0><0x9F><0x97><0x8B>️ Lists & Data Structures:** Managing collections of data like users, customer accounts, and transactions.
* **📄 File Handling:** Reading and writing data to text files (`users.txt`, `customers.txt`, `accounts.txt`, `transactions.txt`).

## 🚀 Getting Started

Ready to run the banking system? Here's how:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
    *(Replace `<repository_url>` with the actual URL of your repository)*

2.  **Navigate to the project directory:**
    ```bash
    cd Python-Banking-System-main # Or your repository name
    ```
3.  **(Optional but Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4.  **Run the main script:**
    ```bash
    python main.py
    ```

    Follow the prompts on your screen to interact with the system.

## 🧑‍🤝‍🧑 Usage

Once the script is running, you'll be greeted with the main login prompt.

* **Super User:** Log in using administrator credentials (e.g., `admin`/`admin1234`) to create staff users.
* **Staff:** Log in with staff credentials (created by the Super User) to manage customer accounts (add, edit, view reports).
* **Customer:** Log in with your **Account Number** (generated when the staff adds you) and password to access your account transactions and details.

### Example Walkthrough

This example demonstrates the core workflow, covering several key steps from initial execution to customer transactions:

1.  **Initialization:** Running the `main.py` script presents the main welcome and login screen.
2.  **Super User Actions:** Logging in as the `admin` Super User (using credentials like `admin`/`admin1234`) allows access to the SuperUser Menu. From here, a new Staff user (`pedro`) is created with their own username and password. The Super User then logs out.
3.  **Staff User Actions:** The newly created `pedro` Staff user logs in using their credentials. They access the Staff Menu and choose to add a new Customer (`Fabian`). During this process, customer details (name, DOB, account type) and a password are provided. Note the automatically generated `Account Number` (e.g., `0562800001`) provided upon successful customer creation, which is crucial for the customer's login. The Staff user then logs out.
4.  **Customer Login Process:** The example highlights the correct login procedure for customers. It shows **failed attempts** when trying to log in using the customer's *name* (`Fabian`) or internal *ID* (`1`). It then demonstrates the **successful login** using the assigned **Account Number** (`0562800001`) and the password set during creation (`fabiancustomer`).
5.  **Customer Transactions & Validation:** Once logged in as the customer (`0562800001`), the example shows accessing the customer menu. A successful deposit transaction (`1000`) is performed. Subsequently, it demonstrates the system's input validation by attempting a withdrawal (`2000`) that would breach the minimum balance requirement for the Savings account (RM100), resulting in a clear transaction error message displaying the current balance.


## 🛠️ Technologies Used

* **🐍 Python:** The backbone of this application, providing a versatile and readable language.
* **📦 Standard Library:** Leveraging Python's built-in modules for efficient file handling and other essential operations.

## 📂 Project Structure

The project follows a modular design, making it easy to understand and maintain:

* **🧩 Functions:** Encapsulating specific tasks into reusable blocks of code.
* **<0xF0><0x9F><0x97><0x8B>️ Lists:** Efficiently managing collections of data like customer accounts and transactions.
* **📄 File Handling:** Reading and writing data to text files for persistent storage.

## 🚀 Getting Started

Ready to run the banking system? Here's how:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
    *(Replace `<repository_url>` with the actual URL of your repository)*

2.  **Navigate to the project directory:**
    ```bash
    cd your-repository-name
    ```

3.  **Run the main script:**
    ```bash
    python main.py  # Or the name of your main script
    ```

    Follow the prompts on your screen to interact with the system as either an administrator or a customer.

## 🧑‍🤝‍🧑 Usage

Once the script is running, you'll be greeted with a main menu. Choose the appropriate option based on your role:

* **Admin:** Log in using administrator credentials to manage customer accounts and system settings.
* **Customer:** Log in with your unique customer ID and PIN to access your account transactions and statements.

## 🔮 Future Enhancements

While the current system is robust, here are some exciting possibilities for future development:

* **<0xF0><0x9F><0x97><0x84> Database Integration:** Moving from text files to a more scalable database system.
* **🛡️ Enhanced Security:** Implementing advanced security measures like password hashing and data encryption.
* **🎨 Graphical User Interface (GUI):** Creating a visual interface for an even better user experience.
* **🌐 Online Transactions:** Adding features like online transfers and bill payments.
* **📊 Advanced Reporting:** Implementing more detailed transaction history and reporting capabilities.

## 📜 License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for complete details.

## 🙏 Acknowledgements

A big thank you to the instructors of the Introduction to Programming in Python course for this valuable learning experience!
