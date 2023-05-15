from langchain import PromptTemplate


jd_extract_template = PromptTemplate(
    input_variables=["text"],
    template='''
    Start of the job description:

    {text}

    end of the job description.

    extract following information:

    position: title of the Job.
    tech_stacks: all experience of technology, tools, programming language, frameworks required for preferred in the job. remember to include all the technology tools into the tech_stacks field.
    summary_for_tech_stack: concisely summarized what the tech stack is about and focus on what the tech stack is used for
    soft_skills: soft skills required for preferred in the job
    other_properties: other relevant experience, property, or personal trait preferred in the job


    return the info above in key-value pair
    ```json
    {{
        "position": "...",
        "tech_stacks": [...],
        "summary_for_tech_stack": "...",
        "soft_skills": [...],
        "other_properties": [...]
    }}
    ```
    do not return any other information, just pure json object.
    ''',
)

jd_template = PromptTemplate(
    input_variables=["position", "tech_stacks",
                     "soft_skills", "other_properties"],
    template="""
This is a job description of {position} position. 
The following are the requirements of tech stacks experience:
{tech_stacks}
The following are the requirements of soft skills:
{soft_skills}
The following are other properties preferred:
{other_properties}

remember that the above requirement does not need to be exact match, but rather the relevant comparable experiment to for same similar purpose is also acceptable.
for example, if there is MySQL in the requirement, then PostgreSQL is also acceptable, since they are both relational database.
if there are Java in the requirement, then Kotlin or C++ are also acceptable. since they are all object oriented programming language.
if requires experience of building a mobile app, then web app is also acceptable.
""",
)

test_jd_extract_input = {
    "text": """About the job
Are you a driven problem solver looking to help our clients tackle some of the most pressing challenges within Government and Public Services (GPS). Join Deloitte's Program Integrity practice to help government agencies protect taxpayer money. To address the threats that perpetuate fraud, waste, and abuse, our clients look to our team to provide the guidance and solutions required to help them stay ahead of emerging issues and protect the integrity of their programs. If you are looking for a rapidly growing, collaborative environment with opportunities to make an impact and grow, our Program Integrity team would be a great fit for you!

Work you'll do

Our team detects situations of fraud, waste, and abuse through reviewing claims. the ML Ops Engineer will be responsible for learning and implementing new infrastructure.

The team

Deloitte's Government and Public Services (GPS) practice - our people, ideas, technology and outcomes-is designed for impact. Serving federal, state, & local government clients as well as public higher education institutions, our team of over 15,000+ professionals brings fresh perspective to help clients anticipate disruption, reimagine the possible, and fulfill their mission promise.

We bring a rigorous approach to help government agencies effectively detect, prevent, and respond to issues related to fraud, waste, and abuse. Our team helps tackle these threats by bringing cutting edge analytics and AI experience with innovative mindsets. Our Program Integrity team focuses on thought diversity and collaborative problem solving to help clients address these challenges holistically, with a common goal to protect the integrity of their programs.

Qualifications

Required:
Bachelor's Degree in Economics, Finance, Statistics, Mathematics, Computer Science, Management Information Systems, Engineering, Business Analytics disciplines, or related area
4-6 Years minimum / no location constraint
2+ years of experience working in a Data Science/Machine Learning Engineering role.
Proficient in Python, Spark (Pyspark), and SQL
Experience deploying and configuring applications in Kubernetes
Experience automating cloud resource deployment in Terraform. Comfortable operating in a Linux environment.
Experience developing production applications with Big Data, with tools like Spark, Hive, and Hadoop.
Experience building model training pipelines in the cloud.
Experience deploying ML services and applications to at least one major cloud platform (AWS, Azure, GCP, IBM Cloud)
Proficient in software design patterns (e.g. understand object-oriented vs functional programming principals, inheritance, writing abstract, reusable, and modular code)
Experience building and deploying microservices as part of Machine Learning/Data Science applications.
Experience with building continuous integration and delivery pipelines for Machine Learning applications.
Preferred:
Experience with at least one deep learning framework (e.g., TensorFlow, PyTorch, Caffe, MxNET)
Experience developing with AWS managed services such as EMR.
Experience orchestrating the deployment and management of predictive models in a cloud environment.
Experience working in an AGILE development team.
The wage range for this role takes into account the wide range of factors that are considered in making compensation decisions including but not limited to skill sets; experience and training; licensure and certifications; and other business and organizational needs. The disclosed range estimate has not been adjusted for the applicable geographic differential associated with the location at which the position may be filled. At Deloitte, it is not typical for an individual to be hired at or near the top of the range for their role and compensation decisions are dependent on the facts and circumstances of each case. A reasonable estimate of the current range is $66,049-$143,556.

You may also be eligible to participate in a discretionary annual incentive program, subject to the rules governing the program, whereby an award, if any, depends on various factors, including, without limitation, individual and organizational performance.
"""
}

final_prompt_test_jd_extraction = jd_extract_template.format(
    **test_jd_extract_input)
# print(final_prompt_test_jd_extraction)
