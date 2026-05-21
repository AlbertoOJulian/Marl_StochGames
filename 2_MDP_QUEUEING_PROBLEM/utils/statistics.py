from collections import Counter


class EpisodeStatistics:
    """
    Summarize experiment.
    """

    def __init__(
            self,
            history):

        self.history = history

    def summarize(self):

        queues = [

            h["queue"]

            for h
            in self.history
        ]

        actions = [

            h["action"]

            for h
            in self.history
        ]

        rewards = [

            h["reward"]

            for h
            in self.history
        ]

        action_counts = (
            Counter(actions)
        )

        print(
            "\n===== Summary ====="
        )

        print(
            "\nAverage Queue:"
        )

        print(
            sum(queues)
            /
            len(queues)
        )

        print(
            "\nAction Frequencies:"
        )

        total = len(
            actions
        )

        for action,count in (
            action_counts.items()
        ):

            print(

                f"{action}: "

                f"{count/total:.2f}"
            )

        print(
            "\nAverage Reward:"
        )

        print(
            sum(rewards)
        / len(rewards)
        )