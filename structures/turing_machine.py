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

            logging.debug('Writing {} and moving {}'.format(instruction.write, instruction.move))

            displacement = self._displacement_for_direction(instruction.move)
            if self.at_index == 0 and displacement == -1:
                self.tape.insert(0, B)
                # No need to move
            else:
                self.at_index += displacement

            if self.at_index >= len(self.tape):
                self.tape.append(B)

            self.state = instruction.new_state

        print self.tape


class MultiplyingTuringMachine(TuringMachine):
    def __init__(self, a, b):
        a_list = ['1'] * a
        b_list = ['1'] * b
        tape = ['#'] + a_list + ['*'] + b_list + ['=']
        super(MultiplyingTuringMachine, self).__init__(tape=tape)
        self.state = 's0'

        self.add_rule(state='s0', read='#', write='#', move=R, new_state='s0')
        self.add_rule(state='s0', read='1', write='b', move=R, new_state='s1')
        self.add_rule(state='s1', read='1', write='1', move=R, new_state='s1')
        self.add_rule(state='s1', read='*', write='*', move=R, new_state='s2')
        self.add_rule(state='s2', read='1', write='t', move=R, new_state='s3')
        self.add_rule(state='s3', read='1', write='1', move=R, new_state='s3')
        self.add_rule(state='s3', read='=', write='=', move=R, new_state='s4')
        self.add_rule(state='s4', read='1', write='1', move=R, new_state='s4')
        self.add_rule(state='s4', read=B, write='1', move=L, new_state='s5')
        self.add_rule(state='s5', read='1', write='1', move=L, new_state='s5')
        self.add_rule(state='s5', read='=', write='=', move=L, new_state='s6')
        self.add_rule(state='s6', read='1', write='1', move=L, new_state='s7')
        self.add_rule(state='s6', read='t', write='1', move=L, new_state='s6')
        self.add_rule(state='s6', read='*', write='*', move=L, new_state='s8')
        self.add_rule(state='s7', read='1', write='1', move=L, new_state='s7')
        self.add_rule(state='s7', read='t', write='t', move=R, new_state='s2')
        self.add_rule(state='s8', read='b', write='b', move=H, new_state='s8')
        self.add_rule(state='s8', read='1', write='1', move=L, new_state='s9')
        self.add_rule(state='s9', read='b', write='b', move=R, new_state='s0')
        self.add_rule(state='s9', read='1', write='1', move=L, new_state='s9')
