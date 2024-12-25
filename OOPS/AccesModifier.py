class MyClass:
    def __init__(self):
        self.public_variable = 10
        self._private_variable = 20
        self.__hidden_variable =  30

    def print_All(self):
        # without underscore
        print(self.public_variable) # part of the public API

        # with undrscore 
        print(self._private_variable) # can still be accessed but not part of public API
        print(self.__hidden_variable) # cant access outside of class but if you really want to access it then you have to use the name as :-  _MyClass__hidden_variable_method()

    def _private_method(self):
        print("hellow")

    def __hidden_variable_method(self):
        print('world')

    

mc = MyClass()

mc.print_All()
mc._private_method()
# mc.__hidden_variable_method()    gets error 
# AttributeError: 'MyClass' object has no attribute '__hidden_variable_method'.


# To access hidden variable do this
mc._MyClass__hidden_variable_method()

