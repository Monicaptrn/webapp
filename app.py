import streamlit as st
from sqlalchemy import text

list_position = ['', 'Waiter', 'Cashier', 'Cheff']
list_gender = ['', 'male', 'female']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://monicapnatalia:AL0SxXokUnH6@ep-aged-wave-13244601.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS EMPLOYEE (id_employee text, employee_name text, gender text, date_of_birth date, position text, handphone text, address text, start_and_finish_time text, total_working_hours time, salary text);')
    session.execute(query)

st.header('RESTAURANT EMPLOYEE DATA MANAGEMENT')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM employee ORDER By id_employee;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO employee (id_employee, employee_name, gender, date_of_birth, position, handphone, address, start_and_finish_time, total_working_hours, salary) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':None, '5':'', '6':'', '7':'', '8':[], '9':None, '10':''})
            session.commit()

    data = conn.query('SELECT * FROM employee ORDER By id_employee;', ttl="0")
    for _, result in data.iterrows():        
        id_employee = result["id_employee"]
        employee_name_lama = result["employee_name"]
        gender_lama = result["gender"]
        date_of_birth_lama = result["date_of_birth"]
        position_lama = result["position"]
        handphone_lama = result["handphone"]
        address_lama = result["address"]
        start_and_finish_time_lama = result["start_and_finish_time "]
        total_working_hours_lama = result["total_working_hours"]
        salary_lama = result["salary"]

        with st.expander(f'a.n. {employee_name_lama}'):
            with st.form(f'data-{id}'):
                id_employee = st.text_input("id_employee", id_employee)
                employee_name_baru = st.text_input("employee_name", employee_name_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                date_of_birth_baru = st.date_of_birth_input("tanggal", date_of_birth_lama)
                position_baru = st.selectbox("position", list_position, list_position.index(position_lama))
                handphone_baru = st.text_input("handphone", handphone_lama)
                address_baru = st.text_input("address", address_lama)
                start_and_finish_time_baru = st.multiselect("start_and_finish_time", ['06:00', '07:00', '08:00', '09:00', '17:00'], eval(start_and_finish_time_lama))
                total_working_hours_baru = st.time_input("total_working_hours", total_working_hours_lama)
                salary_baru = st.text_input("salary", salary_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE employee \
                                          SET id_employee=:1, employee_name=:2, gender=:3, date_of_birth=:4, \
                                          position=:5, handphone=:6, address=:7, start_and_finish_time=:8, total_working_hours=:9, salary=:10;')
                            session.execute(query, {'1':id_employee, '2':employee_name_baru, '3':gender_baru, '4':date_of_birth_baru, 
                                                    '5':position_baru, '6':handphone_baru, '7':address_baru, '8':str(start_and_finish_time_baru), '9':total_working_hours_baru, '10':salary_baru})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM employee WHERE id_employee=:1;')
                        session.execute(query, {'1':id_employee})
                        session.commit()
                        st.experimental_rerun()