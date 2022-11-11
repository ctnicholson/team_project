# World Cup Prediction Game

## Idea

We propose building a game that enables people to compete against friends in predicting the outcomes of the upcoming world cup matches. It would enable people to join a group session and, for every game, predict a set of key metrics (top scorer, winning team, etc.). 

When the game resolves, a set of points is allocated to each friend based on their prediction accuracy, and the process repeats until the final game of the world cup is played. Friends will be able to see each other on the leaderboard and even earn multiplier points based on streaks in performance. In essence, we want to take some of the features from Fantasy Football and make a fantasy-style tournament for the World Cup that can be used with our friends. 

## Learning goals

Enhance our understanding of UI/UX using Flask & HTML
Understand how to architect a multiplayer-based system
Solidify our understanding of APIs in a practical context
Learn how to use APIs that update automatically (without running), which will update the code once a result is determined (similar to betting systems).
Create a sophisticated algorithm to make a fun game

## Implementation plan

We will need to implement the individual user view, which we’re hoping to do in a bracket format so that the user can track their progress throughout the competition. We will need to figure out how to let the user adjust their predictions as different teams move forward in the tournament. 
From the individual points, we will need to be able to allocate them to groups. There may need to be a mechanism that lets users leave or join groups past the start of the tournament. 

We want a way for the users to view a leaderboard, so we will need to determine if that’s in a group or individual format for the rankings.
Although most soccer World Cup APIs are paid, [API-FOOTBALL] (https://www.api-football.com/) we found this one, which is free if less than 100 requests per day are made and involve metrics from goals scored to top goal scorers. We will need to read through the documentation to determine whether it works for the scope of our project and become familiar with it to use it.

## Schedule

November 15th
Map out the system’s necessary components (major files, the flows of information, initialize APIs to collect data)

November 19th
Filter out necessary API data to feed the point-allocation algorithm

November 24th
Develop a point allocation algorithm

November 29th
Create frontend assuming a one-player system


December 4th
Enhance frontend to enable multiplayer-functionality


## Collaboration plan

We’d like to try both individual and team programming throughout this project. We hope to have regular group meetings to tackle problems and pseudo-coding together. We will plan to have clear goals in mind for each meeting, and at the conclusion of each one, we will determine the individual work to be done before the next meeting. We’ll likely be reading API documentation on our own time to ensure we leave plenty of time for the actual group work within our meetings.
What worked well for our group assignment was playing to our strengths, so we plan to continue doing that for this project. It makes sense for us to work with skills we have developed throughout the class, and we cover a wide range of those between the three of us. We want to challenge ourselves to learn more, so we will try to help each other practice concepts that we may not feel super skilled in individually. 

## Risks

We’re glad that the bulk of our work will be after the World Cup kicks off, so we will have incoming data to test our code. However, there will still be a limited amount of matches for us to base our project on. With this data limitation, it may be difficult to account for all the different ways the matches can play out and how the results would go back to our users. 
The knockout games may come after our final deliverable; thus, testing our results based on real-world scores may be difficult. We will need to think of alternative methods to test the code. 

## Additional course content

Continuously updating results used in betting, which updates the code based on real-world results.

Designated user groups that allow for individualized views of the site, perhaps through a login functionality
