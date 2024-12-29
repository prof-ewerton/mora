# python -m venv myvenv
# myvenv\Scripts\activate
# python -m pip install --upgrade pip
# pip install crewai crewai-tools
# pip install langchain_google_genai
# pip install pypdf
# pip install owlready2


from crewai.tools import tool
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM, Agent, Task, Crew, Process
from pypdf import PdfReader
from owlready2 import *

from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


content = """
Gamiﬁcation and Learning Analytics
to Improve Engagement in University Courses
Fabio Cassano (&), Antonio Piccinno, Teresa Roselli,
and Veronica Rossano
Department of Computer Science, University of Bari, Bari, Italy
{fabio.cassano1,antonio.piccinno,teresa.roselli,
veronica.rossano}@uniba.it
Abstract. Gamiﬁcation is one of the most used techniques to improve active
participation and engagement in different kinds of contexts. The use of game
techniques is effective in pushing subjects to be involved in an activity. Since
the early childhood, indeed, the promises of rewards are useful to affect speciﬁc
behaviors. On the other hands, the learning analytics have been largely imple-
mented in education in order to improve the assessment and the self-assessment
of students, above all in e-learning settings. The research presented in this work
aims at combining gami ﬁcation techniques and learning analytics to improve the
engagement in University courses. The paper describes a model of gami ﬁcation
and a learning dashboard de ﬁned based on data in Moodle e-learning platform.
A pilot test of an app android in which both the solutions have been imple-
mented pointed out promising results.
Keywords: Gamiﬁcation /C1Learning analytics /C1E-learning engagement
Learning dashboard
1 Introduction
Mobile devices (such as smartphones and tablets) allow people to be connected and
communicate all over the world. Thanks to the increasing Internet communication
speed and the more powerful mobile Central Processing Unit (CPU), mobile devices
can be used for a wide variety of tasks. According to the age of the user, the device is
prevalently used: to play mobile games, to use email or messaging, to play videos etc.
For the university students, the mobile phone is a critical device. As a matter of facts, it
is used by boys and girls attending the university, not only to check the exam dates and
share notes, but also to message information about lessons.
E-learning is a modern way to allow university students to attend lessons virtually,
using the Internet connection. It is common for many universities to offer online
courses, the MOOCs (Massive Open Online Courses) phenomenon is a proof of this
trend [1, 2]. Many online platforms, such as, Coursera, EdX, Iversity deliver online
contents to all students who have either a Personal Computer (PC) or a mobile device.
This strategy has been so successful, that the main universities all over the world, both
public and private, publish on those platforms their courses.
© Springer Nature Switzerland AG 2019
T. Di Mascio et al. (Eds.): MIS4TEL 2018, AISC 804, pp. 156 -163, 2019.
https://doi.org/10.1007/978-3-319-98872-6_19The MOOCs have been a big revolution in Education, since the university courses
can be attended by all people that need to acquire speci ﬁc knowledge or competences
without to necessary being physical in the site where the lesson is given. This means
that even non-university students can access to high education without physical limi-
tations. Moreover, these courses (and universities) release attending certi ﬁcates, once
the course has been completed, and quali ﬁcation certi ﬁcates if the student successfully
passes the related exam. These certi ﬁcations can be used to improve the curriculum
vitae and then the personal job. Unfortunately, one of the main problems in using
MOOCs and all kind of online courses is the engagement and motivation [3]. The
ﬂexibility and the freedom to attend the e-learning courses often translate into a high
dropout rate [ 4]. Many problems can distract the student from the aim and, after a
failure, the motivation without the teacher support dramatically drops [ 5]. This stu-
dents'failure is a problem also for the educational system [ 6]. In this context, in order
to mitigate this problem of online courses and activities, we propose to apply the
gamiﬁcation approach to improve the student 's active participation and engagement in
online university course. In order to measure the impact of gami ﬁcation, a mobile
application was developed to let the student be more engaged in attending online
activities in her/his university course and, in general, in the university life.
This paper is organized as follows: in the following section some related works are
reported; Sect. 3 describes the adopted gami ﬁcation approach for monitoring engage-
ment and Sect. 4 how it is implemented in a mobile application; in Sect. 5 some
preliminary results of the user testing is reported, and Sect. 6 concludes the paper.
2 Related Works
E-learning systems are widely used in both the university and the work domain. This
form of instruction has grown up during the last twenty years thanks to the greater
Internet speed and the powerful devices that can play videos. There are many guide-
lines on how the e-learning systems should be designed [ 7]. Those fall into the HCI
ﬁeld, where the users need to be considered during all the stages of the development
process. For example, more and more solutions use the same framework to deliver
different contents [8]. The study of how people really learn from this new way to teach
is constantly monitored by the companies that deliver e-learning contents [ 9]. The e-
learning is thus a recent and evolving topic. More and more techniques are used in
order to engage people and let them be more proﬁcient in following courses and learn.
One of them is the so called “Gamiﬁcation”.
Gamiﬁcation is de ﬁned as “the use of game design elements in non-game contexts ”
[10]. The term “gamiﬁcation” is sometimes controversial, but the de ﬁnition given
above and the survey provided in [ 10] clarify that “gamiﬁed” applications are different
from (video) games, serious games or just software applications that provide a playful
interaction, like those considered in [11].
Gamiﬁcation has been proved that improve participation and engagement in e-
learning activities [ 12, 13], in fact, suggests that gami ﬁcation strategies, aligned with
instructional objectives and user context, are effective in improving student participa-
tion and encouraging extracurricular learning. Moreover, game elements such as points,
Gamiﬁcation and Learning Analytics to Improve Engagement 157badges, and leaderboards, are useful strategy in Massive Open Online Courses as [ 14-
16]. On the other hands, once that the online environment stimulates student motivation
and engagement, it is necessary to measure it. In e-learning settings, characterized by
the distance both in terms of time and places, it is necessary to monitor and track the
student activities in online environments. The Learning Analytics (LAs), i.e. the
measurement, collection, analysis and reporting of data about learners and their con-
texts [17] are very useful to meet this objective. There are some research works that
investigate on the relationships among the LAs and engagement [ 18, 19]. The main
novelty of the proposal described in this paper is to combine the use of game elements
in order to foster student engagement in online activities in academic contexts and the
LAs in order to measure and visualize the level of engagement for each single student.
3 The Gami ﬁcation Approach for Monitoring Engagement
In e-learning platforms, keeping track of the user 's learning activities is very important
to make effective and reliable assessment. To improve the quality of assessment in
online courses, even with a large population (as happens in MOOCs), in literature
different solutions have been implemented [20-22]. An interesting solution is the use of
a Learning Dashboards (LD) in the e-learning environments to visualize student 's
engagement in e-learning paths. Usually, LDs allow to visualize the Learning Ana-
lytics. The LAs can be automatically or manually collected by the system. In this
research, LAs and LDs have been used in order to keep high student's engagement and
motivation. To address this challenge, VeeU2.0, a learning dashboard for Moodle, has
been designed and developed to support assessment by both teachers and learners in e-
learning courses [3, 21]. The de ﬁned model has been conceived to monitor the
engagement in an e-learning course through measures of the student 's participation, in
terms of user 's actions in wikis and social posts. Following the game mechanics,
eXperience Points (XP) were de ﬁned. In order to classify the kind of activities per-
formed in the e-learning platform, the XP were subdivided in Degree Course XP
(DC) and Single Course XP (SC). The student can gain DC performing general
activities (Table1) in the e-learning platform and in all online courses published for
her/his degree course. The SC points are gained performing general activities in any
speciﬁc course that student is attending (Table 1). In other words, if the student
accesses (Activity A1) to the e-learning platforms to browse all the online courses of
her/his degree course s/he gain 10 DC points. If the student creates a wiki page in the
“Programming course ” s/he gains 5 SC points.
When the user reaches a certain amount of XP, it gains a new level. Every new
level (for a maximum of 100 levels) allow the student to gain a higher reputation in
both virtual and real class. In order to make visible this reputation, badges can be
collected according to both the points gained and the levels reached. There are three
type of badges Gold, Silver and Bronze and they can be achieved both for the degree
course or for a speciﬁc course. Moreover, the badges can be achieved for each kind of
activities performed by the student, thus a student can have a Gold badge for the DC
access points (Activity A1) but any badge for SC creating wiki pages (A6) this means
158 F. Cassano et al.that the student mainly surfs in the e-learning platforms only to download the learning
resources or to read news, but s/he is not an active participant to online activities.
4 A Mobile App for VeeU2.0
VeeU2.0 is a learning dashboard developed as plugin for Moodle, the e-learning
platform in use in our University. The main goal of VeeU2.0 is to make students and
teachers aware of their engagement in e-learning environment. As a matter of fact,
teachers and students need to be aware of what kinds of interactions are occurring in
the virtual space and how the building up knowledge process happens. The dashboard
offers two points of views, one addressed to the teacher, who can visualise the trend of
the entire class or of a speciﬁc student, and one addressed to the student, who can
visualise her/his rate of participation in each activity and can compare her/his data with
those of the other students. From the teachers' points of view, the information visu-
alised are useful in order to monitor the level of students 'participation and interest in
the subject. This information can lead the teacher to change the teaching strategies in
order to improve the teaching effectiveness. From the student point of view, the
visualised data can help the student 's self-assessment that could be pushed to improve
her/his efforts in the learning process.
In order to improve the ef ﬁcacy of VeeU2.0, a mobile app has been developed and
the gami ﬁcation model was applied. The mobile version (the language is Italian)
reported here, as well as the web app, offers two points of view. One addressed to the
teacher, who can view how many accesses students have done for each course
(Fig.1a), which resources have been downloaded, how many quizzes have been
completed and so on. Moreover, the teacher could visualize information about each
single student in order to verify how her/his learning process is going on. For each
course, the number of access of the student is represented using a histogram together
with a line indicating the mean of accesses of the class in the same period (see Fig.1b).
Gamiﬁcation techniques has been implemented in the app for the student point of
view (Fig. 2). Once the user has selected the degree course, the app shows his/her
progress (Fig. 2a): on the top of the screen the course name is shown and below the
level reached and the overall XP gained are given ( “Livello 3 ” and “99/600” respec-
tively in the ﬁgure). For each course the student can visualise the list of the resources
Table 1. The XP points gained by the user according to the action performed
Activity type XP gained
(A1) Access 10
(A2) Read a wiki page 2
(A3) Put a“like” to a post 2
(A4) Publish a post on the dashboard 2
(A5) Comment a post on the dashboard 3
(A6) Create a wiki page 5
(A7) Edit a wiki page 5
Gamiﬁcation and Learning Analytics to Improve Engagement 159available in the course and the mean of the students that have visualised each resource
(Fig. 2b). The green colour is used for the visualised resources, the red for non-
visualised ones.
In the badge section, the user can see how many (and which type) of badges s/he
has achieved (Fig. 2c). Every time a new badge has reached, a popup message is shown
with details of the badge and how it is possible to increase the number (the value can be
shown by clicking on it). Finally, the leader board of the users shows all the users, for
the selected university course, with the relative amount of XP gained and the level
(Fig.2d).
(a) (b)
Fig. 1. The mobile app from the teacher 's point of view showing students 'accesses (a) for all
courses and (b) for a speci ﬁc course
(a) (b) (c) (d)
Fig. 2. The mobile app from the students 'point of view showing (a) progresses, (b) available
resources, (c) badges achieved and (d) the leader board
160 F. Cassano et al.5 User Testing
In order to evaluate the usability of the application, we performed a user testing with
real end users. The user testing aims at analysing the user behaviour during the
interaction with the system. To this aim, we deﬁned a list of 9 tasks that users have had
to accomplish. The “Thinking aloud ” technique was used in order to better understand
the interaction problems. For lack of space, we cannot report further details on the user
test performed. The sample was composed of 15 students attending one of the Com-
puter Science degree courses at the University of Bari. All students use regularly the
LMS to access the content of the different courses.
Each student used the system alone. A facilitator gave the instructions to the student
and an observer annotated all the signi ﬁcant information about student 's behavior.
During the test the success rate was used as objective measure. The success rate has
been calculated as follows: Success rate = (S + (P * 0,5))/N . Where: S is the number of
tasks successfully completed; P is the number of tasks partially completed; N is the sum
of all tasks. The results of the test are shown in Table 2.
The success rate of 95% could be considered a positive indication about the
usability of the system. Moreover, in order to have a qualitative evaluation of the
system, the students were asked to answer to a 5-Likert scale questionnaire about the
perceived usefulness of the app during the learning process.
Analysing the results, the system has reached a good level of acceptance. The 85%
of the students have appreciated the use of the system and hope that it would be used in
the future. Moreover, the student's appreciation is visible also in the Fig. 3.
Table 2. Results from the user tests with 15 users and 9 tasks (S: success, P: partial, F: failure)
Task1 Task2 Task3 Task4 Task5 Task6 Task7 Task8 Task9
S 1 SSSSSSSSS
S 2 SPSSSSSPS
S 3 SSSSSSSSS
S 4 SSSPFSSSS
S 5 SSSSSSSSS
S 6 SSSSSSSPS
S 7 SPSSSSSSS
S 8 SSSSSSSSS
S 9 SSSSSSSSS
S 1 0 SSSSPSSSS
S 1 1 SSSSSSSSS
S 1 2 SSSSSSSSS
S 1 3 SSSSSSSSS
S 1 4 SSSSPSSSS
S 1 5 SPSSSSSPS
Gamiﬁcation and Learning Analytics to Improve Engagement 161In particular, to the questions about motivation 10 students out 15 give an evalu-
ation between 3 and 4. For what concerning the engagement in e-learning activities, 5
students out 15 give an evaluation higher than 3 (neutral value). The user testing has
revealed also a number of weakness that should be addressed in the next future, but the
results are promising, and this can lead the research to further developments.
6 Conclusions
In this paper we have proposed a mobile application, based on the VeeU2.0 Learning
Dashboard, that allow university student and teachers to be aware about their
engagement, using the gamiﬁcation technique. The students, using the app and inter-
acting with the system, gain XP points that are used to rise their own level. The
application presents for each DC and SC, a leader board about the most proactive
students. The teacher can evaluate the ongoing student's engagement through a speci ﬁc
view.
We performed a preliminary evaluation test with 15 users to perform some tasks
and then a 5-Likert questionnaire has been administered. The preliminary results show
that the proposed app is promising with a good usability and acceptance rate.
References
1. Kennedy, J.: Characteristics of massive open online courses (MOOCs): a research review,
2009-2012. J. Interact. Online Learn. 13(1), 1 -16 (2014)
2. Liyanagunawardena, T.R., Adams, A.A., Williams, S.A.: MOOCs: a systematic study of the
published literature 2008-2012. 14(3), p. 26 (2013)
3. Pesare, E., Roselli, T., Rossano, V.: Visualizing student engagement in e-learning
environment. In: 22th International Conference on Distributed Multimedia Systems
(DMS), pp. 26-33. Knowledge Systems Institute, Skokie, IL 60076, USA (2016)
4. Chakor, Y.A., El Faddouli, N.-e: Abandonment of learners MOOC problematic analysis and
proposed solutions. Int. J. Comput. Appl. 153(2), 35 -37 (2016)
5. Bates, A.W.T.: Technology, E-learning and Distance Education. Routledge, London (2005)
Fig. 3. Results of the students 'appreciation: from 5-Likert scale questionnaires administered to
the 15 participants of the user test, where “1” means “not at all ” and 5 is “deﬁnitely”
162 F. Cassano et al.6. Bennett, R.: Determinants of undergraduate student drop out rates in a university business
studies department. J. Further High. Educ. 27(2), 123 -141 (2003)
7. Clark, R.C., Mayer, R.E. (eds.): E-learning and the Science of Instruction: Proven Guidelines
for Consumers and Designers of Multimedia Learning, 4th edn. Wiley, Hoboken, NJ, USA
(2016)
8. Garrison, D.R.: E-Learning in the 21st Century: A Framework for Research and Practice.
Psychology Press, London (2003)
9. Sun, P.-C., Tsai, R.J., Finger, G., Chen, Y.-Y., Yeh, D.: What drives a successful e-
Learning? An empirical investigation of the critical factors in ﬂuencing learner satisfaction.
Comput. Educ. 50(4), 1183 -1202 (2008)
10. Deterding, S., Dixon, D., Khaled, R., Nacke, L.: From game design elements to
gamefulness: de ﬁning “gamiﬁcation”. In: 15th International Academic MindTrek Confer-
ence: Envisioning Future Media Environments, pp. 9 -15. ACM, New York, NY, USA
(2011)
11. Salah, A.A., Schouten, B.A.M., G öbel, S., Arnrich, B.: Playful Interactions and Serious
Games. IOS Press (2014)
12. Darina, D., Christo, D., Gennady, A., Galia, A.: Gami ﬁcation in education: a systematic
mapping study. J. Educ. Technol. Soc. 18(3), 75 -88 (2015)
13. de-Marcos, L., Dom ínguez, A., Saenz-de-Navarrete, J., Pag és, C.: An empirical study
comparing gami ﬁcation and social networking on e-learning. Comput. Educ. 75,8 2 -91
(2014)
14. Klemke, R., Eradze, M., Antonaci, A.: The ﬂipped MOOC: using gami ﬁcation and learning
analytics in MOOC design — a conceptual approach. Educ. Sci. 8(1), 25 (2018)
15. Chang, J.-W., Wei, H.-Y.: Exploring engaging gami ﬁcation mechanics in massive online
open courses. J. Educ. Technol. Soc. 19(2), 177 -203 (2016)
16. Mazarakis, A.: Using gami ﬁcation for technology enhanced learning: the case of feedback
mechanisms. Bull. IEEE Tech. Comm. Learn. Technol. 17(4), 6 -9 (2015)
17. Long, P., Siemens, G.: Penetrating the fog: analytics in learning and education. EducausE
Rev. 46(5), 31 -40 (2011)
18. Phillips, R., Preston, G., Roberts, P., Cumming-Potvin, W., Herrington, J., Maor, D.,
Gosper, M.: Using academic analytic tools to investigate studying behaviours in technology-
supported learning environments (2010)
19. Pesare, E., Roselli, T., Rossano, V.: Engagement in Social Learning: Detecting Engagement
in Online Communities of Practice, pp. 151 -158. Springer International Publishing (2017)
20. Mu ñoz-Merino, P.J., Ruip érez-Valiente, J.A., Alario-Hoyos, C., P érez-Sanagustín, M.,
Delgado Kloos, C.: Precise effectiveness strategy for analyzing the effectiveness of students
with educational resources and activities in MOOCs. Comput. Hum. Behav.47, 108 -118
(2015)
21. Pesare, E., Roselli, T., Rossano, V., Di Bitonto, P.: Digitally enhanced assessment in virtual
learning environments. J. Vis. Lang. Comput. 31, 252 -259 (2015)
22. Siemens, G.: Learning analytics: envisioning a research discipline and a domain of practice.
In: 2nd International Conference on Learning Analytics and Knowledge (LAK), pp. 4 -8.
ACM, New York, NY, USA (2012)
Gamiﬁcation and Learning Analytics to Improve Engagement 163
"""
string_source = StringKnowledgeSource(
    content=content,
)


