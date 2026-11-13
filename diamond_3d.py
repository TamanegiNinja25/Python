from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

rotation_x = 0.0
rotation_y = 0.0
rotation_z = 0.0

position_x = 0.0
position_y = 0.0
position_z = 0.0

scale = 1.0

def draw_diamond():
    top = (0.0, 1.5, 0.0)
    bottom = (0.0, -1.5, 0.0)

    front = (0.0, 0.0, 1.0)
    back = (0.0, 0.0, -1.0)

    left = (-1.0, 0.0, 0.0)
    right = (1.0, 0.0, 0.0)

    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3fv(top)
    glVertex3fv(front)
    glVertex3fv(right)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3fv(top)
    glVertex3fv(right)
    glVertex3fv(back)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3fv(top)
    glVertex3fv(back)
    glVertex3fv(left)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3fv(top)
    glVertex3fv(left)
    glVertex3fv(front)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3fv(bottom)
    glVertex3fv(right)
    glVertex3fv(front)

    glColor3f(0.0, 1.0, 1.0)
    glVertex3fv(bottom)
    glVertex3fv(back)
    glVertex3fv(right)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3fv(bottom)
    glVertex3fv(left)
    glVertex3fv(back)

    glColor3f(0.5, 0.0, 1.0)
    glVertex3fv(bottom)
    glVertex3fv(front)
    glVertex3fv(left)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    gluLookAt(
        4.0, 3.0, 6.0,
        0.0, 0.0, 0.0,
        0.0, 1.0, 0.0
    )

    glTranslatef(position_x, position_y, position_z)

    glRotatef(rotation_x, 1.0, 0.0, 0.0)
    glRotatef(rotation_y, 0.0, 1.0, 0.0)
    glRotatef(rotation_z, 0.0, 0.0, 1.0)

    glScalef(scale, scale, scale)

    draw_diamond()

    glutSwapBuffers()


def keyboard(key, x, y):
    global rotation_x, rotation_y, rotation_z
    global position_x, position_y, position_z
    global scale

    key = key.decode("utf-8")

    if key == 'w':
        rotation_x += 5

    elif key == 's':
        rotation_x -= 5

    elif key == 'a':
        rotation_y += 5

    elif key == 'd':
        rotation_y -= 5

    elif key == 'q':
        rotation_z += 5

    elif key == 'e':
        rotation_z -= 5

    elif key == '+':
        scale += 0.1

    elif key == '-':
        scale -= 0.1

        if scale < 0.1:
            scale = 0.1

    elif key == 'z':
        position_z += 0.2

    elif key == 'x':
        position_z -= 0.2

    elif key == 'r':
        rotation_x = 0.0
        rotation_y = 0.0
        rotation_z = 0.0

        position_x = 0.0
        position_y = 0.0
        position_z = 0.0

        scale = 1.0

    elif key == '\x1b':
        sys.exit()

    glutPostRedisplay()


def special_keyboard(key, x, y):
    global position_x, position_y

    if key == GLUT_KEY_UP:
        position_y += 0.2

    elif key == GLUT_KEY_DOWN:
        position_y -= 0.2

    elif key == GLUT_KEY_LEFT:
        position_x -= 0.2

    elif key == GLUT_KEY_RIGHT:
        position_x += 0.2

    glutPostRedisplay()


def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(
        45.0,
        float(width) / float(height),
        0.1,
        100.0
    )

    glMatrixMode(GL_MODELVIEW)


def init():
    glClearColor(0.05, 0.05, 0.05, 1.0)

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    glutInit(sys.argv)

    glutInitDisplayMode(
        GLUT_DOUBLE |
        GLUT_RGB |
        GLUT_DEPTH
    )

    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Diamond - GL_TRIANGLES")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keyboard)

    glutMainLoop()


if __name__ == "__main__":
    main()
