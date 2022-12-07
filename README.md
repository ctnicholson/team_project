**Team Members: Maria Herwagen, Callum Nicholson, Benjamin Funk**

**_Why did we do this?_**

Meet Zhi Li, a die-hard soccer fan who is excited for the upcoming World Cup. He loves watching the games and cheering for his favorite team, but he also enjoys the competition and strategic thinking involved in making decisions, and feels there is not a great platform currently out there to do so.

![Football Fan](https://media.tenor.com/EMqayFYzDsAAAAAC/football-world-cup.gif)

One day, Zhi Li learns about our World Cup prediction game and decides to give it a try. He downloads the software from GitHub, creates an account, and starts to make his predictions for the upcoming matches. He finds the user interface to be intuitive and easy to use, and he enjoys the social aspect of the game, which allows him to compete with his friends, family and students, to see who has the best predictions. 

![Prediction](https://media.tenor.com/f0lrUDqGWkYAAAAM/the-smurfs-brainy-smurf.gif)

Eventually, the World Cup reaches the final stage and Zhi Li is in 2nd place, incredibly close to the first place position. He is on the edge of his seat as he watches the final match, and his predictions are on the line. He has bet that Portugall will beat Argentina 2-1, and first place in the league has bet 2-1 for Argentina. In the 92nd minute of the match, Portugal get a penalty... Cristiano Ronaldo stands up to take it. Ronaldo takes a deep breath... the ref blows the whistle... Ronaldo shoots the ball into the top right corner... GOAAAALLLLLL!!! Portugal have won the World Cup and Zhi Li has won his prediction league, and has won bragging rights for the next 4 years in his friend group. He can hardly believe it , and is thrilled to see that he has come out on top of the leaderboard in his league with friends. 

![Zhi Li celebrating win](https://media.tenor.com/HAGXdX-X-1cAAAAM/no1-happy.gif)

---
**_INSTRUCTIONS_**

Here is a quick run through on how you can use our game:

:globe_with_meridians: Click the following link: https://worldcup-bets.herokuapp.com/

:white_check_mark: Register or Login (if user has previously registered), which will send you to Upcoming Fixtures page

:soccer: Make bets for the games, by clicking on "Click to bet!"

:lock: Select score you want to lock in for each team and click submit, which will send you back to Upcoming Fixtures page

:mag_right: Use the navigation bar to navigate across sections, such as the leaderboard page

:confetti_ball: In the leaderboard page you can check your score relative to other users

---
**_IMPLEMENTATION INFORMATION_**

Now, we are sure you are wondering, what is under the hood of the World Cup prediction game, and how does the code really work?

Well here is a diagram to help with our explanation

<img width="2026" alt="Flow chart (Community) (4)" src="https://user-images.githubusercontent.com/112514394/206074976-f4bb6a9d-6c8b-4513-8c72-eb948f7de8eb.png">

* The first step our code performs is pulling the data from our World Cup API (api-sports.io)
* Once this data is pulled, it is processed under the data_reader file. This file cleans the data, and returns teams & scores (scores returned as None for games not played yet) of games not played yet
* Then bet.html loads this information into the table, and gives the user the ability to bet on the game
* Through app.py and registration.html, the user is able to register or login
* The user registers and uses the form to store username and password, which is then encrypted and stored in MongoDB
* Once the user logs in, this automatically loads the bets page (bet.html)
* From bet.html we go to the choose_bet.html which takes in the core predictions 
* These user bets are then appended to MongoDB
* Then, the scoring.py file compares the bets to the real-time updated scores 
* Scoring.py returns each player's points
* Scoring.py sends the player names and points to the leaderboard
* The leaderboard renders a table of players and points

---
**_PROJECT EVOLUTION_**

As the World Cup began, three ambitious software developers - Benji, Maria and Callum - set out on a mission to create the ultimate World Cup prediction game.

The first step in their journey was to brainstorm ideas. As they sat in their office, they threw around different concepts and eventually landed on the idea of creating a tool that would allow users to make predictions about the outcomes of World Cup matches.

With their idea in place, the next step was to find the right API to power their project. After hours of research, they finally found the perfect API and set to work building the functions that would allow them to pull data from the API and use it in their project.

But as they worked on building these functions, they quickly realized that the data they were pulling from the API was messy and unorganized. Undeterred, they spent hours cleaning and organizing the data, transforming it into a format that was easy to work with and ready to be used in their project.

With their data cleaned and organized, it was time to focus on the front end of their project. Using Flask, they created a user-friendly interface with a navigation bar and buttons that allowed users to easily navigate between different pages and interact with the various features of their project.

One of the key features of their project was the ability to make predictions about the outcomes of World Cup matches. To do this, they first had to break down the scoring logic for making predictions and discuss it as a group. They then translated this logic into code, which allowed them to build the prediction functionality into their project.

As users started making predictions, they knew that they needed to create a leaderboard to track their performance. So they spent a lot of time developing this feature, testing it to ensure that it worked properly and was user-friendly. 

In the end, their hard work and collaboration paid off. They had created a World Cup prediction tool that was robust, user-friendly and a lot of fun to use. As users started using their project, they received a lot of positive feedback and were proud of the work that they had done. It was a great experience and a reminder of the power of collaboration and hard work in the world of software development.

---
**_EXTERNAL RESOURCES_**
Navigation bar and registration help: https://medium.com/codex/simple-registration-login-system-with-flask-mongodb-and-bootstrap-8872b16ef915
