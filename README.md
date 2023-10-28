# Overview

This is my Chat Room Program! In this project I am attempting to further my knowledge of Networking as it relates to the Python Programming Language. Also to further my knowledge of working
with threads as well as python packages. 

As stated above the program itself is a Chat Room, the vide below goes into more description on the dtails of the program, but eseentially it utilizes the Client/Server model, meaning that one aspect of the program is a server, meaning it provides a service, in this case a Chat Room, which can be accessed by clients requesting that service, in this case getting into the chat room. The Chat Room itself uses TCP or Transmission Control Protocol. This means that the Program itself relies on the reliability of its connection and the data being transfered. Data is delivered and displayed in order.

The purpose in writing this software was to explore the main conecpts behind networking within the scope of programming, and to further devlop my skills as a software developer and engineer.

[Software Demo Video](https://youtu.be/H4tPrKJFBEw)

# Network Communication

The Architecture that I used in my Program was Clint/Server Architecture, so in essence a server which provides a service, in this case a Chat Room, and clients which request that service, in this case entry to the Chat Room and method of communication with their peers. 

In the case of this program I am using the mostly widly used of the two, namley TCP, because the program itself relies on the integrity and timley delivery of data from the user to the server, so between TCP and UDP, TCP is more practical in this application. The port which I used was 6622 for both the server and the client.

In the case of the Chat Room Program the Format utilized would be text-based with timestamp, a name, and then the raw text communicated to the server,a dn recommunicated to the other clients on the chat bot.

# Development Environment

The tools which I utilized to develop my Chat Room was VScode, and the Python Language with include libraries. 

Python is an extremly useful language when it comes to Networking. It includes both server and socket libraries, but in the case of my program I only utilized the socket library from the python package. As stated before Python is extremly useful in this regard becasue th built in packages allow for the automation of networking within the broader scope of the language itself.

# Useful Websites

* [Real Python - Sockets](https://realpython.com/python-sockets/)
* [Transmission Control Protocol (TCP)](https://www.geeksforgeeks.org/what-is-transmission-control-protocol-tcp/#)
* [User Datagram Protocol](https://www.geeksforgeeks.org/user-datagram-protocol-udp/)
* [Threading](https://www.geeksforgeeks.org/multithreading-python-set-1/)
* [Daemon Threads](https://www.geeksforgeeks.org/python-daemon-threads/)

# Future Work

* Fix Thread communication and ending so that it doesn't display error when users exit Chat Room
* Delve more into number of threads available to be utilized by the server (how many users can it handle?)
* Support for more requests