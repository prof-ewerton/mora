# Gamiﬁcation and Learning Analytics to Improve Engagement in University Courses

## Table of Concepts
| Concept | Context where the concept was found |
|---|---|
| Gamiﬁcation | The use of game design elements in non-game contexts |
| Learning Analytics | The measurement, collection, analysis and reporting of data about learners and their contexts |
| Experience Points (XP) | Points that students can earn by performing certain actions in an e-learning platform |
| Degree Course XP (DC) | XP that students can earn by performing general activities in an e-learning platform |
| Single Course XP (SC) | XP that students can earn by performing general activities in a specific course |
| Learning Dashboards (LD) | A tool that allows students and teachers to visualize student engagement in e-learning environments |
| Badges | A type of reward that students can earn for achieving certain goals |

**Context where the concept was found:**

Gamiﬁcation and Learning Analytics to Improve Engagement in University Courses
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
T. Di Mascio et al. (Eds.): MIS4TEL 2018, AISC 804, pp. 156 –163, 2019.
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
dents’failure is a problem also for the educational system [ 6]. In this context, in order
to mitigate this problem of online courses and activities, we propose to apply the
gamiﬁcation approach to improve the student ’s active participation and engagement in
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
Gamiﬁcation and Learning Analytics to Improve Engagement 157badges, and leaderboards, are useful strategy in Massive Open Online Courses as [ 14–
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
In e-learning platforms, keeping track of the user ’s learning activities is very important
to make effective and reliable assessment. To improve the quality of assessment in
online courses, even with a large population (as happens in MOOCs), in literature
different solutions have been implemented [20–22]. An interesting solution is the use of
a Learning Dashboards (LD) in the e-learning environments to visualize student ’s
engagement in e-learning paths. Usually, LDs allow to visualize the Learning Ana-
lytics. The LAs can be automatically or manually collected by the system. In this
research, LAs and LDs have been used in order to keep high student’s engagement and
motivation. To address this challenge, VeeU2.0, a learning dashboard for Moodle, has
been designed and developed to support assessment by both teachers and learners in e-
learning courses [3