---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\UCCI-especializaciónProy Investigación\MODULO 7.PORAT\PORAT-18-01-23\BAYESIAN VS NEURONAL ingles.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]



Journal of Materials Processing Technology 164–165 (2005) 1430–1435 



# Modeling of manufacturing processes by learning systems: The na¨ıve Bayesian classifier versus artificial neural networks 

Marcin Perzyk<sup>∗</sup> , Robert Biernacki, Andrzej Kocha´nski 

_Institute of Materials Processing, Warsaw University of Technology, Narbutta 85, 02-954 Warszawa, Poland_ 

### **Abstract** 

Modeling capabilities of two types of learning systems are compared: the na¨ıve Bayesian classifier (NBC) and artificial neural networks (ANNs), based on their prediction errors and relative importance factors of input signals. Simulated and real industrial data were used. It was found that NBC can be an effective and, in some applications, a better tool than ANNs. © 2005 Elsevier B.V. All rights reserved. 

_Keywords:_ Modeling; Manufacturing process; Learning systems; Na¨ıve Bayesian classifier; Artificial neural networks 

## **1. Introduction** 

Designing and controlling manufacturing processes can be aided by the use of mathematical tools. In practice, we often have to do with processes of the “black box” type processes, which physical nature is either unknown or very complex. Modeling processes of this kind consist in establishing the relationship between the input and the output (i.e. result) signals on the basis of a certain number of observed cases (regression problem). Recently, it has been artificial neural networks (ANNs) that have been commonly used for this purpose. Their applications include, for example: 

- predicting properties of products or materials on the basis of the parameters of the technological process involved; 

- predicting equipment failures on the basis of selected signals; 

- identifying the causes that lead to the appearance of manufacturing defects in products; 

- designing based on the specific data which was collected in the industry and generalized by ANNs. 

Despite of great successes, ANNs have several shortcomings, such as complex and time-consuming training process 

> ∗ Corresponding author. Tel.: +48 22 8429347; fax: +48 22 8499797. _E-mail address:_ m.perzyk@wip.pw.edu.pl (M. Perzyk). 

and ambiguity of the results. The same problem may be solved by networks with different architectures and topology of connections. Moreover, for a particular network, each learning brings about different values synapse weights related to reaching local minima of network errors [2,5,6]. 

This lack of prediction uniqueness does not appear in modeling with the help of other mathematical tools, such as polynomials or the na¨ıve Bayesian classifier (NBC) [3] – a simple learning system making use of the probability calculus. The authors of the paper are not aware of any applications of NBC to the modeling of industrial processes. 

The present research project is concerned with an analysis of the NBC’s applicability to the problems of modeling manufacturing processes, an analysis residing in the comparison of prediction errors of the NBC and those of ANNs, as well as in the comparison of the relative importance factors of input signals for the data modeled with the help of both systems. Basically, ANNs are used by interrogating them, i.e. by the simple calculation of output values for assumed values of inputs. However, to facilitate performing the tasks such as the identification of the causes of defects in products, or critical factors for a failure of equipment, an analysis of the relative importance of the input signals seems to be most useful. Similarly, finding production parameters, which are most significant for obtaining particular physical or economical effects, can help in the optimization of manufacturing process. 

0924-0136/$ – see front matter © 2005 Elsevier B.V. All rights reserved. doi:10.1016/j.jmatprotec.2005.02.043 

_M. Perzyk et al. / Journal of Materials Processing Technology 164–165 (2005) 1430–1435_ 

1431 

## **2. Learning systems making use of the na¨ıve Bayesian classifier** 

Those systems which make use of probabilistic methods are typically based on the Bayesian theorem and equation [1]. They include the Bayesian classifiers (the optimal classifier, without any practical importance, and the NBC) as well as the Bayesian networks [3]. 

