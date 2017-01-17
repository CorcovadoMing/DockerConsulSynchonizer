import urllib2, os, json, time

def rest_get(url, raw=False):
    try:
        if raw:
            return urllib2.urlopen(urllib2.Request(url+"?raw")).read()
        else:
            return urllib2.urlopen(urllib2.Request(url)).read()
    except:
        LOG(url + " is unreachable", "WARN")
        raise

def rest_put(key, value):
    """ Key is in a url form, so no need to pass the url """
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(key, data=value)
        request.get_method = lambda: 'PUT'
        return opener.open(request)
    except:
        LOG(key + " is unreachable", "WARN")
        raise

def LOG(msg, level="INFO"):
    """ Log to stdout so far """
    print "["+time.asctime()+"][" + level + "] " + msg

def main_loop():
    source_addr = os.environ['CONSUL_SOURCE']
    target_addr = os.environ['CONSUL_TARGET']
    source_url_base = "http://"+source_addr + "/v1/kv/"
    target_url_base = "http://"+target_addr + "/v1/kv/"

    while True:
        try:
            source_keys = map(str, json.loads(rest_get(source_url_base+"docker?keys")))

            # THIS VERSION: Copy all from source
            for key in source_keys:
                value = rest_get(source_url_base+key, raw=True)
                rest_put(target_url_base+key, value)

            LOG("Synced")
        except:
            pass
        finally:
            time.sleep(3)


if __name__ == '__main__':
    main_loop()
