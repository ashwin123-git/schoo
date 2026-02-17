# Email Setup Guide

## ✅ Verification Code Now Sends via Email!

Your Flask app now sends verification codes via SMTP when users sign up.

## 🔧 Configuration

### Option 1: Gmail (Easiest & Free)

1. **Enable 2-Factor Authentication:**
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password:**
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Google will generate a 16-character password

3. **Update `.env` file:**
   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your_email@gmail.com
   SMTP_PASSWORD=xxxx xxxx xxxx xxxx
   ```
   (Use the 16-character password without spaces)

### Option 2: Supabase Email Service

1. **Set up in Supabase Dashboard:**
   - Go to Authentication > Email Templates
   - Click "Custom SMTP"
   - Enter your SMTP details

2. **Update `.env` file:**
   ```
   SMTP_HOST=your_supabase_smtp_host
   SMTP_PORT=465
   SMTP_USER=your_supabase_smtp_user
   SMTP_PASSWORD=your_supabase_smtp_password
   ```

### Option 3: SendGrid (Recommended for Production)

1. **Create SendGrid Account:**
   - Go to https://sendgrid.com
   - Sign up (free tier available)
   - Create an API key

2. **Update `.env` file:**
   ```
   SMTP_HOST=smtp.sendgrid.net
   SMTP_PORT=587
   SMTP_USER=apikey
   SMTP_PASSWORD=SG.your_api_key_here
   ```

### Option 4: Other SMTP Services

Use your provider's SMTP settings:
```
SMTP_HOST=your.smtp.server
SMTP_PORT=587 or 465
SMTP_USER=your_username
SMTP_PASSWORD=your_password
```

## 📧 How It Works Now

### Sign Up Process:
1. User fills email and password
2. Account created
3. **Verification code sent to email** ← NEW!
4. User checks email inbox
5. Enters code in app
6. Can now login

### Email Format:
The verification email is beautifully formatted with:
- Business App branding
- Large, easy-to-read code
- 15-minute expiration notice
- Professional HTML template

## 🧪 Testing

### Without SMTP Setup (Will Show in Console):
```
⚠️  SMTP credentials not configured. Verification code for user@email.com: 123456
```
The code appears in your terminal for testing.

### With SMTP Setup (Will Send Email):
```
✅ Verification email sent to user@email.com
```
Check the user's email inbox for the verification code.

## 🐛 Troubleshooting

### Email Not Sending?

**Check 1: SMTP Credentials**
- Make sure `.env` file has correct SMTP settings
- Verify SMTP_USER and SMTP_PASSWORD are exact
- No extra spaces around values

**Check 2: App Password (Gmail)**
- Use 16-character app password, not your regular Gmail password
- Remove any spaces: `xxxx xxxx xxxx xxxx` → `xxxxxxxxxxxxxxxx`

**Check 3: Terminal Output**
When you sign up, look for messages:
- `✅ Verification email sent` = Working!
- `❌ Error sending email` = Configuration issue
- Shows verification code = Fallback mode (SMTP not set)

**Check 4: Firewall/Network**
- Some networks block SMTP on port 587
- Try port 465 instead (more secure)
- Contact your network admin if blocked

**Check 5: Email Security**
- Check spam/junk folder
- Add sending email to contacts
- Whitelist the domain

### Code Not Working?

- Make sure you're using the exact code sent
- Code expires after 15 minutes
- Check the code format (should be 6 digits)

## 📝 Verify It's Working

1. **Restart the Flask app:**
   ```bash
   # Stop current app (Ctrl+C)
   # Start again
   python run.py
   ```

2. **Go to Sign Up:**
   - http://localhost:5000/api/auth/signup

3. **Fill form:**
   - Email: test@example.com
   - Password: test123456

4. **Check result:**
   - ✅ If SMTP works: Email received
   - ⚠️ If not configured: Check terminal for code

5. **Verify email:**
   - Enter the code from email (or terminal)
   - Should see success message

## 🔐 Security Notes

- ✅ Verification codes are 6 digits (1 million combinations)
- ✅ Codes expire after 15 minutes
- ✅ Only stored in memory (not in database)
- ✅ Passwords are hashed, never stored plain
- ✅ SMTP credentials should be in `.env` (not in code)

## 🚀 Production Deployment

For production:

1. **Use Environment Variables:**
   - Don't put `.env` in git
   - Set variables on hosting platform
   - Use strong, unique passwords

2. **Use Production SMTP:**
   - SendGrid (recommended)
   - Supabase email service
   - AWS SES
   - Your company's email server

3. **Monitor Email Delivery:**
   - Check bounce rates
   - Monitor delivery logs
   - Set up email validation

4. **Update Email Template:**
   - Customize branding
   - Add company logo
   - Include company contact info

## 📚 Next Steps

1. Set up SMTP credentials
2. Update `.env` file
3. Restart Flask app
4. Test sign-up process
5. Verify email received
6. Go to Supabase and set up actual email templates there (optional)

## ❓ Questions?

- **Gmail not working?** Check app password setup
- **Code never arrives?** Check spam folder and SMTP settings
- **Need different SMTP?** Update SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD in `.env`

---

**Status:** ✅ Email verification ready to use!
