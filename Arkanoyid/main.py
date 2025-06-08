import pygame

pygame.init()


back = (200, 255, 255)  # колір фону (background)
mw = pygame.display.set_mode((500, 500))  # Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()


# змінні, що відповідають за координати платформи
racket_x = 200
racket_y = 330


# прапор закінчення гри
game_over = False


# клас із попереднього проекту
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.define_hitbox_color = back
        if color:
            self.define_hitbox_color = color

    def color(self, new_color):
        self.define_hitbox_color = new_color

    def define_hitbox(self):
        pygame.draw.rect(mw, self.define_hitbox_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


# створення м'яча та платформи
ball = Picture("./assets/ball.png", 160, 200, 50, 50)
platform = Picture("./assets/platform.png", racket_x, racket_y, 100, 30)


# Створення ворогів
start_x = 5  # координати створення першого монстра
start_y = 5
count = 9  # кількість монстрів у верхньому ряду
monsters = []  # список для зберігання об'єктів-монстрів
for j in range(3):  # цикл по стовпцях
    y = start_y + (
        55 * j
    )  # координата монстра у кожному слід. стовпці буде зміщена на 55 пікселів по y
    x = start_x + (27.5 * j)  # і 27.5 по x
    for i in range(
        count
    ):  # цикл по рядах(рядків) створює в рядку кількість монстрів,що дорівнює count
        d = Picture("./assets/enemy.png", x, y, 50, 50)  # створюємо монстра
        monsters.append(d)  # додаємо до списку
        x = x + 55  # збільшуємо координату наступного монстра
    count = count - 1  # для наступного ряду зменшуємо кількість монстрів


while not game_over:
    ball.define_hitbox()
    platform.define_hitbox()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # малюємо всіх монстрів зі списку
    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()

    clock.tick