#!/usr/bin/env python3
"""Controlled-path, public-document-only C annotation builder. No ESS answer reader."""
import argparse,csv,hashlib,json,re,subprocess,sys
from pathlib import Path
from source_geometry import pages,lines,select,extract

ROOT=Path(__file__).resolve().parents[2]
OWN=ROOT/'outputs/public-reproduction/c-v2'
CACHE=OWN/'sources'
TARGET=OWN/'annotation.json'
PINS={
 'ESS11-DE-QUESTIONNAIRE':('questionnaire','ESS11_questionnaires_DE.pdf','be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75'),
 'ESS11-DE-SHOWCARDS':('showcards','ESS11_showcards_DE.pdf','786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca'),
 'ESS11-CODEBOOK':('codebook','ESS11_appendix_a7_e04_1.pdf','b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35')}
def sha(b):return hashlib.sha256(b).hexdigest()
def field(value,evidence,status='ORIGINAL_GELESEN_AUTORENFASSUNG_REVIEW_OFFEN'):
 return {'wert':value,'status':status,'belege':evidence if isinstance(evidence,list) else [evidence]}

# Own manual source-page configuration after original text and visual reading.
# page, end of question paragraph, category top/bottom, code-column x, list, layout
CONFIG={
1:(17,129,151,202,None,20,'horizontal'),2:(17,266,277,445,387,21,'vertical'),3:(17,531,541,710,394,22,'vertical'),
4:(18,90,106,237,394,23,'vertical'),5:(18,314,326,399,394,None,'vertical'),6:(18,478,501,612,394,None,'vertical'),
7:(19,102,113,243,394,None,'vertical'),8:(19,340,364,456,394,None,'vertical'),9:(19,579,590,668,None,24,'horizontal'),
10:(20,64,75,153,None,24,'horizontal'),11:(20,228,242,320,384,None,'vertical'),12:(20,419,430,672,383,None,'vertical'),
13:(21,89,104,182,384,None,'vertical'),14:(21,245,256,510,383,None,'vertical'),15:(21,607,618,684,None,25,'horizontal'),
16:(22,90,107,275,387,26,'vertical'),17:(22,366,380,548,387,26,'vertical'),18:(22,627,642,720,384,None,'vertical'),
19:(23,77,132,357,387,None,'vertical'),20:(23,429,446,520,394,None,'vertical'),21:(23,587,636,710,381,None,'vertical'),
22:(24,82.3,132,160,394,None,'entry'),23:(24,223,281,309,381,None,'entry'),24:(24,397,459,487,394,None,'entry'),
25:(24,538,548,635,394,None,'vertical'),26:(25,64,101,207,386,None,'vertical'),27:(25,272.2,322,350,394,None,'entry'),
28:(25,412,462,569,386,None,'vertical'),29:(25,633.5,684,712,394,None,'entry'),30:(26,115,126,318,385,27,'vertical'),
31:(26,410,421,504,None,28,'horizontal'),32:(26,553,564,706,307,29,'vertical'),33:(27,115,127,180,302,None,'vertical'),
34:(27,289,300,544,394,30,'vertical'),35:(28,89,113,357,394,30,'vertical'),36:(28,429,440,684,394,30,'vertical'),
37:(29,102,113,247,394,31,'vertical'),38:(29,313,324,458,394,31,'vertical'),39:(29,498,509,643,394,31,'vertical'),
40:(30,102,126,260,394,32,'vertical'),41:(30,332,355,490,394,32,'vertical'),42:(30,543,566,700,394,32,'vertical'),
43:(31,140,151,278,393,None,'vertical')}
HLABELS={
1:{'00':(33,151,150,180),'10':(390,151,449,180),'77':(450,151,523,180),'88':(525,151,575,180)},
9:{'00':(38,590,150,643),'10':(350,615,443,643),'77':(447,615,516,643),'88':(520,615,560,643)},
10:{'00':(38,75,150,129),'10':(340,100,443,129),'77':(447,100,516,129),'88':(520,100,560,129)},
15:{'00':(33,618,150,659),'10':(400,631,450,659),'77':(453,631,523,659),'88':(525,631,575,659)},
31:{'00':(28,421,150,449),'10':(385,421,448,449),'77':(453,421,525,449),'88':(529,421,570,449)}}

