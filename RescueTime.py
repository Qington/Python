#########################################
##  RescueTime Data Exporter v1.0      ##
##  Created By Dan Nixon 18/09/2011    ##
##  www.dan-nixon.com                  ##
#########################################

import urllib

## You need to set the following values before first use!!
apiKey = "YOUR_API_KEY"
fileDirectory = "C:\\Path\\To\\Output\\File"
filePrefix = "RescueTimeData"

def appMain():
    print "RescueTime Data Exporter v1.0"
    print "Copyright Dan Nixon 2011, www.technoducky.com"
    print ""
    print "All Dates in Format YYYY-MM-DD Please"
    date_s = raw_input("Start Date: ")
    date_e = raw_input("End Date: ")
    print "Getting Data for Interval", date_s, "to", date_e
    params = urllib.urlencode({'key':apiKey, 'perspective':'interval', 'format':'csv', 'restrict_begin':date_s, 'restrict_end':date_e})
    u = urllib.urlopen("http://www.rescuetime.com/anapi/data", params)
    CSVdata = u.read()
    filePath = fileDirectory + "\\" + filePrefix + date_s.replace("-", "") + "-" + date_e.replace("-", "") + ".csv"
    print "Saving Data to", filePath
    f = open(filePath, "w")
    f.write(CSVdata)
    f.close()
    print "Data Saved to", filePath
    print ""

appMain()
