print("Membuat daftar Kontak")
print("="*40)
dict = {'Nama1': 'Ari', 'No. Telp1' : '081267888',
        'Nama2': 'Dina', 'No. Telp2': '087677776'} 
print("Nama\t| Nomor Telpon")
print("-"*40)      
print("%s\t| %s" %(dict['Nama1'], dict['No. Telp1']))
print("%s\t| %s" %(dict['Nama2'], dict['No. Telp2']))
print("="*40)      

print("Menampilkan kontak ari")
print("="*40)      
print(dict['No. Telp1'])
print("="*40)

print("Menambah Kontak baru")
print("="*40)
dict['Nama3']= 'Riko'
dict['No. Telp3']= '087654544'
print(dict)
print("="*40)      

print("Mengubah Kontak Dina dengan Nomor 088999776")
print("="*40)      
dict['No. Telp2']='08899976'
print("%s\t| %s" %(dict['Nama2'], dict['No. Telp2']))
print("="*40)      

print("Menampilkan Semua Nama")
print("="*40)      
print(dict['Nama1'])
print(dict['Nama2'])
print(dict['Nama3'])
print("="*40)      

print("Menampilkan Semua Nomor")
print("="*40)      
print(dict['No. Telp1'])
print(dict['No. Telp2'])
print(dict['No. Telp3'])
print("="*40)      

print("Menampilkan Daftar Nama dan Nomor")
print("="*40)      
print("Nama\t| Nomor Telpon")
print("="*40)      
print("%s\t| %s" %(dict['Nama1'], dict['No. Telp1']))
print("%s\t| %s" %(dict['Nama2'], dict['No. Telp2']))
print("%s\t| %s" %(dict['Nama3'], dict['No. Telp3']))
print("="*40)

print("Menghapus Kontak Dina")
print("="*40)
del dict['No. Telp2']
print(dict)
