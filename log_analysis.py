
import psycopg2

# Log Analysis Project #3
# Udacity Full Stack Nanodegree

# Store global database name
DB_NAME = 'news'

def execute_query(query):
    try:
        db = psycopg2.connect('dbname=' + DB_NAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except BaseException:
        print "Unable to connect to the database.  Please try again."
        
        
        

# Problem 1: What are the most popular three articles of all time?
def top_three_articles():
	query = """SELECT title, COUNT(*) AS views 
    			FROM articles, log 
    			WHERE log.path LIKE concat('%', articles.slug, '%') 
    			GROUP BY articles.title ORDER BY views DESC LIMIT 3;"""
    
    top_three_articles_query = execute_query(query)
    
    print "Top Three Articles By Views"
    for i in top_three_articles_query:
        print " "'" + i[0] + '' ---> ' + str(i[1]) + " views"
    

# Problem 2: Who are the most popular article authors of all time?
def most_popular_authors():
	query = ""

# Problem 3: On which days did more than 1% of requests lead to errors?
def high_error_days():
	query = ""



