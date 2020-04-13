import requests
import settings



# Setting verify to False due to SSL implementation on provider's end
# Used only for the assesement context since SSL is expired it seems
# https://www.ssllabs.com/ssltest/analyze.html?d=drugtargetcommons.fimm.fi&latest
response = requests.get(settings.ENDPOINT, verify=False)

print(response.json())