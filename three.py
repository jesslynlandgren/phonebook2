import pg

db = pg.DB(dbname='music_db')
db.debug = True
db.update('track', {'id':1, 'name':'Hallelujah - 2'})
