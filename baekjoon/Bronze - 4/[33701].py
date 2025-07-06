def name():
  while True:
    result = "n" + randomName() + "gwan"
    if {'k', 'u'}.issubset(result):
      return result

def randomName():
  import random
  import string

  return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(0, 45)))

print(name())
