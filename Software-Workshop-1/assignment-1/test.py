def create_unique(id_list):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :return: final_list is returned and this list contains all of the unique student ids
    """
    final_list = []
    # insert code here to create unique ids
    id_suffixes = {}
    for id in id_list:
        if id not in id_suffixes:
            id_suffixes[id] = 0
            final_list.append(f"{id}0000")
        else:
            id_suffixes[id] += 1
            final_list.append(f"{id}{id_suffixes[id]:04}") # Append a unique ID with leading zeros

    print(final_list)


li = ["mas", "axj", "drs", "axt", "mas", "mas", "jxs", "hxc", "axg"]
create_unique(li)