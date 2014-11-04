a Python client for the OpenBTS NodeManager,
providing access to components in the OpenBTS application suite:
SMQueue, SIPAuthServe, and OpenBTS itself.


### requirements
* OpenBTS 5.0 public alpha (tested on `11465a2`)
* Python 2.7


### installation

```shell
$ pip install openbts
```


### usage

```python
import openbts

# read a config value from SMQueue
smqueue_connection = openbts.components.SMQueue()
response = smqueue_connection.read_config('Bounce.Code')
print response.data['value']
# 101

# update an SIPAuthServe config value
sipauthserve_connection = openbts.components.SIPAuthServe()
response = sipauthserve_connection.update_config('Log.Alarms.Max', 12)
print response.code
# 204

# get realtime OpenBTS monitoring data
openbts_connection = openbts.components.OpenBTS()
response = openbts_connection.monitor()
print response.data['noiseRSSI']
# -67
```

see additional examples in `integration_test.py`


### license
MIT


### releases
* 0.0.2 - config reading and updating for the OpenBTS component
* 0.0.1 - barebones setup for pypi


### resources
* see the [OpenBTS 4.0 manual](http://openbts.org/site/wp-content/uploads/2014/07/OpenBTS-4.0-Manual.pdf)
* and the [NodeManager source](https://github.com/RangeNetworks/NodeManager) from Range


### testing
run unit tests with `nose`:

```shell
$ nosetests --detailed-errors
```

We have quite a few similar unit tests between components.
Many could be written against `openbts.core.BaseComponent`, as the components
all inherit from this single class.  But it seems better to individually
inspect the functionality of each class in `openbts.components`. Anyway,
onward..

Running the integration tests requires one to have a live OpenBTS instance
running on the same machine.  The test will modify real system parameters,
so run it with caution, or better yet, run it against a system not in prod.

```shell
$ python integration_test.py
```


### release process
you need a ~/.pypirc like this:

```
[distutils]
index-servers =
  pypi

[pypi]
repository: https://pypi.python.org/pypi
username: yosemitebandit
password: mhm
```

bump the versions in `setup.py` and in this file, then run:

```shell
$ git tag 0.0.1 -m 'openbts-python v0.0.1'
$ git push origin master --tags
$ python setup.py sdist upload -r pypi
```
