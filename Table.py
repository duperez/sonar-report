from metric.Measures import Measures


class Table:

    def __init__(self, project_name, value_leng=4, name_leng=17):
        self.project_name = project_name
        self.values = []
        self.name_leng = name_leng
        self.value_leng = value_leng

    def setMeasures(self, measures):
        self.values = [Measures(value) for value in measures]

    def showMeasureMetrics(self):
        for metric in self.values:
            print("|" + metric.metric, " " * (self.name_leng - len(metric.metric)) + ":" + metric.value + " " * (self.value_leng - len(metric.value)) + "|")

    def showDetailMetrics(self):
        for metric in self.values:
            print("|", metric.metric, " " * (self.name_leng - len(metric.metric)), ":", metric.value, " " * (self.value_leng - len(metric.value)), "|")

    def showProjectInfo(self):
        print("|NAME" + ": " + self.project_name[:17] + " " * (17 - len(self.project_name[0:21])) + "|")

    def showDelimiter(self):
        print("*" + "-" * ((self.name_leng + self.value_leng) + 2) + "*")

    def printTable(self):
        self.showDelimiter()
        self.showProjectInfo()
        self.showDelimiter()
        self.showMeasureMetrics()
        self.showDelimiter()