import json
def file_saver(json_format):
    json_dump_out_put = json.dumps(json_format , indent=4)
    requiredData = json.loads(json_dump_out_put)
    #print(requiredData["message"])
    with open("just.txt", "w") as outfile:
        outfile.write(json_dump_out_put) 
    outfile.close()
    print("#################this from filesaver")
    return requiredData
