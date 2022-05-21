# Book Recommendation System
## Problem Statement: 
To build a book recommendation system that shows customer recommendation based on the books that they have read or what they are searching/interested in
## High Level Design: Book Recommendation System
 ![image](https://user-images.githubusercontent.com/78153966/169660652-057569f6-3510-47ab-8990-a74354fe4d41.png)


### Introduction:
Book Reading is a huge hobby for people all across the globe. There are three basics needs that are mandatory for customer delight.
1.	Get recommendation based on user personal historical data
2.	Add to point 1, the feedback/ratings of the general set of users to get recommendations
3.	Some Intelligence to find the recommendations even if spelling mistakes are there or full name not being remembered when trying to search
Book Recommendation System is taking care of all these isolated systems that we find and put across the smart solution for getting the recommendations

### HLD Components in Brief:

•	User: A frontend page where user puts his credential

•	Webpage: A frontend form to put the search and get recommendation

•	Login: User credential checking module

•	NLP Algorithms: To check and provide refined inputs in case user has given misspelled or wrong name in search webpage

•	Recommendations Algorithms: To train AI, provide recommendations using Refined Input from NLP Algorithm module and three databases

•	Database User: Contains historical Data of user

•	Database User Ratings: Contains Rating data of all users

•	Database Books: Contains data pertaining to books from where recommendation results shall come as per Recommendation Algorithms


## Low Level Design: Book Recommendation System

### Recommendation Algorithms
![image](https://user-images.githubusercontent.com/78153966/169660665-32c44b0f-54ff-4f09-9bbf-cfce3e61078f.png)

 
•	Essentially an AI engine that trains itself for Recommendations and heart of whole system

•	Shall use Collaborative Filtering Recommendation using k-Nearest Neighbor. k-Nearest Neighbour is a machine learning algorithm to find clusters of similar users based on common ratings, and make predictions using the average rating of top-k nearest neighbors.

•	The start point for Recommendation algorithm is refined search string (name of the book for which recommendations are sought) that is output of NLP Algorithms.

•	Training of AI is done using data sets of users rating data, user historical data for books

•	Output of Recommendation Algorithm are string/s data of Books recommended from data of books

### NLP Algorithms

•	Priority Medium: NLP Algorithm or equivalent logic that can be used in correcting misspelled or partially wrong inputs in search box webpage for refined input to Recommendation engine

•	Natural Language Processing will use Books database to find the match for the book that the user is actually looking for.


### Login

![image](https://user-images.githubusercontent.com/78153966/169660694-01063851-179c-4f53-a2ba-9bd6185e52a3.png)

•	Login Module (Priority Low) shall check credential of User details entered in User Web page

•	It shall check against stored user credential in user’s database and will throw error box in user webpage.

•	In case credentials are correct, it shall move to Webpage and the user’s historical data will be used by Recommendation Algorithms

### User: 
Priority Low: A front end web page to be created using React where user can input his credential. The credentials are checked by Login credential checking module. If credentials are not correct, A pop up to inform user and ask him to enter again. If correct, the user is now defined in the system for getting user historical data, to be used, by Recommendation Algorithms

### Databases

#### Users
•	Contains the historical data of users like their credentials, ratings for books, Location, age etc.

•	User IDs (User-ID) are to be anonymized and map to integers. 

#### Books
•	Books database provides details of books identification number and details as follows
Books are identified by their respective ISBN (ISBN is the thirteen-digit number, which replaces the handling of long bibliographic descriptive records. ISBN is known throughout the world as a short and clear machine-readable identification number, which marks any book unmistakably.)

•	Content-based information (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services.

•	In case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large.

#### Ratings
•	Contains the book rating information through fields of ISBN, Rating and User ID.

•	Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0


### Webpage
* Webpage shall contain
  * Form box where user shall provide the name of book for which he is seeking recommendations
  * Grid or tabular format to display Recommendations as given by Recommendations Algorithms
* To be created using ReactJS 
* API will be created using flask or some other framework (to be decided) so that webpage can make an API call to backend for using the algorithm.
