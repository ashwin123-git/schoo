<<<<<<< HEAD
<<<<<<< HEAD
# Business App

A comprehensive Flask-based business management application with authentication, expense tracking, and team communication features.

## Features

✨ **Key Features:**
- 🔐 Secure user authentication with email verification via Supabase Auth
- 💰 Income and expense tracker with automatic balance calculations
- 📊 Export business logs to PDF with filtering options
- 💬 Real-time group chat for business meetings
- 🎨 Modern, responsive UI built with Tailwind CSS
- 🔍 Advanced filtering by date and log type

## Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd schoo
```

2. **Create a virtual environment:**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Create a `.env` file:**
```bash
cp .env.example .env
```

6. **Update `.env` with your configuration:**
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
DATABASE_URL=sqlite:///business_app.db
```

## Configuration

### Supabase Setup

1. Create a Supabase account at [https://supabase.com](https://supabase.com)
2. Create a new project
3. Configure SMTP settings in Supabase Auth for email verification
4. Copy your Supabase URL and API key to `.env`

## Running the Application

1. **Start the Flask development server:**
```bash
python run.py
```

2. **Access the application:**
Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
schoo/
├── app/
│   ├── models/
│   │   ├── user.py          # User model
│   │   ├── log.py           # Business log model
│   │   └── message.py       # Chat message model
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   ├── logs.py          # Business log routes
│   │   ├── chat.py          # Chat routes
│   │   └── main.py          # Main routes
│   ├── templates/
│   │   ├── index.html       # Home page
│   │   ├── signin.html      # Sign in page
│   │   ├── signup.html      # Sign up page
│   │   └── dashboard.html   # Main dashboard
│   └── __init__.py          # Flask app factory
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── .env.example            # Environment variables template
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/verify-email` - Verify email with code
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user

### Business Logs
- `POST /api/logs/add` - Add new income/expense log
- `GET /api/logs/list` - Get all logs with optional filters
- `GET /api/logs/summary` - Get income, expense, and balance summary
- `GET /api/logs/export-pdf` - Export logs as PDF
- `DELETE /api/logs/delete/<id>` - Delete a log

### Chat
- `POST /api/chat/send` - Send a message
- `GET /api/chat/messages` - Get all messages
- `DELETE /api/chat/delete/<id>` - Delete a message
- `PUT /api/chat/edit/<id>` - Edit a message

## Usage Guide

### Creating an Account
1. Click "Sign Up" on the home page
2. Enter your email and password
3. Check your email for the verification code
4. Enter the verification code to complete registration

### Tracking Business Logs
1. Go to the "Business Logs" section
2. Enter transaction details (Income/Expense, Amount, Description)
3. Click "Add" to record the transaction
4. Use filters to search logs by date and type
5. Click "Export PDF" to download a report

### Group Chat
1. Navigate to the "Group Chat" section
2. Type your message and click "Send"
3. Messages are displayed in real-time for all team members

### Dashboard
The dashboard displays:
- Total Income (all-time)
- Total Expenses (all-time)
- Current Balance

Starting balance: ₹1604

## Technologies Used

- **Backend:** Flask, Flask-SQLAlchemy, Flask-JWT-Extended
- **Database:** SQLite (or PostgreSQL in production)
- **Authentication:** JWT, Supabase Auth
- **Frontend:** HTML5, Tailwind CSS, JavaScript
- **PDF Export:** ReportLab
- **Email:** Supabase SMTP

## Browser Support

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Development

### Running in Development Mode
```bash
export FLASK_ENV=development
python run.py
```

### Creating Database Migrations (if needed)
```bash
flask db init
flask db migrate
flask db upgrade
```

## Deployment

### Production Considerations

1. **Update SECRET_KEY:** Use a strong, random secret key
2. **Use PostgreSQL:** Switch from SQLite to PostgreSQL for production
3. **Enable HTTPS:** Use a reverse proxy like Nginx with SSL
4. **Environment Variables:** Set all sensitive data via environment variables
5. **Database Backups:** Implement regular backup procedures

### Deploying to Heroku

1. Create a `Procfile`:
```
web: gunicorn run:app
```

2. Add `gunicorn` to requirements.txt

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## Security Notes

- ✅ Passwords are hashed using werkzeug.security
- ✅ JWT tokens are used for session management
- ✅ CORS is enabled for cross-origin requests
- ✅ SQL injection protection via SQLAlchemy ORM
- ⚠️ Always use HTTPS in production
- ⚠️ Keep your SECRET_KEY secure

## Troubleshooting

### Port Already in Use
```bash
# Change the port in run.py or run with:
python run.py --port 5001
```

### Database Lock Issues
```bash
# Delete the database and restart:
rm business_app.db
python run.py
```

### Email Not Sending
- Verify Supabase SMTP settings
- Check that the email template is configured in Supabase
- Ensure the SMTP credentials are correct in `.env`

## Future Enhancements

- [ ] User roles and permissions (Admin, Manager, User)
- [ ] Monthly/Yearly financial reports
- [ ] Budget planning and forecasting
- [ ] Invoice generation
- [ ] File sharing in chat
- [ ] Email notifications
- [ ] Dark mode
- [ ] Mobile app

## License

This project is licensed under the MIT License.

## Support

For issues, questions, or suggestions, please create an issue in the repository.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Built with ❤️ for business success**
=======
# langchain
>>>>>>> d9196671744f94742b437a8369099a0157038560
=======
# langchain
>>>>>>> d9196671744f94742b437a8369099a0157038560
