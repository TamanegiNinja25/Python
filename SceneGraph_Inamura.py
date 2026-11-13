import os
import math
import pygame

# -------------------------------------------------------------------
# Scene graph of the flame swordsman image.
# Bottom row  : primitive shapes (circle, line, square, triangle...)
# Middle rows : objects built from those primitives
# Top         : the finished scene
# Arrows point from a part to the object that uses it.
# A red (n) means that part is used n times.
# Hover over a box to read what it is.
# -------------------------------------------------------------------

WIDTH, HEIGHT = 1200, 900

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (215, 30, 30)
DARK_RED = (130, 20, 20)
ORANGE = (255, 140, 20)
YELLOW = (255, 210, 40)
SKIN = (250, 215, 175)
STEEL = (120, 120, 135)
CAPE = (245, 240, 230)


# ---------------- helpers ----------------
def sub(r, fx, fy, fw, fh):
    # A smaller rectangle inside r, given as fractions of r
    return pygame.Rect(r.x + fx * r.w, r.y + fy * r.h, fw * r.w, fh * r.h)


def pt(r, fx, fy):
    return (r.x + fx * r.w, r.y + fy * r.h)


def rect_poly(cx, cy, w, h, angle):
    # Corners of a w x h rectangle centered at (cx, cy), rotated by angle (degrees)
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    corners = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
    return [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in corners]


# ---------------- primitives ----------------
def draw_background(s, r):
    pygame.draw.rect(s, ORANGE, r)
    pygame.draw.rect(s, YELLOW, sub(r, 0, 0, 1, 0.45))
    jag = [pt(r, 0, 1)]
    for i in range(9):
        jag.append(pt(r, i / 8, 0.65 if i % 2 == 0 else 0.85))
    jag.append(pt(r, 1, 1))
    pygame.draw.polygon(s, RED, jag)


def draw_circle(s, r):
    pygame.draw.circle(s, BLACK, r.center, int(min(r.w, r.h) * 0.4), 3)


def draw_filled_circle(s, r):
    pygame.draw.circle(s, BLACK, r.center, int(min(r.w, r.h) * 0.4))


def draw_line(s, r):
    pygame.draw.line(s, BLACK, pt(r, 0.15, 0.5), pt(r, 0.85, 0.5), 4)


def draw_filled_square(s, r):
    side = min(r.w, r.h) * 0.75
    sq = pygame.Rect(0, 0, side, side)
    sq.center = r.center
    pygame.draw.rect(s, BLACK, sq)


def draw_triangle(s, r):
    pygame.draw.polygon(s, BLACK, [pt(r, 0.5, 0.1), pt(r, 0.9, 0.9), pt(r, 0.1, 0.9)])


# ---------------- objects (built from primitives) ----------------
def draw_light_burst(s, r):
    # FILLED CIRCLE + 12 LINES
    cx, cy = r.center
    rad = min(r.w, r.h) * 0.22
    for i in range(12):
        a = math.radians(i * 30)
        p1 = (cx + math.cos(a) * rad * 1.3, cy + math.sin(a) * rad * 1.3)
        p2 = (cx + math.cos(a) * rad * 2.1, cy + math.sin(a) * rad * 2.1)
        pygame.draw.line(s, ORANGE, p1, p2, 3)
    pygame.draw.circle(s, YELLOW, (cx, cy), int(rad))
    pygame.draw.circle(s, ORANGE, (cx, cy), int(rad), 2)


def draw_flame(s, r):
    # 3 TRIANGLES
    pygame.draw.polygon(s, RED, [pt(r, 0.5, 0.0), pt(r, 0.95, 1), pt(r, 0.05, 1)])
    pygame.draw.polygon(s, ORANGE, [pt(r, 0.5, 0.3), pt(r, 0.8, 1), pt(r, 0.2, 1)])
    pygame.draw.polygon(s, YELLOW, [pt(r, 0.5, 0.6), pt(r, 0.65, 1), pt(r, 0.35, 1)])


