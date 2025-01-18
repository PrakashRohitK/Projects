from neo4j import GraphDatabase,basic_auth
driver = GraphDatabase.driver(
  "bolt://75.101.169.245:7687",
  auth=basic_auth("neo4j", "democracies-ceremony-check"))
def create_node():
    n1 = input("Enter label name:")
    n2 = input("Enter Title:")
    n3 = input("Enter Label indicator:")
    z = chr(34)
    cq1 = "CREATE" + "(" + n3 + ":" + n1 + "{title:" + z + n2 + z + "})"
    with driver.session(database="neo4j") as session:
        results = session.write_transaction(
            lambda tx: tx.run(cq1,
                              limit="10").data())
def create_rel():
    z1=input("Enter label indicator of node1:")
    z1_a = input("Enter label name of node1:")
    z2=input("Enter label indicator of node2:")
    z2_a = input("Enter label name of node2:")
    rel=input("Enter Relation indicator:")
    rel_1=input("Enter Relation")
    cq="MATCH("+str(z1)+":"+str(z1_a)+")"+','+"("+str(z2)+":"+str(z2_a)+")"+"CREATE"+"("+str(z1)+")"+'-'+"["+str(rel)+':'+str(rel_1)+"]"+"->"+'('+str(z2)+')'
    cq2='''MATCH(cr:Crop),(cr1:Crops) CREATE (cr1)-[r:is_a_type_of]->(cr) 
'''
    with driver.session(database="neo4j") as session:
        tx = session.begin_transaction()
        tx.run(cq)
        tx.commit()

def delete_graph():
    cq="MATCH (n) DETACH DELETE n"
    with driver.session(database="neo4j") as session:
        results = session.write_transaction(
            lambda tx: tx.run(cq,
                              limit="10").data())
def displayall():
    cq="MATCH (n) RETURN (n)"
    with driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(cq,
                              ).data())
        for res in results:
            print(res)
def ret():
    cq=input("Enter Query:")
    with driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(cq,
                              ).data())
        for res in results:
            print(res)
def exit():
    driver.close()
while True:
    print('''
             *******************************************
            | 🙂Welcome to Graph Database Neo4j!🙂       | 
            |You can do the following operations:       |
            |1) Create a Node                           |
            |2) Create a Relationship for existing nodes|
            |3) Delete Graph                            |
            |4) Display all nodes                       |
            |5) Return some data from graph             |
            |6) Exit                                    |
             *******************************************  
            ''')
    option = int(input("Enter an option: "))
    if option==1:create_node()
    elif option==2: create_rel()
    elif option == 3:delete_graph()
    elif option == 4:displayall()
    elif option==5:ret()
    elif option==6:
        print("Thank you")
        exit()
        break
    else:
        print("Enter a valid option!")
