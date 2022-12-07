from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import data_reader
import bcrypt
import scoring
import leaderboard
import collections.abc

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.iimjdzh.mongodb.net/test")
db = client.get_database('total_records')
records = db.register

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/some-route')
def some_route():
    email = request.session["email"]

    # Connect to the MongoDB database
    client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.iimjdzh.mongodb.net/test")
    db = client.get_database('total_records')
    records = db.register

    # Retrieve the user's bet from the database
    user_bet = records.find_one({"email": email})["bet"]

    
@app.route("/", methods=['post', 'get'])
def landing():
    if request.method == 'GET':
        return render_template('landing.html')
    elif request.method == 'POST':
        if request.form['submit_button'] == 'Login':
            return redirect(url_for("logged_in"))
        elif request.form['submit_button'] == 'Register':
            return redirect(url_for("registration"))


@app.route("/registration", methods=['post', 'get'])
def registration():
    message = ''
    if "email" in session:
        return redirect(url_for("bet"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
        
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
            user_input = {'name': user, 'email': email, 'password': hashed_password, 'bet': []}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
   
            return render_template('logged_in.html', email=new_email)
    return render_template('registration.html')


@app.route("/logged_in")
def logged_in():
    if "email" in session:
        email = session["email"]
        return redirect(url_for("bet"))
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
            
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
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


@app.route("/bet", methods=['POST', 'GET'])
def bet():
  if request.method == 'GET':
    data = data_reader.clean_data()
    arr = []

    for item in data:
      team1, team2 , score = item
      arr.append([team1, team2, score])

    return render_template('bet.html', matches=arr)

  if request.method == 'POST':
    # Use the correct endpoint name when calling url_for()
    selected_game = request.form.get("selected_game")
    # Assign the values of home_score and away_score here
    home_score = request.form.get("home-score")
    away_score = request.form.get("away_score")

    game = request.args.get("game")
    home_team = game["home_team"] if game is not None else "Unknown"
    away_team = game["away_team"] if game is not None else "Unknown"

    
    return redirect(url_for('choose_bet', game=selected_game))
    
    
@app.route("/choose_bet", methods=['POST', 'GET'])
def choose_bet():
  if request.method == 'POST':
    # Retrieve the user's bet from the request object
    home_team = request.form.get("home-team")
    away_team = request.form.get("away-team")
    home_score = request.form.get("home-score")
    away_score = request.form.get("away-score")

    user_bet = {
      "home_team": home_team,
      "away_team": away_team,
      "home_score": home_score,
      "away_score": away_score
    }

    if "email" in session:
        email = session["email"]

        records.update_one({"email": email}, {"$push": {"bet": user_bet}})

    return redirect(url_for('bet'))


  # Get the home and away teams from the request object
  home_team = request.args.get("home-team")
  away_team = request.args.get("away-team")

  # Generate the HTML for the form
  form = """
  <form method="post">
    <input type="hidden" name="home-team" value="{}">
    <input type="hidden" name="away-team" value="{}">
    <label>Enter the predicted score for the {}:</label>
    <input type="number" name="home-score" placeholder="e.g. 5">
    <label>Enter the predicted score for the {}:</label>
    <input type="number" name="away-score" placeholder="e.g. 3">
    <input type="submit" value="Submit">
  </form>
  """.format(home_team, away_team, home_team, away_team)

  # Return the HTML for the form
  return form
    
    
    
@app.route("/leaderboard", methods=['GET'])
def leaderboard_page(): 
    
    leaderboard = {}
    
    if request.method == 'GET':

        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.iimjdzh.mongodb.net/test")
        db = client.get_database('total_records')
        records = db.register

        user_records = records.find()
        for user in user_records:
            if user and 'bet' in user.keys() and isinstance(user['bet'], collections.abc.Sequence):
                for b in (user['bet']):
                    if user['name'] in leaderboard.keys():
                        leaderboard[user['name']] += scoring.get_scores(b)
                    else:
                        leaderboard[user['name']] = scoring.get_scores(b)
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        
    print(sorted_leaderboard)
    return render_template('leaderboard.html', leaderboard=sorted_leaderboard)
                

#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)



