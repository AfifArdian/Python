import smtplib
import datetime as dt
import random
from email.message import EmailMessage

now = dt.datetime.now()
weekday = now.weekday()
my_email = "akanoyui9@gmail.com"
password = "dgdwsffmmydqmdkg" # The password is obtained at app password in your account settings

if weekday == 0:
    with open("quotes.txt", encoding="utf-8") as file:
        all_quotes = file.readlines()
        quotes = random.choice(all_quotes)
    print(quotes)

    msg = EmailMessage()
    msg["Subject"] = "Quotes"
    msg["From"] = my_email
    msg["To"] = my_email
    msg.set_content(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)
        connection.close()






# import smtplib
#
# # Use Gmail
# my_email = "akanoyui9@gmail.com"
# password = "dgdwsffmmydqmdkg" # The password is obtained at app password in your account settings
#
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="yuiakano@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")
#     connection.close()
#
# # Use Yahoo
# # my_yahoo = "yuiakano@yahoo.com"
# # password = "" # The password is obtained at app password in your account settings
# #
# # with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
# #     connection.starttls()
# #     connection.login(user=my_yahoo, password=password)
# #     connection.sendmail(from_addr=my_yahoo,
# #                             to_addrs="akanoyui9@gmail.com",
# #                             msg="Subject:Hello\n\nThis is the body of my email.")
# #     connection.close()

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2002, month=8, day=22, hour=2, minute=20, second=59)
#
# print(date_of_birth)