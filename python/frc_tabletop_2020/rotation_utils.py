import math
from pygame.math import Vector2

def rotate_point(x,y,x0,y0, angle_degrees):
    """
    rotate a point x,y counterclockwise by a given angle around a given origin x0,y0.
   

    The angle should be given in degrees.
    """

    angle=math.radians(angle_degrees)

    x_prime = x0 + math.cos(angle)*(x - x0) - math.sin(angle)*(y - y0)
    y_prime = y0 + math.sin(angle)*(x - x0) + math.cos(angle)*(y - y0)
    return x_prime,y_prime


def rotate_vector(v,v0, angle_degrees):
    """
    rotate a point x,y counterclockwise by a given angle around a given origin x0,y0.
   

    The angle should be given in degrees.
    """


    angle=math.radians(angle_degrees)

    x_prime = v0.x + math.cos(angle)*(v.x - v0.x) - math.sin(angle)*(v.y - v0.y)
    y_prime = v0.y + math.sin(angle)*(v.x - v0.x) + math.cos(angle)*(v.y - v0.y)
    return Vector2(x_prime,y_prime)
