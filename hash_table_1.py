class HashTable:
    def __init__(self):
        self.MAX = 100
        self.holder = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        hsh = 0
        for characters in key:
            hsh += ord(characters)
        return hsh % self.MAX

    def __setitem__(self, key, value): # in order to use '[]' operator '__setitem__' inbuilt functions are overloaded here
        indexer = self.get_hash(key)
        self.holder[indexer] = value

    def __getitem__(self, key):
        return self.holder[self.get_hash(key)]

obj = HashTable()

obj['user_1'] = "Parth"
obj['user_2'] = "Jay"
obj['user_3'] = "Monax"
obj['user_4'] = "Kishan"
obj['user_5'] = "Army"
obj['user_6'] = "Tirth"

print(obj['user_6'])