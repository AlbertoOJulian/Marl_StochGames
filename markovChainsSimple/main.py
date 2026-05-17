import random
from collections import Counter
import matplotlib.pyplot as plt


class MarkovChain:

    def __init__(self, states, transition_matrix):

        self.states = states
        self.transition_matrix = transition_matrix

        self.validate()

    def validate(self):

        for state in self.states:

            if state not in self.transition_matrix:

                raise ValueError(
                    f"{state} missing in transition matrix"
                )

            total = sum(
                self.transition_matrix[state]
            )

            if abs(total - 1.0) > 0.0001:

                raise ValueError(
                    f"{state} probabilities do not sum to 1"
                )

    def get_transition_matrix(self):
        """
        Display transition probabilities
        in a readable format
        """

        print("\nTransition Matrix\n")

        header = "State".ljust(12)

        for state in self.states:
            header += state.ljust(12)

        print(header)

        for state in self.states:

            row = state.ljust(12)

            for probability in self.transition_matrix[state]:

                row += f"{probability:.2f}".ljust(12)

            print(row)

    def next_state(self, current_state):

        probabilities = self.transition_matrix[current_state]

        return random.choices(
            self.states,
            weights=probabilities
        )[0]

    def simulate(
            self,
            start_state,
            n_steps):

        current = start_state

        trajectory = [current]

        for _ in range(n_steps):

            current = self.next_state(
                current
            )

            trajectory.append(current)

        return trajectory

    def compute_statistics(
            self,
            trajectory):

        counts = Counter(
            trajectory
        )

        total = len(
            trajectory
        )

        frequencies = {}

        print("\nLong-run frequencies:\n")

        for state in self.states:

            frequency = (
                counts[state]/total
            )

            frequencies[state] = frequency

            print(
                f"{state}: "
                f"{frequency:.3f}"
            )

        return frequencies

    def plot_frequencies(
            self,
            trajectory):

        counts = Counter(
            trajectory
        )

        frequencies = []

        total = len(
            trajectory
        )

        for state in self.states:

            frequencies.append(
                counts[state]/total
            )

        plt.figure()

        plt.bar(
            self.states,
            frequencies
        )

        plt.xlabel(
            "States"
        )

        plt.ylabel(
            "Frequency"
        )

        plt.title(
            "Estimated Stationary Distribution"
        )

        plt.ylim(
            0,
            1
        )

        plt.show()


def main():

    states = [
        "Sunny",
        "Cloudy",
        "Rainy"
    ]

    transition_matrix = {

        "Sunny":[0.7,0.2,0.1],

        "Cloudy":[0.3,0.4,0.3],

        "Rainy":[0.2,0.5,0.3]
    }

    weather = MarkovChain(
        states,
        transition_matrix
    )

    weather.get_transition_matrix()

    trajectory = weather.simulate(
        start_state="Sunny",
        n_steps=10000
    )

    weather.compute_statistics(
        trajectory
    )

    weather.plot_frequencies(
        trajectory
    )


if __name__ == "__main__":
    main()