---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\UCCI-especializaciónProy Investigación\MODULO 7.PORAT\PORAT-18-01-23\Bayesian- ingles.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

International Journal of Wireless Information Networks (2019) 26:174–182 https://doi.org/10.1007/s10776-019-00436-9 



# **Effective Application of Naive Bayesian Classifier for Personal Online Learning Networks** 

### **Deyan Wang**<sup>**1,2**</sup> **· Amritl Jaharadak Adam**<sup>**1**</sup> **· Ying Xiao**<sup>**2**</sup> **· Ya Gao**<sup>**2**</sup> 

Received: 27 March 2019 / Revised: 11 June 2019 / Accepted: 14 June 2019 / Published online: 2 July 2019 © Springer Science+Business Media, LLC, part of Springer Nature 2019 

### **Abstract** 

Naive Bayesian classifier can be used to classify news and patients, but there are few studies on the classification of educational data. Based on Naïve Bayesian algorithm. This paper studies the relationship between course achievement and employment salary. Quantitative method is adopted as research methodology. The sample data sets were collected from Personal Online Learning Networks, which consist of the Student Performance Management System and Student Employment Management System. The sample category labels were constructed and the Hold-Out method was used to divide data sets into training sets and testing sets. 15 courses’ performance as feature vector and employment wage as category, if the attribute condition was independent, a Naïve Bayesian Classifier was established. The result indicating the higher the grade of DAWEB, ICT, INT and WNDW courses, the higher the employment wage. The conclusion is in accordance with the actual situation: Four courses mainly train students’ comprehensive practical ability. The students who have stronger practical abilities are highly demanded by employers, hence, the higher salary will be provided. At the end, regarding the class conditional probability of _P_ ( _xi_ = _E_ | _s_ = _H_ ) (Performance = E, salary = H) as the weight of courses, build a topological structure diagram of courses. 

**Keywords** Naïve Bayesian · Classifier · Online learning networks · Personal course achievement · Employment salary · Topological structure diagram 

## **1 Introduction** 

Currently, Data Mining (DM) technology and Machine Learning (ML) algorithm has played a prominent role in the field of industry, medicine, environment, biology, aerography etc. Based on wide application of DM technology, with the rapid development of Advanced Scout (AS) software, the coaching staff of National Basketball Association (NBA) are trying to find out interesting patterns in game data. By gathering all the valid information at hand, it enables a coach to assess the effectiveness of making certain coaching decisions and formulate game strategies for subsequent games [1]. 

> * Deyan Wang 

> hju7y8@aliyun.com 

> 1 Management & Science University, Shah Alam, Malaysia 

> 2 

> Wuxi Institute of Technology, School of Internet of Things Technology, Wuxi, Jiangsu, China 

Through collecting incident date and location, such attributes or crime parameters like crime type, criminal ID and the acquaintances, can propose solutions to prediction of criminal problems using Naïve Bayesian theory [2]. The use of low-cost wireless sensor networks is to collect forest data and apply Bayesian theory to monitoring forest cover and physical environment [3]. Bayesian compressive sensing (BCS) has played an increasingly important role in signal processing for dealing with the related problems of sparse representation. BCS generated a Bayesian model to solve the problems of compressing sensing (CS), such as signal sampling processing and model parameters, by adopting a framework of the hierarchical Bayesian. The use of Gaussian and Laplace distribution priors on the basic coefficients has already been demonstrated in previous works [4]. The Bayesian classification is proposed to predict falls risk with vectors of gait variables shown to contribute to falls risk [5]. To improve the life quality of patients suffering from Alzheimer’s disease (AD), the neuropsychological data of 466 volunteers were analyzed by Naive Bayesian method. There 

Vol:.(1234567890)1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

175 

appeared early symptoms and affairs in need of special care. In turn, good suggestions were most likely to be given [6]. 

Nowadays, educational data is gradually attracting more attention from the worldwide. The developing field is promoted as Educational Data Mining (EDM). It refers to developing methods to remove information from the educational circumstances. The application of ML algorithm to education data analysis has become a popular phenomenon [7–12]. 

