import json


#objs = boto3.client.list_objects(Bucket='s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json')
#with open('https://s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json', 'r') as user_file:

with open('./resources/json_test/ol_cddump.json', 'r') as user_file:
     file_contents = user_file.read()
     # print(file_contents)
     # print(type(file_contents))

contents = {}
contents = file_contents.split()
print(type(contents))
for lst in contents:
    print(lst)

    # date_load = json.loads(user_file)
    # print(date_load)
    # print(type(date_load))
    # user_file.close()
