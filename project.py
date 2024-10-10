import random
from googletrans import Translator
# Initialize the Google Translator
translator = Translator()
# Define existing dictionaries for Andhra-Telangana translations
a_t_dict = {
'యాస్తా': 'ఎలా',  # "How"
    'యాస్తకా': 'ఎంతవరకు',  # "Until how much"
    'సరే': 'సరే',  # "Okay"
    'నాన్న': 'తండ్రి',  # "Father"
    'నాన్నగారు': 'తండ్రిగారు',  # "Father (respectful)"
    'అమ్మ': 'తల్లి',  # "Mother"
    'అమ్మగారు': 'తల్లిగారు',  # "Mother (respectful)"
    'బాగున్న': 'మంచిగా ఉంది',  # "Doing well"
    'చెప్పు': 'చెప్పు',  # "Tell me"
    'వచ్చావా?': 'వచ్చావా?',  # "Did you come?"
    'వచ్చారు?': 'వచ్చారు?',  # "Did they come? (respectful)"
    'ధన్యవాదాలు': 'ధన్యవాదాలు',  # "Thank you"
    'పట్టణం': 'నగరం',  # "City"
    'గుండు': 'గుంట',  # "Pit"
    'గుడ్డు': 'గుడి',  # "Temple"
    'చీకటి': 'చీకటి',  # "Dark"
    'వర్షం': 'ముత్యాలు',  # "Rain"
    'చెక్క': 'చెక్క',  # "Tree"
    'రొట్టె': 'రొట్టె',  # "Bread"
    'పాలకూర': 'కూర',  # "Vegetable"
    'పప్పు': 'పప్పు',  # "Lentils"
    'చాయ్': 'చాయ్',  # "Tea"
    'జీడిపప్పు': 'జీడిపప్పు',  # "Cashew nut"
    'ఉయ్యాల': 'తీపి',  # "Sweet"
    'కూర': 'కూర',  # "Curry"
    'జీలకర్ర': 'జీలకర్ర',  # "Cumin"
    'గారు': 'గారు',  # "Sir/Madam"
    'బబ్బాయి': 'బాబాయ్',  # "Boy"
    'చిన్నప్పటి': 'చిన్నప్పుడు',  # "Childhood"
    'వార్తలు': 'వార్తలు',  # "News"
    'సమయం': 'సమయం',  # "Time"
    'ఆనందం': 'ఆనందం',  # "Happiness"
    'పదవీ': 'పదవి',  # "Position"
    'ప్రపంచం': 'ప్రపంచం',  # "World"
    'నిన్న': 'నిన్న',  # "Yesterday"
    'ఈ రోజు': 'ఈ రోజు',  # "Today"
    'రేపు': 'రేపు',  # "Tomorrow"
    'సాయంత్రం': 'సాయంత్రం',  # "Evening"
    'రాత్రి': 'రాత్రి',  # "Night"
    'ఉదయం': 'ఉదయం',  # "Morning"
    'కళ': 'కళ',  # "Art"
    'నడక': 'నడక',  # "Walk"
    'ఉత్సాహం': 'ఉత్సాహం',  # "Enthusiasm"
    'సుఖం': 'సుఖం',  # "Comfort"
    'బలమైనది': 'బలమైనది',  # "Strong"
    'మహా': 'మహా',  # "Great"
    'బామ్మ': 'బామ్మ',  # "Grandmother"
    'తాత': 'తాత',  # "Grandfather"
    'అక్క': 'అక్క',  # "Elder sister"
    'చెల్లి': 'చెల్లి',  # "Younger sister"
    'కక్క': 'కక్క',  # "Younger brother"
    'తిను': 'తిను',  # "Eat"
    'బ్రతుకుడు': 'బ్రతుకుడు',  # "Live"
    'చూడు': 'చూడు',  # "See"
    'వాటా': 'వాటా',  # "Speak"
    'చేసు': 'చేయు',  # "Do"
    'జరా': 'జరా',  # "Few/Some"
    'మీద': 'మీద',  # "On/Above"
    'లోపట': 'లోపల',  # "Inside"
    'బేగ రండి': 'రండిరా',  # "Come quickly"
    'అక్కడ మీది కనపడిందా?': 'అక్కడ మీది ఆఉపడదా?',  # "Did you see that there?"
    'వేటకాలి': 'దేవలాదు',  # "Search"
    'దిండు': 'మేట',  # "Mattress"
    'వీలే దోవలో': 'తవ్వడం',  # "Dig"
    'గురువారం': 'బేస్తవారం',  # "Thursday"
    'సిక్': 'సుస్తయ్యాడు',  # "Sick"
    'హాస్పిటల్': 'దవఖానా',  # "Hospital"
    'బాబాయ్': 'కాకయ్య',  # "Uncle (paternal)"
    'ఎడరా వెళ్ళడం': 'ముండల వెళ్ళడం',  # "Go straight"
    'ఎడమకి కోయె': 'ఎడమకి తిరుగు',  # "Take a left"
    'బక్రీద్': 'యాట్ట',  # "Killing a goat"
    'సఖినాలు': 'సకేనాలు' #traditional sweet
}
t_a_dict = {v: k for k, v in a_t_dict.items()}

