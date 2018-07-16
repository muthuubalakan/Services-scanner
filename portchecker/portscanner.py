#!/usr/bin/env python3
#
##
import socket
import asyncio
from portchecker import PortChecker


checker = PortChecker()


async def scan(r):
    """Return list of listenting ports"""
    # localhost for your local machine
    host = "localhost"
    open_ports = []
    for port in range(0, r):
        # TCP socket connection
        # Attempts connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_availabe = sock.connect_ex((host, port))
        if port_availabe == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


async def port_match(port_list):
    for port in port_list:
        if not isinstance(port, str):
            port = str(port)
        checker.port_finder(port)


async def queries():
    """Return detailed info about ports

    Recommended for only get addtional info about pre-assigned port
    """
    query_type = str(input("\nFor further details, Please enter Yes or Y: "))
    query_type = query_type.upper()
    if not query_type == 'YES' or 'Y':
        # Call
        return False
    return checker.query()


async def task():
    # Create task
    # line up asyncio tasks
    number = 22263
    # wait until get the portlist
    port_list = await scan(number)
    print("Port list prepared..")
    await port_match(port_list)
    print("\nProcess completed..")
    await queries()

# initiate loop.
loop = asyncio.get_event_loop()
loop.run_until_complete(task())
