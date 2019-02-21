import os
import luigi
import GroupsToCSV

class Meetup(luigi.WrapperTask):
    def run(self):
        print("Running Meetup")

    def requires(self):
        key = '33283a4b5829744936f26583c4e319'
        lat = os.getenv('LAT', "51.5072")
        lon = os.getenv('LON', "0.1275")

        yield GroupsToCSV.GroupsToCSV(key, lat, lon)