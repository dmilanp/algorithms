from copy import copy
import logging
import random
import sys

from core.quicksort import quicksort


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger(__name__)

PER_TEST_ITERATIONS = 100


def test_quicksort(_list):
    l_sorted = sorted(copy(_list))
    try:
        l = quicksort(copy(_list))
    except Exception as e:
        logging.error("Error sorting {}".format(_list))
        raise e
    assert l == l_sorted


if __name__ == '__main__':

    # Tests to run
    tests = [test_quicksort]

    for test in tests:
        for _ in range(PER_TEST_ITERATIONS):
            list = random.sample(range(0, 100), 100)
            test(list)

