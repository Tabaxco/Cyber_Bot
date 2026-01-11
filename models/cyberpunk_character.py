class Cyberpunk_Character():
    def __init__(self, id_user, id_server, name, age, role, inte, will, cool, emp, tech, ref, luck, body, dex, move, apperance):
        self.id_user = id_user
        self.id_server = id_server

        #Characteristics
        self.name = name
        self.age = age
        self.role = role

        #Mentral group
        self.inte = inte
        self.will = will
        self.cool = cool
        self.emp = emp

        #Combat group
        self.tech = tech
        self.ref = ref

        #Fortune group
        self.luck = luck

        #Physical group
        self.body = body
        self.dex = dex
        self.move = move

        self.apperance = apperance