def draw_head(s, r):
    # CIRCLE (face) + 10 TRIANGLES (hair spikes) + 2 FILLED CIRCLES (eyes)
    cx, cy = r.centerx, r.y + r.h * 0.6
    rad = min(r.w, r.h) * 0.28
    for i in range(10):
        a = math.radians(180 + 18 * i + 9)
        b1 = math.radians(180 + 18 * i)
        b2 = math.radians(180 + 18 * (i + 1))
        tip = (cx + math.cos(a) * rad * 1.75, cy + math.sin(a) * rad * 1.75)
        base1 = (cx + math.cos(b1) * rad * 0.9, cy + math.sin(b1) * rad * 0.9)
        base2 = (cx + math.cos(b2) * rad * 0.9, cy + math.sin(b2) * rad * 0.9)
        pygame.draw.polygon(s, YELLOW if i % 2 else ORANGE, [base1, tip, base2])
    pygame.draw.circle(s, SKIN, (cx, cy), int(rad))
    pygame.draw.circle(s, BLACK, (cx, cy), int(rad), 2)
    eye = max(2, int(rad * 0.18))
    pygame.draw.circle(s, ORANGE, (int(cx - rad * 0.4), int(cy - rad * 0.1)), eye)
    pygame.draw.circle(s, ORANGE, (int(cx + rad * 0.4), int(cy - rad * 0.1)), eye)


def draw_arm(s, r, angle=0):
    # 2 FILLED SQUARES (upper arm + forearm), stretched into bars
    cx, cy = r.center
    length = r.w * 0.45
    thick = max(4, r.h * 0.25)
    a = math.radians(angle)
    dx, dy = math.cos(a) * length / 2, math.sin(a) * length / 2
    pygame.draw.polygon(s, BLACK, rect_poly(cx - dx, cy - dy, length, thick, angle))
    pygame.draw.polygon(s, (60, 60, 60), rect_poly(cx + dx, cy + dy, length, thick * 0.85, angle))


def draw_sword(s, r):
    # LINE (blade) + FILLED SQUARE (handle) + 4 FLAMES (fire trail)
    start, end = pt(r, 0.2, 0.85), pt(r, 0.92, 0.12)
    for i in range(4):
        f = 0.35 + i * 0.17
        fx = start[0] + (end[0] - start[0]) * f
        fy = start[1] + (end[1] - start[1]) * f
        size = r.w * 0.16
        draw_flame(s, pygame.Rect(fx - size / 2, fy - size * 1.1, size, size))
    pygame.draw.line(s, STEEL, start, end, max(2, int(r.w * 0.03)))
    pygame.draw.polygon(s, DARK_RED, rect_poly(r.x + r.w * 0.14, r.y + r.h * 0.9,
                                               r.w * 0.2, max(4, r.h * 0.09), -45))


def draw_body(s, r):
    # 3 FILLED SQUARES (torso + 2 legs) + TRIANGLE (cape)
    cape = [pt(r, 0.45, 0.02), pt(r, 0.98, 0.0), pt(r, 0.85, 0.75)]
    pygame.draw.polygon(s, CAPE, cape)
    pygame.draw.polygon(s, RED, cape, 2)
    pygame.draw.rect(s, DARK_RED, sub(r, 0.3, 0.45, 0.16, 0.55))
    pygame.draw.rect(s, DARK_RED, sub(r, 0.52, 0.45, 0.16, 0.55))
    pygame.draw.rect(s, BLACK, sub(r, 0.26, 0.0, 0.46, 0.48))


def draw_swordsman(s, r):
    # HEAD + BODY + 2 ARMS + SWORD
    draw_body(s, sub(r, 0.25, 0.32, 0.6, 0.66))
    draw_arm(s, sub(r, 0.02, 0.36, 0.4, 0.14), 0)
    draw_arm(s, sub(r, 0.55, 0.2, 0.3, 0.14), -40)
    draw_sword(s, sub(r, 0.62, 0.0, 0.38, 0.32))
    draw_head(s, sub(r, 0.32, 0.0, 0.36, 0.34))


