import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
input()
pygame.event.wait