#mapper.py
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import warnings
from sklearn.preprocessing import LabelEncoder
warnings.filterwarnings("ignore")

df = pd.read_csv('Mall_Customers.csv')
number = LabelEncoder()
df_gen = number.fit_transform(df['Gender'])
dfg = pd.DataFrame(data = df_gen)
dfu = pd.concat([df,dfg],axis=1)
df = dfu.drop('Gender',axis=1 ,inplace = True)
df = dfu.rename(columns = {0:'Gender'})

df = df[['Age' , 'Gender','Annual Income (k$)' ,'Spending Score (1-100)']].iloc[: , :].values

KMeans = (KMeans(n_clusters = 6 ,init='k-means++', n_init = 10 ,max_iter=300, 
                        tol=0.0001,  random_state= 45, algorithm='elkan') )
KMeans.fit(df)
labels = KMeans.labels_
centroids = KMeans.cluster_centers_
ine = KMeans.inertia_

c0 = str(np.around(np.array(centroids[0]),2))
c1 = str(np.around(np.array(centroids[1]),2))
c2 = str(np.around(np.array(centroids[2]),2))
c3 = str(np.around(np.array(centroids[3]),2))
c4 = str(np.around(np.array(centroids[4]),2))
c5 = str(np.around(np.array(centroids[5]),2))

for x in np.nditer(labels):
#write the results to standard output STDOUT
    #var =  "%s\t%s" % (x, 1)
    #if x == 0:
        #print(var,'\t',c0)
    if x == 0:
        var =  "%s\t%s\t%s" % (x,c0, 1)
        print(var)
    elif x == 1:
        var =  "%s\t%s\t%s" % (x,c1, 1)
        print(var)
    elif x == 2:
        var =  "%s\t%s\t%s" % (x,c2, 1)
        print(var)
    elif x == 3:
        var =  "%s\t%s\t%s" % (x,c3, 1)
        print(var)
    elif x == 4:
        var =  "%s\t%s\t%s" % (x,c4, 1)
        print(var)
    elif x == 5:
        var =  "%s\t%s\t%s" % (x,c5, 1)
        print(var)