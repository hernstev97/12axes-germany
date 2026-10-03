"""Versionierter E2-Quellenvertrag, keine CAPI- oder wissenschaftliche Freigabe.

Die Originalzellgeometrie, Pflichtkontexte und 18 sichtbaren Lesefassungen
wurden aus dem abgeschlossenen unabhängigen INVENTORY-004-E-Reproduktionsaudit
übernommen und werden hier als AUTOREN-Code weiterverwendet. Das ist keine
neue unabhängige Prüfung. E-S01/E-R03: sichtbare Liste58 ohne Punkt; der
unveränderte Roh-Tokenextrakt behält den Punkt. Zwei frische Nachprüfungen
müssen diesen zusätzlichen Vertrag unabhängig an Originalen kontrollieren.
Die Eingabe pages muss separat aus den gepinnten drei Original-PDFs erzeugt
und ihre Byteherkunft geprüft sein. Diese reine Funktion prüft keine Dateien.
"""
import re

SOURCE_PINS = {
 'ESS11-DE-QUESTIONNAIRE': 'be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75',
 'ESS11-DE-SHOWCARDS': '786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca',
 'ESS11-CODEBOOK': 'b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35',
}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def extraction(ws, box):
    a,b,c,d = box
    selected = [w for w in ws if w['x0'] >= a-.05 and w['x1'] <= c+.05 and w['y0'] >= b-.05 and w['y0'] < d]
    lines = []
    for w in sorted(selected, key=lambda w:(w['y0'], w['x0'])):
        if not lines or abs(lines[-1][0]['y0'] - w['y0']) > .3:
            lines.append([w])
        else:
            lines[-1].append(w)
    text = '\n'.join(' '.join(w['text'] for w in sorted(line, key=lambda w:w['x0'])) for line in lines)
    return selected, text

IDS = ['E1','E2','E3','E4','E5','E6','E7','E8M','E8W','E9M','E10M','E11M','E9W','E10W','E11W'] + ['E'+str(n) for n in range(12,29)]

LISTS = {**{f'E{n}':51 for n in range(2,6)}, 'E1':50, 'E6':52,'E7':53, **{f'E{n}{s}':n+46 for n in range(8,12) for s in ['M','W']}, 'E12':58,'E13':58,'E14':59, **{f'E{n}':n+45 for n in range(15,19)}, **{f'E{n}':64 for n in range(19,23)}, **{f'E{n}':65 for n in range(23,26)},'E26':66,'E27':67,'E28':67}

VISIBLE = {
    50: ['Mann','Frau','Andere Bezeichnung','Möchte nicht antworten'],
    51: ['0 Überhaupt nicht','1','2','3','4','5','6 Voll und ganz'],
    52: ['0 Überhaupt nicht männlich','1','2','3','4','5','6 Sehr männlich'],
    53: ['0 Überhaupt nicht weiblich','1','2','3','4','5','6 Sehr weiblich'],
    54: ['0 Überhaupt nicht wichtig','1','2','3','4','5','6 Äußerst wichtig'],
    55: ['Ja - einmal','Ja - mehr als einmal','Nein','War noch nie bei einem Arzt oder einer Ärztin oder habe versucht, eine medizinische Behandlung zu bekommen'],
    56: ['Ja - einmal','Ja - mehr als einmal','Nein','Ich hatte noch nie einen Job oder habe mich nie um einen Job beworben'],
    57: ['Ja - einmal','Ja - mehr als einmal','Nein','Ich hatte noch nie Kontakt mit der Polizei'],
    58: ['Frauen werden weniger gerecht behandelt als Männer','Männer werden weniger gerecht behandelt als Frauen','Frauen und Männer werden gleichermaßen gerecht behandelt'],
    59: ['Die Polizei behandelt Frauen weniger gerecht als Männer','Die Polizei behandelt Männer weniger gerecht als Frauen','Frauen und Männer werden gleichermaßen gerecht behandelt'],
    60: ['0 Sehr schlecht für das Familienleben in Deutschland','1','2','3','4','5','6 Sehr gut für das Familienleben in Deutschland'],
    61: ['0 Sehr schlecht für die Politik in Deutschland','1','2','3','4','5','6 Sehr gut für die Politik in Deutschland'],
    62: ['0 Sehr schlecht für Unternehmen in Deutschland','1','2','3','4','5','6 Sehr gut für Unternehmen in Deutschland'],
    63: ['0 Sehr schlecht für die Stärke der Wirtschaft in Deutschland','1','2','3','4','5','6 Sehr gut für die Stärke der Wirtschaft in Deutschland'],
    64: ['Sehr dafür','Eher dafür','Weder dafür noch dagegen','Eher dagegen','Sehr dagegen'],
    65: ['Nie','Selten','Manchmal','Oft','Immer'],
    66: ['Nie','Selten','Manchmal','Oft','Immer'],
    67: ['Stimme stark zu','Stimme zu','Weder noch','Lehne ab','Lehne stark ab']
}

