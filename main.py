import csv
import convertor


def convert_temperature(target_temp):
    with open('temperature.csv', 'r') as file:
        reader = csv.DictReader(file)

        with open('converted_temperature.csv', 'w') as output_file:
            fieldnames = ['Date', 'Reading']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:                
                temp_str = row['Reading']               
                number = int(''.join(filter(str.isdigit, temp_str.strip())))                
                unit = temp_str[-1:]              
                rest_number = number

                if (target_temp == 'C'):
                    if (unit == 'F'):
                        rest_number = int(convertor.temperature.
                                          convert_fahrenheit_to_celsius(number))                      
                elif (target_temp == 'F'):
                    if (unit == 'C'):
                        rest_number = int(convertor.temperature.
                                          convert_celsius_to_fahrenheit(number))                      

                writer.writerow({'Date': row['Date'], 'Reading':
                                 str(rest_number) + '°' + target_temp})
    

# convert_temperature('C')
convert_temperature('F')
