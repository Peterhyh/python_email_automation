# Run this file and the generated messages will be located in the ReadyToSend folder.


with open("/Users/PeterHuynh/Desktop/Coding/Python/email_automation/input/template.txt") as data:
    template = data.read()

string_to_replace = "[name]"

with open("/Users/PeterHuynh/Desktop/Coding/Python/email_automation/input/names/names.txt") as data:
    name_list = data.read().split()

for name in name_list:
    output = template.replace(string_to_replace, name)
    with open(f"/Users/PeterHuynh/Desktop/Coding/Python/email_automation/output/ReadyToSend/{name}.txt", mode="w") as data:
        data.write(output)
