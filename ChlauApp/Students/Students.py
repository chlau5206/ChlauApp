# Students/Student.py -- Contains the routes and CRUD operations

from flask import render_template, request, redirect, url_for
from ChlauApp import db  # Import the db instance
from ChlauApp.models import Student  # Import the Student model
from . import students_bp  # student blueprint


@students_bp.route('/')
def show_students():
    students = Student.query.all()
    return render_template('students/students.html', students=students)

@students_bp.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    course = request.form.get('course')
    grade = request.form.get('grade')
    new_student = Student(name=name, course=course, grade=grade)
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('students_bp.show_students'))

@students_bp.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('students_bp.show_students'))

@students_bp.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    student = Student.query.get(id)
    if student:
        student.name = request.form.get('name')
        student.course = request.form.get('course')
        student.grade = request.form.get('grade')
        db.session.commit()
    return redirect(url_for('students_bp.show_students'))
