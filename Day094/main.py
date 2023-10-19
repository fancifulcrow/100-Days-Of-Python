import pyautogui
from selenium import webdriver
from selenium.webdriver.edge import service


class Dinosaur:
    def __init__(self):
        self.jumps = 0


    # check for obstacles
    def obstacle_ahead(self):
        # get a suitable position away from the dinosaur to detect obstacles
        x0, y0 = 300, 788
        # account for the increasing speed of the game by adjusting the detection point 
        # to slowly move further way from the dinosaur
        x = x0 + int(self.jumps * .3)
        # get the pixel at our detection point
        pixel = pyautogui.pixel(x, y0)
        # if color of the pixel is darker return true else return false
        for color in pixel:
            if color < 128:
                return True
        return False

    
    # make the dinosaur jump
    def jump(self):
        pyautogui.press("up")


if __name__ == "__main__":
    # load the game with selenium
    service = service.Service(r"..\msedgedriver.exe")
    driver = webdriver.Edge(service=service)

    driver.get("https://elgoog.im/dinosaur-game/")
    driver.maximize_window()

    # start the bot
    dino = Dinosaur()

    pyautogui.sleep(10)
    dino.jump()

    while True:
        if dino.obstacle_ahead():
            dino.jump()