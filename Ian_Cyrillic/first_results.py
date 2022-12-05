import json
# from parser import Parser

column_names = ["Header", "ElEquiv", "LaEquiv", "WordClass", "Mem", "GramEnd"]

for page_num in range(1, 40000):
    print(page_num)
    with open(f"search_results/pages/{page_num}.json", encoding='utf8') as file:
        page = json.load(file)

    page = page['response']['result']
    if "WordClass" not in page or "propr." not in page["WordClass"]:
        continue

    with open("nouns.csv", "ab") as output:
        output.write(bytes(str(page_num), encoding='utf8') + b",")
        output.write(bytes(f"{','.join(column_names)}\n"))
        for column_name in column_names:
            if column_name not in column_names:
                continue
            if column_name in page:

                column = page[column_name]
                if isinstance(column, list):
                    if len(column) == 1:
                        column = bytes(column[0], encoding='utf8')
                    else:
                        column = b"/".join([bytes(c, encoding='utf8') for c in column])
                else:
                    column = bytes(column, encoding='utf8')
                output.write(column)
            output.write(b",")
        output.write(b"\n")
