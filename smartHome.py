import argparse
import tempSensor.tempSensor as ts



parser = argparse.ArgumentParser()
parser.add_argument("--tempRecord", help="Record temperature reading", action="store_true")
parser.add_argument("--loadDrivers", help="Load the Drivers",  action="store_true")
args = parser.parse_args()



if args.tempRecord:
    tmp = ts.temperatureSensor()
    tmp.testOutput()
    if args.loadDrivers:
        tmp.loadDrivers()
    tmp.recordTemp()
