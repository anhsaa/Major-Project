def databaseJsonConverter(cur):
    rows=cur.fetchall()
    row_headers=[x[0] for x in cur.description]
    jsonData=[]
    print(rows)
    for result in rows:
        print(result)
        jsonData.append(dict(zip(row_headers,result)))
    return jsonData