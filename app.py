import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from utils.resume_builder import create_resume
from utils.study_material import generate_notes
from utils.interview_questions import questions

app = Flask(__name__)

app.config['SECRET_KEY'] = 'careerprep-premium-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///career_copilot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create DB
with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        
        flash('Invalid email or password.', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


# Resume Builder
@app.route('/resume', methods=['GET', 'POST'])
@login_required
def resume():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        education = request.form['education']
        skills = request.form['skills']
        projects = request.form['projects']

        create_resume(name, email, phone, education, skills, projects)
        flash("Resume Generated Successfully!", 'success')
        return redirect(url_for('view_resumes'))

    return render_template('resume.html')

@app.route('/view_resumes')
@login_required
def view_resumes():
    resume_dir = os.path.join(app.root_path, 'resumes')
    if not os.path.exists(resume_dir):
        os.makedirs(resume_dir)
    files = os.listdir(resume_dir)
    return render_template('view_resumes.html', files=files)

@app.route('/download/<filename>')
@login_required
def download_resume(filename):
    resume_dir = os.path.join(app.root_path, 'resumes')
    return send_from_directory(resume_dir, filename)


# Study Material Generator
@app.route('/study', methods=['GET', 'POST'])
@login_required
def study():
    notes = ""
    if request.method == 'POST':
        text = request.form['text']
        notes = generate_notes(text)

    return render_template('study.html', notes=notes)


# Interview Preparation
@app.route('/interview')
@login_required
def interview():
    return render_template('interview.html', questions=questions)


# Career Roadmap
@app.route('/roadmap', methods=['GET', 'POST'])
@login_required
def roadmap():
    roadmap_data = None
    if request.method == 'POST':
        goal = request.form.get('goal')
        # Simple logic for roadmap for now
        roadmap_data = {
            "Software Developer": [
                "Learn Basics (HTML/CSS/JS)",
                "Pick a Backend (Python/Node)",
                "Database Fundamentals (SQL)",
                "Frameworks (Flask/Django)",
                "Build Projects & Portfolio",
                "Start Applying for Internships"
            ],
            "Data Scientist": [
                "Math & Statistics",
                "Advanced Python (Pandas/NumPy)",
                "Data Visualization (Matplotlib)",
                "Machine Learning Basics",
                "Deep Learning & AI",
                "Kaggle Competitions"
            ]
        }.get(goal, [
            "Learn core concepts of the field",
            "Get hands-on experience via projects",
            "Build a strong networking profile",
            "Prepare for interviews",
            "Apply for junior roles"
        ])

    return render_template('roadmap.html', roadmap_data=roadmap_data)


if __name__ == '__main__':
    app.run(debug=True)
