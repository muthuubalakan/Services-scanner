#
# Neccessary modules
import os
import json

__all__ = ['PortChecker']


class PortChecker:
    """Return port information

    PortChecker list out all assigned ports in Linux-machine.

    PortChecker.port_finder() gives the open port with details
    other arguments:
        query provides additional information about port assignment.
    """

    def load_json(self):
        # Use configuration file
        # predefine
        data = open("conf.json")
        data = json.load(data)
        return data

    def get_data(self):
        # return read file object
        data = self.load_json()
        path = data.get('filename', {}).get('path')
        filename = data.get('filename', {}).get('file_')
        filename = path + '/' + filename
        if not self.is_file(filename):
            return False
        read_file = open(filename, 'r')
        return read_file

    def is_file(self, filename):
        # make sure file is located on local machine.
        if not os.path.isfile(filename):
            return False
        return True

    def query(self):
        """For additional info about ports

        verify port assignment.
        Read port vulnerability and secure ports.
        """
        for line in self.get_data():
            print(line)
        return False

    def file_to_dict(self):
        # Unnecessary checkups, Remove it if it doesn't make any sense.
        if not self.is_file:
            files = os.listdir("/etc")
            for file_ in files:
                if 'service' in file_:
                    print("Possible file >>>", file_)

        filename = self.get_data()
        result = {}
        # Slicing data
        for line in filename:
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

    def port_finder(self, port_number):
        """Return list of open ports"""

        result = self.file_to_dict()
        for key, value in result.items():
            # Every ports has predefined protocols
            # Make sure that it is not fallacious
            ports_ip = value.split('/')
            if ports_ip[0] == port_number:
                print("\n")
                print("OPEN PORT: {}".format(port_number))
                print("--------------------------")
                print("PORT {} DETAILS: \n"
                      "--------------------------\n"
                      "PORT: {} \n"
                      "INTERNET PROTOCOL: {} \n"
                      "PORT TYPE: {}"
                      .format(port_number,
                              port_number,
                              ports_ip[1].upper(),
                              key.upper()))
