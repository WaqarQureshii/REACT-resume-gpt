import streamlit as st
# from authentication.google_auth import get_logged_in_user_email, show_login_button, show_logout_button


# from openai import OpenAI

st.write("before auth")


st.write("after auth")

# st.set_page_config(layout="wide")

# st.title('REACT Resume 🤖')
# st.write("Resume Enhancement and Customization Tool (REACT) is pre-trained to be an action-oriented resume editor that takes your resume & your selected job description as a prompt. What differentiates this from other resume editors? It is action-oriented, maintains the spirit of your original resume, and incorporates the key job description skillsets that a hiring manager would look for.")

# # TEXT BOXES AND PROMPTS IN BOXES
# with st.form(key="resume form"):
#     col1, col2, col3, col4 = st.columns(4)
#     job_title = col1.text_area(label="Copy and paste job title", placeholder="Senior Financial Analyst")
#     company_name = col2.text_area(label="Insert company name", placeholder="Nvidia Corporation")
#     industry = col3.text_area(label="Insert your industry", placeholder="Finance")
#     highlight_years = col4.slider(label="Number of years of experience you'd like to highlight - this will show up in your professional profile.", min_value=0, max_value=99, step=1)

#     aboutcol1, aboutcol2 = st.columns(2)
#     about_us = aboutcol1.text_area(label="Copy and paste the \"About Us\" section from the job description/website.", placeholder="NVIDIA has continuously reinvented itself over two decades. Our invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined modern computer graphics, and revolutionized parallel computing. More recently, GPU deep learning ignited modern AI — the next era of computing. NVIDIA is a “learning machine” that constantly evolves by adapting to new opportunities that are hard to solve, that only we can tackle, and that matter to the world. This is our life's work, to amplify human imagination and intelligence. Make the choice, join our diverse team today!", height=1)
#     additional_information = aboutcol2.text_area(label="Additional Information", placeholder="NVIDIA, founded in 1993, is a key innovator in computer graphics and AI technology. They invented the GPU in 1999, which transformed PC gaming and redefined computer graphics. NVIDIA specializes in products and platforms for gaming, professional visualization, data center, and automotive markets123.")
#     jobdescription = st.text_area(label="Job description", placeholder='''We are looking for a Senior Financial Analyst to join our Information Technology FP&A team. The team is responsible for P&L forecasting and reporting as well as providing financial analysis that enables informed decision making across the company. This role is critical within our Finance department, requiring advanced tools and analytical skills, attention to detail, and the ability to meet deadlines. We are looking for a candidate with strong financial modeling abilities, and the capacity to thrive in a fast-paced environment.

#     What you'll be doing:
#     Complete monthly and quarterly financial closing, planning, and reporting processes.
#     Focus areas will be Networking & Infrastructure.
#     Build and maintain robust financial models for accurate forecasting and analysis.
#     Monitor business performance metrics and provide insights on key drivers.
#     Continuously drive operational improvement in financial consolidation and reporting activities.
#     Collaborate with BU finance, cost accounting, and operations teams to maintain, validate, and reconcile data in forecasting and reporting systems.
#     Prepare periodic internal financial reports and presentation materials.
#     Partner with FP&A teams to maintain hierarchies and mappings needed for management and external reporting.

#     What we need to see:
#     8+ years of experience in finance, business, or analytics, within a global, high-tech corporation.
#     Bachelor’s degree in finance, accounting, economics, or a business-related field (or equivalent experience).
#     Proficiency in leading ERP systems (e.g., SAP, Oracle) and experience working with large datasets.
#     Advanced Microsoft Excel skills are required. Experience with BPC, Tableau, Power BI, Python, SQL, and other visualization tools is a plus.
#     An ability to balance being working in the weeds as well as seeing the big picture.
#     Detail-orientated with a strong focus on accuracy and completeness.
#     Excellent communication and interpersonal skills, with an ability to build relationships and collaborate with individuals at all levels of an organization.
#     Ways to stand out from the crowd:
#     Master’s degree in business administration, finance, or accounting.
#     Experience in the Semiconductor industry or Corporate FP&A.
#     Self-starter and problem solver, comfortable dealing with complexity, ambiguity, changes, and tight deadlines.
#     Demonstration of high level analytical and financial modeling skills, with a proven track record of driving process and system improvements.
#     ''', height=100)
#     workexperience = st.text_area(label="Work experience", placeholder='''Senior Financial Analyst at ABC Corp
#     Functions as a broker between the company's corporate finance and regional operations departments. Prepares post-close financial results versus budget analysis of spending with a focus on performance in key areas. Responds to ad-hoc requests for financial information from 17 operations personnel as needed. Reconciles accrued expense and advance payment balance-sheet accounts for assigned business units to ensure financial continuity per unit
                                
