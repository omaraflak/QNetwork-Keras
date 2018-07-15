from game import Game
from keras.models import Sequential
from keras.layers import Dense, InputLayer
import matplotlib.pyplot as plt
import numpy as np

game = Game()

model = Sequential()
model.add(InputLayer(batch_input_shape=(1, game.length)))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(game.actionsCount, activation='linear'))
model.compile(loss='mse', optimizer='adadelta', metrics=['mae'])

gamma = 0.7
epsilon = 0.1
epsilonDecay = 0.999
epochs = 10

plt.title('Total reward per Game')
plt.ylabel('Game')
plt.xlabel('Reward')
reward = []

for i in range(epochs):
    print("Episode {}/{}".format(i + 1, epochs))
    s = game.reset()
    r_sum = 0

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
        r_sum += r

    reward.append(r_sum)

plt.plot(reward)
plt.show()
