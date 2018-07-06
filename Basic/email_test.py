'''
2 단계 인증을 사용하는 경우  앱 비밀번호를 생성하여 사용함
구글 계정 --> 2단계인증 --> 앱비밀번호 생성 --> 생성된 16자리 비밀번호를 사용한다.
'''
import smtplib
import mimetypes

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email import encoders
import os

# SMTP server address
smtpHost = "smtp.gmail.com"
senderAddr = "sckim007@gmail.com"
recipientAddr = "sckim007@etri.re.kr"

# Set Directory
dirName = "attach"

# Set file
#fileName = "test.GIF"

# Set text
text = "Test email in python 3.6, file attachment"

# Create MIMEMultipart
msg = MIMEMultipart()

msg['From'] = senderAddr
msg['To'] = recipientAddr
msg['Subject'] = "test email"

# Attach text part
textPart = MIMEText(text)
msg.attach(textPart)

for fileName in os.listdir(dirName):
    pathName = os.path.join(dirName, fileName)
    # 체크 파일 타입
    ctype, encoding = mimetypes.guess_type(pathName)

    #  파일 타입을 확인할 수 없거나 인코딩 혹은 압푹 되었을 때는 'octet-steam'으로 정의함
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    # ctype을 '/'로 나눈다.  splict의 두번째 parameter는 나눌 최대 횟수를 의미함.
    maintype, subtype = ctype.split('/', 1)

    if maintype == 'text':
        print("--------< text >--------", subtype)
        fp = open(pathName, 'rb')
        attachPart = MIMEText(fp.read(), _subtype=subtype, _charset='utf-8')
        fp.close()
        # encode the payload using Base64
        encoders.encode_base64(attachPart)
    elif maintype == 'image':
        print("--------< image >--------", subtype)
        fp = open(pathName, 'rb')
        attachPart = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        print("--------< audio >--------", subtype)
        fp = open(pathName, 'rb')
        attachPart = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        print("--------< other >--------", subtype)
        fp = open(pathName, 'rb')
        attachPart = MIMEBase(maintype, subtype)
        attachPart.set_payload(fp.read())
        fp.close()
        # encode the payload using Base64
        encoders.encode_base64(attachPart)

    # 파일 이름을 msg 헤더로 추가한다.
    attachPart.add_header('Content-Disposition', 'attachment', filename=fileName)
    msg.attach(attachPart)

'''    
# Attach attachment part
fd = open(fileName,'rb')
attachPart = MIMEImage(fd.read())
fd.close()
msg.attach(attachPart)
msg.add_header('Content-Disposition', 'attachment', fileName='test.GIF')
'''

'''
fileFD = open(fileName, 'rb')
filePart = MIMEImage(fileFD.read())
fileFD.close()

# attach
msg.attach(filePart)
msg.add_header('Content-Disposition', 'attachment', fileName='test.GIF')
'''

# SMTP 서버를 이용해 메일을 보낸다.
smtp = smtplib.SMTP(smtpHost, 587)
smtp.ehlo()     # Say hello
smtp.starttls() # TLS 사용
smtp.login("sckim007@gmail.com", "ujxihgdoyxowrbim")    # 계정, 앱비밀번호
smtp.sendmail(senderAddr, [recipientAddr,], msg.as_string())
smtp.quit()