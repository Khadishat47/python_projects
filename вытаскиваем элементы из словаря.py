from pprint import pprint
def format_name_list(names: list):
    d=''
    if len(names)>1:
        for i in range(len(names)-1):
            d+=names[i]['name']+ ', '
        return (d[:-2]+' и '+names[-1]['name'])
    elif len(names)==1:
        d+=names[0]['name']
        return d
    else:
        return d

names=[{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]

pprint(type(format_name_list(names)))
