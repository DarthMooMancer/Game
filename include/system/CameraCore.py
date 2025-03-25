from include.System import Display as dp
import pygame
from pygame import Surface
from pygame.sprite import Sprite
from typing import List, Optional

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = dp.win  # Use your display surface
        self.offset = pygame.Vector2(0, 0)

        # Center point calculation
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

    def center_on(self, target: Sprite):
        """Center the camera on the target sprite."""
        if hasattr(target, "rect"):  # Ensure Pyright recognizes rect
            self.offset.x = target.rect.centerx - self.half_width
            self.offset.y = target.rect.centery - self.half_height

    def draw(
        self, 
        surface: Surface, 
        bgsurf: Optional[Surface] = None, 
        special_flags: int = 0
    ) -> List[pygame.Rect]:
        """Draw sprites with camera offset."""
        rects = []

        for sprite in self.sprites():
            # Explicitly cast to Sprite and use hasattr to ensure Pyright recognizes attributes
            if isinstance(sprite, Sprite) and hasattr(sprite, "rect") and hasattr(sprite, "image"):
                offset_rect = sprite.rect.topleft - self.offset
                surface.blit(sprite.image, offset_rect)
                rects.append(sprite.rect)

        return rects

