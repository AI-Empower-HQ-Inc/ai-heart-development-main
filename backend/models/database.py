try:
    from flask_sqlalchemy import SQLAlchemy
except ImportError:
    raise ImportError(
        "The 'flask_sqlalchemy' package is required. "
        "Install it with 'pip install flask_sqlalchemy'."
    )

from datetime import datetime
import uuid

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=True)
    name = db.Column(db.String(100), nullable=True)
    spiritual_level = db.Column(db.String(50), default='beginner')
    preferred_gurus = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    sessions = db.relationship('SpiritualSession', backref='user', lazy=True)
    user_sessions = db.relationship('UserSession', backref='user', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'spiritual_level': self.spiritual_level,
            'preferred_gurus': self.preferred_gurus,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class SpiritualSession(db.Model):
    __tablename__ = 'spiritual_sessions'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)
    guru_type = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    satisfaction_rating = db.Column(db.Integer)
    session_duration = db.Column(db.Integer)  # in seconds
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'guru_type': self.guru_type,
            'question': self.question,
            'response': self.response,
            'satisfaction_rating': self.satisfaction_rating,
            'created_at': self.created_at.isoformat()
        }

class DailyWisdom(db.Model):
    __tablename__ = 'daily_wisdom'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    date = db.Column(db.Date, unique=True, nullable=False)
    sloka_sanskrit = db.Column(db.Text)
    sloka_translation = db.Column(db.Text)
    wisdom_message = db.Column(db.Text)
    guru_type = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'sloka_sanskrit': self.sloka_sanskrit,
            'sloka_translation': self.sloka_translation,
            'wisdom_message': self.wisdom_message,
            'guru_type': self.guru_type
        }

class UserSession(db.Model):
    __tablename__ = 'user_sessions'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    session_type = db.Column(db.String(50), nullable=False, default='meditation')
    status = db.Column(db.String(20), nullable=False, default='active')  # active, completed, cancelled
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)  # in seconds
    notes = db.Column(db.Text)
    reflection = db.Column(db.Text)
    real_life_application = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'session_type': self.session_type,
            'status': self.status,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'duration': self.duration,
            'notes': self.notes,
            'reflection': self.reflection,
            'real_life_application': self.real_life_application
        }