def draw_scene(s, r):
    # The whole picture: BACKGROUND + LIGHT BURST + 20 FLAMES + SWORDSMAN
    draw_background(s, r)
    draw_light_burst(s, sub(r, 0.3, 0.1, 0.4, 0.6))
    for i in range(10):
        draw_flame(s, sub(r, i / 10, 0.78, 0.1, 0.22))
        draw_flame(s, sub(r, 0.0 if i < 5 else 0.92, 0.1 + (i % 5) * 0.13, 0.08, 0.13))
    draw_swordsman(s, sub(r, 0.25, 0.08, 0.5, 0.86))


# ---------------- scene graph data ----------------
class Node:
    def __init__(self, name, x, y, w, h, draw_fn, desc, label=True):
        self.name = name
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = (x, y)
        self.draw_fn = draw_fn
        self.desc = desc
        self.label = label


def build_graph():
    P_Y, O_Y, BOX = 730, 560, 110
    n = {
        # Primitives
        "BACKGROUND": Node("BACKGROUND", 80, P_Y, BOX, BOX, draw_background,
                           "Glowing orange backdrop with a jagged red edge."),
        "CIRCLE": Node("CIRCLE", 260, P_Y, BOX, BOX, draw_circle,
                       "Circle outline, used for the face."),
        "FILLED CIRCLE": Node("FILLED CIRCLE", 430, P_Y, BOX, BOX, draw_filled_circle,
                              "Filled circle, used for the light burst core and the eyes."),
        "TRIANGLE": Node("TRIANGLE", 600, P_Y, BOX, BOX, draw_triangle,
                         "Triangle, used for flames, hair spikes and the cape."),
        "LINE": Node("LINE", 1000, P_Y, BOX, BOX, draw_line,
                     "Line, used for the light rays and the sword blade."),
        "FILLED SQUARE": Node("FILLED SQUARE", 1135, P_Y, BOX, BOX, draw_filled_square,
                              "Filled square, stretched for the arms, torso, legs and sword handle."),
        # Objects
        "LIGHT BURST": Node("LIGHT BURST", 300, O_Y, BOX, BOX, draw_light_burst,
                            "The bright glow behind the swordsman: 1 filled circle + 12 lines."),
        "FLAME": Node("FLAME", 450, O_Y, BOX, BOX, draw_flame,
                      "One flame: 3 stacked triangles. Reused in the scene and on the sword."),
        "HEAD": Node("HEAD", 600, O_Y, BOX, BOX, draw_head,
                     "Head: circle face, 10 triangle hair spikes, 2 filled-circle eyes."),
        "BODY": Node("BODY", 750, O_Y, BOX, BOX, draw_body,
                     "Body: 3 filled squares (torso, 2 legs) and a triangle cape."),
        "ARM": Node("ARM", 900, O_Y, BOX, BOX, draw_arm,
                    "Arm: 2 filled squares (upper arm and forearm). Used twice."),
        "SWORD": Node("SWORD", 1090, 395, BOX, BOX, draw_sword,
                      "Sword: line blade, filled-square handle, 4 flames along the blade."),
        "SWORDSMAN": Node("SWORDSMAN", 850, 250, 130, 120, draw_swordsman,
                          "The character: head, body, 2 arms and the sword."),
        "SCENE": Node("SCENE", 600, 95, 260, 150, draw_scene,
                      "The finished image: background, light burst, 20 flames and the swordsman.",
                      label=False),
    }

    # (part, object that uses it, how many times)
    edges = [
        ("BACKGROUND", "SCENE", 1),
        ("LIGHT BURST", "SCENE", 1),
        ("FLAME", "SCENE", 20),
        ("SWORDSMAN", "SCENE", 1),
        ("FILLED CIRCLE", "LIGHT BURST", 1),
        ("LINE", "LIGHT BURST", 12),
        ("TRIANGLE", "FLAME", 3),
        ("CIRCLE", "HEAD", 1),
        ("FILLED CIRCLE", "HEAD", 2),
        ("TRIANGLE", "HEAD", 10),
        ("FILLED SQUARE", "ARM", 2),
        ("LINE", "SWORD", 1),
        ("FILLED SQUARE", "SWORD", 1),
        ("FLAME", "SWORD", 4),
        ("FILLED SQUARE", "BODY", 3),
        ("TRIANGLE", "BODY", 1),
        ("HEAD", "SWORDSMAN", 1),
        ("BODY", "SWORDSMAN", 1),
        ("ARM", "SWORDSMAN", 2),
        ("SWORD", "SWORDSMAN", 1),
    ]
    return n, edges


