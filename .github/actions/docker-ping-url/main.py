import os
import time

import requests


def ping_url(url, delay, max_trials):
    trials = 0

    while trials < max_trials:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return True

        time.sleep(delay)
        trials += 1

    return False


def run():
    url = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY", "5"))

    max_trials_value = os.getenv("INPUT_MAX-TRIALS")
    if max_trials_value is None:
        max_trials_value = os.getenv("INPUT_MAX_TRIALS", "10")
    max_trials = int(max_trials_value)

    result = ping_url(url=url, delay=delay, max_trials=max_trials)
    if result is False:
        raise Exception("Could not get a 200 response within the maximum number of trials")


if __name__ == "__main__":
    run()