The United States has global science and technology power. Officially the country launched a ‘Big Data Research and Development Initiative’ on March 29, 2012 [13]. Through collecting and processing large and complex data information, the program may contribute to obtaining wider knowledge and insight, enhancing the abilities, speeding up scientific and engineering development, strengthening the system of homeland security, transforming educational and learning model, and officially motivating the “Big Data” into national strategic level. The government announced to have invested $200 million. In the area of education, the National Science Foundation of the United States also announced additional investment of $10 million in stimulating the development of large data research in area of social and human sciences. As for educational field, various of universities with noticeable reputation, like Yale University, Harvard University, Stanford University and others, have also carried out some relevant research programs for big data; In addition, some organizations, composed of The American School Administrators Association (ASAA), the Consortium for School Networking (COSN) and a global information technology research and consulting firm called ‘Garter, implemented a cooperative project entitled ‘closing the gap: turning data into action’. The project was designed to promote school use of large data in Student Information Systems (SIS) and Learning Management Systems (LMS). 

The Bayesian classifier is used to analyze students’ emotions and activities published on social media such as Twitter, Facebook etc. The focus is on evaluating whether students’ burden of studies is too heavy, whether their negative emotions are too serious, and whether they lack social activities [14]. According to students’ academic performance record, stored in Enrollment Management System (EMS), there shows an indication of two synthetic attributes: the inherent difficulty and the competence measure, concerned with student performance in a given course and the grades obtained in related courses. The term of “Student Performance Recommender System”(SPRS) is presented to tailor the advice and support for students [15]. Here presents a user-friendly decision supportive software. The purpose is to accurately predict student performance in the final examination of the academic year, based on a predictor of grades [16]. After selecting 5 academic courses, each of them constitutes an individual data set and can apply ML techniques to timely predict postgraduates’ performance tendency [17]. 

Most of colleges may rely on various Database Management Systems (DMS). The DMS generates huge information data every day. It remains to be discussed on the topic of how to apply data mining technology to make effective use of these information data in the School Management System (SMS). Through the analysis in graduates’ performance and employment salary, curriculum weight should be set to enhance the relationship. Therefore, students could get clearer understanding of course goals in future, stimulate more interest in diverse learning and benefit from that. 

The rest of this paper is organized as follows. Section 2 presents how to construct the data sets and optimize them. Based on the Bayesian decision theory and Naïve Bayesian, Sect. 3 develops the methods of smoothing and continuous attributes processing and model evaluation method. How to apply Naïve Bayesian is indicated in Sect. 4. Section 5 performs simulations evaluation, followed by the conclusion in Sect. 6. 

## **2  Data** 

The acquisition of data sets utilized in this study are collected from University Management System (UMS), as common as many other prestigious universities. In general, UMS have certain subsystems that students are usually familiar with, such as Student Information Management System (SIMS), Student Performance Management System (SPMS) and Student Employment Management System (SEMS) etc. 

The scores of each volunteer are truly recorded in the SPMS. In this way, 357 students in majors of network technology and 15 courses score were selected as target group. There contains detailed information in SEMS on the employment information of graduates, including employment units, employment salaries etc. The focus attribute is salary. Joint of SPMS and SEMS build a sample data set. Each instance has 15 attributes and a label, 15 courses as 15 attributes, the score as attribute value and the salary as the label. Thus, sample data structure goes in Table 1. 

Sample data set values in Table 2. 

Usually, there are two kinds of ways to record scores. One is continuous value, such as a percentage score of ‘95’ and the other one is discrete value, such as a grade score of ‘Excellent’. In the paper, the rule of correspondence is as shown in Table 3. 

## **3  Method** 

Bayesian decision Theory [18] is the basic method of carrying out decisions under the frame of probability. For the classification task, the Bayesian decision theory states how to select the best category markers based on the probability 

1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

176 

#### **Table 1** Sample data structure 

