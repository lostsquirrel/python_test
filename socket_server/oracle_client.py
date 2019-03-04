# myscript.py


import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("ivms_thr", "ivms_thr", "192.168.5.27/orcl")

cursor = connection.cursor()
cursor.execute("""
select * from v_gcxx  where jgsk between 
to_date('2018-11-09 12:00:00', 'yyyy-mm-dd hh24:mi:ss') and
to_date('2018-11-09 12:01:00', 'yyyy-mm-dd hh24:mi:ss')
    """)
for row in cursor:
    print("Values:", row)

cursor.close()
