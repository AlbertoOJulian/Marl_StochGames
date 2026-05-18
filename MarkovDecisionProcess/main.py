from environments.weather_mdp import WeatherMDP
from agents.fixed_policy_agent import FixedPolicyAgent

from utils.visualization import (
    print_episode
)

from utils.statistics import (
    EpisodeStatistics
)

states = [
    "Sunny",
    "Cloudy",
    "Rainy"
]

actions = [
    "StayInside",
    "GoOutside"
]


transition_model = {

    "StayInside":{

        "Sunny":[0.95,0.04,0.01],

        "Cloudy":[0.3,0.4,0.3],

        "Rainy":[0.2,0.5,0.3]
    },

    "GoOutside":{

        "Sunny":[0.5,0.3,0.2],

        "Cloudy":[0.2,0.5,0.3],

        "Rainy":[0.1,0.3,0.6]
    }
}


rewards = {

    "Sunny":{

        "StayInside":2,
        "GoOutside":10
    },

    "Cloudy":{

        "StayInside":4,
        "GoOutside":5
    },

    "Rainy":{

        "StayInside":8,
        "GoOutside":-5
    }
}


policy = {

    "Sunny":"GoOutside",

    "Cloudy":"GoOutside",

    "Rainy":"StayInside"
}


environment = WeatherMDP(
    states,
    actions,
    transition_model,
    rewards
)

agent = FixedPolicyAgent(
    policy
)


state = "Sunny"

history = []

for t in range(20):

    action = (
        agent.choose_action(
            state
        )
    )

    next_state,reward = (
        environment.step(
            state,
            action
        )
    )

    history.append({

        "time":t,
        "state":state,
        "action":action,
        "reward":reward,
        "next_state":next_state
    })

    state = next_state


print_episode(history)

stats = EpisodeStatistics(
    history
)

stats.summarize()