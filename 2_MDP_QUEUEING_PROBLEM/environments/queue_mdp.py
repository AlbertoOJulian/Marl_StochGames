import random


class QueueMDP:

    def __init__(
            self,
            config):

        self.config = config


    def expected_arrivals(
            self):
        """
        Compute expected arrivals:

        E[X] = Σ x P(x)

        Returns:
            float
        """

        expected = 0

        for value,prob in zip(

                self.config.arrival_values,

                self.config.arrival_probs):

            expected += (
                value*prob
            )

        return expected


    def expected_service(
            self,
            action):
        """
        Compute expected customers
        served for a given action.

        Assumes equal probability
        among service choices.

        Example:

        Medium=[1,2]

        E=(1+2)/2
        """

        service_values = (

            self.config
            .service_options[action]
        )

        return (

            sum(service_values)

            /

            len(service_values)

        )

    def expected_drift(
            self,
            action):
        """
        Compute expected queue drift.

        Drift:

        E[arrivals]
        -
        E[served]

        Interpretation:

        Positive:
            queue tends to grow

        Negative:
            queue tends to shrink

        Near zero:
            stable region

        Inputs:
            action

        Returns:
            float
        """

        expected_arrivals = (
            self.expected_arrivals()
        )

        expected_service = (
            self.expected_service(
                action
            )
        )

        return (

            expected_arrivals

            -

            expected_service

        )

    def generate_arrivals(self):

        return random.choices(

            self.config
            .arrival_values,

            weights=
            self.config
            .arrival_probs

        )[0]


    def generate_service(
            self,
            action):

        choices=(

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

        arrivals=(
            self.generate_arrivals()
        )

        served=(
            self.generate_service(
                action
            )
        )

        next_queue=(

            queue
            + arrivals
            - served
        )

        next_queue=max(
            0,
            next_queue
        )

        next_queue=min(
            next_queue,
            self.config.max_queue
        )

        reward=(
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