

class Words:

    """
    TODO research an API to get words from and check
    guesses against.
    Also, implement a db to store used words in
    """

    @staticmethod
    def get_word():
        return "table"


    @staticmethod
    def is_valid(self, word):
        if len(word) != 5:
            return False
        else:
            return True
        #update to check against dictionary API
