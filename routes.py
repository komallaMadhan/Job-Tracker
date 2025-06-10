from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from models import Job, db

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    try:
        jobs = Job.query.all()
        return render_template('index.html', jobs=jobs)
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return render_template('index.html', jobs=[])

@routes.route('/add', methods=['POST'])
def add_job():
    try:
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']
        date_applied = request.form['date_applied']
        notes = request.form['notes']

        new_job = Job(company=company, position=position, status=status,
                      date_applied=date_applied, notes=notes)
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('routes.index'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('routes.index'))

@routes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_job(id):
    job = Job.query.get_or_404(id)
    if request.method == 'POST':
        try:
            job.company = request.form['company']
            job.position = request.form['position']
            job.status = request.form['status']
            job.date_applied = request.form['date_applied']
            job.notes = request.form['notes']
            db.session.commit()
            return redirect(url_for('routes.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('routes.edit_job', id=id))
    return render_template('edit.html', job=job)

@routes.route('/delete/<int:id>')
def delete_job(id):
    try:
        job = Job.query.get_or_404(id)
        db.session.delete(job)
        db.session.commit()
        return redirect(url_for('routes.index'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('routes.index'))
