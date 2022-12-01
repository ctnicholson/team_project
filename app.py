from flask import Flask, render_template, request, url_for, redirect, session
import pymongo


app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://benjaminfunk:projectworldcup@cluster0.ak4mbaf.mongodb.net/test")
db = client.get_database('total_records')
records = db.register

@app.route("/", methods=['post', 'get'])
def landing():
    if request.method == 'GET':
        return render_template('landing.html')
    elif request.method == 'POST':
        if request.form['submit_button'] == 'login':
            return redirect(url_for("logged_in"))
        elif request.form['submit_button'] == 'registration':
            return redirect(url_for("registration"))


@app.route("/registration", methods=['post', 'get'])
def registration():
    message = ''
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('registration.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('registration.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('registration.html', message=message)
        else:
            user_input = {'name': user, 'email': email, 'password': password2}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
   
            return render_template('logged_in.html', email=new_email)
    return render_template('registration.html')

@app.route("/logged_in")
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in.html', email=email)
    else:
        return redirect(url_for("login"))
    
@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

       
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            
            if password == passwordcheck:
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")
    else:
        return render_template('registrations.html')




#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)
