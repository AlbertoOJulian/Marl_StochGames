class FixedPolicyAgent:

    def __init__(self, policy):

        self.policy = policy

    def choose_action(
            self,
            state):

        return self.policy[state]