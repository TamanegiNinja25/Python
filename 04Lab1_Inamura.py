import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():

    glBegin(GL_TRIANGLES)
    
    glColor3f(1, 0, 0) #RED
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)

    glColor3f(0, 1, 0) #GREEN
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)

    glColor3f(0, 0, 1) #BLUE
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)

    glColor3f(1, 1, 0) #YELLOW
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)

    glColor3f(1, 0, 1) #MAGENTA
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)

    glColor3f(0, 1, 1) #CYAN
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)

    glEnd()
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("04Lab1_Inamura")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -7)
    glEnable(GL_DEPTH_TEST)
    glScalef(0.5, 0.5, 0.5)

    move_x = 0
    move_y = 0
    move_z = 0
    rotate_x = 0
    rotate_y = 0
    rotate_z = 0
    scale = 1.0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_x -= 1
                if event.key == pygame.K_d:
                    move_x += 1
                if event.key == pygame.K_w:
                    move_y += 1
                if event.key == pygame.K_s:
                    move_y -= 1
                if event.key == pygame.K_q:
                    move_z += 1
                if event.key == pygame.K_e:
                    move_z -= 1
                if event.key == pygame.K_x:
                    rotate_x += 10
                if event.key == pygame.K_y:
                    rotate_y += 10
                if event.key == pygame.K_z:
                    rotate_z += 10
                if event.key == pygame.K_UP:
                    scale += 0.1
                if event.key == pygame.K_DOWN:
                    scale -= 0.1
                if scale < 0.1:
                    scale = 0.1
                if event.key == pygame.K_r:
                    move_x = 0
                    move_y = 0
                    move_z = 0
                    rotate_x = 0
                    rotate_y = 0
                    rotate_z = 0
                    scale = 1.0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -7)
        glTranslatef(move_x, move_y, move_z)
        glRotatef(rotate_x, 1, 0, 0)
        glRotatef(rotate_y, 0, 1, 0)
        glRotatef(rotate_z, 0, 0, 1)
        glScalef(0.5 * scale, 0.5 * scale, 0.5 * scale)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()
if __name__ == "__main__":
    main()
