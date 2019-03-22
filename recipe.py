import random    

ingredients = ['chocolate', 'salt', 'sugar', 'caramel', 'tea', 'lard', 'apples', 'refried beans', 'Taco Bell\'s Dorito\'s Locos Tacos™', 'mango', 'spaetzel', 'okunomiyaki', 'pickles', 'bread']
prep = ['saute', 'deep-fry', 'bake', 'boil', 'microwave', 'defrost', 'chop', 'slice', 'dice', 'mash', 'scorch', 'melt']

steps = random.randint(1, 10)

print("Step 1: take " + str(random.randint(2, 100)) + " lemons and " + random.choice(prep) + " them thoroughly.")
for i in range(1, steps):
    print("Step " + str(i) + ": " + random.choice(prep) + " " + str(random.randint(2, 100)) + " " + random.choice(ingredients))
print("Step " + str(steps + 1) + ": mix everything together with the lemons")

print("Step " + str(steps + 2) + ": serve and enjoy!")
