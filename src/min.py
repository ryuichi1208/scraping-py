import requests
res = requests.get('https://tonari-it.com';)
#print(res.text)
with open('tonari-it.html', 'w') as file:
    file.write(res.text)

    
