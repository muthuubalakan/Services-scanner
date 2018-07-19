#!/usr/bin/env python3
#
##
import socket
import asyncio
import sys
import os
import json

from portchecker import PortChecker


FAILURE = 1
PATH = 'assets/conf.json'


class Scanner(PortChecker):
    """Scanner - Port scanner for Linux-server

    Arguments:
        Host ---> Local host
        total_ports ---> Total no.of ports

    Usage:
        >>>from portscanner import Scanner
        >>>Scanner()
    """

    def __init__(self, host=None, total_ports=None):
        self.data = LoadJson().load_json()
        self.common = self.data.get('common', {})
        self.number = total_ports
        if not (self.number or isinstance(self.number, int)):
            self.number = self.common.get('ports')
            # Total number of ports
        self.host = host
        if not self.host:
            self.host = self.common.get('host')
        self.loop = asyncio.get_event_loop()
        super().__init__(self.data)
        if self.check():
            self.loop.run_until_complete(self.task(self.number))

    async def port_match(self, port_list):

        if not len(port_list) > 0:
            raise Exception("Empty List")

        for port in port_list:
            if not isinstance(port, str):
                port = str(port)
            if not hasattr(PortChecker, 'port_finder'):
                raise AttributeError
            self.port_finder(port)
        return None

    def check(self):
        """Only for localhost"""
        if self.host not in self.data['hosts']:
            sys.stderr.write("Invalid host")
            sys.exit(1)
        return True

    async def run(self, n=None):
        sem = asyncio.Semaphore(1000)
        open_ports = []
        async with sem:
            for port in range(0, n):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                port_availabe = sock.connect_ex((self.host, port))
                if port_availabe == 0:
                    open_ports.append(port)
                sock.close()
            return open_ports

    async def queries(self):
        query_type = str(input("\nFor further details Y/N: "))
        query_type = query_type.upper()
        if query_type != 'Y':
            return False
        return self.query()

    async def task(self, number):
        port_list = await self.run(number)
        print("Port list prepared..")
        await self.port_match(port_list)
        print("\nProcess completed..")
        await self.queries()


class LoadJson:

    """Extract json to dict"""

    def __init__(self):
        self.filename = PATH
        if not self.filename.endswith('.json'):
            sys.stderr.write('Invalid json file')
            sys.exit(FAILURE)

    def is_file(self):
        if not os.path.isfile(self.filename):
            return False
        return open(self.filename)

    def load_json(self):
        data = self.is_file()
        if data:
            return json.load(data)
        return False

if __name__ == '__main__':
    scanner = Scanner()
