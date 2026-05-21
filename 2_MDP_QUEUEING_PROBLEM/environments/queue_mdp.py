import random


class QueueMDP:
    """
    Queue-based MDP environment.

    State:
        queue length

    Dynamics:
        arrivals occur randomly
        action determines service level

    Reward:
        penalize queue size
        penalize expensive service
    """

    def __init__(
            self,
            config):

        self.config = config

    def generate_arrivals(self):
        """
        Random customer arrivals.
        """

        return random.choices(

            self.config.arrival_values,

            weights=
            self.config.arrival_probs

        )[0]

    def generate_service(
            self,
            action):
        """
        Determine customers served.
        """

        choices = (

            self.config
            .service_options[action]

        )

        return random.choice(
            choices
        )

    def compute_reward(
            self,
            queue,
            action):
        """
        Reward function.

        Smaller queues better.

        Expensive service penalized.
        """

        return (

            -queue

            -

            self.config
            .service_cost[action]
        )

    def step(
            self,
            queue,
            action):

        """
        Execute one transition.

        Returns:

            next_queue
            reward
            arrivals
            served
        """

        arrivals = (
            self.generate_arrivals()
        )

        served = (
            self.generate_service(
                action
            )
        )

        next_queue = (

            queue

            + arrivals

            - served
        )

        next_queue = max(
            0,
            next_queue
        )

        next_queue = min(
            next_queue,
            self.config.max_queue
        )

        reward = (
            self.compute_reward(
                next_queue,
                action
            )
        )

        return (
            next_queue,
            reward,
            arrivals,
            served
        )