# Context is selected separately from response captions and question wording.
# name, page, rectangle, type, exact applicable item numbers.
CONTEXTS=[
('intro-person-life',17,(28,75,565,90),'einleitung',range(1,30)),
('intro-personal',19,(28,50,565,64),'einleitung',range(7,30)),
('intro-attachment',19,(28,501,570,530),'einleitung',[9,10]),
('c12-filter',20,(28,367,565,379),'filter',[12]),
('c12-interviewer',20,(28,380,570,405.3),'interviewer',[12]),
('c13-filter',21,(28,50,580,75.3),'filter',[13,14]),
('c14-filter',21,(28,218,565,231),'filter',[14]),
('all-c15',21,(28,555,565,568),'an-alle',range(15,19)),
('c19-filter',23,(28,50,565,62.6),'filter',[19]),
('c19-interviewer',23,(71,75,565,115),'interviewer',[19]),
('all-c20',23,(28,402,565,415),'an-alle',[20,21]),
('c21-geography',23,(28,585,570,625),'interviewer',[21]),
('c22-filter',24,(28,50,565,63),'filter',[22,23]),
('c22-coding',24,(67,82,565,96),'eingabe-kodieranweisung',[22]),
('c22-entry',24,(28,107,565,122),'eingabe-kodieranweisung',[22]),
('c23-geography',24,(28,221,570,247.1),'interviewer',[23]),
('c23-entry',24,(28,247,565,261),'eingabe-kodieranweisung',[23]),
('all-c24',24,(28,345,565,358),'an-alle',[24,25,26]),
('c24-coding',24,(67,396,565,411),'eingabe-kodieranweisung',[24]),
('c24-entry',24,(28,421,565,450),'eingabe-kodieranweisung',[24]),
('c26-geography',25,(28,62,570,101),'interviewer',[26]),
('c27-filter',25,(28,246,565,259.2),'filter',[27]),
('c27-coding',25,(67,272,565,286),'eingabe-kodieranweisung',[27]),
('c27-entry',25,(28,297,565,312),'eingabe-kodieranweisung',[27]),
('all-c28',25,(28,386,565,398.9),'an-alle',[28]),
('c28-geography',25,(28,411,570,451),'interviewer',[28]),
('c29-filter',25,(28,607,565,620.6),'filter',[29]),
('c29-coding',25,(67,633,565,648),'eingabe-kodieranweisung',[29]),
('c29-entry',25,(28,658,565,674),'eingabe-kodieranweisung',[29]),
('all-c30',26,(28,50,565,62),'an-alle',[30]),
('intro-climate',26,(28,62,565,77),'einleitung',range(30,43)),
('c31-filter-not55',26,(28,358,565,372),'filter',range(31,43)),
('c33-randomisation',27,(28,50,570,89),'interviewer-administration',range(33,43)),
('c34-group1',27,(28,224,565,236.6),'filter',[34,35,36]),
('c37-group2',29,(28,50,565,62.6),'filter',[37,38,39]),
('c40-group3',30,(28,50,565,62.6),'filter',[40,41,42]),
('all-c43',31,(28,50,565,62),'an-alle',[43]),
('intro-eu',31,(28,62,565,77),'einleitung',[43])]
ROUTES={
11:[(['1'],'C12',(410,242,520,258)),(['2','7','8'],'C13',(410,283,520,299))],
12:[(['01','02','21','22','03','04','05','06','07','08','09','77'],'C15',(424,487,530,502))],
13:[(['1'],'C14',(410,104,520,120)),(['2','7','8'],'C15',(410,146,520,162))],
14:[(['01','02','21','22','03','04','05','06','07','08','09','77'],'C15',(424,313,530,328))],
18:[(['1'],'C19',(407,642,520,658)),(['2','7','8'],'C20',(407,683,520,699))],
21:[(['1'],'C24',(409,636,520,652)),(['2'],'C22',(409,656,520,672)),(['7','8'],'C24',(409,688,520,703))],
26:[(['1'],'C28',(414,101,520,135)),(['2'],'C27',(414,139,520,167)),(['7','8'],'C28',(414,178,520,208))],
28:[(['1'],'C30',(414,462,520,496)),(['2'],'C29',(414,501,520,529)),(['7','8'],'C30',(414,539,520,569))],
30:[(['01','02','03','04','05'],'C31',(407,176,530,191)),(['55'],'EINLEITUNG VOR C43',(407,257,565,287)),(['77','88'],'C31',(407,296,530,311))],
33:[(['1'],'C34',(329,127,440,142)),(['2'],'C37',(329,147,440,161)),(['3'],'C40',(329,166,440,181))],
36:[(None,'EINLEITUNG VOR C43',(28,740,565,754))],
39:[(None,'EINLEITUNG VOR C43',(28,703,565,718))],
43:[(None,'MODUL D',(33,289,565,303))]}

