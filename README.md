# QNetwork Keras

QNetwork implemented with Keras.

# Game

The goal is simple : the agent has to go from point A to point B.

    A..........B

* If he stays in point A, a negative reward of **-1** is given.
* If he reaches point B, a positive reward of **10** is given.
* Any position inbetween has a **0** reward.

The agent has two actions available :

* Left
* Right
