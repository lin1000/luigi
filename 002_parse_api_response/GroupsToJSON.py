import luigi
import requests
import json
from collections import Counter

class GroupsToJSON(luigi.Task):
    key = luigi.Parameter()
    lat = luigi.Parameter()
    lon = luigi.Parameter()

    def run(self):
        seed_topic = "nosql"
        uri = "https://api.meetup.com/2/groups?&topic={0}&lat={1}&lon={2}&key={3}".format(seed_topic, self.lat, self.lon, self.key)

        r = requests.get(uri)
        all_topics = [topic["urlkey"]  for result in r.json()["results"] for topic in result["topics"]]
        c = Counter(all_topics)

        topics = [entry[0] for entry in c.most_common(10)]

        groups = {}
        for topic in topics:
            uri = "https://api.meetup.com/2/groups?&topic={0}&lat={1}&lon={2}&key={3}".format(topic, self.lat, self.lon, self.key)
            r = requests.get(uri)
            for group in r.json()["results"]:
                groups[group["id"]] = group

        with self.output().open('w') as groups_file:
            print("output success")
            json.dump(list(groups.values()), groups_file, indent=4, sort_keys=True)

    def output(self):
        return luigi.LocalTarget("./groups.json")
