from requests.auth import HTTPBasicAuth
import requests
import json
import os
from Naked.toolshed.shell import execute_js, muterun_js
import wapitest as tk

def create_Request(response_token,EmailId):
    request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/create_request_generic"

    # Note: Wrong input from Documentation: Content-Type
    headers = {"userEmail":EmailId,"wolken_token":response_token,"Content-Type":"application/json"}
    data = {"requestMasterVO":{"sourceId":6,"requestDesc":"Test","requestedEmail":"testFandLName@gmail.com"},
            "descDetailsVO":{"descLarge":"test"},
            "userDetails":{"userFname":"testFName","userLname":"testLname"}}
    print(type(str(data)))
    data = requests.post(url=request_url, data=str(data), headers=headers)
    return data



res = tk.login_module()
data = create_Request(res,"poornima@wolkensoftware.com")
print(data.json())
