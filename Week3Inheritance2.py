#**Questions left to answer: 2, 5**

#Question1: parent class
class Spell:
  def __init__(self, incantation, name):
    self.name = name
    self.incantation = incantation

  def __str__(self):
    return self.name + ' ' + self.incantation + '\n' + self.get_description()

  def get_description(self):
    return 'No description'

  def execute(self):
    print (self.incantation)

#Question 1: child class 1
class Accio(Spell):
  def __init__(self):
    Spell.__init__(self, 'Accio', 'Summoning Charm')

#Question 1: child class 2
class Confundo(Spell):
  def __init__(self):
    Spell.__init__(self, 'Confundo', 'Confundus Charm')

  def get_description(self):
    return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):
  print (spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

#Question 3 output:
#Accio Summoning Charm Accio
#No description
#Confundus Charm Causes the victim to become confused and befuddled. Confundo

#Question 4: The get_description method in the Confundo class is called on because it overrides the original get_description method in Spell class

#Question 5: 