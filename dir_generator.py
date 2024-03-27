#!/usr/bin/env python3
import os
import sys
import argparse
from dir_names import directoryDict
import datetime
from os.path import expanduser

# Colors & Font Options
C_GREEN = "\033[1;32m"
C_RED = "\033[1;31m"
C_RESET = "\033[0m"
C_WHITE = "\033[1;37m"
C_YELLOW = "\033[1;33m"
BOLD = "\033[1m"

# Ascii banner
def print_banner():
    ascii_art = f"{C_GREEN}"
    ascii_art += """
    ____  _         ______                           __            
   / __ \(_)____   / ____/__  ____  ___  _________ _/ /_____  _____
  / / / / / ___/  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / /_/ / / /     / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_____/_/_/      \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                                   
    """
    ascii_art += f"{C_RESET}"
    print(ascii_art)

# Prints Banner
print_banner()

# Help and Args Options
cli_parser = argparse.ArgumentParser(description="A simple script to generate testing directories.")
cli_parser.add_argument('-n', help='Supply Engagement name', required=True)
cli_parser.add_argument('-m', help='Supply comma separated methodologies (options are {})'.format(' '.join(directoryDict.keys())))

args = cli_parser.parse_args()
methodologies = []

if args.m:
    methodologies = args.m.split(',')
    for methodology in methodologies:
        if methodology not in directoryDict.keys():
            sys.stderr.write(f"{BOLD}{C_RED}[*] Warning: {C_RESET}{BOLD}{methodology}{C_RED} is not an allowed methodology,{C_RESET} see --help menu\n")
            sys.exit(1)
else:
    methodologies = directoryDict.keys()

# Main Prog
try:
    if args.n: # verify engagement name is set
        home = expanduser("~")
        date = datetime.datetime.now().strftime("-%b-%d-%Y")
        if sys.platform != "linux":
            engagement_dir = f"C:\\Pentests\\Engagements\\{args.n}{date}" # change the this path to suit your use case if using windows or you want it in a specific place.
        else:
            engagement_dir = f"{home}/{args.n}{date}"
        if not os.path.exists(engagement_dir):
            print(f"{BOLD}[*] Creating Engagement Directories...{C_RESET}")
            os.makedirs(engagement_dir) # Make root directory
            for methodology in methodologies:
                os.makedirs(f"{engagement_dir}/{methodology}") # Create methodology directories
                for output in directoryDict[methodology]:
                    os.makedirs(f"{engagement_dir}/{methodology}/{output}") # Create tool directories
            print(f"{BOLD}{C_GREEN}[*] {engagement_dir} successfully created{C_RESET}") # Success message showing path & new dir
            print()
        else:
            print(f"{BOLD}{C_YELLOW}[*] Warning: {engagement_dir} already exists. Choose another name.{C_RESET}") # Warning message
            print()
except KeyboardInterrupt:
    sys.exit(0)
