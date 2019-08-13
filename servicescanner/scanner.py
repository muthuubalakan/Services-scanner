#!/usr/bin/env python3
# coding: utf-8
import socket
import asyncio
import sys
import os
import json
import logging
import psutil


assert sys.platform == 'linux', (
    'LINUX WANTED!.'
    f'No {sys.platform} support'
)


FAILURE = 1
PORT_MAX = 65535
SUCCESS = 0


class Services:
    def processes(self):
        res = []
        for process in psutil.process_iter():
            obj = {"name": process.name()}
            conn = process.connections()
            for c in conn:
                obj["port"] = c.laddr.port
            res.append(obj)
        return res


class ProtocolChecker:
    
    @property
    def read_proto(self):
        with open('/etc/services', 'r') as f:
            return f.readlines()

    def query(self):
        query = yield
        if not query:
            return None
        for line in self.get_data():
            yield line
            

    def file_to_dict(self):
        result = {}
        for line in self.read_proto:
            word = line.split()[:2]
            word = [x.strip('\x00') for x in word]
            i = iter(word)
            data = dict(zip(i, i))
            if data == {}:
                del data
            elif '#'in data.keys():
                del data
            elif '#>'in data.keys():
                del data
            else:
                for key,  value in data.items():
                    result[key] = value
        return result

    def port_finder(self, service):
        port_number = service.get('port')
        name = service.get('name')
        result = self.file_to_dict()
      
        for key, value in result.items():
            ports_ip = value.split('/')
            if ports_ip[0] == str(port_number):
                print(name + " " * 30 + str(port_number) + " "*30 +  ports_ip[1].upper() + " "*30 +   key.upper() + "\n")



class Scanner:
    
    
    class TCPConnection:
        
        def __init__(self):
            self.family = socket.AF_INET   # Use it for debugging.
            self.type = socket.SOCK_STREAM
            self.sock = socket.socket(self.family, self.type)
        
        def __repr__(self):
            return 'TCPConnection(socket={})'.format(self.sock)
        
        async def __aenter__(self):
            return self.sock
            
        async def __aexit__(self, *args):
            self.sock.close()
            
            
    def __init__(self):
        self._host = '127.0.0.1'
        self.loop = asyncio.get_event_loop()

    async def port_match(self, port_list):
        if not port_list:
            sys.stdout("No open ports.")
            sys.exit(SUCCESS)
        
        assert hasattr(self, 'port_finder'), (
            'Need `port_finder`'
        )
        print("Service" + " "*30 + "Port" + " "*30 + "Protocol" + " "*30+  "Type" + "\n\n")
        s = Services()
        running_services = s.processes()
        
        all_services = []
        for service in running_services:
            for port in port_list:
                if service.get('port') == port:
                    all_services.append(service)
                    

        for service in all_services:        
            self.port_finder(service)


    async def run(self, n=None):
        sem = asyncio.Semaphore(1000)
        open_ports = []
        async with sem:
            for port in range(0, n):
                async with self.TCPConnection() as connection:
                    port_number = connection.connect_ex((self._host, port))
                    if port_number == 0:
                        open_ports.append(port)
            return open_ports
    
    async def task(self, max):
        port_list = await self.run(max)
        await self.port_match(port_list)
        await self.ports_protocols()
    
    async def ports_protocols(self):
        pass
    
    @property
    def scan(self):
        self.loop.run_until_complete(self.task(PORT_MAX))
        


class TCPScanner(Scanner, ProtocolChecker):
    """Base class"""
    pass
