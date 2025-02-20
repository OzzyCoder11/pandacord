# pandacord Documentary

This is a new Python PyPI package that uses Discord's API to send messages, verify tokens and more. **I will never add a "token joiner" as that is against Discord's ToS.** This should only be used for automation. Anything you do is not up to me and is not my fault, I discourage you to use this package maliciously.

Firstly, you must install. Use PIP to do this.
```bat
pip install pandacord
```

Next, you can add a token by using a class. Below is an example.

```py
import pandacord as pc

a = pc.Token("Your Token Here") # lets say this is a working vaild token

a.validate() # all values saved to a.info. this also returns [True, <username>, <discriminator>, <userid>]

if a.info[0]:
  print("This token is valid.")
  print(f"Username: {a.info[1]}#{a.info[2]}") # Output: Username: username#0001
```

Futhermore, you can send messages.

```py
a.message(1234567890000, "Sent using pandacord!") # returns [response.status_code, response.json()]
```
Output:
![image](https://github.com/user-attachments/assets/1d74fbec-7330-4ae9-b240-b3ab259f4594)

It sents the message using requests. Additionally, proxies may be added with:
```py
a.message(1234567890000, "Sent using pandacord!", {"http": "http://1.1.1.1"}) # returns [response.status_code, response.json()]
```

Introduced in version 2.0.0, you can now use webhooks in an advanced way. Here is an example:

```py
import pandacord as pc

a = pc.Webhook("https://discord.com/api/webhooks/1234567890/1234567890") # pretent this is a valid webhook

# to send a message, you must use the send function

a.send(content="Sent with pandacord Webhooks!")
```
Output: ![image](https://github.com/user-attachments/assets/2d4f96e0-b008-47ff-89fc-ec55b1d91fb5)

To use webhook in an advanced way, you can add embeds. Unfortunately, these are very simple embeds. But here is an expample:

```py
a.send_embed(
    title="Pandacord!",
    description="This is sent with Pandacord!",
    color=0x00ff00
)
```
Output: ![image](https://github.com/user-attachments/assets/8d50df7a-62d0-4459-ae5e-8f329a9c6258)

Something smaller, you can see if the user is connected to the internet with:

```py
import pandacord as pc
import sys

if pc.other.test_wifi():
  do_something()
else:
  sys.exit()
```

Finally for 2.0.0, you can get infomation from invites. Here is an example:

```py
import pandacord as pc

a = pc.Invite("tiktok") # you must not add discord.gg/ | im using tiktok as an example

print(a.get_info()[1].get('guild').get('name')) # Output: TikTok
print(a.get_info()[1].get('guild').get('id'))   # Output: 893568518853914664
```
