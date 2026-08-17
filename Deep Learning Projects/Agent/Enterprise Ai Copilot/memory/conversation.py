class ConversationMemory:

    def __init__(self):
        self.history = []

    def add_message(self, message):
        self.history.append(message)

    def get_history(self):
        return list(self.history)

    def clear(self):
        self.history.clear()

    def size(self):
        return len(self.history)