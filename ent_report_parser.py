#!/usr/bin/python

import csv

final_list = []
confirmed_list = []


def update_hypervisor_ent():
    # print("Here to update hypervisor entitlement")
    for item in final_list:
        # print(item[0])
        if 'Name' in item[0]:
            confirmed_list.append(item)
        elif 'virt-who' in item[0]:
            # print ("HERE ....: {}".format(item))
            confirmed_list.append(item)
        else:
            # print("Content Host here: {}".format(item))
            aux = item
            for hypers in final_list:
                if aux[6] in hypers:
                    aux[7] = hypers[16]
                    break
            confirmed_list.append(aux)

    pass

def save_in_file():
    with open('parsed_output.csv','w') as f:
        writer = csv.writer(f)
        # for elements in final_list:
        for elements in confirmed_list:
            writer.writerow(elements)
        
        print("Done. File parsed_output.csv created!")

def parse_subs(to_parse):
    local_list = to_parse.replace("[", "").replace("]", "").replace("\'", "").replace("\"", "").split("|")
    return local_list

def main():
    import os.path

    if (os.path.isfile('report.csv')):
        pass
    else:
        print("Please, create the file named report.csv using the command below")
        print("\"# hammer csv content-hosts --export > report.csv\" and then rerun this script.")
        exit(1)

    with open('report.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            local_list = []
            if (row[14] == "Subscriptions"):
                name=row[0]
                local_list.append(name)
                org=row[1]
                local_list.append(org)
                env=row[2]
                local_list.append(env)
                content_view=row[3]
                local_list.append(content_view)
                host_collections=row[4]
                local_list.append(host_collections)
                virtual=row[5]
                local_list.append(virtual)
                guest_of_host=row[6]
                local_list.append(guest_of_host)
                
                # Hypervisor Ent Here
                local_list.append("Host Subscription")

                os=row[7]
                local_list.append(os)
                arch=row[8]
                local_list.append(arch)
                sockets=row[9]
                local_list.append(sockets)
                ram=row[10]
                local_list.append(ram)
                cores=row[11]
                local_list.append(cores)
                sla=row[12]
                local_list.append(sla)
                # products=row[13]
                # local_list.append(products)
                # subscriptions=row[14]
                # local_list.append(subscriptions)

                # ???
                local_list.append("CHECK")
                # SKU
                local_list.append("SKU")
                # Description
                local_list.append("Subscription Name")
                # Contract X
                local_list.append("Contract")
                # Contract Y
                local_list.append("Account Number")

                final_list.append(local_list)



            else:
                # for b in len(row[14]):
                aux = row[14].replace(", "," - ").split(",")

                if (len(aux) == 1):
                    # print (aux)

                    obj = parse_subs(str(aux))

                    name=row[0]
                    local_list.append(name)
                    org=row[1]
                    local_list.append(org)
                    env=row[2]
                    local_list.append(env)
                    content_view=row[3]
                    local_list.append(content_view)
                    host_collections=row[4]
                    local_list.append(host_collections)
                    virtual=row[5]
                    local_list.append(virtual)
                    guest_of_host=row[6]
                    local_list.append(guest_of_host)

                    # Hyper here
                    local_list.append("")

                    os=row[7]
                    local_list.append(os)
                    arch=row[8]
                    local_list.append(arch)
                    sockets=row[9]
                    local_list.append(sockets)
                    ram=row[10]
                    local_list.append(ram)
                    cores=row[11]
                    local_list.append(cores)
                    sla=row[12]
                    local_list.append(sla)
                    # products=row[13]
                    # local_list.append(products)
                    # subscriptions=row[14]
                    # local_list.append(subscriptions)

                    # ???
                    try:
                        local_list.append(obj[0])
                    except IndexError as identifier:
                        # pass
                        local_list.append("")
                    
                    # SKU
                    try:
                        local_list.append(obj[1])
                    except IndexError as identifier:
                        # pass
                        local_list.append("")

                    # Description
                    try:
                        local_list.append(obj[2])
                    except IndexError as identifier:
                        # pass
                        local_list.append("")
                    
                    # Contract X
                    try:
                        local_list.append(obj[3])
                    except IndexError as identifier:
                        # pass
                        local_list.append("")


                    # Contract Y
                    try:
                        local_list.append(obj[4])
                    except IndexError as identifier:
                        # pass
                        local_list.append("")


                    # print("here")
                    final_list.append(local_list)
                    pass

                if (len(aux) != 1):
                    for x in aux:
                        # print (x)
                        obj = parse_subs(x)
                        
                        local_list = []
                        
                        name=row[0]
                        local_list.append(name)
                        org=row[1]
                        local_list.append(org)
                        env=row[2]
                        local_list.append(env)
                        content_view=row[3]
                        local_list.append(content_view)
                        host_collections=row[4]
                        local_list.append(host_collections)
                        virtual=row[5]
                        local_list.append(virtual)
                        guest_of_host=row[6]
                        local_list.append(guest_of_host)

                        # Hyper here
                        local_list.append("")

                        os=row[7]
                        local_list.append(os)
                        arch=row[8]
                        local_list.append(arch)
                        sockets=row[9]
                        local_list.append(sockets)
                        ram=row[10]
                        local_list.append(ram)
                        cores=row[11]
                        local_list.append(cores)
                        sla=row[12]
                        local_list.append(sla)
                        # products=row[13]
                        # local_list.append(products)
                        # subscriptions=row[14]
                        # local_list.append(subscriptions)


                        # ???
                        try:
                            local_list.append(obj[0])
                        except IndexError as identifier:
                            # pass
                            local_list.append("")
                        
                        # SKU
                        try:
                            local_list.append(obj[1])
                        except IndexError as identifier:
                            # pass
                            local_list.append("")

                        # Description
                        try:
                            local_list.append(obj[2])
                        except IndexError as identifier:
                            # pass
                            local_list.append("")
                        
                        # Contract X
                        try:
                            local_list.append(obj[3])
                        except IndexError as identifier:
                            # pass
                            local_list.append("")


                        # Contract Y
                        try:
                            local_list.append(obj[4])
                        except IndexError as identifier:
                            # pass
                            local_list.append("")


                        final_list.append(local_list)
                        pass

main()
update_hypervisor_ent()
save_in_file()