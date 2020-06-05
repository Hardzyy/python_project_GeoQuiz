from flask import redirect, url_for, flash, render_template, request, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from sweater import db, app
from sweater.models import Users, Europe, Africa, Asia, Oceania, Europeflags
from sweater.quizbackend import get_random


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('pages/index.html')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('pages/main.html')


@app.route('/testFlagEurope', methods=['GET', 'POST'])
@login_required
def test_europe_flag():
    return render_template('tests/testFlagEurope.html', page_name="Test Flags of Europe")


@app.route('/update_eu_flags', methods=['POST', 'GET'])
@login_required
def update_europe_flag():
    array = get_random(Europeflags)
    return render_template('updata/updata_eu_flags.html', title='Test Flags of Europe', right_ans=array[0].name,
                           name=array[0].url_img, ans1=array[1].name, ans2=array[2].name, ans3=array[3].name,
                           ans4=array[4].name)


@app.route('/update_eu_flags/', methods=['POST', 'GET'])
@login_required
def update_eu_flag():
    array = get_random(Europeflags)
    return jsonify({'data': render_template('updata/updata_flag.html', right_ans=array[0].name,
                   name=array[0].url_img, ans1=array[1].name, ans2=array[2].name, ans3=array[3].name,
                   ans4=array[4].name)})


@app.route('/end_test_flag', methods=['GET', 'POST'])
@login_required
def end_test_flag():
    return jsonify({'data': render_template('updata/end_test_flag.html')})


@app.route('/testEurope', methods=['GET', 'POST'])
@login_required
def test_europe():
    return render_template('tests/testEurope.html', page_name="Test Europe")


@app.route('/update_eu', methods=['POST', 'GET'])
@login_required
def update_europe():
    array = get_random(Europe)
    return render_template('updata/updata_eu.html', title='Test Europe', right_ans=array[0].capital, name=array[0].name,
                           ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)


@app.route('/update_eu/', methods=['POST', 'GET'])
@login_required
def update_eu():
    array = get_random(Europe)
    return jsonify({'data': render_template('updata/updata.html', right_ans=array[0].capital, name=array[0].name,
                           ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)})


@app.route('/testAfrica', methods=['GET', 'POST'])
@login_required
def test_africa():
    return render_template('tests/testAfrica.html', page_name="Test Africa")


@app.route('/update_af', methods=['POST', 'GET'])
@login_required
def update_africa():
    array = get_random(Africa)
    return render_template('updata/updata_af.html', title='Test Africa', right_ans=array[0].capital, name=array[0].name,
                           ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)


@app.route('/update_af/', methods=['POST', 'GET'])
@login_required
def update_af():
    array = get_random(Africa)
    return jsonify({'data': render_template('updata/updata.html', right_ans=array[0].capital, name=array[0].name,
                           ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)})


@app.route('/testAsia', methods=['GET', 'POST'])
@login_required
def test_asia():
    return render_template('tests/testAsia.html', page_name="Test Asia")


@app.route('/update_as', methods=['POST', 'GET'])
@login_required
def update_asia():
    array = get_random(Asia)
    return render_template('updata/updata_as.html', title='Test Asia', right_ans=array[0].capital, name=array[0].name,
                           ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)


@app.route('/update_as/', methods=['POST', 'GET'])
@login_required
def update_as():
    array = get_random(Asia)
    return jsonify({'data': render_template('updata/updata.html', right_ans=array[0].capital, name=array[0].name,
                    ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)})


@app.route('/testOceania', methods=['GET', 'POST'])
@login_required
def test_oceania():
    return render_template('tests/testOceania.html', page_name="Test Oceania")


@app.route('/update_oc', methods=['POST', 'GET'])
@login_required
def update_oceania():
    array = get_random(Oceania)
    return render_template('updata/updata_oc.html', title='Test Asia', right_ans=array[0].capital, name=array[0].name,
                           ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)


@app.route('/update_oc/', methods=['POST', 'GET'])
@login_required
def update_oc():
    array = get_random(Oceania)
    return jsonify({'data': render_template('updata/updata.html', right_ans=array[0].capital, name=array[0].name,
                    ans1=array[1].capital, ans2=array[2].capital, ans3=array[3].capital, ans4=array[4].capital)})


@app.route('/end_test', methods=['GET', 'POST'])
@login_required
def end_test():
    return jsonify({'data': render_template('updata/end_test.html')})


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

    return render_template('pages/register.html')


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
    return render_template('pages/login.html')


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
