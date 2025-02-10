def split_records_by_prefix(split_length, base_path, cdr_database, input_file_path):
    prefixes_set = set()
    prefix_mapping = {}
    prefix_file = open(base_path + "Auxiliar" + cdr_database + "\\pr")
    for prefix in prefix_file:
        prefix = prefix.replace("/", "-")

        prefixes_set.add(prefix.replace("\n", ""))
    prefix_file.close()
    mapping_file = open(base_path + "Auxiliar" + cdr_database + "\\aae")
    for prefix in mapping_file:
        prefix = prefix.replace("/", "-")

        prefix = prefix.replace("\n", "")
        prefix_parts = prefix.split("|")
        prefix_mapping[prefix_parts[0]] = prefix_parts[1]

    mapping_file.close()

    for prefix in prefixes_set:
        prefix = prefix.replace("/", "-")

        globals()["a" + prefix] = open(
            base_path + "Arqparciais" + cdr_database + "\\" + prefix + ".txt", "w"
        )
    data_file = open(input_file_path)
    for record_line in data_file:
        record_line = (
            record_line[0:split_length].replace("/", "-") + record_line[split_length:]
        )

        current_prefix = record_line[0:split_length]
        if current_prefix in prefix_mapping:
            mapping_file = globals()["a" + prefix_mapping[record_line[0:split_length]]]
            record_line = (
                record_line[0:split_length].replace("-", "/")
                + record_line[split_length:]
            )
            mapping_file.write(record_line)

    data_file.close()

    for prefix in prefixes_set:
        prefix = prefix.replace("/", "-")
        mapping_file = globals()["a" + prefix]
        mapping_file.close()
