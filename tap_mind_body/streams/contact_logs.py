from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ContactLogsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'contact_logs'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['clients']
    RESPONSE_KEY = 'ContactLogs'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'Client',
        'Staff',
        'ClientCreditCard',
        'ClientRelationship',
        'Liability',
        'SalesRep',
        'Appointment',
        'Unavailability' ,
        'Availability',
        'Relationship',
        'Resource',
        'SessionType',
        'Program',
        'Location',
        'Amenity'
    ]
        
    @property
    def path(self):
        return '/client/contactlogs'
        
    def get_params(self, client_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClientID': client_id
        }
        return params       
    