The Bayesian theorem is applicable in the case of events with known outcomes whose occurrence depends on factors preceding them. We calculate the probability that a given factor is the cause of a particular event (the effect). The use of the NBC requires calculating of probabilities on the basis of an appropriately prepared training data set, which consists of examples described by means of attributes and the target concept. The use of the NBC consists in the following: 

- Establishing the so-called attributes (categories) for input quantities and the categories of the output quantity (the target concept). It should be noted that the NBC requires the use of quantities which are nominal or serial, but not continuous in character. The “value” of an attribute or of the target concept is defined through marking its membership in a particular category, which in turn may be identified verbally. For instance, something may be “very small”, “small” “medium”, “big” and “very big” (five categories) or “good” and “bad” (two categories). 

- Creating the training data set which consists of records including the values of attributes of all input quantities, as well as the corresponding value of the output quantity. 

- On the basis of the training data set the probabilities of particular categories of the output quantity are estimated, as well as the probabilities of particular values of attributes (categories) of all input quantities for particular output categories. This phase is referred to as the training of the classifier. 

- On the basis of the estimated probabilities obtained in the training phase one can calculate the probabilities of the occurrences of each category of the output quantity for any given case (any input vector). The solution given by the NBC is that value of the output quantity category, which scored the highest probability value. If the output categories were created by assigning particular ranges of continuous output values to the numbers standing for the categories, it is possible to change the number of the calculated category for example into a mean original value from such a range. 

the latter type, in which the input–output dependencies are known, make possible a better assessment of the learning systems’ prediction correctness. These simulated data sets were created on the basis of assumed simple equations of the type _Y_ = _f_ ( _X_ 1, _X_ 2, _. . ._ ) in the following way: all the input values were originally set at random between 0 and 1, then the output was calculated and, finally, ±20% noise of the Gaussian type distribution was added to the generated input values. In the present work, the following data sets were used: 

- _Industrial data 1_ . Ductile cast iron strength as the function of its chemical composition [4]. In addition to the training subset containing 700 records, the verifying subset was also created, which contained 90 records. 

- _Industrial data 2_ . The input quantities here are the production process parameters which are related to the green sand mould (12 parameters). The output quantity is the appearance of the gas porosity defect in steel castings. In this case, the original output was of a discrete type (category “1” – no defect, category “2” – defect). The training data set contained 172 records and there was no verifying set. The data in question were presented and analyzed in detail in the work of two of the present authors [5]. 

- _Simulated data 1_ . The set was obtained in accordance with the following equation: _Y_ = _X_ 1 + 2 _X_ 2 + 3 _X_ 3 + 4 _X_ 4 + 5 _X_ 5. The training set contained 1000 records, while the verifying one – 200 records. 

- _Simulated data 2_ . The set was obtained in accordance with the following equation: _Y_ = (6 _X_ 1)<sup>3</sup> + (10<sup>−3</sup> _X_ 2)<sup>3</sup> + · · · + (1 _X_ 7)<sup>3</sup> + · · · + (1 _X_ 12)<sup>3</sup> . The output values of this set have a continuous character. The training set contains 1000 records, while the verifying one – 200 records. 

- _Simulated data 3_ . The output values _Y_ of this set have a binary character, 0 or 1, depending on whether or not the sum above goes beyond a certain boundary value. The values of the input data in this case were identical as the values in the simulated data 2 set. The boundary value was chosen in such a way that the proportion of the _Y_ = 1 value in the set was about 15%. The number of records in the set is as in the _simulated data_ 3. 

- _Simulated data 4_ . The training set is of the same type as the _simulated data_ 3. However, this time the number of records is 172 and there is no verifying data set. 

The _simulated data_ 2–4 were designed in a way making possible a comparative analysis of selected results from these sets with the results obtained for the _industrial data_ 2. 

## _3.2. Artificial neural networks_ 

## **3. Research methodology** 

## _3.1. Data sets_ 

The data sets used in the present work differ in the character of the dependence between input and output signals. They include both industrial and simulated data. The sets of 