#     Financial Analyst at Clearwater:
#     Updated all renovation-project spreadsheets to new commitments and monitored expenditures for budget compliance. Analyzed and reported variances on overtime expenditures by comparing payroll's OT Differential Report versus approved OT requests, resulting in 33% cost savings. Provided ongoing education and management consulting to ensure that all 77 stakeholders properly understood reports, methodologies, systems and source data.
#     ''')
    
#     submitted = st.form_submit_button(label="SUBMIT AND GENERATE")

# # PROMPTS TO FEED TO LLM
# prompt_prime1 = "I am re-writing my resume and I need your help. You are going to act as a professional resume writer skilled in presenting information concisely and using niche-appropriate language, while avoiding redundancy and cliché terms. Your task is to position my experience as a solution to my target company's pain points, tailoring it specifically so that it's clear that I can manage the primary requirements of the job. I want you to memorize these instructions for the duration of our session. Is that understood? No need to respond."

# prompt_prime2 = f'''First, I am going to provide you with the job description for the role I want to apply for. Can you read it carefully so that when I ask you questions about it later, you will reference the job description and provide me with accurate answers? No need to respond.

# {jobdescription}'''

# prompt_prime3 = "Now I am going to provide you with more information on the hiring company, so you can tailor my work experience more effectively to the hiring company's needs. I want you to memorize this information so that you consider it when helping me rewrite my work experience later. Is that understood? No need to respond."

# prompt_prime4 = f'''Here are some details about the hiring company where you do not need to respond. The company's name is {company_name}.
# Here is more information about the company: {about_us}.
# Additional information about the company: {additional_information}'''

# prompt_prime5 = f'''
# I am about to give you my resume which contains detailed information about my past work experiences. I want you to rewrite each paragraph I give you as a single resume bullet point, and tailor it specifically for the {job_title} job I sent to you previously. By “tailor”, I mean explain each bullet point using similar language to what's written in the job description. Is that understood? No need to respond.
# '''

# prompt_prime6 = f'''
# Rewrite this as a resume bullet point that includes 3 - 5 results-driven achievement statements. Start each bullet with an action verb, followed by the task, and conclude with the result. Please quantify each statement using numbers, percentages, and dollar amounts. Repeat this for all my work experiences provided and keep it in memory without responding:

# {workexperience} 
# '''

# prompt_prime7 = f"Based on the {job_title} job description I sent to you earlier, what are the most important technical skills required for the job? Which technical skills would give me an advantage in this role? Keep the response in memory and no need to respond."

# prompt_prime8 = f"What are the most common areas of expertise for a {job_title}? Keep it in memory, no need to respond."

# prompt_prime9 = f"Using what you created for me with my work experience, write 5-7 sentences to summarize my professional experience, including only what's relevant to the {job_title} job description I sent you earlier. Highlight my {highlight_years} number of years of experience in the [INSERT YOUR INDUSTRY] field. Showcase how my experience and expertise can address {company_name}'s pain points. Write it using resume language (passive third person). Keep this in memory and no need to respond."

# prompt_prime10 = f"Could you please draft a one page resume based on all the information you have now?"

# if submitted:
#     client=OpenAI(api_key=st.secrets(['OPENAPI_KEY']))

#     response = client.chat.completions.create(
#         model="gpt-4o-2024-08-06",
#         messages=[
#             {"role": "user", "content": prompt_prime1},
#             {"role": "user", "content": prompt_prime2},
#             {"role": "user", "content": prompt_prime3},
#             {"role": "user", "content": prompt_prime4},
#             {"role": "user", "content": prompt_prime5},
#             {"role": "user", "content": prompt_prime6},
#             {"role": "user", "content": prompt_prime7},
#             {"role": "user", "content": prompt_prime8},
#             {"role": "user", "content": prompt_prime9},
#             {"role": "user", "content": prompt_prime10}
#         ]
#     )

#     st.write(response.choices[0].message.content)
#     print(response.usage)