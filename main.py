import json

from fastapi import FastAPI, Body, Depends, Request
from app.model import AdminLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer


##################### ACCESS JSON #########################
with open("admin.json", "r") as read_file: 
    adm = json.load(read_file)

with open("forum.json", "r") as read_file: 
    frm = json.load(read_file)

with open("pengajuan.json", "r") as read_file:
    ajuan = json.load(read_file)

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome! This is a FORUM-API by 18219011 Nurul Izza Afkharinah. Hope you enjoy it."}

##################### LOGIN ADMIN #########################
def check_admin(frm: AdminLoginSchema):
    for admin in adm['admin']:
        if admin["username"] == frm.username and admin["password"] == frm.password:
            return True
    return False

def check_admin(ajuan: AdminLoginSchema):
    for admin in adm['admin']:
        if admin["username"] == ajuan.username and admin["password"] == ajuan.password:
            return True
    return False

@app.post("/admin/login", tags=["Admin"])
async def admin_login(admin: AdminLoginSchema = Body(...)):
    if check_admin(admin):
        return signJWT(admin.username)
    return {
        "error": "Wrong username or password!"
    }


##################### CRD FORUM #########################
#read all item
@app.get('/forum', dependencies=[Depends(JWTBearer())], tags=["CRD Forum"])
async def read_all_forum():
    return frm

#read an item
@app.get('/forum/{idForum}', dependencies=[Depends(JWTBearer())], tags=["CRD Forum"]) 
async def read_forum(idForum: int) -> dict: 
    for forum_item in frm['forum']:
        if forum_item['idforum'] == idForum:
            return forum_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

#add item
@app.post('/forum', dependencies=[Depends(JWTBearer())], tags=["CRD Forum"])
async def add_forum(judulforum:str, namapengirim:str, kategori:str) -> dict:
    id = 1
    if(len(frm['forum']) > 0):
        idForum = frm['forum'][len(frm['forum']) - 1]['idforum'] + 1
    new_frm = {'idforum':idForum, 'judulforum':judulforum, 'namapengirim':namapengirim, 'kategori':kategori}
    frm['forum'].append(dict(new_frm))
    read_file.close()
    with open("forum.json", "w") as write_file: 
        json.dump(frm, write_file, indent=4)
    write_file.close()
    
    return (new_frm)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error'
        )

#delete item
@app.delete('/forum/{idForum}', dependencies=[Depends(JWTBearer())], tags=["CRD Forum"]) 
async def delete_forum(idForum: int) -> dict: 
    for forum_item in frm['forum']:
        if forum_item['idforum'] == idForum:
            frm['forum'].remove(forum_item)
            read_file.close()
            with open("forum.json", "w") as write_file: 
                json.dump(frm, write_file, indent=4)
            write_file.close()
            return {'Data Forum Deleted Successfully'}
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

##################### CRUD PENGAJUAN FORUM #########################
#read all item
@app.get('/pengajuan', dependencies=[Depends(JWTBearer())], tags=["CRUD Pengajuan Forum"])
async def read_all_pengajuan():
    return ajuan

#read an item
@app.get('/pengajuan/{idPengajuan}', dependencies=[Depends(JWTBearer())], tags=["CRUD Pengajuan Forum"]) 
async def read_pengajuan(idPengajuan: int) -> dict: 
    for pengajuan_item in ajuan['pengajuan']:
        if pengajuan_item['idpengajuan'] == idPengajuan:
            return pengajuan_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

#add item
@app.post('/pengajuan', dependencies=[Depends(JWTBearer())], tags=["CRUD Pengajuan Forum"])
async def add_pengajuan(judulPengajuan:str, namaPengaju:str, kategori:str) -> dict:
    id = 1
    if(len(ajuan['pengajuan']) > 0):
        idPengajuan = ajuan['pengajuan'][len(ajuan['pengajuan']) - 1]['idpengajuan'] + 1
    status = 'Belum disetujui'
    new_ajuan = {'idpengajuan':idPengajuan, 'judulpengajuan':judulPengajuan, 'namapengajuan':namaPengaju, 'kategori':kategori, 'status':status}
    ajuan['pengajuan'].append(dict(new_ajuan))
    read_file.close()
    with open("pengajuan.json", "w") as write_file: 
        json.dump(ajuan, write_file, indent=4)
    write_file.close()
    
    return (new_ajuan)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error'
        )

#update item
@app.patch('/pengajuan/{idPengajuan}', dependencies=[Depends(JWTBearer())], tags=["CRUD Pengajuan Forum"]) 
async def update_pengajuan(idPengajuan: int) -> dict:
    id = idPengajuan
    for pengajuan_item in ajuan['pengajuan']:
        if(len(frm['forum']) > 0):
            idForum = frm['forum'][len(frm['forum']) - 1]['idforum'] + 1
            if pengajuan_item['idpengajuan'] == idPengajuan:
                judulforum = pengajuan_item['judulpengajuan']
                namapengirim = pengajuan_item['namapengaju']
                kategori = pengajuan_item['kategori']
                ajuan['pengajuan'].remove(pengajuan_item)
    new_frm = {'idforum':idForum, 'judulforum':judulforum, 'namapengirim':namapengirim, 'kategori':kategori}
    frm['forum'].append(dict(new_frm))

    read_file.close()
    with open("forum.json", "w") as write_file: 
        json.dump(frm, write_file, indent=4)
    write_file.close()

    read_file.close()
    with open("pengajuan.json", "w") as write_file: 
        json.dump(ajuan, write_file, indent=4)
    write_file.close()

    return (new_frm)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error'
        )

#delete item
@app.delete('/pengajuan/{idPengajuan}', dependencies=[Depends(JWTBearer())], tags=["CRUD Pengajuan Forum"]) 
async def delete_pengajuan(idPengajuan: int) -> dict: 
    for pengajuan_item in ajuan['pengajuan']:
        if pengajuan_item['idpengajuan'] == idPengajuan:
            ajuan['pengajuan'].remove(pengajuan_item)
            read_file.close()
            with open("pengajuan.json", "w") as write_file: 
                json.dump(ajuan, write_file, indent=4)
            write_file.close()
            return {'Data Pengajuan Forum Deleted Successfully'}
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )