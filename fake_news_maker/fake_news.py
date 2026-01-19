import random


intros = [
    "BREAKING NEWS:",
    "SHOCKING REPORT:",
    "JUST IN:",
    "SCIENTISTS CONFIRM:",
    "VIRAL UPDATE:",
    "SOURCES SAY:",
    "UNBELIEVABLE:"
]


subjects_list = [
    "A local Chaiwala",
    "An angry Auntie",
    "A Bollywood Star",
    "NASA's top scientist",
    "A sleepy Panda",
    "The entire Indian Cricket Team",
    "A confused tourist",
    "An AI Robot",
    "A stray Cow"
]


actions_list = [
    "accidentally invents invisible samosas",
    "bans gravity for 24 hours",
    "finds a secret tunnel to Mars",
    "declares war on spicy food",
    "replaces all currency with Monopoly money",
    "starts a petition to paint the Taj Mahal pink",
    "gets stuck in a washing machine",
    "buys the internet for ₹500",
    "refuses to eat anything but toothpaste"
]


consequences_list = [
    "in the middle of a traffic jam.",
    "during a live TV debate.",
    "and now everyone is confused.",
    "causing panic on WhatsApp groups.",
    "inside a crowded Metro train.",
    "while trying to bargain for vegetables.",
    "and claims it was a 'social experiment'.",
    "after losing a bet."
]

print("The fake News Generator (Press Ctrl+C to stop) ")

while True:

    intro = random.choice(intros)
    subject = random.choice(subjects_list)
    action = random.choice(actions_list)
    consequence = random.choice(consequences_list)

    
    headline = f"{intro} {subject} {action} {consequence}"

    
    print("\n" + headline)
    print("-" * 50)

    
    
    input("Press Enter for more breaking news...")