import shapefile #mengimport shapefile
w=shapefile.Writer('Soal7', shapeType=shapefile.POLYGON) #membuat file bernama Soal7 dan mendifinisikan shapetypenya yaitu POLYGON
w.shapeType #mendeklarasikan(memanggil) shape type
w.field("kolom1","C") #membuat field pertama
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu")  #membuat record pertama
w.poly([[[1,3],[5,3],[1,2],[5,2]]]) #memmbuat polygon pertama
w.close() #menghentikan perintah