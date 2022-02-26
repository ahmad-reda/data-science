# European Soccer Database
## by Ahmad Reda


## Dataset

This database contains +25,000 european Soccer (Football) matches along with +10,000 players' data and their attirbutes.
It covers seasons from 2008 to 2016 in 11 european countries including each team of the lead leauge and the teams' attributes.
The whole database are provided through Kaggle datasets as a stort of a databse file containing different linked tables.
More information is provided through the database link.
https://www.kaggle.com/mkg2020/exploring-the-european-soccer-database/notebook

## Data Wrangling

There are 7 tables to load and get a summary about it.
It needed some efforts to clean this data and make it ready for the analysis as follows:

Drop columns with wrong entries and the columns of betting odds because they are out of the scope of this analysis.
Add the country name and the team name to the matches table.
Change date columns to datetime.
Drop the rows with nan values from the player attributes table
Drop the rows with wrong entries from the player attributes table
Fill nan values from the team attributes table with the smallest value

## Possible and Impossible Quesitions

The possible questions are:
Which league or country has most goals?
Which league or country has most Home wins and most Away wins?
Which teams have most scored goals for Home and Away matches?
Which teams have most golas difference (socred minus conceded) for Home and Away matches?
Which teams have most winning percentage for Home and Away matches?
What are the factors that might affect the match results?
Which players have improved the most?
Which teams have improved the most?

The impossible questions are:
Questions about fouls, cards, corners, ... >>> Because of wrong entries
Questions about players with most goals, penalities, passes, ... >>> Because of lack of data

## Single-factor analysis

Each factor has been analyzed by measuring its effect on the prior probabilities of home winning, away winning or draw.
This Effect is studied using bayes rule.
All factors can be studied using only two functions, one for the numeric factors, and the other function for the string factors.

# Example: The effect of the overall rating of the players on the results of the match

The two graphs give logical results as they indicate a great effect of the overall_rating attribute on the probabilities.
The less the values of home players'overall rating the less the probability of home winning, it even decreases than the away winning probability.
And the more the values of home players'overall rating the more the probability of home winning, it even reaches 80%! at the last category (from 80 to 85).
The same result comes from the analysis of the away graph with great increase in the away winning probability (about 59%)! at the last category (from 80 to 85).

# Interesting facts

Netherlands got the league with most scored goals.
Spain is the leading country in home winning percentage with FC Barcelona and Real Madrid CF in the lead in that over europe teams.
Scoltland is the leading country in away winning percentage with Rangers in the lead in that over europe teams.
Real Madrid CF and FC Barcelona are the leading teams in most scored home goals.
FC Barcelona got the lead in home goals difference and away goals difference.
Marco Reus is the most imporved player throughout the period between 2008 and 2016 with about 95% overall improvement.
Nicola Rigoni is the most improved goal keeper based on goal keeping reflexes throughout the period between 2010 and 2014.
FC Porto is the most improved team in build up play speed throughout the period between 2010 and 2015.
Ajax is the most imporved team in defence pressure throughout the period between 2010 and 2015.

# Factors that might affect the match result

Prior Home win, Away win, Draw probabilities equal 45.8%, 28.8%, and 25.4%, respectively.
Home and away strategy affects the match result in a minor way. This conclusion is questionable because it is not logical. This might have occured due to averaging the values of the positions of the eleven players. For upcoming analysis, it's better to consider it as different strategies, then be analyzed using classes instead of numerical values.
The player's average age barely affect the prior probabilities.
The less the values of home players' overall rating the less the probability of home winning, and the more the values of home players' overall rating the more the probability of home winning. It reached 80%! at the last category.
The less the values of away players' overall rating the less the probability of away winning, and the more the values of away players' overall rating the more the probability of away winning. It reached about 59%! at the last category (more than prior probability of home winning).
The home winning probability reaches more than 80%! when home players' reactions are between 80 and 85, and the away winning probability reaches more than 60%! when away player's reactions are between 80 and 85.
When the home players' attacking work rate is high, there is more chance of home winning. The same result holds true for the away players.
As the home team's defence pressure increases more than the average, the home winning probability increases as it reached more than 60% at the last category. The away winning probability reached about 46% at the last category. This posterior probability is greater than the posterior proability of home winning.
Home teams with free form positioning have more home winning probabilities as it reached about 77%. The same holds true for away teams with free form positioning as the away winning probabilities increaed to about 58% (more than home winning prior probability).

# Final note

All these factors are analyzed separatley based on Bayes' Theroem which means that other factors are fixed at their average values during the analysis.
This might be not practical, but it can be considered as preliminary analysis.
Also, there are no conclusions about signifcance here, as it needs inferential statistical analysis which is not used in this report.