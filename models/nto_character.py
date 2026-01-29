class NtoCharacter():
    def __init__(self, user_id, server_id, name, age, lvl, role, hitpoints, strength, dexterity, constitution, intelligence, wisdom, charisma, apperance):

        self.user_id = user_id
        self.server_id = server_id

        #characteristics
        self.name = name
        self.age = age
        self.lvl = lvl
        self.role = role

        #attributes
        self.hitpoints = hitpoints
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        
        #extra
        self.apperance = apperance

    def modifier_calc(self, attribute_value):
        return (attribute_value - 10) // 2

        