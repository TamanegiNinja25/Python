import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube(r, g, b):

    faces = [
        (1.0, [(1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)]),                (0.6, [(-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1)]),    # Left
        (0.9, [(1, 1, 1), (-1, 1, 1), (-1, 1, -1), (1, 1, -1)]),        
        (0.5, [(1, -1, 1), (-1, -1, 1), (-1, -1, -1), (1, -1, -1)]),    
        (0.8, [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)]),        
        (0.7, [(1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]),    
    ]

    glBegin(GL_TRIANGLES)
    for shade, (v1, v2, v3, v4) in faces:
        glColor3f(r * shade, g * shade, b * shade)
        glVertex3f(*v1)
        glVertex3f(*v2)
        glVertex3f(*v3)
        glVertex3f(*v1)
        glVertex3f(*v3)
        glVertex3f(*v4)
    glEnd()

def draw_object():

    cubes = [
        (-4, (1, 1, 0)),   
        (-2, (0, 1, 0)),   
        ( 0, (1, 0, 0)),   
        ( 2, (0, 0, 1)),   
        ( 4, (1, 0, 1)),   
    ]

    for x, color in cubes:
        glPushMatrix()
        glTranslatef(x, 0, 0)
        draw_cube(*color)
        glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("05 Lab 2")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    move_x = 0
    move_y = 0
    move_z = 0
    rotate_x = 20
    rotate_y = 30
    rotate_z = 0
    scale = 1.0
    auto_spin = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Translation
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
                # Rotation
                if event.key == pygame.K_x:
                    rotate_x += 10
                if event.key == pygame.K_y:
                    rotate_y += 10
                if event.key == pygame.K_z:
                    rotate_z += 10
                if event.key == pygame.K_SPACE:
                    auto_spin = not auto_spin
                # Scaling
                if event.key == pygame.K_UP:
                    scale += 0.1
                if event.key == pygame.K_DOWN:
                    scale -= 0.1
                if scale < 0.1:
                    scale = 0.1
                # Reset
                if event.key == pygame.K_r:
                    move_x = 0
                    move_y = 0
                    move_z = 0
                    rotate_x = 20
                    rotate_y = 30
                    rotate_z = 0
                    scale = 1.0
                    auto_spin = False

        if auto_spin:
            rotate_y += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -16)
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