def original_positions(pages):
    positions = {}
    for page in range(43, 55):
        for word in pages['ESS11-DE-QUESTIONNAIRE'][page-1]:
            identity = word['text'].rstrip('.')
            if identity in IDS and word['x0'] < 70:
                require(identity not in positions, 'Mehrdeutige Originalfragekennung ' + identity)
                positions[identity] = (page, word['y0'])
    require(set(positions) == set(IDS), 'Originalkennungen unvollständig')
    return positions

def expected_context(qid):
    n=int(re.search(r'\d+',qid)[0]);needed={'QCTX-E-intro'}
    if 2<=n<=5:needed|={'QCTX-E2-E5',qid+'-if-necessary'}
    if n in [6,7]:needed|={'QCTX-E6-E7-intro','QCTX-E6-E7-random'}
    if n==8:needed|={'QCTX-E8-gate','QCTX-E8-intro','QCTX-'+qid+'-filter'}
    if 9<=n<=11:needed|={'QCTX-E9'+qid[-1]+'-E11'+qid[-1]+'-filter','QCTX-E9'+qid[-1]+'-E11'+qid[-1]+'-intro'}
    if n>=12:needed.add('QCTX-E12-all')
    if n in [12,13]:needed.add('QCTX-E12-E13-current')
    if n==20:needed.add('QCTX-E20-vignette')
    if n>=23:needed.add('QCTX-E23-E28-intro')
    if n==26:needed.add('SC-L66-definition')
    return needed

def validate_semantics(obj, pages):
    POSITION = original_positions(pages)
    ev=obj['belegregister'];result=[]
    for sid, pin in SOURCE_PINS.items():
        require(obj['quellen'][sid]['sha256'] == pin, 'Quellenpin: ' + sid)
    require([q['frage_id'] for q in obj['fragen']]==IDS,'Identitäten oder Reihenfolge')
    for q in obj['fragen']:
        qid=q['frage_id'];page,start=POSITION[qid]
        end=min([y for i,(p,y) in POSITION.items() if p==page and y>start]+[810])
        original=pages['ESS11-DE-QUESTIONNAIRE'][page-1]
        codewords=sorted([w for w in original if 385<=w['x0']<395 and start<=w['y0']<end and re.fullmatch('[0-8]',w['text'])],key=lambda w:w['y0'])
        cats=q['antwortkategorien_fragebogen']
        require([c['code']['wert'] for c in cats]==[w['text'] for w in codewords],qid+': Originalcodeset')
        for i,(cat,word) in enumerate(zip(cats,codewords)):
            ce=ev[cat['code']['belege'][0]]; le=ev[cat['label_de']['belege'][0]]
            require(ce['pdf_seite']==page and le['pdf_seite']==page,qid+': Quellseite Code/Label')
            require(ce['quelle_id']==le['quelle_id']=='ESS11-DE-QUESTIONNAIRE',qid+': Quellenart Code/Label')
            require(ce['tokenauswahl']==[word],qid+': Quellenzelle Code')
            high=codewords[i+1]['y0']-.1 if i+1<len(codewords) else word['y0']+15
            labeltokens,label=extraction(original,[0,word['y0']-.01,381,high])
            require(le['tokenauswahl']==labeltokens,qid+': Labelbeleg gehört nicht zur Original-Codezeile '+word['text'])
            require(cat['label_de']['wert']==(label or None),qid+': Labelwert')
        refs={e for c in q['kontext'] if c['typ']!='listenanweisung' for e in c['text']['belege']}
        require(expected_context(qid)<=refs,qid+': notwendiger Kontext fehlt '+str(sorted(expected_context(qid)-refs)))
        for c in q['kontext']:
            if c['typ']!='listenanweisung':
                require(c['text']['wert']==ev[c['text']['belege'][0]]['originalextrakt'],qid+': Kontextwortlaut')
        card=q['listenheft'];require(card['nummer']==LISTS[qid] and card['pdf_seite']==LISTS[qid]+1,qid+': Listenposition')
        visible=card['sichtbare_kategorien_de']['wert'];expected=VISIBLE[LISTS[qid]]
        require(visible==expected,qid+': sichtbare Listenlabels')
        if qid[-1] in 'MW':
            n=int(re.search(r'\d+',qid)[0]);want='1' if qid[-1]=='M' else '2';v=q['formulierung_variante'];cb=q['ess_zuordnung']['variablen'][0]
            require(v['zuweisung']=='E1 = '+want,qid+': Originalvariantenfilter')
            cf=cb['filter'][0];require(cf['wert']==ev[cf['belege'][0]]['originalextrakt'],qid+': Codebookfilter-Belegkette')
            require(re.search(r'Ask E'+str(n)+qid[-1].lower()+r' if E1='+want,cf['wert'],re.I),qid+': Codebookvariantenfilter')
        result.append({'questionId':qid,'originalPage':page,'list':LISTS[qid],'originalCodeRows':len(codewords),'requiredContextEvidence':sorted(expected_context(qid)),'status':'BESTANDEN_AUTOR_QUELLENVERTRAG_KEINE_FREIGABE'})
    return result

