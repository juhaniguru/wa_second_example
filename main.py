
import contextlib
import os
import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@contextlib.contextmanager
def connect():
    conn = None
    try:
        conn = sqlite3.connect('users.sqlite')
        yield conn
    finally:
        if conn is not None:
            conn.close()

# _get_users

# erillinen funktio käyttäjien noutamiselle tietokannasta,
# koska tarvitaan useammassa paikassa
def _get_users(conn):
    cur = conn.cursor()
    cur.execute(
        "SELECT users.id, users.name, users.email, departments.name FROM users INNER JOIN departments ON departments.id = users.department_id")
    _users = cur.fetchall()
    users_list = []
    for u in _users:
        users_list.append({'id': u[0], 'name': u[1], 'email': u[2], 'department': u[3]})
    return users_list

@app.route('/users')
def users():
    with connect() as con:
        _users = _get_users(con)
        return render_template('users/index.html', users=_users, error=None)

@app.route('/button_example')
def button_example():
    return render_template('button_example.html')


@app.route('/delete-user', methods=['POST'])
def delete_user():
    _body = request.form
    userid = _body.get('userid')
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (userid, ))
        conn.commit()
        cursor.close()
        return ""

@app.route('/upload', methods=['GET'])
def upload_form():
    return render_template('form_upload.html')

@app.route('/upload', methods=['POST'])
# tämä routehandler hoitaa tiedoston latauksen palvelimelle
def upload_file():
    # määritetään kansio tiedostoille
    # ja luodaan, jos sitä ei ole vielä olemassa
    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if 'file' not in request.files:
        
        # jos file-namella ei löydy dataa reqeust bodysta, laitetaan sama sivu takaisin käyttäjälle virheen kanssa

        return render_template('file_upload.html', error='file not found')
    file = request.files['file']
    if file.filename == '':
        return render_template('file_upload.html', error='no selected file')
    if file:
        # jos file löytyy, tallennetaan se files-kansioon omalla nimellään
        # ja ohjataan käyttäjä takaisin latausformille
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('upload_form'))


@app.route('/pure_js')
def pure_js():
    return render_template('users_pure_js.html')

if __name__ == '__main__':
    app.run(port=3001, debug=True)
