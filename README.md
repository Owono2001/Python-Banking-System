# 🏦 Banking Service System in Python 🐍

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## ✨ Introduction
A **menu-driven banking system** developed for an Introduction to Programming course, featuring secure multi-user access and essential banking operations. Built with pure Python and file-based persistence.

---

## 🌟 Key Features

### **User Roles & Security**
- 👑 **Super Admin** (Default: `admin`/`admin1234`)
  - Create/manage staff accounts
- 👔 **Staff Members**
  - Add/edit customer profiles
  - Generate transaction reports
- 👤 **Customers**
  - Secure login with account number & password
  - Full transaction management

### **Banking Operations**
- 💰 **Deposits/Withdrawals**
  - Real-time balance updates
  - Account-type specific minimum balances:
    - 💵 Savings Account: RM100 minimum
    - 💼 Current Account: RM500 minimum
- 🔢 **Auto-Generated Account Numbers**
  - Unique 10-digit format (e.g., `0562800001`)
- 📊 **Financial Reporting**
  - Custom date-range statements
  - Deposit/withdrawal summaries

### **Data Management**
- 📁 **File-Based Storage**
  - `customer_details.txt`: Customer profiles
  - `accounts`: Transaction records
  - `admin_staff_details`: Staff credentials
- 🔄 **Profile Updates**
  - Modify DOB, account type, passwords
  - Transaction history preservation

---

## 🛠️ Technical Implementation

### **Core Components**
| File                | Description                                  |
|---------------------|----------------------------------------------|
| `main.py`           | Entry point with login system               |
| `Customer_Fun.py`   | Customer transactions & password management |
| `Staff_Fun.py`      | Customer CRUD operations & reporting        |
| `SuperUser_Fun.py`  | Staff account creation                       |
| `python2pseudo.py`  | Python-to-pseudocode converter              |

### **Key Functions**
- `Balance()`: Real-time balance calculation
- `Report()`: Date-filtered transaction history
- `Change_password()`: Secure credential updates
- `Add_Customer()`: Auto-account number generation

---

## 🚀 Getting Started

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/python-banking-system.git
   cd python-banking-system
   
