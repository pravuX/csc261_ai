w1, b = 0.0, 0.0


inputs = [0, 1]
outputs = [1, 0]
epochs = 100
learning_rate = 0.1


def activate(x):
    return 0 if x <= 0 else 1


print("NOT Gate")
for epoch in range(epochs):
    total_error = 0
    for i in range(len(inputs)):
        A = inputs[i]
        target_output = outputs[i]
        predicted_output = activate(w1 * A + b)
        error = target_output - predicted_output
        w1 += learning_rate * error * A
        b += learning_rate * error
        total_error += abs(error)
    if total_error == 0:
        print(f"Converged in {epoch} epochs.")
        print(f"Final weights and biases: {w1}, {b}")
        break

for A in inputs:
    output = activate(w1 * A + b)
    print(f"Input: {A} Output: {output}")
