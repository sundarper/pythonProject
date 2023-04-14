import json

with open('./resources/json_test/personal_info.json', 'r') as user_file:
#with open('//s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json', 'r') as user_file:
    #parsed_json = json.load(user_file)
    file_contents = user_file.read()

    print(file_contents)
    print(type(file_contents))

parsed_json = json.loads(file_contents)
#parsed_json = json.dumps(file_contents)
print(parsed_json)
print(type(parsed_json))

print(parsed_json)
print("response_code = ", parsed_json["response_code"])
print("train_number = ", parsed_json["train_number"])
print("position = ", parsed_json["position"])
print(type(("route = ", parsed_json["route"][0])))
route = ("route = ", parsed_json["route"][0]["has_arrived"])

print(route)
print(type(route_disct))