# Define a simple transliteration dictionary for guessing words
transliteration_dict = {
    'nanna': 'నాన్న',
    'amma': 'అమ్మ',
    'tandri': 'తండ్రి',
    'talli': 'తల్లి',
    'ela': 'ఎలా',
}


def translate_andhra_to_telangana(word):
    return a_t_dict.get(word, "Word not in dictionary")


def translate_telangana_to_andhra(word):
    return t_a_dict.get(word, "Word not in dictionary")


def transliterate_input(english_input):
    """ Convert English input to Telugu using transliteration dictionary """
    return transliteration_dict.get(english_input.lower(), english_input)


# Function to translate English to Telugu using Google Translator
def google_translate_english_to_telugu(text):
    try:
        translated = translator.translate(text, src='en', dest='te')
        return translated.text
    except Exception as e:
        return f"Translation Error: {e}"


def quizgame():
    points = 0
    rounds = 10  # Set the number of rounds for the quiz
    for i in range(rounds):
        user_input = input(
            "Meeku nachina language enter cheyandi Enter the language (andhra or telangana) you want to choose: ")
        if user_input.lower() == "andhra":
            print("Andhra to Telangana")
            word = random.choice(list(a_t_dict.keys()))
            print(f"Translate the Andhra word '{word}' to Telangana:")
            english_text = input("Enter the English text to translate into Telugu: ")
            translated_text = google_translate_english_to_telugu(english_text)
            print(f"Translated text: {translated_text}")
            u_guess = input("Enter your guess: ")
            # Transliterate the user's guess from English to Telugu if necessary
            u_guess_telugu = transliterate_input(u_guess)
            correct_answer = a_t_dict[word]
            if u_guess_telugu == correct_answer:
                print("Correct! +1 point")
                points += 1
            else:
                print(f"Wrong! The correct translation is: {correct_answer}")
        elif user_input.lower() == "telangana":
            print("Telangana to Andhra")
            word = random.choice(list(t_a_dict.keys()))
            print(f"Translate the Telangana word '{word}' to Andhra:")
            u_guess = input("Your guess: ")
            # Transliterate the user's guess from English to Telugu if necessary
            u_guess_telugu = transliterate_input(u_guess)
            correct_answer = t_a_dict[word]
            if u_guess_telugu == correct_answer:
                print("Correct! +1 point")
                points += 1
            else:
                print(f"Wrong! The correct translation is: {correct_answer}")
        else:
            print("Invalid input. Please choose either 'Andhra' or 'Telangana'.")

    print(f"\nGame over! Your final score is: {points}")
    if points > 7:
        print("Chala baga aadaaru! (You played really well!)")
    elif points == 5:
        print("Inka improve cheskovali! (You need to improve!)")
    elif points <= 3:
        print("Maroka sari try cheyandi! (Try again!)")
    else:
        print("Keep practicing!")


def main():
    print("Andariki Namashakaram inka aata modhalaedhama!")
    print("Welcome to the Andhra-Telangana Translation Quiz Game!")
    while True:
        print("\nMenu:")
        print("1. (Aata modaluledhama) Start the quiz game")
        print("2. (Translate English to Telugu) Use Google Translator")
        print("3. Exit")
        choice = input(" (Choice  nu enter cheyandi) Enter your choice (1/2/3): ")
        if choice == '1':
            quizgame()  # Start the quiz game
        elif choice == '2':
            english_text = input("Enter the English text to translate into Telugu: ")
            translated_text = google_translate_english_to_telugu(english_text)
            print(f"Translated text: {translated_text}")
        elif choice == '3':
            print("Game Samapatam")
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
# Start the program
if __name__ == "__main__":
    main()
