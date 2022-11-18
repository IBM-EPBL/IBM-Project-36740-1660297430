import email
from email import message
from importlib.resources import contents
from tkinter import S
from turtle import title
from flask import Flask,redirect, render_template, request, session, url_for, flash
# from flask_restful import Resource, Api, reqparse
import sendgrid
import sys
import os
import json
import requests
from pyexpat import model
from sqlalchemy import PrimaryKeyConstraint
from werkzeug.utils import secure_filename
import ibm_db
from flask_mail import Mail, Message
from markupsafe import escape

# import required module
import requests
import json
# mention url
url = "https://www.fast2sms.com/dev/bulkV2"


# create a dictionary
my_data = {
	# Your default Sender ID
	'sender_id': 'FastSM',
	
	# Put your message here!
	'message': 'Argent.......We need you help to save a life. There is demand for your blood. We request you to donate your blood in your nearby BloodBank connect with our Organization.',
	
	'language': 'english',
	'route': 'p',
	
	# You can send sms to multiple numbers
	# separated by comma.
	 'numbers': '9944222289'	
}

# create a dictionary
headers = {
	'authorization': 'QqbHW076SFDTledzUu4yhiYNIK2tf3LEnkc9Br5ZasOjp1VwxMLsyMZXA8IUPcEbdB6GJgvnDhwFfV2a',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache"
}
# make a post request
response = requests.request("POST",
							url,
							data = my_data,
							headers = headers)
#load json data from sourc
returned_msg = json.loads(response.text)

# print the send message
print(returned_msg['message'])


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bvx19292;PWD=yDuuJH7Oqdzbnxnk;", "", "")
print(conn)
print("connection successful...")




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

# @app.route('/admin')
# def admin():
#     customer = []
#     sql = f"SELECT * FROM customer"
#     stmt = ibm_db.exec_immediate(conn, sql)
#     dictionary = ibm_db.fetch_both(stmt)
#     while dictionary != False:
#         customer.append(dictionary)
#         dictionary = ibm_db.fetch_both(stmt)

#     if customer:
#         sql = "SELECT * FROM customer"
#         stmt = ibm_db.exec_immediate(conn, sql)
#         user = ibm_db.fetch_both(stmt)

#     return render_template('admin.html', customer = customer)



@app.route('/anegative/<andis>')
def anegative(andis):
    ancustomer = []
    sql = f"SELECT * FROM ANEGATIVE where district = '{escape(andis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        ancustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if ancustomer:
        sql = "SELECT * FROM ANEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', ancustomer = ancustomer)

@app.route('/apositive/<apdis>')
def apositive(apdis):
    apcustomer = []
    sql = f"SELECT * FROM APOSITIVE where district = '{escape(apdis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        apcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if apcustomer:
        sql = "SELECT * FROM APOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', apcustomer = apcustomer)

@app.route('/bnegative/<bndis>')
def bnegative(bndis):
    bncustomer = []
    sql = f"SELECT * FROM BNEGATIVE where district = '{escape(bndis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        bncustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if bncustomer:
        sql = "SELECT * FROM BNEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', bncustomer = bncustomer)

@app.route('/bpositive/<bpdis>')
def bpositive(bpdis):
    bpcustomer = []
    sql = f"SELECT * FROM BPOSITIVE where district = '{escape(bpdis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        bpcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if bpcustomer:
        sql = "SELECT * FROM BPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', bpcustomer = bpcustomer)


@app.route('/abnegative/<abndis>')
def abnegative(abndis):
    abncustomer = []
    sql = f"SELECT * FROM ABNEGATIVE where district = '{escape(abndis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        abncustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if abncustomer:
        sql = "SELECT * FROM ABNEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', abncustomer = abncustomer)

@app.route('/abpositive/<abpdis>')
def abpositive(abpdis):
    abpcustomer = []
    sql = f"SELECT * FROM ABPOSITIVE where district = '{escape(abpdis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        abpcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if abpcustomer:
        sql = "SELECT * FROM ABPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', abpcustomer = abpcustomer)


