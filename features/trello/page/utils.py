def table_to_dict(context):
    context.table_values = {}

    try:
        for row in context.table:
            cells = [cell if cell != '' else None for cell in row.cells]
            context.table_values.update(dict(zip(row.headings, cells)))
    except TypeError:
        print("No data to update")

    context.table_values = {k: v for k, v in context.table_values.items() if v}

    return context.table_values

def extract_ids_excluding_key(json_data, key='id', exclude_key='memberships'):
    ids = []

    def recursive_extract(data):
        if isinstance(data, dict):
            if exclude_key in data:
                # Se encontrarmos o key para exclusão, não processamos mais o conteúdo dele
                # Em vez disso, simplesmente ignore e continue
                data.pop(exclude_key)
            for k, v in data.items():
                if k == key:
                    ids.append(v)
                recursive_extract(v)
        elif isinstance(data, list):
            for item in data:
                recursive_extract(item)

    recursive_extract(json_data)
    return ids
