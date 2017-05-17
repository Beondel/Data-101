from numpy import *
import matplotlib.pyplot as plt


def compute_error_for_line_given_points(b, m, points):
    total_error = 0

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b))**2

    return total_error / float(len(points))


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)

    return [b, m]


def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0

    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]

        b_gradient += -(2 / N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / N) * x * (y - ((m_current * x) + b_current))

    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)

    return [new_b, new_m]


def run():
    # step 1: collect data
    points = genfromtxt('data.csv', delimiter=',')
    # step 2: define hyperparameters
    learning_rate = 0.0001  # how fast the model should converge
    initial_b = 0  # initial y intercept
    initial_m = 0  # initial slope
    num_iterations = 1000

    # step 3: train model
    print('starting gradient descent at b = {0}, m = {1}, error = {2}'.format(
        initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print('ending point at b = {1}, m = {2}, error = {3}'.format(num_iterations,
                                                                 b, m, compute_error_for_line_given_points(b, m, points)))


if __name__ == '__main__':
    run()