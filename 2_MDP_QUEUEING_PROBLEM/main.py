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


queue_config = QueueConfig()

policy_config = PolicyConfig()


environment = QueueMDP(
    queue_config
)

agent = FixedPolicyAgent(
    policy_config
)


queue = 0

history = []


for t in range(1000):

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