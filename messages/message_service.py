

class MessageService:

    def __init__(self):
        self.message = ""

    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def clear_message(self):
        self.message = ""