@app.route('/onegative/<ondis>')
def onegative(ondis):
    oncustomer = []
    sql = f"SELECT * FROM ONEGATIVE where district = '{escape(ondis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        oncustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if oncustomer:
        sql = "SELECT * FROM ONEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', oncustomer = oncustomer)

@app.route('/opositive/<opdis>')
def opositive(opdis):
    opcustomer = []
    sql = f"SELECT * FROM OPOSITIVE where district = '{escape(opdis)}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        opcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if opcustomer:
        sql = "SELECT * FROM OPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    return render_template('comments.html', opcustomer = opcustomer)



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

@app.route('/admin')
def admin():
    apcustomer = []
    sql = f"SELECT * FROM APOSITIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        apcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if apcustomer:
        sql = "SELECT * FROM APOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    ancustomer = []
    sql = f"SELECT * FROM ANEGATIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        ancustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if ancustomer:
        sql = "SELECT * FROM ANEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    bpcustomer = []
    sql = f"SELECT * FROM BPOSITIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        bpcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if bpcustomer:
        sql = "SELECT * FROM BPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    bncustomer = []
    sql = f"SELECT * FROM BNEGATIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        bncustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if bncustomer:
        sql = "SELECT * FROM BNEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    abpcustomer = []
    sql = f"SELECT * FROM ABPOSITIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        abpcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if abpcustomer:
        sql = "SELECT * FROM ABPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    abncustomer = []
    sql = f"SELECT * FROM ABNEGATIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        abncustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if abncustomer:
        sql = "SELECT * FROM ABNEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    opcustomer = []
    sql = f"SELECT * FROM OPOSITIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        opcustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if opcustomer:
        sql = "SELECT * FROM OPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    oncustomer = []
    sql = f"SELECT * FROM ONEGATIVE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        oncustomer.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if oncustomer:
        sql = "SELECT * FROM ONEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    apcount = []
    sql = f"SELECT PLACE, count(*) as num FROM APOSITIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        apcount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if apcount:
        sql = "SELECT * FROM APOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    ancount = []
    sql = f"SELECT PLACE, count(*) as num FROM ANEGATIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        ancount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if ancount:
        sql = "SELECT * FROM ANEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    bpcount = []
    sql = f"SELECT PLACE, count(*) as num FROM BPOSITIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        bpcount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if bpcount:
        sql = "SELECT * FROM BPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    bncount = []
    sql = f"SELECT PLACE, count(*) as num FROM BNEGATIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        bncount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if bncount:
        sql = "SELECT * FROM BNEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    abpcount = []
    sql = f"SELECT PLACE, count(*) as num FROM ABPOSITIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        abpcount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if abpcount:
        sql = "SELECT * FROM ABPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    abncount = []
    sql = f"SELECT PLACE, count(*) as num FROM ABNEGATIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        abncount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if abncount:
        sql = "SELECT * FROM ABNEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    opcount = []
    sql = f"SELECT PLACE, count(*) as num FROM OPOSITIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        opcount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if opcount:
        sql = "SELECT * FROM OPOSITIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    oncount = []
    sql = f"SELECT PLACE, count(*) as num FROM ONEGATIVE GROUP BY PLACE;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        oncount.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if oncount:
        sql = "SELECT * FROM ONEGATIVE"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    selled = []
    sql = f"SELECT * FROM REQPLASMA;"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        selled.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if selled:
        sql = "SELECT * FROM REQPLASMA"
        stmt = ibm_db.exec_immediate(conn, sql)
        user = ibm_db.fetch_both(stmt)

    
    return render_template('admin.html',apcustomer = apcustomer, ancustomer = ancustomer,bpcustomer = bpcustomer, bncustomer = bncustomer, abncustomer = abncustomer, abpcustomer = abpcustomer, opcustomer = opcustomer, oncustomer = oncustomer, apcount = apcount, ancount = ancount, bpcount = bpcount, bncount = bncount, abpcount = abpcount, abncount = abncount, opcount = opcount, oncount = oncount, selled = selled )




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

        

        if mail == 'abcd@gmail.com' and password == 'kil':
            return redirect(url_for('admin'))

        else:
            sql = f"select * from customer where email='{escape(mail)}' and password= '{escape(password)}'"
            stmt = ibm_db.exec_immediate(conn, sql)
            data = ibm_db.fetch_both(stmt)
            
        if data:
            session["mail"] = escape(mail)
            session["password"] = escape(password)
            return redirect(url_for('dashboard'))

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

        # sql = "SELECT * FROM reqplasma WHERE name=?"
        # stmt = ibm_db.prepare(conn, sql)
        # ibm_db.bind_param(stmt,1,uname)
        # ibm_db.execute(stmt)
        # account = ibm_db.fetch_assoc(stmt)

    # if account:
    #     return render_template('index.html', msg="You are already a member, please login using your details....")
      
    # else:
        if bloodgrp == 'A-VE':

            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)

            return redirect(url_for("anegative", andis = district))


        elif bloodgrp == 'A+VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("apositive", apdis = district))

        elif bloodgrp == 'B+VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("bpositive", bpdis = district))

        elif bloodgrp == 'B-VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("bnegative", bndis = district))

        elif bloodgrp == 'AB-VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("abnegative", abndis = district))

        elif bloodgrp == 'AB+VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("abpositive", abpdis = district))

        elif bloodgrp == 'O-VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("onegative", ondis = district))

        elif bloodgrp == 'O+VE':
            insert_sql = "INSERT INTO reqplasma VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
            return redirect(url_for("opositive", opdis = district))

        else:
            return "Please INSERT a valid Blood Group and Enter the Blood group in CAPITAL LETTERS like (A+VE, B-VE, AB+VE)..."
        
    # return render_template('comments.html', msg="Student Data saved successfuly..")