|Attribute|Course|Attribute|
|---|---|---|
|sequence<br>number|||
|1|C++ Programming I|CI|
|2|C++ Programming II|CII|
|3|Design and Application of WEB Database|DAWEB|
|4|Fundamentals of Computer Application|FCA|
|5|Network Basics|NB|
|6|Network Security Technology|NST|
|7|Network Switching and Routing|NSR|
|8|Application Mathematics I|AMI|
|9|Application Mathematics II|AMII|
|10|Basic English I|BE I|
|11|Basic English II|BEII|
|12|Integrated Communication Training|ICT|
|13|Network Engineering Project Training|NEPT|
|14|Integrated Network Training|INT|
|15|Wireless Network Deployment Week|WNDW|



Category label is salary (S) 

the category marker which can minimize the conditional risk _R_ ( _c_ | _x_ ) on every sample. The representation is given in Eq. (3): 



Here, _h_ ∗ is called Bayesian optimal classifier, the corresponding overall risk _R_ ( _h_ ∗) is called Bayesian risk. 1 − _R_ ( _h_ ∗) reflects the best performance that the classifier can achieve, that is, the theoretical upper limit of model accuracy that can be generated by machine learning. 

Specifically, if the goal is to minimize the classification error rate, the miscarriage loss _휆ij_ can be written as Eq. (4): 



The conditional risk is given in Eq. (5): 

_R_ ( _c_ | _x_ ) = 1 − _P_ ( _c_ | _x_ ) (5) Thus, the Bayesian optimal classifier of minimizing classification errors is given in Eq. (6): 



and the misjudgment loss in the ideal case where all the related probabilities are known [19]. 

Assuming that there is a possible category tag in _N_ , as _y_ =<sup>{</sup> _c_ 1, _c_ 2, … _cN_ } , _휆ij_ is a loss caused by the misclassification of a sample with the true mark _cj_ as _ci_ . Based on the posteriori probability _P_ ( _ci_ | _x_ ), the expected loss caused by classifying the sample _x_ into _ci_ can be obtained. The same with conditional risk that is based on _x_ , the representation is given by Eq. (1): 



The task now is to find a criterion _h_ ∶ _휒_ ↦ _y_ to minimize the overall risk, the representation is given in Eq. (2): 



For each sample _R_ ( _ci_ � _x_ ) =<sup>∑</sup><sup>_N_</sup> _j_ =1<sup>_휆ijP_(</sup><sup>_cj_�</sup><sup>_x_)</sup><sup>_x_, if the condi-</sup> tional risk as _R_ ( _h_ ( _x_ )| _x_ ) can be minimized, the overall risk will also be minimized. This will produce the Bayesian Decision Rule: to minimize the overall risk, simply select 

For every sample _x_ , select the category mark that can maximize the posteriori probability _P_ ( _c_ | _x_ ). 

It is not difficult to see that in order to minimize the risk of decision by using Bayesian decision criteria, a posteriori probability _P_ ( _c_ | _x_ ) must be obtained first. However, in real life tasks, this is often difficult to obtain directly. From this point of view, machine learning is based on a limited set of training samples to estimate the posterior probability 

**Table 3** Rule of correspondence with percentage grading system and grade system 

|Percentage grading system|Grade system|Value|
|---|---|---|
|90–100|Excellent|E|
|80–89|Good|G|
|70–79|Middle|M|
|60–69|Pass|P|
|0–59|Failure|F|



Category label S value like: High—H, Middle—M, Low—L 

**Table 2** Sample data set values (partial) 

|CI|C II|DAWEB|NB|FCA|…|S|
|---|---|---|---|---|---|---|
|92|Excellent|95|Excellent|Good|…|High|
|76|Good|94|Good|Good|…|High|
|72|Pass|70|Middle|Middle|…|Middle|
|65|Pass|78|Good|Middle|…|Middle|
|67|Pass|96|Middle|Middle|…|High|



1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

177 

_P_ ( _c_ | _x_ ) as accurately as possible. In general, there are two main strategies: Given _x_ , _c_ can be predicted by modeling _P_ ( _c_ | _x_ ) directly, so can get a discrimination model; Also can model the joint probability distribution _P_ ( _x_ , _c_ ) , and then get _P_ ( _c_ | _x_ ), which is the “generating model”. For the generation model, must consider in Eq. (7): 



Based on Bayesian theorem, _P_ ( _c_ | _x_ ) can be written as Eq. (8): 