########## LLM
# llm = ChatGoogleGenerativeAI(model="gemini/gemini-pro", temperature = 0)
llm = LLM(
  api_key=os.getenv("GOOGLE_API_KEY"),
  model="gemini/gemini-pro",
  temperature = 0.0                      # 0.0 - 1.0 para o modelo gemini/gemini-pro
)




########## TOOL1
@tool("Leitor de PDF")
def read_pdf_tool(pdf: str) -> str:
  """Esta ferramenta lê um arquivo em PDF retornando seu conteúdo em modo texto."""
  reader = PdfReader(pdf)
  texto = ""
  for page in reader.pages: 
    texto += page.extract_text()
  return texto

############# TESTE TOOL1
# result = read_pdf_tool._run(**{"pdf": "paper1.pdf"})
# print(result)

############# AGENT1
agent1 = Agent(
    role="Um experiente analisador de dados",
    goal="Analisa e interpreta complexos artigos científicos extraindo conceitos relevantes sobre o tema: {topic}.",
    backstory="Com 10 anos de experiência em análise de dados e {topic}, você se destaca em encontrar os conceitos chaves de um texto.",
    llm=llm,
#    tools=[read_pdf_tool],
    verbose=True,
    max_iter=4,
    knowledge_sources=[string_source],
    embedder={
        "provider": "google",
        "config": {"model": "models/embedding-001"},
    },
)

