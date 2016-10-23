from flask import Flask, g, render_template, request, redirect, url_for, abort, session

import sqlite3
import configuration

from flask import Flask
app = Flask(__name__)
db_location = 'var/movies.db'

@app.route('/')
def root():
  return render_template('homePage.html'), 200

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
      with app.open_resource('movieInsert.sql', mode='r') as f:
        db.cursor().executescript(f.read())
      db.commit()

@app.route('/display', methods=['GET', 'POST'])
def display():

   db = get_db()
   cursor = db.execute('SELECt *  FROM movies')
   movies = [dict(title=row[0],
                  run_time=row[1],
                  Director=row[2],
                  Leading_actor=row[3],
                  release_date=row[4]) for row in cursor.fetchall()]
   return render_template('displayPage.html', movies=movies), 200


if __name__=='__main__':
  app.run('0.0.0.0', debug=True)


