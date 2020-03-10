import csv
import os
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
file_path = os.path.join("Resources", "employee_data.csv")
output_path = os.path.join("Output","PyBoss_output.csv")

with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column header)
    csvwriter.writerow(['Emp ID','First Name', 'Last Name', 'DOB', 'SSN', 'State'])

with open(file_path, 'r') as file_handle:
    csv_handle = csv.reader(file_handle, delimiter=',')
    header = next(csv_handle)

    for row in csv_handle:
        name =  row[1].split(" ")
        first_name = name[0]
        last_name = name[1]
        dob = row[2].split("-")
        dob_new_fmt = (f'{dob[1]}/{dob[2]}/{dob[0]}')
        ssn = row[3].split("-")
        ssn_masked = (f'***-**-{ssn[2]}')
        state = us_state_abbrev[row[4]]
        
        with open(output_path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([row[0], first_name, last_name, dob_new_fmt, ssn_masked, state])        


