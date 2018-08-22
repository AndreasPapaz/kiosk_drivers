import math
import csv
import pandas
# our kitchen on Lake and Racine Ave (41.8851024,-87.6618988)
class KioskMap(object):
    def __init__(self, csv=None):
        self.depot = None
        self.addresses = csv

    def read_csv(self, csv):
        with open(csv, 'rb') as file:
            # spam_read = file.read()
            spamreader = csv.reader(file, delimiter=' ', quotechar='|')
            for line in spam_read:
                print line
            import ipdb; ipdb.set_trace()
