# pandacord Documentary

This is a new Python PyPI package that uses Discord's API to send messages, verify tokens and more. **I will never add a "token joiner" as that is against Discord's ToS.** This should only be used for automation. Anything you do is not up to me and is not my fault, I discourage you to use this package maliciously.

Firstly, you can add a token by using a class. Below is an example.

```py
import pandacord

a = Token("Your Token Here")

a.validate() # all values saved to a.info

if a.info[1]:
  print("This token is valid.")
```
