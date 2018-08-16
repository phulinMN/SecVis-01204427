import pandas as pd
import csv
import json
import random
df_inter = pd.read_csv('./international.csv')
df_domes = pd.read_csv('./domestic.csv')

def csv_to_json(df, name):
    asn = df.ASN.unique()
    nodes = []

    sum_bw = []
    all_sum = 0
    
    for index, i in enumerate(asn):
        n = df[df['ASN']== i]['Bandwidth'].sum() + df[df['ASN-Source']== i]['Bandwidth'].sum()
        all_sum += n
        sum_bw.append(n)
    
    for index,i in enumerate(sum_bw):
        x = i
        a = asn[index]
        j = index - 1
        while j >= 0 and sum_bw[j] > x:
            sum_bw[j+1] = sum_bw[j]
            asn[j+1] = asn[j]
            j = j - 1
        sum_bw[j+1] = x
        asn[j+1] = a

    print(all_sum)
    for index, i in enumerate(asn):
        r = lambda: random.randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())
        label = (df[df['ASN']==i]['Name'].unique())[0]
        print(label)
        node = {
            "color": color,
            "label": label,
            "x": random.randint(-1000,1000),
            "y": random.randint(-1000,1000),
            "attributes": {},
            "id": i,
            "size": (sum_bw[index]/all_sum)*300
        }
        nodes.append(node)
    edges = []
    for index, row in df.iterrows():
        edge = {
            "sourceID": row['ASN-Source'],
            "attributes": {},
            "targetID": row['ASN'],
            "size": 1
        }
        edges.append(edge)
    filejson = json.dumps({'nodes': nodes, 'edges': edges}, indent=4, separators=(',', ': '))
    with open('./' + name + '.json', 'w') as file:
        file.write(filejson)

csv_to_json(df_inter, 'international')
csv_to_json(df_domes, 'domestic')