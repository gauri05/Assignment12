import psutil
import os
import time
import sys


def ProcessDisplay(data):
    listprocess = []
    flag = False
    data = data + ".exe"

    for proc in psutil.process_iter():
        # print (data.lower())

        if data.lower() in proc.name().lower():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                flag = True
                listprocess.append(pinfo)
                print (flag)



            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    if flag == False:
        print ("data does not exits")
    return listprocess


def main():
    # listprocess = []
    if len(sys.argv) != 2:
        print("Error : Invalid number of arguments")
        exit()
    if sys.argv[1] == "-h" or sys.argv[1] == "_H":
        print("This Script is used to traverse specific diretory and display checksum of files")
        exit()
    if sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage : Applicationname AbsolutePath_of_Directory Extention")
        exit()

    path = os.getcwd()
    file = "Log"
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    # print(exits)
    dups = {}

    if not os.path.exists(file):
        try:
            os.mkdir(file)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(file, " file %s.log" % (time.time()))
    f = open(log_path, 'w')

    print("Design automation script which accept process name and display information of that process if it is running:")
    listprocess = ProcessDisplay(sys.argv[1])
    # print(listprocess)
    for elem in listprocess:
        # print(elem)
        f.write(str(elem))
        f.write("\n")
    f.close()


if __name__ == "__main__":
    main()
