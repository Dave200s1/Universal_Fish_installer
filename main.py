#! /usr/bin/env python3
import subprocess


def warning():
  print("Warning this will set your default shell to fish !\n")
  print("Option 1) If you do not want to set fish as default,press N \n")
  print("Option 2) If you want to change the default shell to fish,press Y")

def changeShell():
  cmdChangeShell = "chsh -s `which fish`"
  subprocess.run(cmdChangeShell, shell=True)

#Arch--------------------------------------------
def runUpdates_A():
  cmd = "sudo pacman -Syu"
  subprocess.run(cmd, shell=True)

def installFishShell_Arch():
  print("\n Arch-Fish-Installer")
  runUpdates_A()
  warning()
  userInput = input("Choose an option: ")

  print(userInput)

  if userInput == "n" or userInput == "N":
    print("Default shell will not be changed ;D")
    cmdInstallShell = "sudo pacman -S fish"
    subprocess.run(cmdInstallShell, shell=True)
  elif userInput == "Y" or userInput == "y":
    print("Changing the shell to Fish")
    print("Remeber you can always switch back by using, chsh -s (which bash)")
    cmdInstallShell = "sudo pacman -S fish"
    subprocess.run(cmdInstallShell, shell=True)
    changeShell()
    print("After everything is done, please restart your pc")
  else:
    print("Error :C")

#Ubunut...............................................
def runUpdates_U():
  cmd = "sudo apt update"
  subprocess.run(cmd, shell=True)
  cmd_upgrade = "sudo apt upgrade"
  subprocess.run(cmd_upgrade, shell=True)

def addRepo():
  cmd ="sudo apt-add-repository ppa:fish-shell/release-3"
  subprocess.run(cmd,shell=True)
  runUpdates_A()

def installFishShell_U():
  print("\n Ubunut-Fish-Installer")
  addRepo()
  warning()
  userInput = input("Choose an option: ")

  print(userInput)

  if userInput == "n" or userInput == "N":
    print("Default shell will not be changed ;D")
    cmdInstallShell = "sudo apt install fish"
    subprocess.run(cmdInstallShell, shell=True)
  elif userInput == "Y" or userInput == "y":
    print("Changing the shell to Fish")
    print("Remeber you can always switch back by using, chsh -s (which bash)")
    cmdInstallShell = "sudo apt install fish"
    subprocess.run(cmdInstallShell, shell=True)
    changeShell()
    print("After everything is done, please restart your pc")
  else:
    print("Error :C")

#Solus-----------------------------------------------------
def runUpdates_S():
  print("\n Solus-Fish-Installer")
  cmd_update ="sudo eopkg ur"
  subprocess.run(cmd_update,shell=True)
  cmd_upgrade ="sudo eopkg upgrade"
  subprocess.run(cmd_upgrade,shell=True)

def installFishShell_Solus():
  runUpdates_S()
  warning()
  userInput = input("Choose an option: ")

  print(userInput)

  if userInput == "n" or userInput == "N":
    print("Default shell will not be changed ;D")
    cmdInstallShell = "sudo eopkg install fish"
    subprocess.run(cmdInstallShell, shell=True)
  elif userInput == "Y" or userInput == "y":
    print("Changing the shell to Fish")
    print("Remeber you can always switch back by using, chsh -s (which bash)")
    cmdInstallShell = "sudo eopkg install fish"
    subprocess.run(cmdInstallShell, shell=True)
    changeShell()
    print("After everything is done, please restart your pc")
  else:
    print("Error :C")
  
#-----------------------------------------------------------------
#Enter your OS-Version
def enterOS_Version():
  userInput = input("Enter OS: ")
  if userInput == "Arch" or userInput =="arch":
    print("\n You have entered: Arch ")
    installFishShell_Arch()
  elif userInput =="Solus" or userInput =="solus":
    print("\n You have entered: Solus")
    installFishShell_Solus()
  elif userInput =="Ubuntu" or userInput =="ubuntu":
    print("\n You have entered: Ubuntu")
    installFishShell_U()
  else:
    print("\n Error!")
  
#main
enterOS_Version()