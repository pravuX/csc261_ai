w1, w2, b = 0.0, 0.0, 0.0


def activation(x):
    if x <= 0:
        return 0
    return 1


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
outputs_and = [0, 0, 0, 1]
outputs_or = [0, 1, 1, 1]
epochs = 100
learning_rate = 0.01

# training


def train(outputs):
    global w1, w2, b
    for epoch in range(epochs):
        total_error = 0
        for i in range(len(inputs)):
            A, B = inputs[i]
            target_output = outputs[i]
            predicted_output = activation(
                w1 * A + w2 * B + b)
            error = target_output - predicted_output
            w1 += learning_rate * error * A
            w2 += learning_rate * error * B
            b += learning_rate * error
            total_error += abs(error)
        if total_error == 0:  # model converges
            print(f"Converged in {epoch} epochs.")
            print(
                f"Final weights and biases: {w1}, {w2}, {b}")
            break


# AND
print("AND Gate")
train(outputs_and)
# testing
for i in range(len(inputs)):
    A, B = inputs[i]
    output = activation(w1 * A + w2 * B + b)
    print(f"Input: ({A}, {B})  Output: {output}")

# OR
print("\nOR Gate")
w1, w2, b = 0.0, 0.0, 0.0
train(outputs_or)
# testing
for i in range(len(inputs)):
    A, B = inputs[i]
    output = activation(w1 * A + w2 * B + b)
    print(f"Input: ({A}, {B})  Output: {output}")
