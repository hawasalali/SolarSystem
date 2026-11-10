import pygame
import math
import random

pygame.init()

# Window
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 20)

# Clock
FPS = 60
clock = pygame.time.Clock()

center_x = WIDTH // 2
center_y = HEIGHT // 2

# Planets
planets = [
    {"name": "Mercury", "radius": 80,  "size": 6,  "color": (180, 180, 180), "speed": 0.04},
    {"name": "Venus",   "radius": 120, "size": 8,  "color": (255, 180, 80),  "speed": 0.03},
    {"name": "Earth",   "radius": 170, "size": 9,  "color": (80, 140, 255),  "speed": 0.025},
    {"name": "Mars",    "radius": 220, "size": 8,  "color": (255, 80, 80),   "speed": 0.020},
    {"name": "Jupiter", "radius": 280, "size": 15, "color": (220, 190, 140), "speed": 0.015},
    {"name": "Saturn",  "radius": 350, "size": 13, "color": (230, 210, 140), "speed": 0.012},
    {"name": "Uranus",  "radius": 420, "size": 11, "color": (120, 255, 255), "speed": 0.009},
    {"name": "Neptune", "radius": 500, "size": 11, "color": (80, 100, 255),  "speed": 0.007},
]

# Stars
stars = [
    (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    for _ in range(250)
]

font = pygame.font.SysFont("Arial", 20)
title_font = pygame.font.SysFont("Arial", 50, bold=True)

def draw_glow(surface, x, y, radius, color):
    for i in range(3, 0, -1):
        glow_radius = radius + i * 8
        alpha = 40 // i

        glow_surface = pygame.Surface(
            (glow_radius * 2, glow_radius * 2),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow_surface,
            (*color, alpha),
            (glow_radius, glow_radius),
            glow_radius
        )

        surface.blit(
            glow_surface,
            (x - glow_radius, y - glow_radius)
        )

angle = 0
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)

    # Title
    title = title_font.render("SOLAR SYSTEM", True, (100, 220, 255))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

    # Orbit circles
    for planet in planets:
        pygame.draw.circle(
            screen,
            (50, 50, 80),
            (center_x, center_y),
            planet["radius"],
            1
        )

    # Sun
    draw_glow(screen, center_x, center_y, 25, YELLOW)
    pygame.draw.circle(screen, YELLOW, (center_x, center_y), 25)

    sun_text = font.render("SUN", True, WHITE)
    screen.blit(sun_text, (center_x - 15, center_y + 35))

    # Planets
    for planet in planets:
        x = center_x + math.cos(angle * planet["speed"]) * planet["radius"]
        y = center_y + math.sin(angle * planet["speed"]) * planet["radius"]

        draw_glow(screen, int(x), int(y), planet["size"], planet["color"])

        pygame.draw.circle(
            screen,
            planet["color"],
            (int(x), int(y)),
            planet["size"]
        )

        label = font.render(planet["name"], True, WHITE)
        screen.blit(label, (x + 10, y + 10))

    angle += 1

    pygame.display.flip()

pygame.quit()