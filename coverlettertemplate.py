letter='''Dear <|NAME|>,
          Geeting from XYZ software house.We are very delighted to tell you about your selection.
          You are selected!!
          congratulations.
          have a great day ahead..
          regards,
          HR Manager
          Date:<|DATE|>'''
name=input("enter your name")
date=input("enter your date")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)
print(letter)
