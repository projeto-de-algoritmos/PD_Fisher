import pygame
import colors
import random
import sys


# auxiliary function for customizing text
def text_hollow(font, message, font_color):
    not_color = [c ^ 0xFF for c in font_color]
    base = font.render(message, 0, font_color, not_color)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(not_color)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, not_color)
    img.blit(base, (1, 1))
    img.set_colorkey(not_color)
    return img


# auxiliary function for customizing text
def text_outline(font, message, font_color, outline_color):
    base = font.render(message, 0, font_color)
    outline = text_hollow(font, message, outline_color)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img


def timer_text(screen, value):
    text_timer = text_outline(pygame.font.SysFont('default', 50), str(round(value, 1)), colors.WHITE, colors.BLACK)
    screen.blit(text_timer, (1295, 5))


def game_win_text(screen):
    win_text = text_outline(pygame.font.SysFont('default', 150), 'YOU WIN!', colors.WHITE, colors.BLACK)
    screen.blit(win_text, (430, 300))


def game_lose_text(screen):
    win_text = text_outline(pygame.font.SysFont('default', 150), 'YOU LOSE!', colors.WHITE, colors.BLACK)
    screen.blit(win_text, (410, 300))


def game_finish_text(screen):
    win_text = text_outline(pygame.font.SysFont('default', 150), 'CONGRATULATIONS!', colors.WHITE, colors.BLACK)
    screen.blit(win_text, (130, 300))


def pink_salmon(shoal):
    shoal.weight = random.randint(2, 4)
    shoal.value = random.randint(10, 13)
    shoal.fish_image = pygame.image.load('../src/images/fish/pink_salmon.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Pink salmon"


def pollock(shoal):
    shoal.weight = random.randint(4, 6)
    shoal.value = random.randint(7, 9)
    shoal.fish_image = pygame.image.load('../src/images/fish/pollock.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Pollock"


def gilt_head_bream(shoal):
    shoal.weight = random.randint(7, 10)
    shoal.value = random.randint(7, 10)
    shoal.fish_image = pygame.image.load('../src/images/fish/gilt_head_bream.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Gilt-head bream"


def rockfish(shoal):
    shoal.weight = random.randint(11, 13)
    shoal.value = random.randint(3, 5)
    shoal.fish_image = pygame.image.load('../src/images/fish/rockfish.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Rockfish"


def mackerel(shoal):
    shoal.weight = random.randint(3, 5)
    shoal.value = random.randint(4, 7)
    shoal.fish_image = pygame.image.load('../src/images/fish/mackerel.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Mackerel"


def sea_bass(shoal):
    shoal.weight = random.randint(6, 8)
    shoal.value = random.randint(8, 11)
    shoal.fish_image = pygame.image.load('../src/images/fish/sea_bass.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Sea bass"


def keta(shoal):
    shoal.weight = random.randint(1, 3)
    shoal.value = random.randint(2, 4)
    shoal.fish_image = pygame.image.load('../src/images/fish/keta.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Keta"


def codfish(shoal):
    shoal.weight = random.randint(5, 7)
    shoal.value = random.randint(4, 8)
    shoal.fish_image = pygame.image.load('../src/images/fish/codfish.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Codfish"


def barracuda(shoal):
    shoal.weight = random.randint(8, 10)
    shoal.value = random.randint(11, 13)
    shoal.fish_image = pygame.image.load('../src/images/fish/barracuda.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Barracuda"


def lemonema(shoal):
    shoal.weight = random.randint(3, 9)
    shoal.value = random.randint(5, 6)
    shoal.fish_image = pygame.image.load('../src/images/fish/lemonema.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Lemonema"


def tuna(shoal):
    shoal.weight = random.randint(4, 6)
    shoal.value = random.randint(7, 9)
    shoal.fish_image = pygame.image.load('../src/images/fish/tuna.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Tuna"


def halibut(shoal):
    shoal.weight = random.randint(9, 11)
    shoal.value = random.randint(5, 8)
    shoal.fish_image = pygame.image.load('../src/images/fish/halibut.png')
    shoal.fish_image = pygame.transform.scale(shoal.fish_image, (40, 30))
    shoal.name = "Halibut"


def quit_game():
    pygame.quit()
    sys.exit()


def text_objects(text, font):
    text_surface = font.render(text, True, colors.WHITE)
    return text_surface, text_surface.get_rect()


def button(screen, msg, x, y, w, h, ic, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, (ic[0], ic[1] - 20, ic[2] - 20), (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.SysFont("default", 30)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)
