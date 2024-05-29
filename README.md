# Video Game Recommendation System

- This project aims to develop a recommender system anticipated to be used by community of gamers.
- It system filters out or evaluates games through the opinions of other similar gamers using collaborative filtering technique and suggest recommended games to the intended user.

## Project Demo
- ![User Input](https://raw.githubusercontent.com/HirenRupchandani/Video-Game-Recommendation-System/main/images/Input.png)
- User is asked to rate randomly taken games from the database. This aims to solve the cold start problem so that the system has something to work with

- ![Recommendations](https://raw.githubusercontent.com/HirenRupchandani/Video-Game-Recommendation-System/main/images/recommendations.png)
- User is recommended games using user-item collaborative filtering based on an SVD Matrix created using user-rating data and then recommendations are generated using cosine similarity.

- ![Recommend Popular Games](https://raw.githubusercontent.com/HirenRupchandani/Video-Game-Recommendation-System/main/images/coldStart.png)
- Another solution to the cold start problem is to show popular games (based on their ratings/hours played)
