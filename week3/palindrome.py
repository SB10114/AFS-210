class stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()
    def size(self):
        return len(self.data)
    def isEmpty(self):
        if len(self.data) == 0:
            return False
        else:
            return True   
    def peek (self):
        return self.data[-1]
    
    def __str__(self):
        return str(self.data)

class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data ):
        return self.data.insert(0, data)
  
    def dequeue(self):
        return self.data.pop()
        
    def size(self):
        return len(self.data)
    def isEmpty(self):
        if len(self.data) == 0:
            return False
        else:
            return True   
    def peek (self):
        return self.data[-1]

    def __str__(self):
        return str(self.data)

def isPalindrome (word):
    S = stack()
    Q = queue()

    for letter in word:
        S.push(letter)
        Q.enqueue(letter)
    
    print(S)
    print(Q)

    for char in range(0, S.size()):
        if S.data[char] != Q.data[char]:
            return False

    return True  
    
    
s = input('Enter a string for your value: ')
print(isPalindrome(s))