from colorama import init, Fore, Back, Style
from termcolor import colored


init()  # for Windows
print(Fore.RED + "Hello CodesDope")
print(Back.GREEN + "Hello Again")

print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")

# then use Termcolor for all colored text output
print(colored("Hello, World!", "green", "on_red"))
