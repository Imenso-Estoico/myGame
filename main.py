import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode(size=(500,500))
print("Setup end")

print("Loop start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quiting...")
            pygame.quit()
            quit()
