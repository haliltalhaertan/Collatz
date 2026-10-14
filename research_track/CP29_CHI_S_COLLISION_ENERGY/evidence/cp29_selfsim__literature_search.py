#!/usr/bin/env python3
"""Reproducible bibliographic search, preserving failures and query URLs."""
import requests,json,time,xml.etree.ElementTree as ET
from urllib.parse import urlencode
Q=[('Shmerkin 2019 Annals Lq dimension Furstenberg','Shmerkin Furstenberg Lq self-similar'),('Hochman 2014 Annals self similar entropy overlap','Hochman 2014 overlaps entropy self-similar'),('Varju Bernoulli convolutions absolute continuity','Varju Bernoulli convolutions absolute continuity'),('Breuillard Varju Bernoulli convolutions entropy','Breuillard Varju Bernoulli convolutions entropy'),('Kittle Kogler absolute continuity self-similar measures','Kittle Kogler absolute continuity self similar measures'),('p-adic self-similar measures Lq dimension','p-adic self-similar measures dimension'),('Garsia entropy critical Bernoulli convolutions','Garsia entropy critical Bernoulli convolutions'),('infinite iterated function systems Lq dimension self-similar','infinite iterated function system Lq measures'),('non-Archimedean self-similar measures overlaps','ultrametric self similar measures overlaps')]
s=requests.Session();s.headers['User-Agent']='CP29 research contact: cp29research@example.org'
out=[]
for site,terms in [('openalex',[q[1] for q in Q]),('arxiv',['all:'+q[1].replace(' ',' AND all:') for q in Q]),('semantic',['p-adic self-similar measures','Kittle Kogler absolute continuity'])]:
 for term in terms:
  if site=='openalex':u='https://api.openalex.org/works?'+urlencode({'search':term,'per-page':4,'select':'id,title,publication_year,doi,primary_location,open_access'})
  elif site=='arxiv':u='https://export.arxiv.org/api/query?'+urlencode({'search_query':term,'start':0,'max_results':4})
  else:u='https://api.semanticscholar.org/graph/v1/paper/search?'+urlencode({'query':term,'limit':4,'fields':'title,authors,year,url,externalIds'})
  try:
   r=s.get(u,timeout=22);d={'service':site,'query':term,'url':u,'status':r.status_code}
   if r.ok:
    if site=='openalex':d['results']=[{k:v for k,v in x.items() if k in ('id','title','publication_year','doi','primary_location','open_access')} for x in r.json().get('results',[])]
    elif site=='semantic':d['results']=r.json().get('data',[])
    else:
     root=ET.fromstring(r.text);ns={'a':'http://www.w3.org/2005/Atom'}
     d['results']=[{'title':(x.findtext('a:title','',ns)).strip().replace('\n',' '),'id':x.findtext('a:id','',ns),'summary':x.findtext('a:summary','',ns)[:250]} for x in root.findall('a:entry',ns)]
   else:d['error']=r.text[:250]
  except Exception as e:d={'service':site,'query':term,'url':u,'error':repr(e)}
  out.append(d);print(site,term,d.get('status'),[(x.get('title','')[:65]) for x in d.get('results',[])],flush=True)
  with open('literature_search_results.json','w') as f:json.dump(out,f,indent=2,ensure_ascii=False)
  time.sleep(0.25)