############# TASK1
task1 = Task(
    description="Extrair vários conceitos relevantes sobre {topic} do arquivo {pdf} para análise subsequente.",
    expected_output="""
    Uma relatório contento o título do artigo analisado e uma tabela com os conceitos e um parágrafo do texto original contendo o conceito relacionado.
    Utilize o exemplo abaixo para compor o relatório.
    Exemplo:
    # Título do Artigo
    ## Tabela de Conceitos
    | Conceito | Contexto |
    |-----------|----------|
    | "Conceito achado" | "Parágrafo do texto contendo o conceito" |
    """,
    agent=agent1,
    output_file="concepts.md"
)




########## TOOL2
# LEITOR DE ONTOLOGIA OWL
@tool("Leitor de Ontologia OWL")
def read_onto_tool(onto: str) -> str:
    """Esta ferramenta lê um arquivo em OWL."""
    onto = get_ontology(onto).load()
    response = "CLASSES DA ONTOLOGIA:\n"
    for cls in onto.classes():
        response = response + cls.name + " - "
        if cls.comment:
            for descricao in cls.comment: 
                response = response + descricao + " "
        response = response + ";\n"
    return response

############# TESTE TOOL2
# result = read_onto_tool._run(**{"onto": "onto.owl"})
# print(result)


############# AGENT2
agent2 = Agent(
    role="Um experiente analista de {topic} e pesquisador de ontologia",
    goal="Consegue relacionar conceitos de uma lista entregue por outro agente com classes de uma ontologia extraídas do arquivo {onto}.",
    backstory="Um pesquisador de {topic} com experiência em pesquisa científica e conhecimento em ontologia que consegue relacionar conceitos de uma tabela com classes de uma ontologia do arquivo {onto} com bastante atenção aos detalhes.",
    llm=llm,
    tools=[read_onto_tool],
    verbose=True,
    max_iter=4,
)

############# TASK2
task2 = Task(
    description="Relacionar conceitos entregues por outro agente com as classes de uma ontologia.",
    expected_output="""
    Um relatório formatado em markdown contendo: 
    o título do artigo que foi entregue pelo outro agente, 
    uma tabela dos conceitos que forma possíveis de relacionar com as classes da ontologia e 
    outra tabela com os conceitos que não foram possíveis de estabelecer um relacionamento, quando houverem.
    """,
    agent=agent2,
    output_file="report.md"
)




crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential,  # or Process.hierarchical
    max_iter=4,
    full_output=True,
)

results = crew.kickoff(inputs={'topic': 'Learning Analytics', 'pdf': 'paper1.pdf', 'onto': 'onto.owl'})
print(results)