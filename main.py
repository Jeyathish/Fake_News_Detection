from flask import Flask, request, render_template
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/home1")
def home1():
    return render_template("home1.html")

@app.route("/")
def home2():
    return render_template("login.html")

@app.route('/', methods=['POST', 'GET'])
def my_form_post38():
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            user = request.form['username']
            password = request.form['password']
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                port="3308",
                passwd="",
                database="project_news",
                use_unicode=True,
                charset='ascii'
            )
            mycursor = mydb.cursor()
            sql = "select * from login where Username='" + user + "'and password='" + password + "'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if myresult:
                return render_template('home.html',Username=user)
            else:
                return "error"

@app.route("/feedback")
def home3():
    return render_template("feedback.html")

@app.route('/feedback', methods=['POST'])
def my_form_post5():
    user = request.form['name']
    user1 = request.form['email']
    user2 = request.form['message']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO feedback values('"+user+"','"+user1+"','"+user2+"')"
    mycursor.execute(sql)
    mydb.commit()
    return ("Thank you for your feedback")

@app.route("/about")
def home4():
    return render_template("about.html")

@app.route("/contact")
def home5():
    return render_template("contact.html")

@app.route("/decisionofnews")
def home6():
    return render_template("decisionofnews.html")

@app.route('/decisionofnews', methods=['POST'])
def my_form_post6():
    user = request.form['artno']
    user2 = request.form['feedback']
    user3 = request.form['rating']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO decisionofnews values('"+user+"','"+user2+"','"+user3+"')"
    sql1 = "Update newsdataentry SET NewsDecision='"+user3+"', Feedback='"+user2+"' WHERE Article ='"+user+"'"
    mycursor.execute(sql)
    mycursor.execute(sql1)
    mydb.commit()
    return ("Decision of News Inserted Successfully")

@app.route("/decisionofnews1")
def home21():
    return render_template("decisionofnews1.html")

@app.route('/decisionofnews1', methods=['POST'])
def my_form_post33():
    user = request.form['artno']
    user2 = request.form['feedback']
    user3 = request.form['rating']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "Update decisionofnews SET Feedback='"+user2+"',NewsDecision='"+user3+"' WHERE Article ='"+user+"'"
    sql1 = "Update newsdataentry SET NewsDecision='"+user3+"', Feedback='"+user2+"' WHERE Article ='"+user+"'"
    mycursor.execute(sql)
    mycursor.execute(sql1)
    mydb.commit()
    return ("Decision of News Updated Successfully")

@app.route("/deletenews")
def home7():
    return render_template("deletenews.html")

@app.route('/deletenews', methods=['POST'])
def my_form_post4():
      user = request.form['artno']
      mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          port="3308",
          passwd="",
          database="project_news",
          use_unicode=True,
          charset='ascii'
      )
      mycursor = mydb.cursor()
      sql = "delete from newsdataentry where Article='"+user+"'"
      sql1 = "delete from decisionofnews where Article='"+user+"'"
      mycursor.execute(sql)
      mycursor.execute(sql1)
      mydb.commit()
      return ("Your News was Deleted Successfully")

@app.route("/forget")
def home8():
    return render_template("forget.html")

@app.route("/insertnews")
def home9():
    return render_template("insertnews.html")

@app.route('/insertnews', methods=['POST'])
def my_form_post1():
    user = request.form['artno']
    user1 = request.form['heading']
    user2 = request.form['newss']
    user3 = request.form['location']
    user4 = request.files['image']
    user5 = request.form['newsd']
    user6 = request.form['feedback']

    filename = secure_filename(user4.filename)
    user4.save(app.config['UPLOAD_FOLDER'] + filename)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO newsdataentry values('"+user+"','"+user1+"','"+user2+"','"+user3+"','"+filename+"','"+user5+"','"+user6+"')"
    mycursor.execute(sql)
    mydb.commit()
    return ("Your News was Inserted Successfully")

@app.route("/newsview")
def my_form_post9():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            port="3308",
            passwd="",
            database="project_news",
            use_unicode=True,
            charset='ascii'
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM newsdataentry ORDER BY Article ASC"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        column_names = [i[0] for i in mycursor.description]
        mycursor.close()
        mydb.close()
        return render_template('newsview.html', column_names=column_names, rows=myresult)

@app.route("/updatenews")
def home11():
    return render_template("updatenews.html")

