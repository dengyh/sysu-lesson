import re
import json

listPattern = re.compile(r'\[(.+?)\]')

class Dict:
    def __init__(self, items):
        self.items = items

    def __getattr__(self, key):
        return self.items[key]

def parseResultOfCourseSelection(sysuer):
    source = sysuer.getResultOfCourseSelection()
    result = listPattern.search(source)
    data = json.loads(result.group())
    fields = ['kcmc', 'xf', 'kch', 'pylbm', 'kclbm', 'xnd', 'xq', 'jxbh', 'pkdw', 'kkdw']
    return list(parseFromFields(data ,fields))

def parseScore(sysuer, year, term):
    source = sysuer.getScore(year, term)
    result = listPattern.search(source)
    data = json.loads(result.group())
    fields = ['zpcj', 'xf', 'xs', 'kcywmc', 'zzcj', 'kclb', 'kcmc', 'jxbpm', 'jd', 'xnd', 'xq', 'kch']
    return list(parseFromFields(data ,fields))

def parseFromFields(data, fields):
    for item in data:
        listItem = {}
        for key in fields:
            listItem[key] = item[key]
        yield Dict(listItem)