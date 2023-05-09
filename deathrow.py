import csv 
import copy

def get_data():
    """ Reads the deathrow csv file and returns
    a list with dictionaries for each prisoner.
    """
    deathrow_data = []
    with open('tx_deathrow_full.csv', newline='') as csvfile:
        data_reader = csv.DictReader(csvfile,) 

        # count = 0 # Needed in testing phase
        for row in data_reader:
            deathrow_data.append(row)

            # count += 1
            # if count > 2: # Stopper for testing phase. 
            #     break 
    return deathrow_data 

deathrow_data = get_data()

def to_metric(deathrow_data): 
    """Creates and returns a copy of deathrow_data
    with heights and weights converted to metric values. 
    """
    metric_deathrow_data = copy.deepcopy(deathrow_data)
    # count = 0 # Needed for testing.

    for prisoner in metric_deathrow_data:
        
        # count += 1
        # if count > 2:
        #     break
        if len(prisoner['Height']) > 0 and len(prisoner['Weight']) > 0:
            split_height = prisoner['Height'].split("'")
            feet_to_cm = int((split_height[0])*12)*2.54
            inches_to_cm = int(split_height[1][:-1])*2.54
            total_height = round(feet_to_cm + inches_to_cm, 1)
            prisoner['Height'] = str(total_height) + ' cm'

            split_weight = prisoner['Weight'].split("'")
            pound_to_kg = round(float(split_weight[0])/2.2046, 1)
            prisoner['Weight'] = str(pound_to_kg) + ' kg'

    return metric_deathrow_data 

def county_statistics(deathrow_data):
    """Creates a dictionary with the number of executed
    prisoners in a county.
    """
    county_data = {}
    for prisoner in deathrow_data: 
        if prisoner['County'] in county_data: 
            county_data[prisoner['County']] += 1 
        else: county_data[prisoner['County']] = 1 
    return county_data   

def native_statistics(deathrow_data):
    """ Creates a dictionary with the number of executed
    prisoners from each native county. 
    """
    native_data = {}
    for prisoner in deathrow_data: 
        if prisoner['Native County'] in native_data: 
            native_data[prisoner['Native County']] += 1 
        else: native_data[prisoner['Native County']] = 1 
    return native_data   

def last_words_search(deathrow_data, words):
    """ Searches every Last Statement dictionary entry for each word
    in the given list words. Returns a tuple with the prisoner's info
    if just one of the words is found.
    """
    search_results = []
    for prisoner in deathrow_data:
        statement = prisoner['Last Statement'].split(" ")
        for word in words: 
            if word in statement:
                prisoner_tuple = (prisoner['First Name']
                , prisoner['Date of Birth']
                , prisoner['Last Statement'])
                search_results.append(prisoner_tuple)

    unique_prisoners = []
    for prisoner in search_results:
        if prisoner not in unique_prisoners:
            unique_prisoners.append(prisoner)

    return unique_prisoners
