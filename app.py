from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import hashlib
from datetime import datetime
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.secret_key = "12345678"

client = MongoClient('mongodb://localhost:27017/')
db = client['recruit']
user_collection = db['user']


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/')
def index():
    return redirect(url_for('user_login'))


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])
        user = user_collection.find_one(
            {"username": username, "password": password})
        return redirect(url_for('list_jobs')) if user else redirect(url_for('user_login'))

    return render_template('user/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_collection.find_one({"username": username}):
            return redirect(url_for('register'))

        user_collection.insert_one(
            {"username": username, "password": hash_password(password)})
        return redirect(url_for('user_login'))

    return render_template('user/register.html')


@app.route('/login_admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('list_jobs2')) if username == "admin" and password == "123456" else redirect(url_for('admin_login'))

    return render_template('admin/login2.html')


@app.route('/list', methods=['GET', 'POST'])
def list_jobs():
    department_filter = request.args.get('department')
    title_search = request.args.get('search')
    query = {}

    if department_filter:
        query['department'] = department_filter
    if title_search:
        query['title'] = {'$regex': title_search, '$options': 'i'}

    jobs = db['jobs'].find(query)
    departments = db['jobs'].distinct('department')

    return render_template('user/list.html', jobs=jobs, departments=departments)


@app.route('/list2', methods=['GET', 'POST'])
def list_jobs2():
    department_filter = request.args.get('department')
    title_search = request.args.get('search')
    query = {}

    if department_filter:
        query['department'] = department_filter
    if title_search:
        query['title'] = {'$regex': title_search, '$options': 'i'}

    jobs = db['jobs'].find(query)
    departments = db['jobs'].distinct('department')

    return render_template('admin/list2.html', jobs=jobs, departments=departments)


@app.route('/job/<job_id>', methods=['GET', 'POST'])
def job_detail(job_id):
    job = db['jobs'].find_one({"_id": ObjectId(job_id)})

    if request.method == 'POST':
        files = {k: request.files[k] for k in ['resume', 'cover_letter']}
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        os.makedirs(f"files/{timestamp}")
        paths = {k: f"files/{timestamp}/{v.filename}" for k, v in files.items()}
        for k, v in paths.items():
            files[k].save(v)

        application = {**{k: request.form[k] for k in [
            'first_name', 'last_name', 'email', 'linkedin_profile',
            'authorized_to_work', 'require_visa_sponsorship',
            'current_residence', 'city_state'
        ]}, **paths, 'job_id': job_id, 'state': 0}

        db['applications'].insert_one(application)
        return redirect(url_for('list_jobs'))

    return render_template('user/detail.html', job=job)


@app.route('/job_admin/<job_id>', methods=['GET', 'POST'])
def job_detail2(job_id):
    job = db['jobs'].find_one({"_id": ObjectId(job_id)})
    applications = list(db['applications'].find({"job_id": job_id}))

    if request.method == 'POST':
        updates = {k: request.form[k] for k in [
            'title', 'department', 'nums', 'overview',
            'responsibilities', 'basic', 'preferred'
        ] if request.form[k]}
        if updates:
            db['jobs'].update_one({"_id": ObjectId(job_id)}, {"$set": updates})

        return redirect(url_for('job_detail2', job_id=job_id))

    return render_template('admin/detail2.html', job=job, applications=applications)


@app.route('/profile/<user_id>', methods=['GET', 'POST'])
def profile(user_id):
    application = db['applications'].find_one({"_id": ObjectId(user_id)})
    job = db['jobs'].find_one({"_id": ObjectId(application['job_id'])})

    if request.method == 'POST':
        action = request.form.get('action')
        state = 1 if action == 'accept' else -1 if action == 'reject' else None
        if state:
            db['applications'].update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"state": state}}
            )
        return redirect(url_for('job_detail2', job_id=application['job_id']))

    return render_template('admin/profile.html', application=application, job=job)


@app.route('/add_job', methods=['POST'])
def add_job():
    job_data = {k: request.form[k] for k in [
        'title', 'department', 'nums', 'overview',
        'responsibilities', 'basic', 'preferred'
    ]}
    job_data['nums'] = int(job_data['nums'])
    db['jobs'].insert_one(job_data)
    return jsonify({'status': 'success', 'message': 'Job added successfully!'})


if __name__ == '__main__':
    app.run(debug=True, port=8081)
