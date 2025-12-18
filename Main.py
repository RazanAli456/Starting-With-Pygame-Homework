import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding A Single Pic")
image=pygame.image.load("Neon_Razan.png")
image=pygame.transform.scale(image,(500,500))
done=False
while not done:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done=True
            pygame.quit()
        screen.blit(image,(0,0))      
        pygame.display.flip()