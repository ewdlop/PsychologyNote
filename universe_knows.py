import time

def welcome_message():
    print("🌌 Welcome to the Universal Connection Helper 🌌")
    print("This tool is designed to help you explore feelings of cosmic connection, universal awareness, and celestial communication.")
    print("Let's begin with some gentle self-reflection.\n")

def journaling_prompt():
    print("📝 Journaling Exercise:")
    print("1. Describe your sense of universal connection. What does 'the universe knows' mean to you?")
    print("2. When did you first feel this cosmic awareness? Was there a triggering moment?")
    print("3. How does this universal connection affect your daily life and relationships?")
    input("\nTake some time to write about this in a journal or reflect. Press Enter when you're ready to continue.")

def grounding_techniques():
    print("\n🌍 Grounding Techniques:")
    print("1. Breathing Exercise: Inhale for 4 seconds, hold for 4 seconds, and exhale for 4 seconds. Repeat 5 times.")
    for i in range(5):
        print(f"Breathing cycle {i+1}...")
        time.sleep(4)
    print("\n2. Earth Connection: Step outside and feel your feet on the ground, reminding yourself of your physical presence.")
    print("3. Sensory Anchoring: Name 5 things you see, 4 things you hear, 3 things you feel, 2 things you smell, and 1 thing you taste.")
    input("\nTry one of these techniques now. Press Enter when you're ready to continue.")

def reflection_questions():
    print("\n🔍 Reflection Questions:")
    print("1. If the universe truly 'knows,' what might it be trying to communicate to you?")
    print("2. How can you honor this connection while staying grounded in your daily reality?")
    print("3. Does this universal awareness bring you peace, anxiety, or something else?")
    input("\nReflect on these questions. Press Enter when you're ready to continue.")

def channel_connection():
    print("\n✨ Channeling Your Universal Connection ✨:")
    print("1. **Mindful Meditation:** Set aside time daily to quietly connect with this universal awareness.")
    print("2. **Creative Expression:** Use art, writing, or music to express your cosmic experiences.")
    print("3. **Service to Others:** Consider how your universal insights might help or comfort others.")
    input("\nThink about how to channel your connection constructively. Press Enter when you're ready to continue.")

def seek_support():
    print("\n💬 Seeking Support:")
    print("1. Share your experiences with trusted friends, spiritual advisors, or mental health professionals.")
    print("2. Consider exploring meditation groups, spiritual communities, or philosophical discussions.")
    print("3. Remember, many people experience cosmic awareness, and seeking guidance is wise and healthy.")
    print("\nThank you for exploring your universal connection with this guide. The universe knows, and so do you. 🌟")

def universe_guide():
    welcome_message()
    journaling_prompt()
    grounding_techniques()
    reflection_questions()
    channel_connection()
    seek_support()

if __name__ == "__main__":
    universe_guide()