from os import listdir
from os.path import isfile, join
import json
from matplotlib import pyplot as plt

from dateutil.parser import parse


def normalize_records(records, normalize_date=True, normalize_consumption=True):
    min_date = min([record['time'] for record in records])
    min_date = min_date.timestamp() if normalize_date else 0
    min_consumption = min([record['consumption'] for record in records]) if normalize_consumption else 0
    return [
        {
            'time': record['time'].timestamp() - min_date,
            'consumption': record['consumption'] - min_consumption
        } for record in records
    ]


def parse_record(record):
    if record.get('Type') == "SCM":
        return {
            'id': record['Message']['ID'],
            'time': parse(record['Time']),
            'consumption': record['Message']['Consumption']
        }
    elif record.get('Type') == "SCM+":
       return {
            'id': record['Message']['EndpointID'],
            'time': parse(record['Time']),
            'consumption': record['Message']['Consumption']
        }
    else:
        print(f"Unhandled format: {record.get('Type')}")


def running_average(values):
    averages = [values[0]]
    for i in range(len(values) - 1):

        ratio_to_keep = np.exp(-1 * )
        average = (averages[-1] + value) / 2
        averages.append(average)

    return averages


path = 'captures'
onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f))]


records = []
for filename in onlyfiles:
    with open(filename) as file:
        records += [parse_record(json.loads(line)) for line in file.readlines()]

records_by_id = {}
for record_index, record_to_add in enumerate(records):
    print(f"{record_index} / {len(records)}")
    if record_to_add['id'] not in records_by_id:
        records_by_id[record_to_add['id']] = []

    records_by_id[record_to_add['id']].append({
        k: v for k, v in record_to_add.items() if k in ['time', 'consumption']
    })

    for user_id in records_by_id:
        records_by_id[user_id] = sorted(records_by_id[user_id], key=lambda record: record['time'], reverse=True)

histories_to_graph = {
    user_id: normalize_records(records, normalize_date=False)
    for user_id, records in records_by_id.items()
}

for records in histories_to_graph.values():
    consumptions = [record['consumption'] for record in records]
    differences = [consumptions[i] - consumptions[i-1] for i in range(1, len(consumptions))]
    consumptions = running_average(consumptions)
    times = [record['time'] for record in records][:]
    plt.plot(times, consumptions)
plt.show()

pass


