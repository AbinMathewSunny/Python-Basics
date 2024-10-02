"""BAsics of smtplib"""

import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


my_email = os.getenv("my_email")
password = os.getenv("password")
connection = smtplib.SMTP("smtp.gmail.com", port=587)

connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs=my_email,
                    msg="Subject:HEllo\n\n"
                        "HEllO Email Guys")
connection.close()

#or we can do it like this way
"""
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs="abinsunny7013@gmail.com",
                            msg="Subject:HEllo\n\n""HEllO Email Guys")

"""


"""Working with datetime module"""
# import datetime as dt
# now = dt.datetime.now()
#
# year = now.year
# print(year)
# month = now.month
# day = now.weekday()
#
#
# date_of_birth = dt.datetime(year=2003,month=5,day=7)
# print(date_of_birth)