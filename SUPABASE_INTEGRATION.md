# Supabase Integration Guide

## Overview

This Flask app is designed to work seamlessly with Supabase for:
- Email verification via SMTP
- User authentication
- Secure API access

## Current Implementation Status

### ✅ What's Ready
- User registration with email and password
- Email verification code flow (UI ready)
- JWT token-based authentication
- Database structure compatible with Supabase
- All routes structured for Supabase integration

### 🔧 What Needs Supabase Configuration

1. **Email Verification (SMTP)**
   - Currently: Accepts any verification code
   - Needs: Integration with your Supabase SMTP settings
   - Location: `app/routes/auth.py` lines 55-65

2. **Email Sending**
   - Currently: Not implemented
   - Needs: Supabase Auth email templates configured

## Step-by-Step Supabase Setup

### 1. Create Supabase Project
```
1. Go to https://supabase.com
2. Sign in or create an account
3. Click "New Project"
4. Fill in project details:
   - Name: Your project name
   - Database Password: Strong password
   - Region: Closest to your users
5. Wait for setup (2-3 minutes)
```

### 2. Get Your Credentials
```
1. Go to Project Settings > API
2. Copy:
   - Project URL → SUPABASE_URL in .env
   - anon key → SUPABASE_KEY in .env
3. Keep these secure!
```

### 3. Configure Email (SMTP)
```
1. Go to Authentication > Email Templates
2. Click "Custom SMTP"
3. Fill in your SMTP details:
   - Host: your SMTP host (e.g., smtp.gmail.com)
   - Port: 587 or 465
   - Username: your email
   - Password: your app password (not regular password)
4. Save configuration
5. Test by sending a verification email
```

### 4. Update Environment File
Create `.env` file:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_key_here
SECRET_KEY=your_flask_secret_key
FLASK_ENV=development
DATABASE_URL=sqlite:///business_app.db
```

## Email Verification Implementation

### Current Code (Testing)
```python
# In app/routes/auth.py - verify_email function
# Currently just marks user as verified
```

### To Integrate with Supabase SMTP:

Option 1: Use Supabase Python Client
```python
from supabase import create_client, Client

supabase: Client = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

# Send verification email via Supabase
```

Option 2: Use Supabase Auth Endpoints
```python
# The verification code should be sent via Supabase Auth
# Update the register route to use Supabase
```

## Database Structure

The app uses SQLite, but Supabase can host PostgreSQL. 

### To Switch to Supabase PostgreSQL:

1. Create tables in Supabase:
```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(120) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(120),
  is_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Logs table
CREATE TABLE logs (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  log_type VARCHAR(20) NOT NULL,
  amount FLOAT NOT NULL,
  description VARCHAR(500),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Messages table
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

2. Update DATABASE_URL in .env:
```
DATABASE_URL=postgresql://user:password@db.supabase.co:5432/postgres
```

3. Update config.py to use PostgreSQL driver:
```bash
pip install psycopg2-binary
```

## Authentication Flow with Supabase

### Current Flow (Local)
```
User → Register → Check Email → Verify Code → Login → JWT Token
```

### Recommended Supabase Flow
```
User → Register → Supabase Auth Email → Verify Code → Login → JWT Token
```

## Testing Email Sending

### With Gmail (Free Option)
1. Enable 2-Factor Authentication on your Gmail
2. Create an "App Password" for less secure apps
3. Use app password in SMTP configuration

### With SendGrid (Recommended)
1. Create SendGrid account (free tier available)
2. Create API key
3. Use SendGrid SMTP credentials

### With Mailgun
1. Create Mailgun account
2. Get SMTP credentials
3. Configure in Supabase

## Important Notes

⚠️ **Security:**
- Never commit `.env` file to Git
- Keep SUPABASE_KEY secure (it's your API key)
- Use environment variables for sensitive data
- In production, use separate keys for different environments

📝 **Email Templates:**
- Supabase allows custom email templates
- Design verification email in Supabase Dashboard
- Test sending before going live

🔄 **User Sessions:**
- Current app uses JWT tokens (valid for 30 days)
- Can integrate Supabase sessions for better UX
- User stays logged in across sessions

## Troubleshooting

### Email Not Sending
- Check SMTP credentials are correct
- Verify "Allow less secure apps" if using Gmail
- Check spam/junk folder
- Look at Supabase logs

### Verification Code Not Working
- Make sure code matches Supabase format
- Check if code expired (usually 15 minutes)
- Verify database is connected

### Database Connection Issues
- Test connection string with: psql postgresql://...
- Check if PostgreSQL is running
- Verify firewall allows connections

## Advanced: Custom Email Templates

In Supabase Dashboard:
```
1. Authentication > Email Templates
2. Click "Edit" on verification email
3. Customize template with your branding
4. Use {{.ConfirmationURL}} for verification link
5. Save changes
```

## Example Verification Email Template

```html
<h1>Verify Your Email</h1>
<p>Click the link below to verify your email address:</p>
<a href="{{.ConfirmationURL}}">Verify Email</a>
<p>Or enter this code: {{.Token}}</p>
<p>This link expires in 24 hours.</p>
```

## Next Steps

1. ✅ Create Supabase project
2. ✅ Configure SMTP settings
3. ✅ Update `.env` file
4. ✅ Test email sending
5. ✅ Update `app/routes/auth.py` to use actual Supabase email
6. ✅ Deploy to production

## Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase Auth Guide](https://supabase.com/docs/guides/auth)
- [Flask & Supabase Integration](https://github.com/supabase-community/supabase-py)
- [Email Template Best Practices](https://supabase.com/docs/guides/auth/auth-email-templates)

## Support

If you encounter issues:
1. Check Supabase status page
2. Review app logs
3. Check email delivery logs in Supabase
4. Verify `.env` configuration
5. Test API endpoints with curl or Postman

Good luck! 🚀
