from unittest import TestCase, main
from ScrapeApp.utils import (
    get_groups_list, sort_groups, output_top_groups, write_file
)


class ScrapeTest(TestCase):
    def test_get_groups_list(self):
        self.assertEqual(get_groups_list(1), [])

    def test_sort_groups(self):
        self.assertEqual(sort_groups([]), [])

    def test_output_top_groups(self):
        self.assertEqual(output_top_groups([], 23), [])

    def test_write_file(self):
        self.assertEqual(write_file([], 23), None)


if __name__ == '__main__':
    main()
