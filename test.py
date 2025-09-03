import random

# Word list (you can expand this)
WORDS = ['python', 'hangman', 'programming', 'developer', 'terminal', 'docker', 'security']

# Choose a random word
word = random.choice(WORDS)
word_letters = set(word)
guessed_letters = set()
tries = 6

print("🎮 Welcome to Hangman!")
print(f"You have {tries} lives. Let's begin!")

# Game loop
while tries > 0 and word_letters:
    # Show current progress
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print("\nWord:", ' '.join(display))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Lives left: {tries}")

    # Get user input
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        print("✅ Good guess!")
        word_letters.remove(guess)
    else:
        print("❌ Wrong guess.")
        tries -= 1

# End of game
if not word_letters:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 Game Over! The word was: {word}")
