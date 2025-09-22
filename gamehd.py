import random
import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
score = 0
font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 72)
pygame.display.set_caption("Game Plane")

clock = pygame.time.Clock()

# Tải ảnh
player_image = pygame.image.load("ta.png")
enmy_image = pygame.image.load("dich.png").convert_alpha()
enmy_image = pygame.transform.scale(enmy_image, (50, 50))

# Tạo ảnh viên đạn
bullet_image = pygame.Surface((8, 20))
bullet_image.fill((255, 0, 0))  # Viên đạn màu đỏ

# Group chứa tất cả sprite
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()  # ✅ Sửa tên từ "Bullet" sang "bullets" để tránh xung đột

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.speed = 5
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.defeated = False

    def update(self):
        if self.defeated:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))

        now = pygame.time.get_ticks()
        # ✅ Bắn bằng phím SPACE
        if keys[pygame.K_SPACE] and now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)  # ✅ Thêm vào group bullets

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enmy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

    def update(self):
        if player.defeated:
            return

        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.reset()

        if pygame.sprite.collide_rect(self, player):
            player.defeated = True

    def reset(self):
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Tạo player và thêm vào nhóm sprite
player = Player()
all_sprites.add(player)

# Tạo enemies
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)




# --- Main game loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Kiểm tra va chạm giữa đạn và enemy
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit_enemy in hits:
        score += 10  # ✅ Tăng 10 điểm mỗi enemy bị tiêu diệt
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)


    # Vẽ màn hình
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    if player.defeated:
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()