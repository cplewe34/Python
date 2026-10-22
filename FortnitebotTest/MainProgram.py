from FortniteBot import FortniteBot

bot1 = FortniteBot("George", 100) #this line creates an instance of the fortnite bot class and assigns it to the variable bot1
bot2 = FortniteBot("R2-D2", 80)
bot3 = FortniteBot("AM", 77)

bot1.take_damage(100) #calling the take damage method and passing in the amount of damage as an object 
bot2.take_damage(20) #

print(bot1.name) #holds the name of the bot
print(bot1.health) #holds the health of the bot

print(bot2.name)
print(bot2.health)

print(bot3.name)
print(bot3.health)

print("Before")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)

FortniteBot.max_health = 200

print("After")
print(bot1.max_health)
print(bot2.max_health)
print(bot2.max_health)

