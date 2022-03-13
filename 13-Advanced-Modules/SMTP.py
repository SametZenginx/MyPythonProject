import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart
"""
mesaj["From"] = "Sametzengin4343@gmail.com"

mesaj["To"] = "coskun.m.murat@gmail.com"

mesaj["Subject"] = "Smtp'den mail"

"""



yazi = """

SMTP ile mail gonderiyorum... Ders gayet akıcı ve güzel gidiyor.
Umarım kendimi geliştirebilirim. Sevgilerle...

Mustafa Samet Zengin

"""

mesajGovdesi = MIMEText(yazi,"plain")

mesaj.attach(mesajGovdesi) #Mesaja mesaj gövdemizi attık.

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo() #Smtp serverine baglaniyoruz.

    mail.starttls() #Mutlaka kullanmaliyiz. #Sifrelenmesi icin.

    mail.login("","") #Gmail ve password gir.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail basariyla gonderildi.")

    mail.close()

except:
    sys.stderr.write("Bir Sorun Olustu...")
    sys.stderr.flush
    



    




