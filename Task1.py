class Iterable:
    def __init__(self, data):
        self.data = data
        try:
            self.current_iter = iter(self.data)
        except:
            raise TypeError("Потрібно передавати ітерабельний об'єкт")

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.current_iter)


my_object = Iterable([1, 2, "три", 4.0])

for item in my_object:
    print(item)

# my_object = Iterable(2)  #Тест помилки
#
# for item in my_object:
#     print(item)
