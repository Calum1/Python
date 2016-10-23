from flask import Flask, g, render_template

import sqlite3
import configuration

from flask import Flask
app = Flask(__name__)
db_location = 'var/movies.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
      db = sqlite3.connect(db_location)
      g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('movie.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        with app.open_resource('movieInsert.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route("/display/")
def root():
  return render_template('displayPage.html'), 200

@app.route("/db/")
def display():
    db = get_db()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies ORDER BY title"
    for row in db.cursor().execute(sql):
      page.append('<li>')
      page.append(str(row))
      page.append('</li>')

    page.append('</ul><html>')

    return ''.join(page)

if __name__ =='__main__':
  app.run('0.0.0.0', debug=True)


