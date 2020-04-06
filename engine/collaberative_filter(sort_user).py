import json


def sort_users(users, counter):
    print('Starting sort_users..')
    t = 0
    for user in users:
        if t > 10000:
            break
        t += 1
        try:
            counter[user] = {}
            for profile in counter:
                points = 0
                for product1 in users[user]:
                    for product2 in users[profile]:
                        if product1 == product2:
                            points += 1

                if points != 0:
                    compatibility = len(users[user]) / points
                    counter[user] += {profile: compatibility}
                    counter[profile] += {user: compatibility}

        except IndexError:
            counter[user] = {}

    print(counter)


with open('test.json') as json_file:
    data = json.load(json_file)
    sort_users(data, {})
    json_file.close()


