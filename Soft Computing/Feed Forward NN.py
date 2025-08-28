import numpy as np
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
tragets = np.array([0,0,0,1])
learning_rate= 0.1
epochs = 100
weights = np.random.rand(2)
activation_function =lambda x:1 if x>0 else 0
for epoch in range(epochs):
    for i in range(len(inputs)):
        net_input = np.dot(inputs[i],weights)
        output = activation_function(net_input)
        weights+=learning_rate*(tragets[i]-output)*inputs[i]
print('Final Weights:', weights)