# Students/Student.py -- Contains the routes and CRUD operations

from flask import render_template, request, redirect, url_for, current_app, flash
# from flask_wtf import csrf
from ChlauApp import db # Import the db instance
# from .. import db
# from ChlauApp.models import Student  # Import the Student model
from . import students_bp  # student blueprint
from .Students_forms import StudentForm  # Import the StudentForm
from sqlalchemy import inspect

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    course = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(10), nullable=False)

    def __repr__(self):
         return f"<Student(name='{self.name}', course='{self.course}', grade='{self.grade}')>"

# from flask_sqlalchemy import SQLAlchemy
def table_exists(table_name):
    inspector = inspect(db.engine)
    return inspector.has_table(table_name)

# @students_bp.before_app_first_request
##  error: before_app_first_request method not found.  
# def startup_check():
#     import os
#     if not table_exists('student'):
#         current_app.logger.error("Table 'student' does not exist. Creating table.")
#         db.create_all()  # This will create all tables defined by the models
#     else:
#         current_app.logger.debug("Table 'student' exists.")

@students_bp.route('/')     # D = Display
def show_students():
    students = Student.query.all()
    return render_template('students/Students.html', students=students)

@students_bp.route('/add', methods=['GET', 'POST'])
def add_student():           # C = Create
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Student(name=form.name.data, course=form.course.data, grade=form.grade.data)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('students_bp.show_students'))
    return render_template('students/Students_add.html', form=form)

@students_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):       # U = Update
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        student.course = form.course.data
        student.grade = form.grade.data
        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('students_bp.show_students'))
    return render_template('students/Students_update.html', form=form, student=student)

@students_bp.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):      # R = Remove
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('students_bp.show_students'))

# def send_email(student):
#     msg = Message('New Student Added',
#                   sender='your_email@gmail.com',
#                   recipients=['recipient@example.com'])
#     msg.body = f'Name: {student.name}\nCourse: {student.course}\nGrade: {student.grade}'
#     mail.send(msg)
