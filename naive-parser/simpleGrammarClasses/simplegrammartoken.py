class SimpleGrammarToken:
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos

    def gettoken(self):
        return self.token

    def getpos(self):
        return self.pos
