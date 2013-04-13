import os
import csv

class EHRVendorDataController(object):
    
    state_to_code = {"VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU", "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI", "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID", "FEDERATED STATES OF MICRONESIA": "FM", "Armed Forces Americas": "AA", "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL", "Armed Forces Africa": "AE", "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT", "MASSACHUSETTS": "MA", "PUERTO RICO": "PR", "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD", "NEW MEXICO": "NM", "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO", "Armed Forces Middle East": "AE", "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI", "WEST VIRGINIA": "WV", "WASHINGTON": "WA", "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI", "MARSHALL ISLANDS": "MH", "WYOMING": "WY", "OHIO": "OH", "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV", "LOUISIANA": "LA", "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI", "NORTH DAKOTA": "ND", "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK", "KENTUCKY": "KY", "RHODE ISLAND": "RI", "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR", "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"}
    
    lines=[]

    def __init__(self):
        CSV_FILE = os.path.join(os.path.dirname(__file__), "..","data","mu_report.csv")
        with open(CSV_FILE, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            self.lines = [line for line in reader]
            for line in self.lines:
                line['Business State/Territory'] = self.state_to_code[line['Business State/Territory'].upper()]
            
            
    def create_clean_data(self):
        with open(os.path.join(os.path.dirname(__file__), "..","data",'mu_report.min.csv'), 'wb') as test_file:
            file_writer = csv.writer(test_file)
            file_writer.writerow([key.replace(' ','') for key in self.lines[0].keys()])
            for line in self.lines[:1000]:
                file_writer.writerow([line[key] for key in line.keys()])
                
                    
if  __name__ =='__main__':
    controller = EHRVendorDataController()
    controller.create_clean_data()
        