#!/usr/bin/env python3

# Coded By Digital Gangstars
# Follow Our WebSite: http://www.digitalgangstar.ga
# BL4CKvGHOST - D3S7R0Y3R - DIAX - T0Xic
# MADE IN EGYPT  :)
# Kali Linux Support
# Parrot OS sec support
# Debian systems Support
# Ubuntu Systems Support
# Linux Mint Support
# Archive FIles Files Bruiteforcer
##it cracks zip and 7z too
###Python3 file
#####################################################################
############### Digital Gangstars License ###########################
#####################################################################
# Import The Needed Lib
import time,os,sys,shutil,itertools

name=os.path.basename(__file__)

#checking if the user's operating system is compatible with OBIVELION
if os.name!="posix":
 print("ERROR:",name,"isn't compatible with your system.")
 sys.exit(-1)
#checking if the user Have Unrar And Unzip
for which in ["unrar","p7zip"]:
 if not shutil.which(which):
  print("ERROR:",which,"isn't installed.\nExiting...")
  sys.exit(-1)

# defining the functions
def rc(rf):
 alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#*+-*"
 start=time.time()
 tryn=0
 for a in range(1,len(alphabet)+1):
  for b in itertools.product(alphabet,repeat=a):
   k="".join(b)
   if rf[-4:]==".rar":
    print("Trying:",k)
    kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="All OK\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   elif rf[-4:]==".zip" or rf[-3:]==".7z":
    print("Trying:",k)
    kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="Everything is Ok\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   else:
    print("We Are Cracking (rar , zip , 7z) only , Do Not Be Idiot\nExiting...")

# Check That The File Already Exists . Then Run The File
if len(sys.argv)==2:
 if os.path.exists(sys.argv[1]):
  rc(sys.argv[1])
 else:
  print("Check The File Again! , The File Not Exist.\nExiting...")
else:
 print('''
████▄ ███   ▄███▄      ▄   ▄█ █    ▄█ ████▄    ▄
█   █ █  █  █▀   ▀      █  ██ █    ██ █   █     █
█   █ █ ▀ ▄ ██▄▄   █     █ ██ █    ██ █   █ ██   █
▀████ █  ▄▀ █▄   ▄▀ █    █ ▐█ ███▄ ▐█ ▀████ █ █  █
      ███   ▀███▀    █  █   ▐     ▀ ▐       █  █ █
                      █▐                    █   ██
                      ▐
''')
 print("Obevilion its the Re Writed of the old project (ArchiveMaster)")
 print("OBEVILION")
 print("Now Support Sympols")
 print("Coded By Digital Gangstars (Leader:BL4CKvGHOST)")
 print("GitHub:https://github.com/BL4CKvGHOST")
 print("Blog:http://www.digitalgangstar.ga")
 print("Usage:",name,"[rar file]")
 print("Example:",name,"example.rar")
