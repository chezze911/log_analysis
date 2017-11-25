
import psycopg2

# Log Analysis Project #3
# Udacity Full Stack Nanodegree

# Store global database name
DBNAME = 'news'


def execute_query(query):
    try:
        db = psycopg2.connect('dbname=' + DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except BaseException:
        print("Unable to connect to the database.  Please try again.")
    
    except TypeError:
        print('Type error too!')

    
# Problem 1: What are the most popular three articles of all time?
def top_three_articles():
    query_1 = """SELECT title,views 
                 FROM article_view 
                 LIMIT 3;"""
    
    top_three_query = execute_query(query_1)

    print("\n 1. Top Three Articles: \n")
    for result in top_three_query:
        print('\t' + str(result[0]) + ' ----- ' + str(result[1]) + ' views')


    

# Problem 2: Who are the most popular article authors of all time?
def most_popular_authors():
    query_2 = """SELECT authors.name, sum(article_view.views) AS views 
                 FROM article_view,authors
                 WHERE authors.id = article_view.author
                 GROUP BY authors.name 
                 ORDER BY views DESC;"""
                 
    most_popular_authors_query = execute_query(query_2)

    print("\n 2. Most Popular Article Authors: \n")
    for result in most_popular_authors_query:
        print('\t' + str(result[0]) + ' ----- ' + str(result[1]) + ' views')




# Problem 3: On which days did more than 1% of requests lead to errors?
def over_one_percent_error_days():
    query_3 = """SELECT errors.days,
                 ROUND(((errors.errors/total.total) * 100))
                 as percentage
                 FROM errors, total
                 WHERE total.day = errors.day
                 AND (((errors.errors/total.total) * 100) > 1.0)
                 ORDER BY errors.day DESC;"""
    
    over_one_percent_error_days_query = execute_query(query_3)
    
    print("\n 3. High Error days with more than 1 percent error: \n")
    
    if over_one_percent_error_days_query is None:
        print ( '\t' + 'No values in over_one_percent_error_days_query. Fix query')

    else:
        for result in over_one_percent_error_days_query:
            print('\t' + str(result[0].strftime('%B %d, %Y')) + ' ----- ' + str(result[1]) + '%' + ' errors')




if __name__ == '__main__':
    
    top_three_articles()
    most_popular_authors()
    over_one_percent_error_days()
    


