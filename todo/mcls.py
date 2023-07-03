# The custom dictionary
class MemberTable(dict):
    def __init__(self):
        super().__init__()
        self.member_names = []

    def __setitem__(self, key, value):
        # if the key is not already defined, add to the
        # list of keys.
        if key not in self and not key.startswith("__"):
            self.member_names.append(key)

        # Call superclass
        dict.__setitem__(self, key, value)


# The metaclass
class OrderedClass(type):

    # The prepare function
    @classmethod
    def __prepare__(metacls, name, bases):  # No keywords in this case
        return MemberTable()

    # The metaclass invocation
    def __new__(cls, name, bases, classdict):
        # Note that we replace the classdict with a regular
        # dict before passing it to the superclass, so that we
        # don't continue to record member names after the class
        # has been created.
        result = type.__new__(cls, name, bases, dict(classdict))
        result.member_names = classdict.member_names
        result.me = lambda self: self
        return result


class MyClass(metaclass=OrderedClass):
    # method1 goes in array element 0
    def method1(self):
        pass

    # method2 goes in array element 1
    def method2(self):
        pass


x = MyClass()
print(x)
