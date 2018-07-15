from game import Game
from keras.models import Sequential
from keras.layers import Dense, InputLayer
from time import sleep
import numpy as np

game = Game()

model = Sequential()
model.add(InputLayer(batch_input_shape=(1, game.length)))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(game.actionsCount, activation='linear'))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

gamma = 0.9
epsilon = 0.5
epsilonDecay = 0.999
epochs = 100

for i in range(epochs):
    print("Episode {}/{}".format(i + 1, epochs))
    s = game.reset()

    while not game.finished():
        if np.random.random() < epsilon:
            a = np.random.randint(0, game.actionsCount)
        else:
            a = np.argmax(model.predict(np.identity(game.length)[s:s + 1]))

        r, newS = game.takeAction(a)
        target = r + gamma * np.max(model.predict(np.identity(game.length)[newS:newS + 1]))
        target_vec = model.predict(np.identity(game.length)[s:s + 1])[0]
        target_vec[a] = target
        model.fit(np.identity(game.length)[s:s + 1], target_vec.reshape(-1, game.actionsCount), epochs=1, verbose=0)

        s = newS
        epsilon *= epsilonDecay


# Play Game after training
print("\nPlaying game...")
sleep(0.5)

s = game.reset()
while not game.finished():
    a = np.argmax(model.predict(np.identity(game.length)[s:s + 1]))
    r, newS = game.takeAction(a)
    s = newS
    game.display()
    sleep(0.3)
