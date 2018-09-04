import random
import sys
import psycopg2
conn = psycopg2.connect("host=localhost dbname=tenant_tutorial16 user=aji password=aji1234567")
cur = conn.cursor()


def genword(minchars=3, maxchars=5, istitle=0):
    vocal = ('a', 'e', 'i', 'o', 'u')
    conso = ('w', 'r', 't', 'y', 'i', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'b', 'n', 'm')
    group = []
    numchar = random.randint(minchars, maxchars)
    for i in range(numchar):
        rnd = random.randint(0, 20)
        if rnd is 0:
            full_name = random.choice(vocal) + random.choice(conso)
        if rnd > 0:
            full_name = random.choice(conso) + random.choice(vocal)
        group.append(full_name)
    group_string = "".join(group)
    if istitle is 1:
        return group_string[:numchar].title()
    else:
        return group_string[:numchar]


def genname(minwords=2, maxwords=3, minchars=3, maxchars=5, istitle=1):
    import random
    numword = random.randint(minwords, maxwords)
    group = []
    for i in range(numword):
        dword = genword(minchars, maxchars, istitle)
        group.append(dword)
    return " ".join(group)


def gendesc(minitem=3, maxitem=100, minwords=5, maxwords=10, minchars=3, maxchars=7, istitle=0):
    import random
    numitem = random.randint(minitem, maxitem)
    group = []
    for i in range(numitem):
        ditem = genname(minwords, maxwords, minchars, maxchars, istitle)
        group.append(ditem)
    return ". ".join(group) + "."


print(sys.argv)

if sys.argv[1] is '1' and sys.argv[1] >= 1:

    for gen in range(int(sys.argv[2])):

        schemas = ('satu', 'dua')
        schema_name = random.choice(schemas)
        # print(schema_name)
        q = "SELECT * FROM {0}.auth_user WHERE is_superuser=True" . format(schema_name)
        # print(q)
        cur.execute(q)
        all = cur.fetchall()
        hitung = 0
        for data in all:
            userID = data[0]
            username = data[4]

            # print('{0}|{1}' . format(userID, username))

            qkategori = "SELECT id, nama_barang FROM {0}.barang_post WHERE set_kategori=True ORDER BY random()" . format(schema_name)
            # print(qkategori)
            cur.execute(qkategori)
            kategori_ = cur.fetchone()

            nama_barang = '{0}' . format(genname(minwords=3, maxwords=3, minchars=2, maxchars=7, istitle=1))
            nama_barang_nospace = nama_barang.lower().replace(" ", "")
            nama_barang2 = '{0} {1} [g]' . format(kategori_[1].replace("[g] ", ""), nama_barang)
            deskripsi = gendesc(minitem=3, maxitem=10, minwords=2, maxwords=5, minchars=2, maxchars=7, istitle=1)
            kode_barang = '{0}.{1}.{2}' . format(nama_barang_nospace[:3], userID, kategori_[0])
            updated_at = '{0}-{1}-{2}T{3}:{4}:{5}.{6}+07:00' . format(random.randint(2017, 2018), str(random.randint(1, 12)).zfill(2), str(random.randint(1, 25)).zfill(2), str(random.randint(0, 23)).zfill(2), str(random.randint(0, 59)).zfill(2), str(random.randint(0, 59)).zfill(2), str(random.randint(0, 999999)).zfill(6))
            qINSERT = "INSERT INTO {0}.barang_post (kode_barang, nama_barang, deskripsi, kategori_id, created_by_id, updated_at, set_kategori) VALUES ('{1}', '{2}', '{3}', {4}, {5}, '{6}', False)" . format(schema_name, kode_barang, nama_barang2, deskripsi[:250], kategori_[0], userID, updated_at)
            # print(qINSERT)
            try:
                hitung = gen + 1
                cur.execute(qINSERT)
                # print('Tersimpan... !!')
                cur.execute('SELECT LASTVAL()')
                id_of_new_row = cur.fetchone()[0]
                # print(id_of_new_row)
                if id_of_new_row > 0:
                    kode_barang2 = '{0}.{1}' . format(kode_barang, id_of_new_row)
                    qUPDATE = "UPDATE {0}.barang_post SET kode_barang='{1}' WHERE id = {2}" . format(schema_name, kode_barang2, id_of_new_row)
                    cur.execute(qUPDATE)
                    conn.commit()
                    print('{0} -- {2} | {1}' . format(hitung, nama_barang2, kode_barang2))
                else:
                    print('TIDAK UPDATE dengan kode barang baru... !! {0}' . format(nama_barang2))

            except ValueError:
                print(qINSERT)
                print('Error... Tidak bisa eksekusi INSERT !! {0}' . format(nama_barang2))

elif sys.argv[1] is '0':
    try:
        schemas = ('satu', 'dua')
        for schema_name in schemas:
            cur.execute("DELETE FROM {0}.barang_post WHERE nama_barang LIKE '%[g]%'" . format(schema_name))
            cur.execute("SELECT MAX( id ) FROM {0}.barang_post" . format(schema_name))
            max_id = cur.fetchone()
            max_id = max_id[0] + 1
            # cur.execute("ALTER TABLE {0}.barang_post AUTO_INCREMENT={1};" . format(schema_name, max_id[0]))
            cur.execute("ALTER SEQUENCE {0}.barang_post_id_seq RESTART WITH {1};" . format(schema_name, max_id))
            conn.commit()
        print('Sudah hapus data [g] ...')
    except ValueError:
        print('Gagal hapus data [g] ...')
