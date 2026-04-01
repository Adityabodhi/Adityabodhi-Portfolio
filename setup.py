#!/usr/bin/env python
"""
Run this script to set up your portfolio database with sample data.
Usage: python setup.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User
from portfolio.models import Skill, Project, Experience

print("Running migrations...")
from django.core.management import call_command
call_command('makemigrations', 'portfolio', verbosity=0)
call_command('migrate', verbosity=0)

print("Seeding skills...")
skills_data = [
    ('Python', 'languages', 90, 1),
    ('JavaScript', 'languages', 75, 2),
    ('HTML/CSS', 'languages', 85, 3),
    ('SQL', 'languages', 80, 4),
    ('Flask', 'frameworks', 85, 5),
    ('Django', 'frameworks', 80, 6),
    ('Scikit-learn', 'ml', 82, 7),
    ('TensorFlow', 'ml', 70, 8),
    ('MySQL', 'frameworks', 80, 9),
    ('SQLite', 'frameworks', 85, 10),
    ('Git & GitHub', 'tools', 85, 11),
    ('Jupyter Notebook', 'ml', 90, 12),
    ('Pandas & NumPy', 'ml', 88, 13),
    ('Matplotlib', 'ml', 80, 14),
]
Skill.objects.all().delete()
for name, cat, pct, order in skills_data:
    Skill.objects.create(name=name, category=cat, proficiency=pct, order=order)

print("Seeding projects...")
projects_data = [
    ('Hospital Management System', 'A Flask + MySQL web app for managing hospital appointments. Supports Doctor and Patient roles — patients can book, edit, or delete appointments; doctors can view all bookings.', 'Flask, MySQL, HTML, CSS, Python', 'https://github.com/Adityabodhi/Hospital_managemnt_system', '', True, 1),
    ('Crop Recommendation', 'A machine learning project that recommends suitable crops based on soil and climate parameters using classification algorithms in Jupyter Notebook.', 'Python, Scikit-learn, Pandas, Jupyter, NumPy', 'https://github.com/Adityabodhi/Crop_reccomendation', '', True, 2),
    ('Alzheimer\'s Aid', 'A Python-based AI tool for assisting with Alzheimer\'s disease detection using deep learning and medical image analysis.', 'Python, TensorFlow, Deep Learning, CNN', '', '', True, 3),
    ('Student Record System', 'A Python application for managing student records with full CRUD operations using file handling and database backend.', 'Python, SQLite, CRUD', '', '', True, 4),
    ('Crypto Tracker', 'A JavaScript web app tracking live cryptocurrency prices by integrating with a public crypto API using async fetch and DOM manipulation.', 'JavaScript, REST API, HTML, CSS', 'https://github.com/Adityabodhi/Crypto_tracker', '', True, 5),
    ('Mileage Predictor', 'A machine learning regression model predicting vehicle mileage (MPG) based on car attributes like engine size, weight, and horsepower.', 'Python, Scikit-learn, Matplotlib, Seaborn, Regression', 'https://github.com/Adityabodhi/Mileage-Predictor', '', True, 6),
]
Project.objects.all().delete()
for title, desc, tech, gh, live, featured, order in projects_data:
    Project.objects.create(title=title, description=desc, tech_stack=tech, github_url=gh, live_url=live, is_featured=featured, order=order)

print("Seeding experience...")
Experience.objects.all().delete()
Experience.objects.create(
    role='Artificial Intelligence Intern',
    company='CodeClause (Remote)',
    duration='Jan 2024 – Feb 2024',
    description='Used Python for data analysis and ML model experimentation. Worked with structured datasets to implement and evaluate AI solutions.',
    order=1
)
Experience.objects.create(
    role='Web Development Intern',
    company='Bright Career Infotech',
    duration='Jul 2022 – Aug 2022',
    description='Built an employee data management system with validation and DB integration. Developed data-driven web modules for CRUD operations.',
    order=2
)
Experience.objects.create(
    role='BE - Artificial Intelligence and Data Science',
    company='Savitribai Phule University Pune',
    duration='2023 – Present',
    description='Studying core CS concepts including Data Structures, Algorithms, DBMS, and AI/ML. Built multiple projects combining web development and machine learning.',
    order=3
)
Experience.objects.create(
    role='Self-Taught Full-Stack & ML Developer',
    company='Independent Projects',
    duration='2022 – Present',
    description='Built and deployed full-stack web applications, ML models, and data tools. Worked with Flask, Django, MySQL, Python, JavaScript, and modern ML libraries.',
    order=4
)

# Create superuser if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@portfolio.com', 'admin123')
    print("Superuser created: admin / admin123")

print("\n✅ Setup complete!")
print("Run: python manage.py runserver")
print("Visit: http://127.0.0.1:8000")
print("Admin: http://127.0.0.1:8000/admin  (admin / admin123)")
