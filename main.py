import requests
import pyfiglet

banner = pyfiglet.figlet_format("UShorten")

readme = """
Hello, this is the text contained in the readme. It's really just some disclaimers and information about the program.
This is a python program working with the Bitly API to provide fast link shortening.

Although it requires a username and password to work correctly, it does not store this information.
It also does not store any links entered OR shortened versions of the original links.

One more thing to keep in mind: Bitly sets an amount of links that can be generated for each account.
The limit for a free account is 1,000 links.

Thanks for using and feel free to suggest changes or improvements.



- Brendan McKenney
"""
intro_text = """
Enter your Bitly credentials and then any URL to shorten it!

Contact me at www.brendanmckenney.com or at brendanmckenney@gmail.com.

Thanks!




Enter "Shorten!" to get started:

Or type "readme" to read the readme text.


"""
print(banner)
print(intro_text)

# Bitly account creds
username = "brendanmckenney"
passwd = "Bobcats0114"

while True:
    choice = input()
    if choice = "readme":
        print(readme)
        print("Shorten a link now? Type 'Shorten!'")
        choice = input()
        if choice == "Shorten":
            continue
        else:
            print("Thanks!")
            break

    if choice == "Shorten!":
        #Bitly account credentials input
        print("Please input your Bitly username:")
        username = input()
        print("Now enter your Bitly password:")
        passwd = input()

        # Retrieve/check access token
        auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, passwd))
        if auth_res.status_code == 200:
            access_token = auth_res.content.decode()
            print("Retrieving access token....")
            print("Retrieved access token: ", access_token)
        else:
            print("Couldn't get access token. :( Please check your credentials.")
            exit()


    headers = {"Authorization": f"Bearer {access_token}"}
# Reteive/check GUID
    groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
    if groups_res.status_code == 200:
        groups_data = groups_res.json()['groups'][0]
        guid = groups_data['guid']
    else:
        print("Couldn't get GUID. Check your credentials/bitly account.")
        exit()

#Shortening
    print("Now enter the link you want to shorten: ")
    url = input()
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
    link = shorten_res.json().get("link")
    print("Getting shortened link...")
    print("One second........")
    print()
    print()
    print("Shortened URL: ", link)

    while True:
        answer = str(input('Shorten another link? (y/n): '))
                    if answer in ('y', 'n', 'Y', 'N'):
                break
            print("Please enter either 'y' (Yes) or 'n' (No)")
            if answer == 'y':
                continue
            else:
                print("Thanks for using!")
                break
