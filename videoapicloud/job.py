import json
import os
import httplib2
import base64
from videoapicloud import config

USER_AGENT = 'VideoAPIcloud/1.0.0 (Python)'

def videoapicloud_url():
  return os.getenv('VIDEOAPICLOUD_URL', 'https://api.videoapi.cloud')

def get_authorization_header(api_key):
  if api_key is None:
    api_key = os.getenv('VIDEOAPICLOUD_API_KEY')
  if api_key is None:
    raise ValueError('API key must be specified using the api_key parameter or the VIDEOAPICLOUD_API_KEY environment variable')

  b_api_key = '%s:' % api_key
  return 'Basic ' + base64.b64encode(b_api_key.encode('utf-8')).decode('utf-8')

def submit(config_content, **kwargs):
  h = httplib2.Http()

  headers = {'User-Agent': USER_AGENT, 'Content-Type': 'text/plain', 'Accept': 'application/json'}
  headers['Authorization'] = get_authorization_header(kwargs.get('api_key'))

  response, content = h.request(videoapicloud_url() + '/v1/job', 'POST', body=config_content, headers=headers)

  return json.loads(content.decode('utf-8'))

def api_get(path, api_key=None):
  h = httplib2.Http()

  headers = {'User-Agent': USER_AGENT, 'Content-Type': 'text/plain', 'Accept': 'application/json'}
  headers['Authorization'] = get_authorization_header(api_key)

  response, content = h.request(videoapicloud_url() + path, 'GET', None, headers=headers)

  if response.status == 200:
    return json.loads(content.decode('utf-8'))
  else:
    return None

def create(**kwargs):
  return submit(config.new(**kwargs), **kwargs)

def get(jid, **kwargs):
  return api_get('/v1/jobs/' + str(jid), **kwargs)

def get_all_metadata(jid, **kwargs):
  return api_get('/v1/metadata/jobs/' + str(jid), **kwargs)

def get_metadata_for(jid, source_or_output, **kwargs):
  return api_get('/v1/metadata/jobs/' + str(jid) + '/' + source_or_output, **kwargs)
