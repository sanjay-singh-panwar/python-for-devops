import json
class LogAnalyzer:

    def __init__(self, filename, outputfile):
        self.filename = filename
        self.outputfile = outputfile

    def read_logs(self):
        with open(self.filename, "r") as file:
            return file.readlines()
        
    def analyze(self ):
        count_logs = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }
        lines = self.read_logs()
        for line in lines:
            if "INFO" in line:
                count_logs.update({"INFO": count_logs["INFO"] + 1})
            elif "WARNING" in line:
                count_logs.update({"WARNING": count_logs["WARNING"] + 1})
            elif "ERROR" in line:
                count_logs.update({"ERROR": count_logs["ERROR"] + 1})
            else:
                pass
        return count_logs

    def write_json(self, counts ):
        with open(self.outputfile ,"w+") as json_file:
            json.dump(counts, json_file)

log1 = LogAnalyzer("app.log", "output1.json" )
count_logs = log1.analyze()
log1.write_json(count_logs)


