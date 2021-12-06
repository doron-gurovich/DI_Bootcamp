# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:41:22 2021

@author: 97250
"""

import random

class Company():
    
    company_dict = {
        "QA": "Qatar Airways",
        "SA": "Singapore Airlines",
        "JA": "Japan Airlines",
        "CA": "Cathay Pacific Airways",
        "EA": "EVA Air",
        "HA": "Hainan Airlines",
        "AF": "Air France"
    }
    
    def __init__(self, company_id, name):
        self.company_id = company_id
        self.name = name
        
        self.planes = []
        
        for k1, v1 in Company.company_dict.items():
            for k2, v2 in Airplane.airplane_dict.items():
                if v1 == name and v1 == v2:
                    self.planes.append(k2)
        
    
class Airplane():
    
    airplane_dict = {
        "Douglas DC-3": "Qatar Airways",
        "Boeing 727": "Singapore Airlines",
        "Boeing 737": "Singapore Airlines",
        "Boeing 747": "Singapore Airlines",
        "Boeing 757": "Japan Airlines",
        "Boeing 777": "Cathay Pacific Airways",
        "Airbus A320": "EVA Air",
        "Airbus A330": "Hainan Airlines",
        "Cessna 172": "Air France"
        }
    
    def __init__(self, airplane_id, company, current_location):
        self.airplane_id = airplane_id
        self.current_location = current_location
        self.company = company
        
        self.next_flight = []

    def fly(self, destintion):
        pass
    
    def location_on_date(self, date):
        result = False
        
        return result
    
    def available_on_date(self, date, location):
        result = False
        
        if self.location_on_date(date) == location:
            result = True
        
        return result


class Flight():
    def __init__(self, flight_id, date, destination, origine, plane):
        self.flight_id = flight_id
        self.date = date
        self.destination = destination
        self.origine = origine
        self.plane = plane
        
    def take_off(self):
        pass
    
    def land(self):
        pass

class Airport():
    
    location_dict = {
        "CAN": "Guangzhou",
        "ATL": "Atlanta", 
        "CTU": "Sichuan", 
        "DFW": "Dallas", 
        "CKG": "Yubei", 
        "PEK": "Beijing", 
        "HND": "Tokyo", 
        "ORD": "Chicago"
        }
    
    def __init__(self, airport_id, city):
        self.airport_id = airport_id
        self.city = city
        
        self.scheduled_departures = []
        self.scheduled_arrivals = []
        
    def schedule_flight(self,datetime, other):
        
        self.scheduled_departures.append((datetime, other))
        other.scheduled_arrivals.append((datetime, self))
        
        return True
    
    def info(self, start_date, end_date):

        result_departue = ' '.join([el for el in self.scheduled_departue if el[0] in range(start_date, end_date)])
        result_arrivals = ' '.join([el for el in self.scheduled_arrivals if el[0] in range(start_date, end_date)])
                
        print(result_arrivals, result_departue)
        
        return True

### -----------------------------MAIN---------------------------------------

Companies_list = []

for k, v in Company.company_dict.items():
    Companies_list.append(Company(k, v))

Airplanes_list = []

for k, v in Airplane.airplane_dict.items():
    Airplanes_list.append(Airplane(k, v, random.choice(list(Airplane.airplane_dict.values()))))

Airpots_list = []

for k, v in Airport.location_dict.items():
    Airpots_list.append(Airport(k, v))