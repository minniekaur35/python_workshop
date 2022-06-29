class do_iterations:
    def __iter__(self):
        self.number = 2
        return self

    def __next__(self):
        if self.number <= 2000:
            x = self.number
            self.number = self.number * 2
            return x
        else:
            raise StopIteration

the_iter_class = do_iterations()
itered = iter(the_iter_class)

for num in itered:
    print(num)