def anchor_points(nodes, edges):
    # Spread arrow ends along each box edge so they don't overlap
    starts, ends = {}, {}
    for name, node in nodes.items():
        outgoing = sorted([e for e in edges if e[0] == name], key=lambda e: nodes[e[1]].rect.centerx)
        for i, e in enumerate(outgoing):
            r = node.rect
            starts[e] = (r.left + r.w * (i + 1) / (len(outgoing) + 1), r.top)
        incoming = sorted([e for e in edges if e[1] == name], key=lambda e: nodes[e[0]].rect.centerx)
        for i, e in enumerate(incoming):
            r = node.rect
            ends[e] = (r.left + r.w * (i + 1) / (len(incoming) + 1), r.bottom)
    return starts, ends


def draw_arrow(s, start, end, color=BLACK):
    pygame.draw.line(s, color, start, end, 2)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 11
    left = (end[0] - size * math.cos(angle - 0.4), end[1] - size * math.sin(angle - 0.4))
    right = (end[0] - size * math.cos(angle + 0.4), end[1] - size * math.sin(angle + 0.4))
    pygame.draw.polygon(s, color, [end, left, right])


def draw_node(s, node, font, hovered, photo):
    r = node.rect
    pygame.draw.rect(s, WHITE, r)
    if node.label:
        icon = pygame.Rect(r.x + 8, r.y + 8, r.w - 16, r.h - 34)
        node.draw_fn(s, icon)
        text = font.render(node.name, True, BLACK)
        s.blit(text, text.get_rect(center=(r.centerx, r.bottom - 14)))
    elif photo:
        s.blit(pygame.transform.smoothscale(photo, r.size), r.topleft)
    else:
        node.draw_fn(s, r)
    pygame.draw.rect(s, RED if node is hovered else BLACK, r, 3 if node is hovered else 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Scene Graph - Inamura")

    label_font = pygame.font.SysFont("arial", 13, bold=True)
    count_font = pygame.font.SysFont("arial", 16, bold=True)
    caption_font = pygame.font.SysFont("arial", 18, bold=True, italic=True)
    info_font = pygame.font.SysFont("arial", 17)

    # Optional: put the real picture next to this file as "scene.jpg"
    # and it will be shown in the top box instead of the drawn version.
    photo = None
    photo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scene.jpg")
    if os.path.exists(photo_path):
        photo = pygame.image.load(photo_path)

    nodes, edges = build_graph()
    starts, ends = anchor_points(nodes, edges)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse = pygame.mouse.get_pos()
        hovered = next((nd for nd in nodes.values() if nd.rect.collidepoint(mouse)), None)

        screen.fill(WHITE)

        for e in edges:
            highlight = hovered is not None and hovered.name in (e[0], e[1])
            draw_arrow(screen, starts[e], ends[e], RED if highlight else BLACK)

        for e in edges:
            if e[2] > 1:
                sx, sy = starts[e]
                ex, ey = ends[e]
                lx, ly = sx + (ex - sx) * 0.3, sy + (ey - sy) * 0.3
                text = count_font.render("(" + str(e[2]) + ")", True, RED)
                bg = text.get_rect(center=(lx, ly)).inflate(4, 2)
                pygame.draw.rect(screen, WHITE, bg)
                screen.blit(text, text.get_rect(center=(lx, ly)))

        for nd in nodes.values():
            draw_node(screen, nd, label_font, hovered, photo)

        caption = caption_font.render("Figure. The flame swordsman scene and its scene graph.", True, BLACK)
        screen.blit(caption, caption.get_rect(center=(WIDTH // 2, 812)))

        panel = pygame.Rect(20, HEIGHT - 70, WIDTH - 40, 50)
        pygame.draw.rect(screen, (240, 240, 240), panel, border_radius=8)
        info = hovered.name + ": " + hovered.desc if hovered else \
            "Hover over a box. Arrows point from a part to the object that uses it; red (n) = number of copies."
        screen.blit(info_font.render(info, True, BLACK), (panel.x + 15, panel.y + 15))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
