
def databaseJsonConverter(cur):
    rows=cur.fetchall()
    row_headers=[x[0] for x in cur.description]
    jsonData=[]
    for result in rows:
        jsonData.append(dict(zip(row_headers,result)))
    cur.close()
    return jsonData