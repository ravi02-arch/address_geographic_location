import xml.etree.ElementTree as ET
from xml.dom import minidom

import requests

from app.configs.security_key_config import API_key
from app.configs.url_config import google_apis_url as url
from app.helper.app_logger import logger

"""
The AccessGeometricData class takes in two parameters address and output_format and has multiple methods to 
return latitude and longitude along with address in asked format either json or xml.
"""


class AccessGeometricData:
    def __init__(self, address, output_format):
        self.__address = address
        self.__output_format = output_format

    def get_address_lat_lng(self):
        """
        this method requests the maps.googleapis.com url to get
        geometric data for requested address and calls __process_google_apis_response
        method to return processed response
        :return:
        """
        try:
            querystring = {"address": self.__address,
                           "key": API_key}
            self.__response = requests.request("GET", url + self.__output_format, params=querystring)
            result = self.__process_google_apis_response()
            return result
        except Exception as ex:
            print("error in get_address_location method: {}".format(ex))
            logger.error("error in get_address_location method: {}".format(ex))

    def __process_google_apis_response(self):
        """
        this method calls the required method depending on output_format either __get_json_response
        or __get_xml_response
        :return:
        """
        try:
            if self.__output_format == 'json':
                return self.__get_json_response()
            elif self.__output_format == 'xml':
                return self.__get_xml_response()
        except Exception as ex:
            print("error in process_google_apis_response method: {}".format(ex))
            logger.error("error in process_google_apis_response method: {}".format(ex))

    def __get_json_response(self):
        """
        this method processes the json response
        :return:
        """
        try:
            final_dictionary = {}
            final_dictionary["coordinates"] = self.__response.json()["results"][0]["geometry"]["location"]
            final_dictionary["address"] = self.__address
            return final_dictionary
        except Exception as ex:
            print("error in get_json_response method: {}".format(ex))
            logger.error("error in get_json_response method: {}".format(ex))

    def __get_xml_response(self):
        """
        this method processes the xml response
        :return:
        """
        try:
            xml_doc = {}
            string_xml = self.__response.content
            myroot = ET.fromstring(string_xml)
            for item in myroot.findall('./result/geometry/location/'):
                xml_doc[item.tag] = item.text

            root = ET.Element("root")
            ET.SubElement(root, "address").text = self.__address
            coordinates = ET.SubElement(root, "coordinates")
            ET.SubElement(coordinates, "lat").text = xml_doc['lat']
            ET.SubElement(coordinates, "lng").text = xml_doc['lng']
            rough_string = ET.tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            return reparsed.toprettyxml(encoding="UTF-8")
        except Exception as ex:
            print("error in get_xml_response method: {}".format(ex))
            logger.error("error in get_xml_response method: {}".format(ex))