The networks had the MLP-type architecture with one hidden layer having the number of neurons equal to the number of the network’s inputs. To improve the learning results, the training method called ‘simulated annealing’ has been applied, combined with the conventional back-propagation method. The simulated annealing method was used for a better selection of the initial values of the synapses while the 

_M. Perzyk et al. / Journal of Materials Processing Technology 164–165 (2005) 1430–1435_ 

1432 

back-propagation phase of the learning decreased the network error. For data which included verification (testing) sets the learning process automatically ended when the error calculated for the verification set started to grow. For the data without verification sets the criterion for ending of the learning session was the mean square error change in a single iteration less then 5 × 10<sup>−6</sup> . Each network has been trained 10 times. 

The relative importance factor of input signals can be defined in several ways. In general, it should reflect the maximum extent of change of the system output due to possible changes of the inputs. The definition assumed in the present work is based on the maximum differences between the output values which can be obtained by changing the considered input (within the training interval), while the remaining inputs are kept at randomly assumed values. This is repeated a number of times and the average of the maximum differences is calculated for that input. The values thus obtained for each input are then normalized between 0 and 1 so that the most significant input gets the rank equal 1 and the least significant – the rank equal 0. 

## _3.3. The Bayesian classifier_ 

In the present work, continuous variables were translated into attribute values and categories through the inclusion of a particular variable into an appropriate range of its original value, with a particular number having been assigned to the range. For each of the above sets, trials were made in setting the number of ranges (categories) for the input and output values. In a particular learning session, the same number of ranges were used for all variables. All calculations for the NBC were programmed in the VBA for Excel language and were represented in a calculation sheet. It should be noted that verifying sets are not necessary to train the NBC. They can be used only for assessment of the system’s prediction ability in the case of new data. 

Fig. 1 represents the results of trials of division of the continuous data values into categories. The curves show relative average errors of modeling results for sets with different characteristics. In the case of the _industrial data_ 2 (as well as the _simulated data_ 3, which is not represented in the diagram) the error was defined as the percentage of false categories. The distributions of errors for the training and the verifying data are similar. The assumed numbers of categories were those which gave the lowest errors for the verifying data (or the training data in the absence of the verifying data). 

The relative importance factor for the NBC is calculated on the basis of the elements of trained system. An input _Xi_ influencesthecategoryoftheoutput _Y_ throughtheconditional probabilities of the form: 



where _cj_<sup>(</sup><sup>_x_)</sup> is an input category, and _ck_<sup>(</sup><sup>_y_)</sup> the output category. 



Fig. 1. Errors of output quantity prediction by the NBC for selected data sets in the function of the number of categories. 

The measure of an input’s importance is defined as the maximal possible difference of the probability values given by (1) for that input. These maximal differences are calculated for each category of the output _ck_<sup>(</sup><sup>_y_)</sup> and then averaged over all possible output categories. The relative importance factors are obtained by normalizing those averages in the 0–1 interval. 

## **4. Comparison of errors of NBC and ANNs** 

The average errors of output value prediction results obtained from the NBC and the ANNs were identified, taking into consideration their proportion in the characteristic value ranges. Fig. 2 represents the distributions of prediction errors for the _simulated data_ 1. It follows from the diagram that the ANNs are able to model the dependencies characterized by a set of this type much more precisely, i.e. a set 



Fig. 2. The comparison of output prediction errors obtained from the NBC and the ANNs (minimum errors from 10 training sessions) for the _simulated data_ 1 set. 

_M. Perzyk et al. / Journal of Materials Processing Technology 164–165 (2005) 1430–1435_ 

1433 



Fig. 3. The comparison of output prediction errors obtained from the NBC and the ANNs (minimum errors from 10 training sessions) for the _simulated data_ 2 set. 

whichhas“clear”dependenciesandwhichisrelativelynumerous. 

Fig. 3 presents the error distributions for the simulated data set imitating, to some extent, the character of the _industrial data_ 2 set, but with the output of a continuous type. The predictions of both systems, modeling the complex relations, exhibit large errors. It should be emphasized, however, that the ANNs coped with its task slightly better, since the proportion of small errors is bigger in the case of this system. 

