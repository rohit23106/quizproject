import pygame
import random
import time
# Initialize Pygame
pygame.init()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Telugu Translation Quiz")
# Define a list of questions with English words and their corresponding Telugu translations
questions = [
    {"question_en": "Apple", "answer_te": "ఆపిల్", "options": ["ఆపిల్", "కామెటి", "పేరుగు", "కీరా"]},
    {"question_en": "Book", "answer_te": "పుస్తకం", "options": ["పుస్తకం", "వ్రాస్తే", "వసంతం", "మొరపులి"]},
    {"question_en": "House", "answer_te": "ఇల్లు", "options": ["ఇల్లు", "కిలుక", "పరువు", "ఉల్లిపాయ"]},
    {"question_en": "Water", "answer_te": "నీరు", "options": ["నీరు", "పాలు", "కూర", "అరటి"]},
    {"question_en": "Friend", "answer_te": "మిత్రుడు", "options": ["మిత్రుడు", "కోతి", "కదలిపెట్టాడు", "అతని"]},
    {"question_en": "Dog", "answer_te": "కుక్క", "options": ["కుక్క", "మృగం", "పూస", "ఎలుక"]},
    {"question_en": "Chair", "answer_te": "కుర్చీ", "options": ["కుర్చీ", "కిటికీ", "తలుపు", "బల్ల"]},
    {"question_en": "Sun", "answer_te": "సూర్యుడు", "options": ["సూర్యుడు", "చంద్రుడు", "తార", "మెగా"]},
    {"question_en": "Moon", "answer_te": "చంద్రుడు", "options": ["చంద్రుడు", "తార", "వెలుగు", "చీకటి"]},
    {"question_en": "Food", "answer_te": "ఆహారం", "options": ["ఆహారం", "పాని", "కూర", "నూనె"]},
    {"question_en": "Tree", "answer_te": "మర్రి", "options": ["మర్రి", "వృక్షం", "కాయ", "పూవు"]},
    {"question_en": "Flower", "answer_te": "పూవు", "options": ["పూవు", "కాయ", "కుసుమం", "పాప"]},
    {"question_en": "Fruit", "answer_te": "పండు", "options": ["పండు", "కాయ", "మొక్క", "పూలు"]},
    {"question_en": "Car", "answer_te": "కారు", "options": ["కారు", "బస్సు", "సైకిల్", "బండి"]},
    {"question_en": "School", "answer_te": "పాఠశాల", "options": ["పాఠశాల", "కళాశాల", "కంపని", "ఆస్పత్రి"]},
    {"question_en": "Doctor", "answer_te": "వైద్యుడు", "options": ["వైద్యుడు", "ఇంజనీరు", "ఉపాధ్యాయుడు", "విద్యార్థి"]},
    {"question_en": "Teacher", "answer_te": "ఉపాధ్యాయుడు",
     "options": ["ఉపాధ్యాయుడు", "వైద్యుడు", "విద్యార్థి", "కార్మికుడు"]},
    {"question_en": "River", "answer_te": "నది", "options": ["నది", "ఋతువు", "సముద్రం", "కన్నీరు"]},
    {"question_en": "Mountain", "answer_te": "పర్వతం", "options": ["పర్వతం", "గుట్ట", "కొండ", "వృక్షం"]},
    {"question_en": "Computer", "answer_te": "కంప్యూటర్", "options": ["కంప్యూటర్", "ఫోన్", "కలంపు", "పుస్తకం"]},
    {"question_en": "Train", "answer_te": "రైలు", "options": ["రైలు", "బస్సు", "విమానము", "గాడి"]},
    {"question_en": "Television", "answer_te": "దూరదర్శిని", "options": ["దూరదర్శిని", "ఫోన్", "సంవత్సరం", "పేపర్"]},
    {"question_en": "Fish", "answer_te": "చేప", "options": ["చేప", "పిల్లి", "కుక్క", "పందికొక్కు"]},
    {"question_en": "Bird", "answer_te": "పక్షి", "options": ["పక్షి", "మృగం", "చేప", "నక్క"]},
    {"question_en": "Clothes", "answer_te": "బట్టలు", "options": ["బట్టలు", "బంగారం", "అద్దకం", "పనస"]},
    {"question_en": "Mother", "answer_te": "తల్లి", "options": ["తల్లి", "అమ్మ", "అత్త", "అక్క"]},
    {"question_en": "Father", "answer_te": "తండ్రి", "options": ["తండ్రి", "నాన్న", "దాదా", "కన్నయ్య"]},
    {"question_en": "Brother", "answer_te": "అన్న", "options": ["అన్న", "చెల్లి", "తమ్ముడు", "బాబాయి"]},
    {"question_en": "Sister", "answer_te": "చెల్లి", "options": ["చెల్లి", "అక్క", "తల్లి", "మామ"]},
    {"question_en": "Grandmother", "answer_te": "నానమ్మ", "options": ["నానమ్మ", "తాతయ్య", "మామ", "ముత్తయ్య"]},
    {"question_en": "Grandfather", "answer_te": "తాతయ్య", "options": ["తాతయ్య", "నానమ్మ", "చినమ్మ", "పెద్దమ్మ"]},
    {"question_en": "Market", "answer_te": "సంత", "options": ["సంత", "చౌక", "ధర", "సమాజం"]},
    {"question_en": "Love", "answer_te": "ప్రేమ", "options": ["ప్రేమ", "కోపం", "పెద్దరికం", "కారుణ్యం"]},
    {"question_en": "Book", "answer_te": "పుస్తకం", "options": ["పుస్తకం", "లేఖ", "కన్నీరు", "కళాశాల"]},
    {"question_en": "Fish", "answer_te": "చేప", "options": ["చేప", "పాప", "పంది", "కుక్క"]},
    {"question_en": "Orange", "answer_te": "కమలాపండు", "options": ["కమలాపండు", "పండుపళ్ళు", "దీర్ఘం", "కీరపండు"]},
    {"question_en": "Telephone", "answer_te": "టెలిఫోన్", "options": ["టెలిఫోన్", "కంప్యూటర్", "తాళం", "రాజ"]},
    {"question_en": "Candle", "answer_te": "మొమ", "options": ["మొమ", "వెలుగు", "చీకటి", "దీపం"]},
    {"question_en": "Pencil", "answer_te": "పెన్సిల్", "options": ["పెన్సిల్", "కలంపు", "పుస్తకం", "తలుపు"]},
    {"question_en": "Table", "answer_te": "బల్ల", "options": ["బల్ల", "కుర్చీ", "తలుపు", "కిటికీ"]},
    {"question_en": "Elephant", "answer_te": "ఏనుగు", "options": ["ఏనుగు", "పులి", "సింహం", "పంది"]},
    {"question_en": "Lion", "answer_te": "సింహం", "options": ["సింహం", "పులి", "ఏనుగు", "జింక"]},
    {"question_en": "Tiger", "answer_te": "పులి", "options": ["పులి", "జింక", "సింహం", "ఎలుగు"]},
    {"question_en": "Cat", "answer_te": "పిల్లి", "options": ["పిల్లి", "కుక్క", "చిలుక", "పుంత"]},
]
# Function to select a random question
def get_random_question():
    return random.choice(questions)
