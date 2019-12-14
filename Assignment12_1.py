import psutil
import os
import time



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






    path= os.getcwd()
    file="Log"
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

    print("Design automation script which display information of running processes as its name, PID,Username:")
    listprocess = ProcessDisplay()
    #print(listprocess)
    for elem in listprocess:
        #print(elem)
        f.write(str(elem))
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()
