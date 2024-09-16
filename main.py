import random

words = ["apple", "bloom", "crane", "dwell", "eagle", "frost", "glade", "haste", "ideal", "jolly", "kneel", "light", "mound", "noble", "ocean", "piano", "quilt", "rally", "scale", "trace", "ultra", "vivid", "whale", "xenon", "yacht", "zesty"]

def get_feedback(secret_word, guess_word):
    feedback = ""
    for i, c in enumerate(guess_word):
        if c == secret_word[i]:
            feedback += c.upper()
        elif c in secret_word:
            feedback += c.lower()
        else:
            feedback += "*"
    return feedback

secret_word = random.choice(words)

print("Welcome to Secret Words!")
print("Guess the 5-letter word. You have 6 attempts.")

for attempt in range(1, 7):
    guess = input(f"Attempt {attempt}/6: Enter your guess: ").lower()
    
    while len(guess) != 5 or not guess.isalpha():
        print("Invalid input. Please make sure you enter a 5-letter word.")
        guess = input(f"Attempt {attempt}/6: Enter your guess: ").lower()
    
    if guess == secret_word:
        print(f"Congratulations! You've guessed the word: {secret_word.upper()}")
        break
    else:
        feedback = get_feedback(secret_word, guess)
        print(f"Feedback: {feedback}")
        if attempt == 6:
            print(f"Sorry, you've run out of attempts. The word was: {secret_word.upper()}")