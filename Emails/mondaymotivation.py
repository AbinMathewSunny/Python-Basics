import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv
load_dotenv()


my_email = os.getenv("my_email")
password = os.getenv("password")


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quot_file:
        all_quotes = quot_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
