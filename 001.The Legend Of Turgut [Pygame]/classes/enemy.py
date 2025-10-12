import pygame
import random
from settings.settings import *
from classes.entity import Entity
from functions.get_os_adapted_path import get_os_adapted_path


class Enemy(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.sprite_type = "enemy"
        self.obstacle_sprites = obstacle_sprites  # Ajout des obstacles

        # Initialisation de l'image et de la position
        self.image = self.get_initial_image()
        self.rect = self.image.get_rect(topleft=pos)
        # Ajout d'une hitbox plus précise
        self.hitbox = self.rect.inflate(0, -10)

        # Paramètres de mouvement
        self.speed = 4
        self.direction = pygame.math.Vector2()
        self.random_move_timer = 0
        self.move_duration = 0
        self.current_direction = "idle"

        # États et animations
        self.status = "idle"
        self.import_graphics()
        self.frame_index = 0
        self.animation_speed = 0.15

    def get_initial_image(self):
        """Retourne l'image initiale de l'ennemi"""
        enemy_path = get_os_adapted_path("imagesOfEnnemies", "20.png")
        return pygame.image.load(enemy_path).convert_alpha()

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right
                    self.rect.centerx = self.hitbox.centerx

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom
                    self.rect.centery = self.hitbox.centery

    def import_graphics(self):
        """Charge toutes les animations de l'ennemi"""
        enemy_assets = {
            "up": [get_os_adapted_path("imagesOfEnnemies", "30.png"),
                   # ./imagesOfEnnemies/30.png
                   get_os_adapted_path("imagesOfEnnemies", "10.png")],
            # ./imagesOfEnnemies/10.png
            "down": [get_os_adapted_path("imagesOfEnnemies", "12.png"),
                     # ./imagesOfEnnemies/12.png
                     get_os_adapted_path("imagesOfEnnemies", "32.png")],
            # ./imagesOfEnnemies/32.png
            "left": [get_os_adapted_path("imagesOfEnnemies", "33.png"),
                     # ./imagesOfEnnemies/33.png
                     get_os_adapted_path("imagesOfEnnemies", "13.png")],
            # ./imagesOfEnnemies/13.png
            "right": [get_os_adapted_path("imagesOfEnnemies", "11.png"),
                      # ./imagesOfEnnemies/11.png
                      get_os_adapted_path("imagesOfEnnemies", "31.png")],
            # ./imagesOfEnnemies/31.png
            "idle": [get_os_adapted_path("imagesOfEnnemies", "02.png")]
            # ./imagesOfEnnemies/02.png
        }

        self.animations = {}
        for status, paths in enemy_assets.items():
            self.animations[status] = [pygame.image.load(
                path).convert_alpha() for path in paths]

    def get_random_direction(self):
        """Génère une direction aléatoire"""
        directions = {
            "up": pygame.math.Vector2(0, -1),
            "down": pygame.math.Vector2(0, 1),
            "left": pygame.math.Vector2(-1, 0),
            "right": pygame.math.Vector2(1, 0),
            "idle": pygame.math.Vector2(0, 0)
        }

        # Choisir une direction aléatoire
        direction_key = random.choice(list(directions.keys()))
        self.current_direction = direction_key
        return directions[direction_key]

    def get_status(self):
        """Détermine le statut de l'ennemi en fonction de sa direction"""
        if self.direction.x == 0 and self.direction.y == 0:
            self.status = "idle"
        else:
            self.status = self.current_direction

    def animate(self):
        """Gère l'animation de l'ennemi"""
        animation = self.animations.get(self.status, self.animations["idle"])

        # Incrémentation de l'index d'animation
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Mise à jour de l'image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Mouvement horizontal
        self.hitbox.x += self.direction.x * speed
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # Mouvement vertical
        self.hitbox.y += self.direction.y * speed
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def get_direction_toward_player(self, player):
        """Détermine la direction vers le joueur"""
        if player:
            direction = pygame.math.Vector2(
                player.rect.center) - pygame.math.Vector2(self.rect.center)
            if direction.magnitude() != 0:
                return direction.normalize()
        return pygame.math.Vector2()

    def update_random_movement(self, player=None):
        """Met à jour le mouvement de l'ennemi (mélange de mouvement aléatoire et direction vers le joueur)"""
        self.random_move_timer += 1

        # Définir un pourcentage de chance que l'ennemi suive le joueur
        follow_player_chance = 0.95  # 90% de chance

        if self.random_move_timer >= self.move_duration or self.check_obstacle_ahead():
            self.random_move_timer = 0
            self.move_duration = random.randint(5, 10)

            # Décider aléatoirement si l'ennemi suit le joueur ou se déplace aléatoirement
            if player and random.random() < follow_player_chance:
                self.direction = self.get_direction_toward_player(player)
                self.current_direction = "following"
            elif player:
                self.direction = self.get_direction_toward_player(player)
                self.current_direction = "following"
            else:
                self.direction = self.get_random_direction()

        self.get_status()

    def check_obstacle_ahead(self):
        """Vérifie s'il y a un obstacle dans la direction actuelle"""
        if self.direction.magnitude() == 0:
            return False

        # Crée un rectangle légèrement devant l'ennemi
        check_distance = 20  # Distance de vérification
        future_pos = self.hitbox.copy()
        future_pos.x += self.direction.x * check_distance
        future_pos.y += self.direction.y * check_distance

        for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(future_pos):
                return True
        return False

    def update(self, player=None):
        """Mise à jour de l'ennemi"""
        self.update_random_movement()
        self.move(self.speed)
        self.animate()
