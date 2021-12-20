# -*- coding: utf-8 -*-

import sqlite3


"""           JOIN OPERASYONU             """


#iki tane tabloyu birleştirmek. (bu sanatçı ve albüm listesi olabilir)

def joinOperation():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("""select artists.Name, albums.Title 
                                from artists inner join albums
                                on artists.ArtistId = albums.ArtistId """)
                                
    for row in cursor:
        print(row[0] + " / " +row[1]+"\n\n")
        
                                
""" 

 "DB Browser for SQLite" da  SQL kodunu yürüt kısmına
'select albums.Title, artists.Name from artists inner join albums
on artists.ArtistId = albums.AlbumId' yazıp çalıştırırsak,
alt tarafta tabloyu hemen görüntüleriz. 

"""
    
    