# pip install pandas
# pip install matplotlib


import pandas as pandas
import matplotlib.pyplot as plt
import os

# Setup file and read it into df using panda
filesdir = 'data/EPL/2018-19/E0.csv'
df = pandas.read_csv(filesdir)

# describe the csv
print(df.shape)
print(df.count())

# make a fig for the graph to be shown in
fig = plt.figure(figsize=(18,10))

# make a graph of the FTR values (full time results)
plt.subplot2grid((2,3), (0,0)) # gives the graph a location
df.FTR.value_counts(normalize=True).plot(kind="bar", alpha=1)
plt.title("Full Time Results")


# make a scatter graph of halftime results vs full time reslts
plt.subplot2grid((2,3), (0,1))
plt.scatter(df.HTHG, df.FTHG, alpha=0.1)
plt.title("(Home Team) Full Time Goals vs Half Time Goals")

# make a scatter graph of halftime results vs full time reslts
plt.subplot2grid((2,3), (0,2))
plt.scatter(df.HTAG, df.FTAG, alpha=0.1)
plt.title("(Away Team) Full Time Goals vs Half Time Goals")


# make a scatter graph of halftime results vs full time reslts
plt.subplot2grid((2,3), (0,1))
plt.scatter(df.HTHG, df.FTHG, alpha=0.1)
plt.title("Full Time Goals vs Half Time Goals")


# make a scatter graph of referees vs full time reslts (Home )
plt.subplot2grid((2,3), (1,0))
plt.scatter(df.FTHG, df.Referee, alpha=0.1)
plt.title("Referee full time home goals")

# make a scatter graph of referees vs full time reslts ( away)
plt.subplot2grid((2,3), (1,1))
plt.scatter(df.FTAG, df.Referee, alpha=0.1)
plt.title("Referee full time away goals")

# graph of full time home goals vs who won
#plt.subplot2grid((2,3), (1, 2), colspan=2)
# for x in ['H', 'A', 'D']:
    # df.FTHG[df.FTR == x].plot(kind="kde")
# plt.title("Full Time goals vs winner")
# plt.legend("Home", "Away", "Draw")

plt.show()