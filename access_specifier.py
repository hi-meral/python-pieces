class Student:

    a = 20

    def __init__(self) -> None:
        pass

    def _protectedclass(self):
        print("protected")

    def __privateclass(self):
        print("private")

    def publicclass(self):
        self.__privateclass()


class Newboy(Student):
    def __init__(self) -> None:
        super().__init__()
        super()._protectedclass()
        # super().__privateclass()  ## error


s = Student()
n = Newboy()  # call protected

s._protectedclass()  # true
s.publicclass()  # true

n._protectedclass()

n.publicclass()
# s.__privateclass()  # error

print(s.a)
