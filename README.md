# Medium Tag Ranker

The porpuse of this project is to list tags usage on Medium, based on a tags search.

Let's say you're in doubt which of the following tags you should use on your article: `java`, `spring` or `spring-boot`.  
With Tag Ranker you can get these tags usages as:

    > python3 app.py java spring spring-boot

    # then you get:
    +-------------+-------+
    |     Tag     | Count |
    +-------------+-------+
    |     java    | 81744 |
    |    spring   | 19576 |
    | spring-boot | 18564 |
    +-------------+-------+

### Running locally
It's pretty simple:

    > pip3 install -r requirements
    > python3 app.py <tags-separated-by-space>