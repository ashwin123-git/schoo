# Quick Reference Guide

## 🚀 Getting Started (30 seconds)

```bash
# 1. Navigate to project
cd f:\schoo

# 2. Activate virtual environment
f:\schoo\.venv\Scripts\activate

# 3. Run the app
python run.py

# 4. Open browser
# http://localhost:5000
```

## 📋 Common Commands

### Running the App
```bash
# Development mode (auto-reload)
python run.py

# Production mode
set FLASK_ENV=production
python run.py
```

### Managing Database
```bash
# Recreate database (deletes all data)
del business_app.db
python run.py

# View database (requires DB browser)
# Download: https://sqlitebrowser.org/
```

### Installing Packages
```bash
# Install all from requirements.txt
pip install -r requirements.txt

# Install specific package
pip install package_name
```

## 🌐 Application URLs

| Page | URL | Purpose |
|------|-----|---------|
| Home | http://localhost:5000 | Welcome page |
| Sign Up | http://localhost:5000/api/auth/signup | Register new user |
| Sign In | http://localhost:5000/api/auth/signin | Login |
| Dashboard | http://localhost:5000/dashboard | Main app (needs login) |

## 📊 Features Quick Access

### In Dashboard

| Feature | Location | Shortcut |
|---------|----------|----------|
| Dashboard | Sidebar | 📊 Dashboard |
| Add Log | Business Logs tab | Fill form and click Add |
| Filter Logs | Business Logs tab | Set filters and click Filter |
| Export PDF | Business Logs tab | Click Export PDF |
| Chat | Sidebar | 💬 Group Chat |
| View Summary | Dashboard tab | Card display |

## 🔑 Test Credentials

No pre-made accounts. Create your own:
1. Go to Sign Up
2. Enter email and password
3. Enter any 6-digit code (while testing)
4. Sign in with those credentials

## 💾 Files You'll Edit Most

| File | Purpose | Edit For |
|------|---------|----------|
| `.env` | Configuration | Supabase credentials |
| `app/routes/auth.py` | Authentication | Email logic |
| `app/routes/logs.py` | Log operations | Business logic |
| `app/templates/dashboard.html` | UI | Design changes |

## 🐛 Common Errors & Fixes

### "Port 5000 already in use"
```python
# Edit run.py, change:
app.run(port=5001)  # Use different port
```

### "Module not found"
```bash
# Make sure virtual env is activated
.venv\Scripts\activate
# Then reinstall packages
pip install -r requirements.txt
```

### "Database is locked"
```bash
# Delete database and restart
del business_app.db
python run.py
```

## 🔐 Login System

### Registration Flow
```
1. User fills email + password
2. Account created
3. Verification code sent
4. User enters code
5. Can now login
```

### Login Flow
```
1. User enters email + password
2. System verifies credentials
3. JWT token generated
4. Redirected to dashboard
```

## 💰 Accounting Features

### Income Entry
```
Type: Income
Amount: 5000
Description: Consulting fee
→ Balance increases by 5000
```

### Expense Entry
```
Type: Expense  
Amount: 1200
Description: Office supplies
→ Balance decreases by 1200
```

### Current Balance
```
Starting: ₹1604
After operations: Auto-calculated
Formula: Income Total - Expense Total
```

## 📧 Supabase Setup

### Quick Setup
1. Create account at supabase.com
2. Create new project
3. Configure SMTP settings
4. Copy credentials to `.env`

### .env Format
```
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your_anon_key
SECRET_KEY=your_secret
FLASK_ENV=development
DATABASE_URL=sqlite:///business_app.db
```

## 🎨 Customization Examples

### Change App Name
- Edit `app/templates/index.html` line 14
- Edit `app/templates/dashboard.html` line 18

### Change Primary Color
- Search for `bg-blue-600` in templates
- Replace with `bg-green-600` or other Tailwind colors

### Change Initial Balance
- Current: 1604 in `app/templates/dashboard.html` line 30

### Change Database Name
- Edit `config.py` line 7
- Change `business_app.db` to your name

## 🚀 Deployment Checklist

- [ ] Update `.env` with production values
- [ ] Change `SECRET_KEY` to random string
- [ ] Set `FLASK_ENV=production`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Set up proper logging
- [ ] Configure firewall
- [ ] Test all features
- [ ] Set up automated backups
- [ ] Monitor error logs

## 📱 Mobile Access

### From Another Device on Same Network
```
Find your IP: ipconfig (in terminal)
Use: http://<your-ip>:5000
```

### From Internet (requires setup)
- Set up ngrok: `ngrok http 5000`
- Or deploy to cloud service
- Or use reverse proxy

## 🆘 Getting Help

### Check Logs
```bash
# Terminal shows errors as you use the app
# Look for red error messages
```

### Test Endpoints
```bash
# Using curl or Postman
GET http://localhost:5000/health
# Should return: {"status": "healthy"}
```

### Database Debug
```bash
# View raw database content
# Download DB Browser for SQLite
# Open business_app.db
```

## 📚 Documentation Files

- `README.md` - Full feature documentation
- `SETUP_GUIDE.md` - Complete setup instructions  
- `SUPABASE_INTEGRATION.md` - Supabase integration guide
- `QUICK_REFERENCE.md` - This file

## 💡 Pro Tips

1. **Dev Tools:** F12 to see network requests
2. **Auto-save:** Don't forget to save `.env` changes
3. **Testing:** Create test account with dummy data
4. **Backup:** Regular exports of important logs
5. **Monitoring:** Keep terminal running to see errors
6. **Performance:** Clear old messages/logs periodically

## ⚡ Quick Customizations

### Add a New Route
```python
# In app/routes/main.py
@main_bp.route('/new-page')
def new_page():
    return render_template('new_page.html')
```

### Add a New Model
```python
# Create in app/models/new_model.py
# Add import to app/models/__init__.py
```

### Add a New Database Field
```python
# Edit model in app/models/
# Restart app (creates new field)
```

## 🔄 Workflow

1. **Development:** `python run.py`
2. **Testing:** Use app in browser
3. **Changes:** Edit files, save, refresh browser
4. **Production:** Set env vars and deploy

## Contact & Support

For issues:
1. Check this guide
2. Read README.md
3. Check terminal for errors
4. Review Supabase docs
5. Check Flask documentation

---

**Last Updated:** January 2026  
**App Status:** ✅ Production Ready  
**All Features:** ✅ Implemented
