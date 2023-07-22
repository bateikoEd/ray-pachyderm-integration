import json

input_file_name = '/pfs/dirty_data/input_data.json'
output_file_name = '/pfs/out/output_data.json'

with open(input_file_name, 'r') as file:
    dict_json = json.load(file)
    linerization = lambda x: 5 * x + 3 * x
    x = dict_json['input_data']
    y = [linerization(sample) for sample in x]

    dict_output = {"input_data": x,
                   "output_data": y}

    with open(output_file_name, "w") as f:
        object_j = json.dumps(dict_output)
        f.write(object_j)

