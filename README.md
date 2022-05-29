# Book Recommendation System
## Table Of Contents
=================

Project Brief

Compatible Programs

Built with

Problem Statement

High Level Design

HLD Components in Brief

Low Level Design: Book Recommendation System 

Recommendation Algorithms 

NLP Algorithms 

Login 

User  

Databases 

Webpage 

Agile Methodology 

Changes Incorporated using Agile Methodologies 

Final App 

Search Bar 

Recommendations 

Project Brief
-------------

Book Recommendation System is a project built under Microsoft Engage 2022 Program, with a focus to use Algorithms to address real-life problem statements. The objective of the project is to create and showcase a working model using Agile methodology to address the identified Problem Statement and follow the real time practices of HLD, LLD, identifications of agile deviations and overall learnings and highlighting future scope of the project

### Platform

Laptops and Desktops: Any Browser

### Built with

Frontend: ReactJS

Backend: Python

Tools: Flask framework using PyCharm

Datasets: Kaggle

Problem Statement
-----------------

Book Reading is a huge hobby for people all across the globe. There are three basics needs that are mandatory for customer delight.

1. Get recommendation based on user personal historical data

2. Add to point 1, the feedback/ratings of the general set of users to get recommendations

3. Some Intelligence to find the recommendations even if spelling mistakes are there or full name not being remembered when trying to search

Book Recommendation System is taking care of all these isolated systems that we find and put across the smart solution for getting the recommendations

High Level Design
-----------------

![](file:///C:/Users/shriy/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

### HLD Components in Brief:

- User: A frontend page where user puts his credential

- Webpage: A frontend form to put the search and get recommendation

- Login: User credential checking module

- NLP Algorithms: To check and provide refined inputs in case user has given misspelled or wrong name in search webpage

- Recommendations Algorithms: To train AI, provide recommendations using Refined Input from NLP Algorithm module and three databases

- Database User: Contains historical Data of user

- Database User Ratings: Contains Rating data of all users

- Database Books: Contains data pertaining to books from where recommendation results shall come as per Recommendation Algorithms

Low Level Design: Book Recommendation System
--------------------------------------------

### Recommendation Algorithms

![](file:///C:/Users/shriy/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

Essentially an AI engine that trains itself for Recommendations and heart of whole system

Shall use Collaborative Filtering Recommendation using k-Nearest Neighbor. k-Nearest Neighbour is a machine learning algorithm to find clusters of similar users based on common ratings, and make predictions using the average rating of top-k nearest neighbors.

The start point for Recommendation algorithm is refined search string (name of the book for which recommendations are sought) that is output of NLP Algorithms

Training of AI is done using data sets of users rating data, user historical data for books

Output of Recommendation Algorithm are string/s data of Books recommended from data of books

### NLP Algorithms

Priority Medium: NLP Algorithm or equivalent logic that can be used in correcting misspelled or partially wrong inputs in search box webpage for refined input to Recommendation engine

Natural Language Processing will use Books database to find the match for the book that the user is actually looking for.

### Login

![Diagram

Description automatically generated](file:///C:/Users/shriy/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)

Login Module (Priority Low) shall check credential of User details entered in User Web page

- It shall check against stored user credential in user's database and will throw error box in user webpage.

- In case credentials are correct, it shall move to Webpage and the user's historical data will be used by Recommendation Algorithms

### User:

Priority Low: A front end web page to be created using React where user can input his credential. The credentials are checked by Login credential checking module. If credentials are not correct, A pop up to inform user and ask him to enter again. If correct, the user is now defined in the system for getting user historical data, to be used, by Recommendation Algorithms

### Databases

#### Users

Contains the historical data of users like their credentials, ratings for books, Location, age etc.

User IDs (User-ID) are to be anonymized and map to integers.

#### Books

Books database provides details of books identification number and details as follows

Books are identified by their respective ISBN (ISBN is the thirteen-digit number, which replaces the handling of long bibliographic descriptive records. ISBN is known throughout the world as a short and clear machine-readable identification number, which marks any book unmistakably.)

Content-based information (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services.

In case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large.

### Ratings

- Contains the book rating information through fields of ISBN, Rating and User ID.

- Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0

### Webpage

Webpage shall contain

- Form box where user shall provide the name of book for which he is seeking recommendations

- Grid or tabular format to display Recommendations as given by Recommendations Algorithms

- To be created using ReactJS

- API will be created using flask or some other framework (to be decided) so that webpage can make an API call to backend for using the algorithm.

Agile Methodology
-----------------

### What is Agile Methodology

Agile is a development methodology adopted today in the software industry. Agile promotes teamwork, flexible procedures etc. Since I was the only one working on the project, I used flexible procedures of Agile Methodology to arrive at Final App

Changes Incorporated using Agile Methodologies
----------------------------------------------

### NLP Algorithm:

It was assumed that NLP algorithms will be required to sort the inputs given by User so that Book name can be cross referenced from Database and recommendations are provided accordingly.

During the development, It was found that ReactJS can be used for same task and hence NLP Algorithm incorporations was dropped and Final App was made using ReactJS

### User Login

It was a low priority component due to time constraints, accordingly, it was moved to future scope and removed from scope of the Final App

### Book not found in dataset

It was found that there shall be an eventuality wherein book typed is not in data set. Accordingly, additional scope was added to final App wherein, if book is not found in dataset, a book not found message is to be displayed

Final App
---------

Final App has now a web page with a search window and a button.

- As the App is launched the records of the books are fetched using an API call to local host server (5 to 10 seconds) and works in the background

- User can now enter the name of the book for which he seeks recommendations

- As user starts typing into the search bar, the exact/similar names of the books are fetched from local hosts and are displayed simultaneously in list form

- User can now select the book for which he wants to have a recommendation and click on search button

- Once the user clicks on the search button, the recommendation engine gets the input through API call

- Recommendation Engine now process the input with cross reference of user data and rating data and provides the outputs as name of the book

- This output data goes to web page through API call and are displayed as Recommended books

- Book not found Message is displayed if user enters a book name that is not in data set

Future Scope                
----------------------------

The Future Scope of Book Recommendation System can be broadly divided into two:

### Existing Project Scope

Clearly following are the existing project scope that were not attempted due to lack of time

- User Login module: wherein User can login his credential and is able to use application after verification

- User gets other details of Recommended books like Author, ratings etc.

- Genre of the book to be incorporated in data set and selection

### Future Project Scope

With modification and increased scope, the Book Recommendation System can be modified to Product Recommendation System

- Introduction of field like Attributes, sizes, colour, genre, Gender, age group in datasets and selection of the same on webpage can make the system ready for Product recommendations

- The API of the Recommendation Engine can be made available for other websites to use it
