from flask import Flask, render_template, request, redirect, url_for, abort, session
import configuration

app=Flask(__name__)



@app.route('/home', methods=['GET'])
def root():
    return render_template('homePage.html'), 200

if __name__ =="__main__":
  app.run(host='0.0.0.0', debug=True)



