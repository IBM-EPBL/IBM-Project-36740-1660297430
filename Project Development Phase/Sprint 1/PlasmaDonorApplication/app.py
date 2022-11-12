from flask import *
from flask import Flask,url_for, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS
from markupsafe import escape
from flask_db2 import DB2
import ibm_db
from cgi import print_form
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bvx19292;PWD=yDuuJH7Oqdzbnxnk;", "", "")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/users")
def profile1():
    return render_template('profile.html')

# ****************************************   DATABASE    *******************************************



@app.route("/database")
def database():
    stmt = ibm_db.exec_immediate(conn, "SELECT * from students")
    user = ibm_db.fetch_both(stmt)

    return render_template("profile.html", user = user)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['uname']
        mail = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        sql = "SELECT * FROM customer WHERE name=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,uname)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        return render_template('index.html', msg="You are already a member, please login using your details....")
      
    else:
      insert_sql = "INSERT INTO customer VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, uname)
      ibm_db.bind_param(prep_stmt, 2, mail)
      ibm_db.bind_param(prep_stmt, 3, phone)
      ibm_db.bind_param(prep_stmt, 4, password)
      ibm_db.execute(prep_stmt)
    
    return render_template('agentlogin.html', msg="Student Data saved successfuly..")


# @app.route("/database/<string:name>")
# def database(name):
#     stmt = ibm_db.exec_immediate(conn, "SELECT * from students where name = %s", (name))
#     user = ibm_db.fetch_both(stmt)
#     # len = ibm_db.num_rows(stmt)
#     return render_template("profile.html", user = user)




  
    
if __name__== "__main__":
    app.run(use_reloader = True, debug= True)

