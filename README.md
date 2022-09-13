# bestrappers79topresent
Analysis of Rappers lyrics and their general themes by artists

In this repository, I will be attempting to access, acquire lyrics of best rappers through the years by album(s) of the year nominated for best rapper and analyze the themes using text analysis with nltk and build a visual representation of what the potential culture of r&b and hip hop was like during the years.


*best_rappers.csv* -- Manually collected top hip hop artists of the year (1979-2021) as declared by Complex

      - https://www.complex.com/music/the-best-rapper-alive-every-year-since-1979
      
      - future build will expand on top 5 rappers of the year
      
*request_genius.py* -- Access through genius api with a client access token (not provided)

                      - initiates base url & parameters
                      
                      - collect searched artists api-path
                      
                      - future build: collect first 20 songs of given artist sorted by popularity
                      
                      - get lyrics url * I will implement a faster method using asynchronous method*

*<unprovided> auth.py* -- access_token  = "insert client access token"

                      - create access token after creating an api-client through https://genius.com/api-clients
                      
                      - future future build: will implement an oauth2 authenticator for a spotify sentiment analyzer