# Function to display text on the screen
def display_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
# Function to handle the timer
def display_timer(start_time, limit=15):
    current_time = time.time()
    elapsed = current_time - start_time
    remaining = max(0, int(limit - elapsed))
    display_text(f"Time left: {remaining} seconds", 30, RED, 50, 150)
    return remaining == 0  # Return True if time is up
# Function to display the game over screen
def game_over(score):
    screen.fill(WHITE)
    display_text(f"Game Over! Your final score is: {score}", 50, BLUE, 50, 250)
    if score > 7:
        display_text("Chala baga aadaaru! (You played really well!)", 40, GREEN, 50, 300)
    elif score == 5:
        display_text("Inka improve cheskovali! (You need to improve!)", 40, RED, 50, 300)
    else:
        display_text("Maroka sari try cheyandi! (Try again!)", 40, RED, 50, 300)
    pygame.display.flip()
    pygame.time.wait(3000)
# Function to handle single or multiplayer game mode
def run_game(multiplayer=False):
    running = True
    player_scores = [0, 0]  # For Player 1 and Player 2
    player_turn = 0  # Track whose turn it is (Player 1: 0, Player 2: 1)
    question = get_random_question()
    start_time = time.time()  # Timer start
    while running:
        screen.fill(WHITE)
        display_text(f"Player {player_turn + 1}'s Turn", 40, BLUE, 50, 50)
        display_text("Guess the Telugu translation:", 40, BLACK, 50, 100)
        display_text(f"{question['question_en']}", 60, BLACK, 50, 200)
        # Shuffle options for multiple choice
        options = question["options"]
        random.shuffle(options)
        for i, option in enumerate(options):
            display_text(f"{i + 1}. {option}", 40, BLACK, 50, 300 + i * 50)
        display_text("Enter the number of your answer:", 40, BLACK, 50, 500)
        if display_timer(start_time):
            display_text("Time's up!", 40, RED, 50, 550)
            pygame.display.flip()
            pygame.time.wait(2000)
            question = get_random_question()  # Get a new question
            player_turn = 1 - player_turn  # Switch player turn
            start_time = time.time()  # Reset the timer
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    user_choice = int(event.unicode) - 1
                    if 0 <= user_choice < len(options):
                        if options[user_choice] == question["answer_te"]:
                            player_scores[player_turn] += 1
                            display_text("Correct! +1 Point", 40, GREEN, 50, 550)
                        else:
                            display_text(f"Wrong! The answer was: {question['answer_te']}", 40, RED, 50, 550)

                        pygame.display.flip()
                        pygame.time.wait(2000)  # Wait for 2 seconds before the next question
                        question = get_random_question()  # Get a new question
                        player_turn = 1 - player_turn  # Switch player turn
                        start_time = time.time()  # Reset the timer
        pygame.display.flip()

    # Display final scores and game over screen
    game_over(player_scores[0] if not multiplayer else max(player_scores))

    pygame.quit()

# Menu to select game mode
def menu():
    screen.fill(WHITE)
    display_text("Welcome to the Telugu Translation Quiz!", 50, BLACK, 50, 100)
    display_text("1. Single Player", 40, BLACK, 50, 200)
    display_text("2. Multiplayer", 40, BLACK, 50, 250)
    display_text("3. Exit", 40, BLACK, 50, 300)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    run_game(multiplayer=False)
                elif event.key == pygame.K_2:
                    run_game(multiplayer=True)
                elif event.key == pygame.K_3:
                    pygame.quit()
                    return
# Run the game menu
if __name__ == "__main__":
    menu()