from dataclasses import dataclass


@dataclass
class PolicyConfig:
    """
    Parameters controlling
    fixed threshold policy.
    """

    low_threshold: int = 4

    high_threshold: int = 7