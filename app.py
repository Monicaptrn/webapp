import streamlit as st
from sqlalchemy import text

list_jabatan = ['', 'Waiter', 'Cashier', 'Cheff']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://monicapnatalia:AL0SxXokUnH6@ep-aged-wave-13244601.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS EMPLOYEE (id serial, employee_name varchar, gender char(30), date_of_birth date, \
                                                         jabatan varchar, handphone varchar, start_and_finish_time varchar, total_working_hours time, salary varchar);')
    session.execute(query)

st.header('RESTAURANT EMPLOYEE DATA MANAGEMENT coba')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM EMPLOYEE ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO employee (employee_name, gender, date_of_birth, jabatan, handphone, start_and_finish_time, total_working_hours, salary) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':None, '4':'', '5':'', '6':[], '7':None, '8':''})
            session.commit()

    data = conn.query('SELECT * FROM employee ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        employee_name_lama = result["employee_name"]
        gender_lama = result["gender"]
        date_of_birth_lama = result["date_of_birth"]
        jabatan_lama = result["jabatan"]
        handphone_lama = result["handphone"]
        start_and_finish_time_lama = result["start_and_finish_time"]
        total_working_hours_lama = result["total_working_hours"]
        salary_lama = result["salary"]

        with st.expander(f'a.n. {employee_name_lama}'):
            with st.form(f'data-{id}'):
                employee_name_baru = st.text_input("employee_name", employee_name_lama)
                gender_baru = st.text_input("gender", gender_lama)
                date_of_birth_baru = st.date_input("date_of_birth", date_of_birth_lama)
                jabatan_baru = st.selectbox("jabatan", list_jabatan, list_jabatan.index(jabatan_lama))
                handphone_baru = st.text_input("handphone", handphone_lama)
                start_and_finish_time_baru = st.multiselect("start_and_finish_time", ['06:00', '07:00', '08:00', '09:00', '17:00'], start_and_finish_time_lama)
                total_working_hours_baru = st.time_input("total_working_hours", total_working_hours_lama)
                salary_baru = st.text_input("salary", salary_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE employee \
                                          SET employee_name=:1, gender=:2, date_of_birth=:3, \
                                          jabatan=:4, handphone=:5, start_and_finish_time=:6, total_working_hours=:7, salary=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':employee_name_baru, '2':gender_baru, '3':date_of_birth_baru, 
                                                    '4':jabatan_baru, '5':handphone_baru, '6':str(start_and_finish_time_baru), '7':total_working_hours_baru, '8':salary_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM employee WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
