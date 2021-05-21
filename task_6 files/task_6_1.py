import re  # import regular expressions module
list_of_tuples = []

with open("nginx_logs.txt", encoding="UTF-8") as logs_file:
    for line in logs_file:
        line = line.replace('-', '')

        remote_addr = re.search("[0-9]+.[0-9]+.[0-9]+.[0-9]+", line)    # get the IP-address

        type_resource = line.split('"')[1]                              # get request type and URL
        requested_type = type_resource.split(' ')[0]                    # take out request type
        requested_resource = re.search('/[^\s]+', type_resource)        # take out request URL

        list_of_tuples.append((remote_addr.group(), requested_type, requested_resource.group()))

for tuple in list_of_tuples[:10]:
    print(tuple)
