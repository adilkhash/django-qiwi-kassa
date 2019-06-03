# Django Qiwi Kassa

## Description
Django app to work with Qiwi Kassa


## Install
```
pip install django-qiwi-kassa
```

Add `qiwi_kassa` to INSTALLED_APPS

### Step 1.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qiwi_kassa',
]
```

### Step 2.
Add to `settings.py` QIWI_KASSA_SECRET_KEY constant:

```python
QIWI_KASSA_SECRET_KEY = 'QIWI_KASSA_SECRET_KEY'
```
