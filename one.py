import pg

db = pg.DB(dbname='music_db')
query = db.query('select * from track')

for row in query:
    print row
