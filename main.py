import random
import os


# List of words that can be used
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "house", "car", "dog", "cat", "tree", "flower", "sun", "moon", "star", "chicken", "beef", "pork", "fish", "bird", "fish", "snake", "lizard", "turtle", "spider", "crab", "lobster", "shrimp", "octopus"]

word = random.choice(words)

lives = 5

while True:
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  print(f"Lives: {lives}")
  print("")
  print(f"The word has {len(word)} letters.")
  print("")
  print("Type your guess")
  print("")

  answer = str(input())
  print("")

  if answer == word:
    print("Correct!")
    break
  else:
    lives -= 1
    if lives == 0:
      print("You lost!")
      break


