# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:49:01 2019

@author: Huda
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:30:27 2019

@author: Aishy
"""

import datetime
from time import process_time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import sys,os,random
from sklearn import metrics
from random import choice
from os.path import join

K_FOLDS=10

#******************************************************************************************************
#this function recieve text_cunks directory path 
#return accuracy in_domain and out_domain in the three tasks 
#******************************************************************************************************
def bagOfwords(dir_path): 

 datetime.datetime.now()
 print(datetime.datetime.now())           
 data_path1=dir_path+'\\europe_data'
 data_path2=dir_path+'\\non_europe_data' 
 labels_europe_task1=[]
 labels_europe_task2=[]
 labels_europe_task3=[]
 europe=[] #the data of the training set 
 non_shufled_europe=[]
 for reddit_country in os.listdir(data_path1):
     if ((reddit_country != "reddit.Armenia.txt.tok.clean") and (reddit_country!="reddit.Canada.txt.tok.clean") and (reddit_country!="reddit.China.txt.tok.clean") and (reddit_country!="reddit.Cyprus.txt.tok.clean")
     and (reddit_country!="reddit.Georgia.txt.tok.clean") and (reddit_country!="reddit.India.txt.tok.clean") and (reddit_country!="reddit.Israel.txt.tok.clean") and (reddit_country!="reddit.Macedonia.txt.tok.clean")
     and (reddit_country!="reddit.Malta.txt.tok.clean") and (reddit_country!="reddit.Moldova.txt.tok.clean") and (reddit_country!="reddit.Montenegro.txt.tok.clean") and (reddit_country!="reddit.Vietnam.txt.tok.clean")
     and(reddit_country!="reddit.Mexico.txt.tok.clean")and(reddit_country!="reddit.NewZealand.txt.tok.clean")) :
         big_chunk=[]
         country_path=join(data_path1, reddit_country)
         index1 = reddit_country.index('reddit')
         index2 =reddit_country.index('.txt.tok.clean') 
         country_name=reddit_country[index1+7:index2]
         number_chunks=0  
         print(country_name)
         while(number_chunks<20000):  
           chunk=""
           author=np.random.choice(os.listdir(country_path))
           filename = np.random.choice(os.listdir(join(country_path,author)))
           f=open((country_path+'//'+author+'//'+filename),'r',encoding="utf-8") 
           lines = [a.strip() for a in f.readlines()]
           result = [choice(lines) for a in range(50)] #the result contain a 50 random lines from the chunk
           
           #add the result to array to shuffle the sentences later:
           big_chunk+=result
           
           #add the chunk without shuffling to the dataset:
           chunk=' '.join(result)
           non_shufled_europe.append(chunk)
           
           #creating labels_Vector to each task:
           lang=Countrylang[country_name]
           labels_europe_task1.append(lang)
           labels_europe_task2.append(langfamily[lang])
           
           if (lang=="English"):
             labels_europe_task3.append("native")
           else:
             labels_europe_task3.append("nonnative")

           number_chunks+=1
         
         #shuffling the sentences:   
         random.shuffle(big_chunk) 
         
         #recollect the sentences to chunks: 
         mini_chunk=0
         i=0
         while mini_chunk!=20000: 
             my_chunk=""
             lines_num=0
             while lines_num!=50:
                 lines_num+=1
                 my_chunk=my_chunk+" "+big_chunk[i]
                 i+=1
             
             europe.append(my_chunk)
             mini_chunk+=1
         
        
        
 labels_non_europe_task1=[] 
 labels_non_europe_task2=[]
 labels_non_europe_task3=[]     
 non_europe=[] #the data of the test set 
 non_shufled_non_europe=[]
 for reddit_country in os.listdir(data_path2):
     if ((reddit_country != "reddit.Armenia.txt.tok.clean") and (reddit_country!="reddit.Canada.txt.tok.clean") and (reddit_country!="reddit.China.txt.tok.clean") and (reddit_country!="reddit.Cyprus.txt.tok.clean")
     and (reddit_country!="reddit.Georgia.txt.tok.clean") and (reddit_country!="reddit.India.txt.tok.clean") and (reddit_country!="reddit.Israel.txt.tok.clean") and (reddit_country!="reddit.Macedonia.txt.tok.clean")
     and (reddit_country!="reddit.Malta.txt.tok.clean") and (reddit_country!="reddit.Moldova.txt.tok.clean") and (reddit_country!="reddit.Montenegro.txt.tok.clean") and (reddit_country!="reddit.Vietnam.txt.tok.clean")
     and(reddit_country!="reddit.Mexico.txt.tok.clean")and(reddit_country!="reddit.NewZealand.txt.tok.clean")) :
         big_chunk=[]
         country_path=join(data_path2, reddit_country)
         index1 = reddit_country.index('reddit')
         index2 =reddit_country.index('.txt.tok.clean') 
         country_name=reddit_country[index1+7:index2]
         number_chunks=0  
         print(country_name)
         while(number_chunks<20000):  
           chunk=""
           author=np.random.choice(os.listdir(country_path))
           filename = np.random.choice(os.listdir(join(country_path,author)))
           f=open((country_path+'//'+author+'//'+filename),'r',encoding="utf-8")  
           lines = [a.strip() for a in f.readlines()]
           result = [choice(lines) for a in range(50)] #the result contain a 50 random lines from the chunk
           
           #add the result to array to shuffle the sentences later:
           big_chunk+=result
           
           #add the chunk without shuffling to the dataset:
           chunk=' '.join(result)
           non_shufled_non_europe.append(chunk)
           
           #creating labels_Vector to each task:
           lang=Countrylang[country_name]
           labels_non_europe_task1.append(lang)
           labels_non_europe_task2.append(langfamily[lang])

           lang=Countrylang[country_name]
           if (lang=="English"):
               labels_non_europe_task3.append("native")
           else:
               labels_non_europe_task3.append("nonnative")

           number_chunks+=1
           
         #shuffling the sentences:  
         random.shuffle(big_chunk) 
         
         #recollect the sentences to chunks:
         mini_chunk=0
         i=0
         while mini_chunk!=20000 : 
             my_chunk=""
             lines_num=0
             while lines_num!=50:
                 lines_num+=1
                 my_chunk=my_chunk+" "+big_chunk[i]
                 i+=1

             non_europe.append(my_chunk)
             mini_chunk+=1  
    
 big_chunk=[]

 #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ TASK 1- native language -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
 print("TASK 1- native language")
 print("classfying with shuffling:")
 count_vect = CountVectorizer(stop_words='english')
 X_train_counts = count_vect.fit_transform(europe)
 clf = MultinomialNB()
 scores = cross_val_score(clf,X_train_counts,labels_europe_task1, cv = K_FOLDS, error_score='raise')
 accuracy = scores.mean() 
   
 print("the accuracy in-domain is:",str(round(accuracy * 100,2)) + "%")    

 test_counts = count_vect.transform(non_europe)
 fitted_model = clf.fit(X_train_counts,labels_europe_task1)
 acc=fitted_model.predict(test_counts)   
  
 print("the accuracy out-domain is:",str(round(metrics.accuracy_score(labels_non_europe_task1,acc)*100,2))+"%")
 print("\n")
 #**************************************************************************************************************
 print("classfying without shuffling:")
 count_vect = CountVectorizer(stop_words='english')
 X_train_counts = count_vect.fit_transform(non_shufled_europe)
 clf = MultinomialNB()
 scores = cross_val_score(clf,X_train_counts,labels_europe_task1, cv = K_FOLDS, error_score='raise')
 accuracy = scores.mean() 
   
 print("the accuracy in-domain is:",str(round(accuracy * 100,2)) + "%")    

 test_counts = count_vect.transform(non_shufled_non_europe)

 fitted_model = clf.fit(X_train_counts,labels_europe_task1)
 acc=fitted_model.predict(test_counts)   
  
 print("the accuracy out-domain is:",str(round(metrics.accuracy_score(labels_non_europe_task1,acc)*100,2))+"%")
 print("\n")
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ TASK 2-language family -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
 print("TASK 2-language family")
 print("classfying with shuffling:")
 count_vect = CountVectorizer(stop_words='english')
 X_train_counts = count_vect.fit_transform(europe)
 clf = MultinomialNB()
 scores = cross_val_score(clf,X_train_counts,labels_europe_task2, cv = K_FOLDS, error_score='raise')
 accuracy = scores.mean() 
   
 print("the accuracy in-domain is:",str(round(accuracy * 100,2)) + "%")    

 test_counts = count_vect.transform(non_europe)
 fitted_model = clf.fit(X_train_counts,labels_europe_task2)
 acc=fitted_model.predict(test_counts)   
  
 print("the accuracy out-domain is:",str(round(metrics.accuracy_score(labels_non_europe_task2,acc)*100,2))+"%")
 print("\n")
 #**************************************************************************************************************
 print("classfying without shuffling:")
 count_vect = CountVectorizer(stop_words='english')
 X_train_counts = count_vect.fit_transform(non_shufled_europe)
 clf = MultinomialNB()
 scores = cross_val_score(clf,X_train_counts,labels_europe_task2, cv = K_FOLDS, error_score='raise')
 accuracy = scores.mean() 
   
 print("the accuracy in-domain is:",str(round(accuracy * 100,2)) + "%")    

 test_counts = count_vect.transform(non_shufled_non_europe)

 fitted_model = clf.fit(X_train_counts,labels_europe_task2)
 acc=fitted_model.predict(test_counts)   
  
 print("the accuracy out-domain is:",str(round(metrics.accuracy_score(labels_non_europe_task2,acc)*100,2))+"%")
 print("\n")
 
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ TASK 3- native/non-native -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
 print("TASK 3- native/non-native")
 print("classfying with shuffling:")
 count_vect = CountVectorizer(stop_words='english')
 X_train_counts = count_vect.fit_transform(europe)
 clf = MultinomialNB()
 scores = cross_val_score(clf,X_train_counts,labels_europe_task3, cv = K_FOLDS, error_score='raise')
 accuracy = scores.mean() 
   
 print("the accuracy in-domain is:",str(round(accuracy * 100,2)) + "%")    

 test_counts = count_vect.transform(non_europe)
 fitted_model = clf.fit(X_train_counts,labels_europe_task3)
 acc=fitted_model.predict(test_counts)   
  
 print("the accuracy out-domain is:",str(round(metrics.accuracy_score(labels_non_europe_task3,acc)*100,2))+"%")
 print("\n")
 #**************************************************************************************************************
 print("classfying without shuffling:")
 count_vect = CountVectorizer(stop_words='english')
 X_train_counts = count_vect.fit_transform(non_shufled_europe)
 clf = MultinomialNB()
 scores = cross_val_score(clf,X_train_counts,labels_europe_task3, cv = K_FOLDS, error_score='raise')
 accuracy = scores.mean() 
   
 print("the accuracy in-domain is:",str(round(accuracy * 100,2)) + "%")    

 test_counts = count_vect.transform(non_shufled_non_europe)

 fitted_model = clf.fit(X_train_counts,labels_europe_task3)
 acc=fitted_model.predict(test_counts)   
  
 print("the accuracy out-domain is:",str(round(metrics.accuracy_score(labels_non_europe_task3,acc)*100,2))+"%")
 print("\n")
 
 
 
 
 
 
 datetime.datetime.now()
 print(datetime.datetime.now())
Countrylang ={"UK":"English","US":"English","NewZealand":"English","Australia":"English","Ireland":"English","Austria":"German","Germany":"German","Albania":"Albania","Bosnia":"Bosnia","Bulgaria":"Bulgaria","Croatia":"Croatia" 
,"Czech":"Czech","Denmark":"Denmark","Estonia":"Estonia","Finland":"Finland","France":"France","Greece":"Greece","Hungary":"Hungary","Iceland":"Iceland","Italy":"Italy","Latvia":"Latvia","Lithuania":"Lithuania","Netherlands":"Netherlands" 
,"Norway":"Norway","Poland":"Poland","Portugal":"Portugal","Romania":"Romania","Russia":"Russia","Serbia":"Serbia","Slovakia":"Slovakia","Slovenia":"Slovenia","Spain":"Spanish","Mexico":"Spanish","Sweden":"Sweden","Turkey":"Turkey","Ukraine":"Ukraine"
}

langfamily={"English":"Native","German":"Germanic","Albania":"Else","Bosnia":"Balto-Slavic","Bulgaria":"Balto-Slavic","Croatia":"Balto-Slavic"
            ,"Czech":"Balto-Slavic","Denmark":"Germanic","Estonia":"Else","Finland":"Else","France":"Latin","Greece":"Else","Hungary":"Else"
            ,"Iceland":"Germanic","Italy":"Latin","Latvia":"Balto-Slavic","Lithuania":"Balto-Slavic","Netherlands":"Germanic","Norway":"Germanic"
            ,"Poland":"Balto-Slavic","Portugal":"Latin","Romania":"Latin","Russia":"Balto-Slavic","Serbia":"Balto-Slavic","Slovakia":"Balto-Slavic"
            ,"Slovenia":"Balto-Slavic","Spanish":"Latin","Sweden":"Germanic","Turkey":"Else","Ukraine":"Balto-Slavic"
            }

                      
    

def main(argv):
 start=process_time() 
 bagOfwords(str(sys.argv[1])) #the path of text_chunks directory
 t=process_time() 
 print("All done :-), the time it's take {0:.4f}".format((t-start)/60),"min")
 
 

pass
if __name__ == "__main__":
    result = main(sys.argv)
    if result is not False:
      print("The process was completed successfully...\n")
    