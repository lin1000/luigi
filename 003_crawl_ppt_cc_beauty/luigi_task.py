import luigi
import time

class CrawlPttCcBeauty(luigi.Task):

    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('Beauty.txt')

    def run(self):
        time.sleep(15)
        with self.output().open('w') as outfile:
            outfile.write('Hello Beauty!\n')
        time.sleep(15)

class ProcessImage(luigi.Task):
    name = luigi.Parameter()
    password = luigi.Parameter()

    def requires(self):
        return CrawlPttCcBeauty()

    def output(self):
        return luigi.LocalTarget(self.input().path + '.name_' + self.name + ".txt")

    def run(self):
        time.sleep(15)
        with self.input().open() as infile, self.output().open('w') as outfile:
            text = infile.read()
            text = text.replace('Beauty', self.name)
            outfile.write(text)
        time.sleep(15)


if __name__ == '__main__':
    luigi.run()        