import random, time

forever = 1

while forever == 1 
    
		ideas = ["Game", "Trail Art", "Shape Art", "Featured Project"]

    idea_chosen = ideas[random.randint(0, len(ideas) - 1)]
		
		print("Make a: " + idea_chosen)
		
		time.sleep(10)
