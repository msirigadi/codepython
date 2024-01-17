import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')

class RedField(BluePrint):
    def yellow(self):
        pass

gf = GreenField()
gf.hello()

#This will throw error as we have not defines the abstract class method in subclass.
#All abstract class abstract methods has to be difined in sub classes
rf = RedField()


