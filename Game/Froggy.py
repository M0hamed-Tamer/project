import pygame
import random

# تهيئة pygame
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