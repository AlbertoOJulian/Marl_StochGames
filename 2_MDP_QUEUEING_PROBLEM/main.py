from environments.queue_mdp import (
    QueueMDP
)

from agents.fixed_policy_agent import (
    FixedPolicyAgent
)

from configs.queue_config import (
    QueueConfig
)

from configs.policy_config import (
    PolicyConfig
)

from utils.visualization import (
    print_episode
)

from utils.statistics import (
    EpisodeStatistics
)

from algorithms.policy_evaluation import (
    PolicyEvaluator
)


queue_config = QueueConfig()

policy_config = PolicyConfig()


environment = QueueMDP(
    queue_config
)

agent = FixedPolicyAgent(
    policy_config
)


## Expected Arrivals, Service, and Drift
print(
    "\nExpected Arrivals:"
)

print(
    environment.expected_arrivals()
)


for action in [

        "NoAction",

        "LowService",

        "MediumService",

        "HighService"

]:

    print(

        f"\nExpected Service "
        f"{action}:"

    )

    print(

        environment
        .expected_service(
            action
        )
    )


print("\nExpected Drift")

for action in [

        "NoAction",

        "LowService",

        "MediumService",

        "HighService"

]:

    drift = (
        environment
        .expected_drift(
            action
        )
    )

    print(

        f"{action}: "

        f"{drift:.2f}"

    )

queue = 0

history = []


for t in range(100):

    action = (
        agent.choose_action(
            queue
        )
    )

    (
        next_queue,
        reward,
        arrivals,
        served

    ) = environment.step(
        queue,
        action
    )

    history.append({

        "time": t,

        "queue": queue,

        "action": action,

        "arrivals": arrivals,

        "served": served,

        "next_queue": next_queue,

        "reward": reward
    })

    queue = next_queue


print_episode(
    history
)

stats = (
    EpisodeStatistics(
        history
    )
)

stats.summarize()

evaluator=PolicyEvaluator(

    environment,

    agent,

    gamma=.95,

    iterations=1000
)

values=(
    evaluator.evaluate()
)

print(
    "\nState Values"
)

for state,value in (
        values.items()
):

    print(

        f"Queue {state}: "

        f"{value:.2f}"
    )