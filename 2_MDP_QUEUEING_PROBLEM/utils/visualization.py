def print_episode(
        history):
    """
    Print simulation history.
    """

    print("\nEpisode\n")

    for step in history:

        print(

            f"time={step['time']} | "

            f"queue={step['queue']} | "

            f"action={step['action']} | "

            f"arrivals={step['arrivals']} | "

            f"served={step['served']} | "

            f"next={step['next_queue']} | "

            f"reward={step['reward']}"

        )