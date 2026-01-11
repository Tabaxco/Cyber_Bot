from random import randint

def rolling(input="1d20"):
        result = []
        operators = ["+", "-" , "x", "/"]
        optor = None
        bonus = None

        quantity, facesoperatorandmodifier = input.lower().split("d")
        quantity = int(quantity)

        for operator in operators:
               if operator in facesoperatorandmodifier:
                    optor = operator
                    faces, modifier = facesoperatorandmodifier.split(optor)
                    faces = int(faces)
                    modifier = int(modifier)
                    break

        if optor is None:
               faces = int(facesoperatorandmodifier)

        if faces < 1:
               raise ValueError("As faces devem ser maior ou igual a 1!")
 
        
        for q in range(quantity):
            result.append(randint(1, faces))
        
        sumresult = sum(result)

        if optor:
          if optor == "+":
               sumresult += modifier
          elif optor == "-":
               bonus = modifier
          elif optor == "x":
               sumresult *= modifier
          elif optor == "/":
               sumresult //= modifier
          else:
               bonus = ""
          bonus = f" {optor} {modifier}"
        
        message = f'` {sumresult} ` ⟵ {result} {quantity}d{faces}'
        message += bonus if bonus else ""

        return message