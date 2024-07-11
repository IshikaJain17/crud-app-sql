import mysql.connector
import streamlit as st
mysqldb = mysql.connector.connect(host='localhost', user='root', password='ishuthegreat17@123',database='crud_new1')
mysqlcursor = mysqldb.cursor()

def main():
    st.title("Crud operations with mysql");
    
    option=st.sidebar.selectbox("Select an Operation",('Create', 'Read', 'Update', 'Delete'))
    if option=='Create':
        st.subheader('Create a Record')
        name=st.text_input("Enter Name")
        email=st.text_input("Enter Email")
        if st.button("Create"):
          sql =  'insert into users(name,email) values(%s, %s)'
          val = (name, email)    
          mysqlcursor.execute(sql, val)
          mysqldb.commit()
          st.success("Record Created Successfully!!!")
    
    elif option=='Read':
        st.subheader('Read a Record')
        mysqlcursor.execute("select * from users")
        result = mysqlcursor.fetchall()
        for row in result:
            st.write(row)

    elif option=='Update':
        st.subheader('Update a Record')
        id = st.number_input("Enter Id", min_value=1)
        name = st.text_input('Enter New Name')
        email = st.text_input("Enter New Email")
        if st.button("Update"):
            sql = "update users set name=%s, email=%s where id=%s"
            val=(name, email, id)
            mysqlcursor.execute(sql, val)
            mysqldb.commit()
            st.success("Record Updated Successfully!!!")
    elif option=='Delete':
        st.subheader('Delete a Record')
        id=st.number_input('Enter ID', min_value=1)
        if st.button("Delete"):
            sql = "delete from users where id=%s"
            val=(id,)
            mysqlcursor.execute(sql, val)
            mysqldb.commit()
            st.success("Record Deleted Successfully!!!")
if __name__=='__main__':
    main()

mysqldb.close()