_P_ ( _c_ ) is the class prior probability; Y is class conditional probability of sample _x_ relative to class marker _c_ , also can be called likelihood. _P_ ( _x_ ) is “evidence” for normalization. For sample _x_ , Evidence factor _P_ ( _x_ ) is independent of class markers. So, the problem of estimating _P_ ( _c_ | _x_ ) is converted to how to estimate prior _P_ ( _c_ ) and likelihood [20] _P_ ( _x_ | _c_ ) based on training data _D_ . Therefore, the class priori probability _P_ ( _c_ ) expresses the proportion of the samples in the sample space. According to the large number rate, the _P_ ( _c_ ) can be estimated by the frequency of the various samples when the training set contains enough independent and identically distributed samples. 

For class conditional probability _P_ ( _x_ | _c_ ) , because it involves the joint probability for all attributes of _x_ , it will be difficult to estimate directly from the frequency of sample occurrence. For example, assuming that the _d_ attributes of the sample are all binary, the sample will have 2<sup>_d_</sup> possible values, In practical applications, this value is often much larger than the number of training samples _m_ . In other words, a lot of sample values don’t appear in the training set at all and use frequency directly to estimate _P_ ( _x_ | _c_ ) is obviously can’t work as “Not observed” is usually different from “Zero probability of occurrence.” [21]. 

It is simple to find that the difficulty of estimating a posterior probability _P_ ( _c_ | _x_ ) based on Bayesian formula is that the class conditional probability _P_ ( _x_ | _c_ ) is the joint probability of all attributes, so it is difficult to estimate the probability from a limited training sample. The Naïve Bayesian classifier adopts the assumption that “attribute condition is independent”, hypothesis based on attribute condition independence, Eq. (8) can be rewritten as Eq. (9) [22]: 



here _d_ is the number of attribute, _xi_ is the value of _x_ on the _i_ attribute. 

Because _p_ ( _x_ ) is the same for all categories, Bayesian criterion that based on Eq. (6) can be rewritten as Eq. (10): 



This is expression of naïve Bayesian classifier. 

Obviously, the training process of Naïve Bayesian classifier is to estimate the class prior probability _P_ ( _c_ ) based on the training set _D_ and estimate the conditional probability _P_ ( _xi_ | _c_ ) for each attribute. 

_Dc_ Represent the set of samples of class _c_ in training set _D_ , if there are sufficient independent and distribute samples, the class prior probability can be easily evaluated in Eq. (11) 





Continuous attribute could not be directly classified. However, Probability Density Function could be considered. Assume the formulate _P_ ( _xi_ | _c_ ) ∼ _N_ ( _휇c_ , _i_ , _휎c_<sup>2</sup> , _i_<sup>) is valid,</sup><sup>_휇c_,</sup><sup>_i_is</sup> the mean of the sample of class _c_ on the _i_ attribute, _휎c_<sup>2</sup> , _i_<sup>is</sup> the variance of the sample of class _c_ on the _i_ attribute, the conditional probability _P_ ( _xi_ | _c_ ) can be evaluated in Eq. (13) 



To prevent erasing other attributes’ information that has never appeared in the training set, smoothing method is always used during evaluation of the probability value, Laplacian [23] correction is the most general. N represents the number of possible classes in the training set D, N _i_ represents the number of possible values for the _i_ attribute, the Eqs. (11) and (12) can be revised in Eqs. (14) and (15) 





ML is to “train” or “study” to a model by a suitable algorithm using a part of existing data. The part of existing 

1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

178 

data used to train is always called training set and the rest part is called testing set. Testing set is always used to test the model’s ability to distinguish new samples, then approximately consider test errors as generalization error. Training set and testing set are both divided from sample. The generation rules of training set and testing set will greatly affect the generalization error of classifier. 

Hold-Out [24] is the method that divides data set Dinto two mutually exclusive sets, one group as training set _S_ and another is testing set T. D = _S_ ∪ _T_ , _S_ ∩ _T_ = � . Besides, _S_ is used to train a model and T is used to evaluate the test error as the generalization error. The division of training set and test set should keep the consistency of data distribution as much as possible, avoiding the introduction of additional deviation due to data partitioning process and an impact on the final result. The traditional approach is to use 2/3 or 4/5 of data set as training set and the others as testing set. Then after several times of partition and repeat experiment, every time it should produce a test error, then calculate a mean value as the Hold-Out’s evaluation result. 

