# ✅ Todo App — Flask + PostgreSQL

A full-stack **Todo application** with user authentication, built with Python (Flask) and PostgreSQL. Each user can sign up, log in, and manage their own personal todo list securely.

---

> [!NOTE]
> 🤖 **The frontend (HTML templates) was generated with the assistance of AI.**

---

## 🚀 Features

- 🔐 User registration & login with hashed passwords
- 🔒 Session-based authentication
- ➕ Create todos (title + description)
- 🗑️ Delete todos (user can only delete their own)
- 🚪 Logout support
- 💾 Persistent storage via PostgreSQL
- 🌐 Server-side rendering with Jinja2 templates

---

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3, Flask                   |
| Database   | PostgreSQL                        |
| ORM        | SQLAlchemy (Mapped / mapped_column)|
| Auth       | Werkzeug password hashing, Flask session |
| Frontend   | HTML, CSS — AI-generated          |
| Templating | Jinja2                            |

---

## 📁 Project Structure

```
project_01/
│
├── main.py                  # Flask app, models, and all routes
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignores .env, secrets, venv
├── .env.example             # Example environment variable template
│
└── templates/
    ├── home.html            # Landing page
    ├── sign_up.html         # Registration form
    ├── login.html           # Login form
    ├── todo.html            # Todo dashboard (create & delete)
    └── invalid.html         # Invalid login page
```

---

## 🗃️ Database Schema

**Table: `user`**

| Column   | Type    | Constraints         |
|----------|---------|---------------------|
| id       | Integer | Primary key         |
| email    | String  | Unique, not null    |
| password | String  | Hashed, not null    |

**Table: `todo`**

| Column  | Type       | Constraints              |
|---------|------------|--------------------------|
| id      | Integer    | Primary key              |
| title   | String(30) | Not null                 |
| desc    | String     | Optional description     |
| user_id | Integer    | Foreign key → `user.id`  |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- pip

---

### 1. Clone the Repository

```bash
git clone https://github.com/jeetpopat222-art/Todo_app-using-flask-database-postgresql-.git
cd Todo_app-using-flask-database-postgresql-
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

Create a database in PostgreSQL:

```sql
CREATE DATABASE project01;
```

### 5. Configure the App

Open `main.py` and update the following lines with your credentials:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<user>:<password>@127.0.0.1:5432/project01"
app.secret_key = "your-secret-key"
```

> ⚠️ **Important:** Move these values to a `.env` file and load them with `python-dotenv` before pushing to a public repository. Both values are currently marked with `# put in gitignore` comments in the source.

### 6. Run the App

```bash
python main.py
```

The app will automatically create all database tables on first run via `db.create_all()`.

Open your browser at: **http://127.0.0.1:5000**

---

## 🔐 Security Notes

- Passwords are hashed using **Werkzeug's** `generate_password_hash` before being stored.
- Todos are **user-scoped** — users can only view and delete their own tasks.
- A `safety_check()` helper guards all authenticated routes against unauthorized access.
- **Do not commit** your database URI or secret key to version control — use `.env` or environment variables in production.

---

## 🌐 Routes Overview

| Method     | Route             | Description                        |
|------------|-------------------|------------------------------------|
| GET        | `/`               | Home / landing page                |
| GET, POST  | `/signup`         | User registration                  |
| GET, POST  | `/login`          | User login                         |
| POST       | `/create_todo`    | Create a new todo (auth required)  |
| POST       | `/delete/<id>`    | Delete a todo (auth required)      |
| GET        | `/logout`         | Clear session and log out          |

---

## 📦 Requirements

Key dependencies (see `requirements.txt` for full list):

```
Flask
Flask-SQLAlchemy
SQLAlchemy
psycopg2-binary
Werkzeug
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Jeet Popat**  
GitHub: [@jeetpopat222-art](https://github.com/jeetpopat222-art)