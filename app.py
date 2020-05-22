import argparse
from linux_info import LinuxInfo

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="request",
                                   help="Введите команду, чтобы получить необходимую информацию")

interface = subparsers.add_parser("interface",
                                  help="Сетевые интерфейсы")
rout = subparsers.add_parser("rout",
                             help="Маршрут по умолчанию")
processor = subparsers.add_parser("processor",
                                  help="Информация о состоянии процессора")
processes = subparsers.add_parser("processes",
                                  help="Информация о процессах")
list_processes = subparsers.add_parser("list_processes",
                                       help="Список всех процессов")
interface_status = subparsers.add_parser("interface_status",
                                         help="Статистика работы сетевых интерфейсов")
service_status = subparsers.add_parser("service_status",
                                       help="Статус работы сервиса")
service_status.add_argument("service",
                            help="Статус работы определенного сервиса")
port_status = subparsers.add_parser("port_status",
                                    help="Состояние сетевого порта на сервере")
port_status.add_argument("port",
                         help="Состояние сетевого порта на сервере (TCP или UDP)",
                         choices=["upd", "tcp"])
package_version = subparsers.add_parser("package_version",
                                        help="Версия пакета")
package_version.add_argument("package",
                             help="Версия пакета (имя пакета передается как аргумент)")
list_files = subparsers.add_parser("list_files",
                                   help="Список файлов в директории (указать директорию)")
list_files.add_argument("path_to_directory",
                        help="Путь до директории")
current_directory = subparsers.add_parser("current_directory",
                                          help="Текущая директория")
core_version = subparsers.add_parser("core_version",
                                     help="Версия ядра")
os_version = subparsers.add_parser("os_version",
                                   help="Версия операционной системы")

args = parser.parse_args()
request = args.request

info = LinuxInfo()

if request == "interface":
    info.get_interface()
elif request == "rout":
    info.get_rout()
elif request == "processor":
    info.get_processor()
elif request == "processes":
    info.get_processes()
elif request == "list_processes":
    info.get_list_processes()
elif request == "interface_status":
    info.get_interface_status()
elif request == "service_status":
    info.get_service_status(args.service)
elif request == "port_status":
    info.get_port_status(args.port)
elif request == "package_version":
    info.get_package_version(args.package)
elif request == "list_files":
    info.get_list_files(args.path_to_directory)
elif request == "current_directory":
    info.get_current_directory()
elif request == "core_version":
    info.get_core_version()
elif request == "os_version":
    info.get_os_version()
