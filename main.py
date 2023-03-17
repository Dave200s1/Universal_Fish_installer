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

#OpenSUSE.................................................
def runUpdates_SUSE():
  cmd = "sudo zypper ref"
  subprocess.run(cmd,shell=True)
  cmd_upgrade = "sudo zypper update"
  subprocess.run(cmd_upgrade,shell=True)

def addRepo_Thumbleweed():
  cmd = "sudo zypper addrepo https://download.opensuse.org/repositories/shells:fish:release:3/openSUSE_Tumbleweed/shells:fish:release:3.repo"
  subprocess.run(cmd,shell=True)
  print("\n Repo added. ;)")

def addRepo_Leap():
  cmd = "sudo zypper addrepo https://download.opensuse.org/repositories/shells:fish:release:3/15.4/shells:fish:release:3.repo"
  subprocess.run(cmd,shell=True)
  print("\n Repo added. ;)")

def install_FishSchell_SUSE():
  print("\n OpenSUSE Fish-Shell-Installer")
  choose_Version = input("Choose version(Thumbleweed/Leap): ")
  print(choose_Version)
  if choose_Version == "Leap" or choose_Version =="leap":
    print("\n launching Leap-Installer")
    warning()
    install_option = input("choose an option(y/n): ")
    if install_option == "y" or install_option =="Y":
      print("\n default shell will be changed ...")
      addRepo_Leap()
      runUpdates_SUSE()
      cmd_install = "sudo zypper install fish"
      subprocess.run(cmd_install,shell=True)
      changeShell()
    elif install_option == "n" or install_option == "N":
      print("\n default shell will not be changed ; )")
      addRepo_Leap()
      runUpdates_SUSE()
      cmd_install = "sudo zypper install fish"
      subprocess.run(cmd_install,shell=True)   
  elif choose_Version == "Thumbleweed" or  choose_Version == "thumbleweed":
    print("\n launching Thumbleweed-Installer")
    warning()
    install_option == input("choose an option(y/n): ")
    if install_option == "y" or install_option =="Y":
      print("\n default shell will be changed ...")
      addRepo_Thumbleweed()
      runUpdates_SUSE()
      cmd_install = "sudo zypper install fish"
      subprocess.run(cmd_install,shell=True)
      changeShell()
    elif install_option == "n" or install_option == "N":
      print("\n default shell will not be changed ; )")
      addRepo_Thumbleweed()
      runUpdates_SUSE()
      cmd_install = "sudo zypper install fish"
      subprocess.run(cmd_install,shell=True)   

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
  userInput = input("Enter OS(Arch,Solus,OpenSuSe,Ubuntu): ")
  if userInput == "Arch" or userInput =="arch":
    print("\n You have entered: Arch ")
    installFishShell_Arch()
  elif userInput =="Solus" or userInput =="solus":
    print("\n You have entered: Solus")
    installFishShell_Solus()
  elif userInput =="Ubuntu" or userInput =="ubuntu":
    print("\n You have entered: Ubuntu")
    installFishShell_U()
  elif userInput == "OpenSuse" or userInput == "opensuse":
    print("\n You have entered: OpenSUSE")
    install_FishSchell_SUSE()
  else:
    print("\n Error!")
    print("\n invalid Input !!")
  
#main
enterOS_Version()