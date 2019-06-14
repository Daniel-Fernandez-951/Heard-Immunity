import requests
import random
from fake_headers import Headers
from termcolor import colored
from faker import Faker

count = 0

while True:
        fake = Faker()

        url = ''

        email = fake.email()
        name = fake.name()
        address = fake.address()
        occupation = fake.job()
        phone = fake.phone_number()
        dob = fake.date_of_birth(tzinfo=None, minimum_age=9, maximum_age=86)

        fdata = {"customer_name": name,
                 "address": address,
                 "occupation": occupation,
                 "phone_number": phone,
                 "email_address": email,
                 "dob": dob
                 }


        header = Headers(headers=False)
        headers = header.generate()

        s = requests.Session()
        r = s.post(url, data=fdata, headers=headers)

        response = str(r)
        rcode = response[11:14]

        def status_check():
            if rcode == "200":
                count = count + 1
                return(colored('\n\nData dumped! \t\t %s \t %s ' % (rcode, count), 'green', attrs=['bold']))
            else:
                return(colored('\n\nNo Success \t\t %s \n ' % rcode, 'red', attrs=['bold']))

        status = status_check()

        print(status, '\n', name, '\n', dob, '\n', email, '\n', phone, '\n', occupation, '\n', address, status)
