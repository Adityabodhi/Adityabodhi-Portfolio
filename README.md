# Adityabodhi Gaikwad — Django Portfolio

A premium, modern full-stack portfolio website built with Django, featuring projects, skills, experience, and a contact form. Fully responsive with dark/light mode and glassmorphism UI.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run setup (migrations + seed data + admin user)
python setup.py

# 3. Start the server
python manage.py runserver
```

Visit → http://127.0.0.1:8000  


## 📄 Customization
1. **Resume**: Replace `portfolio/static/portfolio/resume.pdf` with your actual resume PDF.
2. **Profile Photo**: Update `portfolio/static/portfolio/images/profile.jpg`.
3. **Projects**: Add/edit via the **Admin Panel** at `/admin`.

## 🚢 Deployment (Railway / Render / Heroku)

This project is deployment-ready with **WhiteNoise** for static files and **Gunicorn**.

### 1. Environment Variables
Create a `.env` file (or set in your hosting provider) based on `.env.example`:
- `SECRET_KEY`: A long, random string.
- `DEBUG`: `False` for production.
- `ALLOWED_HOSTS`: Your domain (e.g., `yourapp.up.railway.app`).

### 2. Deployment Steps (Railway)
1. Push your code to a GitHub repository.
2. Connect the repository to [Railway](https://railway.app/).
3. Railway will automatically detect the `Procfile` and `runtime.txt`.
4. Add your environment variables in the Railway dashboard.
5. Deploy!

## 📁 Project Structure
```
portfolio_django/
├── manage.py
├── setup.py              ← Run this first!
├── requirements.txt
├── Procfile              ← For deployment
├── runtime.txt           ← Python version
├── .env.example          ← Template for env vars
└── portfolio/
    ├── settings.py       ← Updated with production settings
    ├── urls.py
    ├── static/           ← Static assets (CSS, JS, Images, Resume)
    └── templates/        ← HTML files (index.html, etc.)
```

## 🛠 Tech Stack
- **Backend**: Django 4.2
- **Frontend**: Vanilla HTML/CSS/JS (Glassmorphism, Syne & DM Sans fonts)
- **Deployment**: WhiteNoise, Gunicorn, Railway/Heroku-ready
- **Images**: Pillow, AI-generated project backgrounds
