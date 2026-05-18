import random


class WeatherMDP:

    def __init__(
            self,
            states,
            actions,
            transition_model,
            rewards):

        self.states = states
        self.actions = actions

        self.transition_model = transition_model

        self.rewards = rewards

    def next_state(
            self,
            current_state,
            action):

        probabilities = (
            self.transition_model
            [action]
            [current_state]
        )

        next_state = random.choices(
            self.states,
            weights=probabilities
        )[0]

        reward = (
            self.rewards
            [current_state]
            [action]
        )

        return next_state, reward

    def step(
            self,
            current_state,
            action):

        return self.next_state(
            current_state,
            action
        )