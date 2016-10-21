from flask import Flask, render_template
import configuration

app=Flask(__name__)



@app.route('/home')
def root():
    return render_template('homePage.html'), 200

if __name__ =="__main__":
  app.run(
          host=app.config['ip_address'],
          port=int(app.config['port']))


