from flask import Flask
from flask_restful import Resource, Api
import pickle
import pandas as pd
import numpy as np
from flask_cors import CORS



app = Flask(__name__)

CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self, book_name):
        books = pd.read_csv("C:\\Users\\shriy\\book-recommendation-system\\Books.csv")
        users = pd.read_csv("C:\\Users\\shriy\\book-recommendation-system\\Users.csv")
        rating = pd.read_csv("C:\\Users\\shriy\\book-recommendation-system\\Ratings.csv")
        books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]
        rating.rename(columns={'Book-Rating': 'Rating'}, inplace=True)
        books.rename(columns={'Book-Title': 'Title', 'Book-Author': 'Author', 'Year-Of-Publication': 'Year','Publisher': 'Publisher'}, inplace=True)
        s = rating['User-ID'].value_counts() > 200
        n = s[s].index
        rating = rating[rating['User-ID'].isin(n)]
        rating_with_books = rating.merge(books, on='ISBN')
        number_rating = rating_with_books.groupby('Title')['Rating'].count().reset_index()
        number_rating.rename(columns={'Rating': 'number of rating'}, inplace=True)
        final_ratings = rating_with_books.merge(number_rating, on='Title')
        final_ratings = final_ratings[['User-ID', 'ISBN', 'Rating', 'Title', 'Author', 'Year', 'Publisher', 'number of rating',]]
        final_ratings = final_ratings[final_ratings['number of rating'] >= 50]
        final_ratings.drop_duplicates(['User-ID', 'Title'], inplace=True)
        book_pivot = final_ratings.pivot_table(columns='User-ID', index='Title', values='Rating')
        book_pivot.fillna(0, inplace=True)
        book_pivot.iloc[237, :].values.reshape(1, -1)



        #budget = request.args.get('budget')
        print(book_name)
        # Let's load the package
        book_name = str(book_name)
        #df = pd.DataFrame(book_name, columns=['Title'])
        book_id = np.where(book_pivot.index == book_name)[0][0]
        model = pickle.load(open('model.pkl', 'rb'))
        distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1))
        ans=''
        for i in range(len(suggestions)):
            if i == 0:
                ans="the suggestions of "+ book_name + " are : "

            if not i:
                for item in book_pivot.index[suggestions[i]]:
                    ans = ans + " " + item + ","
                #ans= ans +str(book_pivot.index[suggestions[i]])
        #prediction = model.predict(df)
        #prediction = str(prediction[0])

        return str(ans)



#data api
class getData(Resource):
    def get(self):
            books = pd.read_csv("C:\\Users\\shriy\\book-recommendation-system\\Books.csv")
            users = pd.read_csv("C:\\Users\\shriy\\book-recommendation-system\\Users.csv")
            rating = pd.read_csv("C:\\Users\\shriy\\book-recommendation-system\\Ratings.csv")
            #df = df.rename(columns={'Book-Title': 'Title', 'Book-Author': 'Author', 'Year-Of-Publication': 'Year','Publisher': 'Publisher'}, inplace=True)
            #print(df.head())
            #out = {'key':str}

            rating.rename(columns={'Book-Rating': 'Rating'}, inplace=True)
            books.rename(columns={'Book-Title': 'Title', 'Book-Author': 'Author', 'Year-Of-Publication': 'Year',
                                  'Publisher': 'Publisher'}, inplace=True)
            s = rating['User-ID'].value_counts() > 200
            n = s[s].index
            rating = rating[rating['User-ID'].isin(n)]
            rating_with_books = rating.merge(books, on='ISBN')
            number_rating = rating_with_books.groupby('Title')['Rating'].count().reset_index()
            number_rating.rename(columns={'Rating': 'number of rating'}, inplace=True)
            final_ratings = rating_with_books.merge(number_rating, on='Title')
            final_ratings = final_ratings[
                ['User-ID', 'ISBN', 'Rating', 'Title', 'Author', 'Year', 'Publisher', 'number of rating', 'Image-URL-S',
                 'Image-URL-M', 'Image-URL-L']]
            final_ratings = final_ratings[final_ratings['number of rating'] >= 50]
            final_ratings.drop_duplicates(['User-ID', 'Title'], inplace=True)

            #book_pivot = final_ratings.pivot_table(columns='User-ID', index='Title', values='Rating')
            #book_pivot.fillna(0, inplace=True)
            #book_pivot.iloc[237, :].values.reshape(1, -1)




            res = final_ratings.to_json()
            #print( res)
            return res


api.add_resource(getData, '/api')
api.add_resource(prediction, '/prediction/<book_name>')



if __name__ == '__main__':
    app.run()
