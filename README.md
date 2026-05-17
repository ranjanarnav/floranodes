# FloraNodes - Django Hosting Website

FloraNodes is a full-stack hosting website built with Django, featuring VPS hosting plans, dedicated server pages, a checkout system, contact management, responsive UI, and production-ready deployment support.

---

## 🌐 Features

- VPS Hosting Plans
- Dedicated Hosting Pages
- Responsive Modern UI
- Checkout System
- Contact Form Management
- Policy Pages (Privacy Policy, Refund Policy, Terms of Service)
- Static & Media File Support
- Production Deployment Ready

---

## 🛠 Tech Stack

### Backend
- Django
- Python
- SQLite3

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

---

## 📂 Project Structure

```bash
FloraNodes/
│── manage.py
│── requirements.txt
│── db.sqlite3
│
├── GlichX/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── static/
├── staticfiles/
└── category_icons/
```

---

# ⚙️ Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/ranjanarnav/floranodes.git
```

---

## 2. Navigate to Project Folder

```bash
cd floranodes
```

---

## 3. Create Virtual Environment

### Windows

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Apply Database Migrations

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

## 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## 7. Collect Static Files

```bash
python manage.py collectstatic
```

Type:

```bash
yes
```

when prompted.

---

## 8. Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

Visit:

```text
http://127.0.0.1:8000/admin
```

Login using your superuser credentials.

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Deployment

For production deployment:

1. Set:

```python
DEBUG = False
```

2. Configure:

```python
ALLOWED_HOSTS = []
```

3. Collect static files:

```bash
python manage.py collectstatic
```

4. Configure static and media file serving.

5. Use **Gunicorn + Nginx** for Linux VPS deployment.

6. Store sensitive values in a `.env` file.

---

## 👨‍💻 Developer

Developed by **Arnav Ranjan** as a Django full-stack project for learning and portfolio development.

GitHub:  
https://github.com/ranjanarnav

---

## 📌 Project Purpose

FloraNodes was built to explore and practice:

- Django Full-Stack Development
- Hosting Website Architecture
- Responsive Frontend Design
- Static & Media File Handling
- Checkout Flow Integration
- Deployment Concepts

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful, consider giving it a **star** on GitHub.
