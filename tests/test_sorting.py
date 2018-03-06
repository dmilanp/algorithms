import logging
import random
import sys

import pytest

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger(__name__)

from core import sorting

TEST_COUNT = 5

test_cases = [
    random.sample(range(100), random.randint(10, 30))
    for x in xrange(TEST_COUNT)
]

@pytest.mark.parametrize(
    'sorter',
    [
        (sorting.BubbleSort),
        (sorting.QuickSort),
        (sorting.InsertionSort),
        (sorting.MergeSort),
    ]
)
def test_simple(sorter):
    logging.info('Using {}'.format(sorter.__name__))

    for test_case in test_cases:
        logging.info('Testing {}'.format(test_case))
        assert sorter().sort(test_case) == sorted(test_case)