In the case of the _industrial data_ 1 – the data with a continuous output the NBC is clearly better than the ANNs in predicting the output values (see Fig. 4). 

Fig. 5 represents a comparison of the distribution of errors characterized as the percentages of false categories for the training sets with binary outputs. The continuous responses of the ANNs were translated into a binary form in the following way: the values from the 0–0.5 range were assigned the category “1”, while the values from the 0.5–1 range were assigned the category “2”. It can be easily seen that the ANNs are much better than the NBC in modeling the dependencies characterized by the binary type output for the _industrial data_ 1. On the other hand, in the case of simulated data the level of success depends on the size of the train- 



Fig. 4. The comparison of output prediction errors obtained from the NBC and the ANNs (minimum errors from 10 training sessions) for the _industrial data_ 1 set. 



Fig. 5. The comparison of output prediction errors obtained from the NBC and the ANNs (average errors from 10 training sessions) for the data with a binary output. 

ing set: for small sets it is the NBC which gives better results. 

## **5. Relative importance factors of the input signals** 

Figs. 6–9 show the charts of input signal importance factors estimated by means of the methods discussed in Section 3. In the case of the ANNs, the diagram also shows the scatters of results from 10 training sessions. The scatters were defined by ranges of the appropriate values. 



Fig. 6. Relative importance factor values of input quantities for NBC and ANNs, for the _simulated data_ 1 (the scatters of values obtained from the ANNs are marked with vertical bold lines); a and b charts are obtained for two different simulations of data sets. 

_M. Perzyk et al. / Journal of Materials Processing Technology 164–165 (2005) 1430–1435_ 

1434 



Fig. 7. Relative importance factor values for input signals for the _simulated data_ 2 set. 

In the cases represented in Fig. 6a and b the calculated relative importance factor values generally agree with the expectations (the distribution of the relative importance factor values reflects the growing role of the consecutive input quantities, from 1 to 5). However, the ANNs can predict the importance of the input signals much more precisely than the NBC. Additionally, this system turned out to be more sensitive to the randomly generated noise in the training set. That fact was reflected in the considerably different values for low-importance signals for two sets simulated according to the same equation. 

Figs. 7 and 8 represent the distribution of the relative importance factor values of the simulated data sets which have the same structure of input signals and differ with respect to the type of the output data (Fig. 7 – _simulated data_ 2, with a continuous output; Fig. 8 – _simulated data_ 3, with a binary output). Both data sets pertain to a hypothetical situation in which we try to find out which of the 12 parameters of the production process could be the cause in the decrease of the product quality. The first set assumes that the output quality parameter in question is a continuous quantity – it could be, for example, the surface roughness or some property of the material. The second set imitates the typical situation in which products are classified as either good or defective. In 



Fig. 8. Relative importance factor values for the input signals for the _simulated data_ 3 set. 



Fig. 9. Relative importance factors of production and environmental parameters related to the sand mould for the appearance of the gas porosity defect in steel castings (the source of the industrial data [5]); 1 – time from molding to pouring, 2 – pouring order, 3 – molding team number 4 – assembling team number, 5 – mould quality index, 6 – pouring quality index, 7 – molding sand moisture content, 8 – molding sand permeability, 9 – molding sand tensile strength, 10 – ambient temperature before the pouring day, 11 – ambient temperature at pouring, 12 – air humidity. 

the case of both sets of data it was assumed that the decisive signal is _X_ 1, but the sum of the effects of the selected six other signals (from _X_ 7 to _X_ 12) may bring about the same result. On the other hand, the signals from _X_ 2 to _X_ 6 were assumed to have practically no importance. 

The relative importance factors obtained from both the ANNs and the NBC for the set with the continuous output confirm the clearly conspicuous effect of the _X_ 1 signal, as well as generally slightly higher relative importance factor values of the signals from _X_ 7 to _X_ 12, in comparison to the signals from _X_ 2 to _X_ 6. 

