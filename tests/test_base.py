import unittest
from src.base import BaseClass


class TestBaseClass(unittest.TestCase):

    def test_number_subjects_error(self):
        with self.assertRaises(ValueError):
            bclass = BaseClass(10)
        with self.assertRaises(ValueError):
            bclass = BaseClass(6)

    def test_get_weigheted_cp(self):
        bclass = BaseClass(7)
        raw_cp = [24, 30, 35, 42, 48, 47, 48]
        aggregate_cp = [42, 54, 73, 79, 81, 82, 84]
        weighted_cp = [24, 30.4256, 38.2099, 43.5431, 47.1351, 46.9285, 48]

        for rcp, acp, wcp in zip(raw_cp, aggregate_cp, weighted_cp):
            with self.subTest(raw=rcp, aggregate=acp):
                self.assertEqual(wcp, bclass.get_weighted_cp(rcp, acp))

    def test_get_raw_cp(self):
        bclass = BaseClass(7)
        letter_grades = {
            'a': 12,
            'a-': 11,
            'b+': 10,
            'b': 9,
            'b-': 8,
            'c+': 7,
            'c': 6,
            'c-': 5,
            'd+': 4,
            'd': 3,
            'd-': 2,
            'e': 1
        }
        for letter, points in letter_grades.items():
            with self.subTest(letter=letter):
                self.assertEqual(points, bclass.get_raw_cp(letter))

    def test_select_group2(self):
        bclass = BaseClass(7)
        selections = {
            '1': ['Biology'],
            '2': ['Chemistry'],
            '3': ['Physics'],
            '4': ['General Science'],
            '1, 2': ['Biology', 'Chemistry'],
            '1, 3': ['Biology', 'Physics'],
            '1, 4': ['Biology', 'General Science'],
            '2, 3': ['Chemistry', 'Physics'],
            '2, 4': ['Chemistry', 'General Science'],
            '3, 4': ['Physics', 'General Science'],
            '1, 2, 3': ['Biology', 'Chemistry', 'Physics'],
            '1, 2, 4': ['Biology', 'Chemistry', 'General Science'],
            '1, 3, 4': ['Biology', 'Physics', 'General Science'],
            '2, 3, 4': ['Chemistry', 'Physics', 'General Science']
        }
        for selection, subjects in selections.items():
            with self.subTest(selection=selection):
                self.assertEqual(subjects, bclass.select_group2(selection))

    def test_select_group3(self):
        bclass = BaseClass(7)
        selections = {
            '1': ['Christian Religious Education'],
            '2': ['Geography'],
            '3': ['Hindu Religious Education'],
            '4': ['History and Government'],
            '5': ['Islamic Religious Education'],
            '1, 2': ['Christian Religious Education', 'Geography'],
            '1, 3':
            ['Christian Religious Education', 'Hindu Religious Education'],
            '1, 4':
            ['Christian Religious Education', 'History and Government'],
            '1, 5':
            ['Christian Religious Education', 'Islamic Religious Education'],
            '2, 3': ['Geography', 'Hindu Religious Education'],
            '2, 4': ['Geography', 'History and Government'],
            '2, 5': ['Geography', 'Islamic Religious Education'],
            '3, 4': ['Hindu Religious Education', 'History and Government'],
            '3, 5': [
                'Hindu Religious Education', 'Islamic Religious Education'
            ],
            '4, 5': ['History and Government', 'Islamic Religious Education']
        }
        for selection, subjects in selections.items():
            with self.subTest(selection=selection):
                self.assertEqual(subjects, bclass.select_group3(selection))

    def test_select_group4(self):
        bclass = BaseClass(7)
        selections = {
            '1': ['Agriculture'],
            '2': ['Art and Design'],
            '3': ['Aviation Technology'],
            '4': ['Building Construction'],
            '5': ['Computer Studies'],
            '6': ['Drawing and Design'],
            '7': ['Electricity'],
            '8': ['Home Science'],
            '9': ['Metalwork'],
            '10': ['Power Mechanics'],
            '11': ['Woodwork']
        }
        for selection, subjects in selections.items():
            with self.subTest(selection=selection):
                self.assertEqual(subjects, bclass.select_group4(selection))

    def test_select_group5(self):
        bclass = BaseClass(7)
        selections = {
            '1': ['Arabic'],
            '2': ['Business Studies'],
            '3': ['French'],
            '4': ['German'],
            '5': ['Kenya Sign Language'],
            '6': ['Music']
        }
        for selection, subjects in selections.items():
            with self.subTest(selection=selection):
                self.assertEqual(subjects, bclass.select_group5(selection))
