class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size 
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        # key modulus table_size
        # h = 0
        # for char in str(key):
        #     h += ord(char)
        # return h % self.size
        return key % self.size

    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self,key,data):
        # Insert your code here to store key and data 
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            hashvalue = self.rehash(key)
            if self.slots[hashvalue] == None:
                self.slots[hashvalue] = key
                self.data[hashvalue] = data
            else:
                print("unresolved collisions")

    def get(self,key):
        # Insert your code here to get data by key
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == key:
            return self.data[hashvalue]
        else: 
            hashvalue = self.rehash(key)
            if self.slots[hashvalue] == key:
                return self.data[hashvalue]
        return None 

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[59] = 'G'
H[70] = 'H'
H[12] = 'I'
# Store remaining input data

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H[52])
