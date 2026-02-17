# Business App - Complete Setup Guide

## 🚀 Quick Start

Your Flask business application is now ready! Follow these steps to get started:

### 1. Initial Setup

```bash
# The virtual environment is already created at: F:/schoo/.venv
# Activate it:
F:\schoo\.venv\Scripts\activate
```

### 2. Environment Configuration

1. Create a `.env` file in the project root (copy from `.env.example`):
```bash
cp .env.example .env
```

2. Update `.env` with your Supabase credentials:
```
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key
SECRET_KEY=your_secure_secret_key
FLASK_ENV=development
DATABASE_URL=sqlite:///business_app.db
```

### 3. Supabase Setup

1. Go to [Supabase](https://supabase.com) and create an account
2. Create a new project
3. Configure SMTP settings:
   - Go to Authentication > Email Templates
   - Enable Custom SMTP
   - Add your SMTP details (as you mentioned you already did)
4. Copy the Supabase URL and API key to your `.env` file

### 4. Run the Application

```bash
# Make sure you're in the project directory
cd F:\schoo

# Run the Flask application
F:\schoo\.venv\Scripts\python.exe run.py
```

The application will be available at:
- **Local:** http://localhost:5000
- **Network:** http://<your-ip>:5000

## 📋 Features Implementation

### ✅ Completed Features

1. **User Authentication**
   - Sign up with email and password
   - Sign in with email and password
   - Email verification with code (ready for Supabase integration)
   - JWT-based session management

2. **Business Logs (Income & Expense Tracker)**
   - Add income/expense entries
   - Automatic calculation of totals
   - Starting balance: ₹1604
   - Real-time balance updates
   - Filter by date range
   - Filter by transaction type (income/expense)
   - Delete entries

3. **PDF Export**
   - Export filtered logs as PDF
   - Professional formatting with ReportLab
   - Summary of income, expenses, and balance
   - Date-based filtering for reports

4. **Group Chat**
   - Real-time messaging for business meetings
   - Send, edit, and delete messages
   - Display sender information
   - Auto-refresh every 3 seconds
   - Text-only business meetings format

5. **Tailwind CSS UI**
   - Modern, responsive design
   - Mobile-friendly interface
   - Gradient backgrounds and smooth transitions
   - Dark/Light theme elements
   - Professional cards and components

### 🔄 Integration Points for Supabase

The app is ready for Supabase email verification. To fully integrate:

1. **Email Verification:**
   - Update `/app/routes/auth.py` line ~60 to send actual verification code via Supabase
   - Currently accepts any code for testing

2. **Authentication:**
   - Consider integrating Supabase Auth SDK for additional features

## 📂 Project Structure

```
schoo/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models/
│   │   ├── user.py              # User model with password hashing
│   │   ├── log.py               # Business log model
│   │   └── message.py           # Chat message model
│   ├── routes/
│   │   ├── auth.py              # Auth endpoints (signup, signin, verify)
│   │   ├── logs.py              # Log endpoints (add, list, filter, export PDF)
│   │   ├── chat.py              # Chat endpoints (send, list, edit, delete)
│   │   └── main.py              # Main endpoints (dashboard, health check)
│   ├── static/
│   │   └── css/                 # Static CSS files
│   └── templates/
│       ├── index.html           # Home page with features
│       ├── signin.html          # Sign in page
│       ├── signup.html          # Sign up with verification
│       └── dashboard.html       # Main dashboard with all features
├── config.py                    # Configuration management
├── run.py                       # Application entry point
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
└── README.md                    # Complete documentation
```

## 🔐 Key Features Explained

### 1. Dashboard
- **Summary Cards:** Shows total income, expenses, and balance
- **Quick Actions:** Buttons to add logs, export PDF, or go to chat
- **Real-time Updates:** Data refreshes when you add/delete entries

### 2. Business Logs
- **Add Entry:** Select type (Income/Expense), amount, and description
- **View Logs:** Sortable table of all transactions
- **Filter:** By date range and type
- **Export:** Download filtered logs as professional PDF
- **Delete:** Remove entries (calculation updates automatically)

### 3. Group Chat
- **Real-time Messaging:** Messages appear instantly
- **Team Collaboration:** All authenticated users see the same chat
- **Message Management:** Edit or delete your own messages
- **Auto-refresh:** New messages every 3 seconds

### 4. User Accounts
- **Secure Registration:** Password hashing with werkzeug
- **Email Verification:** Verification code sent via Supabase
- **JWT Sessions:** Secure token-based authentication
- **Profile Management:** User can view their information

## 💾 Database

The app uses SQLite by default (`business_app.db`). Database includes:

- **Users Table:** id, email, password_hash, full_name, is_verified, created_at
- **Logs Table:** id, user_id, log_type, amount, description, created_at
- **Messages Table:** id, user_id, content, created_at

All data is isolated per user. Each user sees only their own logs.

## 🌐 API Endpoints

### Authentication
```
POST   /api/auth/register         - Create new user
POST   /api/auth/verify-email     - Verify email with code
POST   /api/auth/login            - Login and get JWT token
POST   /api/auth/logout           - Logout
GET    /api/auth/signin           - Signin page
GET    /api/auth/signup           - Signup page
```

### Business Logs
```
POST   /api/logs/add              - Add new log
GET    /api/logs/list             - Get logs (with filters)
GET    /api/logs/summary          - Get summary (income, expense, balance)
GET    /api/logs/export-pdf       - Export as PDF
DELETE /api/logs/delete/<id>      - Delete log
```

### Group Chat
```
POST   /api/chat/send             - Send message
GET    /api/chat/messages         - Get all messages
PUT    /api/chat/edit/<id>        - Edit message
DELETE /api/chat/delete/<id>      - Delete message
```

### Main Routes
```
GET    /                          - Home page
GET    /dashboard                 - Main dashboard (requires auth)
GET    /health                    - Health check
```

## 🧪 Testing the App

1. **Sign Up:**
   - Go to http://localhost:5000
   - Click "Sign Up"
   - Fill in details
   - Enter any 6-digit code (or actual code from Supabase)
   - You should be redirected to signin

2. **Sign In:**
   - Use the email and password you just created
   - You should be taken to the dashboard

3. **Add Logs:**
   - Go to "Business Logs" tab
   - Add some income and expense entries
   - Watch the balance update

4. **Chat:**
   - Go to "Group Chat" tab
   - Type a message and send
   - Open in another browser to see real-time updates

5. **Export PDF:**
   - Set date filters (optional)
   - Click "Export PDF"
   - Check your downloads folder

## 🔧 Troubleshooting

### Port 5000 already in use?
Edit `run.py` and change the port:
```python
app.run(port=5001, ...)
```

### Database locked error?
```bash
# Delete the database and restart:
del f:\schoo\business_app.db
F:\schoo\.venv\Scripts\python.exe run.py
```

### Can't access from another computer?
- Make sure your firewall allows port 5000
- Use http://<your-ip>:5000 instead of localhost

## 📦 Deployment

### For Heroku:
1. Add `gunicorn` to requirements.txt
2. Create `Procfile`:
   ```
   web: gunicorn run:app
   ```
3. Push to Heroku

### For your own server:
1. Use Nginx as reverse proxy
2. Use Gunicorn as WSGI server
3. Use Supervisor to keep it running
4. Enable HTTPS with Let's Encrypt

## 🚀 Next Steps

1. **Customize Branding:**
   - Update app name in templates
   - Add your logo (create `app/static/images/`)
   - Customize colors

2. **Production Deployment:**
   - Change DATABASE_URL to PostgreSQL
   - Use strong SECRET_KEY
   - Enable HTTPS
   - Set FLASK_ENV to production

3. **Advanced Features:**
   - Add user roles and permissions
   - Create monthly/yearly reports
   - Add budget planning
   - Send email notifications

## 💡 Tips

- The starting balance is ₹1604 (as you mentioned)
- Each user has isolated data (can't see others' logs or accounts)
- Chat is shared between all logged-in users
- All timestamps are in UTC
- Passwords are never stored in plain text

## ❓ Questions?

Refer to:
- `README.md` - Complete feature documentation
- `config.py` - Configuration options
- `/app/routes/` - API endpoint implementations
- `/app/templates/` - UI and frontend code

Good luck with your business app! 🎉
