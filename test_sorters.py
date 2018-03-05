import logging
import sys

import pytest

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger(__name__)

import core

test_cases = [
    [86, 59, 64, 0, 36, 5, 67, 66, 42, 71, 76, 73, 50, 97, 78, 23, 45, 55, 20, 41],
]

@pytest.mark.parametrize('sorter',
    [
        (core.BubbleSort),
        (core.QuickSort)
    ]
)
def test_simple(sorter):
    logging.info('Using {}'.format(sorter.__name__))

    for test_case in test_cases:
        logging.info('Testing {}'.format(test_case))
        assert sorter().sort(test_case) == sorted(test_case)


