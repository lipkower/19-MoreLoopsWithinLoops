"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Emma Lipkowski.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is non negative.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    # for k in range(rectangle):
    #   for i in range(n):
    #       print(i + 1, end='')
    rect = rectangle.clone()
    upper_left_x = rect.get_upper_left_corner().x
    print(upper_left_x)
    lower_right_x = rect.get_lower_right_corner().x
    print(lower_right_x)
    upper_left_y = rect.get_upper_left_corner().y
    lower_right_y = rect.get_lower_right_corner().y
    diff_x = rect.get_width()
    diff_y = rect.get_height()
    rectangle.attach_to(window)
    for i in range(n):
        for j in range(i + 1):
            rect = rg.Rectangle(rg.Point(upper_left_x, upper_left_y), rg.Point(lower_right_x, lower_right_y))
            rect.attach_to(window)
            upper_left_x = upper_left_x + diff_x
            lower_right_x = lower_right_x + diff_x
            print('The upper_left_x value is:', upper_left_x)
            print('The lower_right_x value is:', lower_right_x)
        upper_left_x = rectangle.get_upper_left_corner().x - ((i + 1) * diff_x / 2)
        lower_right_x = rectangle.get_lower_right_corner().x - ((i + 1) * diff_x / 2)
        upper_left_y = rectangle.get_upper_left_corner().y - ((i + 1) * diff_y)
        lower_right_y = rectangle.get_lower_right_corner().y - ((i + 1) * diff_y)
    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
