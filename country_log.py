# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 01:20:29 2019

@author: Aishy
"""

# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import sys,os,codecs
from os.path import join
"""
Created on Tue May 28 17:47:26 2019

@author: Huda 
"""
# extracting 500 keywords per country in-domain, using the improved log-odds method (Jurafsky et al. (2014))
# recieve text_chunks directory path
# creating 500 keyword file for each country

countries_Dict={}

def countryWords(my_country,dir_path):
   data_path=dir_path+'\\europe_data' #europe path
   country_path=join(data_path, my_country)
   countryWords={}
   for author in os.listdir(country_path):#author path
         author_path=join(country_path,author)
         if ((my_country != "reddit.Armenia.txt.tok.clean") and (my_country!="reddit.Canada.txt.tok.clean") and (my_country!="reddit.China.txt.tok.clean") and (my_country!="reddit.Cyprus.txt.tok.clean")
         and (my_country!="reddit.Georgia.txt.tok.clean") and (my_country!="reddit.India.txt.tok.clean") and (my_country!="reddit.Israel.txt.tok.clean") and (my_country!="reddit.Macedonia.txt.tok.clean")
         and (my_country!="reddit.Malta.txt.tok.clean") and (my_country!="reddit.Moldova.txt.tok.clean") and (my_country!="reddit.Montenegro.txt.tok.clean") and (my_country!="reddit.Vietnam.txt.tok.clean")) :
             for chunk in os.listdir(author_path):
                 print(author_path+chunk)
                 chunk_file=open(join(author_path,chunk), "r",encoding='utf8')
                 for line in chunk_file:
                     sentence=set(line.split())
                     for element in sentence:
                         if element not in countryWords.keys():
                             countryWords[element]=1
                         else:
                             countryWords[element]+=1
   
  
    
    
   otherWords={}
   for reddit_country in os.listdir(data_path):
       country_path=join(data_path, reddit_country)
       for author in os.listdir(country_path):#author path
           author_path=join(country_path,author)
           if ((reddit_country != "reddit.Armenia.txt.tok.clean") and (reddit_country!="reddit.Canada.txt.tok.clean") and (reddit_country!="reddit.China.txt.tok.clean") and (reddit_country!="reddit.Cyprus.txt.tok.clean")
           and (reddit_country!="reddit.Georgia.txt.tok.clean") and (reddit_country!="reddit.India.txt.tok.clean") and (reddit_country!="reddit.Israel.txt.tok.clean") and (reddit_country!="reddit.Macedonia.txt.tok.clean")
           and (reddit_country!="reddit.Malta.txt.tok.clean") and (reddit_country!="reddit.Moldova.txt.tok.clean") and (reddit_country!="reddit.Montenegro.txt.tok.clean") and (reddit_country!="reddit.Vietnam.txt.tok.clean")) :
               if(reddit_country!=my_country):
                   for chunk in os.listdir(author_path):
                       print(author_path+chunk)
                       chunk_file=open(join(author_path,chunk), "r",encoding='utf8')
                       for line in chunk_file:
                           sentence=set(line.split())
                           for element in sentence:
                               if element not in otherWords.keys():
                                   otherWords[element]=1
                               else:
                                   otherWords[element]+=1
                                   
                               if element not in countryWords:
                                       countryWords[element]=0
   for element in countryWords:
      if element not in otherWords:
         otherWords[element]=0
          
   return  countryWords,otherWords              


def backGround(W1,W2):
    background={}
    for key in W1:
        background[key]=W1[key]+W2[key]
    return background  

def logOdds(counts1,counts2,prior):
 sigmasquared = defaultdict(float)
 sigma = defaultdict(float)
 delta = defaultdict(float)

 for word in prior.keys():
    prior[word] = int(prior[word] + 0.5)

 for word in counts2.keys():
    counts1[word] = int(counts1[word] + 0.5)
    if prior[word] == 0:
        prior[word] = 1

 for word in counts1.keys():
    counts2[word] = int(counts2[word] + 0.5)
    if prior[word] == 0:
        prior[word] = 1

 n1  = sum(counts1.values())
 n2  = sum(counts2.values())
 nprior = sum(prior.values())


 for word in prior.keys():
    if prior[word] > 0:
        l1 = float(counts1[word] + prior[word]) / (( n1 + nprior ) - (counts1[word] + prior[word]))
        l2 = float(counts2[word] + prior[word]) / (( n2 + nprior ) - (counts2[word] + prior[word]))
        sigmasquared[word] =  1/(float(counts1[word]) + float(prior[word])) + 1/(float(counts2[word]) + float(prior[word]))
        sigma[word] =  math.sqrt(sigmasquared[word])
        delta[word] = ( math.log(l1) - math.log(l2) ) / sigma[word]
        

 return delta

    
    

def main(argv):
 dir_path=str(sys.argv[1]) # text_chunks directory
 data_path=dir_path+'\\europe_data' #europe path
 for reddit_country in os.listdir(data_path):
     if ((reddit_country != "reddit.Armenia.txt.tok.clean") and (reddit_country!="reddit.Canada.txt.tok.clean") and (reddit_country!="reddit.China.txt.tok.clean") and (reddit_country!="reddit.Cyprus.txt.tok.clean")
     and (reddit_country!="reddit.Georgia.txt.tok.clean") and (reddit_country!="reddit.India.txt.tok.clean") and (reddit_country!="reddit.Israel.txt.tok.clean") and (reddit_country!="reddit.Macedonia.txt.tok.clean")
     and (reddit_country!="reddit.Malta.txt.tok.clean") and (reddit_country!="reddit.Moldova.txt.tok.clean") and (reddit_country!="reddit.Montenegro.txt.tok.clean") and (reddit_country!="reddit.Vietnam.txt.tok.clean")) :
         Words1,Words2=countryWords(reddit_country,dir_path) 
         prior=backGround(Words1,Words2)
         delta=logOdds(Words1,Words2,prior)
         file = codecs.open(reddit_country,'w+', encoding='utf8')
         num=500
         for word in sorted(delta, key=delta.get,reverse=True):
             file.write(word + " %.3f" % delta[word])
             file.write("\n")
             num-=1
             if num==0:
                 break;
   
     
pass
if __name__ == "__main__":
    result =   main(sys.argv)
    if result is not False:
      print("The process was completed successfully...\n")    