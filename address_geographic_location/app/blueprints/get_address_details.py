from flask import request, Blueprint

from app.api_manager.address_details_processing import AccessGeometricData
from app.helper.app_logger import logger

address_details = Blueprint('address_details', __name__)

"""
The below method gets address and output format from form data and instantiate the AccessGeometricData
class and then calls it get_address_lat_lng property which returns the required output.
"""


@address_details.route('/getAddressDetails', methods=['POST'])
def get_address_details():
    try:
        address = request.form['address']
        output_format = request.form['output_format']
        response = AccessGeometricData(address=address, output_format=output_format)
        return response.get_address_lat_lng()
    except Exception as ex:
        print('exception in get_address_details method: {}'.format(str(ex)))
        logger.error('exception in get_address_details method:{}'.format(str(ex)))
