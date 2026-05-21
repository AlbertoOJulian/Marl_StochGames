from dataclasses import dataclass, field


@dataclass
class QueueConfig:
    """
    Configuration parameters for queue environment.
    """

    max_queue: int = 10

    arrival_values: list = field(
        default_factory=lambda: [0, 1, 2]
    )

    arrival_probs: list = field(
        default_factory=lambda: [
            0.2,
            0.5,
            0.3
        ]
    )

    service_options: dict = field(
        default_factory=lambda: {

            "NoAction": [0],

            "LowService": [0,1],

            "MediumService": [1,2],

            "HighService": [2,3]
        }
    )

    service_cost: dict = field(
        default_factory=lambda: {

            "NoAction":0,

            "LowService":0,

            "MediumService":2,

            "HighService":20
        }
    )