_k_ -fold [18, 25] cross validation is the method that divides data set D into _k_ c number mutually exclusive sets with the same size. In D = _D_ 1 ∪ _D_ 2 ∪ ⋯ ∪ _Dk_ , _Di_ ∩ _Dj_ = �( _i_ ≠ _j_ ) , every subset _Di_ keeps consistency of data distribution as far as possible. The union of _k_ − 1 subsets are used as the training set as a time and remaining subsets are as testing set. The _k_ -group training/test set can train and test _k_ times, and finally can return the average of _k_ test results. _k_ value is usually as 5/10/20. Figure 1 gives the _k_ = 10 sketch map of cross validation. 

## **4  Apply Naïve Bayesian** 

In Table 2, scores are described by percentage grading system or grade system. Percentage grading system is called continuous attribute and grade system is called discrete attribute. The continuous attribute can’t be classified, so Machine learning always applies Eq. (13) to calculate condition probability. But percentage grading system and grade system are familiar with teachers and students, so, treatment of continuous attribute doesn’t use Eq. (13), Reference Table 3, change percentage grading to grade and convert Tables 2, 3 and 4. 

From Table 4, attribute value still has some other unknown grade, for instance, the C++ Programming I have no failure score in training set. So conditional probabilities _P_ ( _x_ | _ci_ ) are: 



Apply Eqs. (14) and (15) to smooth, 



The process of predicting the correlation between Achievement and Employment salary is divided 357 data samples into 

**Fig. 1** 10-Fold cross validation representation 



**Table 4** Dataset of discrete attribute 

|CI|CII|DAWEB|NB|FCA|…|S|
|---|---|---|---|---|---|---|
|E|E|E|E|G|…|H|
|M|G|E|G|G|…|H|
|M|P|M|M|M|…|M|
|P|P|M|G|M|…|M|
|P|P|E|M|M|…|H|



1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

179 

**Table 5** Conditional probability _P_ ( _xi_ | _c_ ) (partial) 

|P|xi|||||
|---|---|---|---|---|---|
||CI|CII|DAWEB|NB|FCA|
|_P_(_xi_ =_E_|_S_=_H_)|0.285714|0.392857|0.750000|0.285714|0.071429|
|_P_(_xi_ =_G_|_S_=_H_)|0.214286|0.178571|0.107143|0.357143|0.285714|
|_P_(_xi_ =_M_|_S_=_H_)|0.142857|0.250000|0.071429|0.214286|0.428571|
|_P_(_xi_ =_P_|_S_=_H_)|0.321429|0.142587|0.035714|0.107143|0.178571|
|_P_(_xi_ =_F_|_S_=_H_)|0.035714|0.035714|0.035714|0.035714|0.035714|
|_P_(_xi_ =_E_|_S_=_M_)|0.041237|0.046392|0.195876|0.041237|0.015464|
|_P_(_xi_ =_G_|_S_=_M_)|0.170103|0.149485|0.402062|0.097938|0.123711|
|_P_(_xi_ =_M_|_S_=_M_)|0.309278|0.206186|0.247423|0.231959|0.427835|
|_P_(_xi_ =_P_|_S_=_M_)|0.474227|0.587629|0.149485|0.618557|0.422680|
|_P_(_xi_ =_F_|_S_=_M_)|0.005155|0.010309|0.005155|0.010309|0.010309|
|_P_(_xi_ =_E_|_S_=_L_)|0.023256|0.046512|0.023256|0.023256|0.023256|
|_P_(_xi_ =_G_|_S_=_L_)|0.116279|0.093023|0.302326|0.093023|0.069767|
|_P_(_xi_ =_M_|_S_=_L_)|0.395349|0.139535|0.255814|0.162791|0.325581|
|_P_(_xi_ =_P_|_S_=_L_)|0.441860|0.674419|0.372093|0.674419|0.558140|
|_P_(_xi_ =_F_|_S_=_L_)|0.023256|0.046512|0.046512|0.046512|0.023256|







