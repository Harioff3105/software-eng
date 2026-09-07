from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
import math
app=FastAPI(title='Scholarship Recommendation ML Service',version='1.0.0')
class Request(BaseModel):
    profile: dict[str,Any]={}
    scholarships: list[dict[str,Any]]=[]
def score(profile,s):
    score=0.0
    tags=set(str(x).lower() for x in profile.get('interests',[]))
    stags=set(str(x).lower() for x in s.get('tags',[]))
    score += 0.55*(len(tags&stags)/max(1,len(tags)))
    if profile.get('gpa') is not None and s.get('eligibility',{}).get('minGpa') is not None:
        score += 0.25 if float(profile['gpa'])>=float(s['eligibility']['minGpa']) else 0
    if profile.get('income') is not None and s.get('eligibility',{}).get('maxIncome') is not None:
        score += 0.20 if float(profile['income'])<=float(s['eligibility']['maxIncome']) else 0
    return round(min(1.0,score),4)
@app.get('/health')
def health(): return {'ok':True,'service':'ml-recommendation'}
@app.post('/recommend')
def recommend(req:Request):
    ranked=[{**s,'score':score(req.profile,s)} for s in req.scholarships]
    ranked.sort(key=lambda x:x['score'],reverse=True)
    return {'recommendations':ranked[:10]}
