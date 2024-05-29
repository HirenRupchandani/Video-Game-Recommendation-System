import random
import string
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tkinter import Button,Entry,Spinbox,IntVar,Label,Frame,Tk,END
from Random100 import Random100
from SVD100 import SVD_Recommend
from COS100 import COS_Recommend

class Recommender:
    def randomString(self, strLen=20):
        letters=string.ascii_letters+string.digits
        return ''.join(random.choice(letters) for i in range(strLen))

    def __init__(self,root):
        self.userID=self.randomString()
        height=720
        width=1440
        offset=50
        data_game = pd.read_csv('game_name.csv', delimiter=',', names = ['app','gameid','gameName','genre'])
        self.data_ratings = pd.read_csv('ratings.csv', delimiter=',', names = ['gameid','userid','ratings'])
        d=data_game[['gameid','gameName','genre']]
        n1=pd.DataFrame(d)
        select=n1.sample(10)
        select=select.values.flatten()
        select=select.tolist()
        self.gameID=select[0::3]
        self.gameName=select[1::3]
        self.genre=select[2::3]
        print(self.gameID)
        print(self.gameName)
        print(self.genre)
        
        self.val1=IntVar()
        self.val2=IntVar()
        self.val3=IntVar()
        self.val4=IntVar()
        self.val5=IntVar()
        self.val6=IntVar()
        self.val7=IntVar()
        self.val8=IntVar()
        self.val9=IntVar()
        self.val10=IntVar()
        self.f=Frame(root,height=height, width=width)
        self.f.propagate(0)
        self.f.pack()
        self.f.configure(bg='#1b2838')
        self.e=Entry(self.f)
        
        #self.l1=Label(text="Enter the Username: ")
        #self.l2=Label(text="Enter the Password: ")
        self.title=Label(self.f,text="Game Recommendation System",fg="white",bg='#1b2838',font =( "Verdana",25,"bold"))
        self.title.place(x=400,y=5)
        self.info=Label(self.f,text="Enter some ratings for given games (1-5): ",fg="white",bg='#1b2838',font =( "Verdana",15,"bold"))
        self.info.place(x=50,y=50)
        self.game1=Label(self.f,text=self.gameName[0],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game1.place(x=10,y=50+offset)
        self.genre1=Label(self.f,text=self.genre[0],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre1.place(x=350,y=50+offset)
        self.s1=Spinbox(self.f,from_=1, to=5,textvariable=self.val1,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s1.place(x=450+offset,y=50+offset)
        self.game2=Label(self.f,text=self.gameName[1],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game2.place(x=10,y=100+offset)
        self.genre2=Label(self.f,text=self.genre[1],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre2.place(x=350,y=100+offset)
        self.s2=Spinbox(self.f,from_=1, to=5,textvariable=self.val2,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s2.place(x=450+offset,y=100+offset)
        self.game3=Label(self.f,text=self.gameName[2],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game3.place(x=10,y=150+offset)
        self.genre3=Label(self.f,text=self.genre[2],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre3.place(x=350,y=150+offset)
        self.s3=Spinbox(self.f,from_=1, to=5,textvariable=self.val3,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s3.place(x=450+offset,y=150+offset)
        self.game4=Label(self.f,text=self.gameName[3],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game4.place(x=10,y=200+offset)
        self.genre4=Label(self.f,text=self.genre[3],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre4.place(x=350,y=200+offset)
        self.s4=Spinbox(self.f,from_=1, to=5,textvariable=self.val4,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s4.place(x=450+offset,y=200+offset)
        self.game5=Label(self.f,text=self.gameName[4],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game5.place(x=10,y=250+offset)
        self.genre5=Label(self.f,text=self.genre[4],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre5.place(x=350,y=250+offset)
        self.s5=Spinbox(self.f,from_=1, to=5,textvariable=self.val5,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s5.place(x=450+offset,y=250+offset)
        self.game6=Label(self.f,text=self.gameName[5],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game6.place(x=10,y=300+offset)
        self.genre6=Label(self.f,text=self.genre[5],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre6.place(x=350,y=300+offset)
        self.s6=Spinbox(self.f,from_=1, to=5,textvariable=self.val6,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s6.place(x=450+offset,y=300+offset)
        self.game7=Label(self.f,text=self.gameName[6],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game7.place(x=10,y=350+offset)
        self.genre7=Label(self.f,text=self.genre[6],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre7.place(x=350,y=350+offset)
        self.s7=Spinbox(self.f,from_=1, to=5,textvariable=self.val7,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s7.place(x=450+offset,y=350+offset)
        self.game8=Label(self.f,text=self.gameName[7],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game8.place(x=10,y=400+offset)
        self.genre8=Label(self.f,text=self.genre[7],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre8.place(x=350,y=400+offset)
        self.s8=Spinbox(self.f,from_=1, to=5,textvariable=self.val8,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s8.place(x=450+offset,y=400+offset)
        self.game9=Label(self.f,text=self.gameName[8],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game9.place(x=10,y=450+offset)
        self.genre9=Label(self.f,text=self.genre[8],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre9.place(x=350,y=450+offset)
        self.s9=Spinbox(self.f,from_=1, to=5,textvariable=self.val9,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s9.place(x=450+offset,y=450+offset)
        self.game10=Label(self.f,text=self.gameName[9],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.game10.place(x=10,y=500+offset)
        self.genre10=Label(self.f,text=self.genre[9],fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.genre10.place(x=350,y=500+offset)
        self.s10=Spinbox(self.f,from_=1, to=5,textvariable=self.val10,width=5,fg="#9CBBC7",bg='#000000',font=("Verdana",10,"bold"))
        self.s10.place(x=450+offset,y=500+offset)
        
        self.b = Button(self.f, text='Submit', command=self.recommendGames,fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.b.place(x=350,y=600)
        self.b2 = Button(self.f, text='Popular Games', command=self.popular,fg="#9CBBC7",bg='#1b2838',font =( "Verdana",10,"bold"))
        self.b2.place(x=200,y=600)
        
    def popular(self):
        appender=[]
        title=['Game ID','Game Name','Genre']
        res=[]
        rating=[]
        finalResult=[]
        watched=[]
        result=[]
        xaxis=0
        yaxis=0
        self.e.destroy()
        rating.append(self.val1.get())
        rating.append(self.val2.get())
        rating.append(self.val3.get())
        rating.append(self.val4.get())
        rating.append(self.val5.get())
        rating.append(self.val6.get())
        rating.append(self.val7.get())
        rating.append(self.val8.get())
        rating.append(self.val9.get())
        rating.append(self.val10.get())
        for i in range(len(self.gameID)):
            appender=[]
            value=rating[i]
            GI=self.gameID[i]
            appender.append(GI)
            appender.append(self.userID)
            appender.append(value)
            res.append(appender)
        #print(res)
        for x in res:
    
            a_series = pd.Series(x, index = self.data_ratings.columns)
            self.data_ratings = self.data_ratings.append(a_series, ignore_index=True)
        
        #print(self.data_ratings.tail(10))

        #saving in a new file
        self.data_ratings.to_csv("ratings.csv", index=False, header=False)
        counter=10
        randomer=Random100()
        randomReco,randomWatched=randomer.Random_Recommend(self.userID)
        for i in randomReco:
            result.append(i)
        for j in randomWatched:
            watched.append(j)
        for itemID,itemName,genre,rating in result:
            appender=[]
            if not itemID in watched:
                appender.append(itemID)
                appender.append(itemName)
                appender.append(genre)
                #appender.append(str(rating))
                finalResult.append(appender)
                counter-=1
                if counter==0:
                    break
        self.result1=Label(self.f,text="Some Popular Games",fg="white",bg='#1b2838',font =( "Verdana",15,"bold"))
        self.result1.place(x=700,y=50)
        
        for i in range(len(title)):
            self.e=Entry(root,width=30,bd=5,fg='white',bg='#1b2838',font =( "Verdana",10,'bold'))
            self.e.place(x=600+xaxis,y=100)
            self.e.insert(END,title[i])
            xaxis+=180
            
        for i in range(len(finalResult)):
            yaxis+=25
            xaxis=0
            for j in range(len(finalResult[0])):
                
                self.e=Entry(root,width=30,bd=5,fg='white',bg='#1b2838',font =( "Verdana",8,'bold'))
                self.e.place(x=600+xaxis,y=100+yaxis)
                self.e.insert(END,finalResult[i][j])
                xaxis+=180
        
        
    def recommendGames(self):
        self.e.destroy()
        appender=[]
        title=['Game ID','Game Name','Genre','Predicted Rating']
        res=[]
        rating=[]
        finalResultSVD=[]
        finalResultCOS=[]
        xaxis=0
        yaxis=0
        rating.append(self.val1.get())
        rating.append(self.val2.get())
        rating.append(self.val3.get())
        rating.append(self.val4.get())
        rating.append(self.val5.get())
        rating.append(self.val6.get())
        rating.append(self.val7.get())
        rating.append(self.val8.get())
        rating.append(self.val9.get())
        rating.append(self.val10.get())
        for i in range(len(self.gameID)):
            appender=[]
            value=rating[i]
            GI=self.gameID[i]
            appender.append(GI)
            appender.append(self.userID)
            appender.append(value)
            res.append(appender)
        print(res)
        for x in res:
    
            a_series = pd.Series(x, index = self.data_ratings.columns)
            self.data_ratings = self.data_ratings.append(a_series, ignore_index=True)
        
        print('\nInserting generated data into Dataframe: ')
        print(self.data_ratings.tail(10))

        #saving in a new file
        self.data_ratings.to_csv("ratings.csv", index=False, header=False)
        counter=5
        svd=SVD_Recommend()
        svdRecommendation,svdWatched=svd.SVDR(self.userID)
        cosr=COS_Recommend()
        cosRecommendation,cosWatched=cosr.CosR(self.userID)
        '''
        for i in svdRecommendation:
            result.append(i)
        for j in svdWatched:
            watched.append(j)
        for i in cosRecommendation:
            result.append(i)
        for j in cosWatched:
            watched.append(j)
       '''
        for itemID,itemName,genre,rating in svdRecommendation:
            appender=[]
            if not itemID in svdWatched:
                appender.append(itemID)
                appender.append(itemName)
                appender.append(genre)
                appender.append(str(rating))
                finalResultSVD.append(appender)
                counter-=1
                if counter==0:
                    break
        counter=5
        for itemID,itemName,genre,rating in cosRecommendation:
            appender=[]
            if not itemID in cosWatched:
                appender.append(itemID)
                appender.append(itemName)
                appender.append(genre)
                appender.append(str(rating))
                finalResultCOS.append(appender)
                counter-=1
                if counter==0:
                    break
        self.result1=Label(self.f,text="Some SVD Recommendations based on your given data are: ",fg="white",bg='#1b2838',font =( "Verdana",15,"bold"))
        self.result1.place(x=650,y=50)
        
        for i in range(len(finalResultSVD[0])):
            self.e=Entry(root,width=30,bd=5,fg='white',bg='#1b2838',font =( "Verdana",10,'bold'))
            self.e.place(x=600+xaxis,y=100)
            self.e.insert(END,title[i])
            xaxis+=180
            
        for i in range(len(finalResultSVD)):
            yaxis+=25
            xaxis=0
            for j in range(len(finalResultSVD[0])):
                
                self.e=Entry(root,width=30,bd=5,fg='white',bg='#1b2838',font =( "Verdana",8,'bold'))
                self.e.place(x=600+xaxis,y=100+yaxis)
                self.e.insert(END,finalResultSVD[i][j])
                xaxis+=180
        xaxis=0
        yaxis=0
        self.result2=Label(self.f,text="Some Cosine Recommendations based on your given data are: ",fg="white",bg='#1b2838',font =( "Verdana",15,"bold"))
        self.result2.place(x=650,y=275)
        
        for i in range(len(finalResultCOS[0])):
            self.e=Entry(root,width=30,bd=5,fg='white',bg='#1b2838',font =( "Verdana",10,'bold'))
            self.e.place(x=600+xaxis,y=325)
            self.e.insert(END,title[i])
            xaxis+=180
            
        for i in range(len(finalResultCOS)):
            yaxis+=25
            xaxis=0
            for j in range(len(finalResultCOS[0])):
                
                self.e=Entry(root,width=30,bd=5,fg='white',bg='#1b2838',font =( "Verdana",8,'bold'))
                self.e.place(x=600+xaxis,y=325+yaxis)
                self.e.insert(END,finalResultCOS[i][j])
                xaxis+=180

root=Tk()
root.title("Game Recommendation System")
mb=Recommender(root)
root.mainloop()
