# 🍽️ Restaurant Menu QR Code Generator

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.x-green?style=for-the-badge&logo=django)
![QR Code](https://img.shields.io/badge/QRCode-Generation-orange?style=for-the-badge)

A full-stack web application built with **Python & Django** that allows restaurant owners to generate, manage, and share QR codes linked to their digital menus. Customers can scan the QR code with any smartphone to instantly view the restaurant's menu — no app required.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Workflow](#-workflow)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Use Cases](#-use-cases)
- [Advantages](#-advantages)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)

---

## ✨ Features

- 🔐 Restaurant owner authentication (Register / Login / Logout)
- 🍕 Create and manage digital menus with categories & items
- 📷 Auto-generate unique QR codes for each menu
- 🖨️ Download QR codes as PNG for printing
- 📱 Mobile-friendly menu view for customers
- 🔄 Real-time menu updates reflected instantly on scan
- 🗂️ Manage multiple menus per restaurant
- 🌐 Shareable public menu URL

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | Python 3.10+, Django 6.x |
| Frontend    | HTML5, CSS3, Bootstrap 5 |
| Database    | SQLite (Dev) / PostgreSQL (Prod) |
| QR Library  | `qrcode`, `Pillow`      |
| Auth        | Django Auth System      |
| Storage     | Django Media Files      |

---

## 📁 Project Structure

```
restaurant-qr-menu/
│
├── manage.py                    # Django project entry point
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not committed)
├── .gitignore
├── README.md
│
├── config/                      # Project-level settings
│   ├── __init__.py
│   ├── settings.py              # Django settings (DB, Auth, Media, etc.)
│   ├── urls.py                  # Root URL configuration
│   └── wsgi.py
│
├── accounts/                    # User authentication app
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       └── register.html
│   ├── admin.py
│   ├── forms.py                 # Login & Registration forms
│   ├── models.py                # Custom User / Restaurant Profile model
│   ├── urls.py
│   └── views.py                 # Register, Login, Logout views
│
├── menu/                        # Core menu management app
│   ├── migrations/
│   ├── templates/
│   │   └── menu/
│   │       ├── dashboard.html   # Owner dashboard
│   │       ├── menu_form.html   # Create/Edit menu
│   │       ├── menu_detail.html # Manage items in a menu
│   │       └── public_menu.html # Customer-facing menu view
│   ├── admin.py
│   ├── forms.py                 # Menu & MenuItem forms
│   ├── models.py                # Menu, Category, MenuItem models
│   ├── urls.py
│   └── views.py                 # CRUD views for menus and items
│
├── qr_generator/                # QR Code generation app
│   ├── migrations/
│   ├── templates/
│   │   └── qr_generator/
│   │       └── qr_display.html  # QR preview + download page
│   ├── admin.py
│   ├── models.py                # QRCode model (stores generated QR image)
│   ├── urls.py
│   ├── utils.py                 # QR generation logic using `qrcode` library
│   └── views.py                 # Generate, display, and download QR views
│
├── static/                      # Global static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│
└── media/                       # User-uploaded & generated files
    └── qrcodes/                 # Generated QR code images stored here
```

---

## 🔄 Workflow

```
┌─────────────────────────────────────────────────────┐
│                   RESTAURANT OWNER                  │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │  Register / Login       │
          │  (accounts app)         │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │  Create Digital Menu    │  ← Add categories, items,
          │  (menu app)             │     prices, descriptions
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │  Generate QR Code       │  ← Unique URL embedded
          │  (qr_generator app)     │     into QR image (PNG)
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │  Download & Print QR    │  ← Place on tables,
          │  Code PNG               │     receipts, posters
          └────────────┬────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│                     CUSTOMER                        │
│                                                     │
│   📱 Scans QR Code  →  Opens public menu URL in    │
│      browser        →  Views menu (no app needed)  │
└─────────────────────────────────────────────────────┘
```

### Step-by-Step Flow

1. **Owner Registers** → Creates restaurant profile
2. **Creates a Menu** → Adds categories (Starters, Mains, Desserts) and items with prices
3. **Generates QR Code** → System creates a unique URL (`/menu/view/<uuid>/`) and encodes it into a QR image using the `qrcode` library
4. **QR Saved** → PNG stored in `media/qrcodes/`, path saved in database
5. **Owner Downloads/Prints** QR code and places it on tables
6. **Customer Scans** → Browser opens the public menu page — live, always up-to-date

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/restaurant-qr-menu.git
cd restaurant-qr-menu

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (admin access)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

### Requirements (`requirements.txt`)

```
Django>=4.2
qrcode[pil]
Pillow
python-decouple
psycopg2-binary       # For PostgreSQL (optional)
```

---

## 🚀 Usage

| Role            | Action                                                                 |
|-----------------|------------------------------------------------------------------------|
| Restaurant Owner | Register → Create menu → Add items → Generate QR → Download & print  |
| Customer         | Scan QR code with phone → View menu in browser                        |
| Admin            | Manage all users, menus, and QR codes via `/admin/` panel             |

---

## 💡 Use Cases

- 🍔 **Fast Food Outlets** — Display QR codes at the counter for a paperless menu experience
- 🍷 **Fine Dining Restaurants** — Elegant table QR codes replace physical menus
- ☕ **Cafés & Bakeries** — Quick seasonal menu updates without reprinting
- 🏨 **Hotels & Resorts** — Room service menus accessible via QR on the room TV or table
- 🎪 **Food Stalls & Events** — Lightweight, portable digital menu for pop-ups and fairs
- 🌍 **Multi-language Menus** — Future-ready for serving menus in multiple languages via one QR

---

## 🏆 Advantages

### For Restaurant Owners
| Advantage | Description |
|-----------|-------------|
| 💰 Cost Saving | Eliminate recurring printing costs for physical menus |
| ⚡ Instant Updates | Change prices or items anytime — no reprint needed |
| 🌿 Eco-Friendly | Reduce paper waste significantly |
| 📊 Scalable | Manage multiple menus / branches from one dashboard |
| 🔒 Secure | Only authenticated owners can modify menus |

### For Customers
| Advantage | Description |
|-----------|-------------|
| 📱 No App Needed | Works directly in any smartphone browser |
| 🚀 Fast Access | Scan → View in under 2 seconds |
| 🧼 Hygienic | No shared physical menus (important post-pandemic) |
| 🔗 Shareable | Customers can share the menu link with friends |

### For Developers
| Advantage | Description |
|-----------|-------------|
| 🧩 Modular Django Apps | Clean separation of concerns across apps |
| 🔧 Easily Extensible | Add features like PDF menus, analytics, or multilingual support |
| 🐳 Docker Ready | Can be containerized for easy deployment |

---

## 📸 Screenshots

> *(Add your project screenshots here)*

| Dashboard | QR Code View | Customer Menu |
|-----------|-------------|---------------|
| ![Dashboard](screenshots/dashboard.png) | ![QR](screenshots/qr_view.png) | ![Menu](screenshots/menu.png) |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@samar_gupta](https://github.com/samar-12-23)
- LinkedIn: [yourlinkedin](https://www.linkedin.com/in/samar-gupta-449536284/)
- Email: samargupta0206@gmail.com

---

> ⭐ If you found this project helpful, please consider giving it a star on GitHub!
