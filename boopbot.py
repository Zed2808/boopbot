#!/usr/bin/python

import socket
import sys

server = 'irc.twitch.tv'
channel = 'dudeofa'
botnick = 'ZedBot2808'
botpass = 'oauth:l52pfcfw0ylokylxcdtgr4ef46vpilx'

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting to ' + server)
irc.connect((server, 6667))
#irc.send(('USER ' + botnick + ' ' + botnick + ' ' + botnick + ' :I am BoopBot!\n').encode('UTF-8'))
irc.send(('PASS ' + botpass + '\n').encode('UTF-8'))
irc.send(('NICK ' + botnick + '\n').encode('UTF-8'))
#irc.send(('PRIVMSG nickserv :iNOOPE\r\n').encode('UTF-8'))
irc.send(('JOIN ' + channel + '\n').encode('UTF-8'))

while True:
    text = irc.recv(2040)
    print(text.decode('UTF-8'))

    if text.find(('PING').encode('UTF-8')) != -1:
        irc.send(('PONG ' + str(text).split()[1] + '\r\n').encode('UTF-8'))

    if text.find((':!boop').encode('UTF-8')) != -1:
        irc.send(('PRIVMSG ' + channel + ' :Beep boop! \r\n').encode('UTF-8'))

    if text.find((':!greet').encode('UTF-8')) != -1:
        t = text.split((':!greet').encode('UTF-8'))
        to = t[1].strip()
        irc.send(('PRIVMSG ' + channel + ' :Hello ' + to.decode('UTF-8') + '! \r\n').encode('UTF-8'))

    if text.find((':!songoftheday').encode('UTF-8')) != -1:
        song = open('song.txt').read()
        irc.send(('PRIVMSG ' + channel + ' :The song of the day is ' + song + ' \r\n').encode('UTF-8'))
