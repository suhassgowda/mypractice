import json


import unittest


class Testing(unittest.TestCase):

    def read_business_rules_from_DMH_API_Response(self):
        """
                Read the business rules from the DMH API response
        """
        with open('DMH_API_Response.json', errors="ignore") as f:
            data = json.load(f)
        object = json.dumps(data)
        json_object = json.loads(object)
        business_rules = json_object['process']['pipeline_params']['transformation_config']['age_bands']
        return business_rules


if __name__ == '__main__':
    unittest.main()
