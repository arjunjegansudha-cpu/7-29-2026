class pet:
    def __init__ (self,name,age,species):
        self.name=name
        self.age=age
        self.species=species

labrador=pet('zues',3,'dog')
dobermen=pet('buck',7,'dog')
poodle=pet('toffe',6,'dog')
print('{} the {} is {} years old'.format(labrador.name,labrador.species,labrador.age))
print('{} the {} is {} years old'.format(dobermen.name,dobermen.species,dobermen.age))
print('{} the {} is {} years old'.format(poodle.name,poodle.species,poodle.age))