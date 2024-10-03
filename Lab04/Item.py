
# Name, description, rarity and ownership

class Item:
    def __init__ (self,name, description, rarity, ownership):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership= ownership

    def pick_up (self,owner):
        self._ownership=owner # When item is pickep up, ownership chages to character's name
        print( str(self.name),"is now owned by", str(self._ownership))
    
    def thrown_away (self):
        if self._ownership == "":
            print(True)
        else:
            self._ownership = "" # When thrown away, ownership is lost
            print(False)

    def use (self):
        print (self.name,"is used ")


class Weapon(Item):
    def __init__ (self, name, rarity,  damage, type, ownership=None, description=None, equipped=False):
        super().__init__(name, rarity, description, ownership)
        self.type=type
        
        self.equipped= equipped

        # Attach modifier based on rarity
        if rarity in ["common","uncommon", "epic"]:
            self._atachmodifier=1
        elif rarity == "legendary":
            self._atachmodifier=1.15    
        else:
            print('Choose a valid rarity category')
        self.damage= damage*self._atachmodifier

    def equip (self):
        self.equipped=True
        print (self.name,"is equiped by",self._ownership)

    def use (self):
        print (self.name,"is used, dealing",self.damage," damage")    
     
class Shield(Weapon):
    def __init__ (self, name,  defense, rarity="common", broken=False, ownership=None, description=None, equipped=False):
        super().__init__(name, rarity,description, ownership)
        #self.type=type
        
        self.equipped= equipped
        
        # Defense modifier if broken
        if broken == True:
            self._defensepower=0.5    
        else:
            self._defensepower=1    

        # Defense modifier based on rarity
        if rarity in ["common","uncommon", "epic"]:
            self._defensemodifier=1
        elif rarity == "legendary":
            self._defensemodifier=1.10    
        else:
            print('Choose a valid rarity category')

        # Total defense
        self.defense = self._defensepower*self._defensemodifier*defense

    def use (self):
        if self.equipped==True:
             print (self.name,"is used, blocking",self.defense," damage") 
        else:
            pass

    def throw_away (self):
        if self.equipped == False:
            pass
        else:
            self.equipped=False
            print(self.name," is throw away")

class Potion ():
    @staticmethod
    def from_ability(cls, name, owner, type, description=None, value=50,effective_time=30, was_used=""):
        # Description based on type
        cls.name=name
        cls.owner=owner
        cls.type=type

        if type == "attack":
            cls.description= "Potion will add", cls.value, "attack powers when used"
        elif type == "defense":
            cls.description= "Potion will add", cls.value, "defense powers when used"  
        elif type == "HP":
            cls.description= "Potion will restore", cls.value, "health when used" 
        else:
            print('Choose a valid type category')

