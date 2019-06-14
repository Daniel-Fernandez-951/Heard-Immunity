import requests
import random
from fake_headers import Headers
from termcolor import colored
from faker import Faker

fake = Faker()
url = ''

def makeFakeform():
    email = str(fake.email())
    name = str(fake.name())
    address = str(fake.address())
    occupation = str(fake.job())
    phone = str(fake.phone_number())
    dob = str(fake.date_of_birth(tzinfo=None, minimum_age=9, maximum_age=86))

    fdata = {"customer_name": name,
             "address": address.replace('\n', ' '),
             "occupation": occupation,
             "phone_number": phone,
             "email_address": email,
             "dob": dob
             }
    return(fdata)
data = makeFakeform()

header = Headers(headers=False)
headers = header.generate()

s = requests.Session()
r = s.post(url, data=data, headers=headers)

response = str(r)
rcode = response[11:14]

def status_check():
    if rcode == "200":
        return(colored('\n\nData dumped! \t\t %s ' % rcode, 'green', attrs=['bold']))
    else:
        return(colored('\n\nNo Success \t\t %s \n ' % rcode, 'red', attrs=['bold']))



status = status_check()

print(status, '\n', name, '\n', dob, '\n', email, '\n', phone, '\n', occupation, '\n', address, status)



'''
Multithreading A Python Program:

    import sys
    import subprocess

    procs = []
    for i in range(86):
        proc = subprocess.Popen([sys.executable, 'task.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
        procs.append(proc)

    for proc in procs:
        proc.wait()



'''
# https://docs.python.org/3/library/subprocess.html
        # .communicate() get errors, output
