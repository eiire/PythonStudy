from unittest import TestCase


class Test(TestCase):
    def test_solve_task(self):
        from CodeWars.kyu_5.direction_reduction import solve
        self.assertEqual(
            solve.dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST']
        )

        self.assertEqual(
            solve.dir_reduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']),
            ['NORTH', 'NORTH']
        )

        self.assertEqual(
            solve.dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]),
            ["NORTH", "WEST", "SOUTH", "EAST"]
        )
