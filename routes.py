# routes.py

from app import app
from app import cursor, conn
from flask import render_template, request

# homepage
@app.route('/')  # root : main page
def index():
    # by default, 'render_template' looks inside the folder 'template'
    cursor.execute("SELECT * FROM posts")
    result = cursor.fetchall()
    return render_template('index.html', data=result)

# form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        # request.method == 'POST'
        #name = request.form['name']
        #message = request.form['message']
        #cursor.execute("INSERT INTO posts (name, message) VALUES (%s,%s);", (name, message))
        #conn.commit()
        #return render_template('thanks.html')
        return render_template('sorry.html')