**Fig. 2** 15 Courses conditional probability when _P_ ( _c_ ) = _P_ ( _S_ = _H_ ) 

training sets and test sets using the partitioning ratio of 2/3 of the “Hold-Out” method, 250 training data sets and 107 testing data sets. Approximate Generalization Errors (APGE) are obtained. The modeling process is as follows: 

Deterministic data sample → Partition training set and test set →  Establishment the prediction model → evaluation model. 

## **5  Analysis** 

Class prior probability _P_ ( _c_ ) are: _P_ ( _S_ = _H_ ) = 0.0949 , _P_ ( _S_ = _M_ ) = 0.7510 and _P_ ( _S_ = _L_ ) = 0.15415 . Partial attribute Conditional probability _P_ ( _xi_ | _c_ ) is shown in Table 5. 

The results are very interesting. Indeed, compared with Cross Validation, Hold Out has the positive result with low 

**Fig. 3** 15 Courses conditional probability when _P_ ( _c_ ) = _P_ ( _S_ = _M_ ) 



**Fig. 4** 15 Courses conditional probability when _P_ ( _c_ ) = _P_ ( _S_ = _L_ ) 

1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

180 

#### **Fig. 5** WANG Rosenthal model 



classification error rate _E_ ( _f_ ; _D_ ) , especially when the ratio is 2/3. If using 107 testing sets to validate the classifier, the _E_ ( _f_ ; _D_ ) is 0.792456. But, for furthermore analysis, only test the data sets that classifier label is S = H, the _E_ ( _f_ ; _D_ ) up to 0.925436. First, 15 courses Conditional probability _P_ ( _xi_ | _c_ ) is in Fig. 2 when class prior probability _P_ ( _c_ ) = _P_ ( _S_ = _H_ ) , then 15 courses Conditional probability _P_ ( _xi_ | _c_ ) is in Fig. 3 when class prior probability _P_ ( _c_ ) = _P_ ( _S_ = _M_ ) , and 15 courses Conditional probability _P_ ( _xi_ | _c_ ) is in Fig. 4 when class prior probability _P_ ( _c_ ) = _P_ ( _S_ = _L_ ). 

## **6  Conclusion** 

According to Fig. 2, the courses of DAWEB, ICT, INT and WNDW mentioned, have significant value. It is indicated that the teaching content belong to a segment of project actual operation. Therefore, the training program fulfills the same requirement and objective of the vocational development. For a student, if the better the content of comprehensive training they could master, the faster the entry into the technology application link they will achieve. From a perspective of a company, such talents are obviously highly demanded and valued. Naturally, the employers are willing to provide satisfactory salaries to both sides. As we see in Fig. 2, you can not get high wage if your grades are fail. 

Relatively speaking, it is pointed that, the randomness of student performance is large but with a low performance index. However, there are also more contributing factors that should be involved. On the contrary, through the analysis of students, who achieve a higher salary, the key factors may be different with a better finding of positive effect. The results of the study show that, an idea that the better you learn, the better you will get the higher salary job, is accessible and validated. The research results are in accordance with the real case in reality. Thus, the experimental results are evaluated and considered effective. As in Fig. 4, if your grades only are pass, maybe your wage is low. 

In 1968, Professor Rosenthal together with his assistant, came to a primary school for conducting an experiment of a disguised IQ test on 18 classes, from Grade 1 to 6. At first, the most important part during the preparation was to select 

a group of students at random, with the percentage of 20%. However, the scores were not disclosed to teachers but they were told that, the list of the students could be expected to be “the most intellectual bloomers” and these bloomers’ names were informed on the paper. After a semester, the study led to the conclusion that, the selected students obtained relatively high scores during the courses and became more selfconfident compared with others due to teacher expectation and influence on student achievement. This research supported the theory of observer-expectancy effect [26, 27]. 

Rosenthal’s theory is to stimulate students learning through effective hints. By this theory, we are trying to build a visual graph model, as shown in Fig. 5 is a topological sort diagram based on Network Technology Major. Here are 15 courses as nodes. The sequence of courses is offered as directed edges and the weight of the course has conditional probability _P_ ( _xi_ = _E_ | _s_ = _H_ ) (score = E, salary = H). For studying courses with the higher weight, it is strongly recommended that the students should pay more attention and devote more energy. 

