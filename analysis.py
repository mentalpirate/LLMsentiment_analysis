gemini_api_key = "AIzaSyCHa4QEdndsHJfHQRSms-9qmgHr16vnX38"


import requests
genurl = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={}".format(gemini_api_key)
data = {
    "contents":[{"parts":[{"text":prompt}]}]
}
headers = {
    'Content-Type': 'application/json'
}

requests.post(headers=headers, data=data, url=genurl )




json_data = {

}


prompt = f"""
You are an expert linguist, who is good at classifying customer review sentiments into Positive/Negative labels.
Help me classify customer reviews into: Positive,Neutral and Negative with score in scale of 5.
Customer reviews are provided between three back ticks.
In your output, only return the Json code back as output - which is provided between three backticks.
Your task is to update predicted labels under 'pred_label' in the Json code.
Don't make any changes to Json code format, please.

```
{json_data}
```
"""