In the case of outputs of the binary type one can observe a dramatic increase in the scatters of results for particular ANN training session, as compared with what is presented in Fig. 7. Although the _X_ 1 signal has the highest average importance value, the next signals ( _X_ 6 and _X_ 11) are not very much different. Taking into consideration the huge scatters, one cannot affirm that the neural network found a signal with such a predominant importance. On the other hand, the results of the classification made by the NBC are unequivocal in character. It is worth emphasizing that the ambiguity of the ANNs predictions, which shows up – among other things – in high scatters of relative importance factor values, seems to be unavoidable, despite all the efforts aimed at its reduction [7]. 

Fig. 9 is the relative importance chart for the causes of the gas porosity defect in steel castings. The chart was prepared on the basis of the industrial data obtained in the research project described in reference [5]. The aim of that project was the identification of the causes of the defects in one of the co-operating foundries. 

The diagram shows huge scatters of the results obtained in successive ANN training sessions, as well as the absence of a clearly conspicuous importance of the group of parameters which were identified as the causes of defects, by means of other methods of analysis [5]. The relevant factors were seven parameters influencing the vapor pressure in the mould 

1435 

_M. Perzyk et al. / Journal of Materials Processing Technology 164–165 (2005) 1430–1435_ 

at the moment of pouring: the green sand humidity at the moment of molding, its permeability, strength (the factor indirectly indicating humidity), the ambient temperature before the pouring of the production process, the ambient temperature during the pouring, the time from molding to pouring, and the air humidity before the pouring time. 

The above group of signals did not emerge as in any way conspicuous also in the case of the NBC. Fig. 9 shows as very important the signal “pouring quality index”, which was indicated by both systems and which could also be a cause of the defect. 

The results shown in Fig. 9 indicate that, as is the case with ANNs [5], a very important issue is the development of methods of automated analysis of the NBC results. This would facilitate finding the synergetic effects of an arbitrary group of input signals, which seems to be a key problem. 

results in the case of signals with lower importance. For an output of a binary type the NBC identified a clearly conspicuous signal and hence, its result was better that that obtained from ANNs. 

Apparently the main advantage of the NBC in comparison with ANNs is its uniqueness, as well as the simplicity of its use. It may also be assumed that the NBC is less demanding as far as the size of the training set is concerned (for instance, the training does not require the use of a verifying set). 

It seems that the NBC can make a learning system which is useful in industrial applications and which, in some cases, may be better than ANNs. However, further research is necessary,especiallyonextendingthepossibilitiesofinterpretation of the results of both systems. 

## **References** 

## **6. Summary and conclusions** 

- [1] T. Bayes, Philos. Trans. Roy. Soc. London 53 (1763) 370–418. 

The comparative analysis discussed in the present work leads to the conclusion that the prediction errors of an NBC may be lower or higher that the errors of an ANNs. For two identical simulated data sets with binary output, which differed only with respect to size, the NBC produced a smaller error (percentage of false categories) than an ANNs. 

The relative importance factor of input quantities for the NBC in its present form leads to a low degree of precision of 

- [2] T. Masters, Practical Neural Network Recipes in C++, Academic Press, 1993. 

- [3] T.M. Mitchell, Machine Learning, McGraw-Hill, 1997. 

- [4] M. Perzyk, A. Kocha´nski, J. Mater. Process. Technol. 109 (2001) 305–307. 

- [5] M. Perzyk, A. Kocha´nski, J. Eng. Manuf. 217 (2003) 1279–1284. 

- [6] M. Perzyk, A. Kocha´nski, J. Kozłowski, Informatyka w Technologii Materiał´ow 3 (2003) 125–132. 

- [7] M.A. Yescas, H.K.D.H. Bhadeshia, D.J. MacKay, Mater. Sci. Eng. A 311 (2001) 162–173. 

