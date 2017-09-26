#!/usr/bin/env python3

# Full Linux Support
# Work On All Linux Distros


'''
Copyrights (C) 2017 Youssef Hesham
'''

# Import The Needed Lib
import time
import os
import sys
import shutil
import itertools

name=os.path.basename(__file__)

#checking if the user's operating system is compatible with Obevilion
if os.name!="posix":
 print("ERROR:",name,"isn't compatible with your system yet! - We will notify you about the new releases")
 sys.exit(-1)
#checking if the user Have Unrar And Unzip
for which in ["unrar","p7zip"]:
 if not shutil.which(which):
  print("ERROR:",which,"isn't installed.\nExiting...")
  sys.exit(-1)

#defining the functions
def rc(rf):
 alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#"
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
      print("Password Cracked!:",repr(k))
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
      print("Password Cracked:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   else:
    print("We Are Cracking (rar , zip , 7z) only  \nExiting...")

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
                           NO ONE WILL GIVE YOU FREEDOM
                           YOU TAKE IT!
''')
 print("Obevilion its the Re Writed of the old project (ArchiveMaster)")
 print("OBEVILION")
 print("Updates: now officialy obevilion is the strongest Cracking Script")
 print("Coded By BL4CKvGHOST")
 print("GitHub: https://github.com/BL4CKvGHOST")
 print("Twitter: https://twitter.com/BL4CKvGHOST")
 print("Usage:",name,"[path to rar file]")
 print("Example:","Python3 ",name,"example.zip")
