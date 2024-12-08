import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Words:

    def __init__(self, font, words, pos):

        self.position = pos
        self.font = pg.font.SysFont(font, 13)
        self.font_render = self.font.render(words, 1, WHITE)

    def render(self, surf):
        surf.blit(self.font_render, self.position)


class WordScreen:

    def __init__(self, font, big_words, small_words, screen_size):

        self.screen_size = screen_size
        self.big_font = pg.font.SysFont(font, 20)
        self.small_font = pg.font.SysFont(font, 13)
        self.big_render = self.big_font.render(big_words, 1, WHITE)
        self.small_render = self.small_font.render(small_words, 1, WHITE)

    def render(self, surf):
        surf.blit(self.big_render, ((self.screen_size[0] - self.big_render.get_width()) // 2, (self.screen_size[1] - (self.big_render.get_height() + self.small_render.get_height())) // 2))
        surf.blit(self.small_render, ((self.screen_size[0] - self.small_render.get_width()) // 2, (self.screen_size[1] - (self.big_render.get_height() + self.small_render.get_height())) // 2 + self.big_render.get_height()))

