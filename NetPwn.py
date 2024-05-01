import random
import time
import string
import sys
from colorama import init, Fore

init(autoreset=True)

# Game logo
game_logo = [
    Fore.LIGHTBLUE_EX + "  _   _      _   _____              ",
    " | \ | |    | | |  __ \                ",
    " |  \| | ___| |_| |__) |_      ___ __  ",
    " | . ` |/ _ \ __|  ___/\ \ /\ / / '_ \ ",
    " | |\  |  __/ |_| |     \ V  V /| | | |",
    " |_| \_|\___|\__|_|      \_/\_/ |_| |_|",
    "                                       ",
]


# Starting sequence
# Starting sequence
def starting_sequence():

    input(f"\nPress {Fore.LIGHTBLUE_EX}ENTER{Fore.RESET} to start the simulation...\n")
    time.sleep(0.25)
    print(f"{Fore.LIGHTGREEN_EX}Initiating The Boot Sequence...\n")
    time.sleep(0.25)

    tasks = [
        "Turning on network interfaces",
        "Running diagnostic checks",
        "Initializing hacking tools",
        "Starting simulation environment",
        "Enabling firewall protections",
    ]

    max_bar_width = 30
    max_task_length = max(len(task) for task in tasks)

    for task in tasks:
        for i in range(101):
            progress_bar = f"{'▧' * int(i / (100 / max_bar_width)):<{max_bar_width}}"
            loading_text = f"{task.ljust(max_task_length)} | Progress: | {progress_bar} | {i}%"
            sys.stdout.write(f"\r{Fore.LIGHTGREEN_EX}{loading_text}{Fore.RESET}")
            sys.stdout.flush()
            time.sleep(0.02)

        print("")  # Move to the next line after completing each task

    # Print the completion message after all tasks are completed

    print("")
    time.sleep(0.5)
    print(f"{Fore.LIGHTGREEN_EX}Boot Sequence Succesfully Completed...")
    time.sleep(0.5)
    print(f"{Fore.LIGHTGREEN_EX}Entering The Simulation...")
    time.sleep(0.5)
    print("")


class Network:
    def __init__(self, name, bank_balance, tools_level):
        self.name = name
        self.bank_balance = bank_balance
        self.tools_level = tools_level
        self.ip_address = '.'.join(str(random.randint(0, 255)) for _ in range(4))
        self.security_level = min(10, random.randint(1, 10) + self.tools_level)
        self.base_hackability = 0.99  # Base hackability set to 50%

    def __str__(self):
        return f"{Fore.LIGHTBLUE_EX}Network Name:{Fore.WHITE}   {self.name}\n{Fore.LIGHTBLUE_EX}    IP Address:{Fore.WHITE}      {self.ip_address}\n{Fore.LIGHTBLUE_EX}    Bank Balance: {Fore.WHITE}   ${self.bank_balance}\n{Fore.LIGHTBLUE_EX}    Security Level:{Fore.WHITE}  {self.security_level}\n{Fore.LIGHTBLUE_EX}    Hackability:{Fore.WHITE}     {self.calculate_hackability():.2%}\n"

    def calculate_hackability(self):
        return max(self.base_hackability, 1.0 - (self.security_level / 10) + (self.tools_level / 20))  # Recalculate hackability with tools upgrade


