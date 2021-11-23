import re 

f = open("potential-contacts.txt", "r").read()
numbers = re.findall(r'\(?\d{3}\)?-?\d{3}-\d{4}', f)
numbers.sort()
# print(numbers)
email =re.findall(r'[a-z0-9]+@+[a-z0-9]+.[a-z]+', f)
email.sort()

number_content = ''
for num in sorted(numbers):
    number_content += str(num)+"\n"

with open('phone_numbers.txt', 'w+') as file:
    file.write(number_content)

email_content = ''
for ele in sorted(email):
    email_content += str(ele)
    email_content += f'\n'

with open('emails.txt', 'w+') as file:
    file.write(email_content)