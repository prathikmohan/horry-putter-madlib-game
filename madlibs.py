#string concatanation (how to put strings together)

#create string that says "subscribe to ____"

# youtuber = "prathik mohan" #some string variable

# print("subscribe to " + youtuber) #should have space after ending eg: "hello "
# print("subscribe to {}".format(youtuber)) #most frequently seen
# #third method is using fstring
# print(f"subscribe to {youtuber}") #cleanest way to express concatanation



#starting project - creating basic skeleton code

# blank_adj = input("Adjective: ")
# blank_verb = input("Verb1: ")
# blank_verb2 = input("Verb2: ")
# famous_person = input("Famous Name: ")

# madlib = f"computer programming is so {blank_adj}! It makes me so excited all \
# the time because I love to {blank_verb}. Stay hydrated {blank_verb2} like you are \
# {famous_person}!"

# print(madlib)


#actual Horry Putter Madlib Game

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
noun4 = input("Noun: ")
noun5 = input("Noun: ")
noun6 = input("Noun: ")
noun_plural = input("Noun plural: ")
body_part = input("Body part (plural): ")
body_part2 = input("Body part: ")
verb = input("Verb: ")
verb_past = input("Verb (past tense): ")
verb_past2 = input("Verb (past tense): ")
spell1 = input("Spell: ")
spell2 = input("Spell: ")

madlib = f"A {adj1} glow burst suddenly across the enchanted sky above them as an edge of \
dazzling sun appeared over the sill of the nearest {noun1}. The light hit both of their {body_part} \
at the same time, so that Veldemort’s was suddenly a flaming {noun2}. Horry heard the high voice \
shriek as he too {verb_past} his best hope to the heavens, pointing Draco’s {noun3}:\n\
\"{spell1}!\"\n\
\"{spell2}!\"\n\
The bang was like a cannon blast, and the {adj2} flames that erupted between them, \
at the dead center of the circle they had been treading, marked the point where the \
{noun_plural} collided. Horry saw Veldemort’s {adj3} jet meet his own spell, saw the Elder Wand \
fly high, dark against the sunrise, spinning across the enchanted ceiling like the \
head of Nagini, spinning through the air toward the master it would not {verb}, who had \
come to take full possession of it at last. And Horry, with the unerring skill of a Seeker, \
caught the {noun4} in his free hand as Veldemort fell backward, arms splayed, the slit pupils \
of the {adj4} {body_part2} rolling upward. Tom Riddle hit the floor with a mundane finality, his body \
feeble and shrunken, the white hands empty, the snakelike face vacant and unknowing. Veldemort \
was dead, {verb_past2} by his own rebounding {noun5}, and Horry stood with two wands in his hands, \
staring down at his enemy’s {noun6}."

print(madlib)