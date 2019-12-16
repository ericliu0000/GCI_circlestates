# Program to calculate the state of two circles for GCI by eliu0000
import pygame


input1 = float(input("What is the radius of the first circle?\n"))
input2 = float(input("What is the radius of the second circle?\n"))
distance = float(input("What is the distance between the center of the two circles?\n"))

# This ensures circle_1 is always the largest circle. This is needed later on,
# as the canvas scale must depend on the largest object to scale correctly.
circle_1 = max(input1, input2)
circle_2 = min(input1, input2)

edgeDist = float(distance - (circle_1 + circle_2))

# Calculates zoom based on maximum horizontal width, allowing for a 50 px
# border on each side.
canvas_scale = 500/(2 * (circle_1 + circle_2) + edgeDist)

radius_1 = circle_1 * canvas_scale
radius_2 = circle_2 * canvas_scale
draw_distance = distance * canvas_scale

# Generates text message to display on pygame canvas based on the radius of
# the circles, the distance between the centers, as well as the distance
# between the edges of the circles.
def message(large_circle, small_circle, distance):
    if large_circle == small_circle and distance == 0:
        return "The circles are equal to each other"
    elif distance == 0:
        return "The circles are concentric"
    elif edgeDist == 0 or edgeDist == -2 * (small_circle):
        return "The circles are tangential"
    elif edgeDist > 0 or edgeDist < -2 * (small_circle):
        return "The circles do not intersect"
    elif edgeDist > -2 * small_circle and edgeDist < 0:
        return "The circles intersect twice"


def draw(large_circle, small_circle, distance, text):
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    # Offset calculations based on a 50 px border from the top left corner.
    # All other sides, except the bottom, maintain a 50 px border because of
    # the canvas scale.
    y_offset = large_circle + 50
    center_1 = 50 + large_circle
    center_2 = center_1 + distance

    # Prepares text from the message function
    font = pygame.font.Font('freesansbold.ttf', 32)
    draw_text = font.render(str(text), True, white, black)
    text_object = draw_text.get_rect()
    text_object.center = (300, 650)

    # Draws the text, larger circle (in blue), and smaller circle (in red)
    gameDisplay.blit(draw_text, text_object)
    pygame.draw.circle(gameDisplay, blue, (center_1, y_offset), large_circle, 2)
    pygame.draw.circle(gameDisplay, red, (center_2, y_offset), small_circle, 1)


pygame.init()
gameDisplay = pygame.display.set_mode((600, 700))
pygame.display.set_caption("State of Two Circles")

display_text = message(circle_1, circle_2, distance)
draw(int(radius_1), int(radius_2), int(draw_distance), display_text)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