@app.route('/donateplasma', methods=['GET', 'POST'])
def donateplasma():
    if request.method == 'POST':
        uname = request.form['uname']
        phone = request.form['phone']
        bloodgrp = request.form['bloodgroup']
        place = request.form['place']
        district = request.form['district']

        # sql = "SELECT * FROM donateplasma WHERE name=?"
        # stmt = ibm_db.prepare(conn, sql)
        # ibm_db.bind_param(stmt,1,uname)
        # ibm_db.execute(stmt)
        # account = ibm_db.fetch_assoc(stmt)

    # if account:
    #     return render_template('index.html', msg="You are already a member, please login using your details....")
      
    # else:
        if bloodgrp == 'A+VE':
            insert_sql = "INSERT INTO APOSITIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)

        elif (bloodgrp == 'A-VE'):
            insert_sql = "INSERT INTO ANEGATIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)

        elif (bloodgrp == 'B+VE'):
            insert_sql = "INSERT INTO BPOSITIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)

        elif (bloodgrp == 'B-VE'):
            insert_sql = "INSERT INTO BNEGATIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)

        elif (bloodgrp == 'AB+VE'):
            insert_sql = "INSERT INTO ABPOSITIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
        
        elif (bloodgrp == 'AB-VE'):
            insert_sql = "INSERT INTO ABNEGATIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)
        
        elif (bloodgrp == 'O+VE'):
            insert_sql = "INSERT INTO OPOSITIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)


        elif (bloodgrp == 'O-VE'):
            insert_sql = "INSERT INTO ONEGATIVE VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, uname)
            ibm_db.bind_param(prep_stmt, 2, phone)
            ibm_db.bind_param(prep_stmt, 3, bloodgrp)
            ibm_db.bind_param(prep_stmt, 4, place)
            ibm_db.bind_param(prep_stmt, 5, district)
            ibm_db.execute(prep_stmt)

        else:
            return "Please INSERT a valid Blood Group and Enter the Blood group in CAPITAL LETTERS like (A+VE, B-VE, AB+VE)..."
    
    return render_template('thanks.html', msg="Student Data saved successfuly..")
    # return redirect(url_for("place",plc = place))




#---------------------------------------- Count -------------------------------------







    



if __name__ == "__main__":
    app.run(debug=True)

