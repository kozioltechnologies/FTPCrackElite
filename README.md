# FTPCrackElite

FTPCrackElite(FTPCE) is an open source ftp cracking tool that uses mutliple techingiques to crack ftp servers. FTPCE offers
a wide variety of tools to test the secuirty of your ftp server. The tool-kit is broken down into diffrent modules or tools. These tools can 
be used to crack a ftp server. To start cracking ftp you must start the program. FTPCE uses Python 2.7, when running on ubuntu machine run command in the saved folder of the program:
```
python ftpce-0.1.py
```
Once the program is booted and you agree to the terms of service you must then choose a module to running the command
```
list
```
This command shows all of the modules that are loaded in the ftpce toolkit. Once you have choosen the module you want to use type the command
```
load
```
Once enter you are prompted to enter the name of the module you wish to load.
# BruteForce Module

Once you select this moudule you must set the host address, the port, the username which you want to bruteforce and the password technique in which you want to brute force.
                                                               Command to set host:
```
set host
enter
"HOST"
enter

```

Command to set Port:

```
set port
enter
"port"
enter

```

Command to set User:

```
set user
enter
"username"
enter

```

Command to set Password Crack Style:

```
set password
enter
"You can select #1 for a word list and #2 for random passwords"
enter
"If you selected #1 you will be prompted to enter the location of the wordlist.txt and if you selected #2 you will enter the length of the password

```
To begin the crack
```
exploit
```

Once the password has been found the program will stop and print the username and password.

# Anonymous account checker

In some FTP servers, there is a anonymous account that is active that was created by default and not deleted by the admin. This module is very simple, ones started it asks for the host address of the server and the port of the server. Then it tries to find if indead the anonymous account is active, and if the account is active it will print the username and password of it.

# FTP Connect(Beta)

This module allows you to connect to a ftp server and then upload or download a file. Once the module is loaded you must enter in the 

```
Host
Port
Username 
Password
Directory of the ftp
```
Once finished entering the ftp server information you will be connected to the ftp server and in a position where you will be able to upload and
download files off of the server 
Command to download:

```
Download
```
To download you must provide the filename of which you want to download
Command to upload:
```
Upload
```
To upload you must provide the filename to upload
