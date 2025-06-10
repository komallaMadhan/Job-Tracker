from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    date_applied = db.Column(db.String(20))
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"Job(company='{self.company}', position='{self.position}', status='{self.status}')"
