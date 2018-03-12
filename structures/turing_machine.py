from collections import defaultdict, namedtuple

import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger(__name__)


B = 'B'
L = 'left'
R = 'right'
H = 'halt'


class TuringMachine(object):

    Instruction = namedtuple('Instruction', 'write, move, new_state')

    def __init__(self, tape=[], rules={}):
        super(TuringMachine, self).__init__()
        self.at_index = 0
        self.tape = tape or [B]
        self.rules = defaultdict(dict)
        self.rules.update(rules)
        self.state = 0

    def add_rule(self, state, read, write, move, new_state=None):
        assert move in [L, R, H]
        read_at_state = self.rules[state].get(read)

        if read_at_state:
            logging.info('Rule already exists for reading {} at state {}'.format(read, state))
            return
        else:
            if not new_state:
                new_state = state
            self.rules[state][read] = TuringMachine.Instruction(write=write, move=move, new_state=new_state)

    @staticmethod
    def _displacement_for_direction(move):
        assert move in [L, R]
        if move == L:
            return -1
        else:
            return 1

    def run(self):
        while True:
            current_symbol = self.tape[self.at_index]
            instruction = self.rules[self.state].get(current_symbol)

            if not instruction:
                logging.warning('No instruction for symbol {} at state {}. Quitting...'.format(
                    current_symbol, self.state)
                )
                exit(0)

            self.tape[self.at_index] = instruction.write
            if instruction.move == H:
                logging.debug('Reached halting state. Halting...')
                break

            logging.info('Writing {} and moving {}'.format(instruction.write, instruction.move))

            displacement = self._displacement_for_direction(instruction.move)
            if self.at_index == 0 and displacement == -1:
                self.tape.insert(0, B)
                # No need to move
            else:
                self.at_index += displacement
            self.state = instruction.new_state


class MultiplyingTuringMachine(TuringMachine):
    def __init__(self, a, b):
        a_list = [1] * a
        b_list = [1] * b
        tape = [B] + a_list + ['*'] + b_list + ['=']
        super(MultiplyingTuringMachine, self).__init__(tape=tape)

    def run(self):
        raise NotImplementedError('No rules to multiply numbers yet')

