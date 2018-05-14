from flask import Blueprint, render_template
from simpledu.models import Course, User

course = Blueprint('course', __name__, url_prefix='/courses')

@course.route('/')
def course_index():
	courses = Course.query.all()
	users = User.query.all() 
	return render_template('courses.html', courses=courses, users=users)