import sys
import os
import threading as th


#Defining the main function

def DIRB(domain):
    os.system(f"dirb https://{domain}")


def THREADING():

    #Reading lines from the specified file

    with open(sys.argv[1],'r') as file:
        lines = file.readlines()

    threads = []

    #Limiting the number of threads to specified

    semaphore = th.Semaphore(int(sys.argv[2]))

    for line in lines:
        domain = line.strip()

        semaphore.acquire()

        thread = th.Thread(target=DIRB, args=(domain,))
        thread.start()
        threads.append(thread)

    #Making the threads execute concurrently

    for thread in threads:
        thread.join()


print()
print(f"USING {sys.argv[2]} THREADS..")


THREADING()
