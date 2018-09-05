f = open('data.csv', 'r')
l = f.read().split('\n')
while '' in l: l.remove('')
f.close()

json = ''
for line in l:
    start = line.split(',')[-2]
    end = line.split(',')[-1]
    try:
        title = line.split('"')[1]
    except:
        title = line.split(',')[0]
    json += ',\n    {\n        "title": "'
    json += title
    json += '",\n        "start": '
    json += start
    json += ',\n        "end": '
    json += end
    json += ',\n        "bar": 2,\n        "row": 0\n    }'

f = open('out', 'w')
f.write(json)
f.close()
