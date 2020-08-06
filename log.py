from data import request as req
from Table import Table
from data.prop import Prop

pro = Prop()

req = req.SonarRequest(pro.get_by_key("sonar_url"), pro.get_by_key("key"))

req.setGenerelMetrics(pro.get_by_key("metrics"))

tbl = Table(pro.get_by_key("name"))

tbl.setMeasures(req.makeRequest(req.generic)["measures"])

tbl.printTable()