letter = ''' Dear <|NAME|>
you are selected!

Date: <|DATE|>'''
letter = letter.replace('<|NAME|>', input("Enter Name"))
letter = letter.replace("<|DATE|>", input('ENTER Date'))

print(letter)
