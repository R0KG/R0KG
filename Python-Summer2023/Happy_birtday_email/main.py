import smtplib
import datetime as dt
import random
import unidecode
# jqpeqxxpzszoqwal
my_email = "int1994019@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt",encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
        connection.starttls()
        connection.login(my_email, password="jqpeqxxpzszoqwal")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="approm12@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}".encode("utf-8")
        )