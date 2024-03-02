from flask import render_template,flash,Flask,request
import sqlite3
from mails import *

con = sqlite3.connect("userinfo.db",check_same_thread=False)
cur = con.cursor()

cur.execute("create table if not exists inquiries( nam varchar,email varchar,message varchar ,subject varchar)")

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"

@app.route('/',methods=['GET', 'POST'])
def home():
  if request.method == "POST":
       nam = request.form.get('name')
       email = request.form.get('email')
       subject = request.form.get('subject')
       message = request.form.get('textarea')

       cur.execute("insert into inquiries values('{}','{}','{}','{}')".format(nam,email,subject,message))
       con.commit()

       mailtoclient(email,nam)
       mailtoourself(email,nam,message,subject)
       flash("Thanks For your interest We'll Contact you soon",category="success")


  return render_template("index.html")


@app.route('/requests')
def requests():
     cur.execute("select * from inquiries")
     row = cur.fetchall()
     return render_template("requests.html",rows=row)


if __name__ == '__main__':
    app.run(debug=True)