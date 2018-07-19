import sys
import os

PLATFORM = 'linux'


class PortChecker:
    """PortChecker version 0.0.2

    Argument:
        filename ---- >> configuration path

    Usage:
        PortChecker(path)
    """
    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        # return read file object
        data = self.filename
        path = data.get('filename', {}).get('path')
        filename = data.get('filename', {}).get('file_')
        filename = path + '/' + filename
        if not self.is_file(filename):
            platform = sys.platform
            if platform != PLATFORM:
                sys.stderr.write("Only runs on Linux\n")
                sys.exit(1)
            files = os.listdir("/etc")
            for f in files:
                if 'services' in f:
                    filename = "/etc/"+f
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
