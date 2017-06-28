
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
        
        
def print_query_results(query_results):
    print query_results['title']
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ' ---- ' + str(result[1]) + ' views')

# Problem 1: What are the most popular three articles of all time?
query_1 = "SELECT title,views FROM article_view LIMIT 3"
    
query_1_results = dict()

query_1_results['title'] = "\n 1. Top Three Articles By Views \n"
    
    

# Problem 2: Who are the most popular article authors of all time?
query_2 = ""
query_2_results = dict()
query_2_results['title'] = "Most Popular Article Authors By Views"

# Problem 3: On which days did more than 1% of requests lead to errors?
query_3 = ""
query_3_results = dict()
query_3_results['title'] = "High Error days with more than 1 percent error"


# Store query results and print output
query_1_results['results'] = execute_query(query_1)

#print output
print_query_results(query_1_results)



