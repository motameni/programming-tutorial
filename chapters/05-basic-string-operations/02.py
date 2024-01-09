astring = "motameni1371@outlook.com"

postfix_list = ["gmail.com", "yahoo.com"]

for postfix in postfix_list:
    if astring.endswith("@%s" % postfix):
        print("Correct Email!")
