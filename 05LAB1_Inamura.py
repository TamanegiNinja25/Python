import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():

    glBegin(GL_TRIANGLES)

    # Right face
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)

    # Left face
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)

    # Top face
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)

    # Bottom face
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)

    # Front face
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)

    # Back face
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)

    glEnd()

def draw_object():
    # Cube 1 - largest, dark green
    glPushMatrix()
    glScalef(1.0, 1.0, 1.0)
    glColor3f(0.0, 0.4, 0.0)
    draw_cube()
    glPopMatrix()

    # Cube 2 - medium-large, green
    glPushMatrix()
    glScalef(0.8, 0.8, 0.8)
    glColor3f(0.0, 0.55, 0.0)
    draw_cube()
    glPopMatrix()

    # Cube 3 - medium-small, light green
    glPushMatrix()
    glScalef(0.6, 0.6, 0.6)
    glColor3f(0.0, 0.75, 0.0)
    draw_cube()
    glPopMatrix()

    # Cube 4 - smallest, bright green
    glPushMatrix()
    glScalef(0.4, 0.4, 0.4)
    glColor3f(0.0, 1.0, 0.0)
    draw_cube()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("05 Lab 1")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    # Depth test is left off so the smaller cubes, drawn last,
    # stay visible on top of the larger ones (as in the sample output).

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
        glScalef(scale, scale, scale)
        draw_object()
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()

if __name__ == "__main__":
    main()
