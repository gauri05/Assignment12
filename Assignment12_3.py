import psutil
import os
import time
import sys



def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])

            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

def main():

    if len(sys.argv) != 2:
        print("Error : Invalid number of arguments")
        exit()
    if sys.argv[1] == "-h" or sys.argv[1] == "_H":
        print("This Script is used to traverse specific diretory and display checksum of files")
        exit()
    if sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage : Applicationname AbsolutePath_of_Directory Extention")
        exit()

    path= os.getcwd()
    dirnm=sys.argv[1]
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    # print(exits)
    dups = {}

    if not os.path.exists(dirnm):
        try:
            os.mkdir(dirnm)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(dirnm, " file %s.log" % (time.time()))
    f = open(log_path, 'w')

    print("Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username. :")
    listprocess = ProcessDisplay()
    #print(listprocess)
    for elem in listprocess:
        #print(elem)
        f.write(str(elem))
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()
