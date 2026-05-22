# 🍽️ Restaurant Menu QR Code Generator

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.x-green?style=for-the-badge&logo=django)
![QR Code](https://img.shields.io/badge/QRCode-Generation-orange?style=for-the-badge)

A free-to-use web application built with **Python & Django** that allows any restaurant owner to generate QR codes for their menu. The owner simply submits a **Google Drive link or any menu URL** (PDF, image, or webpage), and the app encodes it into a single QR code. This **same QR code** is then assigned to each table in the restaurant — every table is individually recorded in the database, but all tables share the same generated QR image. Customers scan the QR from any table and instantly access the menu. No login required for customers, no app needed.

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

- 🆓 **Free for all** — any restaurant owner can register and use the app at no cost
- 🔐 Owner registration & login to access the QR generator dashboard
- 🔗 Accept a **Google Drive link or any menu URL** (PDF, image, webpage) as input
- 📷 Generate a single QR code that encodes the provided menu link
- 🪑 Owner defines the **number of tables** — each table is saved as a separate record in the database
- 🔁 **Same QR code** is used across all tables (one menu link = one QR for the whole restaurant)
- 🖨️ Download the QR code as PNG for printing and placing on each table
- 📱 Customers scan QR from any table → menu opens instantly in browser, no login needed
- 🌐 Simple, clean form-based interface — no complex menu builder required

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | Python 3.10+, Django 6.x |
| Frontend    | HTML5, Bootstrap 5 (CDN), JavaScript (CDN) |
| Database    | SQLite (Dev) / PostgreSQL (Prod) |
| QR Library  | `qrcode`, `Pillow`      |
| Input       | Google Drive Link / Any Menu URL |
| Styling CDN | Bootstrap CSS via jsDelivr / cdnjs |
| JS CDN      | Bootstrap JS / jQuery via jsDelivr / cdnjs |
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
│   ├── models.py                # Restaurant owner / User profile model
│   ├── urls.py
│   └── views.py                 # Register, Login, Logout views
│
├── qr_generator/                # Core QR Code generation app
│   ├── migrations/
│   ├── templates/
│   │   └── qr_generator/
│   │       ├── index.html       # Form: enter restaurant name + Drive/menu link
│   │       └── qr_display.html  # QR code preview + download page
│   ├── admin.py
│   ├── forms.py                 # QRCodeForm (restaurant name, menu link/URL, no. of tables)
│   ├── models.py                # QRCode model (menu URL, QR image path) + Table model (table number, linked to QRCode)
│   ├── urls.py
│   ├── utils.py                 # QR generation logic using `qrcode` + `Pillow`
│   └── views.py                 # Handle form input → generate QR → display/download
│
├── static/                      # Global static files (minimal — styling via CDN)
│   └── images/                  # Local images/icons if any
│
│   # NOTE: Bootstrap CSS & JS are loaded via CDN links in base HTML template
│   # No local css/ or js/ folders needed
│
└── media/                       # Generated QR code images stored here
    └── qrcodes/
```

---

## 🔄 Workflow

```
┌─────────────────────────────────────────────────────┐
│          ANY RESTAURANT OWNER  (Free to use)        │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │  Register / Login       │
          │  (Free, no cost)        │
          └────────────┬────────────┘
                       │
                       ▼
          ┌──────────────────────────────────┐
          │  Fill the QR Generator Form      │
          │  - Restaurant Name               │
          │  - Paste Google Drive link or    │
          │    any Menu URL (PDF/image/page) │
          │  - Number of Tables              │
          └────────────┬─────────────────────┘
                       │
                       ▼
          ┌──────────────────────────────────┐
          │  Django saves each table as a    │
          │  separate DB record              │
          │  (Table 1, Table 2 ... Table N)  │
          │  All linked to the same QRCode   │
          └────────────┬─────────────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │  Single QR Code PNG     │
          │  generated from the     │
          │  menu URL via `qrcode`  │
          │  + `Pillow`, saved to   │
          │  media/qrcodes/         │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │  Owner downloads the    │  ← Same QR printed &
          │  QR Code PNG            │    placed on every table
          └────────────┬────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│               CUSTOMER (No login needed)            │
│                                                     │
│   📱 Scans QR from any table → Browser opens the   │
│      Drive link / menu URL (PDF, image, page)       │
└─────────────────────────────────────────────────────┘
```

### Step-by-Step Flow

1. **Any owner registers for free** → No subscription or payment required
2. **Fills the form** → Enters the restaurant name, pastes a **Google Drive link or menu URL**, and specifies the number of tables
3. **Tables recorded in DB** → Each table (Table 1, Table 2, ... Table N) is stored as an individual record in the database, all linked to the same QR code entry
4. **Single QR code generated** → Django passes the menu URL to `utils.py`, which uses the `qrcode` library to encode it into one QR image (PNG) — the same image applies to all tables
5. **Owner downloads & prints** → Prints the single QR code and places it on every table in the restaurant
6. **Customer scans** → No login, no app — phone camera opens the menu link directly from any table

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
Django>=6.0
qrcode[pil]
Pillow
python-decouple
psycopg2-binary       # For PostgreSQL (optional)
```

---

## 🚀 Usage

| Role            | Action                                                                                          |
|-----------------|-------------------------------------------------------------------------------------------------|
| Restaurant Owner | Register free → Paste menu link → Enter table count → Generate QR → Download & print on tables |
| Customer         | Scan QR from any table → Menu opens in browser instantly, no login or app needed               |
| Admin            | View and manage all registered owners, QR records, and table entries via `/admin/` panel        |

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
| 🆓 Completely Free | Any owner can register and use the app at zero cost |
| ⚡ Super Simple | Paste a Drive link or menu URL, enter table count — QR is ready instantly |
| 🪑 Per-Table Tracking | Each table is individually recorded in the DB for clear management and future scalability |
| 🔁 One QR for All Tables | A single QR code image is generated and reused across every table — no need to create separate codes |
| 💰 Cost Saving | Eliminate recurring menu printing costs; update the Drive file anytime without a new QR |
| 🔗 Works with Existing Menus | Any shareable Drive link or hosted menu URL works out of the box |
| 🌿 Eco-Friendly | Go fully digital and reduce paper waste |

### For Customers
| Advantage | Description |
|-----------|-------------|
| 📱 No App, No Login | Just scan — menu opens directly in the phone browser, zero friction |
| 🚀 Instant Access | Scan → menu visible in under 2 seconds |
| 🧼 Hygienic | No shared physical menus passed between customers |
| 🔗 Shareable | Customers can forward the menu link to anyone |

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
- GitHub: [@samar-12-23](https://github.com/samar-12-23)
- LinkedIn: [samar-gupta-339536284](https://www.linkedin.com/in/samar-gupta-449536284/)
- Email: samargupta0206@gmail.com

---

> ⭐ If you found this project helpful, please consider giving it a star on GitHub!
