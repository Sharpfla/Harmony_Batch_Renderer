import subprocess
from api.config import Config as cfg 
import api
from api.functions import render_latests

def prompt_YN(base_text="Select an Option?"):
    answered = False
    choice = None
    while not answered:
        ans = input(base_text+" (Yy/Nn)\n")
        choice = ans.strip().lower()
        if choice in ["y","n"]:
            answered = True 
    return choice == "y"
def prompt_list_select(options= ["A", "B", "C"], default=0, base_text="Enter a number to select "):
    answered = False
    choice = default
    while not answered:
        print(base_text + f" (default = {options[default]})")
        for i, op in enumerate(options):
            print(f"{i}) {op}")
        choice = int(input(" "))
        if choice > len(options):
            print("Invalid input")
        else:
            answered = True
    return options[choice]

print("Welcome to the batch render!")
print(cfg.SEARCH_DIR)
UPDATE_SEARCH_DIR = prompt_YN("Would you like to change the search directory")

if UPDATE_SEARCH_DIR == True:
    print("updated")

cfg.SELECTED_HARMONY_VERSION = prompt_list_select(base_text = "Which version of Harmony would you like to render from?",  options= ["V20", "V21", "V21.1", "V22"])

render_latests(cfg)