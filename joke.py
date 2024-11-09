import random

# List of programming and Python jokes
jokes = [
    "Why do Python programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Java developers wear glasses? Because they don’t C#!",
    "Why was the developer unhappy at their job? They wanted arrays.",
    "Why did the Python developer break up with the JavaScript developer? Because they couldn't handle each other's syntax!",
    "Why do programmers hate nature? It has too many bugs.",
    "Why did the Python data scientist get thrown out of the bar? They kept trying to sample everything.",
    "How do functions break up? They stop calling each other.",
    "Why did the programmer quit their job? Because they didn’t get arrays.",
    "What’s a programmer’s favorite place to hang out? The Foo Bar!"
]

def random_joke():
    # Select a random joke from the list
    joke = random.choice(jokes)
    print("\nHere's a joke for you! 🤣")
    print(joke)

# Run the joke generator
random_joke()

