from unittest import TestCase, main

from project.soccer_player import SoccerPlayer


class SoccerPlayerTest(TestCase):

    def setUp(self):
        self.p = SoccerPlayer("test_name", 18, 10, "Barcelona")

    def test_init_to_default(self):
        self.assertEqual("test_name", self.p.name)
        self.assertEqual(18, self.p.age)
        self.assertEqual(10, self.p.goals)
        self.assertEqual("Barcelona", self.p.team)
        self.assertFalse(self.p.achievements)

    def test_init_instance(self):
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.age, int)
        self.assertIsInstance(self.p.goals, int)
        self.assertIsInstance(self.p.team, str)

    def test_name_raise_value_error_len_equal_5(self):
        with self.assertRaises(ValueError) as err:
            self.p.name = "test1"
        self.assertEqual("Name should be more than 5 symbols!", str(err.exception))

    def test_name_raise_value_error_len_less_then_5(self):
        with self.assertRaises(ValueError) as err:
            self.p.name = "test"
        self.assertEqual("Name should be more than 5 symbols!", str(err.exception))

    def test_age_rase_value_error_under_16_years(self):
        with self.assertRaises(ValueError) as err:
            self.p.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(err.exception))

    def test_goals_under_zero(self):
        self.p.goals = -1
        self.assertEqual(0, self.p.goals)

    def test_team(self):
        with self.assertRaises(ValueError) as err:
            self.p.team = "Barselona1"
        actual = "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!"
        self.assertEqual(actual, str(err.exception) )

    def test_change_team_raise_invalid_team_name(self):
        self.assertEqual("Invalid team name!", self.p.change_team("Barselona2"))

    def test_change_team_raise_successfully_changed(self):
        actual = self.p.change_team("PSG")
        self.assertEqual("PSG", self.p.team)
        self.assertEqual("Team successfully changed!", actual)

    def test_add_new_achievement(self):
        actual = self.p.add_new_achievement("achievement")
        self.assertEqual({"achievement": 1}, self.p.achievements)
        self.assertEqual("achievement has been successfully added to the achievements collection!", actual)

    def test_add_new_achievement_more_then_one(self):
        self.p.achievements = {"achievement1": 1, "achievement2": 2, "achievement3": 3}
        actual = self.p.add_new_achievement("achievement2")
        self.assertEqual({"achievement1": 1, "achievement2": 3, "achievement3": 3}, self.p.achievements)
        self.assertEqual("achievement2 has been successfully added to the achievements collection!", actual)

    def test_lt_for_goals_other_player_has_less_goals(self):
        p2 = SoccerPlayer("test_name1", 18, 15, "Barcelona")
        actual = self.p.__lt__(p2)
        self.assertEqual("test_name1 is a top goal scorer! S/he scored more than test_name.", actual)

    def test_lt_for_goals_other_player_has_more_goals(self):
        p2 = SoccerPlayer("test_name1", 18, 5, "Barcelona")
        actual = self.p.__lt__(p2)
        self.assertEqual("test_name is a better goal scorer than test_name1.", actual)


if __name__ == "__main__":
    main()

