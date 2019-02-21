import luigi

# this class extends the Luigi base class ExternalTask
# because we’re simply pulling in an external file
# it only needs an output() function
class readLogFile(luigi.ExternalTask):

    def output(self):
        return luigi.LocalTarget('./logs/access_log_20180611-171527.log')

class grabIPs(luigi.Task): # standard Luigi Task class
 
   def requires(self):
       # we need to read the log file before we can process it
       return readLogFile()
 
   def run(self):
       ips = []
 
       # use the file passed from the previous task
       with self.input().open() as f:
           for line in f:
               # a quick glance at the file tells us the first
               # element is the IP. We split on whitespace and take
               # the first element
               ip = line.split()[0]
               # if we haven’t seen this ip yet, add it
               if ip not in ips:
                   ips.append(ip)
 
       # count how many unique IPs there are
       num_ips = len(ips)
 
       # write the results (this is where you could use hdfs/db/etc)
       with self.output().open('w') as f:
           f.write(str(num_ips))
 
   def output(self):
       # the results are written to numips.txt
       return luigi.LocalTarget('numips.txt')

if __name__ == '__main__':
 
   #luigi.run(["--local-scheduler"], main_task_cls=grabIPs)
   luigi.run([], main_task_cls=grabIPs)