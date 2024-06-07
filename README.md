# automation
## others/delete_modem_sms.js
When number of SMS in my GP modem becomes too high it fails to decode and display those messages. It doesn't even allow me to delete those message. So, I research for a bit and created this script to delete those SMS. I can find the SMS ids by trying to open the SMS page. Then use the following python code to get the ids.
```python
import json

filepath = "sms.json"
ids = ""
with open(filepath, "r") as f:
    data = json.load(f)
    for message in data["messages"]:
        id_number = message["id"]
        if id_number.isnumeric():
            ids += id_number + "%3B"

output_file = "ids.txt"
with open(output_file, "w") as f:
    f.write(ids)
```
I have some more work to do on this script. They are:
* [ ] Add a function to print all SMS in console.
* [ ] Add a function to delete all SMS.
