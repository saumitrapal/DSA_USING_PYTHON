#-----------------------------------------Note---------------------------------------------#

# class are the blueprint of object means framework of object.
# here i create Cookie classes under cookie classess __inti__() is constractor
# and get-color() and set_color() are method. get_color() return the color of cookie and
# set_color() is set a color of cookie.

#----------------------------------------define classess------------------------------------#
class Cookie:
    # this __init__() -> knows as constractor.
    def __init__(self, color):
        self.color = color
    
    # get_color() -> is a method. that's return the color of cookie.    
    def get_color(self):
        return self.color
    
    # set_color() -> is a method. that set the color of cookie.
    def set_color(self, color):
        self.color = color
        
cookie_one = Cookie("Red")
print(cookie_one.get_color())

cookie_one.set_color("Blue")
print(cookie_one.get_color())
    