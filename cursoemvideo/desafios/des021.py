import pygame
import os

pygame.mixer.init()

caminho = os.path.dirname(__file__)

pygame.mixer.music.load(os.path.join(caminho, 'des021.mp3'))

pygame.mixer.music.play()

input('Pressione ENTER para encerrar...')