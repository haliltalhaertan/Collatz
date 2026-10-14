#!/usr/bin/env python3
"""Save PDFs locally and extract text for source-checking; excerpts in final report attributed by arXiv ID."""
import requests,concurrent.futures,os
from pypdf import PdfReader
ids=['1609.07802','1212.1873','1602.00261','1510.04043','2409.18936','2307.07375','1907.07121','2303.07785','2103.12684','2501.17795','1912.10987']
os.makedirs('primary_sources',exist_ok=True)
def get(i):
 try:
  r=requests.get('https://arxiv.org/pdf/'+i,timeout=65);r.raise_for_status()
  if not r.content.startswith(b'%PDF'):return (i,'non pdf '+r.text[:120])
  fn='primary_sources/'+i+'.pdf';open(fn,'wb').write(r.content)
  text='\n'.join((p.extract_text() or '') for p in PdfReader(fn).pages)
  open('primary_sources/'+i+'.txt','w').write(text)
  return (i,len(text))
 except Exception as e:return (i,repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for result in pool.map(get,ids):print(result,flush=True)
