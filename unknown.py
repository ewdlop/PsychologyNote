import time

def welcome_message():
    print("Welcome to the Psychospy Helper!")
    print("This program is designed to help you explore your feelings, understand your experiences, and find grounding techniques.")
    print("Let's begin with a short reflection.\n")

def journaling_prompt():
    print("Journaling Exercise:")
    print("1. Think about when these feelings started. Was there a specific event?")
    print("2. What do these experiences mean to you? Are they positive or negative?")
    print("3. How do they affect your daily life?\n")
    input("Take some time to write about this in a journal. Press Enter when you're ready to continue.")

def grounding_techniques():
    print("\nGrounding Techniques:")
    print("1. Breathing Exercise: Inhale for 4 seconds, hold for 4 seconds, and exhale for 4 seconds. Repeat 5 times.")
    for i in range(5):
        print(f"Breathing cycle {i+1}...")
        time.sleep(4)
    print("2. Sensory Awareness: Name 5 things you see, 4 things you hear, 3 things you feel, 2 things you smell, and 1 thing you taste.")
    print("3. Hold an ice cube or splash cold water on your face to reconnect with the present moment.")
    input("Try one of these techniques now. Press Enter when you're ready to continue.")

def reflection_questions():
    print("\nReflection Questions:")
    print("1. If you feel possessed, what does this feeling tell you? Is it trying to communicate something?")
    print("2. If you believe you have secret powers, how do you think these powers could help you or others?")
    print("3. Do these feelings occur during specific situations or when you're around certain people?")
    input("Take a moment to reflect on these questions. Press Enter when you're ready to continue.")

def seek_support():
    print("\nSeeking Support:")
    print("1. Consider reaching out to a trusted friend, therapist, or spiritual advisor to discuss your feelings.")
    print("2. Therapy options like trauma-informed care or mindfulness-based approaches can be very helpful.")
    print("3. Remember, you're not alone, and seeking help is a sign of strength.\n")
    print("Thank you for exploring your feelings with this program. You can return to this process anytime you need.\n")

def psychospy_helper():
    welcome_message()
    journaling_prompt()
    grounding_techniques()
    reflection_questions()
    seek_support()

if __name__ == "__main__":
    psychospy_helper()
