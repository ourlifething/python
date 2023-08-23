import requests as req
import json


url = 'http://api.open-notify.org/iss-now.json' # web API
res = req.get(url)
data = json.loads(res.text)
pos = data['iss_position']
print(f"Issの緯度は{pos['latitude']},軽度は{pos['longitude']}")

# Issの緯度は-36.8432,軽度は164.4617

"""json data 
{
"iss_position": {
"latitude": "-14.5215",
"longitude": "141.9504"
},
"message": "success",
"timestamp": 1692766840
}
"""

