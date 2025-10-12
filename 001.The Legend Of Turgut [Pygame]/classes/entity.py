import pygame
from settings.settings import *
from functions.get_os_adapted_path import get_os_adapted_path
from settings.settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2(0, 0)
        self.hitbox = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)

    def move(self):
        """Déplacement du joueur avec gestion des collisions."""
        if self.direction.length() > 0:
            self.hitbox.x += self.direction.x * self.speed
            self.collision("horizontal")
            self.hitbox.y += self.direction.y * self.speed
            self.collision("vertical")
            self.rect.center = self.hitbox.center

    def collision(self, direction):
        """Vérification des collisions du joueur."""
        for sprite in self.obstacle_sprites:
            if hasattr(sprite, "hitbox") and sprite.hitbox.colliderect(self.hitbox):
                if direction == "horizontal":
                    if self.direction.x > 0:  # Vers la droite
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:  # Vers la gauche
                        self.hitbox.left = sprite.hitbox.right
                elif direction == "vertical":
                    if self.direction.y > 0:  # Vers le bas
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:  # Vers le haut
                        self.hitbox.top = sprite.hitbox.bottom