In Fig. 5, the courses of WNDW, ICT and DAWEB have higher weight than others. 

**Acknowledgements** Our research is supported by the Project supported by the Educational Reform of Higher Education in Jiangsu Province of China (2017JSJG283). 

## **References** 

1. B. Inderpal and C. Edward, Advanced scout: data mining and knowledge discovery in NBA data, _Data Mining and Knowledge Discovery_ , Vol. 1, pp. 121–125, 1997. https ://doi. org/10.1023/a:10097 82106 822. 

2. S. V. Mehmet and G. Mustafa, Criminal prediction using Naive Bayesian theory, _Neural Computing & Applications_ , Vol. 28, pp. 2581–2592, 2017. https ://doi.org/10.1007/s0052 1-016-2205-z. 

3. A. Mohammad and C. Girija, Energy efficient data mining scheme for high dimensional data, _Procedia Computer Science_ , Vol. 46, pp. 483–490, 2015. https ://doi.org/10.1016/j.procs .2015.02.047. 

4. X. Li, L. M. Zhang and S. H. A. Zhang, Efficient Bayesian networks for slope safety evaluation with large quantity monitoring information, _Geoscience Frontiers_ , Vol. 9, No. 6, pp. 1679–1687, 2018. 

5. M. Matthew, P. L. De Leon, and D. Keeley, Bayesian classification of falls risk, _Gait & Posture_ , Vol. 67, pp. 99–103, 2019. 

1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

181 

6. S. R. Bhagya Shree and H. S. Sheshadri, Diagnosis of Alzheimer’s disease using Naive Bayesian Classifier, _Neural Computing & Applications_ , Vol. 29, pp. 123–132, 2018. https ://doi.org/10.1007/ s0052 1-016-2416-3. 

7. R. Cristobal and V. Sebastian, Educational data mining: a survey from 1995 to 2005, _Expert Systems with Applications_ , Vol. 33, No. 1, pp. 135–146, 2007. https ://doi.org/10.1016/j.eswa.2006.04.005. 

8. Y. Zhu, A data driven education decision support system, _International Journal of Emerging Technologies in Learning (iJET)_ , Vol. 13, No. 11, p. 4, 2018. https ://doi.org/10.3991/ijet.v13i1 1.9582. 

9. F. Grivokostopoulou, I. Perikos, and I. Hatzilygeroudis, Utilizing semantic web technologies and data mining techniques to analyze students learning and predict final performance, _International Conference on Teaching, Assessment and Learning (TALE)_ , pp 488–494, 2014. https ://doi.org/10.1109/tale.2014.70625 71. 

10. I. E. Livieris, T. Mikropoulos, and P. Pintelas, A decision support system for predicting students’ performance, _Themes in Science and Technology Education_ , Vol. 9, pp. 43–57, 2016. 

11. H. M. Nagy, W. M. Aly, and O. F. Hegazy, An educational data mining system for advising higher education students, _World Academy of Science, Engineering and Technology, International Journal of Computer, Electrical, Automation, Control and Information Engineering_ , Vol. 7, No. 10, pp. 175–179, 2013. 

12. A. Y. Noaman, J. M. Luna, A. H. M. Ragab, and S. Ventura, Recommending degree studies according to students’ attitudes in high school by means of subgroup discovery, _International Journal of Computational Intelligence Systems_ , Vol. 9, No. 6, pp. 1101–1117, 2016. https ://doi.org/10.1080/18756 891.2016.12565 73. 

13. Y. Lang and L. Kong, _The U.S. Government Released “Big Data Research and Development Initiative”_ , 2012. http://escj.cnic.cn/ cn/y2012 /v3/i2/89. 

14. S. Patil and S. Kulkarni, Mining social media data for understanding students’ learning experiences using Memetic algorithm, _Materials Today: Proceedings_ , Vol. 5, No. 1, pp. 693–699, 2015. https ://doi.org/10.1016/j.matpr .2017.11.135. 

