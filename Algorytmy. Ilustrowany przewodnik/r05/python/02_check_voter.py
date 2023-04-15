voted = {}
def check_voter(name):
  if voted.get(name):
    print "Pogoniæ go!"
  else:
    voted[name] = True
    print "Niech zag³osuje!"

check_voter("tomasz")
check_voter("micha³")
check_voter("micha³")
