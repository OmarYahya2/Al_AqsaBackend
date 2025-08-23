#!/usr/bin/env python
"""
Script to create superuser after first deployment
Run this manually after the first successful deployment
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin_user():
    """Create admin user if it doesn't exist"""
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@alaqsamedical.com',
                password='admin123456'
            )
            print("✅ Admin user created successfully!")
            print("Username: admin")
            print("Password: admin123456")
            print("⚠️  Please change the password after first login!")
        else:
            print("ℹ️  Admin user already exists")
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")

if __name__ == "__main__":
    create_admin_user()
