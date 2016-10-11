import pg

db = pg.DB(dbname='music_db')
db.debug = True
db.delete('track', {'id':2})
