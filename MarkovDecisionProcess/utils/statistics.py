from collections import Counter


class EpisodeStatistics:

    def __init__(self, history):

        self.history = history

    def summarize(self):

        states = [
            h["state"]
            for h in self.history
        ]

        actions = [
            h["action"]
            for h in self.history
        ]

        rewards = [
            h["reward"]
            for h in self.history
        ]

        state_counts = Counter(states)

        action_counts = Counter(actions)

        total_reward = sum(rewards)

        avg_reward = (
            total_reward /
            len(rewards)
        )

        print("\n===== Summary =====")

        print("\nState Frequencies")

        total_states = len(states)

        for state,count in state_counts.items():

            print(
                f"{state}: "
                f"{count/total_states:.3f}"
            )

        print("\nAction Frequencies")

        total_actions = len(actions)

        for action,count in action_counts.items():

            print(
                f"{action}: "
                f"{count/total_actions:.3f}"
            )

        print(
            f"\nTotal Reward: "
            f"{total_reward}"
        )

        print(
            f"Average Reward: "
            f"{avg_reward:.2f}"
        )