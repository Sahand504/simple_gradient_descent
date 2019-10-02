
import matplotlib.pyplot as plt

PRECISION = 0.0001
MAX_STEP = 1000
ALPHA = 0.01
MIN_BETA, MAX_BETA = -5, +5

def func(beta):
    return beta**2


def dfunc(beta):
    return 2 * beta


next_beta = 4.5
beta_list = [next_beta]
f_list = [func(next_beta)]

step_count = 1
for i in range(1, MAX_STEP):
    if step_count == MAX_STEP-1:
        print("ALGORITHM STOPPED DUE TO MAX NUMBER OF STEPS")
        break

    current_beta = next_beta
    next_beta = current_beta - ALPHA * dfunc(current_beta)
    print("beta (step " + str(step_count) + ") = " + str(next_beta))

    if next_beta < MIN_BETA or next_beta > MAX_BETA:
        print("ERROR! BETA GET OUT OF THE RANGE!")
        next_beta = current_beta
        break

    if abs(func(next_beta) - func(current_beta)) <= PRECISION:
        print("CLOSE ENOUGH IN STEP " + str(step_count))
        break

    f = func(next_beta)
    beta_list.append(next_beta)
    f_list.append(f)
    step_count += 1

print("FINAL BETA = " + str(next_beta))
plt.plot(list(range(1, step_count+1)), f_list)
plt.xlabel("number of step")
plt.ylabel("f")
plt.show()