@app.route('/updatenews', methods=['POST'])
def my_form_post3():
    user = request.form['artno']
    user1 = request.form['heading']
    user2 = request.form['newss']
    user3 = request.form['location']
    user4 = request.files['image']
    user5 = request.form['newsd']
    user6 = request.form['feedback']

    filename = secure_filename(user4.filename)
    user4.save(app.config['UPLOAD_FOLDER'] + filename)

    mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          port="3308",
          passwd="",
          database="project_news",
          use_unicode=True,
          charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "Update newsdataentry SET Newsheading='"+user1+"',Newssummary='"+user2+"',Location='"+user3+"',Image='"+filename+"',NewsDecision='"+user5+"',Feedback='"+user6+"' WHERE Article ='"+user+"'"
    mycursor.execute(sql)
    mydb.commit()
    return ("Your News was Updated Successfully")

@app.route("/register")
def home12():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def my_form_post2():
    user = request.form['username']
    user1 = request.form['email']
    user2 = request.form['password']
    user3 = request.form['confirm-password']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO login values('"+user+"','"+user1+"','"+user2+"','"+user3+"')"
    mycursor.execute(sql)
    mydb.commit()
    return render_template("login.html")

@app.route("/register1")
def home13():
    return render_template("register1.html")

@app.route('/register1', methods=['POST'])
def my_form_post10():
    user = request.form['username']
    user1 = request.form['email']
    user2 = request.form['password']
    user3 = request.form['confirm-password']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO login1 values('"+user+"','"+user1+"','"+user2+"','"+user3+"')"
    mycursor.execute(sql)
    mydb.commit()
    return render_template("login1.html")

@app.route("/newsview1")
def my_form_post11():
      mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          port="3308",
          passwd="",
          database="project_news",
          use_unicode=True,
          charset='ascii'
      )
      mycursor = mydb.cursor()
      sql = "SELECT * FROM newsdataentry ORDER BY Article ASC"
      mycursor.execute(sql)
      myresult = mycursor.fetchall()
      column_names = [i[0] for i in mycursor.description]
      mycursor.close()
      mydb.close()
      return render_template('newsview1.html', column_names=column_names, rows=myresult)

@app.route("/forget1")
def home15():
    return render_template("forget1.html")

@app.route("/forget1", methods=['POST'])
def my_form_post24():
    user = request.form['email']
    return render_template('changepass.html', data=user)

@app.route("/contact1")
def home16():
    return render_template("contact1.html")

@app.route("/about1")
def home17():
    return render_template("about1.html")

@app.route("/login1")
def home18():
    return render_template("login1.html")

@app.route('/login1', methods=['POST', 'GET'])
def my_form_post12():
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            user = request.form['username']
            password = request.form['password']
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                port="3308",
                passwd="",
                database="project_news",
                use_unicode=True,
                charset='ascii'
            )
            mycursor = mydb.cursor()
            sql = "select * from login1 where Username='" + user + "'and password='" + password + "'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if myresult:
                return render_template("home1.html",Username=user)
            else:
                return "error"


@app.route("/newssearch")
def home19():
    return render_template("newssearch.html")

@app.route('/newssearch', methods=['POST', 'GET'])
def my_form_post8():
    user = "Article No: "
    user2 = "Details"
    user1 = request.form['artno']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "select * from newsdataentry where Article='" + user1 + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    column_names = [i[0] for i in mycursor.description]
    mycursor.close()
    mydb.close()
    return render_template('newssearch.html', column_names=column_names, rows=myresult,  data=user1, data1=user, data2=user2, user3=myresult)

@app.route("/newssearch1")
def home20():
    return render_template("newssearch1.html")

@app.route('/newssearch1', methods=['POST', 'GET'])
def my_form_post13():
    user = "Article No: "
    user2 = "Details"
    user1 = request.form['artno']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3308",
        passwd="",
        database="project_news",
        use_unicode=True,
        charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "select * from newsdataentry where Article='" + user1 + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    column_names = [i[0] for i in mycursor.description]
    mycursor.close()
    mydb.close()
    return render_template('newssearch1.html', column_names=column_names, rows=myresult, data=user1, data1=user, data2=user2, user3=myresult)

@app.route("/changepass")
def home22():
    return render_template("changepass.html")

@app.route('/changepass', methods=['POST'])
def my_form_post26():
    user = request.form['email']
    user1 = request.form['newPassword']
    user2 = request.form['confirmPassword']

    mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          port="3308",
          passwd="",
          database="project_news",
          use_unicode=True,
          charset='ascii'
    )
    mycursor = mydb.cursor()
    sql = "Update login1 SET password='"+user1+"',confirmpassword='"+user2+"' WHERE email ='"+user+"'"
    mycursor.execute(sql)
    mydb.commit()
    return ("Your user login password was Changed Successfully")

@app.route("/")
def salvador():
    return "Hello, Friends"

if __name__ == "__main__":
    app.run(debug=True)
