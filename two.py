import pg

db = pg.DB(dbname='music_db')
db.debug = True
# query = db.query("""insert into track(name, duration) values ('Bye Bye Bye', '00:05:30')""")
n = 'Bye Bye Bye'
d = '00:05:30'
db.insert('track', name = n, duration = d)
