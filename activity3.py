class parrot:
    species='bird'
    def __init__ (self,name,age):
        self.name=name
        self.age=age

cockateil=parrot('Bob',10)
kea=parrot('Tim',13)
grey_parrot=parrot('Sam',15)

print('Cockateil is a {}'.format(cockateil.species))
print('Kea is also a {}'.format(kea.species))
print('Grey parrot is also a {}'.format(grey_parrot.species))

print('')
print('{} is a {} years old'.format(cockateil.name,cockateil.age))
print('{} is a {} years old'.format(kea.name,kea.age))
print('{} is a {} years old'.format(grey_parrot.name,grey_parrot.age))