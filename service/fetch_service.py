import settings
import logging
import requests

from service.data_service import store_data

log = logging.getLogger(__name__)

def etl():
    '''
    Base method that orchestrates the etl process
    '''
    for page in fetch_data():
        store_data(page)


def fetch_data():
    
    '''
    Fetching all the data from api in batches of 20 records. (Can be changed from .env file) 
    Implemented as generator in order to push each extracted page to the next
    step without waiting for everything to be in memory to proceed. 
    '''
    
    # Setting verify to False due to SSL implementation on provider's end
    # Used only for the assesement context since SSL seems to be expired
    # https://www.ssllabs.com/ssltest/analyze.html?d=drugtargetcommons.fimm.fi&latest
    try:
        response = requests.get(settings.BASE_URL + settings.API_ENDPOINT + settings.API_LIMIT, verify=False)
        response_time = str(round(response.elapsed.total_seconds(),2))
        log.info('Retrieved ' + settings.BASE_URL + settings.API_ENDPOINT + settings.API_LIMIT +  ' at: ' + response_time + ' seconds')
        yield response.json()['bioactivities']
        while response.json()['meta']['next']:
            response = requests.get(settings.BASE_URL + response.json()['meta']['next'], verify=False)
            response_time = str(round(response.elapsed.total_seconds(),2))
            log.info('Retrieved ' + settings.BASE_URL + response.json()['meta']['next'] +  ' at: ' + response_time + ' seconds')
            yield response.json()['bioactivities']
    except Exception as e:
        log.critical('Cannot retrieve data from ' + settings.BASE_URL + ' ' + str(e))

