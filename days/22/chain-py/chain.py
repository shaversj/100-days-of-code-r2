def is_valid(chain: str):
    # "BEGIN-3;4-2;3-4;2-END"
    split_chain = chain.split(";")
    tree = {}
    bad_chain = False

    # populate map
    for link in split_chain:
        split_link = link.split("-")

        if split_link[0] == split_link[1]:
            bad_chain = True
        else:
            if split_link[0] in tree:
                bad_chain = True
            else:
                tree[split_link[0]] = split_link[1]

    # {'BEGIN': '3', '4': '2', '3': '4', '2': 'END'}

    print(bad_chain)
    links_used = 1
    chain_length = len(tree)
    print(f"chain_length:  {chain_length}")

    value = tree.get("BEGIN")
    if tree.get("BEGIN") == "":
        bad_chain = True
    else:
        while value != "END" and links_used < chain_length:
            # follow the chain until the end or until links_used equals chain_length
            # if links_used = chain_lenth, but value != "END", it means that there is a cycle.
            value = tree.get(value)
            links_used += 1

    print(f"links_used: {links_used}")
    print(value)
    if bad_chain is False and links_used == chain_length and value == "END":
        print("GOOD")
    else:
        print("BAD")
