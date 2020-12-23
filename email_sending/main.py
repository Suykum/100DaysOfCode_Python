import smtplib
import random
import datetime as dt


if dt.datetime.now().weekday() == 2:
    with open("quotes.txt", encoding='utf-8') as file:
        quotes = file.readlines()
    my_email = "*********@gmail.com"
    password = "***********"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="********@yahoo.com",
                            msg=f"Subject: Motivation\n\n{random.choice(quotes)}")
