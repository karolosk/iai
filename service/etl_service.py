import settings
import logging
import requests

log = logging.getLogger(__name__)


def fetch_data():
    
    '''
    Fetching all the data from api in the default batches of 20 records. 
    Implemented as generator in order to push each extracted page to the next
    step without waiting for everything to be in memory to proceed. 
    '''
    
    # Setting verify to False due to SSL implementation on provider's end
    # Used only for the assesement context since SSL seems to be expired
    # https://www.ssllabs.com/ssltest/analyze.html?d=drugtargetcommons.fimm.fi&latest
    response = requests.get(settings.BASE_ENDPOINT + settings.API_ENDPOINT, verify=False)
    respTime = str(round(response.elapsed.total_seconds(),2))
    log.info('Retrieved ' + settings.BASE_ENDPOINT + settings.API_ENDPOINT +  ' at: ' + respTime + ' seconds')
    yield response.json()
    while response.json()['meta']['next']:
        response = requests.get(settings.BASE_ENDPOINT + response.json()['meta']['next'], verify=False)
        respTime = str(round(response.elapsed.total_seconds(),2))
        log.info('Retrieved ' + settings.BASE_ENDPOINT + settings.API_ENDPOINT +  ' at: ' + respTime + ' seconds')
        yield response.json()

def etl():
    '''
    Base method that orchestrates the etl process
    '''
    i = 0
    for page in fetch_data():
        i = i+1
        print(i)