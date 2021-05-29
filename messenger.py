import smtplib

EMAIL = "user"
PASSWORD = "password"


class Messenger:
    def __init__(self):
        self.user = EMAIL
        self.password = PASSWORD

    def send_mail(self, name, instructor, price, page_url):
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=self.user, password=self.password)
            connection.sendmail(
                from_addr=self.user,
                to_addrs=self.user,
                msg=f"{name} by {instructor} is now available for only ${price}\n"
                    f"Click the link below to buy now!\n{page_url}"
            )
