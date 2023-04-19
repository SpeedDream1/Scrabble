import pygame

pygame.init()
pygame.display.set_caption("Menu")
# Interface
police_28 = pygame.font.Font(None,28)
police_32 = pygame.font.Font(None,32)
police_48 = pygame.font.Font(None,48)
police_38 = pygame.font.Font(None,38)

if  pygame.display.Info().current_h < 933 : # Taille barre des taches = 84
    screen_size = (1080, 751)
    format_ecran = 0
else :
    screen_size = (1080, 849)
    format_ecran = 1

screen = pygame.display.set_mode(screen_size)

if format_ecran == 0 :
    bouton_play_coordonnees = (290,70)
    bouton_play_width = 500
    bouton_play_heigth = 100
    bouton_play_color = (0,130,30)
    bouton_play_rect = pygame.Rect(bouton_play_coordonnees[0],bouton_play_coordonnees[1],bouton_play_width,bouton_play_heigth)
    bouton_play_text = police_48.render("Nouvelle Partie",True,(255,255,255))
    bouton_play_text_rect = bouton_play_text.get_rect(center=bouton_play_rect.center)

    bouton_continue_game_coordonnees = (290,240)
    bouton_continue_game_width = 500
    bouton_continue_game_heigth = 100
    bouton_continue_game_color = (0,80,20)
    bouton_continue_game_rect = pygame.Rect(bouton_continue_game_coordonnees[0],bouton_continue_game_coordonnees[1],bouton_continue_game_width,bouton_continue_game_heigth)
    bouton_continue_game_text = police_48.render("Reprendre une Partie",True,(255,255,255))
    bouton_continue_game_text_rect = bouton_continue_game_text.get_rect(center=bouton_continue_game_rect.center)

    bouton_option_coordonnees = (290,410)
    bouton_option_width = 500
    bouton_option_heigth = 100
    bouton_option_color = (80,80,80)
    bouton_option_rect = pygame.Rect(bouton_option_coordonnees[0],bouton_option_coordonnees[1],bouton_option_width,bouton_continue_game_heigth)
    bouton_option_text = police_48.render("Options",True,(255,255,255))
    bouton_option_text_rect = bouton_option_text.get_rect(center=bouton_option_rect.center)

    bouton_exit_coordonnees = (290,580)
    bouton_exit_width = 500
    bouton_exit_heigth = 100
    bouton_exit_color = (175,0,0)
    bouton_exit_rect = pygame.Rect(bouton_exit_coordonnees[0],bouton_exit_coordonnees[1],bouton_exit_width,bouton_exit_heigth)
    bouton_exit_text = police_48.render("Quitter",True,(255,255,255))
    bouton_exit_text_rect = bouton_exit_text.get_rect(center=bouton_exit_rect.center)

else :
    bouton_play_coordonnees = (290,90)
    bouton_play_width = 500
    bouton_play_heigth = 100
    bouton_play_color = (0,130,30)
    bouton_play_rect = pygame.Rect(bouton_play_coordonnees[0],bouton_play_coordonnees[1],bouton_play_width,bouton_play_heigth)
    bouton_play_text = police_48.render("Nouvelle Partie",True,(255,255,255))
    bouton_play_text_rect = bouton_play_text.get_rect(center=bouton_play_rect.center)

    bouton_continue_game_coordonnees = (290,280)
    bouton_continue_game_width = 500
    bouton_continue_game_heigth = 100
    bouton_continue_game_color = (0,80,20)
    bouton_continue_game_rect = pygame.Rect(bouton_continue_game_coordonnees[0],bouton_continue_game_coordonnees[1],bouton_continue_game_width,bouton_continue_game_heigth)
    bouton_continue_game_text = police_48.render("Reprendre une Partie",True,(255,255,255))
    bouton_continue_game_text_rect = bouton_continue_game_text.get_rect(center=bouton_continue_game_rect.center)

    bouton_option_coordonnees = (290,470)
    bouton_option_width = 500
    bouton_option_heigth = 100
    bouton_option_color = (80,80,80)
    bouton_option_rect = pygame.Rect(bouton_option_coordonnees[0],bouton_option_coordonnees[1],bouton_option_width,bouton_continue_game_heigth)
    bouton_option_text = police_48.render("Options",True,(255,255,255))
    bouton_option_text_rect = bouton_option_text.get_rect(center=bouton_option_rect.center)

    bouton_exit_coordonnees = (290,660)
    bouton_exit_width = 500
    bouton_exit_heigth = 100
    bouton_exit_color = (175,0,0)
    bouton_exit_rect = pygame.Rect(bouton_exit_coordonnees[0],bouton_exit_coordonnees[1],bouton_exit_width,bouton_exit_heigth)
    bouton_exit_text = police_48.render("Quitter",True,(255,255,255))
    bouton_exit_text_rect = bouton_exit_text.get_rect(center=bouton_exit_rect.center)

