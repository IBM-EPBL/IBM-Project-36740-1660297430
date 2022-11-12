
# from flask import Flask, render_template
# from cgi import print_form
# import ibm_db

# conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bvx19292;PWD=yDuuJH7Oqdzbnxnk;", "", "")
# app = Flask(__name__)

# print(conn)
# print('Connected Successfully...')

# @app.route('/list')
# def list():
#     students = []
#     sql = "SELECT * FROM demo"
#     stmt = ibm_db.exec_immediate(conn, sql)
#     dictionary = ibm_db.fetch_both(stmt)
#     while dictionary != False:
#         students.append(dictionary)
#         dictionary = ibm_db.fetch_both(stmt)
#     if students:
#         return render_template("profile.html", students = students)
#     else:
#         return '<br><br><br> Students not found '