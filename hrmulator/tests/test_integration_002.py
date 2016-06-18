from unittest import TestCase

from hrmulator import Computer


program_text = """
START:
    move_from_inbox
    copy_to [0]
    move_to_outbox
    copy_from [0]
    jump_if_negative_to COUNT_UP
    jump_if_zero_to START
COUNT_DOWN:
    bump_down [0]
    jump_if_zero_to FINISH
    move_to_outbox
    jump_to COUNT_DOWN
COUNT_UP:
    bump_up [0]
    jump_if_zero_to FINISH
    move_to_outbox
    jump_to COUNT_UP
FINISH:
    move_to_outbox
    jump_to START
"""

class TestIntegration002(TestCase):
    def test_countdown(self):
        computer = Computer()
        computer.set_inbox([3, -3, 0])
        computer.load_program(program_text=program_text)
        computer.run()
        self.assertSequenceEqual(computer.outbox, [3, 2, 1, 0, -3, -2, -1, 0, 0])