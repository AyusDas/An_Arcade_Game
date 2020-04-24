"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import os
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

class Rectangle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 10
        self.width = 50
        self.color = None

def make_rectangle():

    rec = Rectangle()
    rec.color = (random.randrange(256), random.randrange(256), random.randrange(256))
    for i in range(25,SCREEN_WIDTH - 25):
        pass    


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)
        self.dx = 3
        self.dy = 3
        #  sprite lists
        self.player_list = None
        self.player_sprite = None
        self.ball_list = None
        self.ball_sprite = None

    def setup(self):
        #  sprites and sprite lists 

        #--------------------------------------------------------------
        #                       Player
        #--------------------------------------------------------------
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("bridgeB.png",0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 25
        self.player_list.append(self.player_sprite)

        #---------------------------------------------------------------
        #                        Ball
        #---------------------------------------------------------------
        self.ball_list = arcade.SpriteList()
        self.ball_sprite = arcade.Sprite("meteor.png", 0.6)
        self.ball_sprite.center_x = 100
        self.ball_sprite.center_y = 100
        self.ball_list.append(self.ball_sprite)
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.player_list.draw()
        self.ball_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.ball_sprite.center_x += self.dx
        self.ball_sprite.center_y += self.dy

        if self.ball_sprite.center_x < 5 or self.ball_sprite.center_x > SCREEN_WIDTH - 5 :
            self.dx *= -1
        if self.ball_sprite.center_y > SCREEN_HEIGHT - 5 :
            self.dy *= -1
        if arcade.check_for_collision(self.player_sprite, self.ball_sprite):
            self.dy *= -1  
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        #self.player_sprite.center_y = SCREEN_HEIGHT - 10
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
