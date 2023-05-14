class Teams:
    def __init__(self, members):
        self.__myTeam=members
        
    def __len__(self):
        return len(self.__myTeam)
    
    # part 1: add __contains__ protocol
    def __contains__(self, members):
        return members in self.__myTeam
    
    #part 2: add __iter__ protocol
    def __iter__(self):
        return iter(self.__myTeam)

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print('Tim' in classmates)
    print('Sam' in classmates)
    
    #part 2: iterable object reference
    iterator=iter(classmates)
    for member in iterator:
        print(member, end=" ")
    
main()

#Part 3: The class classmates does not implement the __len__ method, the Teams class does.

#Part 4: Interfaces specify what data structures do, implementation is how a data structures does what it does.

#Part 5: One way to design an interface structure so that all possible implementations could store data effectively would involve creating a method in a class for each type.  This creates an interface for each storage type along with a method that would allow it to work. 