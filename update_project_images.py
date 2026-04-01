import os
import shutil
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio.models import Project

# Define mappings from title keywords to static image names
IMAGE_MAPPING = {
    'Hospital': 'hospital.png',
    'Crop': 'crop.png',
    'Alzheimer': 'alzheimer.png',
    'Student': 'student.png',
    'Crypto': 'crypto.png',
    'Mileage': 'mileage.png'
}

# Ensure media/projects directory exists
media_projects_dir = os.path.join(settings.MEDIA_ROOT, 'projects')
os.makedirs(media_projects_dir, exist_ok=True)

static_images_dir = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'portfolio', 'images')

print("Syncing project images...")
for project in Project.objects.all():
    # Find matching image based on title
    image_name = None
    for keyword, filename in IMAGE_MAPPING.items():
        if keyword in project.title:
            image_name = filename
            break
    
    if image_name:
        src_path = os.path.join(static_images_dir, image_name)
        if os.path.exists(src_path):
            # Target path in media
            dest_path = os.path.join(media_projects_dir, image_name)
            shutil.copy2(src_path, dest_path)
            
            # Update database record
            project.image = f"projects/{image_name}"
            project.save()
            print(f"Updated {project.title} with {image_name}")
        else:
            print(f"Static image not found for {project.title}: {src_path}")
    else:
        print(f"No image mapping found for {project.title}")

print("\n✅ Image sync complete!")
