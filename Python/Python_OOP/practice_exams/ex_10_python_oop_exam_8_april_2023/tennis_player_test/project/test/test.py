from unittest import TestCase, main

from project.tennis_player import TennisPlayer

class TennisPlayerTest(TestCase):

    def setUp(self):
        self.player = TennisPlayer("name_test", 20, 200.20)

    def test_init_to_default(self):
        self.assertEqual("name_test",self.player.name)
        self.assertEqual(20,self.player.age)
        self.assertEqual(200.20,self.player.points)
        self.assertFalse(self.player.wins)

    def test_init_types(self):
        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.age, int)
        self.assertIsInstance(self.player.points, float)
        self.assertIsInstance(self.player.wins, list)

    def test_name_raise_value_error_less_two_simbols(self):
        with self.assertRaises(ValueError) as err:
            self.player.name = "t"
        self.assertEqual("Name should be more than 2 symbols!", str(err.exception))

    def test_name_raise_value_error_equal_two_simbols(self):
        with self.assertRaises(ValueError) as err:
            self.player.name = "ts"
        self.assertEqual("Name should be more than 2 symbols!", str(err.exception))

    def test_age_raise_value_error_less_then_18(self):
        with self.assertRaises(ValueError) as err:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(err.exception))

    def test_add_new_win_tournament_has_been_in_list(self):
        self.player.wins = ["tournament_name_test1", "tournament_name_test2"]
        actual = self.player.add_new_win("tournament_name_test1")
        self.assertEqual("tournament_name_test1 has been already added to the list of wins!", actual)

    def test_add_new_win_tournament_has_not_in_list(self):
        self.player.wins = ["tournament_name_test1", "tournament_name_test2"]
        self.player.add_new_win("tournament_name_test3")
        expected = ["tournament_name_test1", "tournament_name_test2", "tournament_name_test3"]
        self.assertEqual(expected, self.player.wins)

    def test__it__other_player_is_better(self):
        player1 = TennisPlayer("name_test1", 30, 300.30)
        actual = player1 > self.player
        #actual = self.player.__lt__(player1)
        expected = "name_test1 is a top seeded player and he/she is better than name_test"
        self.assertEqual(expected, actual)

    def test__it__self_player_is_better(self):
        player1 = TennisPlayer("name_test1", 30, 100.30)
        actual = self.player < player1
        #actual = self.player.__lt__(player1)
        expected = "name_test is a better player than name_test1"
        self.assertEqual(expected, actual)

    def test_str(self):
        actual = str(self.player)
        expected = 'Tennis Player: name_test\nAge: 20\nPoints: 200.2\nTournaments won: '
        self.assertEqual(expected, actual)

    def test_str_with_list_elements(self):
        self.player.wins = ["tournament_name_test1", "tournament_name_test2", "tournament_name_test3"]
        actual = str(self.player)
        expected = ('Tennis Player: name_test\n''Age: 20\nPoints: 200.2\n'
    'Tournaments won: tournament_name_test1, tournament_name_test2, tournament_name_test3')
        self.assertEqual(expected, actual)





if __name__ == "__main__":
    main()