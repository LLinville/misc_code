import requests
import time
import datetime

player_names = [
    "Iron_Spetsai",
    "lowpoly4life",
    "Iron_Barlor",
    "MorekTheGimp",
    "OlofTheWroth",
    "suchironknee",
    "DegeneRaider",
    "Wizidross",
    "OracleLock",
    "Uillyer",
    "Villyer",
    "Patsfan299",
    "nogoodclicks",
    "lowpoly4ever",
    "onlygoodclicks",
    "missedticks"
]

after_fetch_delay = 60 * 60
retry_delay = 60 * 60
retry = False
# fetch_interval = 1 * 60 * 60
# per_name_fetch_interval = fetch_interval / len(player_names)


while True:
    print('\n' + datetime.datetime.fromtimestamp(time.time()).strftime("%Y/%m/%d-%H:%M:%S"))
    for name in player_names:
        for attempt in range(3):
            print(f"Sending update request for {name}")
            try:
                result = requests.get(f"http://crystalmathlabs.com/tracker/update.php?player={name}")
                print(f"Response: {result.status_code}")

                if result.status_code == 200:
                    break

            except Exception as e:
                print(e)
                print(f"Retrying in {retry_delay} sec")
                time.sleep(retry_delay)
                if not retry:
                    break
        else:
            print("Update failed")
        time.sleep(after_fetch_delay)

    # time.sleep(fetch_interval)