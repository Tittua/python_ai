#!/usr/bin/env python
# coding: utf-8

# In[11]:


#import the libraries
import json
import requests
import pandas as pd
import spacy



#!python -m spacy download en_core_web_lg
nlp = spacy.load('en_core_web_lg')

#pulling the data from the end point
response=requests.get('https://devapi.beyondchats.com/api/get_message_with_sources')
#Loading it into json format
data=json.loads(response.content)
#defining empty list for assining the values for data cleaning and analysing
main_id=[]
sub_id=[]
context=[]
reponses=[]
source=[]
link=[]
main_id_loc=[]
sub_id_loc=[]
link_loc=[]

#Extracting the content of the json data and feting the id,respons,source and appending it into different list
for items in data['data']['data']:
    main_id.append(items['id'])
    reponses.append(items['response'])
    source.append(items['source'])
    
#Making a data frame from the above list
df=pd.DataFrame(zip(main_id,reponses,source),columns=['id','response','source'])


#for every elemnets in the dataframe
for items in range(len(df)):
    main_doc=nlp(df['response'][items])
    for x in df['source'][items]:
        
        search_doc=nlp((x['context']))
        #checking the similarity between the response and their corresponding sources and if the similarity 
        if (main_doc.similarity(search_doc)>.45):
            main_id_loc.append(items)
            sub_id_loc.append(x['id'])
            link_loc.append(x['link'])



#converting the values into json format 
combined_list = [{"id": sub_id_loc, "link": link_loc} for sub_id_loc, link_loc in zip(sub_id_loc, link_loc)]
json_output = json.dumps(combined_list, indent=2)
return json_output

