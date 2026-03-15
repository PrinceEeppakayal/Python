
post = input("Enter the post: ")
names = False


if("prince" in post):
    names = True
elif("Prince" in post):
    names = True
elif("PRince" in post):
    names = True
elif("PRInce" in post):
    names = True
elif("PRINce" in post):
    names = True
elif("PRINCe" in post):
    names = True
elif("PRINCE" in post):
    names = True
elif("PrINCE" in post):
    names = True
elif("PriNCE" in post):
    names = True
elif("PrinCE" in post):
    names = True
elif("PrincE" in post):
    names = True
elif("princE" in post):
    names = True
elif("prinCE" in post):
    names = True
elif("priNCE" in post):
    names = True
elif("prINCE" in post):
    names = True
elif("pRINCE" in post):
    names = True
else:
    names = False

if names:
    print("This post is about prince")
else:
    print("This post is not about prince")