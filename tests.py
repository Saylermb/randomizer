import unittest
from itertools import repeat

from randomizer import *
from datetime import datetime, timedelta


class Randomizer(unittest.TestCase):
    test_array = [1, [2], 3, 5, [[54]], 43, 'awda', False, b'123']
    rand = Randomize([1, 3, 1, 4, 5, 6, 7, 232, 43, 54, -1, -277])
    rand_text = Randomize('test test1 test2 test3')
    rand_texts = Randomize(['test', 'test1', 'test2', 'test3'])

    def _test_randomize_int(self):
        int_ = self.rand.element()
        group_int = self.rand.group_elements(100)
        ints_ = self.rand.elements(100)
        self.assertIsInstance(int_, int)
        self.assertIn(int_, self.rand)
        self.assertIsInstance(group_int, str)
        self.assertIsInstance(ints_, list)
        self.assertEqual(len(ints_), 100)

    def test_randomize_int(self):
        [self._test_randomize_int() for _ in range(100)]

    def _test_randomize_text(self):
        text_ = self.rand_text.element()
        group_text = self.rand_text.group_elements(100)
        texts_ = self.rand_text.elements(100)
        self.assertIsInstance(text_, str)
        self.assertIn(text_, self.rand_text)
        self.assertEqual(len(text_), 1)
        self.assertIsInstance(group_text, str)
        self.assertGreater(len(group_text), 100)
        self.assertIsInstance(texts_, list)
        self.assertEqual(len(texts_), 100)

    def test_randomize_text(self):
        [self._test_randomize_text() for _ in range(100)]

    def _test_randomize_texts(self):
        text_ = self.rand_texts.element()
        group_text = self.rand_texts.group_elements(100)
        texts_ = self.rand_texts.elements(100)
        self.assertIsInstance(text_, str)
        self.assertIn(text_, self.rand_texts)
        self.assertIsInstance(group_text, str)
        self.assertEqual(len(group_text.split(' ')), 100)
        self.assertIsInstance(texts_, list)
        self.assertEqual(len(texts_), 100)

    def test_randomize_texts(self):
        [self._test_randomize_texts() for _ in range(100)]

    def _test_random_text_unicode(self):
        text = random_text_unicode(100)
        self.assertTrue(isinstance(text, str))
        self.assertTrue(len(text) == 100)

    def test_random_text_unicode(self):
        [self._test_random_text_unicode() for _ in range(100)]

    def _test_random_text_unicode_r_size(self):
        len_array = list(map(lambda x: len(random_text_unicode(100, random_size=True)), range(10)))
        self.assertTrue(max(len_array) != min(len_array))
        self.assertTrue(0 <= len(random_text_unicode(10, True)) <= 10)

    def test_random_text_unicode_r_size(self):
        [self._test_random_text_unicode_r_size() for _ in range(100)]

    def _test_random_text(self):
        text = random_text(100)
        self.assertEqual(type(text), str)
        self.assertEqual(len(text), 100)

    def test_random_text(self):
        [self._test_random_text() for _ in range(100)]

    def _test_random_text_r_size(self):
        len_array = list(map(lambda x: len(random_text(100, random_size=True)), range(10)))
        self.assertTrue(max(len_array) != min(len_array))

    def test_random_text_r_size(self):
        [self._test_random_text_r_size() for _ in range(100)]

    def _test_random_float(self):
        self.assertTrue(isinstance(random_float(1, 2), float))
        self.assertTrue(isinstance(random_float(1.1, 2.2), float))
        self.assertTrue(isinstance(random_float(-1000, 1000), float))
        self.assertTrue(-1 < random_float(-1, 1) < 1)

    def test_random_float(self):
        [self._test_random_float() for _ in range(100)]

    def _test_random_datetime(self):
        start = datetime.now()
        end = start + timedelta(days=112, minutes=2, seconds=5)
        self.assertTrue(isinstance(random_datetime(start, end), datetime))
        self.assertTrue(start < random_datetime(start, end) < end)

    def test_random_datetime(self):
        [self._test_random_datetime() for _ in range(100)]

    def test_random_list_element(self):
        list(map(random_list_element, repeat(self.test_array, 100)))

    def test_random_bool(self):
        test = list(map(random_list_element, repeat(self.test_array, 100)))
        self.assertTrue(True in test)
        self.assertTrue(False in test)


class Partial(unittest.TestCase):

    def _test_random_unix_time(self):
        test = random_unix_time()
        self.assertIsInstance(test, float)
        self.assertLess(0, test)
        self.assertGreater(datetime.now().timestamp(), test)

    def test_random_unix_time(self):
        [self._test_random_unix_time() for _ in range(100)]

    def _test_random_dt_now(self):
        test = random_dt_now()
        self.assertIsInstance(test, datetime)
        self.assertLess(datetime(1980, 1, 1, 0, 0, 0, 0), test)
        self.assertGreater(datetime.now(), test)

    def test_random_dt_now(self):
        [self._test_random_dt_now() for _ in range(100)]

    def _test_random_positive_float(self):
        self.assertIsInstance(random_positive_float(10.1), float)
        test = random_positive_float(10.1)
        self.assertLess(0, test)
        self.assertGreater(10.1, test)

    def test_random_positive_float(self):
        [self._test_random_positive_float() for _ in range(100)]

    def _test_random_tinyint(self):
        test = random_tinyint()
        self.assertLessEqual(0, test)
        self.assertGreaterEqual(255, test)

    def test_random_tinyint(self):
        [self._test_random_tinyint() for _ in range(100)]

    def _test_random_smallint(self):
        test = random_smallint()
        self.assertLessEqual(-32768, test)
        self.assertGreaterEqual(32767, test)

    def test_random_smallint(self):
        [self._test_random_tinyint() for _ in range(100)]

    def _test_random_mediumint(self):
        test = random_mediumint()
        self.assertLessEqual(-8388608, test)
        self.assertGreaterEqual(8388607, test)

    def test_random_mediumint(self):
        [self._test_random_mediumint() for _ in range(100)]

    def _test_random_int(self):
        test = random_int()
        self.assertLessEqual(-2147483648, test)
        self.assertGreaterEqual(2147483647, test)

    def test_random_int(self):
        [self._test_random_int() for _ in range(1000)]

    def _test_random_bigint(self):
        test = random_bigint()
        self.assertLessEqual(-9223372036854775808, test)
        self.assertGreaterEqual(9223372036854775807, test)

    def test_random_bigint(self):
        [self._test_random_bigint() for _ in range(10000)]
