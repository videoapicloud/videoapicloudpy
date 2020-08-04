# Python client Library for VideoAPI.cloud

## Install

```console
sudo easy_install videoapicloudpy
```

## Submitting the job

Example of `videoapicloud.conf`:

```ini
var s3 = s3://accesskey:secretkey@mybucket

set webhook = http://mysite.com/webhook/videoapicloud?videoId=$vid

-> mp4  = $s3/videos/$vid.mp4
-> webm = $s3/videos/$vid.webm
-> jpg:300x = $s3/previews/thumbs_#num#.jpg, number=3
```

Here is the python code to submit the config file:

```python
import videoapicloud
from videoapicloud import job

job = videoapicloud.job.create(
  api_key='k-api-key',
  conf='videoapicloud.conf',
  source='http://yoursite.com/media/video.mp4',
  vars={'vid': 1234}
)
```

You can also create a job without a config file. To do that you will need to give every settings in the method parameters. Here is the exact same job but without a config file:

```python
vid = 1234
s3 = 's3://accesskey:secretkey@mybucket'

job = videoapicloud.job.create(
  api_key='k-api-key',
  source='http://yoursite.com/media/video.mp4',
  webhook='http://mysite.com/webhook/videoapicloud?videoId=' + str(vid),
  outputs={
    'mp4': s3 + '/videos/video_' + str(vid) + '.mp4',
    'webm': s3 + '/videos/video_' + str(vid) + '.webm',
    'jpg:300x': s3 + '/previews/thumbs_#num#.jpg, number=3'
  }
)
```


Other example usage:

```python
# Getting info about a job
job = videoapicloud.job.get(18370773);

# Retrieving metadata
videoapicloud.job.get_all_metadata(18370773);

# Retrieving the source file metadata only
videoapicloud.job.get_metadata_for(18370773, 'source');
```

Note that you can use the environment variable `VIDEOAPICLOUD_API_KEY` to set your API key.

*Released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).*

---

* VideoAPI.cloud website: https://videoapi.cloud
* API documentation: https://videoapi.cloud/docs
* Contact: [support@videoapi.cloud](mailto:support@videoapi.cloud)
