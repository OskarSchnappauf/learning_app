from PIL import Image
import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

im = Image.open('DNA.jpeg')
st.set_page_config(page_title='Study DNA', page_icon=im, layout="wide")
image = Image.open('HochschuleB-R-S.svg.png')

import plotly.graph_objects as go

labels = ['Introns','Repetitive Seq.','Nicht rep. Seq.', 'Konservierte nicht-kodierende Seq.', 'Protein kodierende Seq']
values = [40, 47, 8, 3.5, 1.5]
night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)',
                'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                     'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                 'rgb(36, 73, 147)', 'rgb(175, 49, 35)']
cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                'rgb(175, 51, 21)', 'rgb(35, 36, 21)']

#values = ['47', '40', '8', '1.5', '3.5']
# Use `hole` to create a donut-like pie chart
#fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig = go.Figure(data=[go.Pie(labels=labels, values=values,
                             hole=.3, pull=[0, 0, 0, 0.2, 0], rotation=90,
                             textinfo='percent+label', textfont_size=12, marker_colors=irises_colors)])
#fig.update_layout(title_text='Human Genome')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
#fig.show()
#fig.write_image("genome.pdf", scale=2)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_happy = "https://assets7.lottiefiles.com/packages/lf20_touohxv0.json"
lottie_json_happy = load_lottieurl(lottie_url_happy)

lottie_url_ok = "https://assets1.lottiefiles.com/private_files/lf30_uDAsLk.json"
lottie_json_ok = load_lottieurl(lottie_url_ok)
#st_lottie(lottie_json)

st.image(image,use_column_width=True)
#st.image(image,use_column_width=True)
st.header('Choose a topic to study')
categories = ['-','Basic concepts', 'Chromosomal disorders','Single nucleotide variants', 'Del/Dups']
option = st.selectbox('',(categories))
if 'count' not in st.session_state:
     st.session_state.count = 0
if 'question_count' not in st.session_state:
     st.session_state.question_count = 0
st.header('Welcome to our Molecular diagnostic study app')


#option = st.sidebar.selectbox('Choose category to study',(categories))
if option == 'Basic concepts':
    with st.form("Question 1"):
        st.subheader('Question 1:')
        correct_answer_Q1 = 'Chromosomes'
        st.write('What gets separated during Meiosis I?')
        answer_Q1 = st.radio("Which one is correct",('Chromatids', 'Chromosomes', 'Centriols', 'DNA'))
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.question_count += 1
            if answer_Q1 == correct_answer_Q1:
                st.write('Yes, good job!')
                st.balloons()
                st.session_state.count += 25
            else:
                st.write('Unfortunately this is not correct, maybe you want to watch this video to refresh your knowledge')
                st.video('https://www.youtube.com/watch?v=84jlwjvrJwY')


    with st.form("Question 2"):
        st.subheader('Question 2:')
        correct_answer_Q2 = 'Proteins'
        st.write('What is produced during translation?')
        answer_Q2 = st.radio("Which one is correct",('DNA', 'RNA', 'tRNA', 'Proteins'))
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.question_count += 1
            if answer_Q2 == correct_answer_Q2:
                st.write('Yes, good job!')
                st.balloons()
                st.session_state.count += 25
            else:
                st.write('Unfortunately this is not correct, maybe you want to watch thsi video to refresh your knowledge')
                st.video('https://www.youtube.com/watch?v=gG7uCskUOrA')

    with st.form("Question 3"):
        st.subheader('Question 3:')
        correct_answer_Q3 = '1.5%'
        st.write('What approximate section of the human genome codes for proteins')
        answer_Q3 = st.radio("Which one is correct",('10%', '5%', '1.5%', '25%'))
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.question_count += 1
            if answer_Q3 == correct_answer_Q3:
                st.write('Yes, good job!')
                st.balloons()
                st.session_state.count += 25
            else:
                st.write('Here comes a proper explanation and a figure to get some context')
                st.plotly_chart(fig, use_container_width=True)

    # with st.form("Question 3"):
    #     st.subheader('Question 3:')
    #     correct_answer_Q4 = 'TAG, TAA, TGA'
    #     st.write('What are the three STOP codons in humans')
    #     answer_Q3 = st.radio("Which one is correct",('TAG, TAA, TGA', 'TAC, TAA, TGA', 'ATG, TAA, TGA', 'TAG, TAA, TGT'))
    #     submitted = st.form_submit_button("Submit")
    #     if submitted:
    #         st.session_state.question_count += 1
    #         if answer_Q4 == correct_answer_Q3:
    #             st.write('Yes, good job!')
    #             st.balloons()
    #             st.session_state.count += 25
    #         else:
    #             st.write('Here comes a proper explanation why the answer is incorrect!')

    with st.form("Question 4"):
        st.subheader('Question 4:')
        correct_words = ('treatment', 'costs', 'personalized', 'prevention')
        st.write('Why is molecular diagnostic so important?')
        answer_4 = st.text_area('Type your answer').split(" ")
        for i in range(len(answer_4)):
            answer_4[i] = answer_4[i].lower().strip()
        submitted = st.form_submit_button("Submit")
        keyword_count = 0
        if submitted:
            st.session_state.question_count += 1
            #st.write(answer_4)
            for word in correct_words:
                if word in answer_4:
                    keyword_count += 1
            if keyword_count == len(correct_words):
                st.write(f'Yes, good job! You got {keyword_count} of {len(correct_words)} keywords correct!')
                st.balloons()
                st.session_state.count += 25
            else:
                st.write(f'You got {keyword_count} of {len(correct_words)} keywords correct!')
                st.write('A perfect answer would be: \n\n'
                """Accurate and early diagnosis: Molecular diagnostic tests can detect diseases at an early stage, often before symptoms appear. This allows for earlier treatment, which can lead to better outcomes and lower healthcare costs. Personalized medicine: Molecular diagnostics can identify genetic variations that may impact an individual's response to certain medications. This information can be used to personalize treatment plans and improve patient outcomes. Infectious disease control: Molecular diagnostics can rapidly identify the presence of infectious diseases, allowing for more targeted treatment and prevention strategies. This is particularly important in controlling outbreaks and pandemics. Cancer diagnosis and treatment: Molecular diagnostics can help identify specific genetic mutations that drive the growth of cancer cells. This information can be used to guide treatment decisions and develop new targeted therapies.""")

st.subheader('Progress bar')
st.write(f'Out of 4 questions, you got {st.session_state.question_count} questions correct')
st.progress(st.session_state.count)


if st.session_state.count == 100 and st.session_state.question_count == 4:
    st.header('All answers correct!!!')
    st_lottie(lottie_json_happy)
if st.session_state.count != 100 and st.session_state.question_count == 4:
    st.header('Not all answers correct, maybe next time!')
    st_lottie(lottie_json_ok)
