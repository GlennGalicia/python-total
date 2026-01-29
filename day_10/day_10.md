# 📘 Day 10

## Pygame Module

## Table of Contents

1. [What is Pygame](#what-is-pygame)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [Additional Resources](#additional-resources)

---

## What is Pygame?

Pygame is a Python library designed to create video games and multimedia applications. It provides functionality for graphics, sound, keyboard/mouse events, collisions, and more.

**Use cases:**

- 2D game development
- Interactive simulations
- Game prototypes
- Multimedia applications

## Installation

### With UV (recommended)

```bash
# Create project
uv init my-game
cd my-game

# Add pygame
uv add pygame

# Verify installation
uv run python -c "import pygame; print(pygame.version.ver)"
```

### Recommended Project Structure

```
my-game/
├── .venv/
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── sprites/
│   │   ├── player.py
│   │   └── enemy.py
│   └── assets/
│       ├── images/
│       └── sounds/
└── README.md
```

## Basic Concepts

### 1. Initialization and Window

```python
import pygame

# Initialize pygame
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Clock to control FPS
clock = pygame.time.Clock()
FPS = 60
```

### 2. Game Loop

```python
running = True

while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game logic
    # (movement, collisions, etc.)

    # 3. Draw
    screen.fill((0, 0, 0))  # Black background
    # Draw sprites, text, etc.

    # 4. Update screen
    pygame.display.flip()
    clock.tick(FPS)  # Maintain 60 FPS

pygame.quit()
```

### 3. Event Handling

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Space pressed")
        if event.key == pygame.K_ESCAPE:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        print(f"Click at ({x}, {y})")
```

### 4. Drawing Shapes

```python
# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Rectangle
pygame.draw.rect(screen, RED, (100, 100, 200, 150))

# Circle
pygame.draw.circle(screen, GREEN, (400, 300), 50)

# Line
pygame.draw.line(screen, BLUE, (0, 0), (800, 600), 5)
```

### 5. Loading and Displaying Images

```python
# Load image
image = pygame.image.load('assets/images/player.png')

# Scale image
image = pygame.transform.scale(image, (64, 64))

# Display image
screen.blit(image, (x, y))
```

### 6. Sprites and Classes

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Sprite image
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))

        # Rectangle for position and collisions
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Speed
        self.speed = 5

    def update(self):
        # Move with keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep within screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# Usage
player = Player(400, 300)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# In game loop
all_sprites.update()
all_sprites.draw(screen)
```

### 7. Collision Detection

```python
# Collision between two sprites
if pygame.sprite.collide_rect(sprite1, sprite2):
    print("Collision!")

# Collision with group
collisions = pygame.sprite.spritecollide(player, enemies, False)
if collisions:
    print("You hit an enemy")

# Remove sprites on collision
pygame.sprite.spritecollide(player, enemies, True)  # True = remove
```

### 8. Text on Screen

```python
# Create font
font = pygame.font.Font(None, 36)  # None = default font

# Render text
text = font.render("Score: 100", True, WHITE)

# Display text
screen.blit(text, (10, 10))
```

### 9. Sounds

```python
# Load sound
jump_sound = pygame.mixer.Sound('assets/sounds/jump.wav')

# Play sound
jump_sound.play()

# Background music
pygame.mixer.music.load('assets/sounds/music.mp3')
pygame.mixer.music.play(-1)  # -1 = infinite loop
```

## Additional Resources

### Official Documentation

- [Pygame Docs](https://www.pygame.org/docs/)
- [Pygame Tutorials](https://www.pygame.org/wiki/tutorials)

### Free Assets

- [OpenGameArt.org](https://opengameart.org/) - Graphics and sprites
- [Freesound.org](https://freesound.org/) - Sound effects
- [Incompetech](https://incompetech.com/music/) - Music

### Complementary Libraries

- `pygame-menu` - Professional menus
- `pytmx` - Load Tiled maps

### Performance Tips

- Use `convert()` or `convert_alpha()` on loaded images
- Group sprites with `pygame.sprite.Group()`
- Avoid expensive operations in game loop
- Use dirty sprites to update only what's necessary

[<< Day 9](../day_09/day_09.md) | [Day 11 >>](../day_11/day_11.md)