import re

class Utilities:

    def __init__(self):
        pass

    def validate_user_input(self, user_input):
        # check to see if user provided a city
        match = re.search(r'\w+, \w+', user_input)
        if match:
            return True
        else:
            match = re.search(r'\d{5}', user_input)
            if match:
                return True
            else:
                return False