import asyncio
import os
import time
import discord
import psutil
from second import GameBot
import threading
import pyautogui






def check_if_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

class MyClient(discord.Client):

    async def on_ready(self):
        self.busy = False
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.logged_in = True
        temp_perk_list = os.listdir(r"images\perk pics")
        self.perk_list = []
        for perk in temp_perk_list:
            perk_name = perk.split(".")[0]
            self.perk_list.append(perk_name)




    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        elif not check_if_process_running("NewWorld"):
            channel = message.channel
            await channel.send("Server host hasnt turned on the game for bot to work")
            return
        if self.busy and message.content.startswith("!hello"):
            channel = message.channel
            await channel.send("Bot is currently busy. Please wait till other user finishes")

        elif message.content.startswith('!hello') and not self.busy:
            channel = message.channel
            self.busy = True
            await channel.send(
                """
TP Bot started, you have 30 seconds
 to reply with 1 of commands:
!searchbyname-"name of the item"-"price/gs"
!searchweapon-"GA/HA/SP/BO/MU/FS/IG/VG/LS/WH/SW/RA"-"PERK"-PERK"-"price/gs"
!searcharmor-"head,chest,feet,legs,hands"-"L/M/H"-"PERK"-"PERK"-"price/gs"
                """, mention_author=True)


            def check(m):
                split_message = m.content.split("-")
                command_list = ["!searchbyname","!searchweapon","!searcharmor"]
                message_validity = False
                if split_message[0] == "!searchbyname":
                    if len(split_message[1]) > 1 and split_message[2].lower() == "price" or split_message[2].lower() == "gs":
                        message_validity = True
                    else:
                        message_validity = False
                elif split_message[0] == "!searchweapon":
                    slot_list = ["GA","HA","SP","BO","MU","FS","IG","VG","LS","WH","SW","SH","RA"]
                    perk_list = self.perk_list
                    # perk_list = ["keen","vicious","enchanted","keenly jagged","keenly empowered","keenly fortified","backstab","vorpal"]
                    if  split_message[1] in slot_list and split_message[2] in perk_list and split_message[3] in perk_list and (split_message[4] == "price" or split_message[4] == "gs"):
                        print(split_message[1])
                        print(split_message[1] in slot_list)
                        message_validity = True
                        print("VALID")
                    else:
                        message_validity = False
                        print("INVALID")
                elif split_message[0] == "!searcharmor":
                    slot_list=["head","chest","legs","feet","hands"]
                    perk_list = ["resilient","refreshing","freedom","keen berserk"]
                    weight_list = ["L","M","H"]
                    if  split_message[1].lower() in slot_list and split_message[2].upper() in weight_list and split_message[3].lower() in perk_list and  split_message[4].lower() in perk_list and split_message[5].lower() == "price" or split_message[5].lower() == "gs":
                        message_validity = True

                return m.author == message.author and m.channel == channel and split_message[0] in command_list and message_validity is True

            # def send_images(channel):
            #     image_names = ["item0", "item1", "item2", "item3", "item4"]
            #     channel.send(file=discord.File(r"images\image_ss.png"))
            #     for image in image_names:
            #         try:
            #             channel.send(file=discord.File(f"{image}.png"))
            #         except FileNotFoundError:
            #             pass


            try:
                m = await client.wait_for("message",timeout=30.0,check = check)
            except asyncio.TimeoutError:
                self.busy=False
                await channel.send(f"30 seconds passed, no (valid) command received from {message.author}, restarting")
            else:
                await channel.send("Searching, please wait")
                bot = GameBot(m.content)
                bot.search()
                self.busy = False
                for image in os.listdir("images\screenshots"):
                    await channel.send(file=discord.File(fr"images\screenshots\{image}"))
                    time.sleep(0.1)
                # await channel.send(file=discord.File(r"images\image_ss.png")), channel.send(file=discord.File("item0.png")), channel.send(file=discord.File("item1.png")),channel.send(file=discord.File("item2.png")),
                    os.remove(fr"images\screenshots\{image}")

    def anti_afk(self):
        time.sleep(60)
        while True:
            try:
                if self.busy:
                    time.sleep(1)
                    continue
                elif not check_if_process_running("NewWorld"):
                    time.sleep(30)
                    continue
                else:
                    self.busy = True
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
                    self.busy = False
                    time.sleep(600)
            except AttributeError:
                print("Bot not yet active so not doing anti afk")
                time.sleep(5)



if __name__ == '__main__':
    with open("token.txt") as token:
        bot_token = token.read()
    client = MyClient()
    afk_thread = threading.Thread(target=client.anti_afk)
    afk_thread.start()
    client.run(bot_token)

