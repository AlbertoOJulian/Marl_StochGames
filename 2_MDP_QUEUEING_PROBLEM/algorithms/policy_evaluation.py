class PolicyEvaluator:
    """
    Estimate state values
    under a fixed policy.

    Computes:

        V(queue)

    for all queue states.
    """

    def __init__(
            self,
            environment,
            agent,
            gamma=.95,
            iterations=1000):

        self.environment=environment

        self.agent=agent

        self.gamma=gamma

        self.iterations=iterations

        self.values={

            s:0

            for s in range(
                environment
                .config
                .max_queue+1
            )
        }


    def evaluate(self):
        """
        Estimate values by
        repeated simulation.
        """
        samples = 100
    
        for _ in range(self.iterations):
    
            new_values = {}
    
            for queue in self.values:
    
                action = (
                    self.agent
                    .choose_action(
                        queue
                    )
                )
    
                total = 0
    
                for _ in range(samples):
    
                    (
                        next_queue,
                        reward,
                        _,
                        _
    
                    )=(
    
                        self.environment
                        .step(
                            queue,
                            action
                        )
                    )
    
                    total += (
    
                        reward
    
                        +
    
                        self.gamma *
    
                        self.values[
                            next_queue
                        ]
    
                    )
    
                new_values[
                    queue
                ] = total/samples
    
            self.values = new_values
    
        return self.values        