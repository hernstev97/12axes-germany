import xml.etree.ElementTree as ET
from pathlib import Path

def pages(path):
    root=ET.parse(path).getroot()
    out=[]
    for p in root.findall('.//{*}page'):
        out.append([dict(text=w.text or '',x0=float(w.attrib['xMin']),x1=float(w.attrib['xMax']),y0=float(w.attrib['yMin']),y1=float(w.attrib['yMax'])) for w in p.findall('.//{*}word')])
    return out

def lines(words):
    result=[]
    for w in sorted(words,key=lambda w:(w['y0'],w['x0'])):
        match=next((l for l in result if abs(l[0]['y0']-w['y0'])<2.1),None)
        if match is None:result.append([w])
        else:match.append(w)
    return [sorted(l,key=lambda w:w['x0']) for l in result]

def extract(words):
    return '\n'.join(' '.join(w['text'] for w in l) for l in lines(words))

def select(words,rect):
    x0,y0,x1,y1=rect
    # y interval selects the word's upper edge; complete token bbox is retained.
    return [w for w in words if w['x0']>=x0-.2 and w['x1']<=x1+.2 and w['y0']>=y0-.2 and w['y0']<y1]

if __name__=='__main__':
    q=pages(Path(__file__).parent/'questionnaire.bbox.html')
    for p in range(17,32):
        print('PAGE',p)
        for l in lines(q[p-1]):
            print(f"{l[0]['y0']:.1f} "+' '.join(f"{w['text']}[{w['x0']:.0f}]" for w in l))
