import urllib2


class Eot(object):

    def __init__(self, agentConfig, checksLogger, rawConfig):
        self.agentConfig = agentConfig
        self.checksLogger = checksLogger
        self.rawConfig = rawConfig
        self.eot_host = 'https://api.eot.pt/api/pulse/last/power?key=<key>'

    def run(self):
        data = {}
        try:
          req = urllib2.Request(self.eot_host)
          request = urllib2.urlopen(req)
          response = request.read()
          data["sede"] = response
        except:
            self.checksLogger.exception("Exception getting data from EOT")

        return data
