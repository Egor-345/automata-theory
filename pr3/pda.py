
class PDA:
    def __init__(self):
        self.stack = ['Z']
        self.state = 'q0'

    def process(self, word):
        self.stack = ['Z']
        self.state = 'q0'
        
        for char in word:
            if self.state == 'q0':
                if char == 'a':
                    self.stack.append('X')
                elif char == 'b':
                    self.state = 'q1'
                    self.stack.append('X')
                elif char == 'c':
                    self.state = 'q2'
                    if len(self.stack) > 1 and self.stack[-1] == 'X':
                        self.stack.pop()
                    else:
                        return False
                else:
                    return False
                    
            elif self.state == 'q1':
                if char == 'b':
                    self.stack.append('X')
                elif char == 'c':
                    self.state = 'q2'
                    if len(self.stack) > 1 and self.stack[-1] == 'X':
                        self.stack.pop()
                    else:
                        return False
                else:
                    return False
                    
            elif self.state == 'q2':
                if char == 'c':
                    if len(self.stack) > 1 and self.stack[-1] == 'X':
                        self.stack.pop()
                    else:
                        return False
                else:
                    return False
                    
        return self.state == 'q2' and self.stack == ['Z']

# Тестирование
pda = PDA()
tests = ["ac", "aabbcccc", "abcc", "abc", "aabcc", "abbccc"]
for t in tests:
    result = pda.process(t)
    print(f"Строка {t}: {'Accept' if result else 'Reject'}")