
"""
# sandbox basic class using character points approach
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def doublespeed(self):
        self.speed *= 2

warrior = Character(100, 50, 10)
ninja = Character(80, 40, 40)

print(f"Warrior speed {warrior.speed}")
print(f"Ninja speed {ninja.speed}")
warrior.doublespeed()
print(f"Warrior speed {warrior.speed}")
print(f"Ninja speed {ninja.speed}")
"""

import turtle

class ClickableMenuItem:
    """
    A single clickable menu item rendered as text with a rectangular hit box.
    """
    def __init__(self, label, x, y, action, width=220, height=30,
                 font=("Arial", 18, "normal"), align="center"):
        self._label = label
        self._x = x
        self._y = y
        self._action = action
        self._width = width
        self._height = height
        self._font = font
        self._align = align

    # --- Rendering ---
    def draw(self, pen):
        pen.penup()
        pen.goto(self._x, self._y)
        pen.write(self._label, align=self._align, font=self._font)
        pen.penup()
        # add border to click box
        pen.goto(self._x - self._width //2 , self._y + self._height) ## start top left
        pen.pendown()
        pen.goto(self._x + self._width //2 , self._y + self._height) # draw top edge
        pen.goto(self._x + self._width //2 , self._y) # draw right edge
        pen.goto(self._x - self._width //2 , self._y) # Draw bottom edge        
        pen.goto(self._x - self._width //2 , self._y + self._height) # Draw left edge
        pen.penup()
        

    # --- Interaction ---
    def contains_point(self, px, py):
        left = self._x - self._width / 2
        right = self._x + self._width / 2
        bottom = self._y
        top = self._y + self._height
        return left <= px <= right and bottom <= py <= top

    def click(self):
        # Call the associated handler
        if callable(self._action):
            self._action()

    # Optional: simple getters if you want read-only access
    def label(self):
        return self._label


class Menu:
    """
    Owns multiple ClickableMenuItems, draws them, and routes clicks.
    """
    def __init__(self, screen, items=None):
        self._screen = screen
        self._items = items[:] if items else []

        self._pen = turtle.Turtle(visible=False)
        self._pen.penup()

        # Hook mouse clicks once; Menu will route them.
        self._screen.onclick(self._on_click)

    def add_item(self, item):
        self._items.append(item)

    def draw(self):
        self._pen.clear()
        for item in self._items:
            item.draw(self._pen)

    def _on_click(self, x, y):
        # If multiple items overlap, first match wins.
        for item in self._items:
            if item.contains_point(x, y):
                item.click()
                break


# ---------------- Example usage ----------------

def main():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Clickable Menu Example")

    def start_game():
        print("Start clicked")

    def options():
        print("Options clicked")

    def quit_game():
        screen.bye()

    menu = Menu(screen)

    menu.add_item(ClickableMenuItem("Start",   0,  80, start_game))
    menu.add_item(ClickableMenuItem("Options", 0,  20, options))
    menu.add_item(ClickableMenuItem("Quit",    0, -40, quit_game))

    menu.draw()
    turtle.done()

if __name__ == "__main__":
    main()
