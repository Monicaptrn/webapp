import streamlit as st
import pandas as pd
from sqlalchemy import text

list_jabatan = ['', 'Waiter', 'Cashier', 'Cheff']
list_gender = ['', 'Male', 'Female']
list_shift = ['', "shift 1", "shift 2", "shift 3", "shift 4"]

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://monicapnatalia:AL0SxXokUnH6@ep-aged-wave-13244601.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS EMPLOYEE (id serial, employee_name text, gender char(30), date_of_birth date, \
                                                         jabatan text, handphone text, shift text, total_working_hours time, salary text);')
    session.execute(query)

st.header('RESTAURANT EMPLOYEE DATA MANAGEMENT')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data","Visualisasi Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM EMPLOYEE ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO employee (employee_name, gender, date_of_birth, jabatan, handphone, shift, total_working_hours, salary) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':None, '4':'', '5':'', '6':'[]', '7':None, '8':''})
            session.commit()

    data = conn.query('SELECT * FROM employee ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        employee_name_lama = result["employee_name"]
        gender_lama = result["gender"]
        date_of_birth_lama = result["date_of_birth"]
        jabatan_lama = result["jabatan"]
        handphone_lama = result["handphone"]
        shift_lama = result["shift"]
        total_working_hours_lama = result["total_working_hours"]
        salary_lama = result["salary"]

        with st.expander(f'a.n. {employee_name_lama}'):
            with st.form(f'data-{id}'):
                employee_name_baru = st.text_input("employee_name", employee_name_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                date_of_birth_baru = st.date_input("date_of_birth", date_of_birth_lama)
                jabatan_baru = st.selectbox("jabatan", list_jabatan, list_jabatan.index(jabatan_lama))
                handphone_baru = st.text_input("handphone", handphone_lama)
                shift_baru = st.multiselect("shift", list_shift, eval(shift_lama))
                total_working_hours_baru = st.time_input("total_working_hours", total_working_hours_lama)
                salary_baru = st.text_input("salary", salary_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE employee \
                                          SET employee_name=:1, gender=:2, date_of_birth=:3, \
                                          jabatan=:4, handphone=:5, shift=:6, total_working_hours=:7, salary=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':employee_name_baru, '2':gender_baru, '3':date_of_birth_baru, '4':jabatan_baru, '5':handphone_baru, '6':str(shift_baru), '7':total_working_hours_baru, '8':salary_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM employee WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
                
if page == "Visualisasi Data":
    st.subheader("Visualisasi Programs")
    data = conn.query('SELECT programs, COUNT(*) as count FROM participant GROUP BY programs;')
    st.bar_chart(data.set_index('programs'))
