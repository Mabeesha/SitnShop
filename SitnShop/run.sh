#!/bin/sh
echo "Running requirements"
pip install -r requirements.txt
echo "installing Solr"
curl -LO https://archive.apache.org/dist/lucene/solr/6.5.0/solr-6.5.0.tgz
mkdir solr
tar -C solr -xf solr-6.5.0.tgz --strip-components=1
cd solr
./bin/solr start                                    # start solr
./bin/solr create -c tester -n basic_config         # create core named 'tester'


./solr/bin/solr start 							solr\bin\solr.cmd restart -p 8983
python3 manage.py rebuild_index					python manage.py rebuild_index	
python3 manage.py build_solr_schema > solr/server/solr/shopcore/conf/schema.xml

python manage.py build_solr_schema > solr/server/solr/shopcore/conf/schema.xml

from market.models import *

from haystack.query import SearchQuerySet as qs
sqs = SearchQuerySet().all()
sqs.count()

sqs[0]
sqs[0].id
sqs[0].text


python3 manage.py shell

qs().filter(address="Address1")


# ./solr/bin/solr status

# Found 1 Solr nodes: 

# Solr process 5512 running on port 8983
# {
#   "solr_home":"/home/hiruna/Desktop/SitnShop/solr/server/solr",
#   "version":"6.5.0 4b16c9a10c3c00cafaf1fc92ec3276a7bc7b8c95 - jimczi - 2017-03-21 20:47:12",
#   "startTime":"2018-12-07T12:25:59.972Z",
#   "uptime":"0 days, 4 hours, 24 minutes, 43 seconds",
#   "memory":"58.1 MB (%11.8) of 490.7 MB"}