15. C. Vialardi, J. Chue, and J. P. Peche, A data mining approach to guide students through the enrollment process based on academic performance, _User Modeling and User-Adapted Interaction_ , Vol. 21, pp. 217–248, 2011. https ://doi.org/10.1007/s1125 7-011-9098-4. 

16. I. E. Livieris, T. Kotsilieris, V. Tampakas, and P. Pintelas, Improving the evaluation process of students’ performance utilizing a decision support software, _Neural Computing and Applications_ , Vol. 15, pp. 235–246, 2018. https ://doi.org/10.1007/s0052 1-018-3756-y. 

17. M. Koutina and K. L. Kermanidis, Predicting postgraduate students’ performance using machine learning techniques, _Artificial Intelligence Applications and Innovations_ , Vol. 364, pp. 159–168, 2011. https ://doi.org/10.1007/978-3-642-23960 -1_20. 

18. Z. H. Zhou, _Machine Learning_ . Tsinghua University, Beijing, 2016. **(Chapter 2,3,7)** . 

19. A. Biedermanna, S. Bozzaba, and F. Taronia, Analysing and exemplifying forensic conclusion criteria in terms of Bayesian decision theory, _Science & Justice_ , Vol. 58, No. 2, pp. 159–165, 2018. https ://doi.org/10.1016/j.sciju s.2017.07.002. 

20. A. P. Dempster, N. M. Laird, and D. B. Rubin, Maximum likelihood from incomplete data via the EM algorithm, _Journal of the American Statistical Association_ , Vol. 100, No. 469, pp. 1–5, 1977. 

22. A. alias Balamurugan, R. Rajaram, S. Pramala, S. Rajalakshmi, C. Jeyendran, and J. D. Prakash, NB+: an improved Naïve Bayesian algorithm, _Knowledge-Based Systems_ , Vol. 24, No. 5, pp. 563– 569, 2011. https ://doi.org/10.1016/j.knosy s.2010.09.007. 

23. M. Fanuel and J.A.K. Suykens, Deformed Laplacians and spectral ranking in directed networks, _Applied and Computational Harmonic Analysis_ , 2017. https ://doi.org/10.1016/j.acha.2017.09.002. **(in press)** . 

24. L. C. Lee, C. Y. Liong, and A. A. Jemain, Validity of the best practice in splitting data for hold-out validation strategy as performed on the ink strokes in the context of forensic science, _Microchemical Journal_ , Vol. 139, pp. 125–133, 2018. https ://doi. org/10.1016/j.micro c.2018.02.009. 

25. G. Jiang and W. Wang, Error estimation based on variance analysis of k-fold cross-validation, _Pattern Recognition_ , Vol. 69, pp. 94–106, 2017. https ://doi.org/10.1016/j.patco g.2017.03.025. 

26. W. Marciszewski and G. Plebanek, On measures on Rosenthal compacta, _Journal of Mathematical Analysis and Applications_ , Vol. 385, No. 1, pp. 185–193, 2012. https ://doi.org/10.1016/j. jmaa.2011.06.030. 

27. X.-L. Hu, An extension of Rosenthal’s inequality, _Applied Mathematics and Computation_ , Vol. 2018, No. 8, pp. 4638–4640, 2011. https ://doi.org/10.1016/j.amc.2011.09.001. 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Deyan Wang** associate professor. Her research interests includeParticle Swarm Optimization and Machine Learning Algorithms, etc. 



**Amritl Jaharadak Adam** Malaysian, Ph.D., associate professor, His research interests include Computer Science, Digital Image Forgery, Computer Games, Data Analytic, ICT, etc. 



21. N. Marhamati, E. K. Buxton, and S. Rahimi, Integration of Z-numbers and Bayesian decision theory: a hybrid approach to decision making under uncertainty and imprecision, _Applied Soft Computing_ , Vol. 72, pp. 273–290, 2018. https ://doi.org/10.1016/j. asoc.2018.07.053. 

1 3 

International Journal of Wireless Information Networks (2019) 26:174–182 

182 



**Ying Xiao** Master, associate professor. His research interests include wireless networks, cloud computing, etc. 



**Ya Gao** Ph.D. His research interests include High Performance Network and Switching, etc. 

1 3 

