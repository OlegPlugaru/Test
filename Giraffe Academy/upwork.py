import os

site = input()


if "https://" in site:
    os.system('open ' + site)
    print("if")

elif "www." in site:
    site = "https://" + site
    os.system("open " + site)
    print("elif")
else:
    site = "https://www." + site
    os.system("open " + site)
    print("else")
