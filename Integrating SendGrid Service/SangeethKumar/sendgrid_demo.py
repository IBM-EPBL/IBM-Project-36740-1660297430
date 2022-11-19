import requests

url = ' https://www.fast2sms.com/dev/bulkV'


message = 'Greeting from Praveen'

numbers = '7708375551, 9345123560'

payload = f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={numbers}'


headers = {
    'authorization' : 'QqbHW076SFDTledzUu4yhiYNIK2tf3LEnkc9Br5ZasOjp1VwxMLsyMZXA8IUPcEbdB6GJgvnDhwFfV2a',
    'Content-Type' : 'application/x-www-form-urlencoded'
}


response = requests.request("POST", url=url, data=payload, headers=headers)

print(response.text)




























# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


# message = Mail(from_email='rishiragul26@gmail.com',
#                 to_emails='rishiragul26@gmail.com',
#                 subject='Sending with SendGrid is Fun',
#                 html_content='<strong> Hello World</strong>')


# # sg = SendGridAPIClient("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")
# # response = sg.send(message)
# # print(response.status_code, response.body)
# try:
#     sg = SendGridAPIClient(os.environ.get('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'))
#     response = sg.send(message)

#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)




# # from_email = Email("aks.praveenkumar2002@gmail.com")
# # to_email = To("aks.praveen2002@gmail.com")
# # subject = "Sending with SendGrid is Fun"
# # content = Content("text/plain", "and easy to do anywhere, even with Python")
# # mail = Mail(from_email, to_email, subject, content)
# # response = sg.client.mail.send.post(request_body=mail.get())
# # print(response.status_code)
# # print(response.body)
# # print(response.headers)