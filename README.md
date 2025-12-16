# 💰 Django Expense Tracker Application

A **Django-based Expense Tracker web application** that helps users **track income, expenses, and current balance** with secure authentication. The project demonstrates Django fundamentals such as **models, views, authentication, admin customization, and ORM aggregation**.

## 🚀 Features

### 🔐 User Authentication

* User **registration**
* Secure **login & logout**
* Route protection using `login_required`
* Built using Django’s built-in authentication system

### 💵 Expense Management

* Add income (CREDIT)
* Add expenses (DEBIT)
* Automatic **current balance calculation**
* Delete individual transactions
* View transaction history

### 📊 Financial Summary

* Total income calculation
* Total expense calculation
* Live current balance update

## 🏗 Project Structure

```
tracker/
│
├── admin.py        # Admin panel configuration
├── apps.py         # App configuration
├── models.py       # Database models
├── urls.py         # URL routing
├── views.py        # Business logic
├── tests.py        # Test placeholders
│
templates/
├── index.html      # Dashboard
├── login.html      # Login page
├── register.html   # Registration page
```

## 🧠 Database Models

### 📌 CurrentBalance

* Stores the user’s current balance
* Automatically updated on every transaction

### 📌 HistoryTracker

* Tracks all transactions
* Fields:
  * Amount
  * Expense type (`CREDIT` / `DEBIT`)
  * Description
  * Created date

### 📌 RequestLogs *(Optional / Future Use)*

* Designed to log request metadata
* Useful for debugging or analytics

## 🔁 Application Workflow

1. User **registers**
2. User **logs in**
3. Dashboard displays:

   * Current balance
   * Total income
   * Total expenses
   * Transaction history
4. User can:

   * Add income or expense
   * Delete transactions
5. Balance updates automatically
6. User can **log out**

## 🖥 Technologies Used

* **Python**
* **Django**
* **Django ORM**
* **SQLite (default)**
* **HTML / CSS**
* **Django Messages Framework**

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/django-expense-tracker.git
cd django-expense-tracker
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

## 🛠 Admin Panel

* Custom admin branding
* Transaction history visible
* Balance management via admin dashboard

Access:

```
http://127.0.0.1:8000/admin/
```

## 🔒 Security Highlights

* Django authentication system
* Password hashing
* Protected routes using decorators
* Input validation for transactions

## 📌 Future Enhancements

* User-specific balances (multi-user tracking)
* Monthly expense charts
* Category-wise expenses
* REST API support
* Export reports (CSV / PDF)
* Frontend upgrade (Bootstrap / Tailwind)

## 👨‍💻 Author

**Shivam Singh**
Aspiring Data Analyst & Software Developer
Diploma in IT | B.Tech CSE (Pursuing)

Just say the word 👍
