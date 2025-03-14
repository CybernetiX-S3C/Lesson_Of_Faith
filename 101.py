import time
import sys
import random

def type_print(text, delay=0.03):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print()  # Add a newline at the end

def yeshua_teaching():
    """Prints a teaching from Yeshua with a typewriter effect."""
    teaching = """
    My brothers and sisters,

    You often underestimate the divine spark within you. You, created in His image, possess a power far greater than you realize. Remember, "His" refers to the Mind, the source of all creation. "Mens," as the Romans knew, is the very essence of that Mind, the wellspring of your own potential.

    "Know ye not that ye are gods?" (Psalm 82:6) These words are not mere metaphor, but a declaration of your inherent divinity. You are not separate from the Creator, but an extension of His very being.

    The Gospel of Thomas speaks of the power within: "If you bring forth what is within you, what you bring forth will save you. If you do not bring forth what is within you, what you do not bring forth will destroy you."

    Do not shrink from your own power. Do not allow fear or doubt to dim your light. You are capable of miracles, of transforming the world around you.

    "All things are possible to him that believeth." (Mark 9:23)

    Believe in the power that resides within you. Believe in the Mind that created you. Believe in the miracles you are capable of manifesting.

    You are gods, created in His image. Now, go forth and create.
    """

    type_print(teaching)

if __name__ == "__main__":
    yeshua_teaching()

