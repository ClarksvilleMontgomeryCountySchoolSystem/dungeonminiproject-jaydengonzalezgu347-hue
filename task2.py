good=r"""
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
           jgs '--'
"""
bad=r"""
                                                              
        88                                                    
  ,d    88                                             ,d     
  88    88                                             88     
MM88MMM 88,dPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYYba, MM88MMM  
  88    88P'    "8a 88P'   "Y8 a8P_____88 ""     `Y8   88     
  88    88       88 88         8PP""""""" ,adPPPPP88   88     
  88,   88       88 88         "8b,   ,aa 88,    ,88   88,    
  "Y888 88       88 88          `"Ybbd8"' `"8bbdP"Y8   "Y888  
  """
has_key = True
if not has_key:
    outcome = "Doom: NOOOOO THE KEYYYYY"
    print(bad)
else:
    outcome = "Click: AREA HAS BEEN GRANTED"
    print(good)
print(outcome)