class Builder:
 def __init__(self,work):
  self.work=work;self.sources={};self.evidence={}
  provenance=json.loads((ROOT/'data/inventar.provenienz.json').read_text())
  self.source_meta=provenance['sources']
  for sid,(stem,filename,pin) in PINS.items():
   source=CACHE/filename
   if sha(source.read_bytes())!=pin:raise ValueError('SOURCE PIN MISMATCH '+sid)
   bbox=work/(stem+'.bbox.html')
   args=['pdftotext','-bbox',str(source),str(bbox)]
   r=subprocess.run(args,capture_output=True,text=True)
   with (OWN/'tool-exits.jsonl').open('a') as f:f.write(json.dumps({'command':args,'exit':r.returncode,'output':r.stdout+r.stderr})+'\n')
   if r.returncode:raise RuntimeError('Poppler extraction failed')
   self.sources[sid]=pages(bbox)
 def ev(self,key,sid,page,words,scope,rect=None):
  if not words:raise ValueError('EMPTY EVIDENCE '+key)
  value=extract(words)
  self.evidence[key]={'evidence_id':key,'quelle_id':sid,'quelle_sha256':PINS[sid][2],
   'pdf_seite':page,'gedruckte_seite':page-1 if sid=='ESS11-CODEBOOK' else (page if sid=='ESS11-DE-QUESTIONNAIRE' else None),
   'gedruckte_fundstelle':scope,'region_pdf_points':rect,'tokenauswahl':words,
   'originalextrakt':value,'originalextrakt_sha256':sha(value.encode()),'umfang':scope,'region_selection':'word upper edge in y interval; full x extent within rectangle; 0.2 PDF point lower/x tolerance; full source token bbox retained',
   'lektuerestatus':'AUTOR_ORIGINAL_GELESEN','unabhaengige_pruefung':'NICHT_GEPRUEFT','lektueredatum':'2026-10-03'}
  return key
 def region(self,key,sid,page,rect,scope):return self.ev(key,sid,page,select(self.sources[sid][page-1],rect),scope,rect)
 def value(self,key):return self.evidence[key]['originalextrakt']
 def codebook(self,var):
  sid='ESS11-CODEBOOK';ps=self.sources[sid]
  if not hasattr(self,'cbanchors'):
   self.cbanchors=[]
   for p,ws in enumerate(ps,1):
    for line in lines(ws):
     if len(line)>1 and line[0]['x0']<90 and re.fullmatch(r'[a-z][a-z0-9_]+',line[0]['text']) and line[1]['text']=='-':
      self.cbanchors.append((line[0]['text'],p,line[0]['y0']))
  anchors=self.cbanchors
  hit=next((i for i,a in enumerate(anchors) if a[0]==var),None)
  if hit is None:raise ValueError('CODEBOOK VARIABLE ABSENT '+var)
  _,page,y=anchors[hit];_,endp,endy=anchors[hit+1]
  # Metadata only. Explicitly omit long international lookup tables, while retaining their header coding/anonymisation notices.
  segments=[]
  for p in range(page,endp+1):
   words=[w for w in ps[p-1] if w['y0']>= (y-.1 if p==page else 60) and w['y1']< (endy if p==endp else 730)]
   if not words:continue
   metadata=[]
   for l in lines(words):
    if re.fullmatch(r'\d+',l[0]['text']) and l[0]['x0']<145:break
    if l[0]['text']=='International':break
    # The separate lookup table begins with its own Applies-to heading.
    if var == 'lnghom2' and ' '.join(w['text'] for w in l).startswith('Applies to variable lnghom2.'):break
    metadata+=l
   if metadata:
    eid=self.ev(f'CB41-{var}-metadata-{p}',sid,p,metadata,f'{var}: eigene Lektüre von Variablenkopf und Metadaten; keine Datendateiprüfung')
    segments.append(eid)
   # Country/language lookup table is not this annotation's category list.
   if var in {'cntbrthd','fbrncntc','mbrncntc','lnghom1','lnghom2'}:break
  loc=[];loc_be=[]
  for eid in segments:
   for l in lines(self.evidence[eid]['tokenauswahl']):
    if l[0]['text']=='Location':
     ws=l[1:];le=self.ev(f'CB41-{var}-location',sid,self.evidence[eid]['pdf_seite'],ws,f'{var}: gedruckte Location-Zelle')
     loc.append(extract(ws));loc_be.append(le)
  if not loc:raise ValueError('CODEBOOK LOCATION ABSENT '+var)
  result={'variable':field(var,segments,'DOKUMENTATION_4_1_KANDIDAT_DATENABGLEICH_4_2_OFFEN'),
   'location':field(loc[0],loc_be,'DOKUMENTATION_4_1_LOCATION_GELESEN'),
   'metadaten':field('\n'.join(self.value(e) for e in segments),segments,'DOKUMENTATION_4_1_TEILLEKTUERE_KOPF_FILTER_BESCHREIBUNG'),
   'lookup_tabellen':{'status':'NICHT_IN_DIE_DEUTSCHEN_ORIGINALKATEGORIEN_UEBERNOMMEN','grund':'Öffene Originaleingaben und spätere Anonymisierung bleiben gesondert abzugleichen'} if var in {'cntbrthd','fbrncntc','mbrncntc','lnghom1','lnghom2'} else None}
  # Read and geometrically serialize finite codebook categories, including continuation pages.
  if var not in {'cntbrthd','fbrncntc','mbrncntc','lnghom1','lnghom2','livecnta'}:
   cats=[];last=None
   for p in range(page,endp+1):
    ws=[w for w in ps[p-1] if w['y0']>= (y-.1 if p==page else 60) and w['y1']< (endy if p==endp else 730)]
    for l in lines(ws):
     if l[0]['x0']<145 and re.fullmatch(r'\d+',l[0]['text']):
      last={'code':l[0],'label':l[1:],'page':p};cats.append(last)
     elif last and l[0]['x0']>=145 and l[0]['x0']<170:last['label']+=l
   result['antwortkategorien_dokumentation41']=[]
   for cat in cats:
    c=cat['code']['text'];eid=self.ev(f'CB41-{var}-code-{c}',sid,cat['page'],[cat['code']],f'{var}: Codezelle {c}')
    lab=self.ev(f'CB41-{var}-label-{c}',sid,cat['page'],cat['label'],f'{var}: Labelzelle zu Code {c}')
    result['antwortkategorien_dokumentation41'].append({'code':field(c,eid),'label':field(self.value(lab),lab)})
  return result
 def build(self):
  rows=list(csv.DictReader((ROOT/'data/inventar.entwurf.csv').open()));cs=[r for r in rows if re.fullmatch(r'C\d+',r['frage_id'])]
  assert [r['frage_id'] for r in cs]==[f'C{i}' for i in range(1,44)]
  Q='ESS11-DE-QUESTIONNAIRE';S='ESS11-DE-SHOWCARDS';questions=[];contexts={i:[] for i in CONFIG}
  for name,page,rect,kind,applies in CONTEXTS:
   eid=self.region('QCTX-'+name,Q,page,rect,'Deutsches Original: '+name)
   for i in applies:contexts[i].append({'typ':kind,'text':field(self.value(eid),eid),'herkunft':'direkt' if i==list(applies)[0] else 'geerbt_im_quellenablauf','quellenposition_vor_item':f'C{list(applies)[0]}','gilt_im_annotierten_ablauf_fuer':[f'C{n}' for n in applies],'geltung':'Annotation des Originalablaufs, kein Auswertungsvertrag'})
  for r in cs:
   i=int(r['frage_id'][1:]);fid=r['frage_id'];page,qend,ctop,cbottom,cx,listno,layout=CONFIG[i];ws=self.sources[Q][page-1]
   anchor=next(w for w in ws if w['text']==fid and w['x0']<50)
   ident=self.ev(fid+'-identity',Q,page,[anchor],fid+' Originalmarker')
   qw=[w for w in ws if w['y0']>=anchor['y0']-.05 and w['y1']<=qend and w['x0']>=60]
   # LISTE/WEITER are separately retained instructions, not part of the question stem.
   ordered=lines(qw)
   if not ordered:raise ValueError('EMPTY WORDING '+fid)
   first=ordered[0];prefix=[]
   while first and first[0]['text'] in {'WEITER','LISTE'}:
    prefix.append(first.pop(0))
    if prefix[-1]['text']=='LISTE':prefix.append(first.pop(0));break
   inline=[]
   for l in ordered:
    idx=next((j for j,w in enumerate(l) if w['text']=='BITTE'),None) if i in {6,7} else None
    if idx is not None:inline+=l[idx:];del l[idx:]
   qw=[w for l in ordered for w in l]
   we=self.ev(fid+'-wording',Q,page,qw,fid+' deutscher Fragewortlaut; Layoutzeilen erhalten')
   if prefix:
    pe=self.ev(fid+'-list-instruction',Q,page,prefix,fid+' Original-Listenanweisung')
    contexts[i].append({'typ':'listenanweisung','text':field(self.value(pe),pe),'herkunft':'direkt'})
   if inline:
    ie=self.ev(fid+'-inline-interviewer',Q,page,inline,fid+' inline Vorleseanweisung')
    contexts[i].append({'typ':'interviewer','text':field(self.value(ie),ie),'herkunft':'direkt'})
   if i==8:
    iwe=[w for w in qw if (w['y0']>313 and w['x0']>=199) or w['y0']>326]
    ie=self.ev(fid+'-conditional-followup',Q,page,iwe,fid+' WENN JA im Originalwortlaut')
    contexts[i].append({'typ':'bedingte-nachfrage-im-wortlaut','text':field(self.value(ie),ie),'herkunft':'direkt'})
   cats=[];allcat=select(ws,(28,ctop,580,cbottom))
   ce=self.ev(fid+'-category-table',Q,page,allcat,fid+' gesamte Original-Antworttabelle einschließlich gedruckter Weiterleitungen',(28,ctop,580,cbottom))
   if layout=='horizontal':
    codes=[w for w in allcat if re.fullmatch(r'\d+',w['text'])]
    if i==31:
     eights=[w for w in codes if w['text']=='8' and w['x0']>520];codes=[w for w in codes if w not in eights]
     # The two vertically printed digits are one 88 code, visually read and explicitly evidenced.
     codes.append({'text':'88','x0':min(w['x0'] for w in eights),'x1':max(w['x1'] for w in eights),'y0':min(w['y0'] for w in eights),'y1':max(w['y1'] for w in eights),'source_digits':eights})
    codes.sort(key=lambda w:w['x0'])
   else:codes=sorted([w for w in allcat if cx-.9<=w['x0']<=cx+1.5 and re.fullmatch(r'\d+',w['text'])],key=lambda w:w['y0'])
   for pos,cw in enumerate(codes):
    c=cw['text'];codewords=cw.get('source_digits',[cw]);code_ev=self.ev(fid+'-code-'+c,Q,page,codewords,fid+' Codezelle '+c)
    if layout=='horizontal':labelwords=select(ws,HLABELS[i][c]) if c in HLABELS[i] else []
    else:
     lower=codes[pos-1]['y1']+.1 if pos else ctop
     upper=cw['y1']+.1
     if i==30 and c=='03':upper=197
     if i==30 and c=='04':lower=197
     labelwords=select(ws,(28,lower,cx-.1,upper))
    if labelwords:
     le=self.ev(fid+'-label-'+c,Q,page,labelwords,fid+' geometrisch zugeordnete Labelzelle zu Code '+c)
     label=field(self.value(le),le,'ORIGINALZELLE_ZUGEORDNET_AUTOR_REVIEW_OFFEN')
    else:label=field(None,ce,'KEIN_LABEL_IN_ORIGINALZELLE_ABGEDRUCKT')
    kind='antwort'
    if c in {'7','77','777','7777'} and label['wert'] and 'verweigert' in label['wert']:kind='antwort-verweigert'
    if c in {'8','88','888','8888'} and label['wert'] and 'Weiß' in label['wert']:kind='weiss-nicht'
    if (i==30 and c=='55') or (i==43 and c in {'33','44','55','65'}):kind='gedruckte-sonderantwort'
    if i==33:kind='administrative-gruppenzuweisung'
    cats.append({'code':field(c,code_ev,'ORIGINALCODE_GELESEN_AUTOR_REVIEW_OFFEN'),'label_de':label,'rolle':{'wert':kind,'status':'AUTORENANNOTATION_KEINE_MISSING_ODER_SCOREENTSCHEIDUNG','belege':[code_ev,ce]},'zellenbezug':{'layout':layout,'zuordnung':'Eigene geometrische Zellenzuordnung und Originallektüre; kein Tokenpresence-Nachweis allein','tabellenbeleg':ce}})
   route=[]
   for k,(applies,target,rect) in enumerate(ROUTES.get(i,[])):
    e=self.region(fid+f'-routing-{k}',Q,page,rect,fid+' gedruckte Weiterleitung')
    route.append({'originaltext':field(self.value(e),e),'bei_originalcodes':field(applies,[e,ce],'ZELLENSPANNE_VISUELL_GELESEN' if applies else 'ORIGINALWEITERLEITUNG_OHNE_EINZELCODES'),'ziel':field(target,e,'ORIGINALZIEL_GELESEN')})
   cb=[self.codebook(v) for v in r['ess_variablen'].split('|')]
   card={'nummer':None,'status':'KEINE_LISTENANWEISUNG_BEI_DIESEM_ORIGINALITEM','belege':[we],'originalinhalt':None}
   if listno:
    sp=listno+1
    # Some PDFs contain an additional nonrendered duplicate text layer. Select the lower complete scale, with a separate actual printed header.
    bounds=(70,320,540,420) if listno in {20,24,25,28} else (70,180,560,740)
    se=self.region(f'S-L{listno}-scale',S,sp,bounds,f'LISTE {listno}: vollständige sichtbare Skala, ohne interne Frage(n)- und Listenüberschrift')
    head=self.region(f'S-L{listno}-header',S,sp,(70,25,550,145),f'LISTE {listno}: gedruckte Frage(n)-Zuordnung und Listennummer')
    card={'nummer':field(listno,head),'status':'ORIGINAL_LISTENHEFT_GELESEN_AUTOR_REVIEW_OFFEN','pdf_seite':sp,'gedruckte_seite':None,'originalinhalt':field(self.value(se),se),'sonderantworten':{'status':'NICHT_AUF_LISTE_ABGEDRUCKT_NUR_FRAGEBOGEN','belege':[se,ce]},'extraktionsgrenze':'Bei LISTE 20/24/25/28 enthält PDF-Textlayer eine zweite Skala; lower complete scale nach sichtbarer Seitenlektüre ausgewählt, keine Inhaltsänderung.' if listno in {20,24,25,28} else None}
    scale_words=self.evidence[se]['tokenauswahl'];normalcats=[c for c in cats if c['rolle']['wert']=='antwort'];cardcats=[]
    if listno in {20,24,25,28}:
     scodes=sorted([w for w in scale_words if w['text'].isdigit()],key=lambda w:w['x0'])
     assert len(scodes)==len(normalcats)==11
     for pos,(cw,qcat) in enumerate(zip(scodes,normalcats)):
      code_e=self.ev(f'S-L{listno}-code-{cw["text"]}',S,sp,[cw],f'LISTE {listno}: gedruckter Zahlplatz {cw["text"]}')
      label_words=[w for w in scale_words if w['y0']<cw['y0'] and (w['x0']<220 if pos==0 else w['x0']>425)] if pos in {0,10} else []
      le=self.ev(f'S-L{listno}-label-{cw["text"]}',S,sp,label_words,f'LISTE {listno}: Endpunktlabel zum Zahlplatz {cw["text"]}') if label_words else None
      cardcats.append({'fragebogen_code_referenz':qcat['code'],'auf_liste_gedruckter_code':field(cw['text'],code_e),'label_de':field(self.value(le) if le else None,le or se,'ORIGINAL_LISTENZELLE_GELESEN' if le else 'KEIN_LABEL_IN_LISTENZELLE_ABGEDRUCKT'),'zuordnung':'Linker/rechter Endpunkt und Zahlplatz nach Seitengeometrie und eigener sichtbarer Lektüre'})
    elif listno in {30,32}:
     scodes=sorted([w for w in scale_words if w['x0']<237 and w['text'].isdigit()],key=lambda w:w['y0'])
     assert len(scodes)==len(normalcats)
     for cw,qcat in zip(scodes,normalcats):
      code_e=self.ev(f'S-L{listno}-code-{cw["text"]}',S,sp,[cw],f'LISTE {listno}: gedruckte Zahlzelle {cw["text"]}')
      lw=[w for w in scale_words if w['x0']>=240 and abs(w['y0']-cw['y0'])<2.1]
      le=self.ev(f'S-L{listno}-label-{cw["text"]}',S,sp,lw,f'LISTE {listno}: Label auf Zeile der Zahlzelle {cw["text"]}') if lw else None
      cardcats.append({'fragebogen_code_referenz':qcat['code'],'auf_liste_gedruckter_code':field(cw['text'],code_e),'label_de':field(self.value(le) if le else None,le or se,'ORIGINAL_LISTENZELLE_GELESEN' if le else 'KEIN_LABEL_IN_LISTENZELLE_ABGEDRUCKT'),'zuordnung':'Gleiche gedruckte Tabellenzeile, separate Zahl-/Label-BBox'})
    else:
     # Whole labels must match consecutively in visible top-to-bottom order; token presence alone does not map a card cell.
     ordered_scale=[w for line in lines(scale_words) for w in line];offset=0
     for qcat in normalcats:
      target_tokens=qcat['label_de']['wert'].split();selected=ordered_scale[offset:offset+len(target_tokens)]
      if [w['text'] for w in selected]!=target_tokens:raise ValueError('SHOWCARD CONSECUTIVE LABEL MISMATCH '+fid+' '+qcat['code']['wert'])
      offset+=len(target_tokens);c=qcat['code']['wert'];le=self.ev(f'S-L{listno}-label-{c}',S,sp,selected,f'LISTE {listno}: vollständige Antwortzeile in Originalreihenfolge, zu Fragebogencode {c}')
      cardcats.append({'fragebogen_code_referenz':qcat['code'],'auf_liste_gedruckter_code':field(None,le,'KEIN_VARIABLE_CODE_AUF_LISTE_ABGEDRUCKT'),'label_de':field(self.value(le),le,'ORIGINAL_LISTENZEILE_GELESEN'),'zuordnung':'Eigene sichtbare Reihenfolge und vollständige aufeinanderfolgende Labeltokens; Codes stammen allein aus Fragebogen'})
     if offset!=len(ordered_scale):raise ValueError('UNASSIGNED SHOWCARD TOKENS '+fid)
    card['antwortkategorien_listenheft']=cardcats
   questions.append({'inventar_id':fid,'frage_id':field(fid,ident),'modul':field('C',ident,'QUELLENABSCHNITT_C'),'status':'OEFFENTLICHE_QUELLENANNOTATION_ENTWURF_REVIEW_OFFEN',
    'variable_zuordnung':{'status':'DOKUMENTATION_4_1_LOCATION_KANDIDAT_DATENABGLEICH_4_2_OFFEN','quellen':cb},
    'wortlaut_de':field(self.value(we),we),'kontext':contexts[i],
    'antwortformat':field('Offene Eingabe' if layout=='entry' else ('CAPI-Randomisierungsresultat' if i==33 else ('Mehrfachnennungen laut Original' if i==19 else 'Gedruckte Antwortskala')),[ce],'AUTORENBESCHREIBUNG_DES_ORIGINALFORMATS'),
    'antwortkategorien_fragebogen':cats,'missingcodes_fragebogen':[c for c in cats if c['rolle']['wert'] in {'antwort-verweigert','weiss-nicht'}],
    'missingcodes_daten':{'wert':None,'status':'DATENAUSGABE_4_2_NICHT_GEPRUEFT','grund':'Keine Datendatei/Antworten gelesen. Gedruckte Interviewcodes sind kein automatischer Missing-/Anonymisierungsvertrag.'},
    'weiterleitungen':route,'weiterleitung_status':'ORIGINALWEITERLEITUNG_GELESEN' if route else 'KEIN_EIGENER_WEITERLEITUNGSTEXT_ABGEDRUCKT',
    'listenheft':card,'eignung_polung_dimension_score':{'status':'NICHT_ENTSCHIEDEN'},'offene_punkte':['OPEN-C-4.2-MISSING','OPEN-C-ITEMURTEILE','OPEN-C-INDEPENDENT-REVIEW']})
  # Explicit scope support for the broader inherited German introductions.
  scope_support={'intro-person-life':['CB41-happy-metadata-70'],'intro-personal':['CB41-health-metadata-72'],'intro-attachment':['CB41-atchctr-metadata-73'],'intro-climate':['CB41-ccnthum-metadata-165']}
  for q in questions:
   for context in q['kontext']:
    eid=context['text']['belege'][0]
    name=eid.removeprefix('QCTX-')
    if name in scope_support:context['geltungsbelege']=context['text']['belege']+scope_support[name]
  opens=[
   ('OPEN-C-4.2-MISSING',list(CONFIG),'Variablen-, Filter-, Missing- und Anonymisierungsabgleich zur tatsächlichen Datenausgabe 4.2 fehlt.'),
   ('OPEN-C-ITEMURTEILE',list(CONFIG),'Keine endgültige Eignung, Ausschluss, Polung, Dimension, Score, Neutralität oder wissenschaftliche Itemabnahme.'),
   ('OPEN-C-INDEPENDENT-REVIEW',list(CONFIG),'Zwei unabhängige neue Reviews und getrennte Modellfamilien-Urteile sind nicht durch Autorenlektüre ersetzt.'),
   ('OPEN-C12-C14-RECODE',[12,14],'Original 21/22 gegenüber Dokumentation 4.1 291/290; Anonymisierung und integrierte/country-spezifische Variablen vor Datenimport prüfen.'),
   ('OPEN-C12-C14-NO88',[12,14],'Original druckt nur 77 als Nichtantwort. Kein 88 ergänzen; spätere Datenmissing gesondert prüfen.'),
   ('OPEN-C19-MULTIRESPONSE',[19],'Fragebogen Mehrfachcodes 01–10,77,88 gegenüber einzelnen 0/1-Indikatoren inkl. dscrnap/dscrna; nicht zusammenlegen, strukturelles Nichtzutreffen von unbekannt/Verweigerung unterscheiden.'),
   ('OPEN-C22-C27-C29-COUNTRYCODES',[22,27,29],'Original zweistellige ISO-Anweisung, Dokumentation4.1 vierstellige/reservierte/anonymisierte Kodierung; keine sichere direkte Übernahme.'),
   ('OPEN-C23-C24-ANONYMISATION',[23,24],'Jahr- und Sprachkodierung sowie spätere Anonymisierung brauchen Ausgabenabgleich; keine Originalkategorien erfunden.'),
   ('OPEN-C31-C32-UNCONDITIONAL',[30,31,32],'C30=55 überspringt C31/C32 bis Einleitung C43; bedingte Antworten tragen keine ungeprüfte unbedingte Dimension. 55/77/88 sind keine strukturellen Nullen.'),
   ('OPEN-C33-C42-EXPERIMENT',[33,34,35,36,37,38,39,40,41,42],'CAPI-Gruppe und Skalenfassungen bleiben getrennt. Keine gepoolte Messung oder Polung beschlossen; gemeinsame Gruppenzuweisung mit Modul I dokumentiert.'),
   ('OPEN-C42-NO-ROUTING',[42],'Nach C42 ist kein expliziter Weiterleitungstext gedruckt; keine erfundene Phrase WEITER MIT EINLEITUNG VOR C43 ergänzen.'),
   ('OPEN-C43-SPECIALS',[43],'33/44/55/65 sind gedruckte Sonderantworten neben 77/88; kein binärer Score-/Missingentscheid getroffen.'),
   ('OPEN-C-LICENSE-EXPORT',list(CONFIG),'CC BY-SA 4.0 Dokumentationsrahmen und Attribution erfasst; konkrete Veröffentlichung/Lizenzentscheidung für spätere Auswahl/Artefakte bleibt offen.'),
   ('OPEN-C-ACTIVE-INVENTORY',list(CONFIG),'Neue Ergänzung wird nicht automatisch mit aktiver CSV/Parser zusammengeführt. Originalbestand 296/205 bleibt unverändert; noch keine Vollabnahme des gesamten Inventars.'),
   ('OPEN-C-CARD-REFERENCES',[1,2,3,4,9,10,15,16,17,30,31,32],'Nummern der deutschen LISTEN und der integrierten englischen CARD-Verweise unterscheiden sich. Deutsche Listen nach Original verwendet; keine Nummerngleichheit unterstellt.')]
  for oid,ids,reason in opens:
   for q in questions:
    if int(q['inventar_id'][1:]) in ids and oid not in q['offene_punkte']:q['offene_punkte'].append(oid)
  return {'schema_version':'1','paket':'INVENTORY-003-C','status':'ENTWURF_NICHT_UNABHAENGIG_GEPRUEFT','createdOn':'2026-10-03',
   'basis':{'csv':'data/inventar.entwurf.csv','csv_sha256':sha((ROOT/'data/inventar.entwurf.csv').read_bytes()),'provenienz_sha256':sha((ROOT/'data/inventar.provenienz.json').read_bytes()),'activeArtifactsChanged':False},
   'geltungsbereich':{'round':11,'questionnaireYear':2023,'metadataEdition':'4.1','targetDataCandidateEdition':'4.2','identitaeten':43,'module':{'C':43},'vollstaendigerEssBestand':False,'originalbestand296_205_unveraendert':True,'empirischePruefung':'NICHT_DURCHGEFUEHRT'},
   'zugriffsgrenzen':{'rawDataRead':False,'respondentRows':False,'portalAnalysis':False,'distributions':False,'peerOrJurorReportsRead':False,'loopFindingsRead':False,'otherModelFamily':False},
   'quellen':{s:{'file':'outputs/loop/inventory002-ab/baseline-check-cache/'+p[1],'url':self.source_meta[s]['url'],'sha256':p[2],'pages':len(self.sources[s]),**({'edition':'4.1'} if s=='ESS11-CODEBOOK' else {})} for s,p in PINS.items()},
   'quellenzugriff':{'authorRereadOn':'2026-10-03','authorStartedUtc':'2026-10-03T05:50:57Z','originalQuelle':'Öffentliche offizielle Quellen, bestehende Pins bytegeprüft. Lokale eigenständige Lektüre, keine Portal-Analysen.','networkRefresh':'NICHT_DURCHGEFUEHRT_DIESE_FASSUNG_NUTZT_GEPINNTE_BYTES','byteEquality41vs42':'NICHT_GEPRUEFT'},
   'lizenz':{'documentation':'CC BY-SA 4.0','url':'https://creativecommons.org/licenses/by-sa/4.0/','attribution':'European Social Survey (ESS), Round 11, Germany questionnaire and showcards (2023); Codebook integrated file edition 4.1. Original URLs and exact hashes in quellen.','aenderungen':'Eigene öffentliche Quellenannotation, Feld-/Zellenzuordnung, Layoutzeilen als Text. Fragebogenwortlaute nicht inhaltlich umgeschrieben.','datenLizenz':'Daten getrennt unter CC BY-NC-SA 4.0 laut docs/lizenzen.md; keine Datendatei genutzt.','veroeffentlichungspruefung':'OFFEN_FUER_KONKRETE_SPAETERE_EXPORTFASSUNG','beleg':'outputs/loop/inventory003-c/license-reading.json; docs/lizenzen.md; Hashes der Lizenzquelle und Regeldatei in input-hashes.json'},
   'belegregister':self.evidence,'fragen':questions,'offene_punkte':[{'id':oid,'fragen':[f'C{i}' for i in ids],'status':'OFFEN','grund':reason} for oid,ids,reason in opens],
   'author':{'runtimeReportedModel':'gpt-6.1-sol','reasoningEffort':'ultra inherited','internalRevisionAndProviderRules':'unknown','role':'source annotation author','startauftrag':'outputs/loop/inventory003-c/startauftrag.txt'}}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',required=True);parser.add_argument('--work',required=True);args=parser.parse_args()
 out=Path(args.out).resolve();work=Path(args.work).resolve()
 if out!=TARGET and not out.is_relative_to(OWN):raise SystemExit('Output outside authorized paths')
 if not work.is_relative_to(OWN):raise SystemExit('Work outside authorized own outputs')
 if not OWN.is_relative_to(ROOT):raise SystemExit('Root mismatch')
 if out.exists() or work.exists():raise SystemExit('Existing output or work directory will not be overwritten')
 work.mkdir(parents=True,exist_ok=False);b=Builder(work);doc=b.build()
 original_limits=dict(doc['zugriffsgrenzen'])
 doc['zugriffsgrenzen']['peerOrJurorReportsRead']=True
 doc['zugriffsgrenzen']['loopFindingsRead']=True
 doc['korrekturprovenienz']={'finding':'C-R01','round':1,'author':'/root','originalAuthorAccessLimits':original_limits,'peerReportsRead':True,'loopFindingsRead':True,'scope':'Nur Metadatenabgrenzung lnghom2; ursprüngliche Quellenautorenphase in author, ursprüngliche Fassung unverändert. Unabhängige Nachprüfung offen.','plan':'outputs/loop/inventory003-c-correction/plan-before-correction.json'}
 out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':'BUILT_DRAFT','identities':len(doc['fragen']),'evidence':len(doc['belegregister']),'output':str(out.relative_to(ROOT)),'sha256':sha(out.read_bytes())}))
if __name__=='__main__':main()
