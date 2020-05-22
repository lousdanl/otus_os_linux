import re
import subprocess


class LinuxInfo:

    @classmethod
    def run_command(cls, request):
        with subprocess.Popen([request], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            result = process.communicate()
            output = result[0].decode()
            error = result[1].decode()
            return output + error

    def get_interface(self):
        request = 'ip addr | grep inet'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_rout(self):
        request = 'ip r | grep default'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_processor(self):
        request = 'cat /proc/cpuinfo'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_processes(self):
        request = 'ps aux'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_list_processes(self):
        request = 'ps aux'
        result = self.run_command(request)
        response = re.findall(r' \d:\d{2} (.+)', result)
        print(response)

    def get_interface_status(self):
        request = 'netstat -i -a'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_service_status(self, service):
        request = f'service {service} status'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_port_status(self, port):
        request = f'netstat -afp {port}'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_package_version(self, package):
        request = f'dpkg -s {package} | grep Version'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_list_files(self, path_to_directory):
        request = f'ls -a {path_to_directory}'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_current_directory(self):
        request = 'pwd'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_core_version(self):
        request = 'uname -r'
        result = self.run_command(request)
        print('Result:\n', result)

    def get_os_version(self):
        request = 'lsb_release -a'
        result = self.run_command(request)
        print('Result:\n', result)
