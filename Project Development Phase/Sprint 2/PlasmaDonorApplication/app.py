import email
from email import message
from importlib.resources import contents
from tkinter import S
from turtle import title
from flask import Flask,redirect, render_template, request, session, url_for, flash
from pyexpat import model
from sqlalchemy import PrimaryKeyConstraint
from werkzeug.utils import secure_filename
import ibm_db
from flask_mail import Mail, Message
from markupsafe import escape



app = Flask(__name__)
mail = Mail(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bvx19292;PWD=yDuuJH7Oqdzbnxnk;", "", "")
print(conn)
print("connection successful...")


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'praveenmurugesan142001@gmail.com'
app.config['MAIL_PASSWORD'] = '9486352215'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
    message = "TEAM ID : PNT2022TMID37544" +" "+ "BATCH ID : B1-1M3E "
    return render_template('index.html',mes=message)


@app.route("/mail")
def mailing():
   msg = Message(
                'Hello',
                sender ='praveenmurugesan142001@gmail.com',
                recipients = ['nilaravi1974@gmail.com']
               )
   msg.body = 'Hello Flask message sent from Flask-Mail'
   mail.send(msg)
   return 'Sent'

#sql = "SELECT * FROM USER"
#stmt = ibm_db.exec_immediate(conn,sql)
#dictionary = ibm_db.fetch_both(stmt)
#while dictionary != False:
#    print("the name is :",dictionary )
#   print("*********************")
#    dictionary = ibm_db.fetch_both(stmt)
@app.route('/admin')
def admin():
    return render_template('admin.html',mes=message)


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods = ['GET','POST'])
def signup():
    return render_template('signup.html')

@app.route('/reqplasma', methods = ['GET','POST'])
def reqplasma():
    return render_template('plasmareq.html')


@app.route('/complaint')
def complaint():
    return render_template('complaint.html')


@app.route('/agentreg')
def agentreg():
    return render_template('agentreg.html')


@app.route('/agentlogin')
def agentlogin():
    return render_template('agentlogin.html')


@app.route('/agenthome')
def agenthome():
    return render_template('agenthome.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['uname']
        mail = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        bloodgrp = request.form['bloodgroup']

        sql = "SELECT * FROM customer WHERE name=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,uname)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        return render_template('index.html', msg="You are already a member, please login using your details....")
      
    else:
      insert_sql = "INSERT INTO customer VALUES (?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, uname)
      ibm_db.bind_param(prep_stmt, 2, mail)
      ibm_db.bind_param(prep_stmt, 3, phone)
      ibm_db.bind_param(prep_stmt, 4, password)
      ibm_db.bind_param(prep_stmt, 5, bloodgrp)
      ibm_db.execute(prep_stmt)
    
    return render_template('agentlogin.html', msg="Student Data saved successfuly..")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    sec = ''
    if request.method == 'POST':
        
        mail = request.form['email']
        password = request.form['password']
        print(mail, password)

        if mail == 'praveenkumarm078.cse@dgct.ac.in' and password == '1410':
            return redirect(url_for('admin'))

        else:
            sql = f"select * from customer where email='{escape(mail)}' and password= '{escape(password)}'"
            stmt = ibm_db.exec_immediate(conn, sql)
            data = ibm_db.fetch_both(stmt)
            
        if data:
            session["mail"] = escape(mail)
            session["password"] = escape(password)
            return redirect(url_for('complaint'))

        else:
            flash("Mismatch in credetials", "danger")
    





@app.route('/needplasma', methods=['GET', 'POST'])
def needplasma():
    if request.method == 'POST':
        uname = request.form['uname']
        phone = request.form['phone']
        bloodgrp = request.form['bloodgroup']
        place = request.form['place']
        district = request.form['district']

        sql = "SELECT * FROM reqplasma WHERE name=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,uname)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        return render_template('index.html', msg="You are already a member, please login using your details....")
      
    else:
      insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, uname)
      ibm_db.bind_param(prep_stmt, 2, phone)
      ibm_db.bind_param(prep_stmt, 3, bloodgrp)
      ibm_db.bind_param(prep_stmt, 4, place)
      ibm_db.bind_param(prep_stmt, 5, district)
      ibm_db.execute(prep_stmt)
    
    return render_template('comments.html', msg="Student Data saved successfuly..")



if __name__ == "__main__":
    app.run(debug=True)

