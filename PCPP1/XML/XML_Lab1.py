"""
Objectives

improving the student's skills in parsing XML documents;
using known methods of the Element object;

Scenario

Have you seen the weather forecast for the coming week? It’ll be an extremely
sunny and warm week. Familiarize yourself with the data in the forecast.xml
file and then complete the following tasks:

Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit
method. The convert_celsius_to_fahrenheit method should convert the temperature
from Celsius to Fahrenheit. Use the following formula:

F = 9/5 * C + 32.

Create a class named ForecastXmlParser and its parse method responsible for
reading data from forecast.xml. Use the TemperatureConverter class to convert
the temperature from Celsius to Fahrenheit (rounded to one decimal place). The
parse method should print the following results:

Monday: 28 Celsius, 82.4 Fahrenheit
Tuesday: 27 Celsius, 80.6 Fahrenheit
Wednesday: 28 Celsius, 82.4 Fahrenheit
Thursday: 29 Celsius, 84.2 Fahrenheit
Friday: 29 Celsius, 84.2 Fahrenheit
Saturday: 32 Celsius, 89.6 Fahrenheit
Sunday: 33 Celsius, 91.4 Fahrenheit
"""

import xml.etree.ElementTree as ET

class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temp_celsius):
        return round(9/5*temp_celsius + 32, 1)

class ForecastXmlParser:
    def __init__(self, xml_file, tc):
        self.file = xml_file
        self.tc = tc
        self.parse()

    def parse(self):
        tree = ET.parse(self.file)
        root = tree.getroot()

        for item in root:
            day = item[0].text
            temp_in_celsius = item[1].text
            temp_in_fahrenheit = str(
                self.tc.convert_celsius_to_fahrenheit(int(item[1].text)))

            print(day + ': ' + temp_in_celsius + ' Celsius, ' +
                  temp_in_fahrenheit +' Fahrenheit')

tc = TemperatureConverter()
fxp = ForecastXmlParser('forecast.xml', tc)

"""
# Solution 2

import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0/5.0 * temperature_in_celsius + 32


class ForecastXmlParser:
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find(
                'temperature_in_celsius').text)
            temperature_in_fahrenheit = round(
                self.temperature_converter.convert_celsius_to_fahrenheit(
                    temperature_in_celsius), 1)
            print('{0}: {1} Celsius, {2} Fahrenheit'.format(
                day, temperature_in_celsius, temperature_in_fahrenheit))

temperature_converter = TemperatureConverter()
forecast_xml_parser = ForecastXmlParser(temperature_converter)
forecast_xml_parser.parse('forecast.xml')

"""


