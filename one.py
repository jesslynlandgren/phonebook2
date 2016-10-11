import pg

db = pg.DB(dbname='music_db')
query = db.query('select * from track')
result = query.namedresult()

for row in result:
    print 'Track Name: {0}, Duration: {1}'.format(row.name, row.duration)
