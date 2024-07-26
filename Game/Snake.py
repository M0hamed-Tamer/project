import pygame
import random

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
