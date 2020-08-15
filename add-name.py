import sys
import json
from collections import OrderedDict
from operator import getitem
'''
Takes existing data of JSON file, username and PR information as input and adds a record to the JSON file
and returns the data of updated JSON file.
'''
def add_record(data,username,pr_dict):
    data[username] = {"count": len(pr_dict),
                      "contributions": pr_dict
                    }

    with open("community-contributions.json","w") as write_file:
            json.dump(data,write_file)
    return data


'''
Takes existing data of JSON file, username and PR information as input and updates a record to the JSON file
and returns the data of updated JSON file.
'''
def update_record(data,username,pr_dict):
    data[username]["count"] +=  len(pr_dict)
    
    for name,link in pr_dict.items():
        data[username]["contributions"][name] = link

    with open("community-contributions.json","w") as write_file:
            json.dump(data,write_file)

    return data

if __name__ == "__main__":

    # Get command line arguments
    #issue_head = sys.argv[1].strip()
    #issue_bod = sys.argv[2].strip() 
    #issue_head = "update|shriaas"
    #issue_bod = """**Name:** pr3 | **Link**: https://github.com/link-to-3rd-pr
    # **Name:** pr4 | **Link**: https://github.com/link-to-4th-pr"""
    '''
    # Get records from JSON file
    with open("community-contributions.json","r") as read_file:
        contr_data = json.load(read_file)

    # Create a dictionary
    pr_dict = {}
    for pr in issue_bod.split("\n"):
        # Assigning PR variables for PR name and link
        link = pr.split('|')[1].strip()
        link = (link.lstrip("**Link**: ")).strip()
        pr_name = pr.split('|')[0].strip()
        pr_name = (pr_name.lstrip("**Name**: ")).strip()
        # Adding PR to the dictionary
        pr_dict[pr_name] = link

    if issue_head.split("|")[0].lower() == "add":
        contr_data = add_record(contr_data,issue_head.split("|")[1],pr_dict)
    
    elif issue_head.split("|")[0].lower() == "update":
        contr_data = update_record(contr_data,issue_head.split("|")[1],pr_dict)
    
    # Update the leader board '''
    with open("Leaderboard.md","r") as read_file:
       
        read_data = read_file.read()
        # starting of leaderboard records
        start = read_data.index('Link of Contribution|\n| --- | --- | --- |\n')+len('Link of Contribution|\n| --- | --- | --- |\n') 
        # ending of leaderboard records
        end = read_data.index('<!-- End of Leaderbaord')
        write_data = read_data[:start]
        
    # TO BE DELETED: extracting data from JSON file
    with open("community-contributions.json","r") as read_file:
        contr_data = json.load(read_file)
        
    print("Originmal Data;",contr_data)
    contr_data = OrderedDict(sorted(contr_data.items(), 
                          key = lambda x: getitem(x[1], 'count'),reverse=True))
    # Writing leaderboard data from JSON file
    records= []
    for usr,info in contr_data.items():
        records.append(f"| [@{usr}](https://github.io/{usr}) | {info['count']} | ")
        for pr, link in info["contributions"].items():
            records.append(f" - [{pr}]({link}) <br>")
        records.append(" |\n")
    write_data =  write_data+ "".join(records) + read_data[end:]

    with open("Leaderboard.md","w") as write_file:
        write_file.write(write_data)
    print("Done! dana dana")