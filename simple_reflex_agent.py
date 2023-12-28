def get_user_input(Q, i):
    response = input(f"{Q[i]}? (True or False)\n")
    if (response.lower().startswith('t')):
        return True
    else:
        return False


def agent():

    # Enumeration of statements
    p, q, r, s, t, u, v, w, x = range(9)

    # Questions about the environment
    Q = [
        "Is hall wet",
        "Is kitchen dry",
        "Is bathroom dry",
        "Is window closed",
        "Is it raining" ]

    truth_values = {
            u: False, v: False,
            w: False, x: False }
    for i in range(len(Q)):
        truth_values[i] = (get_user_input(Q, i))

    # The Rules
    if truth_values[p] and truth_values[q]:
        truth_values[u] = True

    if truth_values[p] and truth_values[r]:
        truth_values[v] = True

    if truth_values[s] or (not truth_values[t]):
        truth_values[w] = False

    if (not truth_values[w]) and truth_values[v]:
        truth_values[x] = True

    # Conclusion
    if truth_values[u] == True:
        print("There is leak in bathroom.")
    elif truth_values[x] == True:
        print("There is leak in kitchen.")
    elif truth_values[w] == True:
        print("Water is from outide.")
    else:
        print("The cause of leak is inconclusive.")


if __name__ == "__main__":
    agent()