class HackerSimulator:
    def __init__(self):
        self.wallet_balance = 1000
        self.player_ip_address = '127.0.0.1'
        self.networks = [Network(f"{random.choice(['Vodafone', 'Cisco', 'Telekom', 'Fritzbox'])}-{random.choice([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5)])}", random.randint(500, 10000), 1) for _ in range(3)]
        self.upgrades = {
            'worm': {'name': 'Worm', 'cost': 200, 'level': 1, 'max_level': 3,
                     'description': 'Hacks the network and scans for more networks to hack in that same network'},
            'virus': {'name': 'Virus', 'cost': 500, 'level': 1, 'max_level': 5,
                      'description': 'Hacks the bot\'s network and randomly gives the player 1-2 upgrades as a reward'},
            'botnet': {'name': 'BotNet', 'cost': 1000, 'level': 1, 'max_level': 2,
                       'description': 'Adds the hacked network to a botnet which increases the player\'s stats'},
            'tool': {'name': 'Tool Upgrade', 'cost': 300, 'level': 1, 'max_level': 5,
                     'description': 'Upgrades the player\'s hacking tools'}
        }

        self.stats = {'total_money_stolen': 0,
                      'total_hacks': 0,
                      'total_exploit_used': {exploit: 0 for exploit in self.upgrades},
                      'botnet_size': 0}  # Default botnet size
        self.max_security_level = max(network.security_level for network in self.networks)
        self.hacked_network = None
        self.botnet = []
        self.exiting = False  # Flag to track if the user is exiting

        # List of hacking tasks
        self.hacking_tasks = [
            f"Pinging {self.networks[0].ip_address}",
            f"Running LinPEAS On {self.networks[0].ip_address}",
            "Reconnaissance",
            "Phishing Attack",
            "Exploiting Vulnerabilities",
            "Social Engineering Attack",
            "Port Scanning",
            "SQL Injection",
            "Man-in-the-Middle Attack",
            "Extracting Password Hashes",
            "Buffer Overflow Exploit",
            "ARP Spoofing",
            "DNS Spoofing",
            "Brute Force Attack",
            "Denial of Service (DoS) Attack",
            "Session Hijacking",
            "Cross-Site Scripting (XSS)",
            "Reverse Engineering",
            "Remote Code Execution",
            "File Inclusion Attack",
            "DNS Enumeration",
            "SNMP Enumeration",
            "Banner Grabbing",
            "VPN Exploitation",
            "SSL/TLS Exploitation"
        ]

        # List of exiting tasks
        self.exiting_tasks = [
            "Destroying Encryption Keys",
            "Covering Tracks",
            "Disabling Alarms",
            "Cutting Network Connections",
            "Falsifying Audit Trails"
        ]

    def display_networks(self):
        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.LIGHTBLUE_EX}Available Networks\n{'-' * 30}")
        for idx, net in enumerate(self.networks):
            net.security_level = min(10, random.randint(1, 10) + net.tools_level)  # Update security level
            net.base_hackability = net.calculate_hackability()  # Recalculate hackability
            print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}{idx}{Fore.WHITE}] {net}")
            if idx < len(self.networks) - 1:
                print(f"{Fore.WHITE}{'-' * 30}")

    def attack_network(self, ip_address):
        target_network = None
        for network in self.networks:
            if network.ip_address == ip_address:
                target_network = network
                break

        if target_network is None:
            print(f"{Fore.RED}Invalid target IP address.")
            return

        detection_chance = random.random()
        if detection_chance > target_network.calculate_hackability():
            print(f"{Fore.RED}Attack failed. Detected by {target_network.name}.")
        else:
            print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Hacking into {target_network.name}...\n{Fore.WHITE}{'-' * 30}\n")
            max_task_length = max(len(task) for task in self.hacking_tasks)
            max_bar_width = 30  # Maximum width for progress bar
            for task in self.hacking_tasks:
                progress = 0
                task_time = random.uniform(3, 5)
                while progress < 100:
                    progress += random.randint(1, 5)
                    progress = min(100, progress)  # Ensuring progress doesn't exceed 100
                    progress_bar_length = int(progress / 100 * max_bar_width)  # Calculate progress bar length
                    progress_bar = f"{'▧' * progress_bar_length:<{max_bar_width}}"
                    task_info = f"{Fore.LIGHTBLUE_EX}{task.ljust(max_task_length)} | Progress: | {progress_bar} | {progress}%"
                    print(f"\r{task_info}", end='', flush=True)
                    time.sleep(task_time / 100)  # Simulating progress over time
                print()  # Move to the next line after completing the task
            print(
                f"{Fore.WHITE}{'-' * 30}\n{Fore.GREEN}Successfully hacked into {target_network.name}")
            loot = target_network.bank_balance
            self.wallet_balance += loot
            self.stats['total_money_stolen'] += loot
            target_network.bank_balance = 0
            self.hacked_network = target_network  # Set the hacked network
            self.display_exploit_menu_after_hack()  # Display the exploit menu after successful hacking

    def display_exploit_menu_after_hack(self):
        exploit_menu_title = f"{Fore.WHITE}{'-' * 30}\n{Fore.LIGHTBLUE_EX}Exploit Menu | {self.hacked_network.name}\n{Fore.WHITE}{'-' * 30}"
        print(exploit_menu_title)
        print("Choose an exploit to use:\n")
        for idx, (exploit, info) in enumerate(self.upgrades.items(), 1):
            print(
                f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}{idx}{Fore.WHITE}] {exploit.capitalize()} - {info['description']} (Cost: ${info['cost']})")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}R{Fore.WHITE}] Return to Main Menu")

        while True:
            choice = input(f"{Fore.WHITE}{'-' * 30}\n{Fore.WHITE}Enter your choice: ")
            if choice.lower() == 'r':
                return
            elif choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.upgrades):
                    exploit, info = list(self.upgrades.items())[choice - 1]
                    if self.wallet_balance >= info['cost']:
                        self.wallet_balance -= info['cost']
                        self.stats['total_exploit_used'][exploit] += 1
                        self.use_exploit(exploit)
                        return
                    else:
                        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Insufficient funds.")
                else:
                    print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Invalid choice.")
            else:
                print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Invalid choice.")

    def use_exploit(self, exploit):
        if exploit == 'worm':
            print("Scanning for more computers in the network...")
            # Add code here to scan for more computers in the network
            for _ in range(3):
                new_device = Network(f"{random.choice(['Phone', 'Laptop', 'Desktop'])}-{random.choice([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5)])}", random.randint(500, 10000), 1)
                self.networks.append(new_device)
            print("New devices discovered in the network.")
            self.display_network_devices_menu()
        elif exploit == 'virus':
            print("Cracking The Device And Checking For Wallet Credentials...")
            # Add code here to randomly give the player 1-2 upgrades as a reward
            reward = random.randint(1, 2)
            print(f"You've been rewarded with {reward} random upgrade(s).")
            for _ in range(reward):
                upgrade = random.choice(list(self.upgrades.keys()))
                self.upgrades[upgrade]['level'] += 1
                print(f"Upgraded {upgrade.capitalize()} to level {self.upgrades[upgrade]['level']}.")
        elif exploit == 'botnet':
            print(f"Adding {self.hacked_network.name} to botnet...")
            self.botnet.append(self.hacked_network)
            self.stats['botnet_size'] += 1
            # Increase hackability % by 10% for all networks in the botnet
            for network in self.botnet:
                network.base_hackability += 0.1
                print(f"Brute Force Performance increased to {network.base_hackability:} Hashes Per Minute")
        else:
            print(f"{exploit.capitalize()} exploit is not implemented yet.")

    def display_network_devices_menu(self):
        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.LIGHTBLUE_EX}Network Devices\n{Fore.WHITE}{'-' * 30}")
        print("Choose a device to exploit:")
        for idx, device in enumerate(self.networks[len(self.networks)-3:], 1):
            print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}{idx}{Fore.WHITE}] {device.name} - IP: {device.ip_address}")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}R{Fore.WHITE}] Return to Main Menu")

        choice = input(f"{Fore.WHITE}{'-' * 30}\nEnter your choice: ")
        if choice.lower() == 'r':
            return
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(self.networks[len(self.networks)-3:]):
                device = self.networks[len(self.networks)-3:][choice - 1]
                self.exploit_device(device)
            else:
                print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Invalid choice.")
        else:
            print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Invalid choice.")

    def exploit_device(self, device):
        print(f"Exploiting {device.name}...")
        hacking_tasks = [
            "Analyzing network vulnerabilities",
            "Scanning for open ports",
            "Exploiting weak security measures",
            "Gaining access to the target device",
            "Extracting sensitive information"
        ]
        print("Initializing hacking sequence...\n")

        max_task_length = max(len(task) for task in hacking_tasks)
        max_bar_width = 30

        for task in hacking_tasks:
            progress = 0
            task_time = random.uniform(2, 5)
            print(f"{Fore.WHITE}{task}{' ' * (max_task_length - len(task))} | Progress: |", end='')
            while progress < 100:
                progress += random.randint(1, 5)
                progress = min(100, progress)  # Ensuring progress doesn't exceed 100
                progress_bar = f"{Fore.LIGHTBLUE_EX}{'▧' * int(progress / (100 / max_bar_width)):<{max_bar_width}}"
                task_info = f"{Fore.RED}{task.ljust(max_task_length)} | Progress: | {progress_bar} | {progress}%"
                print(f"\r{task_info}", end='', flush=True)
                time.sleep(task_time / 100)  # Simulating progress over time
            print()  # Move to the next line after completing the task

        print(f"{Fore.WHITE}Hacking sequence complete!\n")

        exploit_choice = input("Choose exploit (shutdown, encrypt, money transfer, extort): ")
        if exploit_choice.lower() == 'shutdown':
            print(f"{device.name} has been shut down.")
            # Additional logic can be implemented here if needed
        elif exploit_choice.lower() == 'encrypt':
            num_files = random.randint(1, 10)
            print(f"{num_files} of {device.name}'s files have been encrypted.")
            # Additional logic can be implemented here if needed
        elif exploit_choice.lower() == 'money transfer':
            money = device.bank_balance
            self.wallet_balance += money
            device.bank_balance = 0
            print(f"Transferred ${money} from {device.name} to your wallet.")
        elif exploit_choice.lower() == 'extort':
            print(f"Extorted {device.name}.")
            # Additional logic can be implemented here if needed
        else:
            print("Invalid exploit choice.")

        # Returning to the exploits menu
        self.display_exploit_menu_after_hack()

    def display_menu(self):
        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.LIGHTBLUE_EX}{' ' * 10}Main Menu\n{Fore.WHITE}{'-' * 30}")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}1{Fore.WHITE}] Display Available Networks")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}2{Fore.WHITE}] Attack a Network")
        if self.hacked_network:
            print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}3{Fore.WHITE}] Choose Exploit")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}4{Fore.WHITE}] Upgrade Abilities")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}5{Fore.WHITE}] Display Player Stats")
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}6{Fore.WHITE}] Quit")
        print(f"{Fore.WHITE}Type '{Fore.LIGHTBLUE_EX}Help{Fore.WHITE}' for explanations.")
        print(f"{Fore.WHITE}{'-' * 30}")

    def display_help(self):
        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.LIGHTBLUE_EX}Help Menu\n{'-' * 30}")
        print(f"{Fore.LIGHTBLUE_EX}1. Display Available Networks:")
        print(f"{Fore.WHITE}   Lists all networks available for hacking.")
        print(f"{Fore.LIGHTBLUE_EX}2. Attack a Network:")
        print(f"{Fore.WHITE}   Initiates an attack on a selected network.")
        if self.hacked_network:
            print(f"{Fore.LIGHTBLUE_EX}3. Choose Exploit:")
            print(f"{Fore.WHITE}   Select an exploit to use against the hacked network.")
        print(f"{Fore.LIGHTBLUE_EX}4. Upgrade Abilities:")
        print(f"{Fore.WHITE}   Purchase upgrades to enhance hacking abilities.")
        print(f"{Fore.LIGHTBLUE_EX}5. Display Player Stats:")
        print(f"{Fore.WHITE}   Shows various statistics about the player.")
        print(f"{Fore.LIGHTBLUE_EX}6. Quit:")
        print(f"{Fore.WHITE}   Exit the game.")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_networks()
            elif choice == '2':
                print(f"{Fore.WHITE}{'-' * 30}")
                ip_address = input("Enter the IP address of the network to attack: ")
                self.attack_network(ip_address)
            elif choice == '3' and self.hacked_network:
                self.display_exploit_menu_after_hack()  # Display the exploit menu after successful hacking
            elif choice == '4':
                self.upgrade_abilities()
            elif choice == '5':
                self.display_player_stats()
            elif choice == '6':
                self.exiting = True  # Set the exiting flag to True
                self.display_exiting_progress()
                print(f"{Fore.RED}\nAll Tasks Terminated Successfully . . . Going Dark ")
                break  # Exit the loop when the user chooses to quit
            elif choice.lower() == 'help':
                self.display_help()
            else:
                print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Invalid choice.")



    def display_player_stats(self):
        # List of tasks
        tasks = [
            "Decrypting Drive C:",
            "Analyzing financial records",
            "Calculating total funds acquired",
            "Enumerating successful breaches",
            "Analyzing exploit logs",
            "Detecting botnet connections"
        ]

        # Simulate the operation with a progress bar for each task
        max_task_length = max(len(task) for task in tasks)
        max_bar_width = 30

        print()  # Add a newline before the first task

        for task in tasks:
            progress = 0
            task_time = random.uniform(1, 3)
            print(f"{Fore.LIGHTBLUE_EX}{task}{' ' * (max_task_length - len(task))} | Progress: |", end='')
            while progress < 100:
                progress += random.randint(5, 10)
                progress = min(100, progress)  # Ensure progress doesn't exceed 100
                progress_bar = f"{Fore.RED}{'▧' * int(progress / (100 / max_bar_width)):<{max_bar_width}}"
                task_info = f"{Fore.WHITE}{task}{' ' * (max_task_length - len(task))} | Progress: | {progress_bar} | {progress}%"
                print(f"\r{task_info}", end='', flush=True)
                time.sleep(task_time / 100)  # Simulate progress over time
            print()  # Move to the next line after completing the task

        # Display player stats after completion of the loading bar
        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.LIGHTBLUE_EX}          Player Stats\n{Fore.WHITE}{'-' * 30}")
        print(f"Wallet Balance: ${self.wallet_balance}")
        print(f"Total Money Stolen: ${self.stats['total_money_stolen']}")
        print(f"Total Hacks: {self.stats['total_hacks']}")
        print(f"Total Exploits Used:")
        for exploit, count in self.stats['total_exploit_used'].items():
            print(f"  {exploit.capitalize()}: {count}")
        print(f"Botnet Size: {self.stats['botnet_size']}")

    def display_exiting_progress(self):
        print(f"{Fore.WHITE}{'-' * 30}\n{Fore.RED}Shutting Operation Down\n{Fore.WHITE}{'-' * 30}")
        max_task_length = max(len(task) for task in self.exiting_tasks)
        max_bar_width = 30
        for task in self.exiting_tasks:
            progress = 0
            task_time = random.uniform(2, 5)
            while progress < 100:
                progress += random.randint(1, 5)
                progress = min(100, progress)  # Ensuring progress doesn't exceed 100
                progress_bar = f"{'▧' * int(progress / (100 / max_bar_width)):<{max_bar_width}}"
                task_info = f"{Fore.RED}{task.ljust(max_task_length)} | Progress: | {progress_bar} | {progress}%"
                print(f"\r{task_info}", end='', flush=True)
                time.sleep(task_time / 100)  # Simulating progress over time
            print()  # Move to the next line after completing the task


if __name__ == "__main__":
    print('\n'.join(game_logo))
    starting_sequence()  # Invoke the starting sequence
    game = HackerSimulator()
    game.start()
