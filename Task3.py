class ReverseIterator:
    def __init__(self, data):
        self.data = data
        try:
            self.index = len(data) - 1
        except:
            raise TypeError("Потрібно передавати ітерабельний об'єкт")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            element = self.data[self.index]
            self.index -= 1
            return element
        else:
            raise StopIteration


rev = ReverseIterator([1, 2, 3, 4, 5])
iter_rev = iter(rev)

for element in iter_rev:
    print(element)

# rev = ReverseIterator(2) #Тест помилки
