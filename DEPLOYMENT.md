# TAU Django Application - Deployment Guide

## Quick Deploy to Railway (Recommended)

### Step 1: Prepare Your Repository
1. Make sure all your changes are committed to Git
2. Push to GitHub/GitLab

### Step 2: Deploy to Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up/Login with your GitHub account
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will automatically detect it's a Django app

### Step 3: Configure Environment Variables
Add these environment variables in Railway dashboard:

```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-app-name.railway.app
DJANGO_CSRF_TRUSTED_ORIGINS=https://your-app-name.railway.app
DEFAULT_FROM_EMAIL=testmailsitp@gmail.com
SITE_URL=https://your-app-name.railway.app
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### Step 4: Run Migrations
In Railway dashboard, go to your app and run:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```

## Alternative: Deploy to Render

### Step 1: Prepare for Render
1. Create a `render.yaml` file in your project root:

```yaml
services:
  - type: web
    name: tau-django-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn TAU.wsgi:application
    envVars:
      - key: DJANGO_SECRET_KEY
        generateValue: true
      - key: DJANGO_DEBUG
        value: False
      - key: DJANGO_ALLOWED_HOSTS
        value: your-app-name.onrender.com
```

### Step 2: Deploy to Render
1. Go to [Render.com](https://render.com)
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure environment variables as shown above

## Environment Variables Reference

### Required Variables:
- `DJANGO_SECRET_KEY`: Your Django secret key
- `DJANGO_DEBUG`: Set to False for production
- `DJANGO_ALLOWED_HOSTS`: Your domain(s)
- `DJANGO_CSRF_TRUSTED_ORIGINS`: Your HTTPS domain(s)

### Email Configuration:
- `DEFAULT_FROM_EMAIL`: Your sender email
- `SITE_URL`: Your production URL

### Security (Production):
- `SECURE_SSL_REDIRECT`: True
- `SESSION_COOKIE_SECURE`: True
- `CSRF_COOKIE_SECURE`: True

## Post-Deployment Checklist

1. ✅ Run migrations: `python manage.py migrate`
2. ✅ Collect static files: `python manage.py collectstatic --noinput`
3. ✅ Create superuser: `python manage.py createsuperuser`
4. ✅ Test email functionality
5. ✅ Test ticket creation and escalation
6. ✅ Test student account creation

## Troubleshooting

### Common Issues:
1. **Static files not loading**: Make sure `collectstatic` was run
2. **Database errors**: Run migrations
3. **Email not working**: Check Brevo API key and settings
4. **CSRF errors**: Verify `CSRF_TRUSTED_ORIGINS` includes your domain

### Logs:
Check your deployment platform's logs for any errors.

## Support
If you encounter issues, check the logs in your deployment platform's dashboard. 