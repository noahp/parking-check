# 🚗 mbta parking checker

## ⚠️ 💀 Oof, TODO

Doesn't work, due to the payvats site requiring a couple of tokens when fetching
invoices by GET. Need to retool to maybe using simple 2-stage python requests.

```python
import requests
from xml.etree import ElementTree

response = requests.get("https://vats.municipalcitationsolutions.com/payments/PayVats.aspx?location=47")

tree = ElementTree.fromstring(response.content)

# locate __VIEWSTATE and __EVENTVALIDATION for second GET
```

Example request, with some non-required fields (from experimentation) removed:

```bash
curl 'https://vats.municipalcitationsolutions.com/payments/PayVats.aspx?location=47' \
 -H 'Pragma: no-cache' \
 -H 'Origin: https://vats.municipalcitationsolutions.com' \
 -H 'Accept-Encoding: gzip, deflate, br' \
 -H 'Accept-Language: en-US,en;q=0.9' \
 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36' \
 -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
 -H 'Accept: */*' \
 -H 'Cache-Control: no-cache' \
 -H 'X-Requested-With: XMLHttpRequest' \
 -H 'Connection: keep-alive' \
 -H 'Referer: https://vats.municipalcitationsolutions.com/payments/PayVats.aspx?location=47' \

 --data 'ctl00%24ContentPlaceHolder1%24ScriptManager=ctl00%24ContentPlaceHolder1%24updpan1%7Cctl00%24ContentPlaceHolder1%24btnSearchPlate\'

# the following value needs to match from the langing page
'&__VIEWSTATE=<<URL_ENCODED_VALUE_FROM_LANDING_PAGE>>\
&__VIEWSTATEGENERATOR=8DA55DA2\'

# the following value needs to match from the langing page
'&__EVENTVALIDATION=<<URL_ENCODED_VALUE_FROM_LANDING_PAGE>>\
&ctl00%24ContentPlaceHolder1%24ddlLocations=47\
&ctl00%24ContentPlaceHolder1%24hfDiscount=0\
&ctl00%24ContentPlaceHolder1%24hfViolation=\
&ctl00%24ContentPlaceHolder1%24txtCitationID=\
&ctl00%24ContentPlaceHolder1%24cbxNoCitationNumber=on\
&ctl00%24ContentPlaceHolder1%24txtPlateNumber=769LN7\
&ctl00%24ContentPlaceHolder1%24ddlVehicleState=MA\
&__ASYNCPOST=true\
&ctl00%24ContentPlaceHolder1%24btnSearchPlate=Search%20Plate'
```

## What this

Looks up if a MA license plate has any active parking charges on the MBTA site.

Crude, cheesy, and messy.

## Use

```bash
# fire away.
# `check-parking` uses some env vars for target/source email.
# pass a string to check-parking with the plate number
TARGET_EMAIL=<target-email> \
    SOURCE_EMAIL=<source-email> \
    SOURCE_EMAIL_PASSWORD=<source-email-password> \
    check-parking <plate number>
```

The following env variables are used by the script:

- `$TARGET_EMAIL` - destination email address
- `$SOURCE_EMAIL` - source email address
- `$SOURCE_EMAIL_PASSWORD` - source email SMTP password
- `$PLATE_NUMBER` - plate number
