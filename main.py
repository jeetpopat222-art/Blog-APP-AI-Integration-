
from flask import Flask, render_template, request, url_for, redirect,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@127.0.0.1:5432/project01" # put in gitignore
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "jeet_todo_app_2024_xkq9" # put in gitignore

db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(nullable=False)


class Todo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    desc: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", backref="todos")

def safty_check():
    if not session.get("user_id"):
        return redirect  (url_for("home"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        hash_pass = generate_password_hash(password)
        db.session.add(User(email=email, password=hash_pass))
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            session["user_id"] = user.id
            session["email"] = email
            todos = Todo.query.filter_by(user_id=user.id).all()  # ✅ fetch todos
            return render_template("todo.html",todos=todos,email=email)
        else:
            return render_template("invalid.html")
        
    return render_template("login.html")


@app.route("/create_todo", methods=["POST","GET"])
def create_todo():
    check = safty_check()
    if check: return check
    user_id = session.get("user_id")
    title = request.form.get("title")
    desc = request.form.get("desc")

    db.session.add (Todo(title=title, desc=desc, user_id=user_id))
    db.session.commit()

    todos = Todo.query.filter_by(user_id=user_id).all()
    return render_template("todo.html", todos=todos)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    check = safty_check()
    if check: return check
    
    user_id = session.get("user_id")
    email = session.get("email")
    
    delete_todo = Todo.query.filter_by(id=id, user_id=user_id).first()
    
    if not delete_todo:
        return "Unauthorized or Todo not found", 403
    
    db.session.delete(delete_todo)
    db.session.commit()

    todos = Todo.query.filter_by(user_id=user_id).all()
    return render_template("todo.html", todos=todos, email=email)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False) # Use True during test


