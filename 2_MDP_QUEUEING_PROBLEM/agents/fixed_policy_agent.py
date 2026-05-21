class FixedPolicyAgent:
    """
    Threshold-based policy.

    Queue small:
        low service

    Queue medium:
        medium service

    Queue large:
        high service
    """

    def __init__(
            self,
            config):

        self.config = config

    def choose_action(
            self,
            queue):

        """
        Choose service action.
        """

        if queue == 0:

            return "NoAction"

        elif (

            queue
            <
            self.config
            .low_threshold

        ):

            return "LowService"

        elif (

            queue
            <
            self.config
            .high_threshold

        ):

            return "MediumService"

        return "HighService"