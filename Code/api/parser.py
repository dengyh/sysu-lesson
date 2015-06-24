import re
import json

listPattern = re.compile(r'\[(.+?)\]')

class Dict:
    def __init__(self, items):
        self.items = items

    def __getattr__(self, key):
        return self.items[key]

    def __getitem__(self, key):
        return self.items[key]

    def set(self, key, value):
        self.items[key] = value

def parseResultOfCourseSelection(sysuer):
    source = sysuer.getResultOfCourseSelection()
    result = listPattern.search(source)
    data = json.loads(result.group())
    fields = ['kcmc', 'xf', 'kch', 'pylbm', 'kclbm', 'xnd', 'xq', 'jxbh', 'pkdw', 'kkdw', 'xm', 'sksjdd']
    return list(parseFromFields(data ,fields))

def parseScore(sysuer, year, term, type):
    source = sysuer.getScore(year, term, type)
    result = listPattern.search(source)
    data = json.loads(result.group())
    fields = ['zpcj', 'xf', 'xs', 'kcywmc', 'zzcj', 'kclb', 'kcmc', 'jxbpm', 'jd', 'xnd', 'xq', 'kch', 'kclbm']
    return list(parseFromFields(data ,fields))

def parseFromFields(data, fields):
    for item in data:
        listItem = {}
        for key in fields:
            listItem[key] = item.get(key, '')
        yield Dict(listItem)
