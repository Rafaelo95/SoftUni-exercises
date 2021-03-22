class CountdownIterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            self.count -= 1
            return self.count + 1
        raise StopIteration


iterator = CountdownIterator(10)
for item in iterator:
    print(item, end=" ")
