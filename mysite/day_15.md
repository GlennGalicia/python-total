# 📘 Day 15

## Django Framework

## Table of Contents

1. [What is Django](#what-is-django)
2. [Installation](#installation)
3. [Django Project Structure](#django-project-structure)
4. [Basic Concepts](#basic-concepts)
5. [Additional Resources](#additional-resources)

---

## What is Django?

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. It follows the MVT (Model-View-Template) pattern and includes everything you need to build web applications.

**Use cases:**

- Web applications
- Content management systems
- E-commerce platforms
- Social networks
- REST APIs
- Admin dashboards
- Blog platforms

## Installation

### With UV (recommended)

```bash
# Create project
uv init myproject
cd myproject

# Add Django
uv add django

# Verify installation
uv run python -m django --version
```

### Creating a Django Project

```bash
# Create Django project
uv run django-admin startproject mysite .

# Project structure created:
# mysite/
#   __init__.py
#   settings.py
#   urls.py
#   asgi.py
#   wsgi.py
# manage.py
```

### Creating an App

```bash
# Create an app
uv run python manage.py startapp blog

# App structure:
# blog/
#   migrations/
#   __init__.py
#   admin.py
#   apps.py
#   models.py
#   tests.py
#   views.py
```

## Django Project Structure

```
myproject/
├── .venv/
├── pyproject.toml
├── manage.py              # Command-line utility
├── mysite/                # Project settings
│   ├── __init__.py
│   ├── settings.py        # Configuration
│   ├── urls.py            # URL routing
│   ├── asgi.py
│   └── wsgi.py
└── blog/                  # Your app
    ├── migrations/        # Database migrations
    ├── __init__.py
    ├── admin.py           # Admin interface
    ├── apps.py
    ├── models.py          # Database models
    ├── tests.py           # Tests
    └── views.py           # View functions
```

## Basic Concepts

### 1. Settings (settings.py)

```python
# mysite/settings.py

# Add your app to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Your app
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_URL = '/static/'
```

### 2. Models (models.py)

```python
# blog/models.py
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
```

### 3. Creating Database Tables

```bash
# Create migrations
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Output:
# Operations to perform:
#   Apply all migrations: admin, auth, blog, ...
# Running migrations:
#   Applying blog.0001_initial... OK
```

### 4. Views (views.py)

```python
# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Simple view
def index(request):
    return HttpResponse("Hello, World!")


# Template view
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


# Detail view
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
```

### 5. URLs (urls.py)

```python
# blog/urls.py (create this file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post//', views.post_detail, name='post_detail'),
]
```

```python
# mysite/urls.py (main project urls)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

### 6. Templates

```html
<!-- blog/templates/blog/home.html -->

My Blog

Blog Posts

{% for post in posts %}

{{ post.title }}
{{ post.content }}
{{ post.created_at }}

{% endfor %}


```

### 7. Admin Interface

```python
# blog/admin.py
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'content']
```

```bash
# Create superuser
uv run python manage.py createsuperuser

# Start server
uv run python manage.py runserver

# Access admin at: http://127.0.0.1:8000/admin/
```

## Additional Resources

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django REST Framework](https://www.django-rest-framework.org/)

### Learning Resources
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Real Python Django](https://realpython.com/tutorials/django/)

### Popular Django Packages
- `django-crispy-forms` - Better form rendering
- `django-allauth` - Authentication
- `django-rest-framework` - REST APIs
- `celery` - Background tasks
- `django-debug-toolbar` - Development debugging

[<< Day 14](../day_14/day_14.md) | [Home >>](../README.md)