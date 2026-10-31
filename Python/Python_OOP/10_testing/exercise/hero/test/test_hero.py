from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):

    username = "test1"
    level = 10
    health = 100.00
    damage =10.00
    def setUp(self):
        self.h = Hero(self.username, self.level, self.health, self.damage)

    def test_class_attribute_types(self):
        self.assertEqual(Hero.__annotations__['username'], str)
        self.assertEqual(Hero.__annotations__['level'], int)
        self.assertEqual(Hero.__annotations__['health'], float)
        self.assertEqual(Hero.__annotations__['damage'], float)


    def test_init(self):
        self.assertEqual(self.username, self.h.username)
        self.assertEqual(self.level, self.h.level)
        self.assertEqual(self.health, self.h.health)
        self.assertEqual(self.damage, self.h.damage)

    def test_battle_equal_names(self):
        self.enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.h.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_player_health_equal_zero(self):
        self.enemy = Hero("test2", self.level, self.health, self.damage)
        self.h.health = 0
        with self.assertRaises(ValueError) as ver:
            self.h.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ver.exception))

        self.h.health = -1
        with self.assertRaises(ValueError) as ver:
            self.h.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ver.exception))

    def test_battle_enemy_health_equal_zero(self):
        self.enemy = Hero("test2", self.level, self.health, self.damage)
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ver:
            self.h.battle(self.enemy)
        self.assertEqual("You cannot fight test2. He needs to rest", str(ver.exception))

        self.enemy.health = -1
        with self.assertRaises(ValueError) as ver:
            self.h.battle(self.enemy)
        self.assertEqual("You cannot fight test2. He needs to rest", str(ver.exception))

    def test_battle_fight_with_enemy_both_health_drop_under_zero(self):
        self.enemy = Hero("test2", 10, 10, 10)
        self.h.health = 10.00
        self.assertEqual("Draw", self.h.battle(self.enemy))

    def test_battle_fight_with_enemy_both_health_equal_zero(self):
        self.enemy = Hero("test2", 10, 100, 10)
        self.assertEqual("Draw", self.h.battle(self.enemy))

    def test_battle_enemy_health_equal_to_zero(self):
        self.enemy = Hero("test2", 10, 100, 10)
        self.h.health = 1000.00
        self.assertEqual("You win", self.h.battle(self.enemy))
        self.assertEqual(11, self.h.level)
        self.assertEqual(905, self.h.health)
        self.assertEqual(15, self.h.damage)

    def test_battle_enemy_health_under_zero(self):
        self.enemy = Hero("test2", 10, 99, 10)
        self.h.health = 1000.00
        self.assertEqual("You win", self.h.battle(self.enemy))
        self.assertEqual(11, self.h.level)
        self.assertEqual(905, self.h.health)
        self.assertEqual(15, self.h.damage)
        self.assertEqual(-1, self.enemy.health)

    def test_battle_player_lose(self):
        self.enemy = Hero("test2", 5, 101, 5)
        self.h.health = 1000.00
        self.assertEqual("You lose", self.h.battle(self.enemy))
        self.assertEqual(10, self.h.level)
        self.assertEqual(975.00, self.h.health)
        self.assertEqual(10, self.h.damage)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(6, self.enemy.health)
        self.assertEqual(10, self.enemy.damage)

    def test_str(self):
        self.h.__str__
        self.assertEqual(f"Hero {self.username}: {self.level} lvl\n"
               f"Health: {self.health}\n"
               f"Damage: {self.damage}\n", self.h.__str__)

if __name__ == "__main__":
    main()