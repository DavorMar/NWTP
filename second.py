import time
import pyautogui
import os

class GameBot:
    def __init__(self,command):
        self.command = command
        self.perk_dir = "images\perk pics"
        self.login_pics_dir = "images\login_pictures"
        self.ah_pics_dir = r"images\AH pics"

    def check_status(self):

        login_pics= os.listdir(fr"{self.login_pics_dir}")
        pictures_found = True
        check = False
        while pictures_found is True:
            pictures_found = False
            for pic in login_pics:
                button_location = pyautogui.locateOnScreen(fr"{self.login_pics_dir}\{pic}",confidence = 0.8)
                if button_location:
                    check = True
                    button_location_center = pyautogui.center(button_location)
                    button_x,button_y = button_location_center
                    pyautogui.moveTo(button_x,button_y,0.25)
                    time.sleep(1)
                    pyautogui.click()
                    time.sleep(5)
                    pictures_found = True
                    break
        if check:
            time.sleep(35)
            pyautogui.keyDown("S")
            time.sleep(3)
            pyautogui.keyUp("S")
            time.sleep(0.1)
            pyautogui.keyDown("W")
            time.sleep(1.6)
            pyautogui.keyUp("W")
            time.sleep(0.1)
            pyautogui.press("E")

    def anti_afk(self):
        pyautogui.press("escape")
        time.sleep(0.1)
        pyautogui.keyDown("S")
        time.sleep(0.1)
        pyautogui.keyUp("S")
        time.sleep(0.1)
        pyautogui.keyDown("W")
        time.sleep(0.05)
        pyautogui.keyUp("W")
        time.sleep(0.1)
        pyautogui.press("E")

    def search(self):
        time.sleep(5)
        command_split = self.command.split("-")
        if command_split[0] == "!searchbyname":
            self.name_search(command_split[1],command_split[2])
        elif command_split[0] == "!searchweapon":
            self.search_weapon(command_split[1],command_split[2],command_split[3],command_split[4])
        elif command_split[0]== "!searcharmor":
            self.search_armor(command_split[1],command_split[2],command_split[3],command_split[4],command_split[5])


    def search_weapon(self,slot,perk1,perk2,sort):
        perk1 = perk1.lower()
        perk2 = perk2.lower()
        slot = slot.upper()
        #do smth
        x_location = 250
        y_locations_slots1 = {"LF":430,"VG":430,"FS":430,"IG":430,
                              "WH":475,"SP":475,"GA":475,"BO":475,"MU":475,
                              "HA":530,"RA":530,"SW":530}
        y_locations_slots2 = {"LF":430,"VG":490,"FS":550,"IG":620,
                              "WH":430,"SP":500,"GA":550,"BO":620,"MU":680,
                              "HA":430,"RA":500,"SW":550}
        pyautogui.moveTo(130,380,0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(x_location,y_locations_slots1[slot],0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(x_location,y_locations_slots2[slot],0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.5)
        self.delete_perks()
        self.choose_perk(perk1)
        self.choose_perk(perk2)
        time.sleep(2)
        if pyautogui.locateOnScreen(fr"{self.ah_pics_dir}\no_items_found.png", confidence=0.90):
            pass
        else:
            self.sort(sort)
            time.sleep(0.5)

            self.individual_photos()
        pyautogui.moveTo(1800,10,0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.screenshot(r"images\screenshots\image_ss.png")
        time.sleep(1)
        print("took screenshots")


    def search_armor(self,slot,weight,perk1,perk2,sort):
        perk1 = perk1.lower()
        perk2 = perk2.lower()
        slot = slot.lower()
        weight = weight.upper()
        #do smth
        xlocation= 250
        y_locations_slots = {"head":420,"chest":530,"feet":580,"legs":635,"hands":700}
        y_locations_weights={"H":430,"M":500,"L":560}
        pyautogui.moveTo(120,520,0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.moveTo(xlocation,y_locations_slots[slot])
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.moveTo(xlocation,y_locations_weights[weight])
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.5)
        self.delete_perks()
        self.choose_perk(perk1)
        self.choose_perk(perk2)
        time.sleep(2)
        if pyautogui.locateOnScreen(fr"{self.ah_pics_dir}\no_items_found.png",confidence = 0.90):
            pass
        else:
            self.sort(sort)
            time.sleep(0.5)
            self.individual_photos()
        pyautogui.moveTo(1800, 10, 0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.screenshot(r"images\screenshots\image_ss.png")
        time.sleep(1)
        print("took screenshots")



    def name_search(self,name,sort):
        print(name)
        name_split = list(name)
        self.delete_perks()
        pyautogui.moveTo(250,225,0.25)
        time.sleep(0.1)
        pyautogui.click()
        for letter in name_split:
            pyautogui.press(letter)
            time.sleep(0.3)
        pyautogui.press("enter")
        pyautogui.moveTo(225,350,0.25)
        pyautogui.click()
        pyautogui.sleep(2)
        self.sort(sort)

        time.sleep(0.5)
        pyautogui.moveTo(1800, 10, 0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.screenshot(r"images\screenshots\image_ss.png")
        time.sleep(0.1)

    def sort(self,type):
        sort_set = False
        type = type.lower()
        if type == "price":
            pyautogui.moveTo(1065, 300, 0.25)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(1)
            tries = 0
            while sort_set is False and tries < 10:
                tries+=1
                if pyautogui.locateOnScreen(fr"{self.ah_pics_dir}\sort_by_price.PNG",confidence=0.9,grayscale=True):
                    sort_set = True
                    print("SORTED")
                elif pyautogui.locateOnScreen(fr"{self.ah_pics_dir}\price_sort2.jpg",confidence=0.9,grayscale=True):
                    sort_set = True
                    print("SORTED")
                else:
                    pyautogui.moveTo(1065,300,0.25)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(0.5)
        if type == "gs":
            pyautogui.moveTo(1225, 300, 0.25)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(1)
            tries = 0
            while sort_set is False and tries <7:
                tries += 1
                if pyautogui.locateOnScreen(fr"{self.ah_pics_dir}\sort_by_gs.PNG",confidence=0.9,grayscale=True):
                    sort_set = True
                    print("SORTED")
                else:
                    pyautogui.moveTo(1225,300,0.25)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(0.5)

    def global_photo(self):
        time.sleep(0.5)
        pyautogui.screenshot(r"images\screenshots\image_ss.png")

    def delete_perks(self):
        location_x = 465
        location_y = 216
        pyautogui.moveTo(1275, 225, 0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(location_x,location_y,0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.press("escape")
        time.sleep(0.3)


    def choose_perk(self,perk):
        pyautogui.moveTo(1275,225,0.25)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.5)
        perk_found = False
        while not perk_found:
            perk_pos = pyautogui.locateOnScreen(fr"{self.perk_dir}\{perk}.png", confidence = 0.98)
            if perk_pos:
                perk_found = True
                center_perk_pos = pyautogui.center(perk_pos)
                button_x,button_y = center_perk_pos
                pyautogui.moveTo(button_x,button_y,0.25)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.2)
                print(f"found perk {perk}")
            else:
                pyautogui.moveTo(1000,500,0.25)
                time.sleep(0.1)
                pyautogui.scroll(-720)
                time.sleep(0.3)
        pyautogui.press("escape")
        time.sleep(0.5)

    def individual_photos(self):
        time.sleep(0.3)
        x = 0
        space_diff = 76#pixels between each image
        y_pos = 350
        x_pos = 650
        while x < 7:
            time.sleep(0.3)
            pyautogui.moveTo(x_pos,y_pos,0.08)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(x_pos+5,y_pos,0.05)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen(fr"{self.ah_pics_dir}\compare_with_equipped.png",confidence = 0.9):
                pyautogui.screenshot(fr"images\screenshots\item{x}.png")
                y_pos += space_diff
                x_pos += 3
                x += 1
            else:
                break







# time.sleep(3)
# bot = GameBot("davor")
# bot.check_status()





