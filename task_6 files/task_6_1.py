import re  # import regular expressions module
list_of_tuples = []
potential_spamers = {}

with open("nginx_logs.txt", encoding="UTF-8") as logs_file:
    for line in logs_file:
        line = line.replace('-', '')

        remote_addr = re.search("[0-9]+.[0-9]+.[0-9]+.[0-9]+", line)    # get the IP-address
        remote_addr = remote_addr.group()

        type_resource = line.split('"')[1]                              # get request type and URL
        requested_type = type_resource.split(' ')[0]                    # take out request type
        requested_resource = re.search('/[^\s]+', type_resource)        # take out request URL

        if remote_addr in potential_spamers:
            potential_spamers[remote_addr] += 1
        else:
            potential_spamers[remote_addr] = 1

        list_of_tuples.append((remote_addr, requested_type, requested_resource.group()))

for tuple in list_of_tuples[:10]:
    print(tuple)

# task 6_2 - define the spamer
call_number = 0
spamer_IP = ""
for key in potential_spamers:
    if potential_spamers[key] > call_number:
        call_number = potential_spamers[key]
        spamer_IP = key

print("Spammer IP is:", spamer_IP, "he called our server", call_number, "times")
