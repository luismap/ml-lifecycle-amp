!pip install --upgrade pip
!pip install --no-cache-dir --log install-deps-logs/pip-req.log -r 01-install-dep/requirements.txt
import os
#get domain and package location
domain = os.environ["CDSW_DOMAIN"]
#create a cml api key, and add it as an env var
cml_api_key = os.environ["cml_api_key"]
v2api = f"https://{domain}/api/v2/python.tar.gz"

!pip install $v2api
