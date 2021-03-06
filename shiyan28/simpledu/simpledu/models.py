from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for

# 注意这里不再传入 app 了
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True,
                         index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    job = db.Column(db.String(64))
    publish_courses = db.relationship('Course')

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_staff(self):
        return self.role == self.ROLE_STAFF


class Course(Base):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    # Course description
    description = db.Column(db.String(256))
    # Course ico url
    image_url = db.Column(db.String(256))
    # Course author
    author_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='SET NULL'))
    author = db.relationship('User', uselist=False)
    # Chapter
    chapters = db.relationship('Chapter')

    @property
    def url(self):
        return url_for('course.detail', course_id=self.id)

    def __repr__(self):
        return '<Course:{}>'.format(self.name)


class Chapter(Base):
    __tablename__ = 'chapter'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(256))
    # course video url
    video_url = db.Column(db.String(256))
    # video duration, format: '30:15', '1:15:20'
    video_duration = db.Column(db.String(24))
    # link to course, and delete chapters while course deleted
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.id', ondelete='CASCADE'))
    course = db.relationship('Course', uselist=False)

    def __repr__(self):
        return '<Chapter:{}>'.format(self.name)


class Env(Base):
    __tablename__ = 'env'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    # Enverment description
    description = db.Column(db.String(256))
    # module databases
    mdbs = db.relationship('Mdb')

    def __repr__(self):
        return '<Env:{}>'.format(self.name)


class Mdb(Base):
    __tablename__ = 'mdb'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(256))
    # module database link url
    mdb_url = db.Column(db.String(256))
    # link to enverment, and delete mdb while enverment deleted
    env_id = db.Column(db.Integer, db.ForeignKey('env.id', ondelete='CASCADE'))
    env = db.relationship('Env', uselist=False)

    def __repr__(self):
        return '<Mdb:{}>'.format(self.name)

# using flask-migrate upgrade database
# ```
# export FLASK_APP=manage.py
# flask db migrate -m 'extend course table and add chapter table'
# flask db upgrade
# ```
