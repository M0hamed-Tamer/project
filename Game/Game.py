import os
import time
import pygame
import random

def clear():
    """Clear The Terminal"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Froggy():
    pygame.init()

# تعريف الألوان
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # تعريف أبعاد النافذة
    WIDTH = 800
    HEIGHT = 800

    # إنشاء نافذة اللعبة
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Froggy Game")

    # تعريف حجم الضفدع والسيارات
    FROG_SIZE = 50
    CAR_WIDTH = 100
    CAR_HEIGHT = 60

    # تعريف سرعة اللعبة
    SPEED = 60

    class Frog:
        def __init__(self):
            self.x = WIDTH // 2
            self.y = HEIGHT - FROG_SIZE

        def move(self, dx, dy):
            self.x += dx
            self.y += dy
            # التأكد من بقاء الضفدع داخل حدود الشاشة
            self.x = max(0, min(self.x, WIDTH - FROG_SIZE))
            self.y = max(0, min(self.y, HEIGHT - FROG_SIZE))

        def draw(self):
            pygame.draw.rect(screen, GREEN, [self.x, self.y, FROG_SIZE, FROG_SIZE])

    class Car:
        def __init__(self, y):
            self.x = random.randint(0, WIDTH)
            self.y = y
            self.speed = random.randint(5, 10)

        def move(self):
            self.x += self.speed
            if self.x > WIDTH:
                self.x = -CAR_WIDTH

        def draw(self):
            pygame.draw.rect(screen, BLUE, [self.x, self.y, CAR_WIDTH, CAR_HEIGHT])

    def game_loop():
        frog = Frog()
        cars = [Car(100), Car(250), Car(400)]

        clock = pygame.time.Clock()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        frog.move(-FROG_SIZE, 0)
                    elif event.key == pygame.K_RIGHT:
                        frog.move(FROG_SIZE, 0)
                    elif event.key == pygame.K_UP:
                        frog.move(0, -FROG_SIZE)
                    elif event.key == pygame.K_DOWN:
                        frog.move(0, FROG_SIZE)

            screen.fill(BLACK)

            # تحريك ورسم السيارات
            for car in cars:
                car.move()
                car.draw()

                # التحقق من الاصطدام
                if (frog.x < car.x + CAR_WIDTH and
                    frog.x + FROG_SIZE > car.x and
                    frog.y < car.y + CAR_HEIGHT and
                    frog.y + FROG_SIZE > car.y):
                    game_over = True

            # رسم الضفدع
            frog.draw()

            # التحقق من الفوز
            if frog.y <= 0:
                font = pygame.font.SysFont(None, 74)
                text = font.render("You Win!", True, WHITE)
                screen.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 30))
                pygame.display.update()
                pygame.time.wait(2000)
                game_over = True

            pygame.display.update()
            clock.tick(SPEED)

        pygame.quit()

    game_loop()

def Twenty_one():

    CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    def deal_initial_cards():
        return random.choices(CARDS, k=2)

    def deal_card():
        return random.choice(CARDS)

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # Blackjack
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_scores(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
            return "\nYou went over. You lose 😤"
        if user_score == computer_score:
            return "\nDraw 🙃"
        elif computer_score == 0:
            return "\nLose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "\nWin with a Blackjack 😎"
        elif user_score > 21:
            return "\nYou went over. You lose 😭"
        elif computer_score > 21:
            return "\nOpponent went over. You win 😁"
        elif user_score > computer_score:
            return "\nYou win 😃"
        else:
            return "\nYou lose 😤"

    def play_game():
        clear()
        print("Starting Game........")
        user_cards = deal_initial_cards()
        computer_cards = deal_initial_cards()

        is_game_over = False
        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            time.sleep(3)

            print(f"\n\nYour cards are : ({", ".join(map(str, user_cards))}). current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                time.sleep(3)
                should_continue = input("\nGit anther card? Y/N : ").upper()
                if should_continue == 'Y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare_scores(user_score, computer_score))

        while input("Do you want to play a game of Blackjack? Y/N : ").upper() == 'Y':
            play_game()


    play_game()
    print("Thanks for playing!")


def Snake():
# تهيئة pygame
    pygame.init()

    # تعريف الألوان
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # تعريف أبعاد النافذة
    WIDTH = 800
    HEIGHT = 600

    # إنشاء نافذة اللعبة
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # تعريف حجم مربع الثعبان والتفاحة
    BLOCK_SIZE = 25

    # تعريف سرعة اللعبة
    SPEED = 18

    # دالة لرسم الثعبان
    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, WHITE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

    # دالة لعرض الرسائل
    def display_message(msg, color, size, y_displacement=0):
        font = pygame.font.SysFont("comicsansms", size)
        message = font.render(msg, True, color)
        rect = message.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_displacement))
        screen.blit(message, rect)

    # دالة لعرض شاشة البداية
    def game_intro():
        intro = True
        while intro:
            screen.fill(BLUE)
            display_message("Welcome to Snake Game", YELLOW, 50, -100)
            display_message("Press C to Play or Q to Quit", WHITE, 35)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

    # الدالة الرئيسية للعبة
    def game_loop():
        game_over = False
        game_close = False

        # تحديد موقع بداية الثعبان
        x1 = WIDTH / 2
        y1 = HEIGHT / 2

        # تحديد اتجاه حركة الثعبان
        x1_change = 0
        y1_change = 0

        # إنشاء الثعبان
        snake_list = []
        length_of_snake = 1

        # تحديد موقع التفاحة
        foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

        clock = pygame.time.Clock()

        while not game_over:
            while game_close:
                screen.fill(BLACK)
                display_message("You Lost! Press Q-Quit or C-Play Again", RED, 50)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -BLOCK_SIZE
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = BLOCK_SIZE
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -BLOCK_SIZE
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = BLOCK_SIZE
                        x1_change = 0

            # التحقق من اصطدام الثعبان بحدود اللعبة
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                game_close = True
            #
            x1 += x1_change
            y1 += y1_change
            screen.fill(BLACK)
            pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # التحقق من اصطدام الثعبان بنفسه
            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(snake_list)
            pygame.display.update()

            # التحقق من أكل التفاحة
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                length_of_snake += 1

            clock.tick(SPEED)

        pygame.quit()

    # عرض شاشة البداية أولاً
    game_intro()
    # بدء اللعبة
    game_loop()


def main_menu():
    while True:
        clear()
        time.sleep(2)
        print("""Choose a Game To Start......
        
        
1. Froggy
2. Twenty One
3. Snake""")
        choice = input("---------\n").strip().lower()
        if choice in ['1', 'froggy']:
            clear()
            Froggy()
        elif choice in ['2', 'twenty one']:
            clear()
            Twenty_one()
        elif choice in ['3', 'snake']:
            clear()
            Snake()
        else:
            print("Invalid input. Please enter a valid choice...")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()