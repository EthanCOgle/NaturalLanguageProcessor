# Basic Natural Langauge Processor

Built by Ethan Ogle to see how Math can be applied to Computer Science. Built from scratch (no tools or packages) using Linear Algebra techniques I learned in class to see how it would work.

## How It Works

1) Takes input training data to build a stochastic matrix where each entry (i, j) is the probability that j will follow i.
2) Takes an inital word i, multiplies the identity vector of that word to the stochasitc matrix to get the row of probabilities for the next word.
3) Chooses the next word based on the weights of the probabilites.
4) Adds that to the output which represents the Markov Chain and repeat for desired amount of generated content.
