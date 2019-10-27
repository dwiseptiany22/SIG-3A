import shapefile #meng-import library shapefile

w = shapefile.Writer('soal1') #membuat object Writer baru dan memberi argumen berupa nama file dari shapefilenya yaitu soal1
w.shapeType #menentukan shapeTypenya

w.field("kolom1", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom1 dan tipe datanya yaitu char
w.field("kolom2", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom2 dan tipe datanya yaitu char

w.record("ngek", "satu") #mengisi data pada field yang telah dibuat yaitu kolom1 = ngek dan kolom2 = satu
w.record("ngok", "dua") #mengisi data pada field yang telah dibuat yaitu kolom1 = ngok dan kolom2 = dua

w.point(1,1) #mengisi data point sesuai koordinatnya yaitu x = 1 dan y = 1
w.point(2,2) #mengisi data point sesuai koordinatnya yaitu x = 2 dan y = 2

w.close() #menutup file