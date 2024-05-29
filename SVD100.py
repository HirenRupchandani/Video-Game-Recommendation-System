from surprise import Reader, Dataset
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from surprise import SVD,accuracy
from collections import defaultdict
from itertools import chain
ratings=[]
result=[]
watched=[]
counter=15

class SVD_Recommend:
    
    def get_top_n(self,predictions, data, n=10):
        '''Return the top-N recommendation for each user from a set of predictions.
    
        Args:
            predictions(list of Prediction objects): The list of predictions, as
                returned by the test method of an algorithm.
            n(int): The number of recommendation to output for each user. Default
                is 10.
    
        Returns:
        A dict where keys are item (raw) ids and values are lists of tuples:
            [(raw item id, rating estimation), ...] of size n.
        '''
    
        # First map the predictions to each user.
        top_n = defaultdict(list)
        for uid, iid, true_r, est, _ in predictions:
            top_n[uid].append((iid, est))
            
        # Then sort the predictions for each user and retrieve the k highest ones.
        for uid, user_ratings in top_n.items():
            user_ratings.sort(key=lambda x: x[1], reverse=True)
            top_n[uid] = user_ratings[:n]
    
        return top_n
    
    def SVDR(self, user='XkH1zxFUbEctT2NLLzPk'):
        final=[]
        result=[]
        # Define the format
        reader = Reader(line_format='item user rating', sep=',')
        # Load the data from the file using the reader format
        data = Dataset.load_from_file('ratings.csv', reader=reader)
        
        #games.csv has game details like id, name and ganre
        data_game = pd.read_csv('game_name.csv', delimiter=',', names = ['app','gameid','gameName','genre'])
        
        d1=data_game[['gameid']]
        d2=data_game['gameName']
        d5=data_game['genre']
        d3=d1.values.tolist()
        d3=list(chain.from_iterable(d3))
        d4=d2.values.tolist()
        d6=d5.values.tolist()

        trainset=data.build_full_trainset()
        testset=trainset.build_anti_testset()
        # First train an SVD algorithm on the movielens dataset.
        algo = SVD()
        algo.fit(trainset)
        
        predictions = algo.test(testset)
        
        rmse1=accuracy.rmse(predictions)
        mae1=accuracy.mae(predictions)
        print("RMSE score for SVD factorization is: "+str(rmse1))
        print("MAE score for SVD factorization is: "+str(mae1))
        
        top_n = self.get_top_n(predictions, data, n=15)
        games=top_n[user]
        game_ids, pred_ratings = map(list, zip(*games))
        k=0
        
        testUserInnerID = trainset.to_inner_uid(user)
        watched = {}
        for itemID, rating in trainset.ur[testUserInnerID]:
            watched[itemID] = 1
        
        print()
        #print(watched)
        for i in game_ids:
            final=[]
            m=i
            n=d3.index(m)
            final.append(m)
            final.append(d4[n])
            final.append(d6[n])
            final.append(pred_ratings[k])
            k=k+1
            result.append(tuple(final))
            
        return result,watched
        #print(user+"'s top 10 using SVD Matrix Factorization:")

'''svd=SVD_Recommend()
svdRecommendation,svdWatched=svd.SVDR()
for i in svdRecommendation:
    result.append(i)
for j in svdWatched:
    watched.append(j)
for itemID,itemName,rating,genre in result:
    if not itemID in watched:
        print(str(itemID) +"\t"+itemName + "\t"+str(rating))
        counter-=1
        if counter==0:
            break
'''