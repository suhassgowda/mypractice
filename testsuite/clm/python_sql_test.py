
from src.pages.python_sql import DbHelper
import unittest


class Testing(unittest.TestCase):

    def test(self):
        test = DbHelper(self)
        business_rules = test.read_business_rules_from_DMH_API_Response()
        test.values_fetched_One(business_rules)


if __name__ == '__main__':
    unittest.main()
