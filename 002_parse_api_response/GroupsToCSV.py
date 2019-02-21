from luigi.contrib.external_program import ExternalProgramTask

import luigi
import GroupsToJSON

class GroupsToCSV(luigi.contrib.external_program.ExternalProgramTask):
    file_path = "./groups.csv"
    key = luigi.Parameter()
    lat = luigi.Parameter()
    lon = luigi.Parameter()

    def program_args(self):
        return ["/Users/lin1000/github/luigi/002_parse_api_response/group.sh", self.input()[0].path, self.output().path]

    def output(self):
        return luigi.LocalTarget(self.file_path)

    def requires(self):
        yield GroupsToJSON.GroupsToJSON(self.key, self.lat, self.lon)