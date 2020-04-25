
import arcade
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
RECTANGLE_COUNT = 25
SCREEN_TITLE = "Destroy The Boxes"


class StartView(arcade.View):

    def __init__(self):
        super().__init__()
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        msg = "PRESS ENTER TO START"
        arcade.draw_text(msg, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.ALABAMA_CRIMSON, 28, anchor_x= "center")

    def on_key_press(self, key, _modifiers):

        if key == arcade.key.ENTER :
            gameview = MyGame()
            gameview.setup()
            self.window.show_view(gameview)    


class MyGame(arcade.View):

    def __init__(self):

        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)
        
        self.dx = 3
        self.dy = 3
        
        #sprite lists

        #Player-------------------
        self.player_list = None
        self.player_sprite = None
        #-------------------------

        # Ball--------------------
        self.ball_list = None
        self.ball_sprite = None
        #-------------------------

        self.box_rec_list = None
        self.score = 0


    def setup(self):
        #  sprites and sprite lists 

        #--------------------------------------------------------------
        #                       Player
        #--------------------------------------------------------------
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("resources/bridgeB.png",0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 30
        self.player_list.append(self.player_sprite)

        #---------------------------------------------------------------
        #                        Ball
        #---------------------------------------------------------------
        self.ball_list = arcade.SpriteList()
        self.ball_sprite = arcade.Sprite("resources/meteor.png", 0.6)
        self.ball_sprite.center_x = 100
        self.ball_sprite.center_y = 100
        self.ball_list.append(self.ball_sprite)

        self.box_rec_list = arcade.SpriteList()
       
        for i in range(RECTANGLE_COUNT):

            box_rec = arcade.Sprite("resources/boxCrate_double.png",0.5)

            box_rec.center_x = random.randrange(5,SCREEN_WIDTH-5)
            box_rec.center_y = random.randrange(220,SCREEN_HEIGHT-5)

            self.box_rec_list.append(box_rec)
            

    def on_draw(self):
        
        arcade.start_render()
        
        #draw the sprites----------------------
        self.player_list.draw()
        self.ball_list.draw()
        self.box_rec_list.draw()
        #--------------------------------------
        
        # display the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.ALABAMA_CRIMSON, 16)


    def on_update(self, delta_time):
        
        self.ball_sprite.center_x += self.dx
        self.ball_sprite.center_y += self.dy

        self.box_rec_list.update()

        if self.ball_sprite.center_x < 5 or self.ball_sprite.center_x > SCREEN_WIDTH - 5 :
            self.dx *= -1
        if self.ball_sprite.center_y > SCREEN_HEIGHT - 5 :
            self.dy *= -1
        if arcade.check_for_collision(self.player_sprite, self.ball_sprite) and self.player_sprite.center_y < self.ball_sprite.center_y:                      
            self.dy *= -1  
        
        hit_list_blue = arcade.check_for_collision_with_list(self.ball_sprite, self.box_rec_list)
        for box_rec in hit_list_blue:
            if self.ball_sprite.center_y <= box_rec.center_y - 32 or self.ball_sprite.center_y >= box_rec.center_y + 32 :
                self.dx *= 1
                self.dy *= -1
            else:    
                self.dx *= -1
                self.dy *= 1
            box_rec.remove_from_sprite_lists()
            self.score += 1
        
        if self.ball_sprite.center_y < 0 :
            start = StartView()
            self.window.show_view(start)


    def on_mouse_motion(self, x, y, delta_x, delta_y):

        self.player_sprite.center_x = x


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_mouse_visible(False)
    start = StartView()
    window.show_view(start)
    arcade.run()


if __name__ == "__main__":
    main()
