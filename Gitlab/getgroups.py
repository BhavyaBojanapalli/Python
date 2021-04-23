##########################################################################################
# Author : Bhavya Bojanapalli
# get_groups() function returns the groups by passing the user private token
# get_subgroups function iterates the group ID and get the subgroups present in the group.
###########################################################################################

import requests
import json

def get_groups():
    group_ids=[]
    url = #api call for groups
    headers = {'PRIVATE-TOKEN' : #value}
    response = requests.get(url, headers=headers)
    json_format = json.loads(response.text)
    for i in [*range(len(json_format))]:
        group_ids.append(json_format[i]['id'])
    return (group_ids)
    
def get_subgroups(group_ids):
    comb={}
    comb_list=[]
    for id in [*range(len(group_ids))]:
        subgroupnames=[]
        url = #api call for sub-groups
        headers = {'PRIVATE-TOKEN' : #value}
        response = requests.get(url, headers=headers)
        json_format = json.loads(response.text)
        if(response.text == "[]"):
            subgroupnames = []
        else:
            for i in [*range(len(json_format))]:
                subgroupnames.append(json_format[i]['id'])
        comb[group_ids[id]] = subgroupnames
    comb_list.append(comb)
    print(comb_list)

def main():
    group_ids = get_groups()
    get_subgroups(group_ids)
    
    
main()
