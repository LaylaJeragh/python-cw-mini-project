# write your code here
def padel_court_cost(court_type):
   
  if court_type == "indoor" :
     return(30)
  elif court_type == "outdoor" :
     return(20)
  else:
     print("Try again please")



def racket_cost (racket_brand):
  
  if racket_brand== "Bullpadel" :
     return(100)
  elif racket_brand == "Nox" :
     return(140)
  elif racket_brand == "Siux" :
     return(200)
  else:
     print("Try again please")



def padel_ball_cost(ball_boxes):
   if ball_boxes == "box" :
     return(2)
   elif ball_boxes == "two boxes":
      return(3.5)
   elif ball_boxes == "three boxes":
      return (5)
   else:
      print ("Try again please")
      


def padel_game_cost():
  court_type =  input("What type of court do you want (indoor,outdoor)? ")
  racket_brand = input("What type of racket do you want (Nox,Bullpoint,Suix)? ")
  ball_boxes = input("What type of court do you want (box, two boxes, three boxes)? ")
  result = (padel_ball_cost(ball_boxes)+ padel_court_cost(court_type) + racket_cost(racket_brand))
  return result

print (padel_game_cost())


