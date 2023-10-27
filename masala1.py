class String:
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        if isinstance(other, String):
            return self.text == other.text
        return False


s1 = String(text="ok")
s2 = String(text="tk")

print(s1 == s2) 