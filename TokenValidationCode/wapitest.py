from requests.auth import HTTPBasicAuth
import requests
import json
import os
from Naked.toolshed.shell import execute_js, muterun_js
####################################### 1. login module ##########################################
def login_module():
    login_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/login/authenticate"

    res = requests.get(login_url, auth=HTTPBasicAuth('extuse', 'wSOylMKaeTNekc1'))

    print(res.json())

    response_token = res.json()['token']

    return response_token

###################################### 2. Create Request #########################################
def create_Request(response_token,EmailId,firstName):
    request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/create_request_generic"

    # Note: Wrong input from Documentation: Content-Type
    os.remove("C:\\Users\\harsh\Desktop\\rasa_final_project\\TokenValidationCode\\final_prg\\input_db.json")
    print("File Removed!")
    headers = {"userEmail":EmailId,"wolken_token":response_token,"Content-Type":"application/json","FirstName":firstName}
    with open('C:\\Users\\harsh\Desktop\\rasa_final_project\\TokenValidationCode\\final_prg\\input_db.json', "w") as write_file:
        json.dump(headers, write_file)
    success = execute_js('.\\TokenValidationCode\\final_prg\\final_prg.js')
    with open("C:\\Users\\harsh\Desktop\\rasa_final_project\\TokenValidationCode\\final_prg\\outpt.json", "r") as read_file:
        data = json.load(read_file)
    print(data)
    return data


##################################### 3. Update Request ###########################################
def update_request(response_token,EmailId,requestId):
    update_request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/update_request"

    # Note: Wrong input from Documentation: Content-Type
    os.remove("C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\input_update.json")
    print("File Removed!")
    headers = {"userPsNo": EmailId, "wolken_token": response_token, "Content-Type": "application/json","requestId": requestId}
    with open('C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\input_update.json', "w") as write_file:
        json.dump(headers, write_file)
    success = execute_js('.\\TokenValidationCode\\final_prg\\final_2_update.js')
    with open("C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\output_update.json", "r") as read_file:
        data = json.load(read_file)
    print(data)
    return data

#################################### 4. Get All Request #########################################
def get_All_Request(response_token,EmailId):
    all_request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/get_all_request"

    # Note: Wrong input from Documentation: Content-Type
    headers = {"userPsNo":EmailId, "wolken_token": response_token, "Content-Type": "application/json"}

    data = {"myRequestDtlCondition": "3"}

    all_request_res = requests.post(url=all_request_url, data=json.dumps(data), headers=headers)
    print(all_request_res.json())

    return all_request_res

#################################### 5. Get Case Details #########################################
def get_case_details(response_token,EmailId):
    url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/specific_request_details?requestId=1470&sections=REQUEST_MASTER"

    headers = {"userPsNo": EmailId, "wolken_token": response_token}

    case_res = requests.get(url=url, headers=headers)

    print(case_res.json())
    return case_res

#################################### 6. Close Request #########################################
def close_Request(response_token,EmailId,requestId):
    close_request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/update_request"
    try:
    # Note: Wrong input from Documentation: Content-Type
        os.remove("C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\input_close.json")
        print("File Removed!")
        headers = {"userPsNo": EmailId, "wolken_token": response_token, "Content-Type": "application/json","requestId": requestId}
        with open('C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\input_close.json', "w") as write_file:
            json.dump(headers, write_file)
        success = execute_js('.\\TokenValidationCode\\final_prg\\final_close.js')
        with open("C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\output_close.json", "r") as read_file:
            data = json.load(read_file)
        print(data)
        return data
    except Exception as e:
        print(e)
