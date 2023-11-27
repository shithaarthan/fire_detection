import main
from os import system

system('clear')
val = int(input("send threat mail(0 for no/1 for yes) : "))
if val == 1:
   main.fireThreatMsg()