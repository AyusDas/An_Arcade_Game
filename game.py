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

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
RECTANGLE_COUNT = 25
SCREEN_TITLE = "Starting Template"


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

        #Player-------------------
        self.player_list = None
        self.player_sprite = None
        #-------------------------

        # Ball--------------------
        self.ball_list = None
        self.ball_sprite = None
        #-------------------------

        #Rectangles---------------
        self.blue_rec_list = None
        self.red_rec_list = None
        self.lime_rec_list = None
        self.yellow_rec_list = None
        self.purple_rec_list = None
        #--------------------------

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

        #----------------------------------------------------------------
        #                        Rectangles
        #----------------------------------------------------------------
        self.box_rec_list = arcade.SpriteList()
       

        for i in range(RECTANGLE_COUNT):

            box_rec = arcade.Sprite("boxCrate_double.png",0.5)

            box_rec.center_x = random.randrange(5,SCREEN_WIDTH-5)
            box_rec.center_y = random.randrange(200,SCREEN_HEIGHT-5)

            self.box_rec_list.append(box_rec)
            


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.player_list.draw()
        self.ball_list.draw()

        self.box_rec_list.draw()
       
        

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.ball_sprite.center_x += self.dx
        self.ball_sprite.center_y += self.dy

        self.box_rec_list.update()
        


        if self.ball_sprite.center_x < 5 or self.ball_sprite.center_x > SCREEN_WIDTH - 5 :
            self.dx *= -1
        if self.ball_sprite.center_y > SCREEN_HEIGHT - 5 :
            self.dy *= -1
        if arcade.check_for_collision(self.player_sprite, self.ball_sprite):
            self.dy *= -1  
        
        hit_list_blue = arcade.check_for_collision_with_list(self.ball_sprite, self.box_rec_list)
        for box_rec in hit_list_blue:
            if self.ball_sprite.center_y < box_rec.center_y - 1 or self.ball_sprite.center_y > box_rec.center_y + 1 :
                self.dx *= 1
                self.dy *= -1
            else:    
                self.dx *= -1
                self.dy *= 1
            box_rec.remove_from_sprite_lists()
        
       
        
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
