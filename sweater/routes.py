from flask import redirect, url_for, flash, render_template, request, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from sweater import db, app
from sweater.models import Users, Europe
from sweater.quizbackend import get_random


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('main.html')


@app.route('/testEurope', methods=['GET', 'POST'])
@login_required
def test_europe():
    return render_template('testEurope.html')


@app.route('/_update', methods=['POST', 'GET'])
@login_required
def update1():
    array = get_random(Europe)
    return render_template('updata1.html', right_ans=array[0].capital, name=array[0].name, ans1=array[1],
                           ans2=array[2], ans3=array[3], ans4=array[4])


@app.route('/_update/', methods=['POST', 'GET'])
@login_required
def update():
    array = get_random(Europe)
    return jsonify({'data': render_template('updata.html', right_ans=array[0].capital, name=array[0].name,
                                            ans1=array[1], ans2=array[2], ans3=array[3], ans4=array[4])})


@app.route('/end_test', methods=['GET', 'POST'])
@login_required
def end_test():
    return jsonify({'data': render_template('end_test.html')})


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    if request.method == 'POST':
        if not(login or password or password2):
            flash('Please fill all fields!')
        elif password != password2:
            flash('Passwords are not the same!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = Users(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = Users.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main'))
        else:
            flash('Login or password is not correct')
    else:
        flash('Please enter login and password fields')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_singin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response
