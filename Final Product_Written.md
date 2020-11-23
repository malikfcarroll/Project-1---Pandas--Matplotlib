In this project, I sought out to investigate what the prime years of a professional basketball player's career are.
A player's prime can be defined as the best, most productive years of a player's career.
One of the motivations for this project was to be able to predict where a player's performance is, and where it is trending.
For example, a use case would be in the construction of a team.
If I were building a team, I would want a mix of younger, middle-career, and veteran players to spread my risk around, and have some stability in the long run.
A situation you would not want to find yourself in is with a team of aging players, all of whom are exiting their prime and trending downwards.

Using data, I aimed to answer these questions by looking at four key performance statistics over the course of a player's career: points, rebounds, and field goal percentage.
My prediction going into the project was that all four of these statistics would follow somewhat of a bell-shaped curve over time, meaning that the middle years of their careers would be the most productive, with the beginning and ending years the least.
More specifically, I hypothesized that the ages of 26-30 would be the prime years of a given player's career.

When I went about finding a data set to pose these questions to, there were several important factors that were considered:
    Consistency of time period
      - Each era of basketball is different, so I did not want to have data that was skewed by changes in rules, styles of play, medicine, etc.
    Differences in minutes
      - Given that every player and team is different, no two players play the exact same amount of minutes in a season.
      - Players who play more minutes have an opportunity to accumulate higher statistics.
    A population with data covering the entire time period
      - Most players have short careers, yet I needed a population with careers long enough to draw conclusions.
      - At least 10 years needed.

In the end, this was the data set I settled on:
    Source = basketball-reference.com
    Population
      - Full statistics for 15 different players from the 2000-2001 NBA season to the NBA 2009-2010 season
      - 15 players chosen by looking at a list of players with the most All-Star appearances over the time frame
      - Started by including the player with the most appearances, and then adding more as you descend the list
      - Each player must have data from each of the ten seasons in our range, so those who did not were skipped and the next player down the All-Star appearances list was chosen
      - Statistics are already tallied in a per 36 minute format
      - Exported from the source as 15 independent .csv files

Some other factors that are important, but were not considered:
      Differences based on position
        - I would predict that the guard positions might have primes at younger ages than forwards and centers
      Differences based on play style
        - I would predict shooters might have primes at older ages than non-shooters
      Differences based on height
        - I would predict height has little effect on a player's prime
       Differences based on when a player's career started
        - I would predict players who start their careers out of high school might have primes at earlier ages than players who went to college

After completing my research, I concluded the following:

Points vs Age

This plot behaved relatively close to my predictions.
The curve of best fit follows a parabolic pattern, with a player's points highest between the ages of 23 and 27, before falling steadily as the player approaches and passes the age of 30.
Out of all of the regressions, this plot showed the strongest correlation.

Rebounds vs Age

This plot did not show any real effect of age on a player's rebounding.
This was evidence by a nearly horizontal curve of best fit.

Assists vs Age

This plot did not show any real effect of age on a player's passing.
This was evidenced by an R^2 value of less than 0.1

Field Goal Percentage vs Age

This plot did not show any real effect of age on a player's rebounding.
This was evidence by a nearly horizontal curve of best fit.


Overall

In total, the data was not very conclusive as far as shedding light of the ages of a player's prime.

One reason I believe the data was not very helpful in this exercise is because my population included only the best players from the time range.
Each of the players in my population had long, fruitful careers, and were considered the model of consistency over the decade.
For this reason, their career arcs probably don't follow those of an average NBA player.

Another limit of my data set was that there were only 15 players evaluated.
Because of the strict criteria, it was difficult to field a large sample size from which I could have possibly seen more of a trend.

One interesting finding of my research was that although points and field goal percentage are directly tied to each other, they did not exhibit the same behavior.
This was one of the key indicators that the sample was not large enough, as logically this does not make any sense.

Another possibility is that players' rebounding and passing abilities may not actually change much over the course of their careers.
To test this, I would look to get a larger, more diverse population.
