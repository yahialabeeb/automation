import re 

f = open("potential-contacts.txt", "r").read()
resn = re.findall(r'\(?\d{3}\)?-?\d{3}-\d{4}', f)
resn.sort()
# print(numbers)
p_numbers = []
[p_numbers.append(x) for x in resn if x not in p_numbers]
number_content = ''
for num in sorted(p_numbers):
    number_content += str(num)+"\n"

with open('phone_numbers.txt', 'w+') as file:
    file.write(number_content)

res =re.findall(r'[a-z0-9_$]+@+[a-z0-9A-z]+[.a-z-]+', f)
res.sort()
email = []
[email.append(x) for x in res if x not in email]

email_content = ''
for ele in sorted(email):
    email_content += str(ele)
    email_content += f'\n'

with open('emails.txt', 'w+') as file:
    file.write(email_content)