import smtplib
import email.message
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


# # 보안때문에 STMP_SSL을 요구함
# # 아무나 접근할 수 없게끔
# smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
# print(smtp)

# print(smtp.login("sangmin3285@gmail.com",""))


# 메세지
email_msg = EmailMessage()
email_msg.set_content('내 이름은 이상민이다.')


email_msg["Subject"] = "이것은 제목입니다."
email_msg["From"] = "leesangmin3285@gmail.com"
email_msg["To"] = 'sangmingsang@gmail.com'

with open('C:\\workspace\\Basic_python\\Advanced_python\\이두희;.jpg', 'rb') as f:
    img_file  = f.read()

img_type = imghdr.what('이두희;', img_file)
email_msg.add_attachment(img_file, maintype='image', subtype='jpg')

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("sangmin3285@gmail.com","vj7509pt-=+")


# 정규표현식으로 유효성 검사 하기
req = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.+[a-zA-Z]{2,3}$"
# print(re.match(req,'sangmin3285@gmail.com'))

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(email_msg)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


if bool(re.match(req,'sangmin3285@gmail.com')):
    smtp.send_message(email_msg)
    print('정상적으로 메일이 발송되었음')
else:
    print('유효한 이메일 주소가 아님')


sendEmail('sangmin3285@gmail.com')



# 메일 보내는 것
#  이걸 쓰려면 메일 보낼 내용이 필요해
# smtp.send_message(email_msg, )
smtp.quit()