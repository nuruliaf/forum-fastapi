Nama    : Nurul Izza Afkharinah
NIM     : 18219011
Tugas   : API Deployment - Modul Forum dan Pengajuan Forum

Cara Compile di VSCode: 
1. Masuk forum Terminal > New Terminal
2. Pilih terminal 'wsl', pastikan direktori file yang dituju sudah benar
3. $ python3 run.py
4. click link http://127.0.0.1:8081/docs

Deskripsi Singkat Tugas
Authentikasi FastAPI
    Diberikan form autentikasi untuk Admin ketika ingin melakukan CRD Forum dan CRUD Pengajuan Forum. 
    Admin diharuskan melakukan login terlebih dahulu agar mendapat token yang digunakan untuk authorize.
    Di-set username dan password untuk login, yaitu pada file admin.json
    Apabila Admin tidak melakukan login terlebih dahulu, CRD Forum dan CRUD Pengajuan Forum akan gagal dan sistem akan menampilkan pesan 
        {
        "detail": "Not authenticated"
        }
    Step untuk login sebagai berikut:
        1. Admin memasukkan username dan password pada Tag Admin 'Admin Login'
        2. Ketika Admin berhasil melakukan login, sistem akan memberikan access token authorize
        3. Copy access token dan paste di forum 'Authorize' 
        4. Admin berhasil login apabila token benar dan bisa mengakses CRD Forum dan CRUD Pengajuan Forum

CRD Forum
Create new one item forum
    Dilakukan penambahan satu item baru pada forum.json
    Admin hanya perlu meng-input judul forum, nama pengirim, dan kategori yang ingin ditambahkan, tidak perlu melakukan input id forum karena id forum bersifat increment
    Data forum (id forum, judul forum, nama pengirim, dan kategori forum) akan bertambah secara otomatis di forum.json Ketika Admin selesai menambahkan forum dan id forum akan otomatis terurut menaik (id+1)

Read all item forum
    Dilakukan pembacaan seluruh data pada forum.json
    Data yang akan ditampilkan dalam bentuk array yang terdiri dari id forum, judul forum, nama pengirim, dan kategori forum

Read one item forum
    Dilakukan pembacaan salah satu data pada forum.json
    Admin bebas memilih data forum mana yang ingin dibaca dengan hanya meng-input id forum
    Data yang akan ditampilkan hanya satu buah dan dalam bentuk array yang terdiri dari id forum, judul forum, nama pengirim, dan kategori forum

Delete one item forum
    Dilakukan delete untuk satu item forum yang terdapat di forum.json
    Admin diharuskan meng-input id forum yang ingin dihapus
    forum (id forum, judul forum, nama pengirim, dan kategori forum) dengan id forum tersebut akan terhapus secara otomatis, dan forum.json akan melakukan update data

CRUD Pengajuan Forum
Create new one item pengajuan forum
    Dibuat asumsi Admin dapat melakukan pengajuan forum.
    Dilakukan penambahan satu item baru pada pengajuan.json
    Admin hanya perlu meng-input judul pengajuan, nama pengaju, dan kategori yang ingin ditambahkan, tidak perlu melakukan input id pengajuan dan status karena id pengajuan bersifat increment dan status selalu di-set 'Belum disetujui'
    Data pengajuan (id pengajuan, judul pengajuan, nama pengaju, kategori pengajuan, dan status) akan bertambah secara otomatis di pengajuan.json ketika Admin selesai menambahkan pengajuan dan id pengajuan akan otomatis terurut menaik (id+1)
    Namun pada kenyataannya, pengajuan forum hanya dapat dilakukan oleh customer dan admin hanya bertugas untuk menyetujui/menolak pengajuan forum.
    Fungsi Create ini akan digunakan untuk menambah data pengajuan apabila data pada pengajuan.json sudah habis sebab pengajuan telah disetujui oleh Admin dimana data pada pengajuan.json akan berpindah ke forum.json

Read all item pengajuan forum
    Dilakukan pembacaan seluruh data pada pengajuan.json
    Data yang akan ditampilkan dalam bentuk array yang terdiri dari id pengajuan, judul pengajuan, nama pengaju, kategori pengajuan, dan status.

Read one item pengajuan forum
    Dilakukan pembacaan salah satu data pada pengajuan.json
    Admin bebas memilih data pengajuan mana yang ingin dibaca dengan hanya meng-input id pengajuan
    Data yang akan ditampilkan hanya satu buah dan dalam bentuk array yang terdiri dari id pengajuan, judul pengajuan, nama pengaju, kategori pengajuan, dan status.

Update one item pengajuan forum
    Dilakukan update untuk satu item pengajuan forum yang terdapat di pengajuan.json
    Admin hanya perlu meng-input id pengajuan yang ingin disetujui sehingga data dengan id pengajuan yang sudah di-input pada pengajuan.json akan berpindah ke forum.json
    Forum akan ter-update secara otomatis di forum.json ditandai dengan bertambahnya satu data forum di ketika Admin berhasil melakukan update

Delete one item pengajuan forum
    Dilakukan delete untuk satu item pengajuan forum yang terdapat di pengajuan.json
    Admin diharuskan meng-input id pengajuan yang ingin ditolak
    Data pengajuan (id pengajuan, judul pengajuan, nama pengaju, kategori pengajuan, dan status) dengan id pengajuan tersebut akan terhapus secara otomatis, dan pengajuan.json akan melakukan update data