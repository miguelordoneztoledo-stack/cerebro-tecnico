---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Flujo No Permanente\02 Bibliografia\10 Numerical Modeling in Open Channel Hydraulics.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

Numerical Modeling in Open Channel Hydraulics 

Water Science and Technology Library 

##### VOLUME 83 

##### _Editor-in-Chief_ 

V.P. Singh, _Texas A&M University, College Station, TX, U.S.A_ . 

_Editorial Advisory Board_ 

M. Anderson, _Bristol, U.K._ L. Bengtsson, _Lund, Sweden_ J. F. Cruise, _Huntsville, U.S.A._ U. C. Kothyari, _Roorkee, India_ S. E. Serrano, _Philadelphia, U.S.A._ D. Stephenson, _Johannesburg, South Africa_ W. G. Strupczewski, _Warsaw, Poland_ 

For further volumes: http:// www.springer.com/series/6689 

# Numerical Modeling in Open Channel Hydraulics 

Romuald Szymkiewicz 

Faculty of Civil and Environmental Engineering, Gda´nsk University of Technology, Poland 

123 

Romuald Szymkiewicz Faculty of Civil and Environmental Engineering Gda´nsk University of Technology ul. Narutowicza 11/12 80-233 Gda´nsk Poland rszym@pg.gda.pl 

ISBN 978-90-481-3673-5 e-ISBN 978-90-481-3674-2 DOI 10.1007/978-90-481-3674-2 Springer Dordrecht Heidelberg London New York 

Library of Congress Control Number: 2009942268 

###### © Springer Science+Business Media B.V. 2010 

No part of this work may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, microfilming, recording or otherwise, without written permission from the Publisher, with the exception of any material supplied specifically for the purpose of being entered and executed on a computer system, for exclusive use by the purchaser of the work. 

###### Printed on acid-free paper 

Springer is part of Springer Science+Business Media (www.springer.com) 

## **Preface** 

Open channel hydraulics has always been a very interesting domain of scientific and engineering activity because of the great importance of water for human living. The free surface flow, which takes place in the oceans, seas and rivers, can be still regarded as one of the most complex physical processes in the environment. The first source of difficulties is the proper recognition of physical flow processes and their mathematical description. The second one is related to the solution of the derived equations. The equations arising in hydrodynamics are rather complicated and, except some much idealized cases, their solution requires application of the numerical methods. For this reason the great progress in open channel flow modeling that took place during last 40 years paralleled the progress in computer technique, informatics and numerical methods. It is well known that even typical hydraulic engineering problems need applications of computer codes. Thus, we witness a rapid development of ready-made packages, which are widely disseminated and offered for engineers. However, it seems necessary for their users to be familiar with some fundamentals of numerical methods and computational techniques applied for solving the problems of interest. This is helpful for many reasons. The ready-made packages can be effectively and safely applied on condition that the users know their possibilities and limitations. For instance, such knowledge is indispensable to distinguish in the obtained solutions the effects coming from the considered physical processes and those caused by numerical artifacts. This is particularly important in the case of hyperbolic equations, like the Saint-Venant equations or the advection equation. 

In principle, numerical open channel hydraulics can be regarded as a sub-domain of Computational Fluid Dynamics (CFD) and the general methods and experiences of CFD are applicable in open channel flow modeling. Moreover, the open channel flow can be often treated as one-dimensional, which makes it relatively easy to solve compared to multidimensional flows considered in geophysics and industrial engineering. On the other hand, due to a range of specific issues, numerical open channel hydraulics developed into a branch of its own as early as in the years 1960s and 1970s. There exist a number of very good books on the subject, written at that time and later. A non-exhaustive list includes “Unsteady flow in open channel” edited by K. Mahmood and V. Yevjevich and containing the papers written by recognized experts, “Practical aspects of computational river hydraulics” by J.A. Cunge, F.M. 

v 

vi 

Preface 

Holly and A. Verwey, “Computational hydraulics-Elements of the theory of free surface flow” by M.B. Abbott, “Dynamic hydrology” by P.S. Eagleson, “Open channel hydraulics” by V.T. Chow, “Open channel flow” by F.M. Henderson, “Kinematic wave modeling in water resources: surface water hydrology” by V.P. Singh, “The hydraulics of open channel flow: An introduction” by H. Chanson. These books cover most of the theoretical and practical issues related to open channel flow modeling and can be recommended for any engineer working in this field. 

As far as the computational techniques are considered, one can recommend the following books: “Incompressible flow and the finite-element method” by P.M. Gresho and R.L. Sani, “Computational fluid dynamics” by M.B. Abbott and D.R. Basco, “Numerical head transfer and fluid flow” by S.V. Patankar, “Computational physics” by D. Potter, “Computational techniques for fluid dynamics” by C.A.J. Fletcher, “Finite volume methods for hyperbolic problems” by R.J. LeVeque, “The finite element method in engineering science” by O. C. Zienkiewicz. These books covering large area of the fluid dynamics and other engineering sciences are useful for open channel flow modeling as well. 

In view of the continuous advance in numerical techniques, the present book is an attempt to complement the existing works with a more detailed and up-to-date discussion of selected numerical aspects of open channel hydraulics. It is largely based on author’s own research and focuses on one-dimensional models of steady and unsteady flow and transport in open channels and their networks. 

The book is organized in nine chapters. Chapter 1 presents the background information on the open channel hydraulics and the derivation of the governing equations for both steady and unsteady flow, as well as for the transport of the constituents dissolved in the flowing water including the transport of thermal energy. 

The next two chapters cover the basic numerical methods applicable for solving nonlinear equations and systems of linear and nonlinear equations (Chapter 2) and ordinary differential equations and their systems (Chapter 3). Implementation of the presented methods for solution the steady gradually varied flow in a single channel and in channel network is given in Chapter 4. These methods are also the basic building blocks for more complex numerical algorithms described in the following chapters. 

Chapter 5 is an introduction to the partial differential equations of hyperbolic and parabolic types, frequently occurring in open channel hydraulic. It covers the classification of equations, formulation of solution problem, and introduction to the finite difference and element methods. This chapter ends by discussion of convergence, consistency and stability of the numerical methods. 

In Chapters 6 and 7 the advection and advection-diffusion equations are considered. Basing on the solution using the finite difference box scheme, the main problems of numerical integration of the hyperbolic equations are discussed. The modified equation approach for the accuracy analysis of the numerical solution of hyperbolic equations is described. Besides the standard methods of solution, the splitting technique for the advection-diffusion transport equation is presented. 

Chapter 8 is entirely devoted to the unsteady flow. Solution of the system of Saint Venant equations using both finite difference and element methods is described. 

Preface 

vii 

Solution of unsteady flow with moveable bed and the problem of propagation of steep waves are briefly described. 

Chapter 9 covers the simplified models and theirs application for flood routing. Particular attention is focused on the close relation between the spatially lumped models and the discrete forms of distributed models. The conservative properties of the non-linear and linear simplified models are discussed. 

The book includes numerous computational examples and step-by-step descriptions of numerical algorithms. It is the hope of the author that the reader will find it useful and easy to follow. 

I am grateful to Springer and to the members of the Editorial Advisory Board of series Water Science and Technology Library for the possibility of publishing my work. My thanks are to Prof. Witold Strupczewski, for initiating the idea of this book, to the Editor-in-Chief Prof. Vijay. P. Singh for his valuable suggestions on its contents, and to Ms. Petra van Steenbergen and Ms. Cynthia de Jonge for their kind assistance in submitting the manuscript. I would also like to acknowledge the support received from Prof. Ireneusz Kreja, Dean of the Faculty of Civil and Environmental Engineering of the Gda´nsk University of Technology. I owe a lot to the persons who assisted me in the work on the manuscript: Dr. Dariusz Ga˛siorowski, who prepared many numerical examples, Ms. Katarzyna Olszonowicz, who prepared all the figures and my son Dr. Adam Szymkiewicz, whose remarks and suggestions helped to improve the text. Finally, I highly appreciate the effort of all members of staff involved at all stages of the editorial process of my book. 

Gdansk, Poland 

Romuald Szymkiewicz 

## **Contents** 

|**1**<br>**Ope**|**n Chan**|**nel Flow Equations** . . . . . . . . . . . . . . . . . . . . .<br>1|
|---|---|---|
|1.1|Basic i|Definitions<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>1|
|1.2|Gener|al Equations for Incompressible Liquid Flow<br>. . . . . . . .<br>10|
|1.3|Deriva|tion of 1D Dynamic Equation . . . . . . . . . . . . . . . .<br>12|
|1.4|Deriva|tion of 1D Continuity Equation<br>. . . . . . . . . . . . . . .<br>20|
|1.5|System<br>in Ope|of Equations for Unsteady Gradually Varied Flow<br>n Channel<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>21|
|1.6|Steady|Gradually Varied Flow in Open Channel . . . . . . . . . .<br>24|
||1.6.1|Derivation of Governing Equation from the Energy<br>Equation . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
||1.6.2|Derivation of Governing Equation from the System<br>of Saint-Venant Equations . . . . . . . . . . . . . . . . . .<br>27|
|1.7|Storag|e Equation<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>30|
|1.8|Equati|on of Mass Transport . . . . . . . . . . . . . . . . . . . . .<br>33|
||1.8.1|Mass Transport in Flowing Water . . . . . . . . . . . . . .<br>33|
||1.8.2|Derivation of the Mass Transport Equation . . . . . . . . .<br>35|
|1.9|Therm|al Energy Transport Equation . . . . . . . . . . . . . . . .<br>43|
|1.10|Types|of Equations Applied in Open Channel Hydraulics . . . . .<br>49|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>50|
|**2**<br>**Met**|**hods fo**|**r Solving Algebraic Equations and Their Systems** . . . .<br>53|
|2.1|Soluti|on of Non-linear Algebraic Equations . . . . . . . . . . . .<br>53|
||2.1.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . .<br>53|
||2.1.2|Bisection Method . . . . . . . . . . . . . . . . . . . . . .<br>54|
||2.1.3|False Position Method . . . . . . . . . . . . . . . . . . . .<br>56|
||2.1.4|Newton Method . . . . . . . . . . . . . . . . . . . . . . .<br>58|
||2.1.5|Simple Fixed-Point Iteration<br>. . . . . . . . . . . . . . . .<br>62|
||2.1.6|Hybrid Methods . . . . . . . . . . . . . . . . . . . . . . .<br>66|
|2.2|Soluti|on of Systems of the Linear Algebraic Equations<br>. . . . . .<br>69|
||2.2.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . .<br>69|
||2.2.2|Gauss Elimination Method . . . . . . . . . . . . . . . . .<br>72|
||2.2.3|LU Decomposition Method . . . . . . . . . . . . . . . . .<br>76|



ix 

|x||Contents|
|---|---|---|
|2.3|Soluti|on of Non-linear System of Equations . . . . . . . . . . . .<br>79|
||2.3.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . .<br>79|
||2.3.2|Newton Method . . . . . . . . . . . . . . . . . . . . . . .<br>80|
||2.3.3|Picard Method . . . . . . . . . . . . . . . . . . . . . . . .<br>82|
|Refe|rences .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>84|
|**3**<br>**Num**|**erical**|**Solution of Ordinary Differential Equations** . . . . . . .<br>85|
|3.1|Initial-|Value Problem . . . . . . . . . . . . . . . . . . . . . . . .<br>85|
||3.1.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . .<br>85|
||3.1.2|Simple Integration Schemes<br>. . . . . . . . . . . . . . . .<br>87|
||3.1.3|Runge–Kutta Methods<br>. . . . . . . . . . . . . . . . . . .<br>93|
||3.1.4|Accuracy and Stability<br>. . . . . . . . . . . . . . . . . . .<br>99|
|3.2|Initial<br>Differ|Value Problem for a System of Ordinary<br>ential Equations . . . . . . . . . . . . . . . . . . . . . . . .<br>104|
|3.3|Bound|ary Value Problem . . . . . . . . . . . . . . . . . . . . . .<br>107|
|Refe|rences .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>110|
|**4**<br>**Stea**|**dy Gra**|**dually Varied Flow in Open Channels** . . . . . . . . . . .<br>111|
|4.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>111|
||4.1.1|Governing Equations . . . . . . . . . . . . . . . . . . . .<br>111|
||4.1.2<br>4.1.3|Determination of the Water Surface Profiles for<br>Prismatic and Natural Channel . . . . . . . . . . . . . . .<br>112<br>Formulation of the Initial and Boundary Value<br>Problems for Steady Flow Equations . . . . . . . . . . . .<br>116|
|4.2|Numer<br>Gradu|ical Solution of the Initial Value Problem for Steady<br>ally Varied Flow Equation in a Single Channel<br>. . . . . . .<br>118|
||4.2.1|Numerical Integration of the Ordinary<br>Differential Equations . . . . . . . . . . . . . . . . . . . .<br>118|
||4.2.2<br>4.2.3|Solution of the Non-linear Algebraic Equation<br>Furnished by the Method of Integration<br>. . . . . . . . . .<br>120<br>Examples of Numerical Solutions of the Initial<br>Value problem . . . . . . . . . . . . . . . . . . . . . . . .<br>125|
||4.2.4|Flow Profile in a Channel with Sudden Change<br>of Cross-Section . . . . . . . . . . . . . . . . . . . . . . .<br>128|
||4.2.5|Flow Profile in Ice-Covered Channel . . . . . . . . . . . .<br>131|
|4.3|Soluti<br>Varied|on of the Boundary Problem for Steady Gradually<br>Flow Equation in Single Channel . . . . . . . . . . . . . .<br>134|
||4.3.1|Introduction to the Problem . . . . . . . . . . . . . . . . .<br>134|
||4.3.2|Direct Solution Using the Newton Method . . . . . . . . .<br>135|
||4.3.3|<br>Direct Solution Using the Newton Method<br>with Quasi–Variable Discharge . . . . . . . . . . . . . . .<br>139|
||4.3.4|Direct Solution Using the Improved Picard Method . . . .<br>141|
||4.3.5|Solution of the Boundary Problem Using<br>the Shooting Method<br>. . . . . . . . . . . . . . . . . . . .<br>144|
|4.4|Steady<br>4.4.1|Gradually Varied Flow in Open Channel Networks<br>. . . .<br>147<br>Formulation of the Problem . . . . . . . . . . . . . . . . .<br>147|



xi 

|Contents|||xi|
|---|---|---|---|
||4.4.2|Numerical Solution of Steady Gradually Varied<br>Flow Equations in Channel Network . . . . . . . . . . . .|149|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|157|
|**5**<br>**Part**|**ial Dif**|**ferential Equations of Hyperbolic**||
|**and**|**Parabo**|**lic Type**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|159|
|5.1|Types<br>5.1.1<br>5.1.2|of Partial Differential Equations and Their Properties . . . .<br>Classification of the Partial Differential Equations<br>of 2nd Order with Two Independent Variables . . . . . . .<br>Classification of the Partial Differential Equations<br>via Characteristics . . . . . . . . . . . . . . . . . . . . . .|159<br>159<br>161|
||5.1.3|Classification of the Saint Venant System||
|||and Its Characteristics . . . . . . . . . . . . . . . . . . . .|165|
||5.1.4|Well Posed Problem of Solution of the Hyperbolic<br>and Parabolic Equations . . . . . . . . . . . . . . . . . . .|169|
||5.1.5|Properties of the Hyperbolic and Parabolic Equations . . .|174|
||5.1.6|Properties of the Advection-Diffusion Transport Equation .|178|
|5.2|Introd|uction to the Finite Difference Method . . . . . . . . . . . .|183|
||5.2.1|Basic Information . . . . . . . . . . . . . . . . . . . . . .|183|
||5.2.2|Approximation of the Derivatives . . . . . . . . . . . . . .|185|
||5.2.3|Example of Solution: Advection Equation . . . . . . . . .|194|
|5.3|Introd|uction to the Finite Element Method . . . . . . . . . . . . .|197|
||5.3.1|General Concept of the Finite Element Method<br>. . . . . .|197|
||5.3.2|Example of Solution: Diffusion Equation . . . . . . . . . .|203|
|5.4|Proper<br>Differ|ties of the Numerical Methods for Partial<br>ential Equations . . . . . . . . . . . . . . . . . . . . . . . .|209|
||5.4.1|Convergence . . . . . . . . . . . . . . . . . . . . . . . . .|209|
||5.4.2|Consistency . . . . . . . . . . . . . . . . . . . . . . . . .|211|
||5.4.3|Stability . . . . . . . . . . . . . . . . . . . . . . . . . . .|212|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|217|
|**6**<br>**Num**|**erical**|**Solution of the Advection Equation** . . . . . . . . . . . .|219|
|6.1|Soluti|on by the Finite Difference Method<br>. . . . . . . . . . . . .|219|
||6.1.1|Approximation with the Finite Difference Box Scheme . .|219|
||6.1.2|Stability Analysis of the Box Scheme<br>. . . . . . . . . . .|222|
|6.2|Ampli|tude and Phase Errors<br>. . . . . . . . . . . . . . . . . . . .|225|
|6.3|Accur    i|acy Analysis Using the Modified Equation Approach . . . .|231|
|6.4|Soluti<br>Eleme|on of the Advection Equation with the Finite<br>nt Method . . . . . . . . . . . . . . . . . . . . . . . . . . .|239|
||6.4.1|Standard Finite Element Approach . . . . . . . . . . . . .|239|
||6.4.2|Donea Approach<br>. . . . . . . . . . . . . . . . . . . . . .|244|
||6.4.3|<br>Modified Finite Element Approach . . . . . . . . . . . . .|246|
|6.5|Nume<br>with th|i<br>rical Solution of the Advection Equation<br>e Method of Characteristics . . . . . . . . . . . . . . . . .|253|
||6.5.1|Problem Presentation . . . . . . . . . . . . . . . . . . . .|253|
||6.5.2|Linear Interpolation . . . . . . . . . . . . . . . . . . . . .|254|



xii 

Contents 

||6.5.3|Quadratic Interpolation . . . . . . . . . . . . . . . . . . .|255|
|---|---|---|---|
||6.5.4|Holly–Preissmann Method of Interpolation . . . . . . . . .|256|
||6.5.5|Interpolation with Spline Function of 3rd Degree<br>. . . . .|258|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|261|
|**7**<br>**Num**|**erical**|**Solution of the Advection-Diffusion Equation**<br>. . . . . .|263|
|7.1|Introd|uction to the Problem . . . . . . . . . . . . . . . . . . . . .|263|
|7.2|Soluti|on by the Finite Difference Method<br>. . . . . . . . . . . . .|265|
||7.2.1|Solution Using General Two Level Scheme<br>with Up-Winding Effect . . . . . . . . . . . . . . . . . . .|265|
||7.2.2|The Difference Crank-Nicolson Scheme . . . . . . . . . .|269|
||7.2.3|Numerical Diffusion Versus Physical Diffusion<br>. . . . . .|272|
||7.2.4|The QUICKEST Scheme . . . . . . . . . . . . . . . . . .|277|
|7.3|Soluti   i|on Using the Modified Finite Element Method . . . . . . . .|279|
|7.4|Soluti<br>with th|on of the Advection-Diffusion Equation<br>e Splitting Technique<br>. . . . . . . . . . . . . . . . . . . .|283|
|7.5|Soluti<br>the Sp|on of the Advection-Diffusion Equation Using<br>litting Technique and the Convolution Integral<br>. . . . . . .|289|
||7.5.1<br>7.5.2<br>7.5.3<br>7.5.4|Governing Equation and Splitting Technique . . . . . . . .<br>Solution of the Advective-Diffusive Equation<br>by Convolution Approach . . . . . . . . . . . . . . . . . .<br>Solution of the Advective-Diffusive Equation with<br>Variable Parameters and Without Source Term . . . . . . .<br>Solution of the Advective-Diffusive Equation<br>with Source Term . . . . . . . . . . . . . . . . . . . . . .|289<br>290<br>293<br>295|
||7.5.5|Solution of the Advective-Diffusive Equation in an<br>Open Channel Network . . . . . . . . . . . . . . . . . . .|297|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|300|
|**8**<br>**Num**|**erical**|**Integration of the System of Saint Venant Equations**. . .|301|
|8.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|301|
|8.2|Soluti|on of the Saint Venant Equations Using the Box Scheme . .|302|
||8.2.1|Approximation of Equations<br>. . . . . . . . . . . . . . . .|302|
||8.2.2|Accuracy Analysis Using the Modified Equation<br>Approach<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|308|
|8.3|Soluti        i<br>Finite|on of the Saint Venant Equations Using the Modified<br>Element Method . . . . . . . . . . . . . . . . . . . . . . .|313|
||8.3.1|Spatial and Temporal Discretization of the Saint<br>Venant Equations . . . . . . . . . . . . . . . . . . . . . .|313|
||8.3.2<br>8.3.3|Stability Analysis of the Modified Finite Element Method .<br>Numerical Errors Generated by the Modified Finite<br>Element Method . . . . . . . . . . . . . . . . . . . . . . .|320<br>325|
|8.4|Some<br>Equati|Aspects of Practical Application of the Saint Venant<br>ons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|330|
||8.4.1|Formal Requirements and Actual Possibilities . . . . . . .|330|
||8.4.2|Representation of the Channel Cross-Section . . . . . . . .|330|



|Contents|||xiii|
|---|---|---|---|
||8.4.3|Initial and Boundary Conditions<br>. . . . . . . . . . . . . .|333|
||8.4.4<br>|Unsteady Flow in Open Channel Network . . . . . . . . .<br>|337|
|8.5|Soluti<br>Chann|on of the Saint Venant Equations with Movable<br>el Bed . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|343|
||8.5.1|Full System of Equations for the Sediment Transport<br>. . .|343|
||8.5.2|Initial and Boundary Conditions for the Sediment<br>Transport Equations . . . . . . . . . . . . . . . . . . . . .|347|
||8.5.3|Numerical Solution of the Sediment Transport Equations .|349|
|8.6|Applic|ation of the Saint Venant Equations for Steep Waves . . . .|351|
||8.6.1|Problem Presentation . . . . . . . . . . . . . . . . . . . .|351|
||8.6.2|Conservative Form of the Saint Venant Equations . . . . .|353|
||8.6.3|Solution of the Saint Venant Equations with Shock Wave .|356|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|364|
|**9**<br>**Simi**|**plified**|**i Equations of the Unsteady Flow in Open Channel** . . . .|367|
|9.1|Simplii|fied Forms of the Saint Venant Equations . . . . . . . . . .|367|
|9.2|Simplii<br>Equati|fied Flood Routing Models in the Form of Transport<br>ons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|372|
||9.2.1|Kinematic Wave Equation . . . . . . . . . . . . . . . . . .|372|
||9.2.2|Diffusive Wave Equation . . . . . . . . . . . . . . . . . .|373|
||9.2.3|Linear and Non-linear Forms of the Kinematic and<br>Diffusive Wave Equations . . . . . . . . . . . . . . . . . .|377|
|9.3|Mass <br>Flood|and Momentum Conservation in the Simplified<br>Routing Models in the Form of Transport Equations<br>. . . .|380|
||9.3.1<br>|The Mass and Momentum Balance Errors . . . . . . . . .<br>|380|
||9.3.2|Conservative and Non-conservative Forms of the<br>Non-linear Advection-Diffusion Equation . . . . . . . . .|383|
||9.3.3|Possible Forms of the Non-linear Kinematic Wave<br>Equation . . . . . . . . . . . . . . . . . . . . . . . . . . .|384|
||9.3.4|Possible Forms of the Non-linear Diffusive Wave<br>Equation . . . . . . . . . . . . . . . . . . . . . . . . . . .|388|
|9.4|Lump|ed Flood Routing Models . . . . . . . . . . . . . . . . . . .|390|
||9.4.1|Standard Derivation of the Muskingum Equation<br>. . . . .|390|
||9.4.2|Numerical Solution of the Muskingum Equation . . . . . .|392|
||9.4.3|The Muskingum–Cunge Model . . . . . . . . . . . . . . .|394|
||9.4.4|Relation Between the Lumped and Simplified<br>Distributed Models . . . . . . . . . . . . . . . . . . . . .|398|
|9.5|Convo|lution Integral in Open Channel Hydraulics . . . . . . . . .|401|
||<br>9.5.1|<br>Open Channel Reach as a Dynamic System<br>. . . . . . . .|401|
||9.5.2|<br>IUH for Hydrological Models . . . . . . . . . . . . . . . .|407|
||9.5.3|An Alternative IUH for Hydrological Lumped Models . . .|411|
|Refe|rences|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|415|
|**Index**<br>|. . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|417|



## **Chapter 1 Open Channel Flow Equations** 

### **1.1 Basic Definitions** 

_Open channel_ is a conduit in which a part of the cross-section of the flowing stream, taken perpendicularly to the flow velocity vector, is exposed atmosphere. Open channels can be divided into natural and artificial ones. Natural channels, like rivers or creeks, result from the geophysical processes acting at the Earth surface, without essential participation of human activity. Conversely, artificial channels are built by men and comprise, among others, navigable, energetic and irrigation channels. 

Another possible division of open channels is between prismatic and nonprismatic ones. A prismatic channel has constant cross-sectional shape and constant longitudinal bottom slope. Of course, such properties can be possessed only by artificial channels. All natural channels are non-prismatic. A schematic representation of a non-prismatic channel is shown in Fig. 1.1. 

In natural channels the sections can be either compacted (Fig. 1.1a) or composite (Fig. 1.1b). In composite cross-section distinct parts exist (1, 2 and 3 in Fig. 1.1b), characterized by different bed elevations and possibly different bed roughness. This case is representative, for instance, of a river flowing over flooded terrace and calculation of the flow parameters requires appropriate treatment. Figure 1.1a also shows some basic variables used in open channel hydraulics. They are listed below. 

_Water stage_ , denoted by _h_ , is the elevation of the free surface of water at a specific cross-section of the channel, measured with respect to the assumed datum. The elevation of the bottom measured with respect to the same datum is denoted by _Z_ . 

_The depth of flow H_ is the vertical distance between the water surface and the channel bottom. In natural channels the depth and bed elevation have local meaning only, since they vary along the axis _x_ , which is parallel to the flow direction and _y_ axis, which is horizontal and normal to _x_ . Conversely, in prismatic channels both _Z_ and _H_ are uniquely defined for each cross-section and depend on _x_ only. Thus, the following relation holds: 



> R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_1, 

1 

⃝C Springer Science+Business Media B.V. 2010 

1 Open Channel Flow Equations 

2 



<!-- Start of picture text -->
a)<br>B<br>z<br>A H (x ,y ) Ha<br>h<br>p Z (x ,y )<br>datum<br>y<br>b)<br>1 2 3<br><!-- End of picture text -->

**Fig. 1.1** Possible shapes of cross-sections of the non-prismatic channel ( **a** ) compacted, ( **b** ) composite 

The _longitudinal bed slope_ is defined as: 



Its value is usually small, which allows for considerable simplifications of the flow equations. In Fig. 1.2 a longitudinal profile of channel is shown. 

The slope is uniquely defined for prismatic channels only. For natural channels the bed slope has rather local meaning, however its average value along channel axis taken over longer distances of practical interest is rough but important information. 

### _h_ 



<!-- Start of picture text -->
h<br>h ( x )<br>H ( x )<br>H ’( x )<br>ϕ<br>Z(x)<br>datum<br>bottom<br><!-- End of picture text -->

**Fig. 1.2** Definition of the cross-section parameters for prismatic channel 

1.1 Basic Definitions 

3 

The value of _H_ ( _x_ ) should be distinguished from so-called depth of flow of section _H_<sup>′</sup> ( _x_ ), which is measured perpendicularly to the bottom (Fig. 1.2). Since both depths are related to each other by means of the bed slope _H_<sup>′</sup> _(x)_ = _H (x)_ cos _(ϕ)_ , then for small values of the longitudinal bed slope, when cos( _ϕ_ ) ≈ 1, one can assume that H _(_ x _)_ ≈ _H_<sup>′</sup> _(x)_ . Only in particular situations, for steep channels, this difference is appreciable (Akan 2006, French 1985). Consequently, usually it is reasonable to assume that the flow depth is measured vertically from bottom to the water surface, whereas the distance along channel axis is considered as horizontal one. The problem of co-ordinates system is summarized by Liggett (1975) as follows: “For open channel flow the system of co-ordinates is not entirely orthogonal in that _x_ lies in the bed of the channel and _z_ is vertical. This arrangement assumes that the cosine of the channel slope is approximately unity.” 

The cross-section can be characterized by the following geometric parameters: 

- _Top width B_ is the width of the channel at the level of water surface (Fig. 1.1). 

- _Flow area A_ is the wetted cross-sectional area measured perpendicularly to the vector of channel flow velocity. 

- _Wetted perimeter P_ is the length of the interface between the water and the channel bed. 

- _Hydraulic radius R_ is the ratio of the wetted flow area and the wetted perimeter: 



This parameter is meaningful only for compact cross-sections as shown in Fig. 1.1a. 

- _Hydraulic depth Ha_ is the ratio of the wetted flow area _A_ and the top width _B_ : 



_Ha_ and _B_ represent the dimensions of a rectangle of area _A_ equivalent to the natural cross-section (Fig. 1.1a). 

The cross-sections of prismatic channels are typically triangular, rectangular or trapezoidal so the parameters listed above can be expressed as analytical functions of the depth _H_ . Consider for example a trapezoidal channel (Fig. 1.3) characterized by the channel width at the level of bottom _b_ , and the side slope _m_ , which is the cotangent of the angle _ψ_ between the side and horizontal plane. 

For such type of channel the cross-section parameters _A_ , _P_ and _B_ are given by the following formulas: 







1 Open Channel Flow Equations 

4 



<!-- Start of picture text -->
B<br>A<br>H<br>H<br>ψ<br>h<br>m  H b<br>Z<br>datum<br>1:m. 1:m.<br>∇<br>∇<br><!-- End of picture text -->

**Fig. 1.3** Trapezoidal channel cross-section 

For _m_ = 0 the trapezoidal cross-section becomes rectangular, whereas for _b_ = 0 it becomes triangular. For natural channels, the geometric parameters are usually expressed as function of the water stage, presented in tabularized form. 

The basic quantities characterizing liquid flow are: pressure, density, velocity and acceleration. The flow is described by the scalar or vector fields of these variable parameters. In general all those variables depend on three spatial coordinates and time. However, in open channel flow the component of the velocity vector parallel to the channel axis is typically dominating and in addition it has relatively uniform distribution over the cross-section area. Thus, it is assumed that the flow parameters are functions of two variables only: _x_ and _t_ , which represent the spatial coordinate related to the channel axis and time. 

The flowing stream is conveniently characterized by the following averaged quantities: 

- _Discharge_ , which represents the mass or volume of water flowing through considered cross-section per unit time. The volume discharge is defined as: 



where: 

_u_ – normal velocity to the cross-section, 

_A_ – wetted cross-sectional area, 

_Q_ – flow discharge. 

- _Average flow velocity_ in the cross-section, which ensures the same discharge as actual velocity distribution over cross-section. It is defined as follows: 



5 

1.1 Basic Definitions 

where: _U_ – average velocity in a cross-section. 

- _Volume flux per unit time and unit width_ of the vertical cross-section measured between the water surface and the bottom, given by the formula: 



where _q_ is flow discharge related to the width unit of a channel. For channel having a rectangular cross-section _q_ is equal: 



The total energy of water particle traveling along a streamline (a line constructed in the velocity field, so that at its every point the velocity vector is tangential to this line) is given by the Bernoulli equation: 



where: 

_Esl_ – total energy of traveling particle along a streamline, 

_zsl_ – elevation of the streamline above the assumed datum, _psl_ – local pressure, 

_γ_ – specific weight, 

_usl_ – local velocity, 

_g_ – local acceleration due to gravity. 

In Eq. (1.12) the term ( _psl_ / _γ_ ) is the pressure head, whereas the term ( _u_<sup>2</sup> _sl_<sup>_/_2</sup><sup>_g_) rep-</sup> resents velocity head. The term ( _psl_ / _γ_ + _zsl_ ) is called the piezometric head (Chanson 2004). 

When the flow in open channel with cross-sectional average velocity is considered, the total energy of flow referred to the assumed datum is: 



whereas the specific energy of the open channel flow relative to the bottom of a channel is defined by formula (Fig. 1.4): 



where: 

6 

1 Open Channel Flow Equations 

**Fig. 1.4** Representation of the energy equation’s terms 



<!-- Start of picture text -->
E ( x )<br>z<br>α U 2<br>2 g<br>U Es<br>H ( x )<br>Z ( x )<br>datum<br>x<br>bottom<br><!-- End of picture text -->

_E_ – total energy related to the assumed datum, 

_Es_ – specific energy related to the bottom, 

_Z_ – elevation of the bed above the assumed datum, 

_H_ – depth, 

_h_ – elevation of the water surface above the assumed datum, 

_U_ – average flow velocity, 

_α_ – kinetic energy correction factor (Coriolis coefficient). 

The Coriolis coefficient _α_ is introduced to correct the kinetic energy calculated using the average flow velocity _U_ instead of the actual velocities, variable over wetted cross-sectional area _A_ . Comparison of both energies yields: 



Coefficient _α_ is never less than 1. Its value increases with the increasing differentiation of flow velocity distribution over cross-section. 

Analysis of Eq. (1.13) for horizontal channel with _α_ = 1 shows that the specific energy is a function of the flow depth _H_ only, i.e. _Es_ = _Es_ ( _H_ ). From its examination results that _Es_ tends to infinity for _H_ tending either to 0 or to infinity. This means that in the interval ⟨0, ∞) the function _Es_ ( _H_ ) has an extreme minimum point. At this point the following condition resulting from Eq. (1.14) is valid: 



1.1 Basic Definitions 

7 

Then except this point, there are two alternate depths _H_ for which _Es_ ( _H_ ) takes the same values. The depth corresponding to the extreme minimum is _critical depth_ . This depth, designed as _Hc_ , ensures that the flowing stream with flow rate _Q_ has least specific energy or for given specific energy the flow rate is greatest. The critical depth divides the interval ⟨0, ∞) into two parts. The channel flow with _H_ < _Hc_ is so called supercritical or torrential flow, whereas the flow with _H_ > _Hc_ is called subcritical or fluvial one. To distinguish these cases the following dimensionless Froude number is introduced: 



This number, representing the ratio of inertial and gravity forces, is expressed by the average flow velocity _U_ and the celerity of gravity wave in shallow water ( _g H_ )<sup>1/2</sup> . Using the Froude number one can distinguish: 

- critical flow when _Fr_ =1, 

- supercritical flow when _Fr_ > 1, 

- subcritical flow when _Fr_ < 1. 

The subcritical flow is typical form of channel flow. It is characterized by relatively high depths and small velocities. This form of flow is required as the most suitable one in natural channel. The supercritical flow is characterized by relatively small depths and great velocities. In natural conditions it can occur in upper parts of rivers. This kind of flow is typically observed on the weirs of dams. 

Since Eq. (1.13) represents the total mechanical energy related to the assumed datum, then its derivative with regard to _x_ represents local energy grade line slope _S_ . Therefore one can write: 



where _S_ is energy grade line slope or friction slope. The negative sign at right side of Eq. (1.18) takes into account the fact that energy decreases with increasing of _x_ (Fig. 1.4). 

The water flow in open channel can be classified with regard to various criteria. Taking into account the time variability one can distinguish: 

- steady flow, when the flow parameters do not vary in time, 

- unsteady flow when the flow parameters vary in time. 

With the time variation of flow is connected the notion of time-invariant process or system. A channel reach can be considered as a physical system, which is capable to transform the flood wave occurring at the upstream end to the one observed at the downstream end. If the same waves entering the channel at given time intervals produce the same response, the considered channel reach is a time-invariant system. 

1 Open Channel Flow Equations 

8 

It means that its main properties affecting the flow process, such as the shape of cross-sections and hydraulic roughness do not vary in time. In the opposite case, when the channel properties vary in time, the system is called time-variable. 

Steady flows can be further divided with respect to the spatial variability of the parameters. From this point of view one can distinguish uniform and non-uniform flows. A uniform flow is characterized by spatially constant flow parameters such as velocities and depths, so that the water surface and the energy line are parallel to the bottom. Thus uniform flow can occur in prismatic channels only, in which the shape of cross-sections does not vary and the bed slope is constant. In natural channels such kind of flow does not exist. For steady uniform flow the average velocity is given by the well known empirical formulas: 

- The Chézy equation: 



where: 

_CC_ – the Chézy coefficient, 

_R_ – hydraulic radius, 

_s_ – longitudinal channel bed slope, equal to the energy line slope _S_ . 

- The Manning equation 



This equation can be considered as the Chézy equation with _CC_ defined as follows: 



where _nM_ is the Manning roughness coefficient. In SI units this coefficient is expressed in _s_ / _m_<sup>1/3</sup> . 

The depth _Hn_ which satisfies Eqs. (1.19) or (1.20) is called _normal depth_ . In the case of uniform flow, when the flow velocities and wetted cross-sectional areas do not vary, the energy grade line, the hydraulic grade line and bottom line are parallel one another. 

In particular cases it can occur that the normal depth is equal to the critical depth. The channel slope, for which the uniform flow is critical, is called the _critical slope_ (Chanson 2004, French 1985). Usually it is denoted _sc_ . Relation between the normal and critical depths can be used to characterize the channel slope. One can distinguish (Chanson 2004): 

- mild slope when _Hn_ > _Hc_ , 

- critical slope when _Hn_ = _Hc_ , 

- steep slope when _Hn_ < _Hc_ . 

1.1 Basic Definitions 

9 

The non-uniform flow does not satisfy the conditions of uniform flow, so the depths and velocities vary along channel axis. Consequently the bottom, water surface and energy line are not parallel to each other. Depending on the degree of the spatial variability one can distinguish gradually and rapidly varied flows. To explain the essential difference between both types of flow, let us recall the Bernoulli equation (Eq. 1.12). In open channel gradually varied flow the water particles move along nearly straight streamlines. Since the streamlines have insignificant curvature, the cross-sectional surface, orthogonal to the streamline, are nearly flat. It means that they are almost normal to the velocity vectors and the vertical components of velocity do not exist. These assumptions imply that the sum ( _zsl_ + _p_ / _γ_ ) representing the elevation of the hydraulic grade line above the assumed datum, can be considered as constant. Consequently the pressure distribution in the stream flowing in a channel with small bed slope, in which the streamlines are nearly parallel to the bottom, is governed by the hydrostatic law. Conversely, when rapid flow is considered, one needs to take into account the curvature of the streamlines and cross-sections. The law of hydrostatic distribution of pressure along the depth is no longer valid. 

In non-uniform flow the friction slope _S_ is usually also expressed with the Manning formula. Although this formula has been derived for steady uniform flow, it is applicable for non-uniform flow as well. It is assumed that the error generated due to this approximation is small comparing with the one resulting from the estimation of the coefficient _nM_ . The reformed formula (1.20) is used: 



For steady uniform flow the friction slope is constant, whereas for non-uniform flow it varies along channel axis. 

To solve practical open channel flow problems the energy equations written for two neighboring stations is usually applied. For a channel reach presented in Fig. 1.5 it takes the following form: 



where: 

- _hi, hi+_ 1 – elevations of the water surface above the assumed datum in crosssection _i_ and _i+_ 1 respectively, 

- _U_ 1, _Ui+_ 1 – average flow velocities in cross-section _i_ and _i+_ 1 respectively, _S_ – average friction slope between both cross-sections, _Δxi_ – distance between considered stations. 

The average value of the friction slope is determined using its local values in both cross-sections calculated using Eq. (1.22). Equation (1.23) allows us to compute the water surface profile in open channel for steady gradually varied flow. 

1 Open Channel Flow Equations 

10 



**Fig. 1.5** Sketch of a channel reach 

This section covers only basic information on the open channel flow, which is necessary for further presentation of numerical applications. For more comprehensive discussion of the theoretical background for the open channel hydraulics the reader is directed to the works of Akan (2006), Chanson (2004), Chow (1959), French (1985), Henderson (1966), Jain (2000), Singh (1996) and others. 

### **1.2 General Equations for Incompressible Liquid Flow** 

Domination of one component of the velocity vector is a typical attribute of the open channel flow. This feature allows us to consider the flow process as spatially one-dimensional phenomenon. Similarly to the other types of surface water flows, the governing equations are derived from two principles of conservation: 

- momentum conservation law, 

- mass conservation law. 

The derivation can be performed in various ways. The approaches found in the literature differ with respect to the formulation of the principle of conservation, and to the stage at which the one-dimensionality assumption is introduced. For example, the open channel flow equations are very often derived by balancing the fluxes and forces acting on the considered control volume, with an a priori assumption of uniform velocity flow distribution over a channel cross-section. Next, when the governing equations are derived, some additional factors are introduced to correct the balanced quantity. In such a way the correction parameters _α_ or _β_ appear in the 1D dynamic equation. 

A more consistent approach is to derive the unsteady open channel flow equations from general equations of hydrodynamics. It allows us to show clearly that this kind of flow is governed by equations being a particular case of general equations for 3D unsteady flow. In addition, the effects of introduced simplifications and assumptions 

1.2 General Equations for Incompressible Liquid Flow 

11 

can be easily followed. This point of view coincides with the suggestion given by Abbott and Basco (1989). These authors cite Bird, Steward and Lightfoot (1960), who stated: “It is not _. . ._ necessary to formulate a momentum balance (or mass balance for continuity) whenever one begins to work on a new flow problem. In fact, it is seldom desirable to do so. It is quicker, easier and safer to start with the equations of conservation of mass and momentum in general form and to simplify these equations to fit the problem at hand”. Moreover Abbott and Basco (1989) state: “The advantage of this procedure is that when we are finished discarding terms and simplifying the equations (based on intuition, experiments, field data, experience, etc.) we will have available a complete list of assumptions.” This approach will be followed here. 

It is well known that in general case the flow of viscous and incompressible fluid is described by the Navier–Stokes equations and the continuity equation. These equations are derived from the momentum and mass conservation principles, respectively. Although the Navier–Stokes equations describe all forms of flow, in practice they are useful for laminar flow only, while every large scale geophysical surface flow is turbulent (Eagleson 1970). Therefore the open channel flow must be considered as turbulent. In such kind of flow random fluctuations of velocities and pressure are present. Since it is impossible to describe these fluctuations, the instantaneous velocity is expressed in terms of a time-averaged velocity and its random part, according to the Reynolds hypothesis. The same is applied for pressure. Inserting these relations into the Navier–Stokes equations one obtains the Reynolds equations. As a result of this operation an additional tensor of turbulent stresses appears. Applying the Boussinesq concept of the eddy viscosity one obtains the following system of equations (French 1985): 



where: 

_t_ − time, _x_ , _y_ , _z_ − spatial coordinates, _u_ , _v_ , _w_ − components of the velocity vector in _x_ , _y_ and _z_ direction respectively, _ρ_ − water density, _μ_ − coefficient of dynamic viscosity, _μ_<sup>_T_</sup> − coefficient of turbulent viscosity (eddy viscosity), _p_ − pressure, 

1 Open Channel Flow Equations 

12 

- _Fx_ , _Fy_ , _Fz_ − components of gravitational forces in _x_ , _y_ and _z_ direction respectively, 

_Δ_ – Laplace operator. 

The system of Eqs. (1.24), (1.25), (1.26) and (1.27) is formally very similar the system of Navier–Stokes equations. However, it is interpreted in a different way. Eqs. (1.24), (1.25), (1.26) and (1.27) describe the relations between time averaged values of the dependent variable, while the Navier–Stokes equations relate their instantaneous values. Conversely to the coefficient _μ_ depending on the physical properties of the water, the coefficient _μ_<sup>_T_</sup> is a function of the flow turbulence only. As the turbulent diffusion is much more important than the molecular one because _μ_<sup>_T_</sup> ≫ _μ_ (Martin and McCutcheon 1999), is reasonable to neglect the dynamic viscosity. 

The system of Eqs. (1.24), (1.25), (1.26) and (1.27) representing the momentum and mass conservation equations written in general form will be used to derive the equations for open channel flow. 

### **1.3 Derivation of 1D Dynamic Equation** 

Equations (1.23), (1.24), (1.25) and (1.26) can be simplified when the specific features of the open channel flow problem are taken into account. Usually open channel flow can be considered as a propagation of long waves in shallow water. These waves have relatively small amplitudes compared to their lengths so the accelerations and velocities in vertical direction are negligibly small in relation to the accelerations and velocities in horizontal directions. Let us assume the co-ordinate system as shown in Fig. 1.6, in which after Liggett (1975), _x_ corresponds to the direction of the primary flow, _y_ is the horizontal direction normal to primary flow, whereas _z_ is the vertical direction. 

The gravity force is the only force acting along _z_ axis: 



**Fig. 1.6** Assumed system of co-ordinates 



<!-- Start of picture text -->
z<br>H(x,y,t)<br>y<br>h(x,y,t)<br>ϕ<br>Z(x,y) x<br>datum<br>bottom<br><!-- End of picture text -->

1.3 Derivation of 1D Dynamic Equation 

13 

Consequently Eq. (1.26) takes the following form: 



Integration of this equation with regard to _z_ from the bottom to the water surface (Fig. 1.6) 



yields: 



Since at the water surface the pressure is equal to the atmospheric one _p_ ( _h_ )= _Pa_ then the following formula representing pressure variation along _z_ axis accordingly to the hydrostatic pressure law, is obtained: 



where: 



_ρ_ − water density, 

_g_ – acceleration due to gravity, 

_h_ – elevation of the water surface above the datum, 

_Z_ – elevation of the bottom above the datum, 

_z_ – vertical co-ordinate. 

Let us assume that the velocity vector is parallel to _x_ axis – it has one component only _u_ = _u_ ( _z_ , _x_ , _t_ ). Consequently Eq. (1.25) for the component _v_ disappears, whereas Eq. (1.24) becomes: 



In addition, let us assume that the channel bed is inclined towards _x_ axis and its slope is given by the angle _ϕ_ (Fig. 1.6). The only force acting along _x_ axis is the component of the gravitational force parallel to the bottom: 



For a small bottom slope which is usually assumed for open channels (see Section 1.1), one has sin( _ϕ_ ) ≈ tg( _ϕ_ ). Then the component _Fx_ is expressed as: 

1 Open Channel Flow Equations 

14 



where _∂Z_ / _∂x_ accordingly to Eq. (1.2) is the longitudinal channel bed slope. With Eqs. (1.32) and (1.35), Eq. (1.33) is rewritten as follows: 



In turbulent open channel flow the vertical velocity distribution is rather uniform, so the actual velocity _u_ ( _x_ , _z,t_ ) can be replaced by the depth-averaged one _U_ ( _x_ , _t_ ). Let us introduce: 

- the average horizontal velocity _U_ ( _x_ , _t_ ): 



where _H_ = _h_ − _Z_ designates the depth; 

- the deviation _u_<sup>′′</sup> ( _z_ ) of the actual velocity from the average one (Fig. 1.7): 



From Eq. (1.37) results the following condition: 



<!-- Start of picture text -->
z<br>h<br>H u(z)<br>u ( z )<br>U<br>datum<br>Z<br><!-- End of picture text -->

**Fig. 1.7** Actual and averaged distribution of horizontal velocity _u_ along the vertical axis 

15 

1.3 Derivation of 1D Dynamic Equation 



Averaging the horizontal velocity over depth allows us to eliminate the variability in _z_ direction and consequently to reduce the number of dimensions. To do it, Eq. (1.36) must be integrated over depth: 



The integration limits, i.e. the water stage _h_ and the bottom elevation _Z_ , in a general case are functions of the horizontal spatial coordinates. Therefore while integrating Eq. (1.40) we will face a problem of differentiation inside the integral with variable limits. According to the Leibniz rule (Korn and Korn 1968, McQuarrie 2003) in such a case the differentiation of any function _φ_ is carried out as follows: 



Let us integrate subsequent terms of Eq. (1.40). The first term is integrated as follows: 



If we: 

- make use of the definition (1.37), 

- assume that the channel bed does not change its position with time, 

- assume that the velocity at the water surface is equal to the average one then Eq. (1.42) will take the following final form: 



The integral of the second term with Eq. (1.38) is rearrangered to the form: 

16 

1 Open Channel Flow Equations 



Developing the square of sum and assuming that the flow velocities at the water surface and at the channel bottom are equal to the average velocity _U_ , one obtains: 



Integrals in the brackets are calculated term by term as follows: 





The last integral at the right hand side of Eq. (1.45) � _h_ ( _u_<sup>′′</sup> )<sup>2</sup> _dz_ cannot be cal- _Z_ 

culated since the actual distribution of the velocity over the depth is unknown. However, a rough estimation of this integral in relation to the integral (1.46) can be attempted. To this end let us assume a hypothetical vertical distribution of _u_ ( _z_ ) as presented in Fig. 1.8. 

Over the entire depth the deviation of actual velocity is taken as _u_<sup>′′</sup> ( _z_ ) = ±0.2 _U_ . Then we have: 



The result of integration shows that even for the assumed significant nonuniformity of the vertical distribution of velocity, the value of integral (1.48) constitutes only 4% of the value of integral (1.46). To take into account these integral we can consider it as a fraction of integral (1.46) and to add its value to (1.46). This allows us to write: 

1.3 Derivation of 1D Dynamic Equation 

17 



<!-- Start of picture text -->
z<br>h<br>0,5  H<br>H<br>u " = 0,20  U<br>0,5  H<br>u " = – 0,20  U<br>Z<br>U<br>datum<br><!-- End of picture text -->

**Fig. 1.8** Assumed hypothetical vertical distribution of flow velocity 



In this equation we recognize 



as a correction parameter. Coming back to Eq. (1.45) we have: 



Developing of the derivative in Eq. (1.51) yields: 



Neglecting the difference of the last two terms as small value, which additionally can be corrected by chosen value of _β_ , the integral of the second term of Eq. (1.40) takes its following final form: 



1 Open Channel Flow Equations 

18 

Introduction of the correction factor _β_ requires a comment. Assumption of the uniform flow velocity distribution instead of the actual one always requires a correction of the conservative quantity, which depends on the velocity. In the case of the discrete energy equation (1.23) applied for channel flow, comparison of the actual kinetic energy with that calculated with the average velocity shows that it is necessary to introduce the correction factor _α_ , given by Eq. (1.15). This coefficient was introduced into the dynamic equation of the Saint Venant system by Chow (1959). However, Abbott (1979) in this same equation introduces the factor _β_ , which corrects the momentum. It is worth emphasizing that usually at first the unsteady flow equations are derived assuming a priori one dimensionality and afterwards the effect of averaging is corrected. In the derivation from general equations as we have just applied, the correction factor appears naturally as a result of the averaging process. Such a way of derivation ensures a simple interpretation of the corrective parameter _β_ and explains the real reasons of its appearance. It corrects the balance of momentum affected by the average flow velocity introduced instead of the actual velocity distribution over the cross-sectional area. This parameter allows us to include the estimated value of integral (1.48), impossible to be calculated directly. For _u_ ( _z_ )= const., i.e. when _u_ "( _z_ ) = 0 for _Z_ ≤ _z_ ≤ _h_ one obtains _β_ = 1. 

The terms of Eq. (1.40) representing gravitation and pressure are integrated as follows: 





The term describing the turbulent diffusion of momentum in _x_ direction takes the form: 



where _μ_<sup>_D_</sup> is the coefficient of dispersive transport of momentum in _x_ direction. It represents the combined effect of the turbulent viscosity with coefficient _μ_<sup>_T_</sup> and vertical velocity averaging. This is an analogous situation to the one discussed previously, where integrating the term of velocity advection led to the correction factor _β_ (see Eq. 1.50). 

The term describing the momentum transfer in vertical is integrated as follows: 

1.3 Derivation of 1D Dynamic Equation 

19 



The terms in parentheses are the tangential stresses at the water surface and at the bottom, respectively. The former ones are caused by the action of the wind blowing above the water surface in direction parallel to _x_ axis. It generates the stresses which can be estimated using the following formula (Hervouet 2007, Singh 1996): 



where: 

- _a_ – empirical coefficient depending on the density and viscosity of air and on the roughness of the water surface, 

- _W_ – component of the wind velocity vector acting along the channel axis. 

In many practical cases the wind-generated stresses are negligible. They can be important for example in lower parts of river, where the bed slope is typically small. The second term of Eq. (1.57) describing the stresses at the bottom is expressed by the well known formula (Chanson 2004): 



Inserting Eqs. (1.58) and (1.59). In Eq. (1.57) yields: 



Finally, the integration of Eq. (1.40) allows us to present it in the form: 



After dividing both sides by the depth _H_ , which is always non-zero, one obtains: 



Equation (1.62) is the dynamic equation for 1D unsteady open channel gradually varied flow. This equation, derived from Eqs. (1.23), (1.24), (1.25) and (1.26), 

1 Open Channel Flow Equations 

20 

contains all the significant components which determine the flow process. The only process omitted in the derivation is the lateral water inflow distributed along the channel. 

### **1.4 Derivation of 1D Continuity Equation** 

Similarly to the dynamic equation, the continuity equation for one-dimensional flow can be derived from the general three-dimensional from. Let us assume a uniform motion in _y_ direction. Then Eq. (1.27) takes a simpler form, which must be integrated over the depth from the bottom _Z_ ( _x_ ) to the surface _h_ ( _x_ ): 



The terms in parentheses are integrated separately giving: 



where _w_ ( _h_ ) and _w_ ( _Z_ ) are the vertical velocities at the water surface and at the bottom, respectively. These velocities can be found from the kinematic condition at each of the limits, which says that a particle laying at the limit moves together with the limit. Then: 





The total derivatives _Dh_ / _Dt_ and _DZ_ / _Dt_ represent the velocities of traveling water surface and bottom in the vertical direction, respectively: 



1.5 System of Equations for Unsteady Gradually Varied Flow in Open Channel 

21 

In many geophysical flows the motion of the water surface in the vertical direction is caused by external sources like rain, evaporation or lateral inflow. This fact must be taken into account in Eq. (1.68), which should be modified as follows: 



where _δ_ is the source term representing additional inflow. Substitution of Eqs. (1.69) and (1.70) in Eq. (1.65) yields: 



The sum _I_ 1 + _I_ 2, is equivalent to the integral (1.63) and can be written as: 



Since accordingly to Eq. (1.1) we have _h_ = _H_ + _Z_ then Eq. (1.72) becomes: 



In such a way the 1D continuity equation (1.73) for open channel flow was derived from 2D equation via its integration along the vertical direction. 

### **1.5 System of Equations for Unsteady Gradually Varied Flow in Open Channel** 

Integration of the system of equations (1.24), (1.25), (1.26) and (1.27) over the depth with the assumption of uniform flow in _y_ direction allowed us to derive 1D dynamic and continuity equations: 



The above system of partially differential equations describes unsteady flow in an open channel. Let us recall the major assumptions introduced during the derivation: 

1 Open Channel Flow Equations 

22 

- Motion of water is gradually varied, 

- Channel bed slope is small, 

- Flow is considered as one dimensional process, 

- Velocity distribution over depth is uniform, 

- Pressure is governed by the hydrostatic law, 

- Friction slope is estimated as for the steady flow, 

- Lateral inflow does not influence the momentum balance. 

Since Eqs. (1.74) and (1.75) are written per unit channel width, this system is valid for a wide rectangular channel. The parameter _β_ in dynamic equation (1.74) occurred as a result of the integration over depth. It corrects the error in momentum balance introduced by velocity averaging. It appeared naturally from the Leibniz rule applied to calculate the integrals with variable limits. 

Usually, in Eq. (1.74) the last three terms are neglected as less important compared to the others. Dimensionless analysis shows that longitudinal dispersion of momentum is insignificant (French 1985). Similarly, in most cases the temporal and spatial variability of the atmospheric pressure and the wind velocity do not influence remarkably the river flow. Therefore the terms representing them can be omitted. If in addition we assume _β_ = 1 and _δ_ = 0, introduce the bottom slope _s_ defined by Eq. (1.7) and the friction slope _S_ , which for flow per unit width is: 



then Eqs. (1.74) and (1.75) become: 



In practical applications it is more convenient to use the flow rate and water stage instead of depth and velocity as the dependent variables. The equations with new variables can be derived as previously from Eqs. (1.24), (1.25), (1.26) and (1.27), with the same assumptions. However, they should be integrated not only with regard to depth but with regard to the channel width as well. Taking into account that the velocity is averaged over the entire wetted cross-sectional area _A_ , the following system of equations is obtained: 



1.5 System of Equations for Unsteady Gradually Varied Flow in Open Channel 

23 

where: 

- _U_ – cross-sectional average flow velocity, 

- _h_ – water level above assumed datum defined by Eq. (1.1), 

- _A_ – cross-sectional area, 

- _Q_ – flow rate 

_q_ – lateral inflow per unit length of a channel. 

Omitting the lateral inflow _q_ we obtain the unsteady open channel flow equations in the form proposed in 1871 by Barré de Saint-Venant to describe the process of propagation of the flood waves (Chanson 2004). After him, these equations are known in literature as the system of Saint Venant equations. 

The dynamic equation (1.79) is similar to Eq. (1.77). However, the variables involved in Eq. (1.79) are related to the whole cross-section, and not to the unit width. For this reason, their interpretation is different. Now _U_ is the velocity averaged over the cross-section: 



whereas _S_ is the friction slope, which for a channel cross-section is given by formula: 



where _R_ is hydraulic radius. 

Similarly, the correction parameter _β_ is related to the entire cross-section. Now, its general definition resulting from integration of the convective term _u∂u_ / _∂x_ over the whole cross-section is following: 



where _u_<sup>′′</sup> = _u_ – _U_ is the difference between the actual velocity _u_ at any point of the cross-section and the averaged flow velocity _U_ . 

The correction factor _β_ , usually applied in dynamic equation of the Saint Venant system, is given as (Abbott 1979, Liggett 1975): 



This factor called the Boussinesq coefficient (Chanson 2004) represents the ratio of the actual momentum and the momentum calculated with the averaged velocity _U_ . If instead of _u_<sup>′′</sup> we substitute in Eq. (1.83) the expression _u_<sup>′′</sup> = _u_ − _U_ then 

1 Open Channel Flow Equations 

24 



Since with Eq. (1.81) the second term at the right hand side vanishes, then Eq. (1.85) becomes Eq. (1.84). As one can see, integration of the momentum equation over depth using the Leibnitz rule gives another possible viewpoint on introduction of the momentum correction while averaging of the flow velocity. 

Eliminating both depth and average flow velocity from Eqs. (1.79) and (1.80) can be carried out using Eqs. (1.1) and (1.10). In addition, a constant position of the channel bed is assumed so _∂Z_ / _∂t_ = 0. Since the wetted cross-section area _A_ is a function of the water stage _h_ , then one can write: 



These assumptions allow us to reform both equations of unsteady flow to obtain: 



where _B_ is channel width at the water surface level. Equations (1.87) and (1.88) constitute the most popular mathematical model of the unsteady open channel flow. It should be added that the system of Saint Venant equations is expressed in many forms depending on the assumed dependent variables, geometry of a channel and other factors taken into account. For a systematic review of these forms see Singh (1996). 

### **1.6 Steady Gradually Varied Flow in Open Channel** 

In many practical applications the steady and gradually varied flow in open channels must be considered. Typical problem connected with this kind of flow is the determination of the flow profile behind a dam. 

The governing equation describing steady gradually varied flow can be obtained in different ways. The manner of derivation depends on our preferences. We can write balance equation directly for the steady gradually varied flow with introduced a priori simplifying assumptions or to derive them from the Saint Venant equations, describing a more general case of unsteady gradually varied flow. Both approaches will be shown in the following sections. 

25 

1.6 Steady Gradually Varied Flow in Open Channel 

### **_1.6.1 Derivation of Governing Equation from the Energy Equation_** 

Let us consider two neighboring cross-sections enclosing a channel reach of length _dx_ as shown in Fig. 1.9. At the upstream end the depth is equal to _H_ and the average flow velocity is equal to _U_ , whereas at the downstream end we have the depth _H_ + _dH_ and the velocity _U_ + _dU_ , respectively. The Bernoulli equation takes the following form: 



where: 

- _E_ – total mechanical energy above the assumed datum, 

_Z_ – bed elevation with regard to the datum, 

_H_ – depth, 

- _U_ – average flow velocity, 

- _s_ – bottom slope, 

- _S_ – friction slope, 

- _g_ – gravitational acceleration, 

- _α_ – energy correction factor. 



<!-- Start of picture text -->
E(x)<br>z<br>α U 2 S . dx<br>2 g<br>α( UdU +) 2<br>2 g<br>H<br>H + dH<br>s<br>Z<br>Z–s . dx<br>datum<br>dx x<br>U<br>U + dU<br>bottom<br><!-- End of picture text -->

**Fig. 1.9** Schematic representations of a channel reach 

26 

1 Open Channel Flow Equations 

The square velocity at the downstream end can be expressed using an approximate formula, since the term ( _dU_ )<sup>2</sup> can be omitted as significantly smaller than other terms in the expression ( _U_ + _dU_ )<sup>2</sup> : 



Using this relation Eq. (1.89) can be rearranged to the following form: 



The second term at the right-hand side of Eq. (1.90) can be expressed as follows: 



Substitution of Eq. (1.91) in Eq. (1.90) and using the definitions (1.1) and (1.2) yields: 



This is differential representation of the energy conservation principle. Equation (1.92) has general character, since it holds for both prismatic and non-prismatic channels. 

Equation (1.92) can be reduced to the standard form of the steady gradually flow equation for a prismatic channel, in which the depth is dependent variable. To this end let us introduce relation (1.1), which allows us to rewrite Eq. (1.92) as follows: 



Let us differentiate the left-hand side of Eq. (1.93). Assuming that _Q_ = const. one obtains: 



where _B_ is channel width at the water surface. Equations (1.94) and (1.22) are substituted in Eq. (1.93). Simple rearrangement yields: 



1.6 Steady Gradually Varied Flow in Open Channel 

27 

One can assume that in a single channel the direction of the steady flow coincides with the positive direction of _x_ axis. Then the modulus in last term of Eq. (1.95) can be omitted. The next assumption concerns the flow velocity distribution over the cross-section of the channel. It is considered as quasi-uniform, so that one can assume _α_ = 1. Moreover, for a rectangular cross-section the second term in brackets represents the square of the Froude number since: 



Substitution of Eqs. (1.2), (1.22) and (1.96) in Eq. (1.95) yields: 



In such a way the classic ordinary differential equation describing the water surface profile for a steady gradually varied flow is obtained. However, one should remember that it holds only for prismatic channel with _Q_ = const. 

### **_1.6.2 Derivation of Governing Equation from the System of Saint-Venant Equations_** 

The steady gradually varied flow can be considered as a particular case of the unsteady gradually varied flow. For this reason it should be possible to derive the governing equations from the system of Saint Venant equations (1.87) and (1.88), previously discussed. This manner of derivation seems to be more instructive, since it clearly shows the direct relations between the derived equations which govern the steady flow and the fundamental principles of mass and momentum conservation used in open channel flow modeling. In addition, such approach allows us to derive the most general form of the steady flow equations. 

The Saint Venant equations (1.87) and (1.88) can be rewritten for a channel with variable cross-sections and with non-uniform velocity distribution over the crosssections as follows: 



where: 

_t_ – time, 

_x_ – longitudinal distance, 

_h_ – water surface elevation, 

1 Open Channel Flow Equations 

28 

_q_ – lateral inflow, 

_β_ – momentum correction factor _S_ – friction slope given by Eq. (1.22). 

For steady flow one obtains: 



Therefore all the functions depend on the variable _x_ only and consequently Eqs. (1.98) and (1.99) become ordinary differential equations. They take the following forms: 



Equation (1.103) can be rearranged to a form more suitable for integration. To this end both its sides are divided by _g_ · _A_ . This yields: 



Taking into account the definition of the average flow velocity in the channel cross-section (1.9), the first term of Eq. (1.104) is differentiated as: 



Consequently Eq. (1.104) becomes: 



Substitution of Eqs. (1.9) and (1.102) into Eq. (1.106) leads to: 



Therefore, in the case of steady gradually varied flow the water surface profile is described by the following equations: 



1.6 Steady Gradually Varied Flow in Open Channel 

29 



where 



Note that _E_ represents the total energy of the flowing stream related to the assumed datum. A comment is needed to explain the problem of the correction of the conservative quantity represented by the governing differential equation. This correction is introduced when the locally variable velocity over a cross-section is replaced by the average velocity. If the momentum conservation principle is applied as it is done while deriving the dynamic equation in the Saint Venant system, then the correction parameter _β_ should rather be used. On the other hand, if the energy conservation principle is applied, then the correction parameter _α_ should be used. However, during the derivation of the steady flow equation from the system of Saint Venant equations, the dynamic equation (1.99) is transformed into Eq. (1.109) representing the conservation of energy. Therefore, from now on in the governing equation of the steady flow the correction parameter _α_ will be used. Note that when Eq. (1.92) is derived directly from the mechanical energy conservation principle, the parameter _α_ arises in this equation in natural way. 

Since Eqs. (1.108) and (1.109) were derived from the system of Saint Venant equations, they should be applicable for all types of open channels. Indeed, as it will be shown later, numerical integration of Eq. (1.109) by the implicit trapezoidal rule leads to the well known step method, commonly applied in practice. Usually the step method is derived directly from the principle of energy conservation applied for two neighboring cross-sections lying along channel axis, i.e. for discrete system. 

Equation (1.109) can be recast into Eq. (1.97), which has been previously derived for rectangular channel from the energy principle and is more familiar in open channel hydraulics. To this order using Eq. (1.108) the spatial derivative of the mechanical energy is transformed to the form: 



As previously, one can assume that the flow direction coincides with the positive direction of _x_ axis, so that the modulus in the friction slope (Eq. 1.82) is omitted. Substitution of Eqs. (1.82) and (1.111) with Eq. (1.1) in Eq. (1.109) yields: 



1 Open Channel Flow Equations 

30 

For constant flow discharge along the channel axis ( _Q_ = const.), i.e. when the lateral inflow is neglected ( _q_ = 0), one obtains a simpler version of Eq. (1.112): 



For a rectangular channel with longitudinal bed slope _s_ , instead of the water stage _h_ the flow depth _H_ can be introduced. To this end the water level _h_ expressed by Eq. (1.1) is substituted in Eq. (1.113) resulting in the following equation: 



Now, introducing the definition of the longitudinal bed slope (1.2) and the Froude number (1.17) into Eq. (1.114) one obtains: 



Note that for _α_ = 1 Eq. (1.115) coincides with Eq. (1.99). In such a way the classic form of the governing equation for steady gradually varied flow in prismatic open channel was derived directly from the system of Saint Venant equations. 

### **1.7 Storage Equation** 

In hydraulic practice one has often to consider a river flowing through reservoir behind a dam. In such a case the dimensions of wetted cross-sections increase significantly, whereas the average flow velocities decrease. Location of a reservoir along the river course influences propagation of flood waves, reducing their peaks flows and volumes. For flood routing purposes it is sometimes reasonable to neglect spatial variability of the flow parameters and to reduce formally the reservoir to a point characterized by time dependent capacity of retained water only. Such assumption leads to the so-called storage equation. 

To derive the storage equation let us consider the situation shown in Fig. 1.10. The capacity of the reservoir behind the dam depends on the topography of the valley and on the water stage kept in the reservoir _h_ ( _t_ ). 

If the width and depth of the reservoir are not too large, meaning that the flow process is still one dimensional, the flood wave propagating through reservoir can be modeled using the system of Saint Venant equations. However, if we are not interested in considering the internal distribution of the velocity and pressure fields 

1.7 Storage Equation 

31 



<!-- Start of picture text -->
I ( t )<br>V ( h )<br>h ( t )<br>O ( t )<br>I datum<br>O<br>t<br>t<br>I ( t )<br>O ( t )<br>F ( h )<br><!-- End of picture text -->

**Fig. 1.10** Scheme of a retention reservoir 

in the reservoir, the problem of reservoir’s dynamic can be reduced to the problem of mass conservation only, considered at the global scale. In such a case we neglect the flow velocities and the behavior of the reservoir will be described by one dependent variable _h_ ( _t_ ) only. 

To obtain the governing equation let us apply the mass conservation principle to a control volume constituted by the entire capacity of the reservoir, limited by an appropriate control surface. The mass conservation principle means that the time variation of the mass contained in reservoir is caused by the net flow through the control surface only. This statement is expressed as follows: 



where: 

_t_ – time, 

_ρ_ – water density, 

_V_ – control volume, 

_σ_ – control surface, 

**U** – vector of flow velocity, 

**n** – unit vector normal to surface _σ_ and oriented towards outside of volume. 

If we assume constant water density ( _ρ_ = const), then Eq. (1.116) will express the conservation of the water volume in reservoir: 



1 Open Channel Flow Equations 

32 

The first term of equation represents the time variation of volume since: 



The second term represents the net exchange of the water in reservoir with its surrounding. Taking into account the main ways of exchange, this term can be expressed as a sum the following components: 



where: 

_I_ ( _t_ ) – river inflow, _O_ ( _t_ ) – river outflow, _E_ ( _t_ ) – evaporation from reservoir surface, _P_ ( _t_ ) – rainfall on reservoir surface, _G_ ( _t_ ) – infiltration through reservoir bottom. 

Substitution of Eqs. (1.118) and (1.119) in Eq. (1.117) yields: 



This equation, known as the storage equation, represents the volume balance of water in the reservoir. Note that this approach leads to the equations involving the derivative with regard to time only. Equation (1.120) is called the volume balance equation (Singh 1996). 

For practical reasons the storage equation is more often expressed in terms of the water level instead of the volume. The following relation: 



where _F_ ( _h_ ) is area of reservoir at the water level, allows us to rewrite Eq. (1.120) as follows: 



Solving this equation one obtains the function _h_ ( _t_ ) representing time variation of the water level in reservoir caused by the components of balance taken into account in Eq. (1.122). 

Equation (1.122) can be derived in other way, directly from the differential continuity equation (1.80). This manner of derivation will be used in Chapter 9 while discussing the lumped flood routing models. 

1.8 Equation of Mass Transport 

33 

### **1.8 Equation of Mass Transport** 

### **_1.8.1 Mass Transport in Flowing Water_** 

The rivers are recipients of many substances originating either from natural geophysical processes or from human activity. For instance during the water run-off from a catchment small mineral particles are rinsed, which together with the river water form a mixture having the features of solution. In a similar way various chemical substances applied in agriculture are delivered to the rivers and streams, including fertilizers, herbicides and pesticides. An important natural constituent of water is the dissolved oxygen, playing fundamental role in aquatic life. All these substances are readily dissolved in water but they do not react with water. 

The substances present in the flowing water, which for the sake of shortness will be referred to as pollutants, can be divided into active and passive. Active pollutants have significant effect on the density and viscosity of water, thus changing the hydrodynamic conditions of flow. In such case, the equations describing pollutant transport are coupled with the flow equations and should be solved simultaneously. On the other hand, the passive pollutants have negligible influence on flow conditions, and consequently allow for splitting and separate solution of the hydrodynamic and transport problem. 

The pollutants can be also classified with respect to their behaviour in water, into conservative and non-conservative ones. A conservative pollutant does not change its overall mass in time, whereas the non-conservative does. An example of conservative pollutant is the chloride ion. The changes of mass of pollutant may result from its natural properties (for instance radioactive materials), or from chemical and biological processes in which the pollutant is involved (e.g. dissolved oxygen). In the following part we will focus on the transport of passive pollutants, both conservative and non-conservative. 

Let us introduce some basic definitions. The quantity of constituent dissolved in water can be expressed by: 

- the concentration being the ratio of its mass to the volume of water in which it is dissolved 



- the total load in the considered volume of water 



where: 

_c_ – concentration, i.e. mass of considered pollutant per unit volume of water, _Mp_ – mass of considered pollution, _V_ – volume of water. 

1 Open Channel Flow Equations 

34 

The concentration is usually expressed in kg·m<sup>−3</sup> , mg·dm<sup>−3</sup> , or g·m<sup>−3</sup> . The load of pollutant is expressed in mass units, i.e. kg and its derivatives. In the stream charcterized by the discharge _Q_ , the flow rate of dissolved constituent _φ_ is used, instead of the load _Mp_ . It is defined as follows: 



where _φ_ represents the mass of pollutant flowing through the wetted cross-sectional area normal to the channel axis per unit time. 

The intensity of mass transport is defined by the flux, which expresses the mass of pollutants flowing through the unit area of a channel cross-section normal to the velocity vector and per unit time. Then its units are kg·m<sup>−2</sup> ·s<sup>−1</sup> and their derivatives. 

The transport of any pollutant dissolved in the flowing water is considered as a superposition of two fundamental physical processes: advection and diffusion. Advection is the movement of the constituent dissolved in water due to the motion of water itself. Accordingly to Eq. (1.125), the advective flux is expressed as follows: 



where: 



For constant flow velocity advection does not disturb the initial distribution of the concentration over the channel axis (Fig. 1.11). The concentration distribution moves with the average velocity of the stream, so that after time _t_ 1 it takes the position which is shifted with regard to initial one by the value of _L_ = _U_ · _t_ 1. The shape of initial distribution will change for variable flow velocity. 

Advection is a reversible process. It means that for the opposite flow conditions imposed at _t_ = _t_ 1 the distribution of concentration _c_ ( _x_ , _t_ = _t_ 1) will reach the shape and position of initial distribution _c_ ( _x_ , _t_ = 0). 



<!-- Start of picture text -->
c<br>c ( x , t = 0) c ( x , t = t 1)<br>L = U . t1) x<br><!-- End of picture text -->

**Fig. 1.11** Advective transport of initially imposed distribution of concentration with constant flow velocity _U_ 

35 

1.8 Equation of Mass Transport 

The second fundamental transport process is the mass diffusion, which causes the mass of dissolved constituent to move from places of higher concentration towards diminishing concentration. This phenomenon is governed by the Fick’s Ist law of diffusion (Baehr and Stephan 2006). Accordingly to this law the diffusive flux of mass, for instance in _x_ direction, is expressed as: 



where: 

_φx_ – the diffusive flux of mass in _x_ direction, _∂c_ / _∂x_ – gradient of concentration, _D_<sup>_M_</sup> – coefficient of molecular diffusion. 

The negative sign at the right hand side of Eq. (1.127) ensures a positive mass flux in the direction of decreasing concentration _c_ . 

The molecular diffusion is an important transport process when water is at rest or during laminar flow. The value of the diffusion coefficient depends on the physical properties of the solution and its temperature. Typical values of the diffusion coefficient are 10<sup>−10</sup> to 10<sup>−9</sup> m<sup>2</sup> ·s<sup>−1</sup> in liquids (Baehr and Stephan 2006). Conversely to advection, the process of diffusion is irreversible. It means that there is no possibility to obtain the initial concentration distribution by reversing flow conditions. 

As we will see later, an equation similar to the Fick’s law can be applied to describe other processes in flowing stream, which in physical sense have nothing in common with the molecular diffusion. However, the effects of these processes can be considered as similar to the effects of diffusion. Such a case is known as the diffusive analogy, although the coefficient of proportionality does not depend on the physical properties of the considered solution. 

### **_1.8.2 Derivation of the Mass Transport Equation_** 

In the control volume _V_ limited by the control surface _σ_ , the mass of constituent dissolved in the water body can vary in time due to the flux through the surface _σ_ or due to the chemical processes taking place in water, which increase or decrease the mass of constituent. This statement is written as: 



where: 

_c_ – concentration, 

_V_ – control volume, 

36 

1 Open Channel Flow Equations 

_σ_ – control surface, 

**q** – mass flux through the surface _σ_ , 

- **n** – unit vector normal to the surface _σ_ and oriented out of the control volume, 

- _δ_ – density of internal source/sink, which represents the intensity of generation or decay of dissolved constituent. 

Using the Gauss-Ostrogradski theorem (Korn and Korn 1968, McQuarrie 2003), Eq. (1.128) is rewritten as: 



Next, one can substitute Eqs. (1.126) and (1.127) describing the advection and diffusion fluxes into (1.129). Using a more general vector notation one obtains: 



where: 

**U** = ( _u_ , _v_ , _w_ )<sup>_T_</sup> − velocity vector, 

**D**<sup>_M_</sup> – tensor of molecular diffusion having non-zero elements only on main diagonal. 

In scalar form Eq. (1.130) becomes: 



In such a way the 3D advection-diffusion transport equation was derived. It holds for laminar flow only, since the molecular diffusion was taken into consideration. As mentioned earlier, every large-scale flow of surface waters is turbulent (Eagleson 1970), which means that random fluctuations of the velocities and concentration arise. Similarly to the Navier–Stokes equations considered in preceding Section 1.2, the Reynolds approach has to be applied. Therefore it is assumed that the instantaneous values of velocities and concentrations can be expressed as sums of their time-averaged values and fluctuations. The instantaneous value of concentration can be expressed by a formula: 



where _c_ ¯ is the time averaged value of concentration and _c’_ is the fluctuation of concentration from its averaged value. Substituting these relations in Eq. (1.131) and taking into account the rules of operation on the averaged values one obtains: 

1.8 Equation of Mass Transport 

37 



In Eq. <u>(1.133)</u> the bars designate the averaged values, whereas the terms _u_<sup><u>′</u></sup> · _c_<sup><u>′</u></sup> , _v_<sup><u>′</u></sup> · _c_<sup><u>′</u></sup> , _w_<sup><u>′</u></sup> · _c_<sup><u>′</u></sup> containing the products of fluctuations of both velocity and concentration represent the effect of averaging of the advection transport. It is an additional effect of the turbulent transport. Similarly to the turbulent transport of momentum in the Navier–Stokes equations these terms can be expressed using the afore-mentioned diffusive analogy. It implies that the turbulent advective transport can be described with formulas analogous to the Fick’s law (1.127): 







in which the coefficients _D_<sup>_T_</sup> _x_<sup>,</sup><sup>_DT_</sup> _y_<sup>,</sup><sup>_D_</sup> _z_<sup>_T_are called the coefficients of turbulent mass</sup> diffusion. Eq. (1.133) combined with Eqs. (1.134a), (1.134b) and (1.134c) takes the following form: 



The experiments show that the turbulent transport and diffusivity is much greater than the molecular ones (Martin and McCutcheon 1999). Since _D_<sup>_T_</sup> ≫ _D_<sup>_M_</sup> therefore the molecular diffusion can be neglected. In the following the bars denoting the time-averaged values will be omitted. However, from this moment it should be remembered that the velocities and concentration must be interpreted as averaged values. Consequently Eq. (1.135) is rewritten in the following final form: 



1 Open Channel Flow Equations 

38 

Equation (1.136) is 3D advection-diffusion transport equation which is valid for the turbulent flow. Then, if we know the 3D velocity field and we are able to estimate the coefficients of turbulent diffusion, this equation can be solved. For the imposed initial-boundary conditions one obtains the function _c(x_ , _y_ , _z_ , _t)_ . Although such solution is possible, it is not a trivial problem. In open channel hydraulic such approach is rarely applied. Instead, one makes use of the particular properties of the open channel flow to simplify Eq. (1.136). 

Relatively small depths of rivers compared to widths and lengths cause that mixing process in the vertical direction is more rapid than for the other directions normal to the channel axis. Consequently, the vertical distribution of concentration becomes relatively uniform not far away from the source of pollution. It allows us to eliminate vertical dimension from Eq. (1.136). This elimination is carried out by its integration over depth. 

Let us integrate Eq. (1.136) with regard to _z_ changing from the channel bottom to the water stage: 



It is assumed that any function in Eq. (1.137) is averaged vertically using the formula applied previously for the components of flow velocity. Then we will apply the following: 





where _f”_ is the deviation of the actual value of function _f_ from its averaged value _F_ . All functions are replaced accordingly to the formula (1.139) and afterwards the subsequent integrals in Eq. (1.137) are calculated as in the case of the Reynolds equations. Finally, the following 2D advection-diffusion transport equation is obtained: 



1.8 Equation of Mass Transport 

39 

where: 

- _C_ – vertically averaged concentration, 

- _U, V_ – vertically averaged the velocity vector components in _x_ and _y_ direction, respectively. 

Equation (1.141) has been derived with the assumption that no fluxes through the limits of the water layer exist: 



In the case of mass transport in open channels such assumption is admissible. In Eq. (1.141) two additional terms, _u_<sup><u>′′</u></sup> · _c_<sup><u>′′</u></sup> and _v_<sup><u>′′</u></sup> · _c_<sup><u>′′</u></sup> occurred. These terms represent additional mass fluxes, resulting from the vertical averaging of the variable velocity and concentration functions. They are expressed, in a similar manner to the previously considered turbulent transport, with formulas analogous to the Fick’s law: 



where _D_<sup>_D_</sup> _x_<sup>and</sup><sup>_DD_</sup> _y_<sup>arecalledcoefficientsofdispersionin</sup><sup>_x_and</sup><sup>_y_direction,</sup> respectively. Substitution of Eqs. (1.144a) and (1.144b) in Eq. (1.142) yields: 



The coefficients of dispersion _D_<sup>_D_</sup> _x_<sup>and</sup><sup>_DD_</sup> _y_<sup>represent the effect of vertical averag-</sup> ing of velocity and concentration. To better explain the concept of their introduction let us follow the imagination of flow and mass transport processes in open channel basing on idea proposed by Cunge et al. (1980) and presented in Fig. 1.12. 

If the velocity distribution is non-uniform in the vertical direction and the turbulent diffusion does not exist ( _D_<sup>_T_</sup> = 0), then the initial distribution of concentration is traveling along _x_ axis with shape deformation cased by the variable velocity only. Since the particles in the vicinity of the bottom move slower than those in the upper part of the stream, the initial distribution becomes deformed in space as it is shown by the dashed lines in Fig. 1.12. When the flow is turbulent, the rectangular distribution is additionally subjected to increased dispersion caused by random fluctuations 

1 Open Channel Flow Equations 

40 



<!-- Start of picture text -->
t = 0 u = u(z) t = t 1<br>........ . ................................. . ........... . ................................. . ......... .... . ........................... . ....... . ........................ . ................ . .................................. . ................... . ............ . ................................... . ................. . .......................................... . ............................... . .................................... . ........ . ......... . ...... . .<br>U<br><!-- End of picture text -->

**Fig. 1.12** Illustration of dispersion concept in open channel 

of velocities. So the deformation of initial distribution occurs in two ways simultaneously. Because both velocity and concentration distributions are replaced by uniform ones, the observed dispersion of particles should be reproduced by an additional term in the transport equation. This is the reason of introducing of the dispersive terms into Eq. (1.145). The introduced term has diffusive character. However, the coefficient _D_<sup>_D_</sup> is obviously not related to the physical properties of the considered solution but to the degree of non-uniformity of the velocity and concentration distributions. 

As results from experiments, the values of the longitudinal dispersion are significantly larger than those of the turbulent diffusion _D_<sup>_D_</sup> ≫ _D_<sup>_T_</sup> . It appears that _D_<sup>_D_</sup> can reach the value even of the order of 10<sup>2</sup> m<sup>2</sup> ·s<sup>−1</sup> (Cunge et al. 1980). For this reason sometimes the turbulent diffusion in Eq. (1.145) is neglected. 

Considering the pollutant transport in open channels, one can distinguish two different zones in which the mathematical modeling should be carried out using different approaches. If we are dealing with a point source of pollution as in Fig. 1.13, then the pollutant transport in the zones near to the source must be analyzed as 2D (or even 3D) problem. 



<!-- Start of picture text -->
x<br>y<br>Lz<br>L<br>Q<br><!-- End of picture text -->

**Fig. 1.13** Distribution of concentration near the source of pollutant 

1.8 Equation of Mass Transport 

41 

In this zone of length _Lz_ , not far away from the source, we can expect the uniform distribution of concentration in the vertical direction only. Assumption of the uniform distribution over the whole wetted cross-sectional area is not admissible. Thus, for such a case Eq. (1.145) is suitable model. 1D model, preferable for open channels, can be applied only when the pollutants are well mixed over whole crosssection of a channel, which sometimes happens at quite large distant ( _Ly_ in Fig. 1.13) from the point of release of the pollutant. 

When the condition of good mixing is satisfied, Eq. (1.145) can be simplified by elimination of the second dimension normal to the channel axis, i.e. by elimination of the independent variable _y_ . To this order Eq. (1.145) must be integrated over the width of the channel from 0 to _B_ (Fig. 1.14). 

Since we assume that the water does not flow in _y_ direction, i.e. _V_ = 0, and the depths at the limits of integrations are: _H_ ( _y_ = 0), _H_ ( _y_ = _B_ ) = 0 then the integral reduces to: 



The integrals of subsequent terms of Eq. (1.146) are following: 





<!-- Start of picture text -->
h<br>B<br>y dy<br>H (y)<br>Z(y)<br>y<br><!-- End of picture text -->

**Fig. 1.14** Sketch of cross-section for integration of Eq. (1.145) in _y_ direction 

1 Open Channel Flow Equations 

42 



Substitution of Eqs. (1.147), (1.148), (1.149) and (1.150) in Eq. (1.146) yields 



Consequently 1D advection-diffusion transport equation was obtained. In this equation the bar denotes the averaged concentration over cross-sectional area: 



To simplify notation the bar will be omitted, however, in 1D transport equation considered further, the concentration should be interpreted as averaged over channel cross-section. In addition, in the sum of the diffusion coefficients the turbulent diffusion coefficient is neglected as much smaller than the dispersion coefficient and the subscripts _x_ and the superscript _D_ are omitted, since only one coefficient is used. Consequently Eq. (1.151) becomes: 



Equation (1.153) describes 1D advection-diffusion transport of passive pollutant dissolved in water for non-prismatic open channel. In particular cases it can be subjected to additional simplifications. 

The products in Eq. (1.153) can be differentiated: 



If the considered channel is fed by a lateral inflow, then the continuity equation (1.80) is valid. Substitution of this equation as well as of Eq. (1.9) yields: 



1.9 Thermal Energy Transport Equation 

43 

Equation (1.155) can be simplified further. Assuming a constant coefficient of dispersion _D_ and differentiating the diffusive term leads to the following: 



As results from Eq. (1.156), the variability of the wetted cross-sectional area generates an effect of additional advection. Depending on the sign of the derivative _∂A_ / _∂x_ an increase or decrease of the advective transport may occur. 

For steady and uniform flow, when _A_ = const, _U_ = const and _q_ = 0, Eq. (1.156) becomes an advection-diffusion equation with constant parameters: 



It is the simplest form of 1D transport equation. For some initial and boundary conditions Eq. (1.157) can be solved analytically. For this reason it is often used to check the accuracy of the numerical methods applied to solve more realistic forms of transport equations. 

### **1.9 Thermal Energy Transport Equation** 

Apart from dissolved constituents, the flowing stream also transports heat. This phenomenon has several implications. First of all, the heat transport determines the seasonal changes of open channel hydraulic. The most important change occurs at the beginning of winter in temperate and cold climates, when intensive heat exchange through the water–air interface leads to water cooling. When the water temperature reaches 0<sup>◦</sup> C, ice can occur in the stream. After some time, in suitable circumstances the ice layer at the water surface appears. In such a case the hydraulic conditions of flow change radically, from those typical to a free-surface flow to the ones characteristic for closed-conduit flow. The presence of the ice disturbs the navigation and operation of the hydraulic structures. On the other hand the temperature of water determines the possible concentration of the gases dissolved in water influencing in this way the chemical and biological processes. Finally it determines the self-purification and living conditions for aquatic fauna. Therefore the knowledge of the spatial and temporal evolution of the water temperature has essential meaning from the viewpoint both hydraulic and water-quality related studies. 

Variation of the water temperature is described by the head transport equation, which is derived from the energy conservation principle. In this case the conservative quality is the total energy i.e. kinematic and internal (thermal) energy per unit volume of water. Note that for an incompressible liquid like water, the internal energy is defined through its temperature. 

In the case of turbulent flow the energy conservation principle applied for the control volume _V_ of the water limited by the control surface _σ_ leads to the following equation: 

1 Open Channel Flow Equations 

44 



where: 

_t_ – time, 

_θ_ – time averaged temperature of water, 

**u** – time averaged vector of flow velocity, 

**α** – tensor of molecular heat diffusion **α**<sup>_T_</sup> – tensor of turbulent heat diffusion 

The tensors of heat diffusion are given by formulas: 



where: 

**λ** – tensor of molecular heat conduction, **λ**<sup>_T_</sup> – tensor of turbulent heat conduction, _cw_ – specific heat of water, _ρ_ – density of water. 

Both tensors have only 3 non-zero elements located on the main diagonal and related with the respective spatial directions. These components are given as: 











45 

1.9 Thermal Energy Transport Equation 



where _λx_ , _λy_ , _λz_ are the coefficients of molecular heat conductivity in _x_ , _y_ and _z_ direction, respectively, whereas _λ_<sup>_T_</sup> _x_<sup>,</sup><sup>_λT_</sup> _y_<sup>,</sup><sup>_λ_</sup> _z_<sup>_T_arethecoefficientsofturbulentheat</sup> conductivity in the same directions. In SI system the components of tensor of heat diffusion are expressed in the same units as the coefficient of mass diffusion, i.e. in m<sup>2</sup> ·s<sup>−1</sup> . Since the components of turbulent diffusivity tensor are much greater than the coefficients of molecular heat diffusion � **_α_** ≪ **_α_**<sup>_T_�</sup> , then **α** can be neglected. With this assumption Eq. (1.158) can be rewritten in scalar notation as follows: 



As for the mass transport equation, it is well justified to reduce the number of dimensions also in this case. Equation (1.162) can be simplified by integration in the vertical direction from the bottom of water layer to its surface. The integration is carried out with identical assumptions as applied for the mass transport. It means that any function in Eq. (1.162) is averaged in the vertical using the formulas (1.138), (1.139) and (1.140), whereas the velocity vector component in _z_ direction is eliminated ( _w_ = 0). Since in this case the integration is slightly different, let us carry it out. 

Equation (1.162) is integrated over depth: 



where: 

- _T_ – vertically averaged water temperature, 

- _U_ – vertically averaged horizontal flow velocity in _x_ direction, _V_ – vertically averaged horizontal flow velocity in _y_ direction, _u_<sup>′′</sup> – the deviation of actual value of _u_ from its averaged value _U_ , _θ_<sup>′′</sup> – the deviation of actual value of _θ_ from its averaged value _T_ . 

The respective terms of Eq. (1.163) are integrated as follows: 

46 

1 Open Channel Flow Equations 









The integral of the last term of Eq. (1.163) _I_ 6 represents the difference between the fluxes through the water surface at _z_ = _h_ and the channel bottom at _z_ = _Z_ . The energy exchange across the bottom is not important, except for the flow under ice cover. Thus one can assume: 



where _αz_<sup>_T_</sup> is the coefficient of turbulent conductivity in _z_ direction. On the other hand, the flux through the water surface has essential importance for heat transport since this is the main way of energy exchange, which determines the water temperature. One can assume that: 

1.9 Thermal Energy Transport Equation 

47 



<!-- Start of picture text -->
x<br>Ha<br>A<br>φ<br>B<br>dy<br>Q ( L t ,)<br>dx<br>(0, t<br>Q<br>)<br>L<br><!-- End of picture text -->

**Fig. 1.15** Scheme of a channel reach transporting and exchanging heat 



where _φ_ is the net rate of heat transport between the water and the air in both ways. It is caused by many physical processes which take place at the air–water interface (Fig. 1.15). 

Substitution of all calculated integrals in Eq. (1.163) yields: 



The terms _u_<sup><u>′′</u></sup> · _θ_<sup><u>′′</u></sup> _and v_<sup><u>′′</u></sup> · _θ_<sup><u>′′</u></sup> and represent the already well-known additional transport effect, this time due to the fluctuations of the velocity and temperature. As previously, it can be expressed using a formula similar to the Fourier law (Baehr and Stephan 2006): 



in which _αx_<sup>_D_,</sup><sup>_α_</sup> _y_<sup>_D_are the coefficients of longitudinal heat dispersion. Substitution of</sup> Eq. (1.168) in Eq. (1.167) yields: 

1 Open Channel Flow Equations 

48 



Since the order of magnitude of the turbulent diffusion coefficients is much less than the order of magnitude of the dispersion coefficients, the former can be neglected. It allows us to rewrite Eq. (1.169) as follows: 



Equation (1.170) describes 2D unsteady heat transport. In open channel hydraulics this equation is applied locally, in the area where the water is not well mixed over the cross-section and two velocity vector components must be taken into consideration. 

To obtain 1D equation for a channel reach, in which the water is well mixed in cross-section, Eq. (1.170) should be integrated over the channel width _B_ , i.e. in _y_ direction (Fig. 1.14). Since in _y_ direction the water does not move, _V_ = 0. In addition, the depths at the limits of integrations are: _H_ ( _y_ = 0), _H_ ( _y_ = _B_ ) = 0. If there is one flow direction only, then the indices connected with the dispersion coefficient _D_ can be omitted. Finally, the integration is carried out for the reduced form of Eq. (1.170): 



The integration carried out in the same way as for the mass transport equation, gives: 



In this equation: 



1.10 Types of Equations Applied in Open Channel Hydraulics 

49 



The net flux of heat through the water surface _φ_ resulting from the energy balance at the interface has negative sign if the water emits heat towards atmosphere and it has positive sign when heat is absorbed by the water from atmosphere. The term _φ_ takes into account all important processes connected with the heat transfer such as: 

- short wave solar radiation, 

- long wave water surface radiation, 

- long wave atmosphere radiation, 

- sensible heat conducted between the water and atmosphere, 

- latent heat of vaporization or condensation. 

Since some of the above listed processes are determined by the water temperature then the net flux is a function of temperature as well: _φ_ = _φ_ ( _T_ ). 

For a channel reach, which is not fed by the lateral inflow and for a constant coefficient of longitudinal dispersion _α_ , Eq. (1.172) can be further simplified: 



where: 

_U_ = _Q_ / _A_ – averaged velocity, _Ha_ = _A_ / _B_ – hydraulic depth. 

If the flow is steady then _A_ = const. and _U_ = const. In such a case Eq. (1.173) is reduced to the simplest form of the advection-diffusion head transport equation: 



Assuming constant parameters this equation can be solved analytically for some initial-boundary conditions. 

### **1.10 Types of Equations Applied in Open Channel Hydraulics** 

In this chapter the basic equations of open channel hydraulics were introduced. They represent a variety of types depending of the considered kind of flow. For instance, equations defining the critical depth (Eq. 1.16) and the normal depth for steady uniform flow (Eq. 1.20) are nonlinear algebraic equations, with respect to the unknown value of _HC_ or _Hn_ , respectively. In other cases the unknown quantity is a function of 

50 

1 Open Channel Flow Equations 

a single independent variable, either _x_ or _t_ , and is specified by an ordinary differential equation (ODE), which contains derivatives of the function with respect to the considered variable. An example of ODE is given by the storage equation (1.122), while steady gradually varied flow is described by a system of two coupled ODEs (Eqs. 1.108 and 1.109). Finally, if the unknown function depends on both space and time, it is described by a partial differential equation (PDE), which contains derivatives with respect to both x and t. This is the case of mass and energy transport equations (Eq. 1.153 and 1.172), while the Saint Venant equations (1.87) and (1.88) represent a system of two coupled PDEs. 

A common feature of all these equations is that in principle they can be solved only approximately, using numerical methods. Depending on the type of equation to be solved, numerical approaches differ in complexity and may include multiple stages, each of them constituting a separate numerical problem. For instance, ODEs and PDEs are transformed in a process called discretization into systems of linear or nonlinear algebraic equations, which are then solved to obtain the values of the unknown functions at specified points in time-space domain. 

In Chapter 2 we discuss the numerical techniques applied to solve single nonlinear algebraic equations and systems of linear and nonlinear algebraic equations, which are the basic building blocks for more complex numerical algorithms. Numerical solution of ODEs and their systems is the subject of Chapters 3. The methods presented in these two chapters are then applied to solve steady flow problems in Chapters 4. Partial differential equations, which are most challenging type of equations from the numerical point, are discussed from Chapters 5 to 8. 

### **References** 

- Abbott MB (1979) Computational hydraulics-elements of the theory of free surface flow. Pitman, London 

- Abbott MB, Basco DR (1989) Computational fluid dynamics. Longman Scientific and Technical, New York 

Akan AO (2006) Open channel hydraulics. Butterworth-Heinemann, Oxford 

Baehr HD, Stephan K (2006) Heat and mass transfer, 2nd edn. Springer, Berlin/Heidelberg Bird RB, Steward WE, Lightfoot EN (1960) Transport phenomena. Wiley, New York Chanson H (2004) The hydraulics of open channel flow: An introduction, 2nd edn. Elsevier, Oxford Chow VT (1959) Open channel hydraulics. McGraw-Hill, New York 

- Cunge J, Holly FM, Verwey A (1980) Practical aspects of computational river hydraulics. Pitman 

   - Publishing, London 

Eagleson PS (1970) Dynamic hydrology. McGraw-Hill, New York 

French RH (1985) Open channel hydraulics. McGraw-Hill, New York 

Henderson FM (1966) Open channel flow. Macmillan Company, New York 

- Hervouet JM (2007) Free surface flow – modelling with the finite element method. Wiley, 

Chichester 

Jain SC (2000) Open channel flow. Wiley, Chichester 

- Korn GA, Korn TM (1968) Mathematical handbook for scientists and engineers, 2nd edn. McGraw-Hill, New York 

- Liggett JA (1975) Basic equations of unsteady flow. In: Mahmood K, Yevjevich V (eds.) Unsteady flow in open channels. Water Resources Publications, Fort Collins, CO 

51 

References 

Martin JL, McCutcheon SC (1999) Hydrodynamics and transport for water quality modeling. CRC Press, Boca Raton, FL McQuarrie DA (2003) Mathematical methods for scientists and engineers. University Science Books, Sausalito, CA Singh VP (1996) Kinematic wave modelling in water resources: Surface water hydrology. Wiley, New York. 

## **Chapter 2 Methods for Solving Algebraic Equations and Their Systems** 

### **2.1 Solution of Non-linear Algebraic Equations** 

### **_2.1.1 Introduction_** 

In this section we consider the solution of the following equation: 



where _x_ is real variable and _f_ ( _x_ ) is real and continuous. The roots of Eq. (2.1) represent the values of _<u>x</u>_ for which _f_ ( _x_ ) = 0. For our purpose we are interested in determination of the real roots only. 

The determination of the roots is carried out in two stages. At first the searched roots must be located, i.e. we have to know their number and their approximate positions. For this purpose the plot of _f_ ( _x_ ) is very useful and it should be done. On the other hand, usually some reasonable approximation of the searched roots is available from engineering analysis. For example the flow depth cannot be negative number, so all negative roots are eliminated immediately as they are not the subject of interest. 

Each root must be separated from the others, so that in the specified interval designed by two endpoints only a single root exists. Practically this is carried out by examination of the signs of function _f_ ( _x_ ) at two selected values of _x_ , let say _a_ and _b_ . If _f_ ( _x_ ) has opposite sign at both ends of interval ⟨ _a_ , _b_ ⟩ then within this interval at least one root exists (Fig. 2.1). Unfortunately this statement says nothing about the number of roots between _a_ and _b_ . To answer this question an examination of the derivative of function _f_ ( _x_ ) is required. If in the interval ( _a_ , _b_ ) the derivative of function _f_ ( _x_ ) exists and it does not change its sign, i.e. _f_<sup>′</sup> ( _x_ ) > 0 or _f_<sup>′</sup> ( _x_ ) < 0 for _a_ < _x_ < _b_ , then there is a single root in ⟨ _a_ , _b_ ⟩ (Fig. 2.2). 

When an approximate position of the root is found, one can pass to the second stage of calculations. A suitable method for determination of a single root with required level of precision must be applied. In further discussions we assume that the interval in which a single root exists is already known. Some methods use both endpoints of interval containing a root, whereas other ones need one point from 

53 

R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_2, ⃝C Springer Science+Business Media B.V. 2010 

54 

2 Methods for Solving Algebraic Equations and Their Systems 



<!-- Start of picture text -->
f ( X )<br>f ( a )<br>x 1 x 2 x 3 b<br>a x<br>f ( b )<br><!-- End of picture text -->

**Fig. 2.1** Roots of equation _f_ ( _x_ ) = 0 in the interval ⟨ _a_ , _b_ ⟩ 



<!-- Start of picture text -->
f  ( X )<br>f ( b )<br>a x<br>b x<br>f ( a )<br><!-- End of picture text -->

**Fig. 2.2** Single root of function _f_ ( _x_ ) in the interval ⟨ _a_ , _b_ ⟩ 

this interval only. The former are called bracketing methods and the latter – open methods. 

### **_2.1.2 Bisection Method_** 

The concept of bisection method is to divide the interval ⟨ _a_ , _b_ ⟩ in two halves, and to choose for further search the half which contains the root. This procedure is repeated until the required accuracy criterion is satisfied. 

The algorithm of determination the approximated value of the root of Eq. (2.1) in interval ⟨ _a_ , _b_ ⟩ by bisection method with the assumed tolerance _ε_ , can be listed as follows: 

- (1) Compute _c_ = ( _a_ + _b_ )/2, 

- (2) Compute _f_ ( _c_ ), 

- (3) Verify: if | _f_ ( _c_ )| ≤ _ε_ then _c_ is searched value of the root and problem is solved. Otherwise: 

55 

2.1 Solution of Non-linear Algebraic Equations 

- (4) Choose from two subintervals ⟨ _a_ · _c_ ⟩ and ⟨ _c_ , _b_ ⟩ this one, in which is the root and determine endpoints of new interval: if _f_ ( _a_ ) · _f_ ( _c_ ) < 0, then set _b_ = _c_ , otherwise set _a_ = _c_ ; 

- (5) Go to point 1. 

After _i_ th iteration the length of initial interval ⟨ _a_ , _b_ ⟩ is reduced to the following one: 



In general case it is very difficult to estimate the true error of the calculated root. In practice two types of accuracy criteria are commonly used. The first one assumes that _xi_ is a good approximation of searched root of equation _f_ ( _x_ ) = 0, if | _f_ ( _xi_ )| is a small number and conversely, if | _f_ ( _xi_ )| is large number then _xi_ is considered as unsatisfying approximation of the root. The iterations are stopped when: 



where _ε_ is positive number representing the assumed tolerance. However, sometimes this approach can lead to false results, as illustrated in Fig. 2.3. 

Even for small value of _ε_ one can obtain an inaccurate solution of Eq. (2.1) if _f_ ( _x_ ) varies only insignificantly in neighborhood of the root (Fig. 2.3a). 

The second criterion is based on the examination of the length of currently reduced interval. The iterations are stopped, when _bi_ − _ai_ ≤ _ε_<sup>′</sup> where ε<sup>′</sup> is specified tolerance however related to the length of interval, not to the value of function _f_ ( _x_ ), as previously. 

Comparing with other methods, the bisection method converges to the exact solution rather slowly. However it has two important advantages. First of all, it is always convergent, what means that it always leads to the solution. Moreover, it does not 



<!-- Start of picture text -->
a) b)<br>y y<br>y = f ( x )<br>y = f ( x )<br>f ( c )<br>ε f ( c ) ε<br>x c x x c x<br><!-- End of picture text -->

**Fig. 2.3** Various forms of _f_ ( _x_ ) close to the root: slowly ( **a** ) and rapidly ( **b** ) varied 

56 

2 Methods for Solving Algebraic Equations and Their Systems 

require more assumptions on _f_ ( _x_ ) and its derivative, apart from the continuity of _f_ ( _x_ ) in ⟨ _a_ , _b_ ⟩. 

### **_2.1.3 False Position Method_** 

The false position method is one of the oldest methods of solution of the non-linear equations. It is similar in concept to the bisection method, but the interval containing root is divided in two parts proportionally to the values of _f_ ( _x_ ) at the endpoints. Consequently, it is usually more efficient than the bisection method. 

Consider again the interval ⟨ _a_ , _b_ ⟩ containing a single root (Fig. 2.4). 

The points _A_ ( _a_ , _f_ ( _a_ )) and _B_ ( _b_ , _f_ ( _b_ )) we join by a straight line. It intersects the _x_ axis at point _c_ . Its position is calculated using the formula derived from the similarity of triangles (Fig. 2.4): 



Close to the root numbers of the same order may appear in both numerator and denominator of Eq. (2.4), so significant round-off errors can be generated. For this reason a rearranged formula is recommended: 



The second term of Eq. (2.5) can be considered as the correction of _a_ . According to Eq. (2.5) one or both endpoints of the considered interval can move during the iterations. It depends on the shape of function _f_ ( _x_ ) within the interval ⟨ _a_ , _b_ ⟩. For monotonic function, when its second derivative _f_<sup>′′</sup> ( _x_ ) does not change the sign in ⟨ _a_ , _b_ ⟩, one end will be fixed. For instance, if _f_ ( _a_ ) > 0 and _f_<sup>′′</sup> ( _x_ ) > 0 for _a_ ≤ _x_ ≤ _b_ , then the end _a_ is fixed (Fig. 2.5). 

In such a case Eq. (2.5) may be reformed as follows: 



<!-- Start of picture text -->
y A<br>f ( x )<br>f ( a )<br>f ( c )<br>x b<br>a c x<br>f ( b )<br>B<br><!-- End of picture text -->

**Fig. 2.4** Sketch of false position method 

57 

2.1 Solution of Non-linear Algebraic Equations 



<!-- Start of picture text -->
y<br>A<br>f ( a )<br>x i xi  −1 x 1 b = x 0<br>a x x<br>f ( b )<br>B<br>y = f ( x )<br><!-- End of picture text -->

**Fig. 2.5** False position method with one fixed endpoint 



Similar formula can be written in opposite situation as well, when the endpoint _b_ is fixed (Fig. 2.6). 

Note that as the termination criterion rather relation (2.3) should be used. When one end of the interval is fixed, then we approach the root from side of second end and consequently, it is impossible to check the interval’s length. This can be seen in Figs. 2.5 and 2.6. 

The algorithm for solution of the non-linear equation using the false position method is similar to the one for bisection method. The only difference is the way of calculation of the point _c_ dividing the interval ⟨ _a_ , _b_ ⟩. 

_Example 2.1_ A trapezoidal channel with _b_ = 2.5 m, _nM_ = 0.025, _m_ = 1.5, _s_ = 0.0005 carries a discharge _Q_ = 8 m<sup>3</sup> /s. Determine the normal flow depth using the false position method. Assuming the same termination criterion, compare the number of needed iterations with those for the bisection method. 



<!-- Start of picture text -->
y<br>A<br>y = f ( x )<br>f ( a )<br>x b = x 0<br>a x 1 x i x<br>f ( b )<br>B<br><!-- End of picture text -->

**Fig. 2.6** False position method with fixed endpoint _b_ 

58 2 Methods for Solving Algebraic Equations and Their Systems 

The normal depth satisfies the steady uniform discharge flow equation expressed using the Manning formula (1.20) 



For the trapezoidal shape of a channel as presented in Fig. 1.3, the cross-sectional parameters are given by Eqs. (1.5) and (1.6), which lead to the following equation: 



The root of Eq. (2.8) must be searched in the domain of the positive real numbers. Note that _f_ ( _H_ = _0_ ) = _Q_ then _f_ ( _H_ ) is expressed in units of the flow rate, i.e. in [m<sup>3</sup> /s]. This allows us to choose easily the value of the parameter _ε_ representing the tolerance for convergence criterion. The root of Eq. (2.8) was searched in the interval ⟨0, 2.0 m⟩. 

To obtain the normal depth _H_ = 1.546 m with assumed tolerance _ε_ = 0.001 m<sup>3</sup> /s, the false position method required 6 iterations, whereas the bisection method needed 11 iterations to reach the identical result. 

### **_2.1.4 Newton Method_** 

The non-linear equation in standard form _f_ ( _x_ ) = 0 is solved. Assume that approximated value of its root is _xi_ and next approximated value _xi+_ 1 is located from preceding one of distance _h_ , so we have: 



where δ _x_ is a small value. Assuming that _f_ ( _x_ ) is continuous and differentiated its value at point _xi_ +1 can be expressed using the Taylor series expansion: 



The Newton method uses Eq. (2.10) in which the terms with 2nd and higher order of derivatives are neglected. On the other hand, it is expected that _f_ ( _xi_ + δ _x_ ) = 0. Then Eq. (2.10) is reduced to the following: 



and the distance between two consecutive approximations of the root is equal to: 



59 

2.1 Solution of Non-linear Algebraic Equations 

Substitution of Eq. (2.12) in Eq. (2.9) yields: 



Interpretation of formula (2.13) is given in Fig. 2.7. The new approximation of the root _xi+_ 1 is determined by the point of intersection of _x_ axis and a straight line tangential to the function _f_ ( _x_ ) at the old approximation of the root _xi_ . 

The same relation can be derived from the equation of the line tangential to the function _y_ = _f_ ( _x_ ) at point _xi_ . 

An important problem in the Newton method is the first estimation of root. If _f_ ( _a_ ) · _f_ ( _b_ ) < 0, _f_<sup>′</sup> ( _x_ )̸ = 0 for _a_ ≤ _x_ ≤ _b_ and _f_<sup>′′</sup> ( _x_ ) does not change the sign, then any value _x_ 0 from the interval ⟨ _a_ , _b_ ⟩ can be taken as the starting point. However even all those conditions are satisfied, the Newton method may not be successful. One can conclude that before using the Newton method, it is worth to examine the derivative of function _f_ ( _x_ ) and to begin the iteration at the part of interval ⟨ _a_ , _b_ ⟩ in which _f_<sup>′</sup> ( _x_ ) has greater values. 

From Eq. (2.13) results that correction of the root _δx_ decreases the value of derivative increases. It means that the Newton method is more efficient for steep function _f_ ( _x_ ) in surrounding of root. If _f_ ( _x_ ) has local extreme points, it can be impossible to reach the solution at all. 

To stop iterations the criterion (2.3) 



is usually applied. 

The algorithm of solution of a non-linear equation using the Newton method can be written as follows: 



<!-- Start of picture text -->
y<br>B<br>y = f(x)<br>f ( b )<br>f ( xi )<br>a<br>x i  + 1 xi b x<br>f ( a )<br>δ x<br>A<br><!-- End of picture text -->

**Fig. 2.7** Interpretation of the Newton method 

60 

2 Methods for Solving Algebraic Equations and Their Systems 



<!-- Start of picture text -->
f ( x )<br>y = f  ( x )<br>x xi +1 xi x 0 x<br><!-- End of picture text -->

**Fig. 2.8** Newton method with constant tangent 

- (1) Assume the starting point taking _x_ 1 from the interval ⟨ _a_ , _b_ ⟩ containing a single root, 

- (2) Compute _f_ ( _x_ 1), 

- (3) Compute _f_<sup>′</sup> ( _x_ 1), 

- (4) Compute _x_ 2 = _x_ 1 − _f_ ( _x_ 1) _/f_<sup>′</sup> ( _x_ 1) 

- (5) Verify: if | _f_ ( _x_ 2)| ≤ _ε_ then _x_ 2 is searched value of the root and problem is solved. Otherwise: 

- (6) Set _x_ 1 = _x_ 2 and go to point 2. 

Note that in contrast to the bisection and false position methods the Newton method does not refine the interval containing the searched root, i.e. it belongs to the open methods. 

Sometimes the function _f_ ( _x_ ) is difficult to differentiate. In such a case the Newton method can be modified in two ways. In the first case a constant value of derivative is used, corresponding to the derivative calculated at the starting point. Then the Newton formula becomes the following one: 



It means that in the consecutive approximations of the root, the lines parallel to the tangent at _x_ 0 are applied instead of the tangents (Fig. 2.8). 

The second way of modification of the Newton method is based on the numerical approximation of the derivative _f_<sup>′</sup> ( _x_ ). Using the backward difference formula resulting from the Taylor series expansion of the function _f_ ( _x_ ), its derivative is expressed as: 



61 

2.1 Solution of Non-linear Algebraic Equations 

Then Eq. (2.11) takes the following form: 



One can notice that to calculate _xi+_ 1 two preceding approximations are needed. This version of the Newton method is known as the secant method. Note that Eq. (2.17) is very similar to Eq. (2.6). 

_Example 2.2_ A trapezoidal channel with _b_ = 2.5 m, _m_ = 1.5, carries a discharge _Q_ = 8 m<sup>3</sup> /s. Determine the normal flow depth using the Newton method with the assumed tolerance _ε_ = 0.001 m. 

The critical depth satisfies the formula (1.16): 



where: 

_Q_ – flow rate, 

_α_ – Coriolis coefficient, _g_ – acceleration due to gravity, _A_ – wetted cross-section area, _B_ – channel width at the surface level. 

For our purposes Eq. (2.18) is rearranged to the form: 



For the trapezoidal shape of a channel, the cross-sectional parameters are given by Eqs. (2.3) and (2.4). Substituting these formulas in Eq. (2.70) yields: 



Its derivative with regard to _H_ is following: 



The root of Eq. (2.20) is located in the interval ⟨0, 2 m⟩. At its endpoints the function (2.20) takes the following values: _f_ ( _H_ = 0) = 2.5 m and _f_ ( _H_ = 2 m) = –327.259 m. 

Note, that _f_ ( _H_ ) is expressed in units of the length i.e. in [m]. This allows us to choose the value of the parameter _ε_ representing the tolerance. It was assumed to be equal _ε_ = 0.001 m. As the first estimation of root end of the interval was assumed. 

62 

2 Methods for Solving Algebraic Equations and Their Systems 

It means that _H_ 0 = 2 m. For the assumed set of data, the critical depth _H_ = 0.727 m was obtained after 7 iterations. 

### **_2.1.5 Simple Fixed-Point Iteration_** 

Similarly to the Newton method, the fixed-point iteration (or successive substitution) belongs the open methods. In this approach the considered non-linear equation _f_ ( _x_ ) = 0, where _f_ ( _x_ ) is continuous function, is transformed to the equivalent form: 



Assume that the first estimate of the root _x_ 0 is known. The formula (2.22) can be used to predict a new value of _x_ : _x_ 1 = _ϕ_ ( _x_ 0). In next step _x_ 1 is substituted in Eq. (2.22) to calculate _x_ 2 = _ϕ_ ( _x_ 1). Repeating this substitution one obtains a sequence of approximations of the searched root: 



where _i_ is the iteration index. 

The iteration process (2.23) implies two essential questions: 

- How to find the function _ϕ_ ( _x_ )? 

- When is the sequence _xi_ convergent? 

The transformation of equation _f_ ( _x_ ) = 0 into equation _x_ = _ϕ_ ( _x_ ) can be accomplished by algebraic manipulation leading to the isolation of _x_ at the left-hand side of the equality, by adding _x_ to both sides of solved equation _f_ ( _x_ ) = 0 or by simultaneous application of both mentioned techniques. 

As far as the convergence is considered, the following condition ensures that the iterations converge to the root (Chapra and Canale 2006): 



If relation (2.24) is satisfied, then the sequence _xi_ converges for any starting point _x_ 0 taken from the interval ⟨ _a_ , _b_ ⟩. The limit of this sequence is the root. Then the essential problem of solution of the non-linear equation _f_ ( _x_ ) = 0 using the fixed-point iteration, is to transform it into the equation _x_ = _ϕ_ ( _x_ ) ensuring that the condition (2.24) is satisfied. 

63 

2.1 Solution of Non-linear Algebraic Equations 

The properties of the convergence process for fixed-point iteration can be illustrated graphically. To this order let us reform Eq. (2.22) and express it as a set of two following equations: _y_ 1 = _x_ and _y_ 2 = _ϕ_ ( _x_ ). These functions, plotted in _x_ – _y_ plane, intersect at the point corresponding to the root of solved equation _f_ ( _x_ ) = 0 (Fig. 2.9). Starting from the first estimate _x_ 0 we tend to the root through the consecutive estimates, depending on the sign of the derivative _ϕ_<sup>′</sup> ( _x_ ). 

The root can be approached from one side (monotone pattern – Fig. 2.9) or from both sides alternatively (oscillating pattern – Fig. 2.10). 

In Fig. 2.11 an opposite situation is presented. When the condition (2.24) is not satisfied, the iterations diverge. After starting from _x_ 0 the consecutive estimates tend in the opposite direction with regard to the root. 

Transformation of _f_ ( _x_ ) into _ϕ_ ( _x_ ) has essential meaning for successful application of the fixed-point iteration. The proper choice of function _ϕ_ ( _x_ ) should ensure that the solution procedure is convergent, and that the convergence is as fast as possible (see Bjorck and Dahlquist (1974) for more details). 

The algorithm of solution of a non-linear equation using fixed-point iteration can be written as follows: 

- (1) Assume the starting point taking _x_ 1 from the interval ⟨ _a_ , _b_ ⟩ containing a single root, 

- (2) Compute _x_ 2 = _ϕ_ ( _x_ 1), 

- (3) Compute _f_ ( _x_ 2), 

- (4) Verify: if | _f_ ( _x_ 2)| ≤ _ε_ then _x_ 2 is the searched value of the root and problem is solved. 

Otherwise: 

- (5) Set _x_ 1 = _x_ 2 and go to point 2. 



<!-- Start of picture text -->
y<br>B 1 A 0<br>B 2 ϕ (  ) x 0<br>M A 1<br>A 2<br>x x 2 x 1 x 0 x<br>ϕ<br>( x )<br>=<br>y<br>y  = x<br><!-- End of picture text -->

**Fig. 2.9** Fixed-point iteration for 1 > _ϕ_<sup>′</sup> ( _x_ ) > 0 

64 

2 Methods for Solving Algebraic Equations and Their Systems 



<!-- Start of picture text -->
y<br>A 1 B 2<br>M<br>B 3 A 2<br>B 1 A 0<br>x 1 x x 2 x 0 x<br>Fig. 2.10 Fixed-point iteration for 0 >  ϕ ′ ( x ) > – 1<br>Fig. 2.11 Example of<br>y<br>divergent iterations for<br>φ ′ ( x ) < –1<br>A 1 B 2<br>M<br>B 1 A 0<br>A 2<br>x 1 x x 0 x 2 x<br>y =ϕ( x )<br>y =  ϕ (x)<br>= x<br>y<br>y = x<br><!-- End of picture text -->

_Example 2.3_ A trapezoidal channel with _b_ = 2.5 m, _m_ = 1.5, carries a discharge _Q_ = 8 m<sup>3</sup> /s. Determine the critical flow depth using the fixed-point iteration with the assumed tolerance _ε_ = 0.001 m. 

65 

2.1 Solution of Non-linear Algebraic Equations 

The formula (2.18) describing the critical flow is transformed as follows: 



The notations applied in Eq. (2.18) are valid. For the trapezoidal shape of a channel the cross-sectional parameters _A_ and _B_ are given by Eqs. (1.5) and (1.7). Substitution of these equations causes that the critical depth being the root of Eq. (2.25) must be calculated by iteration. 

The fixed-point iteration requires that the function _f_ ( _H_ ) is rearranged to the form: 



In this case the transformation is a delicate issue, since practically all forms obtained by simple algebraic manipulations on Eq. (2.25) do not ensure convergence. Good results are obtained if Eq. (2.25) is rearranged to the following form: 



and next, to its both sides the critical depth _H_ is added: 



Substitution of Eqs. (1.5) and (1.7) in Eq. (2.28) yields the final equation: 



Then the formula for fixed-point iteration is: 



where _i_ is the index of iteration. 

As the termination criterion the following relation involving the results of two consecutive iterations is assumed: 



where the parameter _ε_ represents accepted tolerance. 

The root of Eq. (2.25) is located, as in Example 2.2, in the interval ⟨0, 2 m⟩. At the interval endpoints the function (2.25) takes the following values: _f_ ( _H_ = 0) = 6.524 m and _f_ ( _H_ = 2 m) = –222.739 m. 

66 

2 Methods for Solving Algebraic Equations and Their Systems 

As the starting point of iteration the end of interval was assumed, i.e. _H_ 0 = 2 m. The critical depth _H_ = 0.727 m was obtained after 11 iterations. This is the same result as given by the Newton method in Example 2.2, however to obtain it more iterations were needed. 

### **_2.1.6 Hybrid Methods_** 

The list of available methods to solve nonlinear algebraic equations is much longer (see e.g. Bjorck and Dahlquist 1974, Press et al. 1992) and includes some hybrid approaches, which are modifications or combinations of the four basic ones presented above. Two such methods will be presented here: the Ridders method and the Steffensen method. 

The Ridders method is a combination of the false position and bisection methods (Press et al. 1992). Assume that a single root of non-linear equation (2.1): _f_ ( _x_ ) = 0 is located in the interval ⟨ _a_ , _b_ ⟩. The iterations are performed according to the following algorithm: 

1. Calculate _f_ ( _x_ ) at midpoint of specified interval: _c_ = ( _a_ + _b_ )/2; 

2. Assume, that _f_ ( _x_ ) is approximated in ⟨ _x_ 1, _x_ 2⟩ by an exponential function build on the values of _f_ ( _x_ ) in known points _a_ , _b_ , _c_ , in the following form 



It is a quadratic equation with regard to _e_<sup>_α_</sup> . Its solution is following: 



Apply the false position method, however not for _f_ ( _a_ ), _f_ ( _c_ ), _f_ ( _b_ ) but for _f_ ( _a_ ), _f_ ( _c_ ) _e_<sup>_α_</sup> , _f_ ( _b_ ) _e_<sup>2</sup><sup>_α_</sup> . This allows us to calculate new approximation of the root _d_ . With Eq. (2.33) one obtains: 



3. Reduce the dimensions of the interval by checking of the signs in _a_ , _b_ , _c_ and _d_ . It is carry out as follows: 

If _f_ ( _c_ ) · _f_ ( _d_ ) < 0, then _a_ = _c_ and _b_ = _d_ , 

else 

if _f_ ( _c_ ) · _f_ ( _d_ ) > 0 then if _f_ ( _b_ ) · _f_ ( _d_ ) > 0 then _b_ = _d_ else _a_ = _d_ 

Note that the method uses the function _f_ ( _x_ ) only. Its derivative is not needed. To terminate the iteration the following criterion, similar to this applied in the Newton 

67 

2.1 Solution of Non-linear Algebraic Equations 

method, can be used: |f( _d_ )| ≤ _ε_ , where _ε_ is assumed positive number representing the tolerance. 

The Steffenson method is a modified version of the false position method (Bjorck and Dahlquist 1974), where the iteration convergence is accelerated. The following iterative formula is applied: 



where: 



In Example 2.4 the efficiency of the hybrid methods is compared with the efficiency of those of the standard methods which do not require the derivative of _f_ ( _x_ ). 

_Example 2.4_ In a rectangular channel of width _b_ = 50 m crossed by the sharpcrested weir of height _p_ = 1.0 m which spans entire channel, the flow discharge is _Q_ = 7.20 m (Fig. 2.12). Determine the depth of the water head _h_ taking into account the velocity head and assuming that the flow coefficient is dependent on the water depth. 

Including the velocity head the discharge equation is given as: 



where: 

_h_ – head, 

_b_ – weir width, 



<!-- Start of picture text -->
b<br>h = ? h<br>Q<br>p p<br>3−4  h<br><!-- End of picture text -->

**Fig. 2.12** Sharp-crested weir which spans entire width 

68 

2 Methods for Solving Algebraic Equations and Their Systems 

_v_ 0 – average flow velocity, _g_ – acceleration due to gravity, _K_ – flow coefficient. 

The average flow velocity behind a weir is given as: 



The flow coefficient for the considered type of weir is determined by the following formula (Roberson et al. 1998): 



This formula is valid up to an _h_ / _p_ value of about 10. Equation (2.36) is transformed to the typical form: 



With Eqs. (2.37) and (2.38) this equation is non-linear with regard to head _h_ . For the fixed-point iteration Eq. (2.39) is transformed to the following one: 



The single root of Eq. (2.39) is located in the interval ⟨0, 1.5 m⟩. In the termination criterion, taken in the form of relation | _f_ ( _hi_ )| ≤ _ε_ , the tolerance parameter _ε_ = 0.00001 m<sup>3</sup> /s is assumed. 

The results of consecutive iterations for all applied methods are listed in Table 2.1. Note that the methods differ significantly in efficiency. The total number of iterations needed to reach a solution of the same accuracy varies from 3 to 18. In this case the most effective are the fixed point method and the Ridders method, which require 3 iterations only. Other methods needed much more iterations to reach the solution with the same accuracy. This fact should be taken into considerations, while developing the computer codes for complex problems, in which the non-linear equations are solved many times. 

69 

2.2 Solution of Systems of the Linear Algebraic Equations 

**Table 2.1** Comparison of convergence for selected methods applied to solve Eq. (2.39) 

||Method|||||
|---|---|---|---|---|---|
|Iteration|Fixed point|Bisection|False position|Steffensen|Ridders|
|1|0.78958|0.75000|0.55015|0.15936|0.83379|
|2|0.78934|1.12500|0.73239|0.31090|0.78680|
|3|0.78934|0.93750|0.77665|0.45216|0.78935|
|4|–|0.84375|0.78656|0.57844|–|
|5|–|0.79688|0.78874|0.68184|–|
|6|–|0.77344|0.78922|0.75202|–|
|7|–|0.78516|0.78932|0.78346|–|
|8|–|0.79102|0.78934|0.78918|–|
|9|–|0.78809|0.78935|0.78935|–|
|10|–|0.78955|0.78935|–|–|
|11|–|0.78882|–|–|–|
|12|–|0.78918|–|–|–|
|13|–|0.78937|–|–|–|
|14|–|0.78928|–|–|–|
|15|–|0.78932|–|–|–|
|16|–|0.78934|–|–|–|
|17|–|0.78936|–|–|–|
|18|–|0.78935|–|–|–|



### **2.2 Solution of Systems of the Linear Algebraic Equations** 

### **_2.2.1 Introduction_** 

Solution of systems of linear equations is one of the most basic problems of numerical analysis, which arises in multiple applications, for example when solving partial differential equations with finite difference or finite element method. While many ready-made numerical subroutines for linear systems are available, it seems worthwhile to present in this section some basic algorithms, which can be conveniently used in the framework of numerical modeling of open channel flow. 

Let us consider a system of _N_ linear equations with _N_ unknowns: 



In matrix notation this system is rewritten as follows: 



where: 

2 Methods for Solving Algebraic Equations and Their Systems 

70 



**A** =( _aij_ ) ( _i_ , _j_ = 1, 2, _. . ._ , _N_ ) is real square matrix of system coefficients, **X** =( _xi_ ) ( _i_ = 1, 2, _. . ._ , _N_ ) is column vector of unknowns, **B** =( _bi_ ) ( _i_ = 1, 2, _. . ._ , _N_ ) is the column vector of constants, _N_ is dimension of system. 

It is assumed that the matrix **A** is nonsingular so that the system (2.42) has a solution. In some cases the matrix **A** assumes one of the following particular forms: 

- diagonal matrix, in which the non-zero elements are laying on its main diagonal only, i.e.: 



- identity matrix, which is a diagonal one with all elements on the main diagonal equal to 1: 



Usually the symbol **I** is reserved for this matrix. 

- lower triangular matrix having non zero elements on the main diagonal and below: 



2.2 Solution of Systems of the Linear Algebraic Equations 

71 

**Fig. 2.13** Banded matrix 

having bandwidth equal to 6 



- upper triangle matrix having non zero elements on the main diagonal and above: 



- banded matrix, which has all non zero elements concentrated around the main diagonal within a band of specified bandwidth (Fig. 2.13); 

- sparse matrix, which has a large number of elements equal to zero – banded matrices can be sparse if the band is narrow or if there are many zeros within the band; 

- symmetric matrix for which _aij_ = _aji_ . 

For the cases listed above one can take advantage of the matrix structure to make the solution algorithm much more efficient. 

The methods for solving the systems of algebraic equations are divided into two groups: 

- direct methods, 

- iterative methods. 

Direct methods are capable to provide an exact solution after executing a finite number of mathematical operations (it is true on condition that the round-off errors do not exist). Iterative methods start from an initial guess of the solution and provide a series of its better approximations. If this series is convergent, i.e. if it tends to a limit, this limit is a solution of the considered system (2.42). Therefore the iterative 

2 Methods for Solving Algebraic Equations and Their Systems 

72 

methods are capable to provide the approximate solution only, within the assumed tolerance. 

The choice of a suitable method of solution depends on the dimension of considered system of equations. Generally it is assumed that direct methods are efficient for the systems having rather small dimensions, say 60 by 60. For larger systems, especially with very sparse matrices, iterative methods are recommended as more effective. In such a case application of the direct methods is a waste of computer memory and time of computation. However in the case of open channel flow modeling situation is particular. As results from Chapter 1, all derived equations or their systems are one dimensional. Consequently, the final systems of algebraic equations obtained from discretization of the ordinary or partial differential equations, even those containing hundreds of unknowns, have banded matrices with very narrow bandwidth. For instance, as we will see in Chapters 6, 7 and 8, for 1D transport equation solved by the implicit methods one obtains systems with tri-diagonal matrices, while for the system of Saint Venant equations the bandwidth is equal to 5 or 7, according to the applied method of solution. The matrices’ bandwidths become wider for flow in open channel network. However at the same time they become very sparse, since the total number of the non-zero coefficients in each matrix row is still very small. Consequently, in the case of the equations applied in open channel hydraulics it can be reasonable to apply direct methods to solve even very large systems of equations. However, this can be done on condition that the implemented algorithms for these methods will take into account the untypical properties of matrix. For instance, very efficient solver basing on the Gauss elimination method can be obtained on condition that it works on the non-zero elements only. For this reason this section is limited to direct methods. 

### **_2.2.2 Gauss Elimination Method_** 

Let us begin with the solution of a system of linear algebraic equations with upper triangular matrix: 



or in scalar form: 



Assuming that _uii_ ̸ = 0 ( _i_ = 1, 2, _. . ._ , _N_ ), the unknowns can be calculated in the inverse order: _xN_ , _xN_ –1, _. . ._ , _x_ 1 using the following formulas: 

2.2 Solution of Systems of the Linear Algebraic Equations 

73 



Equations (2.49) can be rewritten shorter as: 



Since the unknowns are calculated from last one to the first one, this algorithm is known as back substitution. Similarly easily one can solve the system of equations with lower triangular matrix. In such a case the computational process is called forward substitution (Bjorck and Dahlquist 1974). 

The Gauss elimination method is the most important direct method to solve any system of linear algebraic equations. It bases on such a way of elimination of the subsequent unknowns, which finally reduces the solved system to the one with upper triangular matrix as Eq. (2.48). Afterwards, the obtained system is solved using previously presented algorithm. 

Now consider the system (2.42) rewritten follows: 



The elimination is performed in multiple sweeps through the whole system and in each sweep the coefficients are modified. Thus, we introduce additional superscript to distinguish coefficients obtained in subsequent sweeps. The superscript equal to 1 is designated to original matrix, i.e.: _a_<sup>(1)</sup> _ij_<sup>=</sup><sup>_aij_and</sup><sup>_b_</sup> _i_<sup>(1)</sup> = _bi_ . Using this convention the system (2.51) is rewritten as: 

74 2 Methods for Solving Algebraic Equations and Their Systems 



Assume that the coefficient matrix is not singular and _a_<sup>(1)</sup> 11̸<sup>= 0. Otherwise, the sys-</sup> tem (2.52) must be rearranged. Let us carry out the following sequence of operations for _i_ = 2, 3, _. . ._ , _N_ : 

- define the multiplier _a_<sup>(1)</sup> _i_ 1<sup>_/ a_</sup> 11<sup>(1),</sup> 

- multiply the first equation by this multiplier, 

- subtract the first equation from _i_ th equation. 

In such a way one obtains a reduced system, which has dimension ( _N_ – 1) × ( _N_ – 1). Its coefficients are _a_<sup>(2)</sup> _ij_<sup>. This system written together with the first equation</sup> of original system (2.51) is as follows: 



Its coefficients are given by the formulas: 



Similarly to the preceding step, assume that _a_<sup>(2)</sup> 22̸<sup>= 0 and repeat the same sequence</sup> of operations but for the reduced system (2.53). We obtain the second reduced system: 



75 

2.2 Solution of Systems of the Linear Algebraic Equations 





Continuing this way of elimination, after _N_ – 1 steps we obtain the following reduced system of equations: 



The coefficients of the above system were calculated by the following formulas: 



where: 



Thus, the final result of elimination is a system with upper triangular matrix (2.55). Now the determination of the unknowns can be done easily, using the formulas (2.50a) and (2.50b). 

The elements _a_<sup>(1)</sup> 11<sup>,</sup><sup>_a_(2)</sup> 22<sup>,</sup><sup>_a_(3)</sup> 33<sup>,</sup><sup>_. . ._,</sup><sup>_a_</sup> _NN_<sup>(</sup><sup>_n_),determiningtheeliminationprocess,are</sup> called the pivot elements. The elimination was possible since we arbitrary assumed that their values differ to zero. If in _k_ th step of elimination the pivot element appears to be equal to zero, it is necessary to rearrange the matrix by changing of the rows in such a way that at position ( _k_ , _k_ ) non zero element must appear (Fig. 2.14). Therefore, row _k_ is swapped with row _l_ for which _a_<sup>(</sup><sup>_k_)</sup> _lk_ ̸<sup>= 0 (Fig. 2.14).</sup> 

̸ It is recommended to choose such row for which: 



where _i_ is the row index. 

There are two cases when the pivot elements certainly differ from zero: 

- when matrix **A** has dominating main diagonal, i.e. when: 

76 

2 Methods for Solving Algebraic Equations and Their Systems 

**Fig. 2.14** Matrix of coefficients after _k_ steps of elimination 



<!-- Start of picture text -->
k<br>l<br><!-- End of picture text -->







- when matrix **A** is symmetrical and positively defined, i.e. when it satisfies the following conditions: 



and 



For any matrix the condition (2.58) may be verified easily, whereas the condition (2.60) is more difficult to check. More information on the problem is given by Bjorck and Dahlquist (1974). 

### **_2.2.3 LU Decomposition Method_** 

Assume that it is possible to decompose the matrix **A** of the system (2.42) and to present it in the form of product of two matrices: lower triangular matrix and upper triangular matrix: 



Then the considered system (2.42) is equivalent to the following one: 



The system (2.62) can be split into two systems: 

2.2 Solution of Systems of the Linear Algebraic Equations 

77 





which should be solved subsequently. 

There is a theorem which states that in fact, each matrix **A** may be rearranged in such a way, that the decomposition on the triangle matrices becomes possible (Bjorck and Dahlquist 1974). This fact results from the equivalency of the Gauss elimination method and **LU** decomposition. Actually, the matrix obtained as the result of elimination is the upper triangular matrix. Accordingly, the elements of the lower matrix are _lik_ = _a_<sup>(</sup> _ik_<sup>_k_)</sup><sup>_/ a_(</sup> _kk_<sup>_k_), which occur in Eq. (2.56) for</sup><sup>_i_= 2, 3,</sup><sup>_. . ._,</sup><sup>_N_;</sup><sup>_k_=</sup> 1, 2, _. . ._ , _i_ – 1 as well as by the elements at the main diagonal _lii_ = 1 for _i_ = 1, 2, _. . ._ , _N_ . Therefore one can write: 



Note that in the decomposition of **A** using the Gauss elimination the vector of right side hand **B** was not involved. This is an advantage of **LU** decomposition technique, since one can decompose **A** only once and after then to use **L** and **U** for various vectors of right side hand. Such situation occurs very often. 

Discretization of 1D partial differential equation using implicit method usually leads to systems of linear algebraic equation (2.42) with tri-diagonal matrices: 



Such a system can be solved using a very simple and effective algorithm, based on the **LU** decomposition. Matrix (2.66) is decomposed in following triangle matrices: 

2 Methods for Solving Algebraic Equations and Their Systems 

78 



The elements _l_ 2, _l_ 3, _. . ._ , _lN_ and _u_ 1, _u_ 2, _u_ 3, _. . ._ , _uN_ are computed using the following formulas: 





Knowing the triangular matrices one can determine the vector **X** by solving the two systems (2.63) and (2.64). The computations are carried out as follows: 





and 





If the system of equations is solved only once for given matrix **A** and the right side hand **B** , then it is not necessary to remember the elements _li_ , and the algorithm becomes simpler: 





2.3 Solution of Non-linear System of Equations 

79 

and 





The presented technique of solution is called the Thomas method or “double sweep” method (Fletcher 1991). This algorithm is very useful and can be applied for many open channel flow problems. 

The Gauss elimination method or **LU** decomposition are especially suitable to solve effectively the systems with banded matrices. After elimination the matrices **L** and **U** are also banded. The only disadvantage is that during elimination the zeros within the band are replaced by non zero elements. 

### **2.3 Solution of Non-linear System of Equations** 

### **_2.3.1 Introduction_** 

Previously, in Section2.2 we considered systems of linear algebraic equations of the form: 



where: **A** is square matrix of the coefficients, **X** is vector of unknowns and **B** is vector of right hand side defined as follows: 



where _aij_ and _bi_ were constant numbers. However, in many engineering applications one obtains systems of algebraic equations in which the coefficients are functions of the unknowns, i.e. _aij_ = _aij_ ( _x_ 1, _x_ 2, _. . ._ , _xN_ ) or/and _bij_ = _bij_ ( _x_ 1, _x_ 2, _. . ._ , _xN_ ). Such systems are called non-linear. In open channel hydraulics the systems of non-linear equations usually arise as a part of more complex algorithms. For instance, some numerical methods of solution applied for the ordinary and partial differential equations or their systems lead to the systems of algebraic non-linear equations. In the next chapters we will see numerous examples of such systems. 

Usually, instead of the form (2.94), the following notation for the non-linear systems is used: 



2 Methods for Solving Algebraic Equations and Their Systems 

80 

where: 

**X** = ( _x_ 1, _x_ 2, _x_ 3, _. . ._ , _xN_ )<sup>_T_</sup> , **F** ( **X** ) = ( _f_ 1( **X** ), _f_ 2( **X** ), _. . ._ , _fN_ ( **X** ))<sup>_T_</sup> , _T_ – transposition symbol, _N_ – dimension of system. 

Of course, both forms are equivalent, since we have: 



and both will be used further. In scalar notation Eq. (2.74) is written as: 



The vector **X** , which satisfies Eq. (2.76) is its solution. 

All numerical methods of solution of the non-linear systems are iterative ones. In the next sections we present the Newton method and the Picard method, which are standard methods commonly applied in open channel hydraulics. 

### **_2.3.2 Newton Method_** 

Assume that approximate solution of Eq. (2.74) is known. Then one can write: 



where: 

**X** – exact solution of Eq. (2.74), **X**<sup>(</sup><sup>_k_)</sup> – solution approximation _i_ iteration _k_ , **_�_ X**<sup>(</sup><sup>_k_)</sup> – vector of differences between exact and estimate, _k_ – index of iteration. 

It is assumed that the functions being the components of system are continuous and differentiated with regard to vector **X** . Since form definition results that **F** ( **X** ) = 0, then using the Taylor series expansion around **X**<sup>(</sup><sup>_k_)</sup> , one can write: 



Solution of Non-linear System of Equations 

2.3 

81 

It means that the Taylor series was truncated and all terms with the derivatives of order higher than one were neglected. The correction vector can be expressed as follows: 



since **X**<sup>(</sup><sup>_k_+1)</sup> estimates of exact solution **X** . Therefore one can write: 



where: 



is the Jacobian matrix of system (2.74). Then the final form of the Newton method is following: 



One can see, that the method applied in the form of Eq. (2.81) is time and memory consuming. In each iteration it requires to build the Jacobian matrix of dimension _N_ × _N_ , and next to inverse it. For these reasons the Newton method is applied rather in the form of Eq. (2.80), rewritten as follows: 



In such a way, instead of inversing of the matrix **J** , a system of linear equations must be solved with regard to the correction vector **_�_ X**<sup>(</sup><sup>_k_)</sup> . Afterwards the new estimate of **X** is calculated: 



This approach is more efficient especially when **J** is banded. Note, that the inversion of a banded matrix produces a matrix, which looses banded form and has all non zero elements. 

In order to reduce the computational time sometimes the original Newton method is modified, similarly to the modification of this method for scalar equation. Instead 

2 Methods for Solving Algebraic Equations and Their Systems 

82 

of computing the Jacobian matrix **J** in each iteration, the Jacobian from the first estimate is applied is all subsequent iterations: 



The convergence of this iteration is slower, but the Jacobian matrix does not have to be calculated in each iteration what is important when the derivatives must be calculated numerically. The criteria of convergence will be discussed in next section. 

### **_2.3.3 Picard Method_** 

The Picard method, also known as the consecutive substitution, is a fixed-point iteration developed for a system of non-linear equations. From the subsequent equations of the system (2.76) one unknown is isolated at left side of equality sign. Then one obtains: 





or using the matrix notation: 



where: 



Given the first estimate **X**<sup>(0)</sup> , one can generate the following sequence of approximations: 



where _k_ is iteration index. If this sequence tends to the limit **X** for _k_ →∞, then this limit is the solution of system (2.74). 

Modified variants of the Picard method are often used. For instance the Picard method can be applied directly to solve the non-linear system in form of Eq. (2.73). In this case, it is given as: 



2.3 Solution of Non-linear System of Equations 

83 

Another version of the method is obtained by transformation of Eq. (2.88) to a formula similar to the Newton one. To this end the term **A**<sup>(</sup><sup>_k_)</sup> · **X**<sup>(</sup><sup>_k_)</sup> is subtracted from both sides of Eq. (2.88): 



Substitution of Eqs. (2.79) and (2.75) in Eq. (2.89) yields 



Equation (2.90) differs from the Newton method in the matrix of coefficients only. Since in Eq. (2.90) an original matrix of the solved system is involved then it is simpler. As we will see in Chpater 4, this method can be quite effective. 

The iterations carried out with the Newton or Picard methods are stopped when the criterion for convergence is satisfied. In both methods one can apply the following tests: 



where: 

_k_ – iteration index, 

_ε_ – positive number being a specified tolerance. 

In this condition the differences between two consecutive iterations are examined. The above criterion is suitable for the cases when the convergence processes is relatively fast. Checking of the solution accuracy for slowly convergent iterations should be carried out thoroughly. Although the consecutive iterations vary insignificantly, the difference between the exact solution and its estimate in _k_ th iteration may be appreciable. Such situation is illustrated in Fig. 2.15. 



<!-- Start of picture text -->
δ<br>exact value<br>x<br>δ<br>a<br>ε<br>ε<br>b<br>* * * * * * * * * * * * * * *<br>*<br>( = 0) k<br>x  initial estimate<br>number of iterations  k<br><!-- End of picture text -->

**Fig. 2.15** Influence of the criterion (2.91) on final error of solution for: ( **a** ) quickly convergent iterations; ( **b** ) slowly convergent iterations 

2 Methods for Solving Algebraic Equations and Their Systems 

84 

To stop the iterations another criterion, in the form of the Euclidean norm, may be employed. This norm, which serves to quantify the size of vector, this case is defined as norm of residual vector: 



The iterations are terminated when the following relation is satisfied: 



where _ε_<sup>′</sup> > 0 determines assumed tolerance. 

Experience shows, that the Newton method converges very quickly on condition that the first estimate is close to the solution. Otherwise it can suffer from possible divergence. Generally it is said, that the Newton method has poor global convergence (Press et al. 1992). As far as the Picard method is considered, it is slower, but converges even if the initial guess is far from the solution. These properties will be confirmed in Chapter 4 while solving some open channel flow problems. 

### **References** 

Bjorck A, Dahlquist G (1974) Numerical methods. Prentice-Hall, Englewood Cliffs, NJ Chapra SC, Canale RP (2006) Numerical methods for engineers. McGraw-Hill, New York Fletcher CAJ (1991) Computational techniques for fluid dynamics, vol. 1. Springer-Verlag, Berlin Press WH, Teukolsky SA, Veterling WT, Flannery BP (1992) Numerical recipes in C. Cambridge 

University Press, Cambridge 

Roberson JA, Cassidy JJ, Chaudhry MH (1998) Hydraulic engineering, 2nd edn. Wiley, New York 

## **Chapter 3 Numerical Solution of Ordinary Differential Equations** 

### **3.1 Initial-Value Problem** 

### **_3.1.1 Introduction_** 

Ordinary differential equations (ODEs) contain derivatives of an unknown function with respect to a single independent variable. Such equations describe for example steady flow in open channel (Eqs. 1.97, 1.108 and 1.109). In this case the independent variable is the spatial coordinate _x_ . Another example is the storage equation (1.122), which is an ODE with respect to time. More time-dependent ODEs will be introduced in Chapter 9. Moreover ODEs with regard to time appear when unsteady flow and transport equations are solved using the finite element method. Their solution is one of the steps in the computational process. 

Consider the following equation: 



where _x_ is the independent variable, whereas _y_ is the dependent variable. Integration of Eq. (3.1) yields: 



where _C_ is the integration constant. Thus, the obtained solution is not unique. Indeed, we have an infinite number of solutions satisfying Eq. (3.1), corresponding to an infinite number of different possible values of the constant _C_ . However, in practice we are interested rather in a unique solution for the specified range of _x_ from the interval ⟨ _a_ , _b_ ⟩. To choose the proper solution, an auxiliary condition must be formulated. In the case of Eq. (3.1) it is called initial condition. Then the problem can be formulated as follows: determine the function _y_ ( _x_ ),which satisfies both 

85 

R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_3, ⃝C Springer Science+Business Media B.V. 2010 

86 

3 Numerical Solution of Ordinary Differential Equations 

the ordinary differential equation (3.1) in the interval ⟨a, b⟩ and the specified initial condition: 



where _a_ and _y_ 0 are specified values. 

The problem of solution of Eq. (3.1) formulated in such a way is called an initial-value problem for the ordinary differential equation. It is assumed that the initial-value problem has a unique solution, i.e. there is only one function _y_ ( _x_ ) which simultaneously satisfies Eq. (3.1) and the initial condition (3.3). The problem of existence and uniqueness of solution is discussed for instance by Ascher and Petzold (1998). 

In majority of engineering applications the initial-value problem for ordinary differential equations is solved using numerical methods. This approach allows us to compute the estimates _y_ 1, _y_ 2,..., _yN_ , of the exact solution _y_ ( _x_ 1), _y_ ( _x_ 2),..., _y_ ( _xN_ ) at selected points _x_ 1, _x_ 2,..., _xN_ within the interval ⟨ _a_ , _b_ ⟩. Starting from the point ( _a_ , _y_ 0) given by the specified initial condition, we have to move over the interval ⟨ _a_ , _b_ ⟩ from one node to the next, calculating the approximated values of the exact solution _y_ ( _xi_ ) until the endpoint _xN_ = _b_ is reached. It is expected that the applied method will generate the approximations _y_ 1, _y_ 2, _. . .yi. . ._ which reproduce the true shape of the function _y_ ( _x_ ) with sufficient accuracy (Fig. 3.1). 

The accuracy of approximation depends on the following two factors: 

- selection of the points _x_ 1, _x_ 2, _. . ._ , 

- method of calculation of the estimates _y_ 1, _y_ 2, _. . ._ . 

The distance between two neighboring nodes, denoted by _�xi_ is called the step size: 



A constant step size is often applied _�xi_ = _�x_ = const and many numerical methods proposed for integration of the ordinary differential equations were derived for constant _�x_ . In principle, constant stepsize can be easily applied for 



<!-- Start of picture text -->
y<br>y ( x )<br>y 0<br>a = x 0 x 1 x 2 x N =  b x<br><!-- End of picture text -->

**Fig. 3.1** Function _y_ ( _x_ ) and its estimate calculated using the numerical method 

3.1 Initial-Value Problem 

87 

time-dependent ODEs, although even in this case variable stepsizes may be recommended for the sake of efficiency. As far as the space-dependent ODEs are considered, constant _�x_ can be used for flow in artificial channels having a constant bed slope and constant shape of the cross-sections. In such a case it is easy to determine the parameters of cross-section as wetted area, wetted perimeter and surface width, as a function of position, i.e. of variable _x_ . Conversely, integration of the same equations for natural channels must be carried out with variable step size. The shape of the rivers’ cross-sections is irregular and varies continuously along their axes. The computational nodes are chosen in such a way that they correspond to the cross-sections for which data obtained from field measurements are available. Therefore, we must apply non-uniform point spacing along _x_ axis. 

The methods of numerical integration of ODEs can be classified according to different criteria. In general, numerical integration schemes lead to algebraic equations, where the unknown represents the value of the function _y_ ( _x_ ) at the next integration point _yi+_ 1. If it can be computed using information only from the last node _i_ , then the method is called one-step. The one-step methods are also called self starting methods. It means that the initial condition is sufficient to perform the computing process by these methods. If the information from more than one preceding step is required ( _yi_ , _yi–_ 1, etc) then the method is called multi-step. To initiate multistep methods, apart from imposed the initial condition, additional values of _y_ at the first few points, i.e. _y_ 1, _y_ 2, _. . ._ must be calculated using a one-step method. 

If the resulting algebraic equation is linear, i.e. _yi+_ 1 can be isolated at one side of the equation: 



then the method is called explicit. In the opposite case _yi+_ 1 cannot be extracted from the algebraic formula, and the following nonlinear relation arises: 



Such a scheme is called implicit. The nonlinear equation has to be solved with regard to _yi_ +1 in each step, using an iterative method. Usually the fixed-point method is applied. Its implementation for Eq. (3.6) is called the “predictor-corrector” method. The prediction of _yi_ +1 is performed using the explicit method, whereas the formula (3.6) serves to its correction. 

There are a variety of methods which belong to the mentioned types. Due to exceptional properties of the rivers only some of them are applicable in open channel hydraulic and therefore only some of them will be presented in this chapter. 

### **_3.1.2 Simple Integration Schemes_** 

Let us begin with a short presentation of the finite differences. The finite difference, being an approximation of the derivative, can be used to derive directly some 

3 Numerical Solution of Ordinary Differential Equations 

88 

methods of solution for both the initial-value and the boundary-value problems. Appropriate difference formula comes from the Taylor series expansion of a function around considered point _x_ . For the function depending on one independent variable only, the Taylor series can be written as follows: 



As this series has infinite number of terms, taking into account any finite number of its terms introduces a truncation error. Consequently instead of the exact value of function its approximation is obtained. Of course, the error of approximation depends on the number of terms taken into consideration. Assuming that only the first three terms are taken into account, an estimate of _y_ ( _xi+_ 1) can be expressed using Eq. (3.7), rewritten in the following form: 



where: 

_yi_ , _yi_ +1 – the values of _y_ ( _x_ ) at node _i_ and _i_ +1 respectively, _�x_ – distance between the nodes _i_ and _i_ +1 

The term _O_ ( _�x_<sup>3</sup> ) indicates that the truncation error is of the order _�x_<sup>3</sup> . It means that the error varies proportionally to the step size _�x_ raised to the 3rd power. If we take a half of step size then the estimated error of _yi_ +1 is reduced 8 times. 

Directly from Eq. (3.8) one can find an estimate of the derivative of 1st order: 



One can notice, that the following finite difference 



approximates the derivative of _y_ ( _x_ ) at node _i_ with accuracy of first order, i.e. _O_ ( _�x_ ). This formula is called the forward difference. 

Similar approach can be applied to derive the backward difference formula. To this order the Taylor series expansion is performed to provide with the estimate of _y_ ( _xi_ –1). It takes the following form: 



3.1 Initial-Value Problem 

89 

This equation yields the formula: 



The approximation by backward difference introduces a truncation error of order _O_ ( _�x_ ), similarly to the forward difference (3.10). Subtracting Eq. (3.8) from Eq. (3.11) gives: 



from which one obtains the approximating formula known as the centered difference: 



In contrast to the previous formulas this one ensures accuracy of 2nd order, i.e. the truncation error is _O_ ( _�x_<sup>2</sup> ). 

All the presented formulas approximating the derivative of the 1st order can be used to derive certain basic methods for numerical solution of the initial-valueproblem. To this end let us approximate Eq. (3.1) at node _i_ (Fig. 3.2) using the previously derived finite differences. Subsequent substitution of the formulas (3.10), (3.12) and (3.14) in Eq. (3.1) yields: 





which gives the explicit or forward Euler method: 



**Fig. 3.2** Sketch for approximation of Eq. (3.1) 



<!-- Start of picture text -->
y<br>θΔ x (1- θ)Δ x<br>P<br>x i −1 xi xp xi +1 x<br>Δ x Δ x<br><!-- End of picture text -->

3 Numerical Solution of Ordinary Differential Equations 

90 

- For the backward difference: 



which gives the implicit or backward Euler method: 







from which results the Nystrom method: 



In the same way further methods can be derived. Assume that the approximation of the derivative is performed at midpoint of the interval ⟨ _xi_ , _xi_ +1⟩, in which the value of _f_ ( _x_ , _y_ ) is taken as arithmetic average from both nodes. Then Eq. (3.1) becomes: 



This is known as the implicit trapezoidal method: 



Both Euler methods and the trapezoidal method can be rewritten as a single unified formula. To obtain this formula let us approximate the differential equation (3.1) at point _P_ (Fig. 3.2). 

The position of point _P_ , which may move within the interval ⟨ _xi_ , _xi_ +1⟩, is determined by the weighting parameter _θ_ defined as follows: 



Since _xi_ ≤ _xP_ ≤ _xi_ +1 then _θ_ ranges from 0 to 1. Approximation of Eq. (3.1) gives: 



The value of derivative _f_ ( _x_ , _y_ ) at point _P_ is calculated by linear interpolation between the endpoints of the interval: 



3.1 Initial-Value Problem 

91 

Substitution of Eq. (3.25) in Eq. (3.24) yields: 



This scheme is equivalent to: 

- the forward Euler method for _θ_ = 0, 

- the implicit trapezoidal rule for _θ_ = 1/2, 

- the Galerkin method for _θ_ = 2/3, 

- the backward Euler method for _θ_ = 1. 

An alternative way of derivation of theses formulas is to consider the integration of ordinary differential equation (3.1) over the domain defined by the boundaries of the interval: 



From Eq. (3.27) results: 



The presented methods differ in the way of approximating of integral, i.e. the quadrature rule used in its calculation. 

Let us consider the forward Euler method (3.16). This formula may be derived from Eq. (3.28) as well. For this purpose the integral in Eq. (3.28) must be calculated using the quadrature in the form of rectangular formula. If the area under the curve in the interval is approximated by the area of the rectangle having dimensions _Δx_ by _f_ ( _xi_ , _yi_ ) (Fig 3.3a) one obtains: 



Introducing this result in Eq. (3.28) one obtains the required forward Euler formula: 



The forward Euler method has a very simple geometrical interpretation shown in Fig. 3.3b. The function _y_ ( _x_ ) in the interval ⟨ _xi_ , _xi_ +1⟩ is replaced by its tangent at point 

3 Numerical Solution of Ordinary Differential Equations 

92 



<!-- Start of picture text -->
a) b)<br>y<br>f ( x y , ) f ( x y , )<br>f ( x yi    i , ) y ( x    i +1)<br>yi +1<br>Δ xf ( x y i    i , )<br>yi<br>x                                    xi                                                  i +1 x                                    xi                                                  i +1<br>Δ x Δ x<br><!-- End of picture text -->

**Fig. 3.3** Interpretation of the explicit Euler method 

_xi_ . From this figure results that the value of the step size _�x_ determines the accuracy of numerical solution. The difference _y_ ( _xi_ )– _yi_ increases with increasing _�x_ . 

Conversely to the forward Euler method, the backward one is obtained if in Eq. (3.28) the integral is approximated by the area of rectangle having dimensions _Δx_ by _f_ ( _xi_ +1, _yi_ +1) (Fig. 3.4): 



Consequently one obtains: 





<!-- Start of picture text -->
f ( x , ) y<br>f ( x , ) y<br>f ( x    y   i +1 ,  i  +1)<br>x                                                 x i i  +1 x<br>Δ x<br><!-- End of picture text -->

**Fig. 3.4** Interpretation of implicit Euler method 

3.1 Initial-Value Problem 

93 



<!-- Start of picture text -->
f ( x , ) y<br>f ( x    y   i +1 ,  i +1)<br>f ( x y , )<br>f ( x y i     i , )<br>x                                                 x i i +1 x<br>Δ x<br><!-- End of picture text -->

**Fig. 3.5** Interpretation of the implicit trapezoidal method 

In other words, the function _y_ ( _x_ ) in the interval ⟨ _xi_ , _xi_ +1⟩ is replaced by its tangent at _xi_ +1. 

If the trapezoidal quadrature formula is applied one can write (Fig. 3.5): 



Substitution of this result in Eq. (3.28) gives the trapezoidal formula (3.22): 



One can say that in this case the function _y_ ( _x_ ) is replaced in the interval ⟨ _xi_ , _xi_ +1⟩ by a straight line with the slope equal to the arithmetic average of the slopes at both endpoints of the interval. 

### **_3.1.3 Runge–Kutta Methods_** 

More accurate methods can be obtained by increasing the number of intermediate points between _xi_ and _xi_ +1. For example, the widely used Runge–Kutta methods can be expressed by the following general formulas: 



3 Numerical Solution of Ordinary Differential Equations 

94 

where 





In these formulas _m_ ≥1, _wj_ , _cj_ , _ajl_ are numerical coefficients. If at node _xi_ an estimate _yi_ is known, then _yi_ +1 at the node _xi_ +1 = _xi_ + _�x_ is obtained from Eq. (3.35a), which uses the previously calculated coefficients _k_ 1, _k_ 2, _. . ._ , _km_ . This is repeated in each step of integration: _i_ = 0, 1, 2, _. . ._ , _N_ where _N_ is number of steps in the interval ⟨ _a_ , _b_ ⟩. If the number of components in Eq. (3.35a) is _m_ , then the corresponding Runge–Kutta method is called _m_ -stage. 

Comparison of Eqs. (3.35a) and (3.28) indicates that in fact the Runge–Kutta methods use some specific estimation of the integral. One can write that: 



Where _f_ ( _x_ , _y_ ) is a certain representative average value of the derivative _dy_ / _dx_ in the interval ⟨ _xi_ , _xi_ + _�x_ ⟩. One can assume that as a quadrature the rectangular method is applied. The area under the curve _f_ ( _x_ , _y_ ) is approximated by the area of rectangular having a base equal to _Δx_ and height defined as an average value calculated with the weighting coefficients _wj_ . 

Let us consider the simplest, one stage Runge–Kutta method with _m_ = 1. Since in this case 



then the condition _w_ 1 = 1 must be satisfied and consequently: 



Then general formula (3.35a) in this case takes the following particular form: 



which is equivalent to the forward Euler formula presented earlier (3.16) (Legras 1971). 

95 

3.1 Initial-Value Problem 

Improvement of the solution accuracy is possible by increasing the number of stages. For _m_ = 2 one obtains two versions of the Runge–Kutta method. They are: 

- the improved Euler method for which: 







- the Euler–Cauchy method for which: 







Both versions have simple geometrical interpretations shown in Figs. 3.6 and 3.7 respectively. 

In the improved Euler method the function _y_ ( _x_ ) is represented in the interval ⟨ _xi_ , _xi_ +1⟩ by a straight line having slope calculated at midpoint, i.e. at _xi_ + _�x_ /2 (Fig. 3.6). The Euler–Cauchy method uses the representative value of the derivative _f_ ( _x_ , _y_ ) 



<!-- Start of picture text -->
y y ( x )<br>y  ( x i +1)<br>yi +1<br>Δ x k 1<br>slope f (  xi  + 2 ,   y +i   ) 2<br>slope  f ( xi , yi )<br>yi<br>x                                                                  xi       i +1 x<br>Δ x /2 Δ x /2<br><!-- End of picture text -->

**Fig 3.6** Interpretation of the improved Euler method 

96 

3 Numerical Solution of Ordinary Differential Equations 



<!-- Start of picture text -->
y slope ( f x i +Δ x ,   y i +Δ x k   1 )<br>y (    ) xi +1<br>yi +1 slope f ( x  i + y i ) +  f ( x  2 i +Δ x ,  + yi Δ xk   1)<br>slope ( f x y i , ) i<br>Δ x . k 1<br>yi<br>x                                                          xi i +1 x<br>Δ x<br><!-- End of picture text -->

**Fig. 3.7** Interpretation of the Euler–Cauchy method 

equal to the arithmetic average value taken for both endpoints of the interval: _xi_ and _xi_ +1 (Fig. 3.7). 

The most popular and widely applied version of the Runge–Kutta method is the 4-stage one. For _m_ =4 one obtains the following formulas (Legras 1971): 











This version is very often applied in open channel hydraulics, however rather to integrate the ordinary differential equations with time as the independent variable. There are the Runge–Kutta formulas derived up to _m_ =8 (Legras 1971). However, formulas with more than 4 stages are seldom used in engineering practice. The same is true for the multistep methods, such as Adams–Bashford, Adams–Moulton or Backward Differentiation Formula (BDF) (see Ascher and Petzold (1998) for more details on these schemes). 

_Example 3.1_ A flood wave of known form is passing through a reservoir closed by a dam with a weir. Knowing that reservoir works accordingly to Eq. (1.122) compute 

3.1 Initial-Value Problem 

97 

the outflow from the reservoir _O_ ( _t_ ) through a weir. The storage equation (1.122) is applied in a simplified form: 



where: 

_t_ – time, 

_h(t)_ – water level above assumed datum, _F(h)_ – area of reservoir at the level of surface, _I(t)_ – inflow into reservoir, _O(t)_ – outflow from reservoir. 

The flood wave is described by the formula: 



where: 



The outflow _O(t)_ from the reservoir takes place through a weir (Fig. 3.8) Since the weir is contracted the flow is governed by the following discharge equation (Roberson et al. 1998): 





<!-- Start of picture text -->
A–A<br>H A L<br>A<br>p.<br>bottom<br>h<br>Z<br>datum<br><!-- End of picture text -->

**Fig. 3.8** Weir of a dam 

3 Numerical Solution of Ordinary Differential Equations 

98 

where: 

_H_ – head, 

_L_ – weir width, 

- _p_ – height of the dam, 

- _Z_ – bottom elevation above the assumed datum, 

- _g_ – acceleration due to gravity, 

_K_ – flow coefficient given as _K_ = 0.40 + 0.05 _H_ / _p_ (Roberson et al. 1997): 

Replacing in Eq. (3.45) the head _H_ with the water level _h_ one obtains: 



The area of the water surface _F_ varies with the water level elevation _h_ as showed in Fig. 3.9: 

Substitution of Eq. (3.162) in Eq. (1.160) yields: 



Solving this storage equation with appropriate initial condition one obtains the function _h_ ( _t_ ) representing the evolution in time of the water level in reservoir. The initial condition _h_ ( _t_ =0) = _h_ 0 can be found from the discharge equation (3.45). To this order one can assume that at the beginning the flow is steady with a constant discharge equal to baseflow _q_ 0. The corresponding head at the weir is given by as: 



**Fig. 3.9** Area of reservoir’s water surface versus elevation of the water level above the assumed datum 



<!-- Start of picture text -->
h  [m]<br>13<br>11<br>9<br>7<br>5<br>0.0 0.2 0.4 0.6 0.8 1.0 1.2 F  [  10 6   m. ]2<br><!-- End of picture text -->

3.1 Initial-Value Problem 

99 

**Fig. 3.10** Transformation of the flood wave _I_ ( _t_ ) flowing through reservoir for two different lengths of weir 



<!-- Start of picture text -->
Q  [m 3 /s]<br>I ( t )<br>100<br>O ( t  )– B = 12.00 m<br>80<br>60<br>40 O ( t  )– B = 7.50 m<br>20<br>0<br>0 24 48 72 96 120 t  [h]<br><!-- End of picture text -->

Therefore the required initial condition takes the following form: 



Knowing this condition one can use the formulas (3.42) for computation the approximated values of _h_ ( _i_ · _�t_ ) ( _i_ = 1, 2, 3, _. . ._ where _�t_ is time step and _i_ is index of time step). 

The following data were assumed: _q_ 0 = 2.50 m<sup>3</sup> /s, _qm_ = 100 m<sup>3</sup> /s, _tm_ = 6 h and _p_ = 5 m. Computations were performed for two values of weir’s length: _L_ = 12.0 m and _L_ = 7.50 m. This parameter mostly influences the discharge through weir so it determines the flood wave transformation process by reservoir. The results of calculations provided by the Runge–Kutta method are shown in Fig. 3.10. 

The changes of time step value in the range from 60 to 360 s only insignificantly affected the final results. 

### **_3.1.4 Accuracy and Stability_** 

Each numerical method of integration of the initial-value problem gives an approximate value of the exact solution. If we assume that at node _xi_ the exact value of solution is known, i.e. _y_ ( _xi_ ) = _yi_ , then the error at node _xi_ +1 is considered as generated in a single step. Obviously, the difference: 



being the error of approximation of the exact solution by the numerical method, should be as small as possible. Smaller value of _r_ ( _�x_ ) means more accurate method of solution. If instead of _yi_ +1, a formula of applied method, which depends on some 

3 Numerical Solution of Ordinary Differential Equations 

100 

coefficients and on the values of the derivative _f_ ( _x_ , _y_ ), is substituted in Eq. (3.50), then one can assume, that the error _r_ is a function of the step size _�x_ only. Therefore it can be expanded in the Taylor series with regard to _�x_ around zero (Ascher and Petzold 1998): 



If the difference (3.50) is equal to zero, all the terms of the Taylor series are equal to zero as well. However the error of approximation exists always, although its magnitude depends on the applied solution scheme. The error of approximation is defined by so called the order of integration method. The considered method is said to be of order _p_ , if for each initial-value problem the first _p_ terms of series (3.51) are equal to zero. Therefore, if a method is of order _p_ , then the error of approximation generated in a single step is: 



This definition is valid for all numerical methods of integration of the initialvalue problem. 

Let us examine accuracy of the methods described by Eq. (3.26): 



The linear multistep methods frequently applied to solve numerically initial value problems for both scalar ordinary differential equation and system of such equations, derived by means of an interpolating polynomial, have a common general form (Ascher and Petzold 1998): 



where: 



_k_ – number of past integration steps, 

_Δx_ – step size. 

Note that the method (3.53) belongs to this family as well. In this case we have _k_ = 1. The corresponding coefficients are given as follows: _α0_ = 1, _α1_ = −1, _β0_ = _θ_ , _β1_ = 1– _θ_ . 

3.1 Initial-Value Problem 

101 

Assume that _y_ ( _x_ ) is the exact solution of the considered ordinary differential equation (3.1) and it possesses the required derivatives. Introducing this function into formula (3.54) one obtains a local error of solution _ri_ : 



As it was stated above, the order of the method can be found by the analysis of the local truncation error. Thus, the nodal values of function _y_ ( _x_ ) and its derivative _f_ ( _x_ ) in Eq. (3.55) are expanded in Taylor series around the node _i_ . Consequently, the error _ri_ will be also expressed in the form of Taylor series: 



with the following coefficients _Cp_ : 



Calculation of these coefficients allows us to find the order of linear multistep method. If _C0_ , _C1_ , _. . ._ , _Cp_ = 0, _Cp_ +1̸=0 then considered method is of order _p_ (Ascher and Petzold 1998). For Eq. (3.53) we obtain: 









One can notice that the method (3.53) is of 1st order for θ̸=1/2 and it is of 2nd order for _θ_ = 1/2. Therefore one can say that: 

- both explicit ( _θ_ = 0) and implicit ( _θ_ = 1) Euler methods are of 1st order since _C_ 0 = 0, _C_ 1 = 0 and _C_ 2̸ = 0, 

- the trapezoidal implicit method ( _θ_ = 1/2) is of 2nd order since _C_ 0 = 0, _C_ 1 = 0, _C_ 2 = 0 and _C_ 3̸ = 0. 

3 Numerical Solution of Ordinary Differential Equations 

102 

The first non-zero coefficient _Cp_ +1 is called the error constant of the method. Note that it is equal to 1/2 or –1/2 for the Euler methods and –1/12 for the implicit trapezoidal rule. 

The second important property of each method of integration is the numerical stability. Roughly speaking, stability means that if the initial condition is slightly changed, then the solution at following points will be also only slightly changed with respect to the original solution. Unstable methods tend to produce oscillatory solutions with unlimited growth of numerical error. To examine this question let us express the linear multistep method in terms of the so-called characteristic polynomials (Ascher and Petzold 1998): 



where _Z_ is a complex number. 

For considered Eq. (3.53) these polynomials take the following forms: 





The region of absolute stability of any method is given by the ratio of both polynomials 



where _i_ is imaginary unit, whereas _ϕ_ ranges in interval ⟨0, 2 _π_ ⟩. A picture of the stability region is obtained by plotting of boundary given by Eq. (3.61) on the complex plane. Substituting Eq. (3.60) in Eq. (3.61) yields: 



Using the following well known relation (McQuarrie 2003): 



Equation (3.62) is rewritten as follows: 



3.1 Initial-Value Problem 

103 

Division of the complex numbers gives: 



One can see that the extent of the region of absolute stability depends on the weighting parameter _θ_ . In Fig. 3.11 are shown the regions corresponding to the selected values of _θ_ . Note that for _θ_ = 0 (explicit Euler method) the region of absolute stability is very small, having the form of unit circle at left part of the complex plane. Increasing of _θ_ increases the stability region, which for _θ_ = 1/2 (the implicit trapezoidal rule) contains the whole left half of the complex plane (Fig. 3.11b). Further increasing of _θ_ includes a fraction of the real part of the complex plane to the region of absolute stability as well (Fig. 3.11a). The largest region of stability is obtained for the implicit Euler method corresponding to _θ_ = 1. It contains entire complex plane except the shadowed unit circle (Fig. 3.11a). 

The theory of the numerical methods for initial value problem in ODEs distinguishes a very important family kind of the so called A-stable methods. This term should not be mistaken with the absolute stability. The difference method is considered as A-stable if its region of absolute stability covers the whole left part of complex plane. This type of methods is recommended for solving so called stiff systems of the ordinary differential equations (Ascher and Petzold 1998). 

In the case of Eq. (3.53) the real part of the complex number defining the region of stability (3.64) can be reduced to the following form: 



Since 0 ≤ _ϕ_ ≤ 2 _π_ then from Eq. (3.65) results that the region of absolute stability of the method (3.53) will be kept at right half of the complex plane if only: 



This condition confirms the results presented in Fig. 3.11. The method (3.53) will be A-stable as long as its weighting parameter _θ_ satisfies the condition (3.66). 

From practical viewpoint the most interesting methods for solving the ordinary differential equations are those which have large region of absolute stability. This explains the reasons of popularity of such methods as the implicit trapezoidal rule and backward Euler method. As we will see in later, these methods are of great importance in open channel hydraulic as well. 

More information on the problems of accuracy and stability analysis is given for example by Ascher and Petzold (1998), Bjorck and Dahlquist (1974), LeVeque (2007), Ralston (1965). 

3 Numerical Solution of Ordinary Differential Equations 

104 



<!-- Start of picture text -->
a)<br>Im ( z )<br>4<br>θ =1/2<br>θ =2/3<br>2<br>θ =1<br>0<br>–2<br>–4<br>–4 –2 0 2 4 6 Re ( z )<br>b)<br>Im ( z )<br>4<br>θ =1/2<br>θ =1/4<br>2<br>θ =0<br>0<br>–2<br>–4<br>–4 –2 0 2 4 6 Re ( z )<br><!-- End of picture text -->

**Fig. 3.11** Absolute stability regions of the method (3.53) for various values of weighting parameter _θ_ : ( **a** ) out of _shadow_ ; ( **b** ) inside of _shadow_ 

### **3.2 Initial Value Problem for a System of Ordinary Differential Equations** 

The initial-value problem, discussed previously for a scalar ordinary differential equation, can be also formulated for a system of ordinary differential equations of the following general form: 



105 

3.2 Initial Value Problem for a System of Ordinary Differential Equations 



The goal is to find such set of the functions _y_ 1( _x_ ), _y_ 2( _x_ ), _. . ._ , _yN_ ( _x_ ), which satisfy simultaneously the system of equations (3.67) in the considered interval ⟨ _a_ , _b_ ⟩ and the following initial conditions: 



where _y_ 1,0, _y_ 2,0, _. . ._ , _yN_ ,0 are given values. 

To solve the initial-value problem one can apply any of the methods derived for the scalar equation. These formulas remain the same. The only difference is that vectors are used instead of scalars. 

Using the vector notation the system (3.67) is rewritten shorter, as follows: 



where 



If for instance the implicit trapezoidal rule (3.139) is applied to solve the system (3.68), then one obtains: 



where _i_ is index of node and _�x_ is step size. Other formulas can be implemented in a similar manner. 

In many cases, for instance in the numerical solution of 1D partial differential equation using the finite element method, one obtains a systems of ordinary differential equations written in the following form: 



where **A** is a constant matrix, whereas **B** is a variable matrix dependent on time _t_ and sometimes, in addition on unknown vector **y** . Obviously, the system (3.70) can be reduced to the form of Eq. (3.68). However such a transformation is not recommended, since both **B** and **A** are tri-diagonal matrices. Diagonalization of Eq. (3.70) requires that the matrix **A** is inverted. However, it should be remembered 

106 

3 Numerical Solution of Ordinary Differential Equations 

that the inversion of a banded matrix gives a matrix **A**<sup>−1</sup> which has all non-zero elements. In such a way the advantage of the tri-diagonal matrix in Eq. (3.70) is lost. 

As it was mentioned in the preceding section, the most suitable methods for solution of the systems of ODEs are the A-stable methods. They are recommended to solve the stiff systems, in which the component equations describe the processes having different time scale. It means that there are some processes which occur much more rapidly than others. After Ascher and Petzold (1998), “An initial value problem is stiff in some interval if the step size needed to maintain stability is much smaller than the step size required to represent the solution accuracy”. However, it appears that among the standard methods only some of them can be classified as A-stable ones. It is proved that only the implicit methods of order not higher than 2, i.e. for _p_ ≤ 2, are A-stable (Ascher and Petzold 1998, Bjorck and Dahlquist 1974). Among all standard methods of solution of the initial-value problem only implicit Euler and implicit trapezoidal methods satisfy both mentioned conditions. The previously introduced unified formula (3.53) can be rewritten in vector notation as: 



with _θ_ ranging from 0 to 1. From the preceding section it is known that for _θ_ = 1 Eq. (3.71) becomes the backward Euler method, whereas for _θ_ = 1/2 it is the implicit trapezoidal one. Remember that this formula is A-stable for 1 _/_ 2 ≤ _θ_ ≤ 1 

To solve the system (3.70) the vector of derivatives: 



is substituted in Eq. (3.71). This gives: 



Multiplying both sides by **A** and grouping similar terms, yields the following system of algebraic equations: 



which can be rewritten as: 



where: 





3.3 Boundary Value Problem 

107 

In such a way the solution of the initial-value problem for a system of ordinary differential equations was reduced to the solution of the system of algebraic equations in each time step. This system may be linear or non-linear one according to the solved problem. In the latter case, an iterative method must be applied. Note that the matrix **R** is banded as the matrices **A** and **B** in the system (3.70). 

### **3.3 Boundary Value Problem** 

The system of the ordinary differential equations considered in preceding section: 



requires some auxiliary information to be solved. If all needed data are specified at the same value of the independent variable _x_ , then the considered problem is the initial-value one. This problem was discussed in previous section. In contrast to the initial-value problem one can formulate another one, in which the auxiliary conditions are specified at different values of the independent variable. Since usually they are imposed at two different points, corresponding to the ends of the interval ⟨ _a_ , _b_ ⟩, then the problem formulated in such a way is called two-point boundaryvalue problem or simply the boundary-value problem. Obviously, more than one additional condition is required only by a system of ordinary differential equations or by an equation of higher order than 1st, which can be reduced to the equivalent system of equations. In open channel hydraulics the ordinary differential equations usually appear in the form of a single equation of 1st order. Thus formally it is impossible to formulate a boundary-value problem directly, in the way mentioned above. However, such type of problem can be formulated if we assume that one of the parameters of the ODE is unknown, but constant in the interval ⟨ _a_ , _b_ ⟩, in which the considered equation is integrated (Ascher and Petzold 1998, Press et al. 1992). Therefore we have: 



where _λ_ is a constant parameter. Then one more ordinary differential equation is added to the system: 



This means that the constant _λ_ is considered as a function over the interval ⟨ _a_ , _b_ ⟩, which is independent of _x_ . 

In such a way we have the system of equations (3.78) and (3.79), for which one can formulate the boundary-value problem. This problem is formulated as follows: 

3 Numerical Solution of Ordinary Differential Equations 

108 

determine the function _y_ ( _x_ ) over the interval ⟨ _a_ , _b_ ⟩ which satisfies within this interval Eqs. (3.78) and (3.79) and moreover, which satisfies the following boundary conditions: 



and 



where _ya_ and _yb_ are specified values of _y_ at both endpoints of the interval. 

To solve numerically the above formulated problem two following approaches can be applied (Bjorck and Dahlquist 1974, Stoer and Bulirsch 1980): 

- the finite difference method, 

- the shooting method. 

Both methods are briefly described below, while more details on their application are provided in Chapter 4. 

In the finite difference method the interval of integration ⟨ _a_ , _b_ ⟩ is divided using _N_ nodes _xi_ into the segments of length _�x_ . Equation (3.79) is approximated at midpoint _xi_ + _�x_ /2 of each segment using the implicit trapezoidal formula (3.22). 



In such a way one obtains _N_ – 1 algebraic equations containing _N_ + 1 unknowns. There are _N_ values of the function _yi_ at each node and the constant parameter _λ_ . To this system two equations should be added, which correspond to the boundary conditions imposed at the endpoints of the interval. Consequently the closed system may be written as follows: 



where: 

**A** – sparse matrix having dimensions ( _N_ + 1)×( _N_ + 1), 

**X** = ( _y_ 1, _y_ 2, _. . ._ , _yN_ –1, _yN_ , _λ_ )<sup>_T_</sup> – vector of unknowns, 

**B** – vector of right side hand. 

Solving this system one obtains the nodal values of _y_ ( _x_ ) and the value of parameter _λ_ . 

The shooting method is based on converting the boundary-value problem into an equivalent initial-value problem (Chapra and Canale 2006). The solution is obtained 

3.3 Boundary Value Problem 

109 



<!-- Start of picture text -->
y<br>y(x, λ 2)<br>ya<br>y(x, λ )<br>y b<br>F( λ 1)<br>y(x, λ 1)<br>x = a x =b x<br><!-- End of picture text -->

**Fig. 3.12** Conversion of the boundary-value problem into a sequence of the initial-value problems 

indirectly. A sequence of solutions of the initial-value problems is carried out for various values of the parameter _λ_ until the condition imposed at _x_ = _b_ is satisfied with specified tolerance. Then the following initial-value problem: 



is solved. Since _y_ = _y_ ( _x_ , _λ_ ) then the solution depends on the assumed value of _λ_ . Solution of the boundary-value problem will be such a solution of the initial-value problem for which the second boundary condition: 





If we introduce the following function: 



which defines the difference between the value of _y_ ( _b_ ) computed for given value of _λ_ and imposed value of _y_ as the boundary condition _yb_ , then solution of problem is reduced to determination of the root of function _F_ ( _λ_ ). To find the root, at first the interval in which it is located must be done. To this order we should specify such two values of _λ_ , say _λ_<sup>(1)</sup> and _λ_<sup>(2)</sup> , for which the following relation is valid: 



Afterwards the bisection or false position method can be used to determine the root with required accuracy i.e. the approximated value of _λ_<sup>¯</sup> . 

3 Numerical Solution of Ordinary Differential Equations 

110 

### **References** 

Ascher UM, Petzold LR (1998) Computer methods for ordinary differential equations and differential – algebraic equations. SIAM, Philadelphia, PA 

Bjorck A, Dahlquist G (1974) Numerical methods. Prentice-Hall, Englewood Cliffs, NJ 

Chapra SC, Canale RP (2006) Numerical methods for engineers. McGraw-Hill, New York Legras J (1971) Méthodes et techniques de l’analyse numérique. Dunod, Paris 

LeVeque RJ (2007) Finite difference methods for ordinary and partial differential equations: 

Steady-state and time dependent problems. SIAM, Philadelphia, PA 

- McQuarrie DA (2003) Mathematical methods for scientists and engineers. University Science Books, Sausalito, CA 

- Press WH, Teukolsky SA, Veterling WT, Flannery BP (1992) Numerical recipes in C. Cambridge University Press, Cambridge 

Ralston A (1965) A fisrt course in numerical analysis. McGraw-Hill, New York Roberson JA, Cassidy JJ, Chandhry MH (1998) Hydraulic engineering, 2nd edn. Wiley, New York Stoer J, Bulirsch R (1980) Introduction to numerical analysis. Springer-Verlag, New York 

## **Chapter 4 Steady Gradually Varied Flow in Open Channels** 

### **4.1 Introduction** 

### **_4.1.1 Governing Equations_** 

In many practical applications the flow in open channels can be considered as steady and gradually varied. Such a flow can take place either in a single channel or in a channel network. The solution of steady flow equation can constitute a separate engineering problem or it can be a part of a more complex problem. The first case arises, for example, while computing the flow distribution and the flow profiles in a watering channel network. The second case can occur in unsteady flow modeling, when steady gradually varied flow in a channel network is assumed as the initial condition for unsteady flow equations. 

Sometimes the analysis of the steady gradually varied flow in channel network is carried out using the unsteady flow equations, i.e. the system of Saint Venant equations. Starting from the hydrostatic state, these equations are solved numerically with the boundary conditions corresponding to the required final steady state. Consequently the water stages and discharges asymptotically tend to their steady state values. However, such an indirect approach seems to be somewhat artificial. It is better to apply a direct approach, i.e. to use the appropriate equations describing steady flow and to solve them with a suitable numerical method. Such a concept is presented below. 

As it was shown in Section 1.6, the governing equations describing steady gradually varied flow can be obtained from the system of Saint Venant equations: 





where: 

_h_ – water level above the accepted datum, 

_Q_ – discharge, 

> R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_4, 

> ⃝C Springer Science+Business Media B.V. 2010 

111 

4 Steady Gradually Varied Flow in Open Channels 

112 

_A_ – wetted cross-sectional area, 

_x_ – longitudinal distance, 

_q_ – lateral inflow, 

_α_ – energy correction factor 

_S_ – friction slope given by equation: 



where: 

##### _nM_ – Manning coefficient, _R_ – hydraulic radius. 

Since Eqs. (4.1) and (4.2) are derived from the Saint Venant equations, they should be applicable for all types of open channels. Indeed, as will be shown later, numerical integration of Eq. (4.2) by the implicit trapezoidal rule leads to the well known step method, commonly applied in practice. Usually the step method is derived directly from the principle of energy conservation applied for the discrete system of two neighboring cross-sections along channel axis. 

### **_4.1.2 Determination of the Water Surface Profiles for Prismatic and Natural Channel_** 

For a rectangular channel and _Q_ = const. Equations (4.1) and (4.2) with α = 1 may be rearranged to the form of Eq. (1.97): 



where: 

_H_ – flow depth, 

_s_ – channel bed slope, _Fr_ – Froude number. 

Equation (4.4) is the base for theoretical analysis of the water surface profiles arising for various flow conditions in open channels. The profiles can be deduced by taking into account the relation between the bed slope _s_ , critical slope _sc_ and the friction slope _S_ , as well as the relations between the flow depth _H_ , normal depth _Hn_ and critical depth _Hc_ . This rather theoretical analysis, presented in detail for example by Chow (1959), French (1985), Singh (1996) and others, provides some qualitative conclusions. Typical water profiles which can occur during the steady gradually varied flow in open channel are presented in Fig. 4.1. 

4.1 Introduction 

113 



<!-- Start of picture text -->
a) b)<br>a<br>a Hc Hn<br>Hn b<br>b<br>Hc<br>c c<br>c) d)<br>b<br>Hc Hc c<br>s  = 0<br>0 < s < s<br>b<br>s  < 0 c<br>c<br>c<br>0< s < s<br><!-- End of picture text -->

**Fig. 4.1** Typical forms of the water flow profiles resulting from the analysis of Eq. (4.4) for channel with mild slope, steep slope, inverse slope and horizontal bed 

Some of the presented profiles are important for engineering practice, such as the backwater curve presented in Fig. 4.2. 

Others have rather theoretical significance, although they can occur locally in particular circumstances, as it is shown in Figs. 4.3 and 4.4. 

Note that the profiles shown in Fig. 4.1 were deduced from the analysis of the relations between the variables involved in Eq. (4.4) but not from its direct solution. To summarize, Eq. (4.4) is rather not applied in modern hydraulics to solve practical problems, although years ago it was adapted to solve some particular cases (Chow 1959). 



<!-- Start of picture text -->
Hn<br>Hc<br>s < sc<br>datum<br><!-- End of picture text -->

**Fig. 4.2** Typical flow profile behind a dam 

4 Steady Gradually Varied Flow in Open Channels 

114 



<!-- Start of picture text -->
Hn<br>Hc<br>s < sc<br><!-- End of picture text -->

**Fig. 4.3** Typical flow profiles at downstream of gate 



<!-- Start of picture text -->
Hn<br>Hc<br>s < sc<br>datum<br>s > sc<br><!-- End of picture text -->

**Fig. 4.4** Typical flow profile occurring between channels of mild slope and channel of steep slope 

For practical application, when natural channels are considered, instead of Eq. (4.4) the discrete energy equation leading to the so-called step method is commonly used. Let us recall this approach. 

A channel reach enclosed by two sections 1 and 2, as presented in Fig. 4.5, is taken into consideration. Neglecting the lateral inflow, i.e. for _q_ = 0 and _Q_ 1 = _Q_ 2, one can write the following equation representing the energy conservation principle: 



where _�Hf_ is the friction loss in the channel reach. 

Sometimes in Eq. (4.5) an additional term representing the so-called eddy losses is introduced as well (French 1985). It takes into account the effects of expansion or contraction caused by sudden change of the cross-sectional area, which can be appreciable in non – prismatic channels. However, it seems that if these losses are neglected in the Saint Venant equations, then they can be omitted in the case of steady flow as well. If the cross-section area changes suddenly at any point in the considered channel, it should be treated as a point of discontinuity of _h_ ( _x_ ), which divides the channel into two segments. At this point special equations connecting both segments must be introduced. They result from the mass and energy conservation principles. This problem is discussed in Section 4.2.4. 

115 

4.1 Introduction 



<!-- Start of picture text -->
α       Q 2 Δ Hf<br>2 gA 2 1 α      Q 2<br>2 gA 22<br>H 1 Q<br>H<br>2<br>h 1 h 2<br>Z 1<br>Z 2<br>datum<br>1 2 x<br>Δ x<br>s<br><!-- End of picture text -->

**Fig. 4.5** Channel reach definition for the step method 

The term _�_ H _f_ is usually approximated using the arithmetic average of the friction slope over the considered channel reach. Then the following formula can be written: 



where _S1_ and _S2_ are the friction slopes given by formula (4.3). Therefore they are calculated as follows: 



Other methods to estimate the average friction slope for a channel reach exist (French 1985). However, they will not be considered here. As it will be shown later, the use of arithmetic average is consistent with the discrete form of the differential equation (4.2) obtained using the implicit trapezoidal method. 

Substitution of Eqs. (4.7a) and (4.7b) in Eq. (4.5) yields: 



It should be remembered, that the calculation of the flow profile proceeds always towards the direction for which the water surface asymptotically tends to the final level corresponding to the normal depth. Depending on the node numeration, it can be the direction of either increasing or decreasing indices. If for example the water level in cross-section number 2, is known, then _h_ 1 can be easily calculated. Since Eq. (4.8) is a non-linear algebraic equation with regard to _h_ 1, then to solve it one 

116 

4 Steady Gradually Varied Flow in Open Channels 

of the well-known methods as for example the bisection, secant or Newton method should be applied. If _h_ 1 is calculated, one can pass to the next reach enclosed by the next pair of sections. This procedure, called the step method (Chow 1959, French 1985), is repeated until the criterion for convergence to the normal water level is satisfied. 

While comparing the two presented approaches to solve the steady gradually varied flow, i.e. by the solution of the ordinary differential equation (4.4) and by the step method, one can notice some kind of inconsistency. For a prismatic channel the general approach, based on the unsteady flow equations, allowed to derive the equations for steady flow, whereas for a non-prismatic channel a different approach had to be used. This makes impression that the steady flow in open channel must be analyzed with different methods to reach the same goal, depending on the geometry of the channel. This fact has been noticed by other authors as well. For instance Roberson et al. (1998) explicitly distinguish the two possible approaches: “Modern methods for computing the water surface profile may be divided into two categories: methods based on the solution of the energy equation between different channel sections and methods based on the solution of the differential equation describing the rate of change of depth with distance”. However, as the matter of fact, both approaches are equivalent. This coincidence will be shown in the next section. 

### **_4.1.3 Formulation of the Initial and Boundary Value Problems for Steady Flow Equations_** 

The water profile along channel axis in steady gradually varied flow can be formally obtained by solving one of the previously presented ordinary differential equations. To this end a proper problem of their solution must be formulated. For practical applications it is more convenient to write the ordinary differential equations with regard to the water stage _h_ ( _x_ ) than with regard to the depth _H_ ( _x_ ). For example, given the flow discharge _Q_ the function _h_ ( _x_ ) can be obtained via the solution of the so-called initial value problem for ordinary differential equation. Such situation is illustrated in Fig. 4.6. 

In a channel, which carries the discharge _Q_ , the water level was raised owing to a dam from the level _hn_ , corresponding to the normal depth, to the assumed level _h_ 0. Then behind a dam the backwater curve occurs (Fig. 4.6). This curve can be calculated on condition that its value _h_ 0 at control _x_ = 0 is known. In such a way it is possible to reproduce all the typical water profiles showed in Fig. 4.1, which can occur in open channel. 

Sometimes the flow profile must be determined in another way. If at both ends of open channel the water levels are imposed and the flow discharge in channel is unknown, the flow profile can be obtained via the solution of the so-called boundary problem (or two points boundary value problem) for ordinary differential equations. 

4.1 Introduction 

117 



<!-- Start of picture text -->
h<br>H ( x )<br>H 0<br>h ( x ) h 0<br>Hn<br>Z ( x )<br>datum<br>x  = 0 x<br>s<br>Q<br><!-- End of picture text -->

**Fig. 4.6** Backwater curve behind a dam – an example of the initial value problem for ordinary differential equation 



<!-- Start of picture text -->
channel<br>h<br>Q<br>h ( x )<br>h 0 hL<br>Z( x )<br>datum<br>x = 0                                                                               x = L x<br>s<br>reservoir reservoir<br><!-- End of picture text -->

**Fig. 4.7** Channel connecting two reservoirs having constant water levels 

This problem has been already presented in Section 3.3. Such a situation takes place when a channel of length _L_ connects two reservoirs, as it is shown in Fig. 4.7. If the water levels in reservoirs are time – invariant, the curve _h_ ( _x_ ) must satisfy the steady gradually varied flow equations in the domain 0 ≤ _x_ ≤ _L_ and two additional conditions imposed at both ends of the channel. 

Another particular set of problems occur for steady gradually varied flow in open channel network. These questions will be taken up in Section 4.4. 

4 Steady Gradually Varied Flow in Open Channels 

118 

### **4.2 Numerical Solution of the Initial Value Problem for Steady Gradually Varied Flow Equation in a Single Channel** 

### **_4.2.1 Numerical Integration of the Ordinary Differential Equations_** 

The steady flow profile can be obtained using a number of relatively simple graphical or analytical approaches, which do not involve numerical computations. However, these methods are limited to prismatic channels, and thus they will not be considered here. Their detailed presentation can be found in French (1985). In this chapter we shall focus on a more general approach, suitable for channels with arbitrary cross-section geometry. 

A general mathematical model of steady flow is given by the previously presented system of the ordinary differential equations (4.1) and (4.2), which with Eq. (4.3) is rewritten as follows: 





These equations describe the flow profile _h_ ( _x_ ) and the discharge _Q_ ( _x_ ) along the channel axis. To calculate these functions for a single channel an appropriate problem of solution for Eqs. (4.9) and (4.10) should be formulated. 

Let us assume a channel of length _L_ , divided by _N_ nodes (at which the channel cross-sections are known), into intervals of length _Δxi_ = _xi_ +1 − _xi_ . When the discharge _Q_ at any channel cross-section is given and the distribution of lateral inflow along channel is known, Eq. (4.9) can be solved immediately. Its integration over the interval _Δxi_ yields: 



This formula allows us to determine the discharges at all nodes along the considered channel reach. To this order the integral in Eq. (4.11) is calculated numerically using any quadrature formula, such as the rectangular or trapezoidal rule. Knowing the discharges _Qi_ ( _i_ = 1, 2, _. . ._ , _N_ ) one can solve Eq. (4.10). For this purpose the following initial value problem is formulated: calculate the water flow profile _h_ ( _x_ ), which satisfies Eq. (4.10) and the initial condition _h_ ( _x_ = _x_ 0) = _h_ 0 imposed at control end of the considered channel reach. 

There exist numerous methods to solve the initial value problem for the ordinary differential equations (Ascher and Petzold 1998, Le Veque 2007, Press et al. 1992, Stoer and Bulirsch 1980). Some of them were presented in Chapter 3. As it was 

4.2 Numerical Solution of the Initial Value Problem 

119 

explained, the cross sections of an open channel obtained by field measurements are distributed along channel in a non-uniform way, so the lengths of intervals _Δxi_ vary. Consequently it is better to avoid such methods of solution, which need an interpolation between neighboring nodes as for instance the methods of Runge– Kutta. Such type of methods can be applied rather for prismatic channels in which interpolation is possible. Similarly, multi-step methods should be avoided, as they are suitable rather for uniformly spaced grid points. For natural rivers with variable cross-sections only the Adams–Moulton method of the lowest order should be applied, since it uses the cross-sectional parameters at the grid points only. For these reasons the implicit trapezoidal rule (3.22) seems to be the best choice: 



where: 

_yi_ , _yi_ +1 are the values of the unknown function at nodes _i_ and _i_ + 1 respectively, _y_<sup>′</sup> _i_<sup>,</sup><sup>_y_′</sup> _i_ +1<sup>are the values of the derivatives of</sup><sup>_y_(</sup><sup>_x_) at nodes</sup><sup>_i_and</sup><sup>_i_+ 1 respectively,</sup> _�x_ is the integration step. 

The trapezoidal rule, being an implicit method, has two important advantages: 

- it ensures approximation of 2nd order of accuracy, 

- it requires data from cross – sections _i_ and _i_ + 1 only, thus it is especially suitable for integration with variable step size as it occurs in open channel. 

Application of the formula (4.12) to solve Eq. (4.10) yields: 



where: 

_i_ – index of cross-section, 

_Δxi_ – length of interval number _i_ . 

Note that if the index _i_ increase as _x_ decreases, then in Eq. (4.13) the step size _Δxi_ should have negative sign. 

Sometimes the lateral inflow _q_ ( _x_ ) can be neglected. With _qi_ = _qi_ +1 = 0 the discharge is _Qi_ = _Qi_ +1 = const. and Eq. (4.13) can be simplified: 

4 Steady Gradually Varied Flow in Open Channels 

120 



Let us compare Eq. (4.14) with Eq. (4.8). It is easy to find out that they are identical. It means that the ordinary differential equation (4.10) solved by the trapezoidal rule coincides with the discrete energy equation (4.8), usually applied to calculate the water profile in natural channels. Note that Eq. (4.14) has been derived directly from the most general mathematical model of 1D unsteady flow in open channel, i.e. the Saint Venent equations. Therefore any special treatment of the steady gradually varied flow in natural channels is not needed. On the other hand, any special procedures for numerical integration of Eq. (4.4) are not needed as well. 

Equation (4.14) should be solved either for prismatic or non-prismatic channel by one of the methods previously listed for Eq. (4.8). In such a way it is possible to obtain the flow profiles corresponding to all zones distinguished by the theoretical analysis of Eq. (4.4) and presented in Fig. 4.1. 

### **_4.2.2 Solution of the Non-linear Algebraic Equation Furnished by the Method of Integration_** 

The goal of the applied approach is to determine the water flow profile for specified depth imposed at the downstream end. Since all variables in Eq. (4.14) corresponding to the node _i_ are known, this algebraic equation contains only one unknown _hi_ +1. However as _hi_ +1 is involved in other parametrs, it cannot be expressed explicitly. To solve the problem Eq. (4.14) is reformed as follows: 



The value of _hi+_ 1 that makes _f_ ( _hi+_ 1) = 0 is the root of Eq. (4.15) and is the solution to the problem. To obtain it one of the numerical methods for determining roots of the non-linear algebraic equations described in Section 2.1 must be applied. 

Numerical experiments provide us with interesting insights into the properties of Eq. (4.15). Apparently no difficulties occur for the standard problem of backwater curve behind a dam, where the intervals _Δx_ are of the order of hundreds meters. However, for other type of flow profiles presented in Fig. 4.1 some computational problems can arise. For instance it appears that starting from the 

4.2 Numerical Solution of the Initial Value Problem 

121 

same initial condition _H_ 0 = _Hc_ , i.e. when the critical depth is imposed at _x_ = 0, two different physically admissible solutions can be obtained. On the other hand, sometimes the correct solution cannot be obtained at all. The possible existence of many solutions results from the existence of multiple roots of the function _f_ ( _hi+_ 1). 

In order to investigate these effects in a more detailed way, let us consider steady gradually varied flow in a trapezoidal channel with _b_ = 3.5 m, _nM_ = 0.015, _m_ = 1.5, _s_ = 0.001 that carries a discharge _Q_ = 4 m<sup>3</sup> /s. To simplify interpretation of the results of calculations let us change the independent variable. Let us use the depth _Hi+_ 1 instead of the water level _hi+_ 1. The objective is to determine the water flow profiles for various characteristic depths imposed at the downstream end as initial condition. 

For the assumed data the normal depth satisfying the Manning formula: 



solved by the false position method (see Section 2.1.3) is equal to _Hn_ = 0.664 m, whereas the critical depth satisfying the equation: 



and solved by the same method, is equal to _Hc_ = 0.490 m. 

The flow profiles are calculated for the following initial conditions imposed at _x_ = 0: 

- _H_ 0 = 1.00 m ( _H_ 0 > _Hn_ and _H_ 0 > _Hc_ ) 

- _H_ 0 = 0.55 m ( _H_ 0 < _Hn_ and _H_ 0 > _Hc_ ) 

- _H_ 0 = 0.45 m ( _H_ 0 < _Hn_ and _H_ 0 < _Hc_ ). 

An analysis of the function _f_ ( _Hi+_ 1) concerns the first reach of channel, which is bounded by the cross-sections 0 and 1. So it will deal with the function _f_ ( _H_ 1) only. 

It is well known that while solving any non-linear algebraic equation, at first the searched root must be separated. In considered Eq. (4.15) all possible roots of function _f_ ( _H_ 1) exist in the domain of positive real numbers. In the interval defined by two endpoints, only one root may exist. Afterwards a suitable method for determination a single root is applied. To check the number of roots and their positions the graph of _f_ ( _H_ 1) should be drawn. 

The plots of function _f_ ( _H_ 1) obtained for the assumed data are presented in Figs. 4.8, 4.10 and 4.11. 

It appears that for the imposed initial value of _H_ 0 the shape of the function _f_ ( _H_ 1) strongly depends on the value of the stepsize _�x_ . One can notice, that depending on the assumed values of _H_ 0 and _Δx_ there are one, two or three roots of the function (4.15) in the domain of real positive numbers. Therefore, while solving Eq. (4.15) 

4 Steady Gradually Varied Flow in Open Channels 

122 

**Fig. 4.8** Function _f_ ( _H_ 1) for various values of stepsize _�x_ with _s_ = 0.001 and _H_ 0 = 1.00 m 



<!-- Start of picture text -->
f ( H 1)<br>3.0<br>Δ x = 1 m<br>2.0 Δx = 12.5 m<br>1.0<br>Δx = 30 m<br>0.0<br>–1.0<br>–2.0 Δx = 100 m<br>–3.0<br>–4.0<br>0.0 0.5 1.0 1.5 2.0<br>H 1[m]<br><!-- End of picture text -->

the separation of the roots must be done very thoroughly. The single root should be properly selected and then its value must be approximated with sufficient accuracy. Otherwise one can find a false root and consequently obtain an unphysical solution. 

The presented plots of _f_ ( _H_ 1) show why only some attempts of computations can be successful, while others can fail or to deliver false solutions. The crucial point during the computational process is to choose the proper value of stepsize _�x_ , since as results form the presented figures, it determines both the shape of function _f_ ( _H_ 1) and the number of its roots. The significance of this parameter is due to the fact that one of the most important terms of Eq. (4.7) representing the losses of energy is governed by the stepsize _�x_ . For example, Fig. 4.8 shows that in the case of a large stepsize applied for the subcritical flow ( _H_ 0 = 1.00 m > _Hc_ ) only one root exists. Then the solution will be always reached without any difficulties. On the other hand, for small values of _�x_ one or even two additional roots occur. However both of them are physically inadmissible. The appropriate root can be identified taking into account that the extreme minimum value of _f_ ( _Hi+_ 1) roughly corresponds to the critical depth, which in this case is equal to _Hc_ = 0.49 m. This is clearly shown in Fig. 4.9. 

Similar results to the ones presented in Fig. 4.8 are also obtained for the following initial condition: _Hc_ = 0.49 m < _H_ ( _x_ = 0) = _H_ 0 = 0.55 m < _Hn_ = 0.664 m. They are shown in Fig. 4.10. 

One should remember that while the calculations proceed from the cross section _i_ to the cross section _i_ + 1 ( _i_ = 1, 2, 3, _. . ._ ), the depth _Hi+_ 1 varies. Therefore at the same time the form of the function _f_ ( _Hi+_ 1) varies as well. For this reason in every cross-section, a separation of the interval containing the searched root must de done very thoroughly. 

4.2 Numerical Solution of the Initial Value Problem 

123 

**Fig. 4.9** Function _f_ ( _H_ 1) for step size _Δx_ = 1.0 m with _s_ = 0.001 and _H_ 0 = 1.0 m has its minimum point at _H_ 1 ≈ _Hc_ .= 0.49 m 

**Fig. 4.10** Function _f_ ( _H_ 1) for various values of step size _Δx_ with _s_ = 0.001 and _H_ 0 = 0.55 m 



<!-- Start of picture text -->
f ( H 1)<br>0.50<br>Δ x  = 1.0 m<br>0.25<br>0.00<br>f min<br>–0.25<br>–0.50<br>0.00 0.25 0.50 0.75 1.00 1.25<br>H 1[m]<br>f ( H 1)<br>4.0<br>Δx = 1 m<br>3.0<br>2.0<br>Δx = 20 m<br>1.0<br>0.0<br>− 1.0<br>Δx = 40 m<br>− 2.0<br>− 3.0<br>0.00 0.50 1.00 1.50<br>H 1[m]<br><!-- End of picture text -->

If the imposed depth _H_ 0 is greater than critical depth, as in the considered case, the root at the right-hand side of the extreme point should be chosen as the proper one. If we choose one of the roots from the left-hand side of the minimum, the calculated solution will have unphysical character. 

Figure 4.11 shows a situation opposite to the ones presented in Figs. 4.8 and 4.10. One can see that with too large step size applied for the supercritical flow ( _H_ 0 = 0.45 m < _Hc_ ) it is impossible to obtain a physically reasonable solution. On the other hand, for small values of _Δx_ two roots occur. However, only one of them is physically admissible. To choose the suitable root one can use previously presented information on the minimum point of _f_ ( _Hi+_ 1), which corresponds to the 

4 Steady Gradually Varied Flow in Open Channels 

124 

**Fig. 4.11** Function _f_ ( _H_ 1) for various values of step size _Δx_ with _s_ = 0.001 and _H_ 0 = 0.45 m 



<!-- Start of picture text -->
f  ( H 1 ) Δ x  = 2.5 m<br>2.0 Δ x  =12.5 m<br>1.0<br>0.0<br>−1.0<br>Δ x  = 40 m<br>−2.0<br>−3.0<br>0.0 0.5 1.0 1.5<br>H   [m]1<br><!-- End of picture text -->

critical depth. Therefore if the imposed depth _H_ 0 is less than critical one, as in this case, the root at left side of extreme point should be chosen. Conversely, if _H_ 0 is greater than _Hc_ we have to choose the one from the right-hand side. 

The influence of the stepsize on the number of roots is a very important conclusion, since in the numerical analysis it is usually considered that the step of integration influences only the accuracy and stability of the numerical solution. The presented results suggest that in some cases the correct solution can be obtained only if additional conditions on the stepsize are satisfied. 

From the above discussed properties of the function _f_ ( _Hi+_ 1) results that it is possible to calculate numerically all types of the flow profiles, which can occur during steady varied flow in open channel. The calculations can be carried out for both artificial and natural channels, since the approach based on the ordinary differential energy equation is capable of predicting the depth of flow at arbitrary longitudinal distances. This feature is an important advantage as in rivers the distances between neighboring cross-sections are variable. However the numerical solution of the non-linear equations should be performed especially thoroughly. The function _f_ ( _Hi+_ 1) given by Eq. (4.15) can have one, two or three roots, which in addition can move along axis. Some of them are physically inadmissible. For these reasons the separation of the interval containing the single root must be carried out very precisely. To determine the root within an interval the bracketing methods should be used, rather than the open ones. Thus, the bisection and false position methods will be more reliable than the Newton and simple fixed-point iteration methods. The latter methods can be applied on condition that the interval containing the correct root is sufficiently narrow, so that _f_ ( _Hi+_ 1) varies monotonically over the interval. 

125 

4.2 Numerical Solution of the Initial Value Problem 

### **_4.2.3 Examples of Numerical Solutions of the Initial Value problem_** 

_Example 4.1_ A trapezoidal channel with _b_ = 3.5 m, _nM_ = 0.015, _m_ = 1.5, _s_ = 0.001 carries a discharge _Q_ = 4 m<sup>3</sup> /s. Determine the water flow profiles for various characteristic depths imposed at the downstream end. 

For the assumed data the normal depth satisfying the Manning formula is equal to _Hn_ = 0.664 m, whereas the critical depth satisfying the Equation (4.16) is equal to _Hc_ = 0.490 m. The flow profiles were computed for _h_ ( _x_ = 0) corresponding to the depths _H_ 0 = 1.0 m > _Hn_ , _H_ 0 = 0.664 m = _Hn_ and _H_ 0 = 0.40 m = _Hc_ . They are shown in Fig. 4.12. As it could be expected, the profiles obtained by numerical solution have typical forms resulting from the theoretical analysis of Eq. (4.4) and presented in Fig. 4.1. The plots correspond to case A – zones a and b. The backwater curve calculated for zone c, i.e. for supercritical flow, is discussed later. 

**Fig. 4.12** Steady gradually varied flow profiles in a channel with uniform longitudinal slope for various depths _H_ 0 imposed at _x_ = 0 



<!-- Start of picture text -->
h [m ]<br>11.75<br>11.50 H 0 Hn<br>11.25<br>H 0= Hn<br>11.00<br>10.75 H 0 Hn<br>10.50<br>10.25<br>10.00<br>–1.0 –0.8 –0.6 –0.4 –0.2 0.0<br>x  [km]<br>bottom<br><!-- End of picture text -->

_Example 4.2_ A trapezoidal channel with _b_ = 3.5 m, _nM_ = 0.015, _m_ = 1.5 and horizontal bed ( _s_ = 0.0) carries a discharge _Q_ = 4 m<sup>3</sup> /s. Determine the water flow profiles for various depths imposed at the downstream end. 

The calculation performed for _H_ 0 = _Hc_ , corresponding to the free overfall at the channel end gave the flow profile in the form of a typical drawdown curve obtained for the critical depth imposed at downstream end (Fig. 4.13). Similar, but more gentle drawdown curve results for a greater value of _H_ 0 imposed as the initial condition at _x_ = 0. 

_Example 4.3_ A trapezoidal channel with _b_ = 3.5 m, _nM_ = 0.015, _m_ = 1.5 and having adverse bed slope _s_ = −0.001 carries a discharge _Q_ = 4 m<sup>3</sup> /s. Determine the water flow profile assuming that the channel terminates in a free overfall, i.e. the critical depth is imposed at the downstream end. 

126 

4 Steady Gradually Varied Flow in Open Channels 



<!-- Start of picture text -->
h  [m]<br>11.25<br>H 0 Hc<br>11.00<br>10.75 H 0= Hc<br>10.50<br>10.25 Hc<br>bottom<br>10.00<br>–1.0 –0.8 –0.6 –0.4 –0.2 0.0<br>x  [km]<br><!-- End of picture text -->

**Fig. 4.13** Steady gradually varied flow profiles in a channel with horizontal bed for various depth _H_ 0 imposed at _x_ = 0 

**Fig. 4.14** Steady gradually varied flow profiles in a channel with adverse slope for _H_ 0 = _Hc_ imposed at _x_ = 0 



<!-- Start of picture text -->
h  [m]<br>12.0<br>H  0 = H c<br>11.5<br>Hc<br>11.0<br>10.5<br>10.0<br>−1.0 −0.8 −0.6 −0.4 −0.2 0.0<br>x  [km]<br>bottom<br><!-- End of picture text -->

In Fig. 4.14 one can see that computed drawdown curve corresponds to the one presented in Fig. 4.3 (case C, zone b). 

_Example 4.4_ A trapezoidal channel with _b_ = 3.5 m, _nM_ = 0.010, _m_ = 1.5 and a steep bed slope _s_ = 0.005 carries a discharge _Q_ = 4 m<sup>3</sup> /s. Determine the water flow profile for the following initial conditions, imposed at _x_ = 0: 

4.2 Numerical Solution of the Initial Value Problem 

127 

##### _h_ [m] 



<!-- Start of picture text -->
10.8<br>H 0 H c<br>10.6 Hn H 0 Hc<br>10.4<br>Hc<br>10.2<br>Hn<br>H o< Hn<br>10.0<br>–20 –15 –10 –5 0<br>x  [m]<br>bottom<br><!-- End of picture text -->

**Fig. 4.15** Steady gradually varied flow profile in channel with steep slope for various depths imposed at _x_ = 0 

- _H_ 0 = 0.75 m > _Hc_ , 

- _Hn< H_ 0 = 0.35 m < _Hc_ , 

- _H_ 0 = 0.25 m < _Hn_ . 

The considered type of flow corresponds to case B in Fig. 4.1. To obtain the results displayed in Fig. 4.15 small stepsize equal to _Δx_ = 1.0 m had to be applied. Note that the flow profiles for all three zones a, b, and c can be reproduced using the same approach. 

_Example 4.5_ An interesting case arises when the critical depth is imposed as the initial condition. To illustrate this problem let us consider steady flow in the channel from Example 4.4. It is a channel with mild slope _s_ = 0.001 < _sc_ for which the critical depth is equal to _Hc_ = 0.49 m. This value is imposed at _x_ = 0 as the initial condition _H_ 0 = _Hc_ . Let us plot the function _f_ ( _H_ 1) given by Eq. (4.15). Figure 4.16 presents the values of the function for the stepsize _Δx_ = 0.25 m. One can see that there are two roots, both located in the vicinity of the minimum point of _f_ ( _H_ 1), which is at _H_ 1 = _Hc_ . Therefore a question arises, which root should be taken into consideration. The choice of the root depends on the type of curve which is required. If the curve in zone b (Fig. 4.1, case A) is searched, then the root at the right-hand side of the minimum point must be chosen. Conversely, if the drawdown curve from zone c is computed, the other root should be taken. Summarizing, the initial condition _H_ 0 = _Hc_ can generate the backwater (zone c) or drawdown (zone c) curve depending on the chosen root. The two possible profiles are presented in Fig. 4.17. 

The presented examples show that practically all possible forms of the flow profile displayed in Fig. 4.1 can be reproduced by the numerical solution of the governing equation for the steady gradually varied flow (4.2). 

4 Steady Gradually Varied Flow in Open Channels 

128 

**Fig. 4.16** Plot of the function _f_ ( _H_ 1) for initial condition _H_ 0 = _Hc_ = 0.49 m and _Δx_ = 0.25 m 



<!-- Start of picture text -->
f(H 1 )<br>0.025<br>0.020<br>0.015<br>0.010<br>0.005<br>0.000<br>0.40 0.45 0.50 0.55 0.60<br>H 1[m]<br><!-- End of picture text -->

**Fig. 4.17** Two different flow profiles computed with _Δx_ = 0.25 m for the same initial condition _H_ 0 = _Hc_ at _x_ = 0 



<!-- Start of picture text -->
h  [m]<br>11.0<br>10.8<br>10.6<br>10.4<br>Hn<br>Hc<br>10.2<br>10.0<br>–100 –75 –500 – 250 0<br>x  [m]<br>bottom<br><!-- End of picture text -->

### **_4.2.4 Flow Profile in a Channel with Sudden Change of Cross-Section_** 

Sometimes the backwater curve should be computed for a channel composed of two reaches with a sharp discontinuity in the cross-section geometry. In such a case a significant local change of the water level can occur. The considered situation is presented in Fig. 4.18. 

Let us assume that the computation of the backwater curve proceeds step by step from the downstream end, where the initial condition is imposed, towards the upstream end. However sometimes it is impossible to continue the computations 

4.2 Numerical Solution of the Initial Value Problem 

129 

#### a) 



<!-- Start of picture text -->
node  i node  i + 1<br>Q Q<br>2<br>b) α Q<br>Δ  H L 2  gAi 2  +1<br>energy line<br>α  Q 2<br>2  gA 2 i<br>water surface<br>h i  +1<br>h i<br>bottom<br>datum<br><!-- End of picture text -->

**Fig. 4.18** Channel changing a cross-section area 

using the same algorithm. It can occur in the junction of two segments having significantly different cross-sections. To overcome the problem, one has to introduce two computational cross-sections, located very close to each other at the two sides of the discontinuity (Fig. 4.18). 

The equation relating water stages and discharges in both segments results from the energy conservation principle written for the two cross-sections. It has the following form: 



where 



_i_ – index of cross-section at left side of junction, 

_i_ + 1 – index of cross-section at right side of junction. 

In open channels the local losses are usually neglected, so Eq. (4.18) becomes: 

4 Steady Gradually Varied Flow in Open Channels 

130 



Note that Eq. (4.19) is equivalent to Eq. (4.14) applied in the step method, if in the latter _Δxi_ = 0 is assumed. Thus, in order to compute the flow profile for a channel with sudden change in cross-section parameters, only a slight modification of the algorithm presented in Section 4.2.2 is required. 

_Example 4.6_ A channel with constant bed slope _s_ = 0.001 and carrying a discharge _Q_ = 4 m<sup>3</sup> /s is composed of two segments of lengths _L_ 1 and _L_ 2. Each part has a trapezoidal cross-section characterized by different parameters: 

- part 1: _L1_ = 550 m, _b1_ = 3.5 m, _nM_ 1= 0.015, _m_ 1 = 1.5, 

- part 2: _L_ 2 = 450 m, _b_ 2 = 2.0 m, _nM_ 2= 0.015, _m_ 2 = 1.4. 

Determine the water flow profile for the water level _h_ ( _x_ = 0) = _h_ 0 imposed at the downstream end. 

The normal depths satisfying the Manning formula are _Hn_ 1 = 0.664 m for the first part of channel and _Hn_ 2 = 0.857 m for the second one. The imposed _h_ ( _x_ = 0) corresponds to the depth _H_ 0 = 1.50 m > _Hn_ 1. The results obtained for _Δx_ =50 m = const. are shown in Fig. 4.19. 

As it could be expected, in the first segment of the channel, a typical backwater curve was obtained. In the node _x_ = −550 m a discontinuity of the water surface occurred, resulting from the sudden change of the channel parameters. Since the velocity head in the first part is smaller than in the second one, the water surface falls while passing between channel segments. Afterwards the flow profile tends asymptotically to _Hn_ 2, which is the normal depth in the second segment of channel. 



<!-- Start of picture text -->
h  [m] part 2 part 1<br>2.0<br>1.5<br>Hn 2<br>1.0<br>H 0<br>0.5 Hn 1<br>0.0<br>–1.0 –0.8 –0.6 –0.4 – 0.2 0.0<br>x  [m]<br>bottom<br><!-- End of picture text -->

**Fig. 4.19** Steady gradually varied flow profile in channel with varying cross-sections for depth _H_ 0 =1.5 m > _Hn_ 1 imposed at _x_ = 0 

4.2 Numerical Solution of the Initial Value Problem 

131 



<!-- Start of picture text -->
h  [m]<br>part 2 part 1<br>2.0<br>1.5<br>1.0 Hn 2<br>H 0<br>0.5 Hn 1<br>0.0<br>–1.0 –0.8 –0.6 –0.4 –0.2 0.0<br>x  [m]<br>bottom<br><!-- End of picture text -->

**Fig. 4.20** Steady gradually varied flow profile in channel with varying cross-sections for depth _H_ 0 =1.5 m > _Hn_ 1 imposed at _x_ = 0 

In next example the same data as in the previous case is used, but the parameters _b_ , _nM_ and _m_ of the two segments are swapped. 

The results of computation are presented in Fig. 4.20. This time the velocity head in the first part is larger than in the second one, so that when moving towards the upstream end one can observe a significant rising of the water surface at the junction of the segments. 

### **_4.2.5 Flow Profile in Ice-Covered Channel_** 

In cold climate regions with long seasons of low temperature the rivers can be covered by ice layer. The appearance of the ice cover radically changes the flow regime. Flow with free surface becomes flow in closed conduit. Consequently the velocity distribution over a cross-section becomes similar to the one in pipes and the energy losses increase remarkably. Additionally, variable coefficient of roughness occurs along the wetted perimeter. Due to the ice cover the flow profile is modified. Comparing with the free surface flow the same discharge _Q_ causes increase of the water levels especially in the upstream part of channel, so that the backwater curve becomes much longer. The knowledge of the new position of the water surface is of great importance for the design of flood banks. 

The flow profile in an ice covered channel can be computed using the same equations for the steady gradually varied flow and a similar solution algorithm. The modifications concern the calculation of the cross-sectional parameters and the equivalent Manning roughness coefficient, which takes into account the additional friction coming from the ice cover. 

4 Steady Gradually Varied Flow in Open Channels 

132 



<!-- Start of picture text -->
ice<br>δi cover<br>δw<br>water<br>h ( x ) h ice( x)<br>datum<br><!-- End of picture text -->

**Fig. 4.21** View of the cross-section of ice layer 

Let us assume that the thickness of ice layer at the channel surface is equal to _δ_ ice. In a hole made in the ice layer, as in Fig. 4.21, the surface of water is below the ice surface. 

The difference is caused by different specific weights of ice and water. Their ratio is _γ_ ice/ _γ w_ = 0.92. Therefore, the bottom of the ice layer is located in water at the depth: 



whereas the elevation of the bottom of the ice layer above the accepted datum is: 



where: 

_δ_ ice– thickness of ice layer, 

_δw_ – submersion of ice layer in water, _h_ ( _x_ )– elevation of the free water surface above the assumed datum, _h_ ice( _x_ ) – elevation of the bottom of ice layer above the assumed datum. 

While solving Eq. (4.14) the unknown function is _h_ ( _x_ ), as previously. However, all the cross-sectional parameters have to be calculated for _h_ ice( _x_ ). 

The next modification concerns the Manning roughness coefficient. Since one part of the wetted perimeter corresponds to the channel bed and the other one to the ice bottom, then as in other 1D flow models, a single equivalent roughness coefficient must be introduced. To this order the relatively simple Belokon formula is applied (French 1985): 



4.2 Numerical Solution of the Initial Value Problem 

133 

where: 

- ( _nM_ ) _e_ – equivalent roughness coefficient, 

- ( _nM_ ) _b_ – roughness coefficient associated with the bed, 

- ( _nM_ )ice– roughness coefficient associated with bottom of ice cover, _p_ ice– wetted perimeter associated with ice cover, _pb_ – wetted perimeter associated with the bed. 

_Example 4.7_ A trapezoidal channel with _b_ = 3.5 m, _m_ = 1.5, _s_ = 0.001 carries a discharge _Q_ = 4 m<sup>3</sup> /s. The Manning roughness coefficient taken for channel bed is equal to ( _nM_ ) _b_ = 0.024. The normal depth satisfying the Manning formula is _Hn_ = 0.664 m. Determine the water flow profiles for two different cases: 

- flow with free surface, 

- flow with ice cover, 

assuming in each case the same initial condition imposed at the downstream end, i.e. _h_ ( _x_ = 0) corresponding to the depth _H_ 0 = 2.0 m > _Hn_ = 0.664 m. The thickness of the ice cover is constant, _δ_ ice = 0.25 m, whereas the Manning coefficient for bottom surface of the ice takes the same value as for channel bed i.e. _nb_ = 0.024. It should be remembered, that the actual values of ( _nM_ )ice can range in a relatively large interval, from 0.01 even to 0.10 (Gray and Prowse, 1993). The computations were carried out for _Δx_ = 50 m. The flow profiles are shown in Fig. 4.22. 

A significant difference between the two cases can be observed. The appearance of the ice cover at the water surface increases the friction loss and consequently also increases the flow depths. In this case, in which the data were assumed arbitrarily, the increase exceeds 30% in the upstream part of channel. 



<!-- Start of picture text -->
h  [m]<br>14.0<br>13.0<br>b<br>12.0<br>a<br>11.0 H 0<br>H n<br>10.0<br>–2.5 –2.0 –1.5 –1.0 –0.5 0.0<br>x  [m]<br>bottom<br><!-- End of picture text -->

**Fig. 4.22** The steady gradually varied flow profile in channel with free surface ( **a** ) and with ice cover ( **b** ) for initial depth _H_ 0 = 2.0 m imposed at _x_ = 0 

4 Steady Gradually Varied Flow in Open Channels 

134 

### **4.3 Solution of the Boundary Problem for Steady Gradually Varied Flow Equation in Single Channel** 

### **_4.3.1 Introduction to the Problem_** 

Apart from the initial value problem for steady gradually varied flow equation, the boundary value problem can be formulated as well. The boundary value problem arises when the depths (or water stages) at the two endpoints of the considered channel are known, but the discharge _Q_ is unknown. The solution of the boundary problem consists in the determination of the water flow profile between the two endpoints and the value of the discharge _Q_ . A typical example of such a problem is the flow in a channel connecting two reservoirs with constant water levels (compare Section 4.1.3). A similar problem can be formulated for a river reach bordered by the upstream and downstream ends. If during the steady gradually varied flow the water levels are measured at both ends of considered reach, then the water flow profile _h_ ( _x_ ) and the discharge _Q_ can be obtained via the solution of the boundary value problem as well. 

Another type of the boundary problem arises when the discharge and the depths at the endpoints are known, but the Manning roughness coefficient _nM_ is unknown. In this case, the solution of the problem results in the flow profile and the value of _nM_ (on condition that _nM_ is constant along the channel reach). 

In practice the boundary problems can be solved using different approaches. The first one is based on the numerical integration of the unsteady flow equations, i.e. the system of Saint Venant equations. The equations are solved for the boundary conditions which asymptotically tend to the required constant values and after a sufficiently long time the steady state solution is reached. Cunge et al. (1980) showed that this system of equations approximated with the box scheme of the finite difference method in the case of steady flow does not coincide with the discrete Bernoulli equation used for computation of the steady flow in non-prismatic channels. Consequently the differences between both approaches can occur. It should be also remembered that while the discharge _Q_ results directly from the solution of the Saint Venant equations, the coefficient _nM_ must be estimated by the trial and error method. 

The second method of calculation of the flow profile and the values of _Q_ or _nM_ is based on the solution of the initial value problem for steady flow. It is performed repetitively for the values of _Q_ or _nM_ which are chosen by trial and error, until the condition imposed at the opposite channel end is satisfied. This approach is known as the shooting method (Bjorck and Dahlquist 1974). A simple variant of this method was applied by Chow (1959) to solve the steady flow in a channel connecting two reservoirs. 

The third possible approach is to solve directly the boundary value problem. To this end the steady flow equation is discretized over the considered channel reach, for example using the finite difference method. This results in a system of algebraic equations involving the water depths at the cross-sections within the channel reach 

135 

4.3 Solution of the Boundary Problem 

and the discharge _Q_ (or the Manning coefficient _nM_ ). The system is nonlinear and should be solved using an iterative method. 

Although the boundary value problem for ordinary differential equations is not formulated in open channel hydraulic, however practically, it is solved using the trial and error approach. In certain cases such problem ought to be formulated, since it allows us to apply general well known mathematical methods to calculate some hydraulic problems as for example the steady flow profile and discharge in channel. 

As the boundary value problem can be formulated for the ordinary differential equations of higher order than 1 or for the system of differential equations, we have to consider the system of equations (4.1) and (4.2): 





After its solution the water flow and discharge are known. However one can assume another situation. Knowing the discharge _Q_ and the water levels at both channel’s ends, one can try to compute the water flow profile and the Manning roughness coefficient _nM_ as a solution of the boundary value problem as well. To this order a constant value of _nM_ must be assumed. Owing to this assumption and neglecting the lateral inflow _q_ one can write formally the following system of ordinary differential equations: 





which should be solved instead of Eqs. (4.23) and (4.24). An approach, in which a new variable is introduced and a new equation is added, is very often applied while solving the boundary value problem for the ordinary differential equations (Ascher and Petzold 1998, Press et al. 1992). 

### **_4.3.2 Direct Solution Using the Newton Method_** 

To solve the boundary problem for the ordinary differential equations by the finite difference method, the channel of length ⟨0, _L_ ⟩ is divided by _N_ nodes into _N_ − 1 intervals _Δxi_ . For simplicity let us assume that the lateral inflow does not exist so we have _q_ = 0. Equations (4.23) and (4.24) are approximated at the midpoint of each interval _xi_ + _Δxi_ /2 by a centered difference corresponding to the implicit trapezoidal rule, applied previously: 

136 4 Steady Gradually Varied Flow in Open Channels 





where: 

_i_ – index of cross section, 

_Δxi_ – length of interval number _i_ . 

From Eq. (4.28) results that _Qi_ = _Qi_ +1 = _Q_ = const. for _i_ = 1, 2, _. . ._ , _N_ , whereas introducing into Eq. (4.25) the energy _E_ and the friction slope _S_ defined by the expressions (4.2) and (4.3) respectively, yields: 



Note that formally this equation coincides with the well known discrete energy equation usually applied to calculate the water profile in natural channels. However in the case of the initial value problem, in Eq. (4.29) only one unknown exists. This allows us to calculate the water level step by step, marching along channel axis from cross-section to cross-section. When solving the boundary value problem, the water levels described by Eq. (4.29) must be solved simultaneously at all cross-sections, since they have to satisfy two imposed boundary conditions. To this order similar equations should be written for each interval _Δxi_ ( _i_ = 1,2, _. . ._ , _N_ − 1). In such a way one obtains a system of _N_ − 1 algebraic equations with _N_ + 1 unknowns. There are _N_ water levels _hi_ at nodes and flow discharge _Q_ . When flow in a single channel is considered, this system has to be completed by two additional equations resulting from the imposed boundary conditions (Fig. 4.23). 



<!-- Start of picture text -->
α Q 2 α Q 2<br>2 gA 2 (x = 0) 2 gA 2 (x = L )<br>h<br>Q<br>H ( x )<br>hd<br>hu<br>h ( x ) Z ( x )<br>datum<br>x = 0 x                              x = L<br><!-- End of picture text -->

**Fig. 4.23** Channel connecting two reservoirs having constant water levels 

4.3 Solution of the Boundary Problem 

137 

Assuming subcritical flow in the channel, the following conditions should be imposed at the ends of channel: 





where: 

- _hu_ , _hd_ – water levels imposed at upstream and downstream reservoir respectively, 

_h_ 1, _hN_ – water levels at upstream and downstream end of channel respectively. 

Since the discharge _Q_ is unknown, the boundary problem formulated above has non–linear boundary conditions. 

The final system of equations can be written in matrix form: 



where: 

**A** – matrix of coefficients, 

**B** = ( _hu_ ,0, _. . ._ ,0, _hd_ ,0)<sup>_T_</sup> – vector of right side, 

**X** = ( _h1_ , _h2_ , _. . ._ , _hN_ − _1_ , _hN_ , _Q_ )<sup>_T_</sup> – vector of unknowns, 

_T_ – transposition symbol. 

The matrix **A** of dimensions ( _N_ + 1) × ( _N_ + 1) is very sparse (Fig. 4.24). Its non-zero elements are defined as follows: 

**Fig. 4.24** Structure of matrix **A** 



<!-- Start of picture text -->
1 N N +1<br>1<br>N<br>N +1<br><!-- End of picture text -->

4 Steady Gradually Varied Flow in Open Channels 

138 











for _i_ = 2,3,· · · , _N_ − 1, 











The system of non-linear equations (4.32) can be solved by the Newton method, which is implemented as follows (see Section 2.3.2): 



where: 

_k_ is iteration index, **_�_ X**<sup>(</sup><sup>_k_)</sup> = **X**<sup>(</sup><sup>_k_+1)</sup> – **X**<sup>(</sup><sup>_k_)</sup> is correction vector, **F**<sup>(</sup><sup>_k_)</sup> = **A**<sup>(</sup><sup>_k_)</sup> **X**<sup>(</sup><sup>_k_)</sup> – **B** is vector of residuals in Eq. (4.32), **J**<sup>(</sup><sup>_k_)</sup> is Jacobian matrix. 

After assuming the first estimation of the unknown vector **X**<sup>(0)</sup> , the iterative process is continued until two succeeding solutions satisfy the following criterions for convergence: 



and 

4.3 Solution of the Boundary Problem 

139 

**Fig. 4.25** Water flow profiles in channel connecting two reservoirs calculated with Newton method for various water levels in downstream reservoir 



<!-- Start of picture text -->
h  [m]<br>8<br>7<br>6<br>5<br>Hd Hn<br>4<br>Hd = Hn<br>3 Hd Hn<br>2<br>0 1000 2000 3000 4000 5000<br>x  [m]<br>��� X(Nk ++11 ) − X( N k) +1��� ≤ εQ (4.36)<br>bottom<br><!-- End of picture text -->

where _εH_ and _εQ_ represent the specified tolerances for water level _Hi_ and discharge _Q_ respectively. 

_Example 4.8_ Let us consider an idealized channel with the following geometrical parameters: _L_ = 5000 m, is _s_ = 0.0005, _b_ = 5 m and _m_ = 1.4. The Manning roughness coefficient is _nM_ = 0.020. The channel is divided by _N_ = 101 nodes into 100 reaches of the constant length _Δx_ = 50 m. The bed elevation above the datum changes linearly from _z_ ( _x_ = 0) = 4.0 m at the upstream end to _z_ ( _x_ = _L_ ) = 2.5 m at the downstream end. The boundary condition imposed at the upstream reservoir was equal to _hu_ = 7.5 m whereas at the downstream one the water level _hd_ takes the following values: 6.5, 5 and 4 m. The velocity head in boundary conditions (see Eqs. (4.30) and (4.31)) is neglected. 

Numerical tests showed that the Newton iterative process was convergent in particular cases only, when the starting value of the discharge _Q_ was close enough to the exact solution. With the initial water level corresponding to the hydrostatic state, rapid convergence is ensured for _Q_<sup>(0)</sup> ranging from 5 to 80 m<sup>3</sup> /s. For example starting from _Q_<sup>(0)</sup> = 40 m<sup>3</sup> /s only 4 iterations are needed to obtain the solution _Q_ = 27.594 m<sup>3</sup> /s with _εH_ = 0.001 m and _εQ_ = 0.1 m<sup>3</sup> /s. Unfortunately for values of _Q_<sup>(0)</sup> outside this range the iterations failed to converge. Thus one can conclude that the Newton method is very effective only on condition that the starting value of the discharge _Q_<sup>(0)</sup> is properly chosen. The calculated flow profiles are shown in Fig. 4.25. 

### **_4.3.3 Direct Solution Using the Newton Method with Quasi–Variable Discharge_** 

Schulte and Chaudhry (1987) solved the steady gradually – varied flow in looped network of open channels using both discrete energy and continuity equations. This 

4 Steady Gradually Varied Flow in Open Channels 

140 

approach can be applied for a single channel as well. In the proposed algorithm two unknowns, the water level and the discharge are introduced at each grid point. Therefore in the numerical solution the discharge is treated as variable which formally varies along _x_ axis, although from the physical point of view the discharge is constant over the entire channel. This approach can be called the solution with quasi–variable discharge. 

Equations (4.27) and (4.28) can be rewritten as follows: 





They constitute the system of non-linear equations, which can be expressed in matrix form similar to Eq. (4.32). However, this time the vector of unknowns has the following structure: 



As one can see, this method leads to a larger system of non-linear algebraic equations, since instead of a system of dimension ( _N_ + 1) × ( _N_ + 1) one obtains a system of dimension (2 _N_ ) × (2 _N_ ). As we have 2( _N_ − 1) equations in form of Eqs. (4.37) and (4.38) two additional equations are required to complete the system. They come from the imposed boundary conditions. The structure of matrix **A** corresponding to the assumed structure of vector **X** (Eq. 4.39) is shown in Fig. 4.26. 

The goal of such approach is to improve the convergence of the Newton iteration process, which in the preceding algorithm can suffer from the lack of convergence. 

**Fig. 4.26** Structure of matrix **A** for the system obtained in Schulte and Chaudhry (1987) method (dots represent non-zero elements) 



<!-- Start of picture text -->
1 2N<br>1<br>2 N<br><!-- End of picture text -->

4.3 Solution of the Boundary Problem 

141 

Compared to the previously described approach, in which only one value of the flow discharge in the channel was computed, solution system of Eqs. (4.37) and (4.38) is more costly in terms of numerical work. However, the iterative process appears less sensitive on the initial guess of the discharge. Practically always a convergent solution is reached. The water profiles computed for the same data as in Example 4.8 are identical to the ones displayed in Fig. 4.25. 

### **_4.3.4 Direct Solution Using the Improved Picard Method_** 

To solve the non linear system of equations the Picard method can be applied as well. The Picard iterative scheme for Eq. (4.32) can be written in the following form (compare Section 2.3.3): 



where _k_ is iteration index. Its application for the single channel considered previously in Example 4.8 showed that regardless of the first evaluation of the discharge _Q_ it was impossible to reach the solution. The typical situation for _Q_<sup>(0)</sup> = 50 m<sup>3</sup> /s is presented in Fig. 4.27 as tooth oscillations. While the water levels relatively quickly tend to the expected values, the discharge _Q_<sup>(</sup><sup>_k_)</sup> oscillates with constant amplitude during subsequent iterations. Therefore the standard Picard method cannot be used in the considered case. 

For the equations of steady gradually varied flow an improvement of the iteration process that it becomes convergent, is possible. As results from Fig. 4.27 the discharge _Q_ oscillates around its real value in the subsequent iterations. This fact suggests the way of improvement of the Picard method. Instead of Eq. (4.40) the following modified scheme can be used (Szymkiewicz and Szymkiewicz 2004): 

**Fig. 4.27** Convergence of the Picard iterative process 



<!-- Start of picture text -->
50<br>40<br>30 standard Picard method<br>modified Picard method<br>20<br>10<br>0<br>0 5 10 15 20<br>number of iterations<br>3/[ms]Q<br><!-- End of picture text -->

4 Steady Gradually Varied Flow in Open Channels 

142 

**Fig. 4.28** Water flow profile in channel connecting two reservoirs calculated with modified Picard method for various water levels in downstream reservoir 



<!-- Start of picture text -->
h  [m]<br>8<br>7<br>6<br>5<br>Hd Hn<br>4<br>Hd = Hn<br>3 Hd Hn<br>2<br>0 1000 2000 3000 4000 5000<br>x  [m]<br>bottom<br><!-- End of picture text -->



where **A**<sup>∗</sup> = **A** �0.5 � **X**<sup>_(k)_</sup> + **X**<sup>_(k_−1</sup><sup>_)_��</sup> is the modified matrix of coefficients. It means that to calculate the vector **X** in iteration _k_ + 1, the matrix **A** is calculated using the arithmetic average value of **X** from two preceding iterations. Consequently the estimation accepted for the next iteration is closer to its real value. For _k_ = 1 **A**<sup>∗</sup> = **A** ( **X**<sup>(0)</sup> ) is recommended. The positive results of the proposed improvement are confirmed by the following example. 

_Example 4.9_ The calculations carried out for the same data as previously with the assumed tolerances _εH_ = 0.001 m and _εQ_ = 0.1 m<sup>3</sup> /s were always successful. The first estimation of the water profile corresponded to the hydrostatic state with _h_ ( _x_ ) = _hu_ = const. The final discharge _Q_ = 27.969 m<sup>3</sup> /s was computed for the initial approximations of _Q_<sup>(0)</sup> ranging from −1,000 to 1,000 m<sup>3</sup> /s after 12 ÷ 15 iterations. The results of improved convergence obtained for _Q_<sup>(0)</sup> = 50 m<sup>3</sup> /s are presented in Fig. 4.28. 

One can notice that the iteration process (4.41) relatively quickly converges to the solution. The performed tests show that _Q_<sup>(0)</sup> can take any positive or negative value except zero. In the last case the hydrostatic state is obtained. This is because for _Q_<sup>(0)</sup> = 0 the system of equations is split into a series of independent equations, each with only one unknown. These results prove indirectly that the system (4.32) has a unique solution. This fact was confirmed additionally by the solution of Eq. (4.32) with the following boundary conditions: _hu_ = 7.5 m and _hd_ = 4.0 m, corresponding to the uniform steady state flow. The water flow profile parallel to the channel bed ( _h_ ( _x_ ) = 2.39 m = const.) and a discharge _Q_ = 30.1 m<sup>3</sup> /s satisfying the Manning formula were obtained. 

Comparing the Newton and Picard methods one can state that the Newton method ensures rapid convergence on condition that it is convergent. It needs only 4–6 iterations to obtain a solution, whereas the modified Picard method needs 12–15 

4.3 Solution of the Boundary Problem 

143 

iterations to obtain the solution with the same tolerances. However the Newton method failed for some sets of data while the Picard one appeared unconditionally convergent. The observed difference in the number of iterations is evident because the Picard method converges linearly while the convergence of the Newton one is quadratic (Bjorck and Dahlquist 1974). 

To solve the system of linear algebraic equations (4.41) with sparse matrix of coefficients an iterative method seems suitable. However the attempts to solve it with Gauss–Seidel and SOR methods failed. Finally, Eqs. (4.34) and (4.41) should be rather solved by the Gauss elimination method in its version using non-zero elements of matrix **J** or **A** only. 

Let us consider the second possible type of the boundary problem for steady gradually varied flow equations, in which the Manning coefficient _nM_ is considered as an unknown. This case is described by Eqs. (4.25) and (4.26). The elements of the vectors **X** and **b** as well as the elements of the matrix **A** must be modified. The vector **X** is defined as follows: 



whereas the matrix **A** has the following elements: 







The vector of the right-hand side **B** = ( _b_ 1, _b_ 2, _. . ._ , _bN_ , _bN_ +1)<sup>_T_</sup> has the following components: 





Numerical tests carried out for the channel described in Example 4.8 show that for _εH_ = 0.0001 and _εn_ = 0.001 the finite difference method with the Picard iteration ensures a convergent solution for any starting value of _nM_<sup>(</sup><sup>_0_)</sup> . However, the number of iterations depends on the initial choice of _nM_<sup>(</sup><sup>_0_)</sup> . 

4 Steady Gradually Varied Flow in Open Channels 

144 

### **_4.3.5 Solution of the Boundary Problem Using the Shooting Method_** 

In this approach the process of solution of the boundary problem for the system of equations (4.23) and (4.24) is carried out as a sequence of solutions of initial value problems. Assuming _q_ = 0 the corresponding initial value problem can be written in the following form (see Section 3.3): 



Since _E_ = _E_ ( _x_ ; _Q_ ) the solution depends on the chosen value of _Q_ . Therefore for any assumed value of _Q_ one obtains the corresponding value of _E_ ( _x_ = _L, Q_ ). Solution of the boundary value problem coincides with the solution of the initial value problem with such a value of _Q_ , for which the boundary condition at the downstream end is satisfied, i.e.: 



Let us introduce the function: 



which represents the difference between the calculated value of _E_ at _x_ = _L_ for the assumed _Q_ and the imposed boundary condition at _x_ = _L_ equal to _EL_ (Fig. 4.29). 

In such a way the solution of the boundary problem can be considered as finding the root of Eq. (4.47). The value of _F_ ( _Q_ ) can be calculated for any value of _Q_ . To this end the initial value problem (4.45) should be solved to obtain _E_ ( _x_ = _L_ , _Q_ ). If a couple of values of _Q_ are known, say _Q_<sup>(1)</sup> and _Q_<sup>(2)</sup> , which satisfy the following relation: 





<!-- Start of picture text -->
E<br>E 0 E ( x ,  Q    (2) )<br>EL<br>(1)<br>F ( Q     )<br>x = 0 x = L x<br>E ( x , Q *)<br>E ( x , Q (1)<br>)<br><!-- End of picture text -->

**Fig. 4.29** Solution of the boundary problem as a sequence of initial value problems 

145 

4.3 Solution of the Boundary Problem 

then the root _Q_<sup>∗</sup> of _F_ ( _Q_ ) is located inside the interval ⟨ _Q_<sup>(1)</sup> , _Q_<sup>(2)</sup> ⟩. The root can be found using one of the methods of solution of the non linear algebraic equations as the bisection method or the secant method. Note that the Newton method is rather less suitable since it requires the derivative of function _F_ ( _Q_ ), which in this case can be obtained via numerical approximation only. 

Let us apply the method to compute the water flow profile and flow discharge in channel connecting two reservoirs with different but constant in time water levels presented in Fig. 4.23. 

_Example 4.10_ A channel connecting two reservoirs of length L = 5,000 m with bed slope s = 0.0005 has trapezoidal cross section with base width b = 10 m and side slope m = 1. The Manning coefficient is equal to _nM_ = 0.030. The channel is divided into N = 50 intervals having constant length Äx = 100 m. The bed elevation varies linearly from 4.0 m above the datum at the upstream end to 2.5 m at the downstream end. As it was showed by Chow (1959), the shape of the flow profile h(x) depends on the relation between the water levels in reservoirs and the normal depth in the channel _Hn_ . 

In the upstream reservoir a constant water level equal to _ho_ = 10.0 m, which corresponds to the depth _Ho_ = 4.0 m, is assumed. The velocity head is neglected. Computations were carried out for the following values of the water levels in the downstream reservoir: _hL_ = 8.75, 7.50 and 4.25 m. These values correspond to the depths: _HL_ = 4.25, 4.00 and 3.75 m. The results of calculations are presented in Fig. 4.30. 

The shapes of the flow profiles agree with those obtained by Chow (1959). The computed discharge for _HL_ = 4.25 m is equal to _Q_ = 102.24 m<sup>3</sup> /s, whereas for _HL_ = 3.75 m it is equal to _Q_ = 123.07 m<sup>3</sup> /s. Further calculations were carried out for the same set of data, but taking into account the velocity head in the boundary condition at the upstream end. The computed velocity heads at the upstream end were: 0.092 m for _hL_ = 8.75 and 0.134 m for _hL_ = 4.25 m. For this 



<!-- Start of picture text -->
H  [m]<br>HL H 0 HL H 0<br>8<br>H   0 = 5 m<br>6<br>H  n = 5 m<br>4<br>2<br>0<br>0 1 2 3 4 L  = 5     x  [km ]<br>s  = 0,0005<br><!-- End of picture text -->

**Fig. 4.30** The flow profiles for various water levels in downstream reservoir 

146 

4 Steady Gradually Varied Flow in Open Channels 



<!-- Start of picture text -->
F ( Q ) [m ]<br>1,0<br>0,5<br>0,0<br>40 80 120 Q  [m/s]3<br>–0,5<br><!-- End of picture text -->

**Fig. 4.31** Plot of function _F_ ( _Q_ ) 

reason the previously computed discharges were modified to _Q_ = 98.022 m<sup>3</sup> /s and _Q_ = 117 m<sup>3</sup> /s respectively. 

In the presented example the function _F_ ( _Q_ ) has a regular shape, as presented in Fig. 4.31, and possesses one root. To find it the bisection method has been applied. The number of iterations depends on the dimension of interval in which the root is localized, and on the required tolerance of solution. For _εH_ = 0.0001 m the total number of iteration was less than 20. 

In contrast to the presented approach Chow (1959) solved the same problem by the trial and error method using in addition the so-called discharge curve _Q_ ( _hL_ ). However, formulation of the boundary value problem allows us to calculate both the flow profile _h_ ( _x_ ) and the discharge _Q_ directly. 

The shooting method can be also used to find the value of the Manning coefficient _nM_ when the discharge _Q_ and the water levels at the endpoints are known. In this case, instead of the root of function _F_ ( _Q_ ), the root of function _F_ ( _nM_ ) should be determined. The function _F_ ( _nM_ ) is defined as follows: 



whereas the criteria for convergence take the following form: 



and 



where _εn_ is the assumed tolerance for the Manning coefficient _nM_ . 

_Example 4.11_ A rectangular channel with _B_ = 0.385 m, and _L_ = 10 m has longitudinal slope equal to _s_ = 0.0005 (Fig. 4.32). Computations were performed over the length of _L_ 1 = 8 m, which was divided into segments of length equal to _Δx_ = 0.5 m = const. 

4.4 Steady Gradually Varied Flow in Open Channel Networks 

147 



<!-- Start of picture text -->
A A–A<br>Q<br>s h ( x )<br>Q<br>A 0,385 m<br>The considered laboratory flume (Szymkiewicz 2000)<br>h  [m]<br>1,3<br>calculated<br>observed<br>1,2<br>1,1<br>1,0<br>0 1 2 3 4 5 6 7 L = 8 x  [m]<br>Q  = 0,375 m3/s<br>s  = 0,0005<br>10 m<br><!-- End of picture text -->

**Fig. 4.32** The considered laboratory flume (Szymkiewicz 2000) 

**Fig. 4.33** Calculated and measured water profile in channel (Szymkiewicz 2000) 

An experiment performed in hydraulic laboratory provided the following data: _Q_ = 0.0375 m<sup>3</sup> /s, _ho_ = 1.314 m, _hL_ = 1.309 m. Only few iterations are needed to obtain the solution satisfying the following tolerances: _εH_ = 0.0001 and _εn_ = 0.001. 

Regardless of the starting value of the Manning coefficient _n_<sup>(0)</sup> _M_<sup>,convergent</sup> solutions were reached. This fact confirms that the iterative process converges unconditionally. The differences between the computed and observed water levels did not exceed 0.002 m, whereas the computed Manning coefficient is equal to _nM_ = 0.0201. In Fig. 4.33 computed and observed water levels are compared. 

### **4.4 Steady Gradually Varied Flow in Open Channel Networks** 

### **_4.4.1 Formulation of the Problem_** 

In practical applications the steady gradually varied flow is considered not only in a single open channel but in open channel networks as well. There are two types of channel networks: tree – type and looped ones (Fig. 4.34). 

4 Steady Gradually Varied Flow in Open Channels 

148 



<!-- Start of picture text -->
a)                                                           b)<br>pending<br>nodes<br>branches<br>loops<br>junctions<br>nodes<br><!-- End of picture text -->

**Fig. 4.34** Tree – type ( **a** ) and looped ( **b** ) network 

A network consists of branches, which join each other in the junction. Usually the junction gathers three branches. If a particle of water starting from an arbitrary point of the network can reach another point via only one possible route, the network is called a tree – type one, whereas if it can travel towards the destination point using multiple alternative ways, the network is called looped. The upper parts of river systems tend to form tree – type networks. In natural conditions the looped network can appear rather in the lowest parts of rivers (deltas). 

In an open channel network one can distinguish two kinds of branches. The first one connects two junctions, i.e. its both ends are located at the neighboring junctions. The second kind of branch has one end located at a junction, whereas the opposite end is a pendant one. Note that the additional conditions, which are required to ensure the solution of flow problem, must be imposed at pendant ends. 

While for a single channel both initial value and boundary value problems can be formulated, for a channel network in principle only the boundary value problem should be formulated, since the discharges in branches and the flow profiles are the goal of computations. Although the governing equations describing this kind of flow are the same, the solution of flow equations for network becomes more complicated comparing with a single channel. 

Various approaches were proposed to solve the boundary value problem for a channel network. Some of them are applicable to tree type networks only. Similarly to a single channel, the final system of nonlinear algebraic equations cannot be efficiently solved by the standard Picard or Newton methods because the iterative process suffer from the lack of convergence. Thus, Schulte and Chaudhry (1987) introduced the discharge _Q_ as an additional unknown at each computational node (see Section 4.3.3), although they do not vary within each branch. This modification allows solving efficiently the resulting system of equations by the Newton method, but the system itself is considerably larger than the system resulting from 

4.4 Steady Gradually Varied Flow in Open Channel Networks 

149 

the approach in which the discharge _Q_ is treated as a single unknown for the whole branch. Consequently, the computational cost of the solution is increased. 

Naidu et al. (1997) have proposed an algorithm based on the decomposition of the channel network into small units. The problem is solved in each unit using the IV order Runge–Kutta method and the local solutions are connected to obtain the final solution for whole network using the shooting method. However, the proposed algorithm works for tree-type networks only. 

The steady flow problem can be also solved indirectly using the Saint-Venant equations describing the unsteady flow, with the specified, constant in time boundary conditions. After a sufficiently long time the system reaches steady state and the corresponding water surface profiles in the channel network are obtained (Cunge et al. 1980). 

All the mentioned methods do not have general character. However, it is possible to propose a very effective general algorithm, which will work for any type of network and for any kind of boundary conditions imposed at pendant channel ends. This approach based on the approximation of the governing equations by the finite difference method appeared a robust tool in the case of single channel and can be successfully adapted for a channel network. 

### **_4.4.2 Numerical Solution of Steady Gradually Varied Flow Equations in Channel Network_** 

Let us consider a channel network consisting of _M_ channels (branches). It can be either tree type or looped one. Each channel is divided into _Nj_ ( _j_ = 1, 2 , _. . ._ , _M_ ) intervals of constant or variable length _Δxi_ . The total number of grid points in whole network is _�Nj_ . In addition, let us assume positive direction of flow in each channel corresponding to the direction of increasing of the indexes. 

To solve the boundary problem for the considered network the governing ordinary differential equations (4.23) and (4.24) are approximated by the finite difference method. Equation (4.23) is approximated, as in the previous section, by centered differences, coinciding with the implicit trapezoidal rule. Since in the network branches the water can flow in both directions, this fact should be taken into account in the sign of the friction force. Therefore for channel _j_ Eq. (4.23) is approximated by the following formula: 



Similar equations are written for each interval _Δxi_ ( _i_ = 1,2, _. . ._ , _Nj_ − 1). In this way one obtains a system of _Nj_ − 1 algebraic equations with _Nj_ + 1 unknowns. There are _Nj_ water levels _hi_ at the nodes and the flow discharge _Qj_ . 

150 

4 Steady Gradually Varied Flow in Open Channels 

The system of equations (4.51) can be presented in the matrix form: 



where: 

**A** – matrix of coefficients, 



The matrix **A** of dimensions ( _Nj_ + 1) × ( _Nj_ + 1) is very sparse. Its structure is similar to the one obtained for a single channel (Fig. 4.24). Its non–zero elements are defined as follows: 

















When flow in a single channel was considered this system had to be completed by two additional equations resulting from the imposed boundary conditions. However, in the case of channel network such system of equations is written for each branch separately. To assembly them, apart from the mentioned boundary conditions, which are imposed at pendant nodes only, additional equations must be specified for each junction. For a junction of three channels _I_ , _J_ , _K_ formed by the nodes _i_ , _j_ , _k_ as presented in Fig. 4.35. one can write the continuity equation: 



151 

###### 4.4 Steady Gradually Varied Flow in Open Channel Networks 

**Fig. 4.35** Junction of three channels 



<!-- Start of picture text -->
K<br>k<br>I i<br>j<br>J<br><!-- End of picture text -->

and the energy equations: 



In the above equations the energy losses are neglected. Sometimes the velocity heads can be also neglected as relatively small. 

For each junction of the considered channel network three additional equations in form of Eqs. (4.54) and (4.55) can be written. This enables us to close the global system of equations for the entire network. The matrix of this system contains submatrices corresponding to each channel in form presented in Eq. (4.52), connected by the equations for junctions. The final matrix is banded and very sparse. 

To better illustrate the presented procedure of solution let us consider a looped channel network as presented in Fig. 4.36. It consists of seven channels and four junctions. The network has two pendant nodes, at which the boundary conditions are imposed. In all branches of the network subcritical flow is assumed. The discharge is assumed positive if the direction of the flow corresponds to the direction of increasing node indices, as shown by the arrows in Fig. 4.36. Each channel is divided into 10 intervals of constant length. Then the total number of grid points is 77. 

For each channel one can write a system of 10 equations in form of Eq. (4.51). Therefore for the entire network one obtains a global system containing 7 subsystems, written for each branch separately. Then one has 70 equations, whereas the 



<!-- Start of picture text -->
1 23 3 33<br>1 11<br>67 77<br>45 5 55 7<br>56<br>66<br>6<br>2<br>12<br>22<br>4<br>44<br>34<br><!-- End of picture text -->

**Fig. 4.36** Example of looped channel network 

152 

4 Steady Gradually Varied Flow in Open Channels 

total number of unknowns is equal to 84 (77 water levels in grid point and 7 discharges in branches). To close the system the following additional equations are introduced: 

- for the four junctions − 4 continuity equations of type (4.54) and 8 energy equations of type (4.55); 

- for the two pendant channel ends (number 1 and 77) − 2 equations given by the prescribed boundary conditions. 

Finally one obtains the global system of dimension 84×84 having 84 unknowns. In each row of the global matrix there are only 3 or 4 non-zero elements. 

Assuming subcritical flow in channel, the following conditions can be imposed at the pendant channel’s ends: 

- the water level with velocity head; 

- the water level; 

- the discharge. 

Preliminary numerical tests carried out for the considered network showed that the Newton iterative method applied to solve Eq. (4.52) failed to converge. This conclusion coincides with the well-established opinion of its poor global convergence properties (Press et al. 1992). On the other hand, application of the modified Picard method described in Subsection 4.3.4 is successful. Therefore the non-linear system of equations (4.52) is solved as follows: 



where _k_ is index of iteration and 



is modified matrix of coefficients. Numerous tests confirmed that with the presented algorithm it is possible to overcome the problem of poor convergence of the standard Picard method. 

_Example 4.12_ Let us consider a problem of the flow past an island, which occurs when a long island divides the river into two channels, as shown in Fig. 4.37. This is a well-known problem in open channel hydraulics. While some special algorithms were proposed to solve such problem (French 1985), it can be considered as a particular case of the flow in a looped channel network and solved with the method described above. 

The system consists of 4 channels and 2 junctions. The network has 2 pendant nodes at which the boundary conditions are imposed. In all branches of the network subcritical flow is assumed. The flow is assumed from the upstream end (node _u_ in Fig. 4.37) towards the downstream end (node _d_ in Fig. 4.37). The positive direction 

153 

4.4 Steady Gradually Varied Flow in Open Channel Networks 



<!-- Start of picture text -->
2<br>1 4<br>( u ) ( d )<br>3<br><!-- End of picture text -->

**Fig. 4.37** Considered channel network 

of flow in each channel is marked with an arrow. The channels have trapezoidal cross-sections. The bed elevation at the upstream end is assumed to be equal to 10.000 m above the datum, whereas at the downstream it is equal to 9.000 m. Each channel is divided into 10 intervals of constant length, which gives the total number of grid points equal to 44. First let us consider a symmetric system, where the two channels surrounding the island have the same parameters (Table 4.1). In such a case the solution must be symmetrical as well. 

The boundary conditions are specified in terms of water levels at the upstream end and the downstream end of the network: _hu_ = 11.500 m, _hd_ = 10.500 m. The results obtained for the data from Table 4.1 are displayed in Table 4.2. 

As it could be expected the flow in channel 1 bifurcated symmetrically into channels 2 and 3. To obtain these results, with the assumed accuracy of _εh_ = 0.001 m and _εQ_ = 0.001 m<sup>3</sup> /s, 18 iterations are needed. The iterations converged for arbitrary initial approximations of the discharges _Q_<sup>(0)</sup> in the channels. 

The second case concerns an asymmetrical network, in which the channels surrounding the island have different characteristics (Table 4.3). Compared to channel 2, channel 3 is longer, narrower, less smooth and has smaller slope. Consequently, the flow in channel 1 bifurcates into channels 2 and 3 in asymmetrical way. As it is shown in Table 4.4, the discharges in the two channels differ by a factor larger than 3. Also in this case no problem with convergence occurs. 

_Example 4.13_ Let us consider the steady gradually varied flow in a tree – type network taken from Naidu et al. (1997), which is presented in Fig. 4.38. It consists of 41 branches. The total number of nodes is 470. 

The parameters of the channels are given in Table 4.5. 

**Table 4.1** Characteristics of the channels from Fig. 4.37 – the symmetric case 

|Channel||Bed width|||||
|---|---|---|---|---|---|---|
|number|Length [m]|[m]|Side slope|Bed slope|_nM_|_Δx_[m]|
|1|300|4.0|1.5|0.001|0.025|30|
|2|400|3.5|1.5|0.001|0.035|40|
|3|400|3.5|1.5|0.001|0.035|40|
|4|300|4.0|1.5|0.001|0.025|30|



154 

4 Steady Gradually Varied Flow in Open Channels 

**Table 4.2** Results for the network from Fig. 4.37 – the symmetric case 

|Channel|Discharge|Upstream<br>water|Downstream<br>water level|
|---|---|---|---|
|number|_Q_[m<sup>3</sup>/s]|level [m]|[m]|
|1|14.451|11.500|11.176|
|2|7.225|11.176|10.810|
|3|7.225|11.176|10.810|
|4|14.451|10.810|10.500|



**Table 4.3** Characteristics of the channels from Fig. 4.37 – the asymmetric case 

|Channel||Bed width|||||
|---|---|---|---|---|---|---|
|number|Length [m]|[m]|Side slope|Bed slope|_nM_|_Δx_[m]|
|1|300|4.0|1.5|0.001|0.025|30|
|2|400|3.5|1.5|0.001|0.035|40|
|3|800|1.5|1.5|0.0005|0.045|80|
|4|300|4.0|1.5|0.001|0.025|30|



**Table 4.4** Results for the network from Fig. 4.37 – the asymmetric case 

|Channel|Discharge|Upstream<br>water|Downstream<br>water level|
|---|---|---|---|
|number|_Q_[m<sup>3</sup>/s]|level [m]|[m]|
|1|12.418|11.500|11.305|
|2|9.370|11.305|10.743|
|3|3.048|11.305|10.743|
|4|12.418|10.743|10.500|



In order to simplify the problem the velocity heads at the junctions are neglected. The first solution is carried out for exactly the same data as in the paper by Naidu et al. (1997). Since their method requires that the discharge is known in at least one branch, _Q_ = 40 m<sup>3</sup> /s is imposed at node number 1, while the water levels are known at all pendant nodes except the node 1 (Table 4.6). 

As the result of calculation the water profiles and discharges in all branches, including the water level at node 1, are obtained. The results of calculation by the modified Picard method differ only insignificantly from those obtained by Naidu et al. (1997). The final result with _εH_ = 0.001 m and _εQ_ = 0.1 m<sup>3</sup> /s was obtained after 18 iterations. The greatest difference, equal to 0.007 m, exists at node 1. At other nodes the depths calculated by both approaches are practically the same. 

The second solution is obtained assuming that the discharges in all branches, including the first one, are unknown. On the other hand, the water levels are known 

155 

4.4 Steady Gradually Varied Flow in Open Channel Networks 



<!-- Start of picture text -->
196<br>156<br>16<br>12<br>449<br>13<br>174 202 17 440 470<br>41<br>7 38 37<br>185 14 11 145<br>39 36<br>15 8 6 10 40<br>5 4 455 35 34<br>9 461<br>134 20 channel number<br>3<br>1 18 21<br>1 2 266<br>337 19<br>node number 27 343<br>23<br>28 33 388<br>31 26 22<br>371<br>29<br>30 32<br>24<br>377<br>360 25<br>320<br><!-- End of picture text -->

**Fig. 4.38** Channel network used in Example 4.13 (after Naidu et al. 1997) 

**Table 4.5** Characteristics of the network from Fig. 4.38 

|Channel|Bed width<br>[m]|Side slope|Bed slope|_nM_|Length [m]|Number<br>of reaches|
|---|---|---|---|---|---|---|
|1|10.0|2.0|0.000133|0.015|2,500.0|20|
|2|8.5|2.0|0.00015|0.016|2,000.0|20|
|3|4.0|2.0|0.00020|0.020|1,500.0|15|
|4|4.0|2.0|0.00021|0.020|1,400.0|15|
|5|1.5|2.0|0.00024|0.022|1,000.0|10|
|6|1.5|2.0|0.00024|0.022|1,100.0|10|
|7|3.0|2.0|0.00022|0.020|1,200.0|15|
|8|1.0|1.0|0.00025|0.022|1,000.0|10|
|9|0.5|1.0|0.00050|0.030|700.0|5|
|10|0.5|1.0|0.00050|0.030|700.0|5|
|11|1.0|1.0|0.00025|0.022|1,000.0|10|
|12|2.0|2.0|0.00024|0.022|1,000.0|10|
|13|1.5|2.0|0.00024|0.022|1,000.0|10|
|14|0.5|1.0|0.00050|0.030|700.0|5|
|15|1.75|2.0|0.00024|0.022|1,000.0|10|
|16|0.9|0.9|0.00025|0.022|900.0|10|
|17|0.5|1.0|0.00050|0.030|700.0|5|
|18|7.0|2.0|0.00016|0.017|1,700.0|15|
|19|3.5|1.0|0.00025|0.022|1,400.0|15|
|20|2.5|2.0|0.00022|0.022|1,300.0|15|
|21|4.0|2.0|0.00017|0.018|1,500.0|15|



156 

4 Steady Gradually Varied Flow in Open Channels 

**Table 4.5** (continued) 

|Channel|Bed width<br>[m]|Side slope|Bed slope|_nM_|Length [m]|Number<br>of reaches|
|---|---|---|---|---|---|---|
|22|2.7|1.0|0.00022|0.022|1,200.0|15|
|23|1.75|2.0|0.00024|0.022|1,200.0|10|
|24|2.0|2.0|0.00024|0.020|1,200.0|10|
|25|1.75|2.0|0.00024|0.022|1,000.0|15|
|26|1.5|2.0|0.00024|0.022|1,100.0|10|
|27|0.5|1.0|0.00050|0.030|700.0|5|
|28|0.5|1.0|0.00050|0.030|700.0|5|
|29|1.75|2.0|0.000024|0.022|1,000.0|10|
|30|0.5|1.0|0.00050|0.030|700.0|5|
|31|1.0|1.0|0.00025|0.025|1,000.0|10|
|32|0.5|1.0|0.00050|0.030|700.0|5|
|33|1.5|2.0|0.00024|0.022|900.0|10|
|34|1.5|1.0|0.00025|0.022|1,200.0|15|
|35|1.5|1.0|0.00025|0.022|900.0|10|
|36|1.25|2.0|0.00024|0.022|800.0|8|
|37|1.0|2.0|0.00022|0.022|1,000.0|15|
|38|1.0|1.0|0.00025|0.022|800.0|8|
|39|0.5|1.0|0.00050|0.030|700.0|5|
|40|0.5|1.0|0.00050|0.030|700.0|5|
|41|0.75|2.0|0.00024|0.022|700.0|8|



**Table 4.6** Water levels imposed at pendant nodes in Fig. 4.38 

|Node|Water levels [m]|Node|Water levels [m]|
|---|---|---|---|
|1|12.199|337|9.608|
|128|10.265|343|9.497|
|134|10.246|360|9.600|
|145|10.242|371|9.587|
|156|10.235|377|9.494|
|174|10.248|388|9.496|
|185|10.249|440|9.212|
|196|10.232|449|9.568|
|202|10.236|455|9.675|
|266|9.761|461|9.231|
|320|9.489|470|9.234|



at all pendant nodes, including node 1, where the previously calculated value is applied. Thus one can expect the resulting discharge value _Q_ in the first branch to be close to the value specified in the previous calculation, i.e. _Q_ = 40 m<sup>3</sup> /s. Indeed, the obtained result is _Q_ = 40.005 m<sup>3</sup> /s. Other discharges are in similarly good agreement with the previous results (differences being less than 0.4%). The solution was obtained after 17 iterations. Thus, it seems that the approach basing on the finite difference discretization of the steady flow equation combined with improved Picard iterative scheme works efficiently for both tree – type and looped channel network and for any type of boundary conditions specified at its pendant ends. 

157 

References 

### **References** 

- Ascher UM, Petzold LR (1998) Computer methods for ordinary differential equations and differential – algebraic equations. SIAM, Philadelphia 

Bjorck A, Dahlquist G (1974) Numerical methods. Prentice-Hall, Englewood Cliffs, NJ 

Chow VT (1959) Open channel hydraulics. Mc Graw-Hill, New York 

- Cunge J, Holly FM, Verwey A (1980) Practical aspects of computational river hydraulics. Pitman Publishing, London 

French RH (1985) Open channel hydraulics. McGraw-Hill, New York 

- Gray DM, Prowse TD (1993) Snow and floating ice. In: Maidment DR (ed.) Handbook of hydrology. McGraw-Hill, New York 

- Le Veque RJ (2007) Finite difference methods for ordinary and partial differential equations: Steady–state and time dependent problems. SIAM, Philadelphia. 

- Naidu BJ, Murty Bhallamudi S, Narasimhan S (1997) GVF computation in tree type channel networks. J. Hydr. Engng. ASCE 123 (8):700–708 

- Press WH, Teukolsky SA, Veterling WT, Flannery BP (1992). Numerical recipes in C, Cambridge University Press 

- Roberson JA, Cassidy JJ, Chaudhry MH (1998) Hydraulic engineering, 2nd edn. Wiley, New York Schulte AM, Chaudhry MH (1987) Gradually-varied flow in open channel network. J. Hydr. Res. 25 (3):358–371 

- Singh VP (1996) Kinematic wave modelling in water resources: Surface water hydrology. John Wiley, New York 

- Stoer J, Bulirsch R (1980) Introduction to numerical analysis. Springer-Verlag, New York 

- Szymkiewicz R (2000) Mathematical modeling of river flow. Polish Scientific Publisher PWN, Warsaw (in polish) 

- Szymkiewicz R, Szymkiewicz A (2004) Method to solve the non-linear systems of equations for steady gradually varied flow in open channel network. Commun. Numer. Methods Engng. 20 (4):299–312 

## **Chapter 5 Partial Differential Equations of Hyperbolic and Parabolic Type** 

### **5.1 Types of Partial Differential Equations and Their Properties** 

### **_5.1.1 Classification of the Partial Differential Equations of 2nd Order with Two Independent Variables_** 

The governing equations for unsteady flow and transport processes presented in Chapter 1 are partial differential equations (PDEs). They result from the application of the laws of conservation of some physical quantities like mass and momentum, and describe the evolution of an unknown function (like the water stage, discharge or concentration) with respect to temporal and spatial variables. Other examples of PDEs, in form of simplified flood routing models, will be introduced later in this book. This chapter discusses in more detail the basic properties of PDEs and numerical techniques applied to solve them. 

As we could see in Chapter 1, a PDE may contain derivatives of various orders (first or second order in the presented examples). Thus, any PDE is additionally labeled as being of 1st order, 2nd order, 3rd order and so on. The order of a partial differential equation corresponds to the highest order of derivative which appears in the considered equation. Moreover, PDEs can be classified as hyperbolic, parabolic and elliptic ones. Since the proper designation of the type of considered equation is essential to formulate well-posed solution problem, let us begin with a brief discussion of classification of the partial differential equations. 

For an equation of 2nd order with two independent variables there is very simple way of classification (Potter 1973). Such kind of equation can be written in the following general form: 



where: 

_t_ , _x_ – independent variable (time and space position respectively), _f_ ( _x_ , _t_ ) – dependent variable, 

> R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_5, ⃝C Springer Science+Business Media B.V. 2010 

159 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

160 

_a1_ , _. . ._ , _a6_ – equation’s coefficients, 

_δ_ ( _x, t_ ) – source term, 

Depending on the form of coefficients, Eq. (5.1) is considered as: 

- linear equation with constant coefficients when _a1_ , _a2_ , _a3_ , _. . ._ = const., 

- linear equation with variable coefficients when _a1_ = _a1_ ( _x_ , _t_ ), _a2_ = _a2_ ( _x_ , _t_ ), _a3_ = _a3_ ( _x_ , _t_ ), _. . ._ , 

- quasi-linear equation when _a1_ = _a1_ ( _x_ , _t_ , _f_ ), _a2_ = _a2_ ( _x_ , _t_ , _f_ ), _a3_ = _a3_ ( _x_ , _t_ , _f_ ), _. . ._ , 

- non-linear equation when _a1_ = _a1_ ( _x_ , _t_ , _f, ∂f_ / _∂t, ∂f/∂x_ ), _a2_ = _a2_ ( _x_ , _t_ , _f, ∂f_ / _∂t, ∂f/∂x_ ), _a3_ = _a3_ ( _x_ , _t_ , _f, ∂f_ / _∂t, ∂f/∂x_ ), _. . ._ . 

As far as the type of equation is considered, Eq. (5.1) is called: 

- elliptic, when _�_ = _a_<sup>2</sup> 2<sup>−</sup><sup>_a_1 ·</sup><sup>_a_3</sup><sup>_<_0</sup> 

- parabolic, when _�_ = _a_<sup>2</sup> 2<sup>−</sup><sup>_a_1 ·</sup><sup>_a_3= 0,</sup> 

- hyperbolic, when _�_ = _a_<sup>2</sup> 2<sup>−</sup><sup>_a_1 ·</sup><sup>_a_3</sup><sup>_>_0.</sup> 

Note that the value of discriminant _�_ determining the type of equation depends only on the values of the coefficients related to the derivatives of the 2nd order. Thus the type of 2nd order equation does not depend on the presence of the terms containing derivatives of 1st order or on the presence of source terms. The system of classification is valid globally only for linear equations with constant coefficients. When the coefficients vary it is possible that Eq. (5.1) can change its type in the considered domain, so the classification is valid only locally. 

In the case of open channel flow the partial differential equations of 2nd order are associated with pollutant transport and simplified models of unsteady flow in the form of diffusive wave (see Chapters 1, 7 and 9). They have the form of advectiondiffusion equation, i.e.: 



where: 

_f_ – scalar function as pollutant concentration or temperature, 

_U_ – cross-sectional average flow velocity, 

_D_ – coefficient of diffusion. 

Comparing Eqs. (5.2) and (5.1) one obtains: 



which means, that the advection-diffusion equation (5.2) is of parabolic type. 

There are some general relations, which enable us to predict the type of PDE even without a detailed analysis. It is known, that the flow problems variable in time (unsteady ones) are described by the equations of hyperbolic or parabolic type. If the considered problem is related to wave propagation, then the equations will be 

5.1 Types of Partial Differential Equations and Their Properties 

161 

certainly of hyperbolic type. However, if in the equations some processes of dissipation are represented, as for example the stresses resulting from the liquid viscosity, heat conduction or mass diffusion, then one can expect equations of parabolic type. Finally, elliptic equations usually describe steady problems and equilibrium states and are rarely used in open channel flow modeling. 

### **_5.1.2 Classification of the Partial Differential Equations via Characteristics_** 

The presented method of classification, while simple and clear, can be applied for the equations of 2nd order only. If we have a single equation of first order or a system of such equations, their type can be defined by the analysis of characteristics. To better explain this approach, let us make a short introduction to the characteristics concept using the simplest type of equation, i.e. the pure advection equation: 



where _U_ is advective velocity. Both sides of Eq. (5.3) are multiplied by _dt_ : 



If we introduce the following notation: 



and substitute it in Eq. (5.4), then we obtain: 



The right hand side of Eq. (5.6) is the total derivative of the function _f_ ( _x, t_ ), so that Eq. (5.4) can be rewritten as follows: 





or 



Therefore Eq. (5.3), which is a PDE, can be integrated as an ordinary differential equation, along the lines defined by Eq. (5.5) in ( _x, t_ ) plane. From Eq. (5.8) results that in this case, the time variation of function _f_ is equal to zero along this line. The formula: 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

162 



defines the characteristics of the pure advection equation, or more precisely, it determines the slope of the line tangent to the characteristic lines. In a general case, when _U_ ̸ = const., the characteristics are curves in ( _x_ , _t_ ) plane. 

The concept of characteristics can be used to classify the partial differential equations of 2nd order like Eq. (5.1). Fletcher (1991) showed, that the discriminant _�_ = _a_<sup>2</sup> 2<sup>−</sup><sup>_a_1·</sup><sup>_a_3 determines both type of equation and the nature of its characteristics.</sup> He found out that: 

- hyperbolic equation has two real characteristics, 

- parabolic equation has one real characteristic; 

- elliptic equation has two imaginary characteristics. 

This is valid for the equations of 1st order as well. 

Coming back to the pure advection equation (5.3), one can find out that this equation is of hyperbolic type. It has one characteristic only, which is real. In addition one can notice that with _U_ = const. its characteristics are straight lines as presented in Fig. 5.1. 

Since along these lines the function _f_ ( _x_ , _t_ ) does not vary, the governing equation can be easily integrated as an ordinary differential equation, on condition that the initial data are given along any line in ( _x_ , _t_ ) plane, which is not a characteristics. These properties form the base of the method of characteristics, one of the fundamental method for solution of PDEs of hyperbolic type (Abbott and Basco 1989). For a long time this method was the only one commonly applied to solve such kind of equations. Even now, the method of characteristics is widely applied to solve the unsteady pipe flow equations, very similar to the Saint Venant equations (Abbott and Basco 1989). In open channel hydraulic, as we shall see later, if the advection diffusion equation is solved by a splitting approach, the method of characteristics is frequently used for solving the advective part. 

As an instructive exercise, let us apply this method to solve of the pure advection equation (5.3). From Eq. (5.7a) results that the function _f_ ( _x_ , _t_ ) does not vary along the characteristic line (5.7b). This fact allows us to find the following formula, representing an exact solution of Eq. (5.3): 

**Fig. 5.1** Characteristics of the pure advection equation for _U_ = const. > 0 



<!-- Start of picture text -->
t<br>U > 0<br>1<br>tg φ  = —<br>U<br>φ<br>x<br><!-- End of picture text -->

5.1 Types of Partial Differential Equations and Their Properties 

163 



Therefore a particle, which at current moment _t_ is in the position defined by _x_ , at _t_ = _t_ 0 was in the following position: 



Since in this case we assumed a constant flow velocity, then the characteristics being a straight line of slope 1/ _U_ , allows us to rewrite Eq. (5.10) as 



From Eq. (5.12) results that the advection equation with constant advective velocity _U_ causes pure translation of the initial distribution of _f_ ( _x_ , _t_ 0) along the channel axis. This information is very useful, since it helps us to evaluate the accuracy of numerical methods of solution. 

In open channel hydraulics the pure advection equation describes the advective transport of pollutants derived in Chapter 1, and as well as the kinematic wave equation, which is a simplified flood routing model (see Chapter 9). Apart from single equations of 1st order, systems of 1st order PDEs exist, as for example the system of Saint Venant equations. Classification of a system of equations can be also carried out using analysis of characteristics. 

In the case of two independent variables _t_ and _x_ the system of two 1st order PDEs with two dependent variables _u_ ( _x_ , _t_ ) and _v_ ( _x_ , _t_ ) has the following general form (Fletcher 1991): 



In matrix notation it can be written as: 



164 5 Partial Differential Equations of Hyperbolic and Parabolic Type 

With 



where: 

- – vector of unknown functions, 

- **A** , **B** – matrices of coefficients, **F** – vector of right hand side. 

From the definition of characteristics results that the total derivative of **_�_** is constant along a characteristic, so that 



where **I** is identity matrix given as follows: 



Thus, Eqs. (5.10), (5.11) and (5.12) can be written together as: 



From the formal definition, the characteristic are such lines in time-space domain, at which the governing system of equation does not possesses a unique solution. This take place when the determinant of the coefficient matrix is equal to zero. This condition leads to the ordinary differential equation, which defines the characteristics. Equation (5.14) has no solution when the determinant of the matrix of coefficients in Eq. (5.16) is equal to zero, i.e. if det ( **A** · _dx_ − **B** · _dt_ ) = 0. This condition can be written as: 



Equation (5.17) has two roots. Their values depend on the value of discriminant _�_ , which is given by: 



5.1 Types of Partial Differential Equations and Their Properties 

165 

The value of discriminant _�_ determines the type of the system of equation. The possible cases are following: 

- for _�_ > 0 Eq. (5.17) has two real roots and the system (5.13) is hyperbolic, 

- for _�_ = 0 Eq. (5.17) has one real and one imaginary root and the system (5.13) is parabolic, 

- for _�_ < 0 Eq. (5.17) has two imaginary roots and the system (5.13) is elliptic. 

Although we consider classification of the systems of PDEs, the same method of classification is valid for a scalar equation as well. Let us reconsider the pure advection equation (5.3). For this equation relation (5.16) takes the following form: 



The equation of characteristic is given by the matrix determinant of Eq. (5.19), which must be equal to zero. Then the condition: 



gives the following relation: 



In such a way we obtained previously derived Eq. (5.9), which defines the characteristic of pure advection equation. Since this characteristic is a real one, the advection equation is classified as a hyperbolic PDE. 

### **_5.1.3 Classification of the Saint Venant System and Its Characteristics_** 

Let us apply the considered approach to examine the system of Saint Venant equations (1.77) and (1.78): 



5 Partial Differential Equations of Hyperbolic and Parabolic Type 

166 

This system is rewritten in the form of Eq. (5.14) with: 



The equation of characteristics is derived from the condition (5.15), which gives: 



From Eq. (5.23) one obtains the following equation: 



Equation (5.24) has positive discriminant _�_ = 4 _U_<sup>2</sup> − 4( _U_<sup>2</sup> − _g_ · _H_ ) = 4 _g_ · _H_ . Its square root is equal to: 



and the equations of characteristics are: 



Therefore the system of Saint Venant equations, having two real characteristics, is classified as hyperbolic. In a similar manner one can classify the systems containing _n_ equations of first order. We will apply this approach in Section 8.5 to classify the system of three equations. 

The physical interpretation of the expression<sup>~~√~~</sup> _<u>g</u>_ <u>·</u> _<u>H</u>_ which appeared in Eq. (5.26) results from the analysis of the simplified form of governing equations (5.22). The first simplification deals with neglecting the source and the advective terms. Equation (5.22) become the following ones: 



5.1 Types of Partial Differential Equations and Their Properties 

167 

Note that omitting the right side of Eq. (5.22a) means that the frictionless flow in horizontal channel is considered. In the next step the linearization of Eq. (5.27b) is performed. Instead of variable coefficient _H_ ( _x_ , _t_ ) a constant one, equal to the average flow depth _H_ is introduced. Therefore we obtain: 



Both equations are differentiated with regard to _x_ and to _t_ respectively, yielding: 



Combining these equations one obtains: 



In a similar way, inverting the order of differentiation of Eqs. (5.28a) and (5.28b), we arrive to the second possible form of the shallow water wave equation 



Setting: 



Equations (5.30) and (5.31) can be presented in the common form: 



In this equation _f_ represents the flow depth _H_ ( _x_ , _t_ ) or the flow velocity _U_ ( _x_ , _t_ ). This equation has the form of the well-known wave equation, describing a vibrating stretched string, where _c_ represents the wave speed in the string (for details see e.g. Billingham and King (2000)). In the case of shallow water equations _c_ is the speed of wave occurring at the free surface of water. Coming back to the equations of characteristics (5.26) one can find out that they represent the net velocities of propagating small disturbances of _H_ or _U_ arising at the surface of stream flowing at the velocity _U_ . These disturbances travel in space and time depending of the relation between _U_ and _c_ . More information on interpretation of the characteristics is 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

168 

provided by an appropriate transformation of the system of shallow water equations (5.22) (Billingham and King 2000, Hervouet 2007, Tan Weiyan 1992). 

Le us consider the system of Eqs. (5.22a) and (5.22b) in its homogeneous version: 



Using relation (5.32) the flow depth is expressed as: 



Substituting Eq. (5.32) in the continuity equation (5.34b) yields: 



Developing the derivatives in (5.36) and dividing both sides of the obtained equation by the factor _g_ · _c_ gives: 



Dynamic equation (5.34a) coupled with Eq. (5.35) yields: 



If we now add and subtract Eqs. (5.37) and (5.38) we obtain the following two equations: 



In such a way the governing system of shallow water equations is expressed in an equivalent form, in which the characteristic equations are involved. Note that both equations describe advective transport of the quantities _U_ + 2 _c_ or _U_ − 2 _c_ with advective celerity _U_ + _c_ or _U_ − _c_ , respectively. Therefore using Eqs. (5.26a) and (5.26b) they can be rewritten as: 



5.1 Types of Partial Differential Equations and Their Properties 

169 



These equations show that the quantities _U_ ± 2 _c_ are constant on the characteristic curves determined by _U_ ± _c_ . The transported quantities are called the Riemann invariants of the system (5.34). The characteristic equations are of great importance for numerical solution of the hyperbolic equations since they allow for an appropriate formulation of the required auxiliary conditions. This is because the character of characteristics vary depending on the relation between the flow velocity _U_ and the wave celerity _c_ . On the other hand these variables are related to each other via the Froude number _Fr_ defined by Eq. (1.17). This number, being the ratio of _U_ and _c,_ allows us to determine the character of channel flow. Assuming _U_ > 0 the following situations are possible: 

- if _U_ < _c_ , ( _Fr_ < 1) the flow is subcritical: the wave celerity exceeds the flow velocity, so any flow disturbance at the considered channel reach travels in both directions, downstream and upstream; 

- if _U_ > _c_ , ( _Fr_ > 1) the flow is supercritical: the flow velocity exceeds the wave celerity, so any flow disturbance at the considered channel reach travels in one direction – downstream; 

- if _U_ = _c_ , ( _Fr_ = 1) the flow is critical. 

The relation between the characteristics of hyperbolic equations and the required auxiliary conditions is the subject of the next section. 

### **_5.1.4 Well Posed Problem of Solution of the Hyperbolic and Parabolic Equations_** 

Classification of the partial differential equations has essentials meaning, because it allows us to formulate properly the problem of solution for the considered PDE. PDEs are solved in strictly defined domains and for strictly defined auxiliary conditions, imposed at the limits of the solution domain. In other words, each solution of the equation or the system of equations corresponds to the conditions a priori imposed on this unknown solution. Therefore the function being the solution of the considered problem must satisfy simultaneously both the solved equation in the domain of solution and the additional conditions imposed at its limits. These additional conditions usually are called the limit conditions. They are divided in two kinds: the initial conditions and the boundary conditions. The initial conditions provide information on the function or the functions in the solution domain at the initial moment _t0_ . They are present in the unsteady problems, when one of the independent variable is time. The boundary conditions, on the other hand, provide information imposed at the physical boundary the considered domain of solution. In open channel flow problems such boundaries are constitute by the upstream end 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

170 

and the downstream end of a channel. If at the boundary of the considered domain the value of the unknown function is given, then it is said that Dirichlet condition is imposed, whereas if the derivative of the function is set, then it is said that Neumann condition is imposed. Apart from the mentioned conditions so-called mixed conditions can be formulated as well. Since in open channel flow they are not applied we do not them discussed here. 

After Hadamard (Fletcher 1991) the problem equation and auxiliary conditions of solution, i.e. the limit conditions are mathematically well posed if they ensure: 

- existence of solution, 

- uniqueness of solution. 

- continuous dependence of solution on the auxiliary conditions. 

The problem of proving the existence of solution is important from the point of view of mathematical formalism. For the purposes of engineering practice, however, it is reasonable to assume that the model equations based on the principles of conservation laws have solution in most cases. 

The uniqueness of solution is related to the auxiliary conditions formulated for the considered type of equation. Generally, if there are too few boundary conditions no unique solution can be obtained, whereas too many conditions imposed at the boundary can generate unphysical solution (Fletcher 1991). In order to properly define the auxiliary conditions one needs to know the type of solved equations. For this reason, the correct classification of considered partial differential equations and the knowledge of their characteristics structure has fundamental meaning for well posedness of solution problem. 

For some problems the way of proper formulation of the initial and boundary conditions is well known. For instance for the hyperbolic equations the following rule is valid: at every boundary of the considered solution domain it is necessary to impose as many additional conditions as many characteristics enter the solution domain from this boundary. This rule results from the nature of characteristics discussed in the preceding section. As an example, let us consider the pure advection equation (5.13): 



The characteristics of Eq. (5.41) on the plane ( _x_ , _t_ ), given by Eq. (5.9) and dependent on the sign of the flow velocity _U_ , are presented in Fig. 5.2. Then if we want to solve Eq. (5.41) in the domain: 0 ≤ _x_ ≤ _L_ and _t_ ≥ 0 with _U_ > 0, the following auxiliary conditions must be prescribed (Fig. 5.2a): 

- initial condition: 

at _t_ = 0 _f_ ( _x_ , 0) = _fi_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ should be imposed 

- boundary condition: 

5.1 Types of Partial Differential Equations and Their Properties 

171 



<!-- Start of picture text -->
a) b)<br>t t<br>x x<br>x = 0 U  > 0 x = L x = 0 U < 0 x = L<br><!-- End of picture text -->

**Fig. 5.2** The characteristics for pure advection equation (5.27) for _U >_ 0 ( **a** ) and for _U_ < 0 ( **b** ) 

at the upstream end _x_ =0 _f_ (0, _t_ )= _f_ 0( _t_ ) for _t_ ≥ 0 should be imposed where _fi_ ( _x_ ) and _f_ 0( _t_ ) are given. 

If the velocity vector has opposite (negative) sign, as in Fig. 5.2b, then the boundary condition must be imposed at the opposite end of the channel reach i.e. at _x_ = _L_ . Generally, for the pure advection equation the boundary condition is prescribed at the end, where the water inflows. 

As the second example let us consider the system of Saint Venant equations (5.22). In the preceding section it was shown that this system possesses two families of real characteristics given by Eqs. (5.26a) and (5.26b): 





In this case the structure of the characteristics in the solution domain (0≤ _x_ ≤ _L_ and _t_ ≥ 0) can vary according to the relation between the flow velocity _U_ and the wave celerity in the shallow water _c_ = _(g_ · _H)_<sup>1</sup><sup>_/_2</sup> . If _U < (g_ · _H)_<sup>1</sup><sup>_/_2</sup> , i.e. for the subcritical flow when the Froude number is less than unity ( _Fr_ < 1), both families of characteristics are inclined in the opposite directions. Their form is presented in Fig. 5.3. 

Since two characteristics enter the solution domain through the line _t_ = 0, two initial conditions must be prescribed: _U_ ( _x_ ,0) = _Ui_ ( _x_ ), _H_ ( _x_ ,0) = _Hi_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ . As only one characteristic enters the solution domain through each of the boundaries _x_ = 0 and _x_ = _L_ , then at each channel end only one additional condition must be imposed: _U_ (0, _t_ ) = _U_ 0( _t_ ) or _H_ (0, _t_ ) = _H_ 0( _t_ ) for _t_ ≥0 and _U_ ( _L_ , _t_ ) = _UL_ ( _t_ ) or _H_ ( _L_ , _t_ ) = _HL_ ( _t_ ) for _t_ ≥ 0. 

If _U > (g_ · _H)_<sup>1</sup><sup>_/_2</sup> , i.e. for the supercritical flow in the channel, when the Froude number is greater than unity ( _Fr_ > 1), both families of characteristics are inclined in the same direction. Their form is presented in Fig. 5.3 by dashed lines. In this 

5 

Partial Differential Equations of Hyperbolic and Parabolic Type 

172 



<!-- Start of picture text -->
t<br>+ +<br>– –<br>– + – +<br>– + +<br>−<br>x  = 0 x  =  L x<br><!-- End of picture text -->

**Fig. 5.3** Characteristics for the system of Saint Venant equations with _U < (g_ · _H)_<sup>1</sup><sup>_/_2</sup> ( _solid lines_ ) and for _U > (g_ · _H)_<sup>1</sup><sup>_/_2</sup> ( _dashed lines_ ) 

case the initial conditions are prescribed identically as previously, so both functions _H_ and _U_ must be imposed for _t_ = 0 and 0 ≤ _x_ ≤ _L_ . The boundary conditions are specified as follows: at the upstream end of the channel _x_ = 0, both functions _U_ (0, _t_ ) = _U_ 0 ( _t_ ) and _H_ (0, _t_ ) = _H_ 0 ( _t_ ) for _t_ ≥ 0 have to be imposed, whereas at the downstream end _x_ = _L_ no condition is required, since through this boundary no characteristic enters the solution domain (Fig. 5.3). 

As results from the presented discussion, the knowledge of the characteristics structure is indispensable in the case of hyperbolic equations because it allows us to prescribe correctly the required auxiliary conditions and consequently to ensure well-posedness of the solution problem. 

Quite a different situation appears in the case of the partial differential equations of parabolic type. In such a case the characteristics are not useful since some of them have imaginary character. The problem of proper formulation of the auxiliary conditions for these equations is well known. To ensure the unique solution of the parabolic equation as diffusion equation (5.17): 



in the solution domain, i.e. for 0 ≤ _x_ ≤ _L_ and _t_ ≥ 0, the following initial-boundary conditions should be specified (Fig. 5.4): 

- for _t_ = 0 the initial condition takes the form: _f_ ( _x_ ,0) = _fi_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ , 

- at the upstream end _x_ = 0 the Dirichlet boundary condition _f_ (0, _t_ ) = _f_ 0( _t_ ) for _t_ ≥ 0, is applied, 

- at the downstream end _x_ = _L_ either the Dirichlet boundary condition _f_ (0, _t_ ) = _fL_ ( _t_ ) for _t_ ≥ 0, or the Neumann condition _∂f_ ( _L_ , _t_ )/ _∂x_ = _φL_ ( _t_ ) for _t_ ≥ 0 is applied. 

Of course, the Dirichlet and Neumann conditions can be inverted and imposed at opposite ends as listed above. However we have to remember that for the advectiondiffusion equation, which is also of parabolic type, the Dirichlet condition must 

5.1 Types of Partial Differential Equations and Their Properties 

173 

**Fig. 5.4** Auxiliary conditions on the solution domain limits for the parabolic equation 



<!-- Start of picture text -->
t<br>boundary condition  f 0 ( t )<br>boundary condition  fL  ( t )  or  f L ( x )<br>x<br>initial condition  f i ( x )<br>t = 0<br>x = 0 x = L x<br><!-- End of picture text -->

be specified at least at one boundary. For a system of parabolic equations a set of additional conditions, similar to the one presented above, have to be imposed for each dependent variable (Fletcher 1991). 

The initial and boundary conditions i.e. the functions _fp_ , _f_ 0 and _fL_ , one should be consistent. Otherwise, false gradients of the function _f_ ( _x_ , _t_ ) can occur during the computation. They can give rise to numerical disturbances. 

The third condition of well-posedness, i.e. stability, requires that insignificant variations of the initial and boundary conditions cause only insignificant variations of the obtained solution. Usually the additional conditions have approximate character. If they are not fulfilled exactly then the errors generated during computation will increase in uncontrolled manner and consequently these errors can dominate the numerical solution. This problem is especially important for the hyperbolic equations. 

By analogy one can formulate similar requirements in relation to the numerical algorithm. It is assumed that the numerical problem is well-posed if: 

- the numerical solution exists. 

- the numerical solution is unique, 

- the numerical solution continuously depends on the approximate auxiliary conditions. 

As states Fletcher (1991), the well-posed numerical problem requires not only the well-posedness of the solution problem for the partial differential equations, but it requires also that the numerical algorithm of solution is well-posed (stable). Only in such a case an approximate solution of the well-posed numerical problem will be close to the exact solution of the well-posed problem for the partial differential equation. 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

174 

### **_5.1.5 Properties of the Hyperbolic and Parabolic Equations_** 

A classical hyperbolic equation, often used as an example to demonstrate the properties of this type of equations, is the linear wave equation (5.33): 



where: 

_t_ – time, 

_x_ – position, 

_c_ – celerity of the wave propagation (in this case = ( _g_ · _H_ )<sup>1</sup><sup>_/_2</sup> ) 

- _f_ ( _x_ , _t_ ) – function satisfying Eq. (5.44), which can be either the flow depth _H_ ( _x_ , _t_ ) or the flow velocity _U_ ( _x_ , _t_ ). 

Generally Eq. (5.44) describes the propagation of a small disturbance on the surface of shallow body of perfect liquid. Assuming _c_ = 1, one obtains: 



Assume that we seek the solution of Eq. (5.45) in the following domain: 0 ≤ _x_ ≤ 1 and _t_ ≥ 0. Since this equation has two real characteristics described by the equations _dx_ / _dt_ = 1 and _dx_ / _dt_ = −1, respectively. shown in Fig. 5.5 (Fletcher 1991), additional conditions must be given at _t_ = 0, _x_ = 0 and _x_ = 1. 

After Fletcher (1991) let us assume the following initial-boundary conditions: 

**–** initial conditions 



**–** boundary conditions 





<!-- Start of picture text -->
t<br>0      1,        0≤ x ≤ t ≥<br>dx dx<br>= − 1 =1<br>dt dt<br>0                                                                              1 x<br><!-- End of picture text -->

**Fig. 5.5** Characteristics of Eq. (5.45) 

5.1 Types of Partial Differential Equations and Their Properties 

175 

**Table 5.1** The values of function (5.33) for 0 ≤ _x_ ≤ 1 

|_x_|_f_(_x_,_t_)|_x_|_f_(_x_,_t_)|
|---|---|---|---|
|0.00|0.000|0.60|−0.294|
|0.10|0.294|0.70|−0.476|
|0.20|0.476|0.75|−0.500|
|0.25|0.500|0.80|−0.476|
|0.30|0.476|0.90|−0.294|
|0.40|0.294|1.00|0.000|
|0.50|0.000|−|−|



For the above specified conditions, Eq. (5.45) has an exact solution (Fletcher 1991): 



This solution has character of a non-damped oscillation, independent of the time _t_ . The values of function (5.46) are displayed in Table 5.1. 

The lack of attenuation of the propagating wave is a typical feature of linear hyperbolic equations. For this reason any discontinuity, introduced into their solution by initial or boundary conditions, will never disappear. Moreover, in the case of the hyperbolic non-linear equations a discontinuity in the solution domain may occur even if the initial and boundary conditions are continuous. 

As far as parabolic PDEs are considered, they arise for problems associated with dissipative mechanisms like, for instance, the liquid viscosity or the diffusive mass or heat transport. The most popular example of such type of equation is the diffusion equations describing the transport of mass or energy without the advection. For the coefficient of diffusion equal to unity ( _D_ = 1 m<sup>2</sup> /s) the diffusion equations is as follows: 



We are looking for its solution in the same domain as it was done previously for the hyperbolic equation, i.e. for 0 ≤ _x_ ≤ 1 and _t_ ≥ 0, with the following auxiliary conditions: 



For those conditions Eq. (5.47) has the following analytical solution (Fletcher 1991): 



From Eq. (5.48) results that the function _f_ ( _x_ , _t_ ) is attenuated exponentially. This process illustrates the mechanism of dissipation. Note that in the hyperbolic 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

176 

**Table 5.2** The values of function (5.48) for 0 ≤ _x_ ≤ 1 

|_x_|_f_(_x, t_=0.0)|_f_(_x, t_=0.05)|_f_(_x, t_=0.10)|
|---|---|---|---|
|0.00|0.000|0.000|0.000|
|0.10|0.309|0.189|0.115|
|0.20|0.588|0.359|0.219|
|0.30|0.809|0.494|0.302|
|0.40|0.951|0.581|0.354|
|0.50|1.000|0.610|0.373|
|0.60|0.951|0.581|0.354|
|0.70|0.809|0.494|0.302|
|0.80|0.588|0.359|0.219|
|0.90|0.309|0.189|0.115|
|1.00|0.000|0.000|0.000|



equations the lack of such a mechanism leads to non-attenuated oscillations. As the solution of a parabolic equation advances in time, it is diffused in space. The presence of the dissipation mechanism causes that even if the initial or boundary conditions contain a discontinuity, it disappears after some time, and the solution inside the considered domain will be always smooth. The function _f_ ( _x_ , _t_ ) for the selected values of time: _t_ = 0, _t_ = 0.05 and _t_ = 0.10 are displayed in Table 5.2. One can see, that the wave is strongly attenuated as time increases. 

The solutions of hyperbolic and parabolic equations presented above can be interpreted in a more general way, via analysis of the Fourier representation of a general solution of wave equation. The Fourier representation of the solution of wave equation can be written as follows (Fletcher 1991): 



where _fm_ ( _x_ , _t_ ) is _m_ th component of representation. Since both considered equations were assumed to be linear, the components of the Fourier representation can be considered independently. Each of them has the following form: 



where: 

_Am_ – amplitude of the _m_ th component, 

_m_ – wave-number related to the components’ wave length _λ_ by formula _m_ = 2 _π_ / _λ_ , 

- _p_ ( _m_ ) – dissipation parameter, which determines how rapidly the amplitude of the wave is attenuated, 

_q_ ( _m_ ) – wave propagation speed, 

_i_ – imaginary unit. 

5.1 Types of Partial Differential Equations and Their Properties 

177 

Equation (5.50) describes the propagation of a plane wave that is subjected to both dissipation and dispersion. The propagating wave is described by two parameters: amplitude and phase speed. If during propagation the amplitude is attenuated, i.e. decreases in time, it is said that the wave is subjected to dissipation. If during propagation the phase speed varies, it is said that the wave is subjected to dispersion. 

Let us assume, that the movement is described by the equations discussed earlier. Introducing successively Eq. (5.50) into these equations one can determine the dissipation parameter _p_ ( _m_ ) and the wave speed _q_ ( _m_ ). Consequently one obtains a particular form of Eq. (5.50) corresponding to the considered equations: 

Since the wave described by Eq. (5.50) must satisfy the partial differential equation (5.44), it can be substituted into this equation. The derivatives of 2nd order in Eq. (5.44) are given as: 







Substitution of Eqs. (5.51) and (5.52) in Eq. (5.44) yields: 

_Am_ · exp ( − _p_ ( _m_ ) _t_ ) exp ( − _i_ · _m_ ( _x_ − _q_ ( _m_ ) _t_ ))( − _p_ ( _m_ ) + _i_ · _m_ · _q_ ( _m_ ))<sup>2</sup> + (5.53) − _c_<sup>2</sup> · _Am_ · exp ( − _p_ ( _m_ ) _t_ ) exp ( − _i_ · _m_ ( _x_ − _q_ ( _m_ ) _t_ )( − _i_ · _m_ )<sup>2</sup> = 0 

Dividing both sides of Eq. (5.53) by Eq. (5.50) and rearranging them one obtains the following expression: 



from which results: 





Then the wave (5.50) satisfying the wave equation (5.44) is expressed as follows: 



5 Partial Differential Equations of Hyperbolic and Parabolic Type 

178 

This is a confirmation of the previously obtained result – the plane wave satisfying the wave equation (5.44) moves without any deformation. In other words, such a wave does not dissipate. 

A similar approach can be applied to the examine the propagation of a plane wave governed by the diffusion equation: 



As the wave described by Eq. (5.50) must satisfy the partial differential equation (5.58), let us substitute them . The derivative of 1st order with regard to time is given as: 



On the other hand, the derivative of 2nd order with regard to _x_ is given by Eq. (5.52). Substitution of Eqs. (5.59) and (5.52) in Eq. (5.58) yields: 



After dividing both sides of Eq. (5.60) by Eq. (5.50) one obtains: 



From this relation results that: 



Therefore the plane wave governed by the diffusion equation (5.58) is as follows: 



In this equation one can notice the factor representing the dissipation process which is responsible for attenuation of the wave amplitude with time. Therefore the properties of the parabolic partial differential equation observed in its exact solution (5.48) are confirmed by the Fourier analysis. 

### **_5.1.6 Properties of the Advection-Diffusion Transport Equation_** 

The wave equation and the diffusion equation are rather seldom applied in open channel hydraulics. However, both equations are closely related to the advectiondiffusion transport equations (1.157) or (1.174) describing the transport of mass or 

5.1 Types of Partial Differential Equations and Their Properties 

179 

heat in open channels. They can be rewritten in simplified form as: 



where: 

_f_ ( _x_ , _t_ ) – function represented transported quantity, 

_U_ – cross-sectional average flow velocity, _D_ – coefficient of diffusion. 

_δ_ – source term. 

The advection-diffusion transport equation is one of the most challenging equations in mathematical physics, as it represents a superposition of two very different transport processes: advection and diffusion. The first one has hyperbolic character, whereas the second one has parabolic character. In the preceding section we discussed the properties of the hyperbolic and parabolic partial differential equations separately, showing that they are completely different. According to the relative intensity of the advective and diffusive transport, Eq. (5.65) can be dominated by either hyperbolic or parabolic features. Numerical problems arise when the transport process is dominated by advection. Thus, it seems instructive to evaluate in more detail the role of subsequent terms of Eq. (5.65). To this order we follow the way applied by Szymkiewicz and Mitosek (2007). 

As we found out previously, the partial differential equations of hyperbolic type are related to the problem of wave propagation without any dissipative process. Therefore in the solution of hyperbolic equation no damping is observed. Consequently any discontinuity introduced into the solution by initial or boundary conditions cannot disappear in time as it happens in case of parabolic equation. 

In order to explain the considered process of damping and smoothing of the propagating wave let us begin with the 1D pure advection equation being the simplest example of the hyperbolic equation. The following equation 



where: 

_f_ – scalar quantity (temperature or concentration), 

_U_ – flow velocity 

describes the transport of heat or mass of dissolved substance by flowing stream of fluid. The term _∂f_ / _∂t_ represents accumulation for unsteady process whereas the term _U ∂f_ / _∂x_ represents advection. If _U_ = const., then according to Eq. (5.66) the initial distribution of _f_ will be translated along _x_ axis without any deformation. In Fig. 5.6 an exact solution of the advective transport equation with constant velocity _U_ = 0.5 m/s is shown. The rectangular distribution of _f_ ( _x_ , _t_ ) imposed at the boundary _x_ = 0 is transported towards the downstream end keeping its initial shape. 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

180 



<!-- Start of picture text -->
f<br>x  = 0.0 x  = 500 m x  = 1000 m<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0 600 1200 1800 2400 3000 3600 t  [s]<br><!-- End of picture text -->

**Fig. 5.6** Pure translation of _f_ along _x_ axis 

Sometimes a hyperbolic equation contains a source term, which represents the exchange of transported quantity or describes a chemical process. To show the role of source term let us consider the following equation, similar to Eq. (5.66): 



where _δ_ represents source ( _δ_ > 0) or sink ( _δ_ < 0) term. Let us assume the simplest form of the source term: 



where _κ_ is a decay coefficient. Exact solution of Eq. (5.67) for the set of data accepted previously and with _κ_ = 0.0001 s<sup>−1</sup> is presented in Fig. 5.7. One can notice that in this case the initially rectangular distribution of _f_ is transported along _x_ axis without any smoothing. Its height is systematically reduced in time with intensity determined by the term _δ_ acting as a sink. Of course, this effect can be considered as some kind of damping. However it has a non-dissipative character. 

It is well known that the dissipative processes are irreversible while advection with source term can be inverted. To this order the signs of _U_ and _δ_ should be reversed. Then starting from final distribution of _f_ at the downstream end one can get the boundary condition at the upstream end. 

To obtain the effect of smoothing of the sharp fronts of _f_ , a diffusion term should be introduced into Eq. (5.67). In this way pure advection equation becomes the advection-diffusion equation (5.65): 



5.1 Types of Partial Differential Equations and Their Properties 

181 



<!-- Start of picture text -->
f<br>x = 0.0<br>1 x = 500 m<br>x = 1000 m<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0 600 1200 1800 2400 3000 3600 t  [s]<br><!-- End of picture text -->

**Fig. 5.7** Advective transport with _δ_ = 0.0001 · _f_ 



<!-- Start of picture text -->
f<br>x = 0.0<br>1<br>x = 500 m<br>x = 1000 m<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0 600 1200 1800 2400 3000 3600 t  [s]<br><!-- End of picture text -->

**Fig. 5.8** Solution of advective-diffusive transport with _U_ = 0.5 m/s, _D_ = 0.625 m<sup>2</sup> /s, _δ_ = 0.0001 · _f_ 

Now instead of a hyperbolic equation we have a parabolic one. Consequently while solving the transport of _f_ having a rectangular distribution at _x_ = 0 one obtains simultaneously the following effects: 

- translation with flow velocity _U_ , 

- reduction of the height of rectangle, 

- smoothing. 

It means that the transported rectangular distribution looses its initial steep shape. In Fig. 5.8 the combined effect of advection with flow velocity _U_ = 0.5 m/s, diffusion with _D_ = 0.625 m<sup>2</sup> /s and sink with _δ_ = 0.0001· _f_ s<sup>−1</sup> is presented. 

The solution of Eqs. (5.66), (5.67) and (5.69) presented above, can be interpreted in a more general way, via analysis of the Fourier representation of a general solution 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

182 

of wave equation (5.50) introduced in the preceding section. First, let us list the functions _f_ and _δ_ as well as the derivatives represented in Eq. (5.69). We have: 







Using these relations one obtains the following Fourier components: 

- for pure advection equation (Eq. 5.66) we have _p_ ( _m_ ) = 0 and _q_ ( _m_ ) = _U_ , which gives: 



- for advection equation with source term (Eq. 5.67) we have _p_ ( _m_ ) = _κ_ and _q_ ( _m_ ) = _U_ , which gives: 



- for advection-diffusion equation (5.69) without the source term ( _δ_ = 0) we have _p_ ( _m_ ) = _D m_<sup>2</sup> and _q_ ( _m_ ) = _U_ , which gives: 



- for advection-diffusion equation (5.69) with the source term in the form of Eq. (5.68) we have _p_ ( _m_ ) = _κ_ + _D_ · _m_<sup>2</sup> and _q_ ( _m_ ) = _U_ , which gives: 



It can be seen that all the considered transport equations, i.e. Equations (5.66), (5.67) and (5.69) ensure wave propagation at the same speed regardless of its wavelength _λ_ (or wave number _m_ since _m_ = 2 _π_ / _λ_ ). In each case all components have the same speed, equal to the advective velocity _q_ ( _m_ ) = _U_ , while the damping process depends on the type of equation. 

For the plane wave governed by pure advection equation (Eq. 5.66) its amplitude is not damped. The propagating wave keeps constant amplitude and consequently initial distribution of transported quantity _f_ is not disturbed, as it was 

5.2 Introduction to the Finite Difference Method 

183 

shown in Fig. 5.6. Introduction of a source term into the pure advection equation (Eq. 5.67) changes the behavior of the propagating wave. While traveling, the wave amplitude is decreased in every time decrement _�t_ by exp (− _κ_ · _�t_ ). Although the general solution (Eq. 5.49) contains an infinite number of the components of the Fourier representation, the process of attenuation is the same for all of them, since it is not dependent on the wave number. All amplitudes are decreased in the same way. Consequently, as the initial distribution of _f_ is decreased proportionally with time, it retains the initially imposed general form, as it was presented in Fig. 5.7. 

The solution of the advection-diffusion transport without the source term (Eq. (5.69) with _δ_ = 0) shows that the propagating plane wave is attenuated because of the diffusion. The diffusive term acts with variable intensity, since the damping depends on the wave number _m_ . The wave attenuation is more rapid for short waves than for long ones. Consequently the amplitude of any component of the Fourier representation is attenuated depending on its wavelength. Since a general solution of the propagation wave (Eq. 5.49) contains an infinite number of components, each of them is damped in a different way. The effect of this process is observed as a smoothing of the initial distribution of _f_ , especially significant for steep fronts. If in the considered advection-diffusion equation the source term with a decay coefficient _κ_ is present, its solution contains coupled effect of both diffusive and source terms (Eq. 5.69). The amplitude of propagating wave is decreased by a term partially dependent on the decay coefficient _κ_ and partially on the coefficient of diffusion _D_ multiplied by the wave number _m_ raised to the second power. The combined effect of both processes is seen in Fig. 5.8. 

The effects caused by various terms of the advection-diffusion transport equations (5.65) are worth to remember, since they are helpful in the interpretation the results of its numerical solution. Numerical errors often produce effects similar to the results of physical processes, for example numerical diffusion influences the solution in the same way as physical diffusion. Thus it is important to know what kind of solution should result from the physical transport mechanisms included in the considered equation. 

### **5.2 Introduction to the Finite Difference Method** 

### **_5.2.1 Basic Information_** 

Partial differential equations describing flow and transport in open channels are routinely solved using numerical methods. Analytical solutions have limited applicability for practical problems, which are characterized by irregular and non-uniformly spaced channel cross-sections and variable in time boundary conditions. Thus, analytical solutions are useful mostly as a tool to verify the accuracy of numerical methods, which are then applied to solve real-life problems. 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

184 

Numerical methods allow to solve the mathematical problems in which both the data and the results of calculations are given in the form of numbers. Operating on numbers is their basic feature. The same feature is characteristic of computers. For this reason there exist a very close relation between the progress in numerical methods and in computer technology. This is particularly true in the domain of solution of the partial differential equations. 

It is well known that differential calculus is based on the concept of continuous medium. This idea must be applied to derive these equations. However, the main concept of the numerical methods is a number. Therefore the continuous domain and the partial differential equations must be converted to the form suitable for a treatment by the computational tools, i.e. a PDE or a system of PDEs must be converted into a system of algebraic equations, suitable for numerical solution. 

In general, this process of transformation is carried out in two stages (Fletcher 1991). At first the continuous domain of solution of the considered equation is discretized, i.e. it is converted into a discrete domain constituted by a set of points, separated from each other. The idea of such conversion is presented in Fig. 5.9. 

The continuous time-space domain _C_ , defined as: _xu_ ≤ _x_ ≤ _xd_ and _t0_ ≤ _t_ ≤ _t_ max, is replaced by a set of points called nodes. The nodes can be uniformly spaced with constant intervals _�x_ = const. and _�t_ = const., or they can be located in nonuniform way. The position of any node is defined by its co-ordinates _xj_ and _tn_ , with 1 ≤ _j_ ≤ _M_ , 1 ≤ _n_ ≤ _N_ . The discrete domain _D_ is then constituted by _M_ × _N_ nodes. The numerical methods allow to calculate the approximate values of the solution of the partial differential equations in these nodes only. To this order the second stage of transformation is necessary, i.e. the conversion of the partial differential equation (or system of _K_ equations) into the system of algebraic equations, i.e.: 



<!-- Start of picture text -->
∂f  1 ⎫<br>∂t + · · · = 0<br>... → A ·  X  =  B , (5.79)<br>⎪⎪⎪⎪⎬<br>∂∂f Kt + · · · = 0 ⎪⎪⎪⎪⎭<br>t t<br>C D<br>t max t<br>N<br>tn<br>t t 1<br>x   u x d x x 1  xj   xM x<br><!-- End of picture text -->

**Fig. 5.9** Conversion of continuous domain _C_ into discrete domain _D_ 

5.2 Introduction to the Finite Difference Method 

185 

where: 

**A** – matrix of coefficients of the system of algebraic equations, **X** – vector of unknowns, 

**B** – vector of right hand side. 

This process is called discretization of the partial differential equations. Its details depend on the applied numerical method. Solving the system of algebraic equations one obtains an approximate solution of the partial differential equation or system of equations. 

Sometimes the discretization is made in two steps. At first, a discretization with regard to one of the independent variables, for instance with regard to _x_ , is carried out. In such a way one obtains a system of ordinary differential equations with regard to the second independent variable, which is usually the time _t_ . In the second step this system is integrated numerically using one of the methods presented in Chapter 3. Such an approach is called semi-discretization and will be applied in the following part of the book. Practically the derivatives with regard to time are always discretized by the finite difference technique, whereas the discretization in space is carried out using various possible methods, like finite difference (FD), finite element (FE) or finite volume (FV). 

As far as the spatial discretization of the open channel flow equations is considered, the finite difference method dominates. This is due to one-dimensional character of the majority of open channel flow problems. Note that practically all equations derived in Chapter 1 are one dimensional. However, some specific flow problems require other methods. For example, to model the flow with shock waves as caused by a dam break, the finite volume method is recommended. On the other hand the well-known finite element method seems to be best suited for 2D or 3D flow problems, while it is generally believed to be less useful for 1D problems. Later in this book we will show that a modification of the standard FE method makes it a very efficient tool also for 1D flow and transport equations. In this chapter basic FD and FE algorithms will be introduced. 

### **_5.2.2 Approximation of the Derivatives_** 

The finite difference method is one of the most frequently used method of solution of the partial differential equations. Its concept is to replace directly the derivatives in the equation by approximate formulas in the form of the difference equations. To this end the continuous domain, which in the case of 1D equations has always a rectangular shape, is covered by the mesh of nodes (grid points) as in Fig. 5.10. This grid is build of two families of straight lines. The first family is parallel to the _x_ axis. The distances between the lines equal to _�xj_ , can vary. The second family is parallel to the time axis _t_ . and it is usually distanced with constant time step _�t_ . If the intervals _�x_ are constant as well, then the grid is uniform. 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

186 



<!-- Start of picture text -->
t t Δ x          xj −1 Δ j<br>n +1<br>Δ t<br>n<br>Δ t<br>1<br>x<br>1                      j  −1         j          j  +1                                                                    j = M<br><!-- End of picture text -->

**Fig. 5.10** Grid points covering the domain of solution at the plane _x_ − _t_ 

In the intersection of both families of lines one obtains the nodes, in which the approximate value of solution will be calculated. In a uniform grid the position of any node can be defined by two indices _j_ and _n_ . The first one determines the spatial co-ordinate _xj_ = ( _j_ −1) _�x_ , whereas the second one – the time _tn_ = ( _n_ −1) _�t_ . 

To convert the partial differential equation into a system of algebraic equations appropriate difference formulas approximating the derivatives must be used. In Chapter 3 some of the simplest expressions resulting directly from the Taylor series expansion were derived. These formulas such as forward (Eq. 3.10), backward (Eq. 3.12) or centered differences (Eq. 3.14) approximating the derivative of 1st order can be applied for discretization the considered equation. There are a variety of approximating formulas, which can be used to transform the partial differential equation. They may be derived using a more general approach which is presented here after Fletcher (1991). 

The general form of applied approximation should be selected a priori. Assume that we are looking for a symmetrical approximating formula of 1st order derivative at node _j_ . Its general equation is assumed to be: 



where _a, b, c_ are the coefficients to be determined and _O_ ( _�x_<sup>_m_</sup> ) indicates the accuracy of applied approximation. Since for approximation carried out at the node _j_ the values of function _f_ in neighboring nodes _j_ − 1 and _j_ + 1 are involved, then the formula (5.80) is said to be symmetrical. 

To determine the unknown coefficients in Eq. (5.80) the nodal values of _f_ are expanded in the Taylor series around the node _j_ . For the function _f_ ( _x_ , _t_ ), depending on two independent variables, the Taylor series is given as: 

5.2 Introduction to the Finite Difference Method 

187 



At any time level _n_ , for the nodes _j_ + 1 and _j_ − 1 distanced respectively by _�x_ and − _�x_ from node _j_ , formula (5.81) becomes: 



Using the Taylor series (5.82) we define the values of _fj_ − _1_ and _fj_ +1 (Fig. 5.11). To this end let us consider equally spaced nodes for which _�xj_ − _1_ = _�xj_ = _�x_ . Next we substitute these expressions into Eq. (5.80). Gathering similar terms one obtains: 



Comparison of the left hand side of Eq. (5.80) and the right side hand of Eq. (5.83) yields: 



For any value of the parameter _c_ , the above equations give: 



<!-- Start of picture text -->
f<br>fj<br>Δ x j −1 Δ x j<br>j −1 j j +1 x<br><!-- End of picture text -->

**Fig. 5.11** Sketch for approximation of the derivatives of _f_ ( _x_ , _t_ ) with regard to _x_ 

188 5 Partial Differential Equations of Hyperbolic and Parabolic Type 



If we assume such value of _c_ that cancels the third term of the right side hand of Eq. (5.83), then one obtains an approximating formula as accurate as possible for the assumed form of Eq. (5.80). This case corresponds to: 



Substitution of these relations in Eq. (5.80) yields: 



In such a way the centered difference formula (3.14) is derived. It ensures the accuracy of 2nd order i.e. produces a truncation error of order _O_ ( _�x_<sup>2</sup> ). 

Following a similar way one can derive a symmetrical formula for the derivative of 2nd order. Assume that the approximation will be carried out using the formula analogical to Eq. (5.80), i.e.: 



then its right side hand is given by Eq. (5.83) as well. Comparison of the left hand side of Eq. (5.85) and the right hand side of Eq. (5.83) yields a system of 3 equations with 3 unknown parameters _a_ , _b_ and _c_ : 



Its solution is the following: 



Consequently the approximating formula for the derivative of 2nd order is: 



This well known three-point symmetrical formula approximates the derivative of 2nd order with accuracy of order _O_ ( _�x_<sup>2</sup> ). Usually Eq. (5.86) is derived directly using the Taylor series expansion. 

The main advantages of the presented approach are: the possibility of derivation of symmetrical or asymmetrical formulas, involving various number of nodes depending on the required order of formula and easy application for both uniform 

5.2 Introduction to the Finite Difference Method 

189 

and non-uniform grids. For illustration let us derive three-points asymmetrical formula approximating the derivative of first order. Assume that its general form is the following: 



Substituting _fj_ +1 and _fj_ +2 as the Taylor series expansion around the node _j_ and regrouping, one obtains: 



Comparing the respective sides of Eqs. (5.87) and (5.88) one can find the following conditions: 



which ensure the most accurate approximating formula. These conditions give: 



Finally the searched asymmetric formula is as follows: 



As it can be seen, this formula approximates the first order derivative with accuracy of _O_ ( _�x_<sup>2</sup> ). In such a way one can derive various formulas approximating the derivatives of various order of the function _f_ ( _x_ ). 

The solution of flow or transport equations for natural open channels is usually performed on non-uniform grids. In such a case the appropriate approximating formulas can be easily derived using the same approach. Assume that the first order derivative is approximated in non-equally spaced nodes at the cross section _j_ as presented in Fig. 5.12. 

A general form of the searched formula is given by Eq. (5.80). The nodal values of function _f_ at _j_ − 1 and _j_ + 1 are calculated with Taylor series expansion around the node _j_ . They are following: 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

190 

0 



**Fig. 5.12** Non-uniformly spaced grid points: _�x_ 1̸ = _�x_ 2̸ = _�x_ 3̸= _. . ._ 



Substitution of Eqs. (5.90) and (5.91) in Eq. (5.80) yields after regrouping: 



Comparing the respective sides of Eqs. (5.80) and (5.92) one obtains the following relations: 



Solution of this system of equations gives: 



where χ is the ratio of the neighboring space intervals: 



Then the approximating formula is given by: 



5.2 Introduction to the Finite Difference Method 

191 

The approximating formula for the second order derivative is carried out similarly. We assume a general formula in the form of Eq. (5.85), in which the nodal values of _f_ given by Eqs. (5.90) and (5.91) are substituted: 



Comparing the respective sides of Eqs. (5.85) and (5.96) one obtains the following relations: 



which yields: 



Substitution of Eqs. (5.97a), (5.97b) and (5.97c) in Eq. (5.85) gives: 



It is obvious that any discretization introduces an error. The exceptions are represented by some particular cases when the exact solution has very simple analytical form. For instance the backward or forward difference ensure exact approximation only when the solution is a linear function of _x_ (Fletcher 1991). 

Summarizing the problem of approximation of the derivative of 1st order, let us list the basic formulas discussed previously in Chapter 3 and in current one. We have: 

**–** forward difference 

**–** backward difference 



5 Partial Differential Equations of Hyperbolic and Parabolic Type 

192 

**–** centred difference 



Using the presented formulas for approximation of the derivatives existing in considered equation, one can combine various versions of the finite difference method. These versions are usually called schemes of the finite difference method. However the numerical schemes constructed using the backward, forward and centred differences for the partial differential hyperbolic equations can generate some negative effects in the solution. These issues will be presented in details in the next sections. Now we can say generally that the obtained numerical solution can contain unphysical oscillations or it can be artificially smoothed. These phenomena are caused by the properties of above mentioned approximating formulas. The wiggles are caused by the centered difference approximating the advective term. This phenomenon arises because the approximation of the first derivative at node _j_ is independent of _fj_ (Abbott and Basco 1989). In Fig. 5.13 one can see two different functions _f_ 1( _x_ ) and _f_ 2( _x_ ) having the same value of 1st order derivative approximated by the centered difference. 

On the other hand, approximation of the first derivative by the backward difference eliminates the wiggles, but at the same time it gives rise to intensive artificial smoothing. To limit both effects it is sometimes necessary to include the nodal value of the unknown function to approximate its first derivative at the same node. Such formula, which covers simultaneously Eqs. (5.99), (5.100) and (5.101) can be simply derived using the previously applied approach. 

The assumed formula for the first derivative (5.80) compared with the result of the Taylor series expansion (5.83) allows us to write the following conditions: 



<!-- Start of picture text -->
f ( x )<br>f    1 ( x )<br>f    2( x )<br>x j –1 x j x j + 1 x<br><!-- End of picture text -->

**Fig. 5.13** Approximation of the 1st order derivative of _f_ ( _x_ ) using the centred difference does not involve _f_ ( _xj_ ) 

5.2 Introduction to the Finite Difference Method 

193 



The coefficients _b_ and _c_ can be expressed in relation to _a_ as follows: 







Substitution of these relations in Eq. (5.80) yields: 



Setting _a_ · _�x_ = − _η_ one obtains: 



This formula involves the weighting parameter _η_ . According to its value, Eq. (5.104) describes all the standard approximations of the 1st derivative given by Eqs. (5.99), (5.100) and (5.101). For _η_ = 0 it gives the forward difference, for _η_ = 0.5 – the centred difference, whereas for _η_ =1 − the backward difference. However the most interesting property of Eq. (5.104) is that, if necessary, it enables a gradual increase of the weight of _fj_ in the approximation of the derivative. 

An in-depth discussion of various aspects of the finite difference method is given by Fletcher (1991). His main suggestions and recommendations, very useful for computational practice, can be summarized as follows: 

1. For a smooth function the truncation error of the Taylor series expansion is dominated by the first term of its truncated part and consequently it determines the accuracy of approximation. This is valid for all approximating formulas. 

2. The accuracy of approximation of the derivatives increases with the order of approximating formula. 

3. The error of approximation depends on the value of mesh dimension _�x_ . It can be expected that this error is more efficiently reduced by decreasing _�x_ than by increasing the order of approximating formula. Therefore, while increasing the order of approximation, grid refinement should be applied simultaneously. 

4. A negative aspect of increasing of the order of approximation is that more nodal values of the function _f_ ( _x_ ) are involved in approximating formulas. Moreover, increasing of formula’s order only very slowly improves the results of computations for sparse mesh. 

5. Increasing of the approximating formula order does not guarantee better accuracy approximation for rapidly varied function, especially when discontinuities 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

194 

occur. This is because in such a case the truncation error of the Taylor series is not dominated by the first term of the neglected part of the series. 

As far as the approximation of the derivative of the first order is considered, Fletcher (1991) concludes that the approximation which should be applied in practice is the one of 2nd order, whereas approximations of higher order should be used in exceptional circumstances only. 

Another very important problem concerns the representation of waves on the numerical grid. This has particular meaning in open channel flow modeling as the considered flow processes have the character of wave motion. Discrete character of grid points gives rise to limited possibility of wave representation. It appears that the shortest waves which can be represented on the mesh spaced with _�x_ have the length equal to double space interval. Then the numerical solution of the partial differential equation at a grid point should be considered as a long-wave representation of its exact solution. As it was shown by Fletcher (1991), all difference formulas better approximate the derivatives in the case of long waves than short ones. This suggests the following conclusion: to improve the results of computations dealing with the wave propagation problems, grid refinement should be applied. Such approach, allowing to take into account the shorter and shorter waves, ought to be used in the case when large gradients are expected in the solution. Comprehensive discussion of this question is presented by Abbott and Basco (1989), Fletcher (1991) and others. We will take up these questions in Chapter 6, while discussing the properties of the applied numerical methods. However at the moment one can find out that except the prismatic channels the grid refinement rather cannot be applied. This is because the data on channel geometry at the grid points are obtained from field measurements. 

### **_5.2.3 Example of Solution: Advection Equation_** 

Using the finite difference method let us solve the pure advection equation (5.3), the simplest example of hyperbolic equation: 



where: 

_f_ – scalar function, _U_ – flow velocity. 

Assume that _U_ = const. > 0 and the solution is searched in the domain: 0 ≤ _x_ ≤ _L_ and _t_ ≥ _0_ , where _L_ is the length of the channel reach, in which flowing water transports the dissolved pollutant. For positive advection velocity, the following initial-boundary conditions are imposed: 

- initial condition: _f_ ( _x_ , _t_ = 0) = _fi_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ 

- boundary condition: _f_ ( _x_ = 0, _t_ ) = _f_ 0( _t_ ) for _t_ ≥ 0 

5.2 Introduction to the Finite Difference Method 

195 



<!-- Start of picture text -->
t Δ x<br>n +1<br>Δ t<br>n<br>j – 1                                            j<br>x<br><!-- End of picture text -->

**Fig. 5.14** Grid points for the upwind scheme 

where _fi_ ( _x_ ) and _f_ 0( _t_ ) are given functions, satisfying the condition of consistency: _fi_ (0) = _f_ 0(0). 

To solve Eq. (5.105) let us apply the difference scheme known as the upwind scheme. This scheme uses the grid points shown in Fig. 5.14. 

The derivatives are approximated at the node ( _j_ , _n_ ) as follows: 



where: 

_j_ – index of cross-section, 

_n_ – index of time level, 

_�x_ – spatial mesh dimension, 

- _�t_ – time step, 

Substitution of Eq. (5.106) in advection equation (5.105) yields: 



where _M_ is the total number of cross-sections. Note that _f_ 1<sup>_n_+1</sup> is known from the boundary condition. Therefore in each equation of the system (5.107) only one unknown _fj_<sup>_n_+1</sup> exists. It can be easily calculated, giving: 



5 Partial Differential Equations of Hyperbolic and Parabolic Type 

196 

where _Ca_ denotes so called advective Courant number, defined as follows: 



Setting in Eq. (5.108) _j_ = 2, 3, _. . ._ , _M_ one can compute the nodal values of the function _f_ in all nodes at the time level _tn_ +1. Note that the computations can be run in any order – not only from the upstream end towards the downstream end. It is impossible to reverse the order of calculations. The numerical schemes, which do not require respecting the imposed order of calculations of _f_ at the new time level, are called explicit schemes. If calculations must be carried out in the required order at the new time level, it is said that an implicit scheme is applied. 

The upwind scheme is extremely simple, but it is rather seldom used to solve practical problems. This classical and very instructive finite difference scheme usually serves to explain some questions of numerical solution of the hyperbolic equations. To examine how the upwind scheme works, let us solve the pure advection equation (5.105) for arbitrary assumed data. 

_Example 5.1_ In a prismatic channel of length _L_ the water flows with constant velocity _U_ . Assume that: 

- _U_ = 0.5 m/s = const., 

- _�x_ = 100 m = const., 

- initial condition is _f_ ( _x_ , _t_ = 0) = 0 for 0 ≤ _x_ ≤ _L_ ; 

- boundary condition is 



with _Fm_ = 100 and _Tm_ = 1,200 s. 

Therefore we will examine advective transport of a scalar quantity represented by the function _f_ , which has the initial distribution in the form of triangle having height of _Fm_ = 100 and a base equal to 2 _Tm_ . 

Taking into account the analytical solution of the advection equation in the form of expression (5.12), one can predict the form of the exact solution in the case considered here. The triangular distribution forced at the upstream end will travel along channel axis with any shape deformation. Then in each cross-section it must be the same, shifted in time only. For our analysis we take the cross-section located in position distanced 5,000 m from the upstream end. 

The results of computations are shown in Fig. 5.15. One can see that the upwind scheme gives exact solution for the Courant number equal to unity ( _Ca_ = 1) only. 

5.3 Introduction to the Finite Element Method 

197 



<!-- Start of picture text -->
f / fm<br>1.2<br>x = 0 x = 5000 m<br>Ca   = 1.0<br>0.8<br>Ca   = 0.75<br>Ca   = 0.50<br>0.4<br>t  [s]<br>0<br>0 3600 7200 10800 14400 18000<br><!-- End of picture text -->

**Fig. 5.15** Solution of the pure advection equation using the upwind scheme for various Courant number 

For other values it produces results completely different from the exact one. One observe the attenuation of triangular distribution, which increases as the Courant number decreases. On the other hand, for _Ca_ > 1 very intensive instabilities in the solution occur (Fig. 5.16). 

The results of numerical experiments carried out for various set of _�x_ and _�t_ indicate that the accuracy of solution is determined by the assumed values of the numerical parameters. The exact solution is obtained only for a particular set of data, for which the advective Courant number is equal to unity. For other sets one obtains either oscillating solutions or damped solutions. Since the only physical process represented in the solved equation is advection, these observed effects must have numerical roots. A more detailed explanation of such behavior is the subject of Section 5.4. 

### **5.3 Introduction to the Finite Element Method** 

### **_5.3.1 General Concept of the Finite Element Method_** 

The finite element method is one of the most popular approaches for solving the partial differentia equations. Its advantages are especially appreciable in application to 2D and 3D problems. On the other hand, it is seldom applied for 1D problems, as in this case it does not seem to possess significant benefits compared with the finite difference method, while being more complicated in implementation. However, using the finite element method one can develop very effective algorithms for solution 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

198 



<!-- Start of picture text -->
f / fm<br>x = 5000m<br>1.2<br>x = 0<br>Ca   = 1.035<br>0.8<br>0.4<br>exact solution<br>0<br>t  [s]<br>–0.4<br>0 3600 7200 10800 14400 18000<br><!-- End of picture text -->

**Fig. 5.16** Solution of the pure advection equation using the upwind scheme for _Ca_ = 1.035 

the open channel flow problems as well. For this reason our presentation of this method will be limited to 1D case. Comprehensive presentations of the finite element method oriented to solve the fluid mechanics problems are given by Gresho and Sani (1998), Fletcher (1991), Oden and Reddy (1976), Zienkiewicz (1972) among others. 

Similarly to the finite difference method, the goal of application of the finite element method is to find an approximate solution of a partial differential equation (or a system of such equations), which must be satisfied by unknown function in the solution domain. As in the finite difference method, in FE method the approximate solution is searched in a set of isolated nodes, which constitute discrete domain covering the continuous physical domain. However, the manner of transformation of the solved differential equation into the system of algebraic equations is quite different. The finite element method belongs to the family of the so-called weighted residual methods. To explain briefly the concept of this approach, let us consider the problem of solution of the partial differential equation written in a symbolic form: 



with the auxiliary conditions imposed at the limits of the solution domain _C_ 



which must be satisfied by the unknown function _f_ ( _x_ , _t_ ). The weighted residual methods assume the following general form of the approximate solution of Eq. (5.110): 

5.3 Introduction to the Finite Element Method 

199 



where: 

_fa_ ( _x_ , _t_ ) – approximation of exact solution _f_ ( _x_ , _t_ ), _αj_ ( _t_ ) – coefficients, which are to be determined, _Nj_ ( _x_ ) – assumed approximating functions. 

For an arbitrary approximation Eq. (5.110) will not be satisfied. Substitution of this approximate solution in Eq. (5.110) yields: 



where _R_ is the equation’s residual. We should try to choose such values of the coefficients _αj_ ( _t_ ) that _R_ is minimized over the solution domain, i.e the best approximation of _f_ is ensured. To find these values the following condition is applied: 



which means that the integral of the weighted residual must be equal to zero. Assuming a set of the weight functions _wj_ one obtains a system of ordinary differential equations for unsteady problem or a system of algebraic equations for steady problem. There are a couple possibilities to choose the weight functions, which lead to various numerical schemes. If we assume that the approximating functions applied in Eq. (5.112) are used, i.e. as the weight functions: 



then the Galerkin method is obtained. For _j_ tending to infinity, the approximated solution _fa_ ( _x_ , _t_ ) should tend to the exact one _f_ ( _x_ , _t_ ) (Fletcher 1991). 

Remember that in 1D unsteady flow process the unknown function _f_ depends on two independent variables: the spatial co-ordinate _x_ and the time _t_ . In such a case the partial differential equation (5.110) is at first approximated in space only using the finite element method. This leads to a system of the ordinary differential equation with regard to time _t_ . Next, the obtained system must be integrated over time. To this end one can use the finite element method as well. However such approach does not give any advantages. It is better to use standard methods of numerical solution of the initial-value problem for the ordinary differential equations, which were presented in Chapter 3. Application of one of these methods leads to the system of algebraic equations, which can be linear or non-linear depending on the solved differential equation. The obtained system is completed by introducing the imposed 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

200 

boundary conditions and after that it is solved usually using direct methods. Let us remember that approximation of 1D partial differential equation leads to the system with banded tridiagonal matrix. For the system of equations the bandwidth is larger. 

In the finite element method the continuous domain is divided into smaller subareas called the finite elements. It is assumed that these elements are joined in a finite number of points lying on the element’s circumference. These points are the nodes, in which the approximate solution will be computed. Since in open channel hydraulics we have 1D equations, then the domain of solution has the form of channel reach of length _L_ so that we have 0 ≤ _x_ ≤ _L_ . Consequently, in this case the applied finite elements can take the form of linear segments only. 

The unknown function _f_ in the solution domain is approximated as follows: 



where: 

_fa_ – approximation of the function _f_ in _C_ , 

**N** ( _x_ ) = ( _N_ 1, _. . ._ , _Nj_ , _Nj_ +1, _. . . NM_ ) – matrix of basis or shape functions, 

**f** ( _t_ ) = ( _f_ 1, _. . ._ , _fj_ , _fj_ +1, _. . ._ , _fM_ )<sup>_T_</sup> – vector of the nodal values of function _f_ , which for time dependent problems has the components being functions of time, _T_ – transposition symbol, 

_M_ – total number of nodes. 

The row matrix **N** has components dependent on space co-ordinates only. They should be chosen in such a way that Eq. (5.116) is satisfied at the nodes. This means that substitution of the node co-ordinates in Eq. (5.116) ensures that the approximation _fa_ must be equal to the nodal value of _f_ . In other words, for _x_ = _xj_ is _fa_ = _fj_ . The set of functions _Nj_ ( _x_ ) is called basis or shape functions (Fletcher 1991, Zienkiewicz 1972). 

Equation (5.114) determining the best approximation of _f_ , in such a case will take the following form: 



Since the considered channel reach was divided with _M_ nodes into _M_ − 1 finite elements of length _�xj_ , Eq. (5.117) can be rewritten as follows: 



The main question, which arises while solving any equation with the finite element method, is the choice of elements and the trial functions. As we found out 

5.3 Introduction to the Finite Element Method 

201 



**Fig. 5.17** Linear finite elements containing 2 nodes ( **a** ) and 3 nodes ( **b** ) 

previously, the shape of elements depends on the dimensionality of solved problem. For open channel flow equation this choice is restricted to segments of straight line. The number of nodes which constitute a segment, depends on the degree of polynomial applied for approximation. For our purposes we will consider the simplest element as shown in Fig. 5.17a, which allows us to apply the linear shape functions only. 

The chosen shape functions must be continuous over an element and they have to ensure that _fa_ is continuous between elements. 

Let us consider a channel reach of length _L_ , which is divided into the subintervals-elements bounded by nodes _j_ and _j_ + 1. Their lengths are _�xj_ = _xj_ +1− _xj_ (Fig. 5.17a). In such element the function _f_ can be approximated using a linear polynomial: 



The coefficients _a_ and _b_ can be determined by the solution of the following system of equations: 





which gives: 





Substitution of Eq. (5.121) in Eq. (5.119) yields: 



This equation can be rewritten as follows: 



202 5 Partial Differential Equations of Hyperbolic and Parabolic Type 

where: 





Therefore for an element containing two nodes the appropriate shape functions have the form of linear Lagrange polynomials. Very similar expression to Eq. (5.123) is derived for the preceding element _j_ − 1. In the approximaring formula for this element the trial functions _Nj_ −1( _x_ ) and _Nj_ ( _x_ ) will occur. Consequently, the function _Nj_ ( _x_ ) contributes to the elements containing the node _j_ only, i.e. it is nonzero in the elements _j_ − 1 and _j_ . In others elements this function is equal to zero. Then _Nj_ ( _x_ ) is defined as follows: 











The function _Nj_ ( _x_ ) shown in Fig. 5.18 has typical form, because of which it is called hat function. 

Differentiation of the shape functions with regard to _x_ in element _j_ gives: 





**Fig. 5.18** The form of linear trial function _Nj_ ( _x_ ) 

5.3 Introduction to the Finite Element Method 

203 



Then the derivative of the approximating function _fa_ ( _x_ ) given by Eq. (5.123) is: 



While solving unsteady flow equations the time derivative of unknown function occurs as well. This derivative in element _j_ is given as: 



Integration of the shape functions over element _j_ is carried out as follows: 



whereas for integration of a product of shape functions the following formula can be used (Zienkiewicz 1972): 



where _α_ and _β_ are the exponents of powers of the shape functions. 

### **_5.3.2 Example of Solution: Diffusion Equation_** 

Let us consider the diffusion equation with _D_ = const.: 



This equation will be solved for the following auxiliary conditions: 

**–** initial condition: 

_f (x_ , _t_ = 0 _)_ = _fi (x)_ for 0 ≤ _x_ ≤ _L(L_ is length of considered channel reach _)_ 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

204 

0 



**Fig. 5.19** Assumed discrete solution domain for the diffusion equation 

**–** boundary conditions: 



The functions _fi_ ( _x_ ), _f_ 0( _t_ ) and _fL_ ( _t_ ) are given. 

To solve Eq. (5.131) the Galerkin finite element method is applied. Assume that considered segment of a channel is divided with _M_ nodes into _M_ − 1 elements of length _�xj_ ( _j_ = 1,2, _. . ._ , _M_ − 1). The discretized solution domain is shown in Fig. 5.19. 

According to the Galerkin procedure the numerical solution must satisfy the condition (5.118). For Eq. (5.131) this condition takes the following form: 



where **N** ( _x_ ) is the vector of shape functions having components given by Eq. (5.125). In Eq. (5.132) the subscript _a_ denotes the approximation of function according to formula (5.123). 

Let us calculate one integral-component of the above sum, corresponding to the element _j_ . Since in this element only two components of the vector **N** (x), i.e. _Nj_ ( _x_ ) and _Nj_ +1( _x_ ), are non-zero then in Eq. (5.132) only two following non-zero products will occur: 



Calculation of the integral (5.133) carried out term by term provides consecutively: 

- The time variation term 

5.3 Introduction to the Finite Element Method 

205 



##### **–** The diffusive term 

Calculation of this term is slightly more complicated. This is because linear polynomials were applied for approximation, whereas in this term the derivative of 2nd order occurs, which cannot be calculated directly. To solve this problem, at first one can carry out an integration by parts decreasing the order of derivative. This is performed as follows: 



Finally, the integral (5.133) equal to _I_ 1<sup>_(j)_−</sup><sup>_I_</sup> 2<sup>_(j)_, is given as:</sup> 



Calculation of the integral (5.134) is performed similarly. For its consecutive terms one obtains: 





Finally, the integral (5.134) equal to _I_ 1<sup>_(j_+1</sup><sup>_)_</sup> − _I_ 2<sup>_(j_+1</sup><sup>_)_</sup> , is given as: 



5 Partial Differential Equations of Hyperbolic and Parabolic Type 

206 

The equations similar to (5.137) and (5.140) are obtained for all elements ( _j_ = 1, 2, _. . ._ , _M_ − 1). According to Eq. (5.132) they should be assembled leading to the following global system of ordinary differential equations: 

**–** for _j_ = 1 



**–** for _j_ = 2, 3, _. . ._ , _M_ −1 



**–** for _j_ = _M_ 



Equation (5.141) can be rewritten in matrix notation as: 



where: 



Both matrices **A** and **B** have dimensions of (2 _M_ ) × (2 _M_ ). 

The initial-value problem for the system (5.142) can be solved using the previously presented implicit trapezoidal method (3.22), yielding the following system of algebraic equations: 

( **A** + 0.5 _�t_ · **B** ) **f** _n_ +1 = ( **A** − 0.5 _�t_ · **B** ) **f** _n_ − 0.5 _�t_ · **F** _n_ +1 − 0.5 _�t_ · **F** _n_ , (5.143) where: 

5.3 Introduction to the Finite Element Method 

207 

_n_ – index of time level, 

_�t_ – time step. 

In such a way the Crank–Nicolson finite element method is obtained. After introducing the required boundary conditions this system of linear algebraic equations is solved with double sweep method giving approximate values of _f_ at next time level. Assume that we consider the solution domain divided into 6 elements. In this case the matrices **A** and **B** have the following structure: 



<!-- Start of picture text -->
Δ x 1 Δ x 1 0 0 0 0 0<br>3 6<br>Δ x 1 Δ x 1 + Δ x 2 Δ x 2 0 0 0 0<br>6 3 3 6<br>0 Δ x 2 Δ x 2 + Δ x 3 0 0 0<br>6 3 6<br>Δx3<br>3<br>A = 0 0 Δ x 3 Δ x 3 + Δ x 4 0 0<br>6 3 6<br>Δ x 4<br>3<br>0 0 0 Δ x 4 Δ x 4 + Δ x 5 0<br>6 3 6<br>Δ x 5<br>3<br>0 0 0 0 Δ x 5 Δ x 5 + Δ x 6<br>6 3 6<br>Δ x 6<br>3<br>0 0 0 0 0 Δ x 6 Δ x 6<br>6 3<br>Δ D x 1 − Δ D x 1 0 0 0 0 0<br>− Δ D x 1 Δ D x 1 + Δ Dx 2 − Δ Dx 2 0 0 0 0<br>0 − Δ Dx 2 Δ Dx 2 + Δ Dx 3 − Δ Dx 3 0 0 0<br>B = 0 0 − Δ Dx 3 Δ Dx 3 + Δ Dx 4 − Δ Dx 4 0 0<br>0 0 0 − Δ Dx 4 Δ Dx 4 + Δ Dx 5 − Δ Dx 5 0<br>0 0 0 0 − Δ Dx 5 Δ Dx 5 + Δ Dx 6 − Δ Dx 6<br>0 0 0 0 0 − Δ Dx 6 Δ Dx 6<br><!-- End of picture text -->

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

208 

Vector **F** represents the fluxes of the transported quantity through the boundary. This vector can have only one nonzero component. This takes place when a Neumann boundary condition _D_ · _∂f_ / _∂x_ is imposed at _x_ = 0 or at _x_ = _L_ . Otherwise its all elements disappear. 

It is interesting to compare the semi-discrete forms of the FE and FD methods. For any internal node for uniform grid points ( _�x_ = const.), the finite element method gives: 



whereas spatial discretization of the diffusion equation by the finite difference method leads to the following formula: 



One can see that in this case the only difference between the methods deals with the approximation of the time derivative at node _j_ . In the finite element method it is considered as a weighted averaged taken from three nodes: _j_ − 1, _j_ and _j_ + 1. Consequently this method requires to solve the system of equations with tri-diagonal matrix for both explicit and implicit schemes. 

_Example 5.2_ Solve the diffusion equation using the Crank–Nicolson finite element method for the following auxiliary conditions: 

- initial condition: _f_ ( _x_ , 0) = 0 for 0 ≤ _x_ ≤ _L_ . 

- boundary conditions: _f_ (0, _t_ ) = 1.0 and _f_ ( _L_ , _t_ ) = 0.0 for _t_ > 0 

Note, that in this case the values of _f_ 1<sup>_n_+1</sup> and _fM_<sup>_n_+1</sup> known as imposed boundary conditions must be introduced into the system (5.143). 

The results of calculations carried out for _L_ = 4 m, _�x_ = 0.1, _D_ = 0.01 m<sup>2</sup> /s are shown in Fig. 5.20. It appears that they are very similar for different values of time step. This fact suggests that conversely to the advection equation solved in Example 5.1 by the finite difference upwind scheme, this time the value of the applied time step is not restricted. 

**Fig. 5.20** Solutions of the diffusion equation obtained for _t_ = 50 s 



<!-- Start of picture text -->
f<br>1.0<br>0.5<br>0.0<br>0.0 0.5 1.0 1.5 2.0 2.5 x  [m]<br><!-- End of picture text -->

5.4 Properties of the Numerical Methods for Partial Differential Equations 

209 

The Crank–Nicolson scheme in both version i.e. with the finite difference and element methods is known as very effective and reliable tool for solving the diffusion equation. A detailed examination of its numerical properties will be given later. 

### **5.4 Properties of the Numerical Methods for Partial Differential Equations** 

### **_5.4.1 Convergence_** 

Each numerical method of solution of the partial differential equations is useful on condition that it is convergent. The theory of truncation error says that refinement of the grid provides more accurate numerical solution. Generalizing, one can expect that approximate solution tends to the exact one, while the mesh dimensions _�t_ and _�x_ are systematically reduced. More formally, one can say that solution of the system of algebraic equations, which approximates the considered partial differential equation is convergent, if it tends to the exact solution of the differential equation for any value of the independent variable, when the mesh dimensions tend to zero (Abbott and Basco 1989, Fletcher 1991). Then it is required that: 



where 

_fj_<sup>_n_</sup> – approximate value of the function _f_ at the node ( _j_ , _n_ ), _f_ ( _xj_ , _tn_ ) – exact value of the function _f_ at the same node ( _xj_ , _tn_ ). 

If this requirement is satisfied, the method is said to be convergent. This statement, while obvious, is usually difficult to be proved theoretically. 

The difference between the exact solution of the partial differential equation and the exact solution of the system of algebraic equations, called the solution error, is given as: 



where _e_<sup>_n_</sup> _j_<sup>isthesolutionerroratthenode(</sup><sup>_j_,</sup><sup>_n_).Itshouldberememberedthatthe</sup> exact solution of the system of algebraic equation is still only the approximate solution of the differential equation. We assume that in the solution of the algebraic equations no errors caused by the iteration process as well as by the round-off errors during the computation are present. 

The value of solution error _Ej_<sup>_n_at the node (</sup><sup>_j_,</sup><sup>_n_) depends on approximation accu-</sup> racy of the differential equation, i.e. on the values of mesh dimensions _�x_ and _�t_ , as well as on the values of higher order derivatives neglected in the numerical 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

210 

approximation. These issues can be illustrated on the examples of the pure advection equation and the pure diffusion equation, which have exact solutions. 

In Section 5.2.3 we considered the numerical solution of advection equation (5.105) using the up-wind scheme given by formula (5.108). The results of this application are shown in Figs. 5.15 and 5.16. Now we will continue the numerical experiments with this scheme using the same data as assumed previously in Example 5.1. Let us remember that this equation has an exact solution. Starting with _�x_ = 100 m and _�t_ = 100 s, which ensures _Ca_ = 0.5, the grid is refined in such a way that constant value of the Courant number _Ca_ is kept. The results of calculation carried out for systematically reduced values of _�x_ and _�t_ are presented in Fig. 5.21. 

Comparing the consecutive solutions with the exact one, we see that the numerical solution approaches the analytical one as the mesh dimensions are reduced. This means that the up-wind scheme provides the solutions which converge to the exact one. 

In this case we managed to demonstrate the convergence of the applied numerical scheme directly via numerical tests, since the exact solution of solved equation is known. Unfortunately, in practical cases the exact solutions of equations are unknown. For this reason for some classes of solved problems the convergence may be proved indirectly. To this end the Lax Equivalence Theorem is applied, which reads as follows: “Given a properly posed initial-value problem and a finite difference approximation to it that satisfies the consistency condition, stability is necessary and sufficient condition for convergence” (Abbott and Basco (1983) after Rychtmyer and Morton (1967)). Therefore, if the considered numerical method satisfies both consistency and stability conditions at the same time it satisfies the convergence condition. The advantage of this approach is obvious, since it is relatively easy to verify the consistency and stability. 



<!-- Start of picture text -->
f/fm<br>x=0 x = 5000 m<br>1.0 Δx=5 m<br> exact<br>solution Δx=12,5 m<br>0.8<br>Δx=25 m<br>0.6 Δx=50 m<br>Δx=100 m<br>0.4<br>0.2<br>t[s]<br>0.0<br>0 3600 7200 10800 14400 18000<br><!-- End of picture text -->

**Fig. 5.21** Effect of mesh shrinking for pure advection equation solved by the up-wind difference scheme 

5.4 Properties of the Numerical Methods for Partial Differential Equations 

211 

### **_5.4.2 Consistency_** 

The system of algebraic equations obtained as an approximation of the partial differentia equation is said to be consistent with this equation if in the limit, when the mesh dimensions tend to zero, it becomes the governing partial differential equation at every node of the grid. This condition is examined by replacing the nodal values of functions by their Taylor series expansion around the considered node. One can say that this is a process inverse to discretization. The equation obtained in such a way is not exactly the same as the original equation, since it contains additional terms. The condition of consistency requires that these extra terms tend to zero as the grid is refined. 

Let us verify the consistency condition for the up-wind scheme for advection equation described in the preceding section (Eq. 5.107): 



All nodal values of _f_ should be replaced by the Taylor series expansion round the node ( _j_ , _n_ ) (see Fig. 5.14): 



The consecutive nodal values present in Eq. (5.147) are following: 



Substitution of Eqs. (5.149) and (5.150) in Eq. (5.147) yields: 



The right hand side of Eq. (5.151) is equal: 



In Eqs. (5.151) and (5.152) the indices are omitted, but we have to remember that it is valid for the node ( _j_ , _n_ ). The extra term _R_ ( _f_ ) results from the truncation error and it depends on the applied method of solution. We expect that _R_ ( _f_ ) will disappear for mesh dimensions tending to zero.Indeed, one can notice that for _�x_ →0 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

212 

and _�t_ →0 _R_ ( _f_ ) →0 and consequently Eq. (5.151) becomes the original advection equation (5.105). The same approach can be used to prove the consistency of any other numerical scheme. 

### **_5.4.3 Stability_** 

As it was fund out previously, a convergent numerical method of solution of the partial differential equation must be not only consistent but stable as well. Stability is a property of a numerical method that ensures damping of any random disturbance which can occur during the computational process. Such disturbance can arise from auxiliary conditions or round-off errors. Typical symptoms of instability are unphysical oscillations occurring in the numerical solution. Let us come back to the results of solution of the pure advection equation using the upwind scheme, which were presented in Figs. 5.15 and 5.16. One can see that as long as the advective Courant number is not greater than unity, the obtained solutions are smooth although they are sometimes inaccurate (Fig. 5.15). However, if the Courant number slightly exceeds unity, the solution is immediately affected by strong oscillations (Fig. 5.16). These oscillations cause that the solution looses its physical sense. The amplitudes of oscillations increase with time and with increasing distance from bounds. It should be mentioned that there are another kinds of oscillations, which can be precluded by stable numerical methods as well. Such oscillations should be distinguished from those generated by instability. In next section this question will be taken up. 

The numerical method is considered stable if insignificant variation of input data causes similarly insignificant variation of the final results. Conversely, if the numerical method is not capable to damp such errors, then these errors can increase in an unlimited way and finally they can dominate the solution. Such method is called unstable one. When an unstable method is applied to solve the open channel unsteady flow equations, then usually the computation fails. This is because the oscillating depth takes the negative values, for which the solved equations are not valid. 

All numerical methods can be divided into the following ones: absolutely stable, conditionally stable and unstable. For obvious reasons the unstable methods are not interesting. To conclude on the stability of applied scheme, an analysis of its stability must be done. This analysis provides the detailed information of particular conditions, which must be satisfied to ensure a stable solution. As it was shown previously, while discussing the solutions of pure advection and pure diffusion equations, a stable solution required certain relations between the mesh dimensions _�x_ and _�t_ , and the physical parameters, being the coefficients of solved equation. The stability analysis can be carried out using the matrix method. The details of this approach are given for instance by Fletcher (1991). However the most commonly applied method of stability analysis is the Neumann approach (Potter 1973, Fletcher 1991, Abbott and Basco 1983). This method is applied below. 

5.4 Properties of the Numerical Methods for Partial Differential Equations 

213 

The numerical methods applied for solving the partial differential equation provides the solution, which approximates the exact one. Then there is a difference between them: 



where: 

_E j_<sup>_n_</sup> – solution error at the node ( _j_ , _n_ ), _f_ ( _xj_ , _tn_ ) – exact solution at the node ( _j_ , _n_ ), _f_<sup>_n_</sup> _j_<sup>– approximate solution at the node (</sup><sup>_j_,</sup><sup>_n_).</sup> 

Such error is introduced at every grid point ( _j_ , _n_ ) for _j_ = 1,2,3, _. . ._ , _M_ and for _n_ = 0,1,2, _. . ._ . 

Let us consider the box scheme applied previously to solve the advection equation (5.105). Since _f_<sup>_n_</sup> _j_<sup>=</sup><sup>_f_(</sup><sup>_xj_,</sup><sup>_tn_) −</sup><sup>_E n_</sup> _j_<sup>thensubstitutionofthisexpressioninEq.</sup> (5.108) yields: 



Since the exact solution _f_ ( _x_ , _t_ ) must satisfy the algebraic equation of the scheme (5.108): 



then Eq. (5.154) is reduced to the following form: 



The same equation can be written for _j_ = 2,3, _. . ._ , _M_ and for _n_ = 0,1,2, _. . ._ . Note, that the system (5.156) has identical structure as the one provided by the up-wind scheme, i.e. as Eq. (5.108). This system is completed by the appropriate initial and boundary conditions. It is assumed that _Ej_<sup>0= 0 for</sup><sup>_j_= 2, 3,</sup><sup>_. . ._,</sup><sup>_M_and</sup><sup>_E_</sup> 1<sup>_n_= 0for</sup> _n_ = 0, 1, 2, _. . ._ , since the exact initial and boundary conditions do not generate any error. 

In the Neumann method the errors at the nodes at considered time level _n_ are expanded in a finite complex Fourier series. The conclusions on stability or instability are deduced by examining how a single component of series behaves while passing from time level _n_ to time level _n_ + 1. 

Using the Fourier series, the error _E j_<sup>_n_</sup> at the node _xj_ can be expressed as follows (Abbott and Basco 1989): 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

214 



##### where: 

_j_ = 2,3, _. . ._ , _M_ , – index of node, _i_ = (−1)<sup>1/2</sup> – imaginary unit, _n_ – index of time level, 

_k_ – index of Fourier component, 

_m_ – wave number, _�x_ – space interval, _A_<sup>_n_</sup> _k_<sup>– Fourier coefficient (amplitude of component</sup><sup>_k_th at the time level</sup><sup>_n_),</sup> _K_ – index of given finite value. 

The wave number is given as: 



where _λ_ is the wave length. Let us multiply both sides of Eq. (5.158) by the space interval _�x_ : 



and let us introduce a new variable _N_ : 



which represents the number of grid intervals over one wavelength. Then Eq. (5.158) can be rearranged to the form: 



where _ϕ_ = _m_ · _�x_ is dimensionless wave number. As the shortest waves represented at the considered grid points have wavelength 2 _�x_ , whereas the longest ones tend to infinity, then 2 ≤ _N_ ≤∞ implies that 0 ≤ _ϕ_ ≤ _π_ . 

For the linear problems as considered here, it is sufficient to examine the behavior of one Fourier component. Therefore, instead of Eq. (5.157), one can consider only one component of the sum corresponding, for example, to _k_ = 1. For simplicity this index will be omitted. Taking into account Eq. (5.158) the chosen component can be written as: 



Note that the time is included in the amplitude _A_<sup>_n_</sup> . 

5.4 Properties of the Numerical Methods for Partial Differential Equations 

215 

Equation (5.161) can be substituted into Eq. (5.156) yielding: 



Dividing both sides by the factor _e_<sup>_i_·</sup><sup>_ϕ_·</sup><sup>_j_</sup> one obtains: 



where 



_G_ is interpreted as the amplification factor of the amplitude of _k_ th component of Fourier representation of the error function, while passing from the time level _n_ to _n_ + 1. The error amplitude will not increase if the modulus of _G_ is not greater than unity: 



Using the Euler relation _e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_</sup> = cos _ϕ_ − _i_ · sin _ϕ_ , Eq. (5.164) is reformed to the following form: 



Since the amplification factor _G_ is a complex number, therefore the condition (5.165) yields: 



This relation can be reduced to the following one: 



Since _ϕ_ ranges from 0 to _π_ , then inequality (5.168) can be verified for its extreme values only. Note that for _ϕ_ = 0 this relation is satisfied for any value of _Ca_ , whereas setting _ϕ_ = _π_ one obtains: 



As the Courant number is always positive, then relation (5.169) will be true for: 



The final conclusion is then following: to avoid amplification of the Fourier wave amplitude while solving the advection equation using the up-wind scheme, 

5 Partial Differential Equations of Hyperbolic and Parabolic Type 

216 

the Courant number cannot exceed unity. This condition implies the following restriction with regard to the applied time step: 



As long as the value of time step _�t_ does not exceed this limit, we can be sure that the solution of the advection equation provided by the upwind scheme is still numerically stable. Since the stability requires satisfying the condition (5.171), then the up-wind scheme is conditionally stable. This property explains the oscillating results of computation provided by _Ca_ = 1.035 and shown in Fig. 5.16. 

Equation (5.170) is known as Courant-Friedrichs-Levy (CFL) condition (Potter 1973). It is valid for all hyperbolic partial differential equations solved by explicit schemes. The Courant number can be interpreted as relation between the propagation celerity in analytical solution (in this case it is the advection velocity _U_ ) and the celerity of propagation in the numerical solution _�x_ / _�t_ (Abbott and Basco 1983). 

Summarizing the above presented considerations, we can state that upwind scheme applied for the advection equation is only conditionally stable – the mesh dimensions must satisfy appropriate relations. Since from the preceding section this scheme is known to be consistent as well, then it is convergent if only the stability conditions is respected while computations. Then, using the Lax Equivalence Theorem we confirmed the convergence of the up-wind scheme. Note that the same was deduced from the numerical experiments. 

As far as the numerical solution of the diffusion equation by the Crank-Nicolson finite element method (5.141) is considered, for uniform elements we have the following formula for any internal node: 



This equation is rewritten in the form: 



where _Cd_ , sometimes called the diffusive Courant number, is given by: 



References 

217 

Using Eq. (5.161) one obtains the following formula for Fourier component representing the error function: 



Dividing both sides of Eq. (5.175) by _A_<sup>_n_</sup> · _e_<sup>_i_·</sup><sup>_ϕ_·</sup><sup>_j_</sup> yields: 



Since � _e_<sup>_i_·</sup><sup>_ϕ_</sup> + _e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_�</sup> _/_ 2 = cos _ϕ_ then 



The stability condition (5.165) requires: 



This relation must be satisfied for the extreme values of the dimensionless wave number _ϕ_ , i.e. for _ϕ_ = 0 and _ϕ_ = _π_ i.e. for cos _ϕ_ = 1 and for cos _ϕ_ = −1. Substituting consecutively these values one can find out that relation (5.178) is satisfied for any value of _Cd_ . Therefore the Crank–Nicolson finite element method applied for solving the diffusion equation is absolutely stable. This explains the results of solution obtained in Example 5.2. 

### **References** 

- Abbott MB, Basco DR (1989) Computational fluid dynamics. Longman Scientific and Technical, New York 

Billingham J, King AC (2000) Wave motion. Cambridge University Press, Cambridge 

Fletcher CAJ (1991) Computational techniques for fluid dynamics, vol. I. Springer-Verlag, Berlin Gresho PM, Sani RL (1998) Incompressible flow and the finite-element method, Advection- 

diffusion, vol. 1. Wiley, Chichester, England 

Hervouet JM (2007) Free surface flow – modeling with the finite element method. Wiley, England Oden JT, Reddy JN (1976) An introduction to the mathematical theory of finite elements. Wiley, New York 

Potter D (1973) Computational physics. Wiley, London 

Rychtmyer RD, Morton KW (1967) Difference methods for initial-value problems. Interscience, 

New York 

- Szymkiewicz R, Mitosek M (2007) Numerical aspects of improvement of the unsteady pipe flow equations. Int. J. Numer. Methods Fluids 55:1039–1058 

Weiyan T (1992) Shallow water hydrodynamics. Elsevier, Amsterdam Zienkiewicz OC (1972) The finite element method in engineering science. McGraw-Hill, London 

## **Chapter 6 Numerical Solution of the Advection Equation** 

### **6.1 Solution by the Finite Difference Method** 

### **_6.1.1 Approximation with the Finite Difference Box Scheme_** 

In order to show the specific problems related to the numerical solution of partial differential hyperbolic equations, let us solve the pure advection equation (5.3): 



where: 

_f_ – scalar function, 

_U_ – flow velocity assumed to be constant. 

To solve this equations one can use a number of finite difference schemes. We begin with applying the implicit four point scheme commonly called the box scheme. This scheme has interesting history (see Abbott and Basco 1989), is well known and frequently used in open channel flow modeling. It is very flexible and particularly suitable for illustrating all the most important aspects of the numerical solution of hyperbolic equations. 

The scheme uses grid points shown in Fig. 6.1. The derivatives are approximated inside the mesh, at point _P_ . To this end the following formulas are used: 



where: 

_j_ – index of cross-section, 

_n_ – index of time level, 

> R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_6, 

> ⃝C Springer Science+Business Media B.V. 2010 

219 

6 Numerical Solution of the Advection Equation 

220 

_�x_ – spatial mesh dimension, 

_�t_ – time step, _ψ_ – weighting parameter which ranges ⟨0, 1⟩, _θ_ – weighting parameter which ranges ⟨0, 1⟩, 

Originally, in the box scheme the meaning of parameter _ψ_ is opposite, since it denotes the distance from the cross-section _j_ − 1 to point P (Fig. 6.1) (Abbott and Basco 1989, Cunge et al. 1980). We change this convention to be compatible with the notation used in the lumped flood routing models presented in Chapter 9, in which the box scheme occurs in implicit way. 

Substitution of Eqs. (6.2) and (6.3) in advection equation (6.1) yields: 



where _M_ is the total number of cross-sections in the considered channel reach. Note, that with the assumption _U_ > 0 the value _f_ 1<sup>_n_+1</sup> is known from the boundary condition proscribed at the upstream end. Therefore in each equation of the system (6.4) only one unknown _fj_<sup>_n_+1</sup> exists. It can be easily isolated, giving: 



<!-- Start of picture text -->
fj n +1 =  α ·  fj n −1 +  β ·  f j  n +  γ ·  f j  n − + 1 1 (6.5)<br>Δ x<br>t (1−ψ)Δ x ψΔ x<br>n + 1<br>(1− θ )Δ t<br>P<br>Δ t<br>θΔ t<br>n<br>j −1                                            j<br>x<br><!-- End of picture text -->

**Fig. 6.1** Grid points for the box scheme 

6.1 Solution by the Finite Difference Method 

221 

where: 







The advective Courant number _Ca_ was defined in preceding chapter (Eq. 5.109) as follows: 



Setting in Eq. (6.5) _j_ = 2, 3, _. . ._ , _M_ one can compute the nodal values of the function _f_ in all nodes at the time level _tn_ +1. Note that the computations must run in a strictly defined order – from the upstream end towards the downstream end and it is impossible to reverse the order of calculations. Such scheme is said to be implicit. 

The box scheme involves two weighting parameters _ψ_ and _θ_ , which can take any value form the interval ⟨0, 1⟩. Moreover the mesh dimensions _�x_ and _�t_ are mutually related via the Courant number (6.7). One can suppose that the values of all mentioned parameters will determine the accuracy of the numerical solution produced by the box scheme. To examine this influence let us solve advection equation (6.1) for an arbitrary set of data. 

_Example 6.1_ In a prismatic channel of length _L_ the water flows with constant velocity _U_ . Assume that: 





where _Fm_ is peak value and _Tm_ is time to peak. Therefore we will examine advective transport of a scalar quantity represented by the function _f_ , which has initial distribution in the form of a triangle with the height equal to _Fm_ and the base equal to 2 _Tm_ . 

Knowing the analytical solution of the advection equation (see Section 5.1.2) we expect that the triangular distribution imposed at the upstream end will travel along the channel axis without any shape deformation. Then in each cross-section it will be shifted in time only. 

6 Numerical Solution of the Advection Equation 

222 



<!-- Start of picture text -->
f / Fm.<br>1.2<br>x = 0 x = 5000 m<br>Ca   = 0.5 Ca   = 1.0<br>0.8<br>Ca   = 2.0<br>0.4<br>0<br>t  [s]<br>0.4<br>0                    3600                  7200                10800               14400                18000<br><!-- End of picture text -->

**Fig. 6.2** Solution of advection equation using the box scheme for various values of the Courant number with _ψ_ = 0.5 and _θ_ = 0.5 

The following data are assumed: _U_ = 0.5 m/s = const., _�x_ = 100 m = const., _Fm_ = 100 and _Tm_ = 1,200 s. As a control we take the cross-section distanced 5,000 m from the upstream end. Let us begin with assuming _ψ_ = 0 and _θ_ = 0. For these values of the weighting parameters one obtains _α_ = _Ca_ , _β_ = 1− _Ca_ and _γ_ = 0, and consequently Eq. (6.5) turns into Eq. (5.108). This version of the box scheme coincides with the upwind scheme previously discussed in Section 5.2.3. The results of computations are shown in Figs. 5.15 and 5.16. 

The results of numerical experiments carried out for other sets of the parameters _ψ_ , _θ_ and _Ca_ are shown in Figs. 6.2, 6.3 and 6.4. One can see that the exact solution is given only for specific combinations of the parameters, as for instance _ψ_ = 0.5, _θ_ = 0.5 and _Ca_ = 1. For other sets one obtains either oscillating or damped solutions. 

Since the only physical process represented in the solved equation is advection then observed effects in its solution must have the numerical roots. In order to explain such behavior of the box scheme let us analyze its numerical properties. 

### **_6.1.2 Stability Analysis of the Box Scheme_** 

It is known from Section 5.4 that the local solution error satisfies the equation of the applied numerical scheme. Therefore, according to Eqs. (6.5) and (5.153) one can write: 



6.1 Solution by the Finite Difference Method 

223 



<!-- Start of picture text -->
f / F m.<br>1.2<br>x = 0 x = 5000 m<br>ψ = 0.5 Ca   =1.0<br>0.8<br>ψ = 0.25<br>0.4<br>ψ = 0.0<br>0<br>t  [s]<br>–0.4<br>0 3600 7200 10800 14400 18000<br><!-- End of picture text -->

**Fig. 6.3** Solution of advection equation using the box scheme for various values of _ψ_ with _θ_ = 0 and _Ca_ = 0.5 



<!-- Start of picture text -->
f / F m.<br>1.2<br>x = 0 x = 5000 m<br>0.8 exact θ = 0.5<br>solution<br>0.4 θ = 1<br>θ = 0.475<br>0<br>t  [s]<br>−0.4<br>0 3600 7200 10800 14400 18000<br><!-- End of picture text -->

**Fig. 6.4** Solution of advection equation using the box scheme for various values of _θ_ with _ψ_ = 0.5 and _Ca_ = 0.5 

6 Numerical Solution of the Advection Equation 

224 

With Fourier representation of the solution error (5.161), Eq. (6.8) takes the following form: 



Dividing both sides by _e_<sup>_i_·</sup><sup>_ϕ_·</sup><sup>_j_</sup> one obtains: 



where _G_ is the amplification factor. The error amplitude should not increase, so it is required that | _G_ | ≤ 1. 

Using the Euler relation _e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_</sup> = cos _ϕ_ − _i_ · sin _ϕ_ (McQuarrie 2003), Eq. (6.10) is reformed to the following form: 



Arithmetic operations on complex numbers allow us to rewrite this equation as: 



The amplification factor _G_ is a complex number, therefore the stability condition | _G_ | ≤ 1 yields the following relation: 





Since _ϕ_ ranges from 0 to _π_ , then inequality (6.13) can be verify for its extreme values only. Setting _ϕ_ = _π_ one obtains: 



This inequality is equivalent to the following relation: 



Substitution of the parameters _α_ , _β_ and _γ_ defined by Eqs. (6.6a), (6.6b) and (6.6c) in Eq. (6.15) yields the following relation: 



225 

6.2 Amplitude and Phase Errors 

which is equivalent to the following two inequalities: 





These relations will be satisfied for: 





Both conditions ensure that the denominators in Eqs. (6.17a) and (6.17b) are always different from zero. Since the inequalities (6.17a) and (6.17b) are satisfied for any value of the Courant number, then the conditions (6.18a) and (6.18b) ensure unconditional stability of the box scheme. 

Note that for _ψ_ = 0 and _θ_ = 0 Eq. (6.5) becomes the upwind scheme, with very different numerical properties. Its stability was analyzed in Section 5.3. 

### **6.2 Amplitude and Phase Errors** 

The numerical results presented in preceding section constitute a good starting point for the discussion of the numerical aspects of solution of the hyperbolic equations. The open channel flow equations, being of hyperbolic type like the advection equation, do not contain any mechanism of dissipation. The solution of such equation has the form of wave, with a specific amplitude and celerity. It is important that the applied numerical scheme changes neither the wave amplitude nor its phase celerity. This means that the numerical methods should not introduce into solution any artificial dissipation or dispersion. The numerical method which generates artificial dissipation is called a dissipative method, whereas the method which produces artificial dispersion is called a dispersive one. In the first case the wave amplitude is attenuated giving rise to unphysical smoothing, whereas in the second case the wave celerity is affected giving rise to the unphysical oscillations of the results. Due to numerical dispersion and dissipation the solution of hyperbolic equations is much more difficult and challenging than the solution of the elliptic equations. The same is true for parabolic equations containing significant advective term, like the advection-diffusion transport equation widely applied to model the motion of scalar quantity in open channels, where the turbulent flow of large Reynolds numbers usually takes place. Both phenomena, having purely numerical roots, can be examined by an appropriate numerical analysis. As an example, let us perform such analysis for the considered numerical solution of the pure advection equation using the difference box scheme. 

226 

6 Numerical Solution of the Advection Equation 

The dissipative and dispersive properties of any numerical scheme are expressed by the amplitude and phase errors. Both errors can by estimated using the amplitude factor _G_ and its modulus. To this end two coefficients of convergence _R_ 1 and _R_ 2 are defined. The coefficient _R_ 1 is expressed by the ratio of the amplification factors for numerical solution and for exact one. For first time these coefficients were introduces by Leendertse (see Abbott and Basco 1989, Cunge et al. 1980, Liggett and Cunge 1975). Since for the exact solution this factor is equal to unity, then the coefficient _R_ 1 is represented by the modulus of the amplification factor | _G_ |. As we will see further, both coefficients of convergence are functions of the Courant number _Ca_ and the variable _N_ , being the number of space interval _�x_ per wavelength of _k_ th Fourier component of the solution. 

Let us begin with an analysis of the dissipative properties of the box scheme. Substitution of Eq. (5.160) in Eq. (6.13) yields the following formula 



Equation (6.19) expresses the modulus of the amplification factor as a function of the parameter _N_ , representing the relation between the wave length _λ_ and the space interval _�x_ (see Eqs. (5.158), (5.159) and (5.160)). 

Plotting this function for selected values of the Courant number and the weighting parameters, one can show the relation between the wave length and intensity of the wave amplitude attenuation. The plots in Figs. 6.5 and 6.6 show that for _Ca_ = 1, _ψ_ = 0.5 and _θ_ = 0.5 the box scheme is dissipation free since | _G_ | = 1 for any 



<!-- Start of picture text -->
G<br>3.00<br>2.50<br>2.00<br>Θ = 0.0<br>1.50 Θ = 0.25<br>Θ = 0.50<br>1.00<br>Θ = 0.75<br>0.50<br>Θ = 0.100<br>0.00<br>0 2 4 6 8 10 12 N<br><!-- End of picture text -->

**Fig. 6.5** Modulus of the amplification factor (6.19) versus the parameter _N_ for advection equation solved by the box with _ψ_ = 0.5 and _Ca_ = 2.0 

6.2 Amplitude and Phase Errors 

227 



<!-- Start of picture text -->
G<br>2.25<br>2.00<br>Ψ = 1.00<br>1.75<br>1.50 Ψ = 0.75<br>1.25 Ψ = 0.50<br>1.00<br>Ψ = 0.00<br>0.75<br>Ψ = 0.25<br>0.50<br>0.25<br>0 2 4 6 8 10 12 N<br><!-- End of picture text -->

**Fig. 6.6** Modulus of the amplification factor (6.19) versus the parameter _N_ for the advection equation solved by the box scheme with _θ_ = 0.5 and _Ca_ = 2.0 

length of the wave. Consequently the wave amplitude is neither damped nor amplified. On the other hand _θ_ ≥ 0.5 and ψ ≤ 0.5 give | _G_ | > 1, which means that the scheme increases the wave amplitude in time. Finally this process leads to numerical instability. This fact could be expected on the basis of the stability analysis carried out previously – compare Eqs. (6.18a) and (6.18b). For other values of the parameters the box scheme becomes dissipative. One can notice that the most intense damping is for short waves (small values of _N_ ) and large Courant numbers. Damping is reduced for increasing wavelength. 

In a similar way can be analyzed the dissipative properties of the up-wind scheme. With _ψ_ = 0 and _θ_ = 0 from Eqs. (6.6a), (6.6b) and (6.6c) results that _α_ = _Ca_ , _β_ = 1 − _Ca_ and _γ_ = 0. Substituting these values in Eq. (6.19) and taking into account Eq. (5.160) one obtains the following formula 



The dissipative behavior of the up-wind scheme is summarized graphically in Fig. 6.7. 

This figure confirms the numerical stability conditions shown previously. As long as the Courant number does not exceed unity, the up-wind scheme damps the wave amplitude ensuring stable solution, since the modulus of its amplification factor does not exceed unity as well. At the same time we can observe (as previously) that short waves are more intensively damped than long ones. For _Ca_ = 1 one obtains | _G_ | = 1, which means that the wave amplitude is neither damped nor amplified. However, for greater values of _Ca_ the scheme becomes unstable, as in this case the value of modulus of the amplification factor exceeds unity. Moreover, Fig. 6.7 

6 Numerical Solution of the Advection Equation 

228 



<!-- Start of picture text -->
G<br>Ca  = 1.25<br>1.25 Ca  = 1.035<br>Ca  = 1.00<br>1.00<br>Ca  = 0.75<br>0.75<br>Ca  = 0.50<br>0.50<br>N<br>0 2 4 6 8 10 12<br><!-- End of picture text -->

**Fig. 6.7** Modulus of the amplification factor versus the parameter _N_ for the advection equation solved by the up-wind scheme 

shows that indeed, as it was mentioned previously, the waves represented on the grid cannot be shorter than 2 _�x_ . Relation (6.20) is valid for _N_ ≥ 2 only. 

The second type of error is the phase error. This one can be represented using the amplitude factor _G_ as well. Since it is a complex number: 



then the phase celerity of _k_ th components of the Fourier series is defined by the angle _φ_ as: 



For the box scheme (Eq. 6.12) one obtains: 



A similar expression can be derived for the exact solution of the pure advection equation. To this end let us write this solution in the following form: 



Substituting Eq. (6.24) in Eq. (6.1) yields: 



6.2 Amplitude and Phase Errors 

229 

This expression can be simplified to: 



Equation (6.26) has the following solution: 



Now this result can be substituted in the solution (6.24): 



For the neighboring time levels _tn_ and _tn_ +1 = _tn_ + _�t_ we obtain respectively: 





Dividing the respective sides of these equations yields: 



Let us compare this equation with Eq. (5.163). Equation (6.31) can be considered as the definition of the amplification factor for exact solution of the pure advection equation. Since _e_<sup>−</sup><sup>_ϕ_·</sup><sup>_i_</sup> = cos ( _ϕ_ ) − _i_ · sin( _ϕ_ ), then the factor takes the following form: 



The corresponding angle _ø_<sup>exact</sup> defining the exact phase celerity of wave is given by the following relation: 



Then one can write: 



Now let us consider again Eq. (6.23) representing the phase celerity of the wave described by the advection equation solved by the box scheme. The numerical scheme is dispersion free, if for any Fourier component _k_ the angle _ø_ is constant. Conversely, if the component’s phase celerity varies, the scheme is dispersive. Note that for the box scheme constant phase celerity is ensured by _ψ_ = 0.5, _θ_ = 0.5 

6 Numerical Solution of the Advection Equation 

230 

and _Ca_ = 1. In such a case one obtains: _α_ = 1, _β_ = 0 and _γ_ = 0. Consequently Eq. (6.23) becomes: 



which means that _ø_ = − _ϕ_ = − _m_ · _�x_ . Therefore, for the mentioned values of the weighting parameters and for the Courant number equal to unity the box scheme is not dispersive. At the same time Eq. (6.35) coincides with Eq. (6.33) for the exact solution of the advection equation. 

Obviously, in real-life cases the computations are performed with _Ca_ ̸ = 1. This means that the dispersion error occurs always. It is interesting to know how the applied scheme changes the phase celerity comparing with the exact solution. Dispersive properties of any scheme are expressed by the coefficient _R_ 2 defined as the ratio of the numerical phase celerity to the exact celerity: 



Substitution of Eqs. (6.23) and (6.34) in Eq. (6.36) yields: 



where _α_ , _β_ and _γ_ are given by Eqs. (6.6a), (6.6b) and (6.6c). 

The coefficient _R_ 2 given by Eq. (6.37) and calculated for _ψ_ = 0.5 and _θ_ = 0.5 is shown in Fig. 6.8 as a function of the wavelength (expressed by _N_ i.e. the number of 



<!-- Start of picture text -->
R 2<br>2.00<br>1.75<br>Ca  = 0.50<br>1.50<br>Ca  = 0.75<br>1.25 Ca  = 1.00<br>1.00<br>0.75 Ca  = 1.50<br>Ca  = 2.00<br>0.50<br>0.25<br>0 2 4 6 8 10 12 14 16 18 20 22 24 N<br><!-- End of picture text -->

**Fig. 6.8** Phase portraits for the box scheme with _ψ_ = 0.5 and _θ_ = 0.5 

6.3 Accuracy Analysis Using the Modified Equation Approach 

231 

space intervals _�x_ per wavelength) for various values of the Courant number. Note that the assumed values of the weighting parameters ensure that the box scheme is dissipation free. Figures 6.5 and 6.6 show that in this case the modulus of the amplification factor is constant and equal to unity. 

In Fig. 6.8 we observe that _R_ 2 decreases with increasing wavelength. The value of this coefficient, being significant for short waves, tends to unity for long waves. It means that the phase celerity of the long waves is less affected by the numerical approximation than the celerity of the short waves. The only case when the wave celerity is not affected corresponds to _Ca_ = 1. Note that the Courant numbers greater than 1 cause that the numerical phase celerity is less than the celerity in the exact solution ( _R_ 2 < 1). For _Ca_ < 1 the situation is opposite. The numerical phase celerity dominates over the one corresponding to the exact solution ( _R_ 2 > 1). This fact can be related to the solution of the advection equation using the box scheme presented in Fig. 6.2. For _Ca_ >1 which corresponds to _R2_ <1, the oscillations occur behind the steep front of _f_ , whereas for _Ca_ <1, or _R2_ >1, the oscillations occur before the front of wave. Let us remember that the shortest waves possible to represent at the numerical grid are equal to 2 _�x_ . For this reason the coefficient _R_ 2 cannot be resolved for _N_ < 2. 

The information on the dissipative and dispersive properties of the numerical schemes provided by the amplification factor _G_ and coefficient _R_ 2 is helpful in the interpretation of the results of computations. However, comparing the graphs as those presented in Figs. 6.7 and 6.8 provides only general (qualitative) information on the properties of the numerical schemes, but it does not allow a quantitative evaluation. 

### **6.3 Accuracy Analysis Using the Modified Equation Approach** 

Since numerical methods are the main tool of solution of partial differential equations, the solution of any open channel flow problem having practical meaning will have approximate character. Therefore the question of great importance is to estimate the accuracy of the obtained solution. Usually, as it was shown in the preceding sections, the only available information on the accuracy concerns the order of approximation of the derivatives. One can say that our knowledge on applied numerical scheme as the order of approximation, its consistency and the stability condition is necessary but insufficient to explain and to predict its behavior. The examples of solution of the pure advection equation using the box scheme, presented in Section 5.2.3, confirm this conclusion. 

The same is true for the coefficients of convergence, which characterize the amplitude and phase error. They explain rather general tendencies of the applied numerical method. As these coefficients are related to the wave lengths, information resulting from such an analysis cannot be used directly to assess the numerical errors generated while solving the differential equations (Fletcher 1991). However, there is a tool which can provide more information on the numerical properties of the applied method of solution and which can help us to better understand the obtained results. It is called the modified equation approach. For the first time the 

6 Numerical Solution of the Advection Equation 

232 

term “modified equation approach” was used in Section 5.4.2 in context of the consistency of numerical method. The method was proposed by Warming and Hyett (1974). Afterwards it was applied by many authors, e.g. Abbott and Basco (1989), Fletcher (1991). Such analysis provides large amount of information and additionally can suggests the way of increasing the solution accuracy. This method is very useful since it gives possibility to separate the numerical and physical effects in the obtained solution. It is particularly well suited for examining numerical dissipation and dispersion. Consequently this approach allows us to interpret correctly the results of computation. Moreover, in the case of hyperbolic equations the modified equation method allows us to draw practically full information on the applied numerical method, including sometimes the stability conditions as well. 

The numerical dissipation and dispersion can be clearly showed while considering the numerical solution of the pure advection equation using the box difference scheme presented in Section 6.1. To this order let us come back to the Section 5.2 and let us take up again the accuracy of approximation of the derivatives. 

The transformation of the partial differential equation into the system of algebraic equations is based on the Taylor series expansion (Korn and Korn 1968): 



While approximating the derivative, the appropriate formulas are obtained owing to truncation of the Taylor series. This process introduces truncation error. For instance, the forward difference (Eq. 5.99): 



is obtained from Eq. (6.38) in which the terms up to the one containing the first derivative only were taken into account: 



In this equation _R_ denotes the truncation terror: 



The exact value of the derivative resulting from (6.40) is: 



As we know from Section 5.4.2, the term _R_ ( _�x_ ) informs us how the error caused by truncation varies with respect to the value of _�x_ . In this case we have: 

6.3 Accuracy Analysis Using the Modified Equation Approach 

233 



which means that the error caused by approximation of the 1st derivative using formula (6.39) vary linearly with the variation of _�x_ . 

Usually the truncation error is related to the order of approximating formula. The latter is determined by the highest order of derivative accounted in the approximating formula. For instance, formula (6.39) approximates the 1st order derivative of _f_ ( _x_ ) with accuracy of 1st order, since in the Taylor series (6.40) only the terms up to first order were taken. Unfortunately, as it was stated previously, the order of the method is a general information only and it says nothing about the nature of the error and its consequences for the solution. However, it appears that the truncation error determines the numerical properties of numerical scheme. To explain this fact, let us remember that for smooth functions the error provided by truncation of the Taylor series is determined by the value of the first term of the truncated part of series. 

As an example consider the following function: 



The 1st derivative of _f_ ( _x_ ) at point _x_ = 1 is equal to 2.7183. If we calculate its approximated value using the formula (6.39) assuming _�x_ = 0.1, then we will obtain: 



Therefore the approximation error is: _δ_ = 2.8588 − 2.7183 = 0.1405. This difference represents the value of the total truncated part of the Taylor series, i.e. it is simply _R_ ( _�x_ ). Now we can calculate the value of the first term of the truncated part for previously assumed _x_ = 1 and _�x_ = 0.1. We obtain: 



One can see that indeed for smooth functions the value of the truncated part of the Taylor series is dominated by the value of its first term. In the considered case the first term is equal to 0.1359, while a sum of other terms is equal to 0.0046 only. 

Fletcher (1991) shows convincingly that the kind of error dominating in the numerical solution depends on the order of derivative in the first term of the truncated part of the Taylor series expansion. He considered the propagation of a plane wave, which simultaneously is subjected to dissipation and dispersion. This wave is described by Eq. (5.50): 



6 Numerical Solution of the Advection Equation 

234 

where: 

_Am_ – amplitude of the _m_ th component, 

_m_ – wave-number related to the components’ wave length _λ_ by formula _m_ = 2 _π_ / _λ_ , 

_p_ ( _m_ ) – dissipation parameter, which determines how rapidly the amplitude of the wave is attenuated, 

_q_ ( _m_ ) – wave propagation speed, 

_i_ – imaginary unit. 

Assume that this wave is governed by the linear advection-diffusion equation: 



We showed previously, in Section 5.1.6, that for this equation Eq. (6.45) has the following parameters: 





then it becomes Eq. (5.77): 



We also found out earlier that Eq. (6.48) describes the wave, which propagates with constant celerity with simultaneously attenuated amplitude. 

Now, assume that the wave (6.45) is governed by the linear Kortweg-de Vries equation (Billingham and King 2000, Whitham 1979): 



where _E_ is the coefficient of dispersion. For his equation we obtain the following: 





and consequently we have: 



In this case the attenuation does not exist. However the wave propagates with celerity depending on the coefficient of dispersion and on the wavelength. If there 

235 

6.3 Accuracy Analysis Using the Modified Equation Approach 

are waves of different length, they move at different speeds, which simply means that dispersion occurs. The advective velocity _U_ is affected more intensive for short wave (large value of _m_ ) than for long ones depending on the sign of _E_ . 

Fletcher (1991) proposes to assume the following rule: the even order derivatives are associated with dissipation process, whereas the odd order derivatives are associated with dispersion process. This assumption has important meaning for the modified equation approach, since it can be related with the truncation error. 

Now we can go back to the solution of advection equation using the difference box scheme given by Eq. (6.4). Following the consistency analysis described in Section 5.4.2, one can see that at each grid point ( _j_ , _n_ ) the box scheme modifies the advection equation to the following form: 



where: 



To facilitate further analysis, all the time derivatives, except that of the 1st order, are eliminated from Eq. (6.53). To this order the advection equation is differentiated: 









Substitution of Eq. (6.54) in Eqs. (6.53) and (6.52) yields: 



236 

6 Numerical Solution of the Advection Equation 

where: 





Equation (6.55) is called modified equation (Fletcher 1991), whereas the coefficients (6.56) and (6.57) are called coefficients of numerical diffusion and numerical dispersion, respectively. For the considered PDE the form of the modified equation depends on the numerical method applied to solve it. Generally one can say that _R_ ( _f_ ) contains all terms of the Taylor series neglected while approximation the derivatives in the solved equation. 

The modified equation allows us to conclude on the properties of the applied scheme. For instance, in Section 5.4.2 such equation was used to prove consistency of the upwind scheme. This equation allows us to deduce other properties as well. 

As far as the order of approximation by the box scheme is considered, from Eqs. (6.56) and (6.57) result that it depends on the values of weighting parameters. For _ψ_ = 0.5 and _θ_ = 0.5 it represents accuracy of 2nd order with regard to both variables _x_ and _t_ . In this case the coefficient of numerical diffusion is cancelled as the space and time derivatives are approximated with the centered difference (see Fig. 6.1). For other values of _θ_ and _ψ_ the scheme is an approximation of 1st order. 

The box scheme will be stable, if the coefficient of numerical diffusion is nonnegative _(Dn_ ⩾ 0 _)_ , since only in such a case the problem of solution of Eq. (6.55) will be well-posed. For _Dn_ < 0, this problem is ill–posed and the solution of Eq. (6.55) does not exist. The condition _Dn_ ≥ 0 will be always satisfied for _θ_ ≥ 0.5 and _ψ_ ≤ 0.5, irrespectively of the value of the Courant number. This means that the box scheme is absolutely stable. For other values of the weighting parameters the scheme is conditionally stable or even unstable. 

The modified equation (6.55) allows us to examine the dissipative and dispersive properties of the box scheme as well. In the modified equation, similarly to Eqs. (6.46) and (6.49), the terms with odd derivatives are associated with the numerical dispersion and the terms with even derivatives are associated with the numerical dissipation. Since for smooth functions the truncation error is determined by the first term of truncated part of the Taylor series, then the first term at the right hand side of Eq. (6.55) will determine the error dominating in the solution. If this term contains an odd derivative, the scheme will be dispersive, whereas if it contains an even derivative – the scheme will be dissipative. Numerical diffusion is associated with the derivative of the lowest even order. Consequently, according to the dominating term in the truncation error, we will obtain either smooth or oscillating solution. These effects have numerical nature and they are unrelated to the physical processes represented in the solved equation. They are particularly distinct when strong gradients of function _f_ occurs in the solution. 

6.3 Accuracy Analysis Using the Modified Equation Approach 

237 

If the applied method is dissipation free, oscillations will occur in the solution. They cannot be explained by the numerical instabilities as they can appear for numerically stable schemes as well. To eliminate them some numerical diffusion should be introduced. If it is sufficiently large, the oscillations are suppressed. At the same time the gradients of function _f_ are reduced – the steep front is smoothed. However in the case of discontinuity of _f_ , the truncation error is not dominated by the first term of the truncated part of the Taylor series, but rather by the next term. Consequently, the oscillations can occur even if the applied scheme is slightly dissipative. The problem of generation of the numerical diffusion is independent of the spatial dimensionality. For 2D and 3D problems tensors of numerical diffusion and dispersion appear at the place of scalar coefficients. 

Using the modified equation (6.55) provided by the box scheme, one can carry out a full analysis and interpretation of the computational results displayed in Figs. 5.15, 5.16, 6.2, 6.3 and 6.4. 

Let us begin with the solution obtained for _θ_ = 0 and _ψ_ = 0, i.e. using the well known upwind scheme. For these values of the weighting parameters one obtains: 





The upwind scheme ensures accuracy of order _O_ ( _�t_ , _�x_ ). Since in this case the term containing the derivative of 2nd order dominates in the truncation error, then in the numerical solution a dissipation error must occur. Consequently the modified equation (6.55) can be rewritten as: 



It means that solving the pure advection equation with upwind scheme, we are actually solving the advection-diffusion equation. The exact solution is provided only for _Ca_ = 1. In this case, as results from Eq. (6.58a), one obtains _Dn_ = 0. This means that the modified equation (6.59) becomes the original Eq. (6.1). Assuming _Ca_ < 1, we have _Dn_ > 0, which triggers numerical diffusion, giving rise to attenuation of the initially imposed distribution of _f_ along the channel axis. This attenuation increases as the Courant number decreases, which can be observed in Fig. 5.15. In such a situation the numerical dispersion of the scheme is not significant, since the right hand side of Eq. (6.55) is dominated by its first term. It is worth to add that for _Ca_ > 1 Eq. (6.59) cannot be solved, as for _Dn_ < 0 the problem of its solution is ill-posed. Confirmation of this conclusion is given in Fig. 5.16, where for _Ca_ = 1.035 numerical instability occurred. 

Now let us consider the case illustrated in Fig. 6.2. These results were provided by _θ_ = 0,5 and _ψ_ = 0,5. For these values, the coefficients of numerical diffusion and dispersion in the modified equation (6.55) are given by: 

6 Numerical Solution of the Advection Equation 

238 





Then this equation takes the following form: 



In such a way the Kortweg-de Vries equation (6.49) is obtained. Equation (6.61) will provide the exact solution only for _Ca_ = 1, for which _En_ = 0. For other values of the Courant number the error of numerical dispersion is generated and the scheme provides oscillating solution. The position of oscillations (before or behind the peak) varies and it depends on the sign of _En_ , i.e. on the assumed value of the Courant number (Fig. 6.2). They will be present always. 

Influence of the weighting parameter _ψ_ is shown in Fig. 6.3. In this case _θ_ = 0.5 and _Ca_ = 0.5 are assumed. For these values the modified equation contains: 



Setting _ψ_ = 0.5 the numerical diffusion is eliminated. In such a case the right hand side of the modified equation is dominated by the dispersive term, since _En_ ̸ = 0. Consequently, an oscillating solution is produced (Fig. 6.3). For _ψ_ < 0.5 the box scheme provides the numerical diffusion. Therefore solution obtained with _ψ_ = 0.25 and _ψ_ = 0.0 is damped and similar to the one provided by the advectiondiffusion equation. On the other hand, for _ψ_ > 0.5 an unstable solution is generated, since _Dn_ < 0. 

The last example of calculation deals with _ψ_ = 0.5 and _Ca_ = 0.5. For these values Eqs. (6.56) and (6.57) give: 





In this version of the box scheme the numerical diffusion is cancelled by setting _θ_ = 0.5. However we obtain _En_ < 0 which means that the scheme is dispersive. Consequently one can observe oscillations behind the peak (Fig. 6.4). Assuming _θ_ > 0.5 we introduce numerical diffusion, which is the most intense for _θ_ = 1. The obtained solution differs appreciably from the exact one. Assuming _θ_ < 0.5 we have _Dn_ < 0. Then the solution should be unstable. Indeed, in Fig. 6.4 one can see the effects of numerical instability for _θ_ = 0.475. 

6.4 Solution of the Advection Equation with the Finite Element Method 

239 

Note that all the presented conclusions were drawn from the modified equation corresponding to the solved pure advection equation. Thus, the modified equation approach seems to be a robust tool for consistency, stability and accuracy analysis for the hyperbolic partial differential equations. In the next sections we will use it many times. 

### **6.4 Solution of the Advection Equation with the Finite Element Method** 

### **_6.4.1 Standard Finite Element Approach_** 

Assume that the pure advection equation (6.1) with constant flow velocity is solved for 0 ≤ _x_ ≤ _L_ and _t_ ≥ 0 with appropriate auxiliary conditions. To solve this equation the Galerkin finite element method, presented in Section 5.3, is applied. The considered channel reach is divided into _M_ − 1 elements of length _�xj_ ( _j_ = 1, 2, _. . ._ , _M_ − 1). The discrete solution domain is shown in Fig. 5.19. According to the Galerkin procedure the numerical solution must satisfy the condition (5.118), which for Eq. (6.1) is written as follows: 



where: 

**N** – vector of shape functions given by Eq. (5.125), _fa_ – aproximation of function _f_ defined by Eq. (5.116). 

Let us calculate a single component of the above sum, corresponding to the element _j_ : 



A similar procedure was applied previously in Section 5.3.2 while solving the diffusion equation. Since in this element only two components of the vector **N** ( _x_ ), i.e. _Nj_ ( _x_ ) and _Nj_ +1( _x_ ), are non-zero then in Eq. (6.65) only two non-zero products, corresponding to these functions will occur. Therefore in element _j_ we have to calculate the following two integrals: 

6 Numerical Solution of the Advection Equation 

240 



Integration of the time derivative in Eq. (6.66a) was carried out in Section 5.3.2. It yields: 



whereas integration of the advective term gives: 



In a similar way is calculated integral (6.66b). Substituting the results of integration in Eqs. (6.66a) and (6.66b) one obtains the following: 



The same equations are obtained for all elements ( _j_ = 1, 2, _. . ._ , _M_ − 1). According to Eq. (6.64) they are assembled in a global system of equations: 





6.4 Solution of the Advection Equation with the Finite Element Method 

241 









In matrix notation this system of ordinary differential equations takes the following form: 



where: 



The integration of such a system of ODEs is described in Chapter 3. The application of generalized two-level scheme (3.71) yields the following system of equations: 



where: 





Let us consider an equation of system (6.72) corresponding to node _j_ . For equally spaced nodes when _�x_ = const., it takes the following form: 



6 Numerical Solution of the Advection Equation 

242 



<!-- Start of picture text -->
Fig. 6.9 Grid points for the t 1 2 1<br>method (6.73)<br>6 3 6<br>t n +1<br>(1− θ) Δ t<br>Δ t<br>θΔ t<br>t n<br>Δ x Δ x<br>x                          x                           xj  −1                               j                                 j +1 x<br><!-- End of picture text -->

where _Ca_ is the advective Courant number defined by Eq. (6.7). One can notice that Eq. (6.73) involves the grid points presented in Fig. 6.9. Appropriate equations for the extreme nodes _j_ = 1 and _j_ = _M_ are given by Eqs. (6.70a) and (6.70c). 

The modified equation corresponding to Eq. (6.73) is as follows: 



The coefficients of numerical diffusion _Dn_ and dispersion _En_ are given by: 



The values of these coefficients depend on the chosen value of _θ_ : 

**–** for the implicit trapezoidal rule ( _θ_ = 1/2): 





**–** for the Galerkin method ( _θ_ = 2/3): 





6.4 Solution of the Advection Equation with the Finite Element Method 

243 

**–** for the implicit Euler method ( _θ_ = 1): 





From the above relations results that the finite element method applied to solve advection equation is dissipation free when the time integration is carried out using the implicit trapezoidal rule, whereas it generates numerical diffusion when the Galerkin or implicit Euler methods are used. Consequently one can expect an oscillatory solution in the first case and an artificially damped solution for the other two methods. The method is absolutely stable for _θ_ ≥ 1/2, since this condition ensures that _Dn_ ≥ 0. 

To illustrate the influence of the weighting parameter _θ_ on the solution accuracy a propagation of the steep front of concentration governed by the pure advection transport equation is considered. 

_Example 6.2_ In a straight open channel of length _L_ the water flows with constant velocity _U_ . Assume: 



- boundary condition: 



The steep front of the function _f_ entering the upstream end travels along channel axis with constant velocity. Assume _U_ = 0.5 m/s = const. and _�x_ = 100 m = const. In Fig. 6.10 this traveling front is shown after _t_ = 7,200 s. The exact solution has the form of sharp front imposed as the boundary condition at _x_ = 0 shifted along _x_ 

**Fig. 6.10** Solution of the advection equation by the finite element method with various values of the weighting parameter _θ_ 



<!-- Start of picture text -->
f<br>1.4<br>1.2 Θ = 0.50<br>1.0<br>exact<br>0.8<br>0.6<br>Θ = 0.67<br>0.4<br>0.2 Θ = 1.00<br>0.0<br>0 1 2 3 4 5 6 7 8 9 10 x  [km]<br><!-- End of picture text -->

6 Numerical Solution of the Advection Equation 

244 

axis to the position _x_ = 0.5 × 7,200 = 3,600 m. This solution cannot be reproduced by the finite element method for any value of _θ_ and for any value of the advective Courant number. As results from Eqs. (6.76a), (6.76b), (6.77a), (6.77b), (6.78a) and (6.78b), regardless of the values of these parameters the finite element method is always either dissipative or dispersive one. Therefore, either unphysical damping or oscillations will be always present in the numerical solution. 

To improve the solution acuracy of the advection equation provided by the finite element method some modifications to its standard version were proposed. Below we present two ways of increasing of the accuracy approximation of the advection equation up to 3rd order with regard to both _x_ and _t_ variables. 

### **_6.4.2 Donea Approach_** 

In the approach proposed by Donea (1984) the approximation accuracy of the time derivative in the advection equation (6.1) is increased. At first this equation is approximated with regard to time: 



For this purpose usually the time derivative is replaced by one of standard difference formula. However, Donea (1984) proposed a more accurate approximation resulting from the Taylor series expansion of the function _f_ ( _x_ , _t_ ) around the time level _n_ . The Taylor formula: 



retaining the terms up to 3th order allows us to express the first order derivative as follows: 



Equation (6.81) is approximation of 3rd order with regard to time. The time derivatives of the order higher than one are eliminated using the following expressions obtained from differentiation of the considered advection equation (6.1): 



Substitution of Eq. (6.81) with Eqs. (6.82a) and (6.82b) in Eq. (6.79) yields: 

245 

6.4 Solution of the Advection Equation with the Finite Element Method 



Approximation of the time derivative gives: 



After regrouping one obtains: 



If we introduce the advective Courant number _Ca_ , Eq. (6.85) will take the final form: 



Note that _f_<sup>_n_+1</sup> and _f_<sup>_n_</sup> must be still discretized with regard to _x_ . To this end the Galerkin finite element method with linear trial functions is used. For uniform grid points the following algebraic equation is obtained: 



Such equation is written for each internal node _j_ = 2,3, _. . ._ , _M_ − 1. For _j_ = 1 the appropriate equation is given by the imposed boundary condition, whereas for _j_ = _M_ Eq. (6.87) is modified according to the rules of the finite element method. Integration of the diffusive term in Eq. (6.86) for linear shape functions was explained in Section 5.3. Consequently one obtains a system of linear algebraic equations with tri-diagonal matrix. Its solution provides the nodal values of the function _f_ at the time level _n_ +1. 

The Donea method used for solving the steep front propagation for the data from Example 6.2 provided much better results compared to the standard finite element method. In Fig. 6.11 one can see that the method produces results which coincide with the exact solution ( _Ca_ = 1) or which are only sightly different from the exact solution for other values of _Ca_ . 

The accuracy analsis using the modified equation approach shows that the method modifies the advection equation to the form of Eq. (6.74) in which _Dn_ = 0 and _En_ = 0 regardless of the value of Courant number. Therefore the method 

246 

6 Numerical Solution of the Advection Equation 



<!-- Start of picture text -->
f<br>1.2<br>Ca   = 0.50<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2 Ca   = 1.0 (exact)<br>0.0<br>0 1 2 3 4 5 6 7 8 9 10<br>x  [km]<br><!-- End of picture text -->

**Fig. 6.11** Solution of the advection equation by the finite element method with Donea formulation 

approximates the advection equation with accuracy of 3rd order with regard to _x_ and _t_ . For _Ca_ = 1 all the terms of higher order in the modified equation dissapear as well, so the method provides the exact solution. The method is only conditionally stable, as for stability the condition _Ca_ ≤ 1 is required (Donea 1984). 

### **_6.4.3 Modified Finite Element Approach_** 

##### **6.4.3.1 The Concept of the Modified Finite Element Method** 

Another approach to improve the standard finite element method was proposed by Szymkiewicz (1995). It deals with modification of the process of integration and it leads to a more general form of algebraic equations approximating the governing equation. The accuracy analysis carried out using the modified equation approach provides information which suggests the way of increasing the solution accuracy up to 3rd order. The resulting formula comprises the standard finite element and finite difference schemes as particular cases. 

According to the Galerkin procedure, described in details in Section 6.4.1, the solution of the advection equation must satisfy condition (5.118), which in this case takes the form of Eq. (6.64). In the standard approach the function _f_ ( _x_ , _t_ ) is approximated as follows: 



6.4 Solution of the Advection Equation with the Finite Element Method 

247 

where: 

_Nj_ ( _x_ ) – vector of shape functions given by Eq. (5.125), _fa_ – aproximation of function _f_ defined by Eq. (5.116). _j_ – index of node, 

_M_ – number of grid points. 

where _fj_ ( _t_ ) represents nodal value of function _f_ ( _x_ , _t_ ). When linear basis functions are applied in each element only two following integrals in Eq. (6.64) exist: 



where _�xj_ is the distance between nodes. This standard approach can be modified. Namely, the integral of the product of approximation of function and basis function in an element can be expressed as a product of certain average value of the function in the element and the integral of the basis function in this element, i.e.: 



The weighted average _fc_ ( _t_ ) in the element can be expressed using the following formulas: 









where _ω_ is a weighting parameter ranging from 0 to 1. Equations (6.90a) and (6.90b) can be rewritten as follows: 



6 Numerical Solution of the Advection Equation 

248 

##### **6.4.3.2 Solution of the Advection Equation Using the Modified Finite Element Method** 

Calculation of a single integral in expression (6.64) over an element is carried out in the following way: 





In these expressions the subscript _a_ denotes approximation according to the formula (6.88) while the subscript _c_ denotes approximation by Eqs. (6.91a) and (6.91b). It means that the alternative way of approximation of equations is applied only to the time derivative, while the derivative of 1st order with regard to _x_ is approximated using the standard approach. 

When all integrals in each element are assembled according to Eq. (6.64), the global system of ordinary differential equations over time of dimension _M_ × _M_ is obtained. For equally spaced nodes this system has the following form: 





**–** for _j_ = 2, 3, _. . ._ , _M_ − 1 



**–** for _j_ = _M_ 



Equation (6.94) can be written in a more compact matrix form: 



6.4 Solution of the Advection Equation with the Finite Element Method 

249 

where: 



The system (6.95), similarly to the one obtained for the standard finite element method, is solved using formula (3.71) with the weighting parameter _θ_ . Its application for (6.95) yields: 



where: 

_n_ – index of time level, 



The equation for node _j_ takes the following form: 



where _Ca_ is the advective Courant number ( _Ca_ = _U_ · _�t_ / _�x_ ). Equation (6.97) involves grid nodes presented in Fig. 6.12. 

**Fig. 6.12** Numerical grid for the modified finite element method 



<!-- Start of picture text -->
t 1− ω 1 − ω<br>ω<br>2 2<br>tn + 1<br>(1 − θ) Δ t<br>Δ t<br>θΔ t<br>t n<br>Δ x Δ x<br>x                          x                           xj  −1                               j                                 j +1 x<br><!-- End of picture text -->

250 

6 Numerical Solution of the Advection Equation 

**Table 6.1** Particular cases of the method depending on the values _ω_ and _θ_ 

|_ω_|_θ_|Method|
|---|---|---|
|1|1/2|FD Crank-Nicolson|
|1|1|FD implicit Euler|
|1|0|FD explicit Euler|
|2/3|1/2|FE Crank-Nicolson|
|2/3|1|FE implicit Euler|



It can be seen that the modified FE approach yields a six-point implicit scheme with two weighting parameters. For some particular values of _ω_ and _θ_ one obtains well known methods of numerical solution of the advection equation. Some of them are listed in Table 6.1. 

##### **6.4.3.3 Stability Analysis of the Modified Finite Element Method** 

Stability analysis for numerical solution of the linear advection equation solved by the modified finite element method is carried out using the Neumann method. In this approach the solution error _E_ ( _x_ , _t_ ) described by the same formula as the considered scheme, is expanded in the Fourier series (see Section 5.4.3). Since we consider the linear equation, the properties of the method can be deduced on the basis of the behaviour of one component of series. 

Substitution of Eq. (5.161) in Eq. (6.97) yields: 



where 



Using the following Euler relations (Korn and Korn 1968): 



Equation (6.98) is reformed to the formula representing the amplification factor: 

251 

6.4 Solution of the Advection Equation with the Finite Element Method 



where _G_ is the amplification factor in the form of complex number. The condition of numerical stability (Potter 1973) | _G_ | ≤ 1 implies the following condition: 



Since 



the condition (6.101) can be rewritten as: 



The dimensionless wave number _φ_ varies in the range 0≤ _ϕ_ ≤ _π,_ so cos<sup>2</sup> ( _φ_ /2), sin<sup>2</sup> ( _φ_ /2) and sin<sup>2</sup> ( _φ_ ) vary as well. The conditions: 





ensure that relation (6.102) is satisfied for any Courant number. Therefore the conditions (6.103a) and (6.103b) guarantee unconditional stability. 

##### **6.4.3.4 Accuracy Analysis Using the Modified Equation Approach** 

The numerical properties of the methods listed in Table 6.1 are well known and we also know that they are rather usuitable to solve the advection equation. However, it appears that using the accuracy analysis carried out by the modified equation approach it is possible to reach a higher order of approximation compared to the methods given in Table 6.1. Let us carry out the accuracy analysis for system (6.97). If all nodal values of function _f_ are expanded in Taylor series around the node ( _j_ , _n_ +1) and substituted in Eq. (6.97), then after regrouping the following modified equation is obtained: 



252 

6 Numerical Solution of the Advection Equation 

The coefficients of numerical diffusion _Dn_ and dispersion _En_ are given by: 





From the modified equation results that the finite element method is of 2nd order of accuracy with regard to both _x_ and _t_ for _θ_ = 1/2 only. For other values of _θ_ it is of 1st order of accuracy with regard to _t_ . However, from formula (6.106) results that the possible order of accuracy can be increased. Namely, for _θ_ = 1/2 and for 



the terms of 2nd and 3rd order in the modified equation (6.104) are cancelled. It means that in this case the proposed version of the finite element method ensures an accuracy of 3rd order with regard to _x_ as well as to _t_ . This holds for _Ca_ ≤ 1 only because of the stability condition (6.103b). Consequently one can expect that appropriate value of the weighting parameter _ω_ will provide more accurate numerical solution than the one given by the standard versions of finite element and finite difference method. 

To illustrate the effect of improvment of the finite element method the advective transport equation is solved. _Example 6.3_ In a straight open channel of length _L_ the water flows with constant velocity _U_ . Assume that: 

**–** initial condition is given by the Gauss distribution 



where _μ_ is mean value and and _σ_ is standard deviation; **–** boundary condition is following: _f_ ( _x_ = 0, _t_ ) = 0 for _t_ ≥ 0. 

The initially imposed distribution of the function _f_ along _x_ axis travels towards downstream channel end with constant velocity. The following set of data is accepted: _U_ = 0.5 m/s, _�x_ = 100 m, _�t_ = 100 s, _μ_ = 1,400 m and _σ_ = 264 m; 

In Fig. 6.13 this distribution is shown for _t_ = 14,400 s. The exact solution perfectly agrees with the numerical solution provided by the modified finite element method. This result confirms that the accuracy of the standard finite element method can be appreciably improved. 

6.5 Numerical Solution of the Advection Equation with the Method of Characteristics 

253 

**Fig. 6.13** Solution of the advection equation by the modified finite element method for _θ_ = 0.5, _Ca_ = 0.5 and _ω_ = 0.625 (exact – _solid line_ , numerical – _dotted line_ ) 



<!-- Start of picture text -->
f<br>t = 0 t = 3 h<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>0 1 2 3 4 5 6 7 8 9 x  [km]<br><!-- End of picture text -->

### **6.5 Numerical Solution of the Advection Equation with the Method of Characteristics** 

### **_6.5.1 Problem Presentation_** 

The difficulties arising in numerical solution of the pure advection equation using the methods based on the approximation of the derivatives were the motivation to seek alternative approaches. One of them is the method of characteristics, which for a long time was the main tool for solving hyperbolic equations. In this section we present a couple of algorithms based on this approach. 

Again, we consider the advection equation (6.1) with _U_ = const. > 0. It is solved in the following domain: 0 ≤ _x_ ≤ _L_ and _t_ ≥ 0. The initial condition is: _f_ ( _x_ , _t_ = 0) = _fi_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ . With assumed _U_ > 0 the boundary condition is imposed at the upstream end ( _x_ = 0) only: _f_ ( _x_ = 0, _t_ ) = _fo_ ( _t_ ) for _t_ ≥ 0. For the constant velocity the characteristics of Eq. (6.1) are straight lines in the ( _x_ , _t_ ) plane defined by Eq. (5.9): 



Let us cover the domain of solution with a mesh having the dimensions _�x_ × _�t_ , as presented in Fig. 6.14. 

If we assume such values of the mesh dimensions _�x_ and _�t_ that they satisfy the characteristic equation (6.108): 



then the diagonals of the mesh will coincide with the characteristics (Fig. 6.14). From the definition of characteristics results that the value of _f_ is constant along a characteristic. Thus, the values at the new time level can be calculated as: 

254 

6 Numerical Solution of the Advection Equation 



<!-- Start of picture text -->
t<br>Δ x Δ x<br>tn  +1<br>Δ t<br>tn<br>Δ t<br>tn –1<br>x                          x                           j  –1 j   xj  +1 x<br><!-- End of picture text -->

**Fig. 6.14** Grid points applied in the method of characteristics 





Equation (6.110) implies that the particle which at the time _tn_ is in the node ( _xj_ , _tn_ ) after the time step _�t_ will travel to the node ( _xj_ +1, _tn_ +1). Then, if the flow velocity _U_ is constant, numerical solution of the advection equation by the method of characteristics is equivalent to the exact solution. 

### **_6.5.2 Linear Interpolation_** 

Unfortunately, in natural channels the flow velocity varies is space ( _U_ = _U_ ( _x_ )) or even in time as well ( _U_ = _U_ ( _x_ , _t_ )). In such a situation it is impossible to construct such a grid which satisfies Eq. (6.108). Consequently the characteristics will no longer coincide with the diagonals of mesh and they will intersect the time level _n_ between the nodes as it is presented in Fig. 6.15. 

As the function _f_ does not vary along the characteristic, its value at the node ( _j_ , _n_ + 1) is equal to the one at the point of intersection _x_<sup>∗</sup> : 



where 



The value of _f_ at _x_<sup>∗</sup> can be calculated, for instance, using the linear interpolation between the nodes _j_ and _j_ − 1. This yields: 

6.5 Numerical Solution of the Advection Equation with the Method of Characteristics 

255 



<!-- Start of picture text -->
Δ x<br>t<br>tn +1<br>Δ t<br>t n<br>x j –2 x                          j  –1 x               x     * j x<br><!-- End of picture text -->

**Fig. 6.15** Characteristic of the advection equation going through grid point ( _j_ , _n_ + 1) and passing between the nodes 



and consequently: 



According to Eq. (5.109), which defines the Courant number we have: 



Substitution of Eq. (6.116) in Eq. (6.115) yields: 



Note that the method of characteristics with the interpolation coincides with the well known upwind scheme, being on the other hand, a particular case of the finite difference box scheme. This scheme was discussed in details in the preceding chapter and it has been shown to generate strong numerical diffusion. The example of its application is given in Figs. 5.15 and 5.16, whereas its numerical properties were described in Section 5.4. 

### **_6.5.3 Quadratic Interpolation_** 

Since linear interpolation appeared unsuccessful, a natural way of increasing of the solution accuracy seems to apply an interpolating polynomial of higher degree say of 2nd degree. For this purpose assume a local system of co-ordinates ( _X_ , _Y_ ) at node _j_ −2 (Fig. 6.15). In this system we define the following polynomial: 



256 

6 Numerical Solution of the Advection Equation 

Using nodes _j_ − 2, _j_ − 1 and _j_ one can express its coefficients as: 



Then Eq. (6.118) takes the following form: 



One can see in Fig. 6.15 that we are looking for the value of _Y_ ( _X_ ) at the point _X_<sup>∗</sup> , which is equal to: 



where _Ca_ is the advective Courant number defined by Eq. (6.116). Since the function _f_ is constant along the characteristics, then its nodal value _fj_<sup>_n_+1</sup> is the same as at the point _X_<sup>∗</sup> , i.e.: 



As the boundary condition is given at node _j_ = 1, then this equation is not self starting and an apparent node _j_ = 0 must be added, where _f_ 0<sup>_n_=</sup><sup>_f_</sup> 1<sup>_n_is assumed. As it</sup> will be shown in the next example, this method also produces significant numerical errors. 

### **_6.5.4 Holly–Preissmann Method of Interpolation_** 

A very interesting approach to solve the problem of interpolation was proposed by Holly and Preissmann (1977). The interpolation is performed between two nodes _j_ − 1 and _j_ using a polynomial of 3rd degree. To determine this polynomial the values of function _f_ as well as its spatial derivative are used. 

Knowing the function _f_ and its derivative at the time level _tn_ at the nodes _j_ − 1 and _j_ , (which makes together 4 values), one can determine the polynomial of 3rd degree. This polynomial is given by the formula: 



in which _Ca_ is the well known Courant number (Eq. 6.116), considered here as an independent variable ranging from 0 to 1. The coefficients _A_ , _B_ , _C_ and _D_ can be determined using the following conditions, satisfied by the polynomial (6.122): 



6.5 Numerical Solution of the Advection Equation with the Method of Characteristics 

257 





These conditions allow us to express the interpolating polynomial as: 



where: 



In order to calculate the derivatives of the function _f_ Holly and Preissmann (1977) assumed that the derivative _∂f_ / _∂x_ is transported similarly to the function _f_ with the advection velocity _U_ . Therefore it satisfies the following advection equation: 



Substitution of the previously determined coefficients _A_ , _B_ , _C_ and _D_ in equation for _Y_<sup>′</sup> ( _α_ ) obtained by differentiation of Eq. (6.122), yields: 



where 



This method provides relatively low numerical diffusion. It is only conditionally stable and can be applied for _Ca_ ≤ 1. Moreover, the method requires as the initial condition not only the values of the unknown function, but also its derivative, which can be problematic in some cases. 

258 

6 Numerical Solution of the Advection Equation 

### **_6.5.5 Interpolation with Spline Function of 3rd Degree_** 

Interpolation of the function _f_ can be carried out using a spline function of 3rd degree (Szymkiewicz 1993). An important feature of this approach is that no limitation of the time step _�t_ exists. 

The spline function of 3rd degree is composed of the segments which is a polynomial of 3rd degree assuming the values of interpolated function at nodes. This function is the most smooth curve among all polynomials of 3rd degree. It is important that the spline function tends to the interpolated one when the distances between the nodes are reduced. The interpolating function is expressed as follows: 



Where: 



_αj_ , _βj_ , _γ j_ – coefficients of the polynomial to be determined, _j_ = 1, 2, _. . ._ , _M_ − 1 – index of node, _M_ – total number of nodes. 

If the values of function _f_ are given at all nodes at the time level _tn_ (Fig. 6.16), then the polynomial (6.127) can be determined. 

It means that the coefficients _αj_ , _βj_ , _γ j_ for _j_ = 1,2, _. . ._ , _M_ − 1 can be calculated. Detailed description of the spline function and the method of its determination is given by Stoer and Bulirsch (1980). The algorithm is very simple and it reduces itself to the solution of the system of linear algebraic equations with tri-diagonal matrix. Knowing the interpolating polynomial, one can use it to compute the values of function _f_ at the points of intersection _xj_<sup>∗ofthebackwardcharacteristicsgoing</sup> through the nodes at the time level _tn_ +1 (Fig. 6.16). In such a way the problem is solved, since we have: 





<!-- Start of picture text -->
t Δ xj<br>t n +1<br>Δ t<br>tn<br>x          x          x           x                  x      x 1 2 3 j −1 j *          j x                       x             xj +1 M −1 M x<br><!-- End of picture text -->

**Fig. 6.16** Grid points with the backward characteristics 

6.5 Numerical Solution of the Advection Equation with the Method of Characteristics 

259 



<!-- Start of picture text -->
t Δ x j<br>t n +1<br>t<br>t n<br>x         x          x          x                 x             x        x             x              x 1 2 3 j− 1 j * j j +1 M− 1 M x<br><!-- End of picture text -->

**Fig. 6.17** Grid points with the forward characteristics 

The value of _f_ 1<sup>_n_+1</sup> is given by the imposed boundary condition. 

The presented approach makes use of the backward characteristics, which start from the nodes at the time level _tn_ +1 and intersect the time level _tn_ . An alternative method would be to apply the forward characteristics starting from the nodes at the time level _tn_ ,which intersect the time level _tn_ +1 (Fig. 6.17). 

The appropriate formula can be derived in a similar way as presented previously. The only difference is that this time the characteristics are going through the nodes at the time level _n_ and they intersect the time level _n_ + 1, so we must interpolate at this level. 

To illustrate the presented techniques of interpolation, they are applied to solve the same case of the advection transport. 

_Example 6.4_ In straight open channel of length _L_ the water flows with constant velocity _U_ . Assume the following auxiliary conditions: 

**–** initial condition is determined by the Gauss distribution 



with the mean value _μ_ and the standard deviation _σ ;_ **–** boundary condition: _f_ ( _x_ = 0, _t_ ) = 0 for _t >_ 0. 

Therefore, the initial distribution of the function _f_ in form of the Gauss distribution moves along the channel axis with constant velocity. Computations are carried out for _U_ = 0.5 m/s, _�x_ = 100 m, _μ_ = 1,400 m, _σ_ = 264 m and for various values of time step _�t_ . 

In Fig. 6.18 this traveling distribution is shown after _t_ = 9,600 s. The exact solution corresponds to the initially imposed distribution, with the center of gravity shifted to the position _x_ = _μ_ + _U_ · _T_ = 1,400 + 0.5 · 9,600 = 6,200 m. This solution is provided by all method of interpolation for _Ca_ = 1. For other values of the Courant number the solution accuracy depends on the applied method of interpolation. 

As it could be expected, the linear interpolation provides strongly smoothed solution for the Courant number less than unity (Fig. 6.18). It is because of the numerical 

260 

6 Numerical Solution of the Advection Equation 

**Fig. 6.18** Solution of the advection equation by the method of characteristics with linear interpolation 



<!-- Start of picture text -->
f / fm<br>t  = 0 t  = 9600 s<br>1.00<br>exact<br>solution<br>0.80<br>C  a = 0.75<br>0.60<br>C  a = 0.50<br>0.40<br>0.20<br>0.00<br>0 2000 4000 6000 8000 10000 x  [m]<br><!-- End of picture text -->

diffusion generated by the method, which disappears for _Ca_ = 1 only. It should be added that for _Ca_ > 1 the linear interpolation produces unstable results. 

Increasing of the degree of interpolating polynomial does not improve the accuracy solution. As one can see in Fig. 6.19, that the polynomial of 2nd degree introduces numerical dispersion and oscillations appear. The same is true for polynomials of higher degrees (Cunge et al. 1980). 

Thus, one can suppose that the standard manner of interpolation cannot be successful and some special interpolating techniques should rather be applied. This suggestion is confirmed by the results displayed in Figs. 6.20 . 

One can see that the method of interpolation proposed by Holly and Preissmann (1977) ensures an excellent agreement with the exact solution. The difference in peak obtained for _Ca_ = 0.5 is 1.6% only. Similarly accurate solution is provided by the interpolation with the spline function. 

**Fig. 6.19** Solution of the advection equation by the method of characteristics with quadratic interpolation 



<!-- Start of picture text -->
f / fm<br>t  = 0 t  = 9600 s<br>1.00<br>exact<br>0.80 solution<br>C  a = 0.25<br>0.60<br>0.40<br>0.20<br>0.00<br>–0.20<br>0 2000 4000 6000 8000 10000 x  [m]<br><!-- End of picture text -->

261 

References 



<!-- Start of picture text -->
f / fm C  a = 0.50<br>t = 0 t = 9600 s<br>1.00<br>0.80<br>0.60<br>exact<br>solution<br>0.40<br>0.20<br>0.00<br>0 2000 4000 6000 8000 10000 x  [m]<br><!-- End of picture text -->

**Fig. 6.20** Solution of the advection equation by the method of characteristics with interpolation by the Holly–Preissmann approach 

### **References** 

- Abbott MB, Basco DR (1989) Computational fluid dynamics. Longman Scientific and Technical, New York 

- Billingham J, King AC (2000) Wave motion. Cambridge University Press, Cambridge 

- Cunge J, Holly FM, Verwey A (1980) Practical aspects of computational river hydraulics. Pitman Publishing, London 

- Donea J (1984) A Taylor–Galerkin method for convective transport problems. Int. J. Num. Meth. Engng. 20:101–119 

- Fletcher CAJ (1991) Computational techniques for fluid dynamics, vol. I. Springer-Verlag, New York 

- Holly FM jr, Preissmann A (1977) Accurate calculation of transport in two dimensions. J. Hydr. Engng. ASCE 103 (11):1259–1277 

- Korn GA, Korn TM (1968) Mathematical handbook for scientists and engineers, 2nd edn. McGraw-Hill, New York 

- Liggett JA, Cunge JA (1975) Numerical methods of solution of the unsteady flow equations. 

   - In: Mahmood K, Yevjewich V (eds) Unsteady flow in open channels. Water Resources Publications, Fort Collins, Colorado, USA 

- McQuarrie DA (2003) Mathematical methods for scientists and engineers. University Science Books, Sausalito 

- Potter D (1973) Computational physics. Wiley, London 

- Stoer J, Bulirsch R (1980) Introduction to numerical analysis. Springer-Verlag, New York 

- Szymkiewicz R (1993) Solution of the advection-diffusion equation using the spline function and 

   - finite elements. Commun. Numer. Methods Engng. 9 (4):197–206 

- Szymkiewicz R (1995) Method to solve 1D unsteady transport and flow equations. J. Hydr. Engng. ASCE 121 (5):396–403 

- Warming RF, Hyett BJ (1974) The modified equation approach to the stability and accuracy analysis of finite-difference methods. J. Comput. Phys. 14:159–179 

- Whitham GB (1979) Lectures on wave propagation. Tata Institute of Fundamental Research, Bombay 

## **Chapter 7 Numerical Solution of the Advection-Diffusion Equation** 

### **7.1 Introduction to the Problem** 

Comparing the advection-diffusion equation (1.157) with the pure advection equation one can notice, that only the diffusive term differs one another equation. However this term introduces an essential difference between both equations. First of all the transport equation becomes a partial differential equation of 2nd order, whereas the advection equation is of 1st order. In addition, the type of equation changes as well. Instead of a hyperbolic equation we face a parabolic one. Consequently the auxiliary conditions should be reformulated as the parabolic equation needs two boundary conditions imposed at both upstream and downstream channel ends. More information on the properties of advection-diffusion equation were given in Section 5.1.6. 

Numerical experiments show that the diffusive term has very positive influence on the numerical solution process. This term has dissipative character so it posses smoothing properties giving rise to positive numerical effects. If the transport is diffusion dominated, no numerical difficulties are expected. In such a case to solve the advection-diffusion equation one can choose any scheme of the finite difference or finite element method. If the applied scheme is dissipation-free, its dispersivity will be neutralized by the diffusion term. Conversely, a dissipative scheme will reinforce the smoothing effect caused by the diffusion term. On the other hand, for the advection dominated transport all numerical problems presented in Chapter 6 related to the pure advection equation, occur. For this reason the essential question is to distinguish, which of the process is dominating. 

A criterion, which allows us to define the participation of both forms of transport is called the Peclet number (Patankar 1980). For the grid points spaced with _�x_ interval this number is given by the following relation: 



263 

R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_7, 

⃝C Springer Science+Business Media B.V. 2010 

264 

7 Numerical Solution of the Advection-Diffusion Equation 

where: 

_P_ – Peclet number, 

_U_ – advection velocity, 

_D_ – coefficient of diffusion, 

_�x_ – mesh dimension. 

The Peclet number can be considered as the relation between the advective and diffusive Courant numbers: 



where: 

_Ca_ – the advection Courant number given by Eq. (5.109), _Cd_ – the diffusive Courant number given by Eq. (5.174). 

Since this number is similar to the Reynolds number, very often it is called the cell Reynolds number (Fletcher 1991). 

From the definition of the Peclet number (7.1) results that: 

- _P_ = ∞ for pure advection equation, when _D_ = 0, 

- _P_ = 0 for pure diffusion equation, when _U_ = 0. 

Numerical difficulties arise for large value of the Peclet number when the transport is dominated by advection. They have the same roots as those connected with the hyperbolic equation. If in the advection-diffusion transport equation the natural physical dissipative process represented by the diffusive term is relatively weak, there is no possibility to suppress the oscillations. On the other hand, if we introduce some numerical dissipation, it can dominate the physical one. Consequently, in the numerical solution too strong attenuation will be observed. The trouble with the numerical diffusion is that it produces in the solution the advection–diffusion equation the same effects as the physical diffusion. 

During the last 30 years many numerical techniques and algorithms were proposed. In these approaches both eulerian and lagrangian representation of the transport equation are used. One can say that the methods basing on the direct approximation of the partial differential equations like the finite difference method or the finite element method applied in their standard forms, do not lead to effective algorithms. Some of the more accurate approaches are presented in the following sections. 

265 

7.2 Solution by the Finite Difference Method 

### **7.2 Solution by the Finite Difference Method** 

### **_7.2.1 Solution Using General Two Level Scheme with Up-Winding Effect_** 

Many finite difference schemes have been proposed to solve the advection-diffusion equation – for a review see e.g. Fletcher (1991). They have different properties and not all of them are equally useful. Generally it can be said that nearly all difference schemes work well for diffusion-dominated transport. Conversely, if the transport is advection-dominated, i.e. for a large Peclet number, practically all of them suffer from poor accuracy. Since the difference methods are based on the Taylor series expansion, a truncation error, greater or smaller, occurs always. Consequently, numerical schemes will always generate a dissipation and dispersion errors. The problems related to the solution of advection-diffusion equation with the finite difference method will be illustrated using a general two-level approximating formula. Note that the box scheme used previously for solving the advection equation is not appropriate for the advection-diffusion equation, since it is not capable to approximate the diffusive term. 

Consider the advection-diffusion equation (1.157) without source term: 



with constant flow velocity _U_ and coefficient of diffusion _D_ are assumed. Equation (7.3) is solved in the following domain: 0 ≤ _x_ ≤ _L_ , _t_ ≥ 0, where _L_ is length of the channel reach. The following auxiliary conditions are assumed: 

**–** initial condition: _f_ ( _x_ , _t_ = 0) = _fi_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ 

**–** boundary conditions: _f_ ( _x_ = 0, _t_ ) = _fo_ ( _t_ ) for _t_ ≥ 0 



where: _fi_ ( _x_ ), _fo_ ( _t_ ), _fL_ ( _t_ ), _ϕL_ ( _t_ ) are known. 

Equation (7.3) is approximated on the numerical grid shown in Fig. 7.1 using previously presented approximating formulas for the derivatives involved in this equation. They are following: 

**–** for 1st order time derivative (Eq. 5.99) 



266 

7 Numerical Solution of the Advection-Diffusion Equation 



<!-- Start of picture text -->
t<br>Δ x Δ x<br>tn +1<br>(1–θ) Δ t<br>P<br>θΔ t<br>tn<br>xj –1 xj xj +1 x<br><!-- End of picture text -->

**Fig. 7.1** Grid points for general two levels difference scheme 

**–** for 1st order spatial derivative (Eq. 5.100) 



**–** for 2nd order spatial derivative (Eq. 5.86) 



where _�t_ is time step and _�x_ is spatial step, whereas _n_ and _j_ are the indices of time level and node, respectively. 

Let us apply these formulas for Eq. (7.3) and assume that it is approximated at point P (Fig. 7.1). The position of this point with respect to the time axis is determined by the parameter _θ_ ranging form 0 to 1. 

Substitution of Eqs. (7.4), (7.5) and (7.6) in Eq. (7.1) yields: 



267 

7.2 Solution by the Finite Difference Method 

where: 

_η_ – the weighting parameter ranging from 0 to 1, _θ_ – the weighting parameter ranging from 0 to 1, 

_M_ – number of grid points. 

Setting _j_ = 2,3, _. . ._ , _M_ – 1 one obtains a system of algebraic equation, which must be completed by the prescribed boundary conditions. In matrix notation this system is rewritten as: 



where: 



The matrix coefficients are as follows: 



_a_ = _θ (_ − _η_ · _Ca_ − _Cd)_ , _b_ = 1 + _θ (Ca (_ 2 _η_ − 1 _)_ + 2 _Cd)_ , _c_ = _θ (Ca (_ 1 − _η)_ − _Cd)_ 



whereas the elements of the vector of the right hand side are: 







In the above equations 



268 

7 Numerical Solution of the Advection-Diffusion Equation 



represent the previously introduced advective and diffusive Courant numbers, respectively. 

Note, that for specific values of the weighting parameters determine some well known schemes are obtained. For instance _θ_ = 1/2 and _η_ = 1/2 correspond to the Crank-Nicolson finite difference scheme; _θ_ = 1 and _η_ = 1/2 – to the fully implicit centered difference scheme; _θ_ = 0 and _η_ = 1 – to the upwind scheme. Thus, Eq. (7.7) can be considered as general two-level difference scheme. 

The accuracy analysis performed using the modified approach, shows that Eq. (7.7) modifies the advection-diffusion equation to the following form: 



The coefficients of numerical diffusion _Dn_ and dispersion _En_ are defined as follows: 





The amplification factor _G_ is expressed as: 



where: 



The condition of numerical stability | _G_ | ≤ 1 requires that: 





For the values of weighting parameters satisfying these relations the scheme is absolutely stable. 

Let us remember that formula (7.5) describes all the standard approximations of 1st order derivative, because _η_ = 0 gives the forward difference, _η_ = 0.5 – the 

269 

7.2 Solution by the Finite Difference Method 

centred difference, whereas _η_ = 1 – the backward difference. Since _η_ can take values from 0 to 1, then Eq. (7.5) is capable to increase the up-wind effect in a gradual manner. 

As it can be seen, for _θ_ = 0.5 and _η_ = 0.5 the coefficient of numerical diffusion (Eq. 7.12) disappears, whereas the coefficient of numerical dispersion (Eq. 7.13) is still present. This means that if the physical diffusion in Eq. (7.3) is not strong enough, oscillations will occur. Therefore in case of weak physical diffusion introduction of some artificial diffusion may be necessary. 

_Example 7.1_ In prismatic open channel of length _L_ the water flows with constant velocity _U_ . The initial condition is determined by the Gauss distribution: 



The following Dirichlet boundary conditions are imposed at both channel ends: 





Assume that: _U_ = 0.5 m/s = const., _D_ = 0.25 m<sup>2</sup> /s = const., _�x_ = 100 m = const. and _�t_ = 25 s ( _Ca_ = 0,125), whereas the mean value is _μ_ = 1,400 m and the standard deviation is _σ_ = 264 m. In Fig. 7.2 the distributions of the function _f_ along channel axis for _t_ = 7,200 s is shown. One can see that the solution obtained for _θ_ = 0.5 and _η_ = 0.5 i.e. for the fully centered scheme is oscillating. Such behavior could be expected, because in this case the value of Peclet number is _P_ = 200, so the transport is advection-dominated. 

To suppress the oscillations, at first _θ_ = 1 is assumed. This increases the dissipativity of the scheme by introducing numerical diffusion, however it appears insufficient to ensure smooth solution. To suppress entirely the oscillations it is necessary to increase the value of the second weighting parameter _η_ as well, _η_ = 0.60 should be assumed. 

Note that to provide smooth solution it was necessary to introduce only small additional up-wind effect. This is an interesting feature of the applied scheme. 

### **_7.2.2 The Difference Crank-Nicolson Scheme_** 

Let us consider the Crank-Nicolson scheme, which is the most commonly applied method for the solution of 1D diffusion equation. We will investigate its behavior in the case of the advection-diffusion equation. Setting in Eq. (7.7) _θ_ = 0.5 and _η_ = 0.5 one obtains: 

7 Numerical Solution of the Advection-Diffusion Equation 

270 



<!-- Start of picture text -->
f/fm<br>t = 0<br>1.00 t = 7200s<br>0.80 θ = 0.50, η= 0.50<br>θ = 1.0, η = 0.50<br>0.60<br>0.40<br>0.20 θ = 1.0, η = 0.60<br>0.00<br>x[m]<br>– 0.20<br>0 2000 4000 6000 8000 10000<br><!-- End of picture text -->

**Fig. 7.2** Solution of the advection-diffusion equation by the difference scheme with _D_ = 0.25 m<sup>2</sup> /s and _Ca_ = 0.125 for various weighting parameters _θ_ and _η_ . 



Collecting the similar terms and substituting of the Courant numbers _Ca_ and _Cd_ one obtains: 



This system of equation is completed using two equations given by the assumed boundary conditions. To illustrate the properties of the Crank-Nicolson scheme, let us solve the advection-diffusion equation (7.3). 

_Example 7.2_ We use the same data as in Example 7.1 except the coefficient of diffusion. Numerical tests carried out for various values of the diffusion coefficient _D_ allow us to notice that some of them generate oscillating solution. However, for increasing value of _D_ the oscillations are systematically reduced and finally they 

7.2 Solution by the Finite Difference Method 

271 



<!-- Start of picture text -->
f/fm<br>t = 0<br>1.00<br>0.80<br>t = 9600 s<br>0.60<br>D = 25 m 2 /s<br>0.40<br>0.20<br>0.00<br>D = 10 m 2 /s<br>x [m]<br>–0.20<br>0 2000 4000 6000 8000 10000<br><!-- End of picture text -->

**Fig. 7.3** Solution of the advection-diffusion equation by the difference Crank-Nicolson scheme with _Ca_ = 1.5 for various coefficients of diffusion 

disappear. This tendency is illustrated in Fig. 7.3. Increasing of the diffusion coefficient gives rise to increased smoothing of the results. 

One can suppose, that the Crank-Nicolson scheme becomes effective tool for solving the advection-diffusion equation for sufficiently large participation of a diffusion in the transport process. 

Explanation of these features of the Crank-Nicolson scheme can be obtained by the analysis of the modified equation (7.11). For the assumed values of the weighting parameters _θ_ = 0.5 and _η_ = 0.5 one obtains: 





It means that the Crank-Nicolson scheme is dissipation free, since both derivatives of 1st order were approximated with the centred difference. The scheme does not generate numerical diffusion ( _Dn_ = 0). However, it is always dispersive, because _En_ cannot be cancelled. Consequently, since no smoothing mechanism exists, the solution of the advection equation by the Crank-Nicolson scheme will be always oscillating. 

On the other hand, while solving the advection-diffusion equation, a smoothing of solution is caused by the physical dissipation represented in the equation by the diffusion term. The intensity of smoothing increases with increasing of the coefficient of diffusion _D_ . For sufficiently large value of _D_ the wiggles are suppressed 

7 Numerical Solution of the Advection-Diffusion Equation 

272 

completely. An explanation of this property, resulting from analysis of the eigenvalues of the matrix of system (7.8) approximating the advection-diffusion equation, is given by Fletcher (1991). The eigenvalues of the tridiagonal matrix of the system (7.8) are related to _a_ , _b_ and _c_ as: 



For solution to be spatially non-oscillatory, the real eigenvalues are required. Therefore the condition: 



must be respected to ensure smooth solution. For the system (7.18), obtained from (7.8) with _θ_ = 0.5 and _η_ = 0.5 corresponding to the Crank-Nicolson scheme, relation (7.22) takes the following form: 



This inequality will be satisfied for: 



Accordingly to Eq. (7.2), the ratio _Ca_ / _Cd_ defines the Peclet number. Therefore, the Crank-Nicolson scheme will provide highly accurate solution of the advectiondiffusion equation on condition that the Peclet number is not greater than 2 ( _P_ ≤ 2). 

### **_7.2.3 Numerical Diffusion Versus Physical Diffusion_** 

A problem of great importance while solving the advection-diffusion transport equation is that the numerical error in form of the numerical diffusion gives rise to the same symptoms in solution as the physical diffusion. Therefore it is very important to distinguish in solution the effects of both processes and not to confuse them. To this order the modified equation approach should be applied as very helpful tool. This problem deals first of all with the advection dominated transport. For diffusion dominated transport the significance of numerical diffusion is relatively low. This fact is illustrated by the example presented below. 

_Example 7.3_ The advection-diffusion equation is solved for a straight prismatic channel in which the water flows at constant velocity _U_ . The channel is divided into intervals of constant length _�x_ . The following initial-boundary conditions are specified: 

7.2 Solution by the Finite Difference Method 

273 

- at _t_ = 0: _f_ ( _x_ , _t_ ) = 0 for _x_ ≥ 0, 

- at _x_ = 0 the function _f_ jumps immediately from 0 to 1 and remains constant i.e.: 



- at the downstream end located at _x_ = _L_ →∞ the function is still equal to zero: _f_ ( _x_ ) = 0. 

These conditions describe the propagation of a steep front, which simultaneously is subjected to the diffusion. Analytical solution of the advection-diffusion equation is following (Chanson 2004, Elliot and James 1984): 



where erfc(·) is the complementary function to the error function erf(·): erfc(·) =1 – erf(·). For more information about the error function see for example McQuarrie (2003). 

The same problem is solved using the difference scheme (7.7) with _θ_ = 0 and _η_ = 1.0. It means that the following explicit scheme is applied: 



The advection-diffusion equation is solved analytically and numerically for _U_ = 0.01 m/s and _�x_ = 1 m. In Figs. 7.4 and 7.5 both solutions are compared for _t_ = 3,000 s. 

Calculations were carried out with _�t_ = 10 s for _D_ = 0.002 m<sup>2</sup> /s and _D_ = 0.02 m<sup>2</sup> /s. This corresponds to the Pecet numbers equal to 5 and 0.5, respectively. Although in both cases one can notice the presence of the numerical diffusion, it is more significant for _P_ = 5, i.e. for advection-dominated transport. For greater 



<!-- Start of picture text -->
f<br>1.00<br>0.50<br>analytical<br>numerical<br>0.00<br>0 20 40 60 80 x [m.]<br><!-- End of picture text -->

**Fig. 7.4** Analytical and numerical solution of the advection-diffusion equation at _t_ = 3,000 s and for _D_ = 0.002 m<sup>2</sup> /s, i.e. for _P_ = 5 

7 Numerical Solution of the Advection-Diffusion Equation 

274 



<!-- Start of picture text -->
f<br>1.00<br>analytical<br>0.50 numerical<br>0.00<br>0 20 40 60 80 x [m.]<br><!-- End of picture text -->

**Fig. 7.5** Analytical and numerical solution of the advection-diffusion equation at _t_ = 3,000 s and for _D_ = 0.02 m<sup>2</sup> /s, i.e. for _P_ = 0.5 

coefficient of diffusion _D_ the influence of the numerical diffusion is relatively small. Note that for _θ_ = 0 and _η_ = 1.0 the coefficient of numerical diffusion (7.12) given as: 



for the assumed data is equal to 0.0045 m<sup>2</sup> /s. Then its relative influence on the considered transport process varies with variation of the coefficient of physical diffusion _D_ . 

To solve the advection-diffusion equation dissipation-free numerical methods should be applied if only possible. As it was shown previously, these methods provide accurate solutions for the Peclet number not greater than 2. Therefore, if the computation can be carried out with low value of the Peclet number, then the best choice is the application of a non-dissipative scheme as the Crank-Nicolson one. In opposite case, when the dissipative numerical method is applied to solve the advection-diffusion equation, we have to remember that in the solution a superposition of the physical and numerical diffusion will take place. We must be able to separate the effects of both processes. This question is particularly important if the value of coefficient of physical diffusion is determined by optimization methods in which the observed and computed functions at the downstream end are compared. In such a situation one can obtain a false value of searched coefficient of physical diffusion. Let us discuss this question using the results of the presented below examples of solution. 

_Example 7.4_ The advection-diffusion equation (7.3) is solved for a straight prismatic channel in which the water flows at constant velocity _U_ . The following initial-boundary conditions are specified: 

**–** at _t_ = 0: 



275 

7.2 Solution by the Finite Difference Method 

where _μ_ is mean value, whereas _σ_ is standard deviation. 

**–** at _x_ = 0 and at _x_ = _L_ is assumed: _f_ ( _x_ = 0, _t_ ) = 0, _f_ ( _x_ = _L_ , _t_ ) = 0 for _t_ ≥ 0. 

The equation is solved using the difference scheme (7.7) with _η_ = 0.5, which generates the numerical diffusion characterized by the following coefficient (Eq. 7.12): 



Note, that for _θ_ = 0.5 Eq. (7.7) becomes the Crank-Nicolson scheme, whereas for _θ_ = 1 we obtain the fully implicit scheme. 

Equally spaced grid is assumed. The computations are performed for the following set of data: _L_ = 15 km, _U_ = 0.5 m/s, _�x_ = 50 m, _�t_ = 50 s, _μ_ = 1400 m, _σ_ = 264 m and _D_ = 12.5 m<sup>2</sup> /s. The obtained results are displayed in Fig. 7.6. 

The Crank-Nicolson scheme ( _θ_ = 0.5) does not generate numerical diffusion – from Eq. (7.28) one obtains _Dn_ = 0. However, the physical diffusion is so strong, that it is capable to ensure smooth solution. Remember that the Crank-Nicolson scheme provides highly accurate solution for _P_ ≤ 2. In the considered case this restriction is respected. 

If we increase the value of the weighting parameter, let’s say assuming _θ_ = 1, then we obtain more damped solution. This is because of the additional numerical diffusion generated by the method. For the assumed data Eq. (7.28) gives 



<!-- Start of picture text -->
f<br>t = 0<br>1.0<br>0.8<br>0.6<br>t = 7200 s<br>0.4<br>θ = 0,5<br>0.2<br>θ = 1<br>0.0<br>0                      2500                   5000                  7500 x [m]<br><!-- End of picture text -->

**Fig. 7.6** Numerical solution of the advection-diffusion equation using the difference scheme (7.7) for various values of the weighting parameter _θ_ 

276 

7 Numerical Solution of the Advection-Diffusion Equation 

_Dn_ = 6.25 m<sup>2</sup> /s. In other words, while solving the advection-diffusion equation (7.3) using the dissipative scheme, as a matter of fact we obtain a solution, which coincides with the exact solution of the following equation: 



If we apply a dissipative method to solve the advection-diffusion equation, then as results form Eq. (7.29), we always reinforce the diffusive transport and consequently we increase smoothing. 

While the numerical dispersion generated by the applied scheme can be identified relatively easily owing to the oscillating solution, identification of the numerical diffusion needs some additional analysis. Note that the lack of evaluation of the numerical diffusion can lead to wrong conclusions on the strength of physical diffusion, since in the solution we observe common effect of both natural and artificial dissipative processes. We must be aware that the numerical diffusion generated by the standard numerical methods for typically used mesh dimensions _�x_ and _�t_ , can be of the order similar to the physical one, i.e. _Dn_ ≈ _D_ . This conclusion is illustrated in the example presented below. 

_Example 7.5_ In straight channel of length _L_ , having constant bed slope and constant cross-sections, the water flows with constant velocity _U_ . Assume that initially at _t_ = 0, the concentration along channel axis is equal to zero: _f_ ( _x_ , _t_ = 0) = 0 for 0 ≤ _x_ ≤ _L_ . At the upstream end _x_ = 0 the following boundary condition is imposed: 



This means that a triangular distribution of concentration with peak _fm_ occurring at _tm_ is assumed. At the downstream end _x_ = _L_ the Neumann boundary condition _∂f /∂x_ | _x_ = _L_ = 0 is imposed. 

The advection-diffusion equation is solved using the difference scheme (7.7) with _η_ = 0.5 for the following data: _L_ = 5,000 m, _�x_ = 50 m, _U_ = 0.5 m/s, _fm_ = 1 and _tm_ = 1,200 s. Computations were performed for the two following sets of parameters: 

(1) _θ_ = 1, _Ca_ = 1, _D_ = 5 m<sup>2</sup> /s; (2) _θ_ = 1, _Ca_ = 1.4, _D_ = 0 m<sup>2</sup> /s. 

The results of calculation obtained for these sets of data are shown in Fig. 7.7. They represent the graph of _f_ in time at position _x_ = 2,500 m. 

As one can see, the results are practically identical for two different sets of data. This fact can be easily explained. Let us calculate the coefficient of numerical diffusion according to Eq. (7.28) for the first set of data: 

7.2 Solution by the Finite Difference Method 

277 



<!-- Start of picture text -->
f<br>1.2<br>x = 0<br>set 1<br>0.8 set 2<br>x  = 2500 m<br>0.4<br>0.0<br>0 3600 7200 10800 14000 18000  t [s]<br><!-- End of picture text -->

**Fig. 7.7** Equivalent effect of the physical and numerical diffusion 



This means that the diffusive transport was artificially increased and the obtained solution coincides with the exact solution of the advection-diffusion equation produced by a non-dissipative method for the following value of diffusion coefficient: _D_ + _Dn_ = 5 + 12.5 m<sup>2</sup> /s = 17.5 m<sup>2</sup> /s. 

In the second set of data the physical diffusion is neglected ( _D_ = 0), whereas the values of _θ_ and _Ca_ are such, that the scheme generates numerical diffusion with _Dn_ = 17.5 m<sup>2</sup> /s. Obviously, in this case the results are the same as previously. Actually, each set of data which satisfies the condition: _D_ + _Dn_ = 17.5 m<sup>2</sup> /s will provide the same numerical solution. 

In such a situation one can expect problems while trying to identify the real value of the coefficient _D_ from the results of field experiments, applying the optimization approach. Since one can obtain the same results for practically infinite number of combinations of the values of parameters _D_ , _θ_ and _Ca_ , then the determination of the extreme point of the objective function may be impossible. This problem may be solved on condition that we are capable to separate the effect of numerical diffusion from the effect of physical diffusion in the solution. As we showed previously, this can be done via the analysis of the modified equation only. 

### **_7.2.4 The QUICKEST Scheme_** 

One of the most frequently applied finite difference approaches is the QUICKEST scheme (Quadratic Upstream Interpolation for Convective Kinematics with 

7 Numerical Solution of the Advection-Diffusion Equation 

278 

Estimated Streaming Terms). This method approximates the advection-diffusion equation with accuracy of 3rd order. 

The QUICKEST scheme was at first proposed by Leonard (1979). To approximate the advective term apart from the grid points the intermediate points _j_ – 1/2 and _j_ + 1/2 are used. At these point the values of function _f_ are determined via quadratic interpolation based on the nodes _j_ – 2, _j_ – 1 and _j_ in the first case, and _j_ – 1, _j_ and _j_ + 1 in second case, respectively. 

An equivalent scheme was derived by Basco (Abbott and Basco 1989), who introduced appropriate difference operators approximating the terms of the advection-diffusion equation. This variant, being more often used, will be presented below. 

Let us approximate the equation of advection-diffusion with explicit centred difference scheme, including the truncation error. One obtains: 



Equation (7. 30) is simplified by: 

- neglecting all terms with spatial derivatives of order higher than 3, 

- replacing all derivatives with regard to time by the spatial derivatives using the expression resulting from advection-diffusion equation (7.3). 

Taking into account these assumptions Eq. (7.30) is rearranged to the following form: 



The differential operators are approximated by the formulas: 



7.3 Solution Using the Modified Finite Element Method 

279 



Substitution of Eqs. (7.32) and (7.33) in Eq. (7. 31) yields the final form of the scheme: 



As in the formula for node _j_ the values of _f_ coming from preceding nodes are involved, the method is not self-starting. 

Note that Eq. (7.34) with _U_ = 0 ( _Ca_ = 0) coincides with the explicit difference scheme for diffusion equation (Eq. (7.7) with _θ_ = 0), whereas for _D_ = 0 and _Ca_ = 1 one obtains the well known formula _fj_<sup>_n_+1</sup> = _fj_<sup>_n_</sup> −1<sup>, coinciding with the upwind</sup> scheme for the advection equation (Eq. 5.108) with _Ca_ = 1). Leonard (1979) showed that the region of stability of method (7.34) varies according to the relation between _Ca_ and _Cd_ . 

### **7.3 Solution Using the Modified Finite Element Method** 

Let us reconsider the advection-diffusion equation (Eq. 7.3) but this time with variable advection velocity _U_ = _U_ ( _x_ ) and constant coefficient of diffusion _D_ = const. Of course all discussed methods can be developed for variable flow velocity. However, as we will see soon, the modified element method allows taking into account _U_ ( _x_ ) in a natural way. 

To solve Eq. (7.3) the modified Galerkin finite element method, presented in the Section 6.4.3, is applied. For some particular choices of the weighting parameters this approach reduces to the well known finite element or finite difference methods. Assume that the segment of a channel is divided with _M_ nodes into _M_ – 1 elements of length _�xj_ ( _j_ = 1,2, _. . ._ , _M_ – 1). The discretized solution domain is shown in Fig. 5.19. 

Accordingly to the Galerkin procedure the numerical solution must satisfy the condition (5.118). For Eq. (7.3) with previously proposed modification this condition takes the following form (Szymkiewicz 1993): 



7 Numerical Solution of the Advection-Diffusion Equation 

280 

where **N** ( _x_ ) is the vector of shape functions having components given by Eq. (5.125). In Eq. (7.35) the subscript _c_ denotes approximation of function according to formula (6.91), whereas _a_ denotes the approximation of the function according to formula (6.88). 

Let us calculate a single component of the above sum, corresponding to the element _j_ . Since in this element only two components of the vector **N** ( _x_ ), i.e. _Nj_ ( _x_ ) and _Nj_ +1( _x_ ), are non-zero, then in Eq. (7.35) only two following non-zero products will occur: 



Calculation of the integrals (7.36) is carried out step by step as it was shown previously: 

- for the time variation term in Section 6.4.3.2 

- for the advective term in Sections 6.4.1 and 6.4.3.2, 

- for the diffusive term in Section 5.3.2 (Eqs. 5.136 and 5.139). 

Finally, the integral (7.36a) gives: 



whereas the integral (7.36b) gives: 



where _ω_ is the weighting parameter ranging from 0 to 1. 

Equations similar to (7.37a) and (7.37b) are obtained for all elements ( _j_ = 1, 2, _. . ._ , _M_ – 1). According to Eq. (7.35) they should be assembled leading to the following global system of ordinary differential equations: 

**–** for _j_ = 1 



7.3 Solution Using the Modified Finite Element Method 

281 









As the Dirichlet boundary conditions at the upstream and downstream ends are imposed, the fluxes at these endpoints disappear. Consequently Eq. (7.38) can be rewritten in the following matrix notation: 



where: 



All matrices are of dimensions of (2 _M_ ) × (2 _M_ ). 

The initial-value problem is solved using the two levels method (3.71) described in Section 3.2. This method used for Eq. (7.39) yields the following system of algebraic equations: 



where: 

_n_ – index of time level, _θ_ – weighting parameter, _�t_ – time step. 

7 Numerical Solution of the Advection-Diffusion Equation 

282 

After introducing the imposed boundary conditions this system is solved using an appropriate method giving approximated value of _f_ at next time level. 

_Example 7.6_ In a straight channel of length _L_ having constant bed slope and constant cross-sections, the water flows with constant velocity. Assume that initially at _t_ = 0, the concentration along channel axis is equal to zero: _f_ ( _x_ , _t_ = 0) = 0 for 0 ≤ _x_ ≤ _L_ . At the upstream end _x_ = 0 the following boundary condition is imposed: 



At the downstream end _x_ = _L_ the Neumann boundary condition 



is assumed. Therefore this example deals with the propagation of the sharp front of concentration caused simultaneously by advection and diffusion (without the source terms). In this case the advective-diffusive transport equation has the analytical solution given by (7.25). 

The following data are assumed: _L_ = 5000 m, _U_ = 0.5 m/s, _�x_ = 100 m, _�t_ = 100 s, which gives _Ca_ = 0.5, whereas the coefficient of diffusion is _D_ = 10 m<sup>2</sup> /s. It means that in this case the Peclet number is relatively high ( _P_ = 40). This indicates that advection dominates in the transport process. 

In the Fig. 7.8 a comparison between analytical and numerical solution is presented. The numerical solution is obtained with the following values of the weighting parameters: _θ_ = 0.5 and _ω_ = 0.625 (calculated using Eq. (6.107)). Very 

**Fig. 7.8** Analytical and numerical solution of the advection-diffusion equation obtained for various time with _P_ = 40 



<!-- Start of picture text -->
f<br>1.0<br>0.8<br>0.6<br>t = 1h t = 2h t = 3h<br>0.4<br>0.2<br>0.0<br>0 1 2 3 4 5 6 7<br>x[km]<br><!-- End of picture text -->

7.4 Solution of the Advection-Diffusion Equation with the Splitting Technique 

283 

small differences between the solutions confirm good properties of the proposed method. In spite of large value of the Peclet number only insignificant wiggles, quickly disappearing with time, occurred. 

### **7.4 Solution of the Advection-Diffusion Equation with the Splitting Technique** 

The splitting technique (also called factorized steps or decomposition method) is not a numerical method of solution of the partial differential equations. It should be rather considered as an approach that simplifies a complex problem by its decomposition. The concept of such approach is to split in each time step the governing equation or the system of equations into a sequence of simpler problems. Next, the obtained equations are solved using the appropriate numerical methods. The splitting process can be carried out in different ways. For example a 2D or 3D problem can be split with regard to the independent spatial variables in order to be solved as a sequence of 1D problems. The governing equation can be decomposed with regard to time as well. An example of such approach is well known Alternating Direction Implicit (ADI) method commonly used to solve 2D diffusion equation in which to reach solution at new time level we ought to perform the calculations in two stages with a half time step at each one (Abbott and Basco 1989). At every stage 1D diffusion equations are solved. Such approach leads to simpler and more efficient algorithms, which save the computational time and memory. 

The decomposition can be also performed with regard to the physical processes present in the governing equation. For instance in the case of advection-diffusion equation we deal with a superposition of two physically different processes: advection and diffusion. Therefore this equation can be split in two equations representing the advective part and the diffusive part respectively. 

Theoretical background of the factorized steps technique was given by Yanenko (1971). A comprehensive and up-to-date information on the splitting technique for hyperbolic problems is given by LeVeque (2002). The method and its implementation is presented by Cunge et al. (1980). Many examples of its implementation for solving both hydrodynamics and transport equations were published in numerous papers as well. In this section we will limit our consideration to the problem of 1D advection-diffusion transport equation. 

Let us consider the advection-diffusion equation with the source term (1.157): 



This equation can be rewritten as follows: 



7 Numerical Solution of the Advection-Diffusion Equation 

284 

where the term _F_ contains all terms of Eq. (7.41) except the time derivative: 



Equation (7.42) integrated over a single time step ⟨ _t_ , _t_ + _�t_ ⟩ gives: 



where _ft_ and _ft_ + _�t_ denote the values of function _f_ at the time levels _t_ and _t_ + _�t_ respectively. Numerical methods differ in the way of approximation of the differential operators in _F_ and in the quadrature method used to calculate the integral in Eq. (7.44). 

From Eq. (7.43) results that the new variable _F_ can be presented as the sum of three components representing the advective and diffusive transport as well as the source term: 



where: 



Substitution of Eq. (7.45) in Eq. (7.44) yields: 



Let us exclude the first two terms of the right side hand and denote them as: 



Then Eq. (7.46) will take a more compact form: 



285 

7.4 Solution of the Advection-Diffusion Equation with the Splitting Technique 

The same can be applied to Eq. (7.48). Introducing a new variable: 



allows us to rewrite Eq. (7.48) as follows: 



As it was afore-mentioned, in each time step _�t_ the solution of the advectiondiffusion equation (7.41) is performed in three stages. In the first stage the pure advection equation (7.47) is solved. Next, the diffusion equation (7.49) is solved using the results obtained in the first stage. As the last stage of the calculation, Eq. (7.50) representing the source term is solved. This algorithm can be written in a more general form. Solution of Eq. (7.41) in the time interval ⟨ _t_ , _t_ + _�t_ ⟩ is obtained as a results of the following sequential solutions: 



The searched value of the function _f_ at the time level _t_ + _�t_ is given as follows: 



Note that in each time step the result obtained from the preceding stage are used as initial condition for the next one. 

The splitting process can introduce an error into solution. As shows LeVeque (2002) this error does not exist for linear problems, whereas it occurs for nonlinear equations. Consequently, for linear problems the order of computational stages preformed in a single time step does not matter. 

The advantage of the splitting technique is the possibility of using different numerical methods for solving each part of the transport equation. To solve the pure advection equation the method of characteristics with appropriate technique of interpolation is very often used, whereas the diffusion equation can be solved using a number of well known numerical methods. For instance Cunge et al. (1980) suggest the Holly-Preissmann approach for solution of the advective part (see Section 6.5.4) and an explicit difference scheme for the diffusive part of the governing equation. Good results can be also achieved with other methods (Szymkiewicz 1995). 

286 

7 Numerical Solution of the Advection-Diffusion Equation 

For illustration of this approach the equation of advection-diffusion transport with a source term describing the decay of the transported matter is solved. If we assume the steady state and the source term in the simplest form _δ_ = _κ_ · _f_ ( _κ_ is constant of decay), then the governing equation (7.41) is reduced to the following ordinary differential equation: 



For constant value _f_ 0 imposed at _x_ = 0 Eq. (7.53) has the exact solution (Elliot and James 1984): 



where: 

_f_ 0 – concentration imposed at the upstream end, 

_κ_ – constant of decay. 

In the example presented below we solve Eq. (7.41) using the splitting technique for such initial and boundary conditions which ensures the solution equivalent to Eq. (7.54). 

_Example 7.7_ In a straight channel of length _L_ in which the water flows with constant velocity _U_ let us solve the advection-diffusion transport equation (7.41): 



Assume that initially at _t_ = 0, the concentration along channel axis is equal to zero: _f_ ( _x_ , _t_ = 0) = 0 for 0 ≤ _x_ ≤ _L_ . At the upstream end _x_ = 0 the following boundary condition is imposed: 



Therefore at _x_ = 0 a jump of function _f_ is imposed. At the downstream end _x_ = _L_ the Neumann boundary condition ( _∂f_ / _∂x_ ) _x_ = _L_ = 0 is assumed. The following numerical methods are applied to solve Eq. (7.55): 

- the method of characteristics with interpolation via spline functions of 3rd degree for the advection term, 

- the Crank-Nicolson difference scheme for the diffusion term, 

- the implicit trapezoidal rule for the source term. 

Equation (7.55) is solved for the following data: _L_ = 12 km, _U_ = 0,5 m/s, _x_ = 100 m, _t_ = 100 s, _D_ = 10 m<sup>2</sup> /s and _κ_ = 0.0004 s<sup>−1</sup> . Since the function imposed at the upstream end does not vary in time, the solution tends to the steady state. For 

7.4 Solution of the Advection-Diffusion Equation with the Splitting Technique 

287 

**Fig. 7.9** Analytical ( _solid line_ ) and numerical ( _dotted line_ ) solutions of the advection-diffusion equation with source term after _t_ = 3 h 



<!-- Start of picture text -->
f<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>0 2 4 6 8<br>x[km]<br><!-- End of picture text -->

the assumed data it is reached after _t_ = 3 h. The function _f_ ( _x_ ) corresponding to this state is shown in Fig. 7.9. For comparison the exact solution (7.54) of Eq. (7.53) is plotted as well. It can be seen that very good agreement between both solutions is obtained. 

_Example 7.8_ Assuming that dissolved mater is fully mixed in the river cross section, the evaluation of the biochemical oxygen demand ( _BOD_ ) and the dissolved oxygen ( _DO_ ) in flowing stream can be described by the system of two 1D equations (Elliot and James 1984): 



where: 

- _t_ – time [s], _x_ – position [m], _B_ – _BOD_ concentration of [mgl<sup>−1</sup> ], _C_ – concentration of _DO_ of [mgl<sup>−1</sup> ]], _U_ – average velocity of water flow [m s<sup>−1</sup> ], _E_ – coefficient of longitudinal dispersion [m<sup>2</sup> s<sup>−1</sup> ], _A_ – wetted cross-sectional area [m<sup>2</sup> ] _K_ 1 – the _BOD_ reaction rate [s<sup>−1</sup> ], _K_ 2 – the reaeration rate coefficient [s<sup>−1</sup> ], _K_ 3 – the rate coefficient for removal of _BOD_ by sedimentation and adsorption [s<sup>−1</sup> ], 

7 Numerical Solution of the Advection-Diffusion Equation 

288 

- C _s_ – the saturated dissolved oxygen concentration [mgl<sup>−1</sup> ], 

- _φ_ – the net removal rate of dissolved oxygen for all processes other then biochemical oxidation. 

One can add that finding appropriate formulas for all biochemical processes represented in the source terms in these equations is a complex task and their mathematical description is still subject of research. We neglect this problem here since the source terms rather do not complicate the numerical solution of advective-diffusive transport equation. 

The required auxiliary conditions are formulated as follows: 

- the initial conditions: for _t_ = 0 _B_ ( _x, t_ ) = _Bi_ ( _x_ ) and _C_ ( _x, t_ ) = _Ci_ ( _x_ ) for 0 ≤ _x_ ≤ _L_ are given, 

- the boundary conditions: 

   - at the upstream end _B_ ( _x_ = 0, _t_ ) = _B_ 0( _t_ ) and _C_ ( _x_ = 0, _t_ ) = _C_ 0( _t_ ) for t≥ 0 are imposed 

   - at the downstream end _(∂B/∂x)x_ = _L_ = _φB (t)_ and _(∂C/∂x)x_ = _L_ = _φC (t)_ for _t_ ≥ 0 are imposed. 

Solving numerically the initial-boundary problem for Eqs. (7.56) and (7.57), the distribution of the dissolved oxygen and the biochemical oxygen demand along considered channel reach is obtained. In the considered example it is assumed that initially _BOD_ ( _x_ , _t_ = 0) = 0 and _DO_ ( _x_ , _t_ = 0) = 5 mg dm<sup>−1</sup> . The time constant load causes that at point _x_ = 0.8 km the _BOD_ increases immediately to 20 mg dm<sup>−1</sup> . The computations were performed for _K_ 1 = 1.25 · 10<sup>−4</sup> s<sup>−1</sup> , _K_ 2 = 5 · 10<sup>−6</sup> s<sup>−1</sup> , _K_ 3 = 5 · 10<sup>−4</sup> s<sup>−1</sup> , _Cs_ = 5 mg l<sup>−1</sup> , _D_ = 10 m<sup>2</sup> /s, _�t_ = 100 s, _L_ = 15 km, _�x_ = 100 m and _U_ = 0.25 m/s. The results obtained for _t_ = 10 h are presented in Fig. 7.10. 

**Fig. 7.10** Steady distribution of BOD and DO along channel downstream of the point of release the pollutant obtained via solution of Eqs. (7.56) and (7.57) 



<!-- Start of picture text -->
mg/dm 3<br>20.0<br>17.5<br>15.0<br>B OD<br>12.5<br>10.0<br>7.5<br>DO<br>5.0<br>2.5<br>0.0<br>0 2 4 6 8 10<br>x [km]<br><!-- End of picture text -->

7.5 Solution of the Advection-Diffusion Equation 

289 

One can notice that the computed distributions _BOD_ ( _x_ ) and _DO_ ( _x_ ) are typical for the flow downstream of the point of discharging when the waste water is released with a load constant in time. 

### **7.5 Solution of the Advection-Diffusion Equation Using the Splitting Technique and the Convolution Integral** 

### **_7.5.1 Governing Equation and Splitting Technique_** 

In certain cases, when the flow in open channel is steady and uniform, 1D linear advective-diffusive equation describing the transport of pollutants can be solved without the approximation of derivatives. In this approach one can use the exact solution of the advective-diffusive equation with constant coefficients obtained for the upstream boundary condition in form of the Dirac delta function and the downstream end tending to infinity. Therefore instead of a system of algebraic equations given by the finite difference or element method, an integral of convolution must be calculated numerically. For this purpose any quadrature method can be used. The error dependent on the accuracy of applied method is much smaller than the one caused by the truncation of Taylor series. Consequently the proposed approach is capable of producing highly accurate solution, because it does not generate any numerical dissipation or dispersion (Szymkiewicz and Weinerowska 2005). 

In Chapter 1 the following equation describing transport of a passive substance dissolved in water in open channel was derived (Eq. 1.153): 



where: 

_t_ – time, 

_x_ – spatial coordinate, 

_f_ – concentration, 

_D_ – coefficient of longitudinal dispersion, 

_A_ – cross-sectional area, 

_Q_ – discharge, 

_δ_ – source term. 

Equation (7.58) is solved in domain: 0 ≤ _x_ ≤ _L_ and _t_ ≥ 0 ( _L_ – length of channel reach). After developing the derivatives in the two first terms and taking into account the continuity equation (1.80) one obtains: 



7 Numerical Solution of the Advection-Diffusion Equation 

290 

where _q_ is lateral inflow. This equation can be rewritten as follows: 



where: 

_U_ = _Q_ / _A_ – cross sectional average velocity, _ϕ_ = _δ_ – _q_ · _f_ / _A_ – modified source term. 

To solve the above equation an approach based on the splitting technique described in preceding section is applied. Equation (7.60) can be rewritten in the form 



where 



At every time step _�t_ Eq. (7.60) is solved in two stages. In the first stage the advective-diffusive transport is considered: 



with the initial condition _f_<sup>(1)</sup> ( _t_ ) = _f_ ( _t_ ). In the second stage the source term is taken into account: 



with the initial condition _f_<sup>(2)</sup> ( _t_ ) = _f_<sup>(1)</sup> ( _t_ + _�t_ ). Finally one obtains: _f_ ( _t_ + _�t_ ) = _f_<sup>(2)</sup> ( _t_ + _�t_ ). The above equations are solved using the convolution approach and the finite difference method, respectively. 

### **_7.5.2 Solution of the Advective-Diffusive Equation by Convolution Approach_** 

Let us consider an advective-diffusive transport equation in the form: 



7.5 Solution of the Advection-Diffusion Equation 

291 

with constant coefficients ( _U_ = const., _D_ = const.). For the initial condition _f_ ( _x_ , _t_ = 0) = 0 and the boundary conditions _f_ ( _x_ = 0, _t_ ) = _δ_ ( _t_ ), _f_ ( _x_ →∞, _t_ ) = 0 for _t_ ≥ 0 the following exact solution is obtained (Eagleson 1970): 



It holds for _t_ > 0 and _x_ > 0. The function _δ_ ( _t_ ) imposed at the upstream end represents the Dirac delta function (McQuarrie 2003). 

A river reach bounded by cross-sections _x_ = 0 and _x_ = _x_ 1 is considered as dynamic linear and time invariant system. Therefore it can be described by a convolution integral: 



where _P_ is memory of the system. Equation (7.66) represents the way of transformation of function _f_ 0( _t_ ) into _f_ 1( _t_ ) (Fig. 7.11). More information on the Dirac delta function and the convolution integral is given in Section 9.5. 

Equation (7.66) allows us to calculate the function _f_ 1( _t_ ) at any point _x_ 1> 0 for any function _f_ 0( _t_ ) imposed at upstream boundary _x_ = 0, on condition that the function _w_ ( _t_ ) is given. 

Equation (7.66) says, that an output at time _t_ is determined by an input taken from time interval ⟨ _t_ – _P_ , _t_ ⟩ because for _t_ ≥ _P_ the function _w_ ( _t_ ) insignificantly differs to zero. In this case for _x_ = _x_ 1 Eq. (7.65) becomes an impulse response function for the considered river reach: 



Application of Eq. (7.66) will be successful on condition that the mass balance is satisfied. This requirement implies the following condition: 



<!-- Start of picture text -->
P<br>w ( t ) dt  = 1 (7.68)<br>�<br>0<br>f 0 f 1<br>t t<br>x  = 0 x  =  x 1 x<br><!-- End of picture text -->

**Fig. 7.11** A channel reach of length _x_ 1 as a system transforming _f_ 0( _t_ ) into _f_ 1( _t_ ) 

7 Numerical Solution of the Advection-Diffusion Equation 

292 

As the convolution integral can be calculated numerically using any quadrature method (Press et al. 1992), this relation can be used to determine suitable value of system memory and time step _�τ_ accepted to compute the integral in Eq. (7.66). We will come back to the Dirac delta function and the convolution technique in Chapter 9, while discussing the linear lumped flood routing models. 

Let us apply the described approach to solve the simplest case of advectivediffusive transport for a steady uniform flow in straight and long channel. 

_Example 7.9_ In open channel a steady uniform flow takes place. The flow velocity _U_ is constant. The initial concentration is equal to zero, whereas at _x_ = 0 the following function _f_ 0( _t_ ) is assumed: 



It means that a rectangular distribution of concentration is imposed. It is a very challenging test for the method of solution. 

Assuming _U_ = 0.5 m s<sup>−1</sup> compute the functions _fi_ ( _t_ ) ( _j_ = 1, 2) at the points _x_ 1 = 1,500 m and _x_ 2 = 3,000 m for two values of diffusion coefficient: _D_ = 0.0005 m<sup>2</sup> s<sup>−1</sup> and 0.5 m<sup>2</sup> s<sup>−1</sup> . 

The obtained solutions presented in Fig. 7.12 are close to the exact one. One can suppose that the error resulting from trapezoidal rule used to integrate a convolution is not significant. The calculations were carried out for _�τ_ = 2 s. The Peclet number (Eq. 7.1) for the data used here is equal to ( _U_ | _D_ ) _�x_ =1,000 _�x_ . It means a total domination of advection in the transport process, even for the smallest value of _�x_ applied in practice. 



<!-- Start of picture text -->
f/fm<br>x  = 0 x  = 1500 m x  = 3000 m<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0 1800 3600 5400 7200 9000 t  [s]<br>boundary condition  D  = 5  10    m  /s. −4 2 D  = 5  10    m  /s. −1 2<br><!-- End of picture text -->

**Fig. 7.12** Advective-diffusive transport of a rectangular distribution of concentration with _U_ = 0.5 m/s 

7.5 Solution of the Advection-Diffusion Equation 

293 

### **_7.5.3 Solution of the Advective-Diffusive Equation with Variable Parameters and Without Source Term_** 

The example of solution presented above concerned a steady uniform flow. As a matter of fact, steady flow in a natural stream is spatially varied. The velocity and cross-sectional areas vary along _x_ axis. Such case of transport is described by Eq. (7.60). Neglecting the source term it can be rewritten as: 



where: 

_U_ = _U_ ( _x_ ) – cross-sectional average velocity, 

_A_ = _A_ ( _x_ ) – area of wetted cross-section. 

Both functions _U_ ( _x_ ) and _A_ ( _x_ ) can be obtained from the solution of the system of equations for steady gradually varied flow described in Chapter 4. 

The convolution approach, which holds for steady uniform flow, can be extended to solve the transport equation with variable coefficients, i.e. for steady gradually varied flow. To this end the diffusive term in Eq. (7.69) is differentiated: 



In this equation the advective velocity and the coefficient of diffusion vary in space. To solve Eq. (7.70) using the presented method, one can “freeze” locally the velocity and the diffusivity. For this purpose a channel of length _L_ is divided into _M_ intervals of length _�xi_ as in the finite difference or finite element method (Fig. 7.13a). 

Each channel reach is considered as a dynamic system in which both the advective velocity and the coefficient of diffusion are assumed constant. Let us introduce new variables defined as follows: 



<!-- Start of picture text -->
a)<br>Δ x 1 Δ x 2 Δ xM<br>x  0 = 0 x                      1 x                                             2 x                    x   M  −1 M =  L x<br>b)<br>f 0( t ) subsystem1 f   (1 t ) subsystem2 f 2  ( t ) ... f M       (−1 t ) subsystem M f    ( M t )<br><!-- End of picture text -->

**Fig. 7.13** A channel divided into intervals of length _�xi_ ( **a** ) represented by _M_ subsystems ( **b** ) 

7 Numerical Solution of the Advection-Diffusion Equation 

294 



where: 

_uj_ – modified average advective velocity between nodes _j_ – 1 and _j_ , _dj_ – average coefficient of diffusion between nodes _j_ – 1 and _j_ . 

For each segment _j_ = 1, 2, _. . ._ , _M_ one obtains the following impulse response: 



Consequently the function _fj_ ( _t_ ) for consecutive nodes ( _j_ = 1, 2, 3, _. . ._ ) can be calculated as follows: 



where _Pj_ is memory of system _j_ . Therefore a channel of length _L_ has been divided into _M_ subsystems of length _�xj_ in series, where the output from preceding reach is the input for next one (Fig. 7.13b). This procedure is illustrated by solution of Eq. (7.69) for steady gradually varied flow. 

_Example 7.10_ In a trapezoidal channel of width _B_ = 10 m, bank slope 1 : 1.5, bed slope _s_ = 0.0005, the Manning coefficient _nM_ = 0.025 the discharge rate is _Q_ = 18.487 m<sup>3</sup> s<sup>−1</sup> . The normal depth corresponding to this value of _Q_ is _Hn_ = 1.5 m. At _x_ = 0 the water level was raised by a dam to _Ho_ = 5 m (Fig. 7.14). For these data the flow profile _h_ ( _x_ ) and the flow velocity _U_ ( _x_ ) are computed with _�x_ = −300 m = const. for 25 nodes using approach presented in Chapter 4. The calculated depths vary from 5 m at _x_ = 0 to 1.502 m at _x_ = −7,200 m. The corresponding crosssectional areas vary from 87.5 m<sup>2</sup> to 18.43 m<sup>2</sup> and velocities from 0.091 to 0.43 m s<sup>−1</sup> respectively. 

Next at the upstream end ( _x_ = −7,200 m) the rectangular distribution of concentration as in Example 7.9, is specified. The function _f_ 25( _t_ ) calculated at the section of a dam for constant coefficient of diffusion _D_ = 0.0075 m<sup>2</sup> s<sup>−1</sup> is presented in Fig. 7.15. 

The initial rectangular distribution of function _f_ travels along _x_ axis with insignificant deformation. It results from varied velocity _U_ ( _x_ ) and small value of _D_ . Due to the lack of numerical dissipation and dispersion the obtained solution is free of oscillations and it keeps very strong gradients. The error of solution can be caused 

7.5 Solution of the Advection-Diffusion Equation 

295 



<!-- Start of picture text -->
h<br>H ( x )<br>H 0<br>.<br>h ( x )<br>Hn<br>Z x ( )<br>datum<br>x = 0 x<br>s =0.0005<br>Q  = 18.487 m3s −1<br><!-- End of picture text -->

**Fig. 7.14** A steady varied flow in a channel 



<!-- Start of picture text -->
f/fm<br>x = −7200 m x = 0<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>0         2000     4000  44000    46000    48000 t  [s]<br><!-- End of picture text -->

**Fig. 7.15** Advective-diffusive transport with varied flow velocity _U_ = _U_ ( _x_ ) 

by numerical calculation of the convolution and by averaging of the flow velocities between the nodes on each intervals _�xi_ ( _i_ = 1, 2, _. . ._ , 25) only. Because the initial distribution is changed insignificantly and the mass balance is satisfied perfectly, one can suppose that this error is relatively small. Note that for assumed set of data the Peclet number is very high ( _P_ = 17,200) and no other method can ensure the solution of Eq. (7.69) with similar accuracy. 

### **_7.5.4 Solution of the Advective-Diffusive Equation with Source Term_** 

The simplest form of transport equation with source term is as follows: 



296 

7 Numerical Solution of the Advection-Diffusion Equation 



<!-- Start of picture text -->
t Δ x<br>t +Δ t<br>t<br>t −Δ t<br>x                    x                       xi                            i +1                             i +2 x<br><!-- End of picture text -->

**Fig. 7.16** The grid points applied to solve Eq. (7.75) 

The domain of solution (0 ≤ _x_ ≤ _L_ and _t_ ≥ 0) is covered by grid points as in the finite difference method. The mesh having dimensions _�x_ × _�t_ is presented in Fig. 7.16. 

A constant flow velocity _U_ between cross-section _xj_ and _xj_ +1 is assumed. Let us assume that the concentration _f_ is known at all time levels preceding _t_ . It is known at the points _x_ 1, _x_ 2, _. . ._ , _xj_ at time level _t_ + _�t_ as well. The aim is to calculate the concentration _f_ at point ( _xj_ +1, _t_ + _�t_ ). According to Eqs. (7.62) and (7.63) in each time step the following equations should be solved: 



with _f_<sup>(1)</sup> ( _t_ ) = _f_ ( _t_ ) and 



with _f_<sup>(2)</sup> ( _t_ ) = _f_<sup>(1)</sup> ( _t_ + _�t_ ). 

In the first stage the value of concentration at node ( _xi_ +1, _t_ + _�t_ ) resulting from advection and diffusion processes is calculated. For this purpose the following equation is used: 



This integration can be carried out as previously by the trapezoidal rule with the integration step equal to _�τ_ . For the time between the time levels, _fj_ ( _t_ – _τ_ ) is calculated using linear interpolation. 

To cover the distance between the cross-section _xj_ and _xj_ +1 a particle of dissolved matter needs time equal to 



7.5 Solution of the Advection-Diffusion Equation 

297 

During this time the pollutant decays and the effect of this process must be taken into account in the second step of calculation. Namely Eq. (7.77) should be solved. To this end the trapezoidal rule is applied: 



where: 

_j_ – index of cross-section, 

_�T_ – time of particle travelling from cross-section _j_ to _j_ + 1, 

_�t_ –mesh dimension in _t_ direction. 

As the source term is dependent on the concentration _f_ , Eq. (7.80) usually is non-linear. Consequently an iterative method must be applied to solve it. 

### **_7.5.5 Solution of the Advective-Diffusive Equation in an Open Channel Network_** 

The convolution approach can be also applied to solve the transport equation in a channel network, with variable coefficients _U_ and _D_ and lateral inflow. Similarly to the steady gradually varied flow in a network, considered in Chapter 4, the transport equation must be discretized for each branch of the network and additional conditions, resulting from conservation principles, must be imposed at junctions. For a junction of two channels showed in Fig. 7.17a they are: 



whereas for a bifurcation of a channel as in Fig. 7.17b, the following relations are valid: 





<!-- Start of picture text -->
a)  b)<br>j k<br>k<br>j<br>i<br>i<br><!-- End of picture text -->

**Fig. 7.17** Junction ( **a** ) and bifurcation ( **b** ) of the channels ( _arrows_ indicate positive flow direction) 

7 Numerical Solution of the Advection-Diffusion Equation 

298 



Equations (7.81), (7.82a) and (7.82b) allow us to solve the advective-diffusive transport equation for the entire network. 

_Example 7.11_ The SGVF is considered in the looped channel network showed in Fig. 7.18. It consists of 10 branches having trapezoidal cross-sections. The characteristics of the considered network are following: 

- bed width 5.0 m; 

- side slope 1:1.5; 

- bed slope 0.0005; 

- Manning coefficient _nM_ = 0.035; 

- length: channels no 1,2,3,8,9,10 – _L_ = 500 m, channels no 4,5,6,7 – _L_ = 1,000 m. 

Each channel is divided into intervals of constant length _�x_ = 50 m. The total number of nodes is equal to 159. The bed elevation at the upstream end (point _a_ ) is 7,000 m, whereas at the downstream end (point _d_ ) it is equal to 8,500 m. The boundary conditions are specified in terms of water levels at the upstream end (point _a_ ) and at the downstream end (point _d_ ) of network. They are as follows: _Ha_ = 7,750 m, _Hd_ = 7,500 m. 

The results of calculations for the network shown in Fig. 7.18 are presented in Table 7.1. 

Now let us apply the convolution approach to solve the advective-diffusive transport equation for a steady uniform flow in considered channel network. The flow velocity _U_ ( _x_ ) and cross-sectional areas _A_ ( _x_ ) are known since they were calculated previously using the SGVF equation. The initial concentration is assumed equal to zero along all branches of the network. At the beginning of the channel number 1 i.e. at point _a_ (Fig. 7.18), the following function _fa_ ( _t_ ) is imposed: 



<!-- Start of picture text -->
7<br>b c<br>3 9<br>6<br>1 10<br>a d<br>5<br>2 8<br>4<br><!-- End of picture text -->

**Fig. 7.18** Looped channel network 

7.5 Solution of the Advection-Diffusion Equation 

299 

**Table 7. 1** Results of solution for network in Fig. 7.18 

|Channel|Discharge [m<sup>3</sup>/s]|Upstream water<br>level [m]|Downstream<br>water level [m]|
|---|---|---|---|
|1|9,706|7,750|7,575|
|2|4,853|7,575|7,544|
|3|4,853|7,575|7,544|
|4|2,427|7,544|7,536|
|5|2,427|7,544|7,536|
|6|2,427|7,544|7,536|
|7|2,427|7,544|7,536|
|8|4,853|7,536|7,526|
|9|4,853|7,536|7,526|
|10|9,706|7,526|7,500|





It means that a rectangular distribution of concentration is assumed (Fig. 7.19, point _a_ ). 

The functions _f_ ( _t_ ) at the points _b, c_ and _d_ were calculated for the value of diffusion coefficient equal to _D_ = 0.00005 m<sup>2</sup> s<sup>−1</sup> . The source term in the following simplest formula is used: 



where _κ_ =0.00005 s<sup>−1</sup> is the constant of decay. 

In Fig. 7.19 the time distribution of concentration at the selected points of the network displayed in Fig. 7.18 is presented. The travelling rectangular distribution of concentration is simultaneously subjected to smoothing caused by diffusion and reduction of its height caused by the source term. Since the value of diffusion coefficient is very low, one can expect that imposed at the upstream end the rectangular 



<!-- Start of picture text -->
  f F /  m..<br>1 node a<br>0.8 node b<br>0.6 node c<br>0.4<br>node d<br>0.2<br>0<br>0 1 2 3 4 5 6 7 8 t  [h]<br><!-- End of picture text -->

**Fig. 7.19** Advective-diffusive transport of rectangular distribution of concentration in the looped network at its selected points computed with _D_ = 0.00005 m<sup>2</sup> /s and _κ_ = 0.00005 s<sup>−1</sup> 

7 Numerical Solution of the Advection-Diffusion Equation 

300 

distribution of concentration will be smoothed insignificantly. Indeed, in the concentration distributions calculated at points _b_ , _c_ and _d_ one can notice, that only the corners are rounded off although the imposed distribution of concentration travels more than 6 h. It can be also seen that the error generated by the implicit trapezoidal method used to integrate a convolution is very low. The calculations were carried out for _�τ_ = 0.1 s and _�t_ = 100 s. In the considered example the Peclet number (Eq. 7.2) is greater than 750,000. It indicates that advection dominates in the transport process. Note that in the calculated distributions no oscillations, typical for the finite difference or finite element method, are observed. 

The obtained solution presented in Fig. 7.19 seems to be close to the exact one, since in this case the source term has the linear form. Consequently the splitting technique, applied for solution of the transport equation, does not generate any additional error. 

### **References** 

- Abbott MB, Basco DR (1989) Computational fluid dynamics. Longman Scientific and Technical, New York 

Chanson H (2004) The hydraulics of open channel flow: An introduction, 2nd edn. Elsevier, Oxford Cunge J, Holly FM, Verwey A (1980) Practical aspects of computational river hydraulics. Pitman Publishing, London 

Eagleson PS (1970) Dynamic hydrology. McGraw-Hill, New York 

Elliot DI, James A (1984) Models of water quality in rivers. In: James A (ed.) An introduction to 

water quality modeling. Wiley, New York 

Fletcher CAJ (1991) Computational techniques for fluid dynamics, vol. I. Springer-Verlag, Berlin Leonard BP (1979) A stable and accurate convective modelling procedure based on quadratic 

upstream interpolation. Comp. meth. in Appl. Mech. and Engng. 19:59–98 

- LeVeque RJ (2002) Finite volume methods for hyperbolic problems. Cambridge University Press, Cambridge 

- McQuarrie DA (2003) Mathematical methods for scientists and engineers. University Sci-ence Books, Sausalito 

- Patankar SV (1980) Numerical head transfer and fluid flow. Hemisphere Publishing Corpo-ration, McGraw-Hill, Washington 

Press WH, Teukolsky SA, Veterling WT, Flannery BP (1992). Numerical recipes in C. Cambridge University Press, Cambridge 

- Szymkiewicz R (1993) Solution of the advection-diffusion equation using the spline function and finite elements. Commun. Numer. Methods Engng. 9 (4):197–206 

- Szymkiewicz R (1995) Method to solve 1D unsteady transport and flow equations. J. Hydr. Engng. ASCE 121 (5):396–403 

Szymkiewicz R, Weinerowska K (2005) Analytical – numerical approach to solve the transport equation for steady gradually varied flow in open channel. Far East J. Appl. Math. 19 (24): 213–228 

Yanenko NN (1971) The method of fractional steps. Springer New York, Berlin, Heidelberg. 

## **Chapter 8 Numerical Integration of the System of Saint Venant Equations** 

### **8.1 Introduction** 

While the equations describing unsteady flow in open channels were derived by Barré de Saint Venant as early as in 1871 (Chanson 2004), for a long time they could not be used successfully in engineering practice. The reasons for such situation were both mathematical complexity of the equations and specific properties of open channels. To overcome these difficulties the hydrologists were looking for simpler equations describing unsteady flow. The simplifications of Saint Venant equations led to the well known models of kinematic wave and diffusive wave. These equations require less data and they can be solved using simpler methods, sometimes even analytical ones. It is important to note that both simplified equations are still widely applied in hydraulic engineering. 

The equations of unsteady flow, being a system of quasi-linear partial differential hyperbolic equations, need initial and boundary conditions, which in practice can be given in numerical form only. On the other hand the data characterizing the natural open channels are given numerically as well. These circumstances cause that the equations of unsteady flow can be solved only using the numerical methods. Thus it is obvious that wide and effective application of the system of Saint Venant equations in hydraulic engineering was closely connected with the progress in informatics and computer technique. Simply, the numerical approach indispensable in open channel flow modeling was possible because of wide availability of the computers. 

At the very beginning the method of characteristics was used for solving the system of Saint Venant equations. Its detailed description for the flows with free surface is given by Abbott (1979). However, because of some difficulties caused by nonlinearity of equations as well as for required non-equally spaced nodes typical for rivers this method was practically gave up. Currently in open channel modeling the finite difference method dominates. During the last 50 years many difference schemes were proposed. For instance Cunge et al. (1980) present the following list of the numerical schemes possible for solving the system of Saint Venant equations: Lax scheme, leap-frog scheme, Abbot-Ionescu scheme, Delf Hydraulic Laboratory scheme, Vasiliev scheme, Gunaratman-Perkins scheme, Preissmann scheme. The 

301 

R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_8, ⃝C Springer Science+Business Media B.V. 2010 

8 Numerical Integration of the System of Saint Venant Equations 

302 

first two schemes are explicit, the others are implicit. Except the Abbot-Ionecu scheme working on so called staggered grid, all of them use the non-staggered grid. This means that in each node the values of both functions _Q_ and _h_ are calculated. 

It is commonly accepted that the most robust scheme is the four point implicit difference scheme or more precisely – the Preissmann scheme (Abbott and Basco 1989, Cunge et al. 1980). Its alternative name is the box scheme. After Cunge et al. (1980) the reasons of its widespread use are follows: 

- it works on non-staggered grid, which allows us to calculate both unknowns in the same nodes. This is important in natural rivers. 

- it relates the variables coming from neighboring nodes only, what allows us using variable space interval _�x_ without affecting the accuracy of approximation. 

- it ensures approximation of 1st order of accuracy and for particular case of 2nd order. 

- it gives exact solution of the linear wave equations for properly chosen values of _�x_ and _�t_ , making possible the comparison of exact and numerical solutions. 

- it is implicit and absolutely stable so it does not require limiting of the value of time step, whereas the imposed boundary conditions are introduced readily. 

Fascinating history of the box scheme is given by Abbott and Basco (1989). Note, that the box scheme was used in Section 6.1 to solve the pure advection equation. 

As it was mentioned previously, the dominating method for solving of the unsteady flow equations is the finite difference method. The finite element method, very effective for 2D and 3D flow problems, is rather seldom applied in open channel hydraulics. Some attempts (Cooley and Moin 1976) seemed to suggest that this method has no distinct advantages compared to the finite difference method, which did encourage its application. However, modifying the standard finite element method one can obtain a numerical solver for the Saint Venant equations as effective as the Preissmann scheme (Szymkiewicz 1991, 1995). It has the form of an implicit two level six point scheme, which for properly chosen weighting parameters represents even 3rd order of accuracy (Szymkiewicz 1995). 

In the next sections we will present the solution of unsteady flow equations using both mentioned approaches, i.e. the implicit four point difference scheme and the modified finite element method. 

### **8.2 Solution of the Saint Venant Equations Using the Box Scheme** 

### **_8.2.1 Approximation of Equations_** 

Consider the system of Saint Venant equations in the form of Eqs. (1.87) and (1.88): 



8.2 Solution of the Saint Venant Equations Using the Box Scheme 

303 



This system is solved for 0≤ _x_ ≤ _L_ and _t_ ≥ 0. Let us assume subcritical flow in the considered channel reach. In such a case the following initial and boundary conditions must be prescribed: _h_ ( _x_ , _t_ = 0) = _hi_ ( _t_ ) and _Q_ ( _x_ , _t_ = 0) = _Qi_ ( _t_ ) _for_ 0 ≤ _x_ ≤ _L_ , _h_ ( _x_ = 0, _t_ ) = _h_ 0( _t_ ) _or Q_ ( _x_ = 0, _t_ ) = _Q_ 0( _t_ ) and _h_ ( _x_ = _L_ , _t_ ) = _hL_ ( _t_ ) _or Q_ ( _x_ = _L_ , _t_ ) = _QL_ ( _t_ ) for _t_ ≥ 0. 

The solution domain is covered with a grid of dimensions _�xi_ × _�t_ ( _i_ = 1, 2, _. . ._ , _M_ ) as presented in Fig. 4.11. Let us consider a single mesh as in Fig. 8.1, containing 4 nodes ( _j_ − _1_ , _n_ ), ( _j_ , _n_ ), ( _j_ − 1, _n_ + 1) and ( _j_ , _n_ + 1). 

Approximation of the derivative is carried out at point _P_ , which is located in the middle of the interval _�xi_ . Note that the Preissmann scheme corresponds to the box scheme with _ψ_ = 0.5, so point _P_ can move along _t_ axis only, in a way controlled by the weighting parameter _θ_ . 

The value of an arbitrary function _fP_ ( _x_ , _t_ ) at point _P_ is approximated as follows (Cunge et al. 1980): 



where: 

_θ_ – weighting parameter ranging from 0 to 1, 

_j_ – index of cross-section, 

_n_ – index of time level. 



<!-- Start of picture text -->
Δ x<br>t Δ x /2 Δ x /2<br>n +1<br>(1− θ)Δ t<br>P<br>Δ t<br>θΔ t<br>n<br>j                                       j + 1<br>x<br><!-- End of picture text -->

**Fig. 8.1** Grid point for the Preissmann scheme 

8 Numerical Integration of the System of Saint Venant Equations 

304 

Appropriate approximating formulas for the derivatives coincide with those given by Eqs. (6.2) and (6.3) for _ψ_ = 0.5: 



Let us apply these formulas to Eqs. (8.1) and (8.2). The dynamic equation becomes: 



The continuity equation (8.2) is approximated in a similar way: 



In both equations index _P_ means that a function or algebraic expression is approximated accordingly to the formula (8.3). Therefore we have: 



305 

8.2 Solution of the Saint Venant Equations Using the Box Scheme 

In Eqs. (8.6a) and (8.6b) the nodal values of the water levels _h_<sup>_n_</sup> _j_<sup>+1</sup> and _h_<sup>_n_</sup> _j_ +<sup>+</sup> 1<sup>1as</sup> well as the flow rates _Q_<sup>_n_</sup> _j_<sup>+1</sup> and _Q_<sup>_n_</sup> _j_ +<sup>+</sup> 1<sup>1areunknowns.Suchapairofequationscan</sup> be written for each space interval i.e. for _j_ =1, 2, 3, _. . ._ , _M_ − 1. Then we obtain a set of 2( _M_ − 1) algebraic equations with 2 _M_ unknowns, representing the nodal values of function _h_ and _Q_ . Two boundary conditions allow us to complete the system: 

**–** for node _j_ = 1: 



**–** for node _j_ = _M_ : 



In the above equations _δ_ 0 and _δL_ are integer numbers that can take the value of 0 or 1. The value of 1 designates the boundary condition imposed in the form of water stage (function _h0_ ( _t_ ) or _hL_ ( _t_ )), whereas the value of 0 corresponds to the flow discharge (function _Q_ 0( _t_ ) or _QL_ ( _t_ )). 

Finally, the system of non-linear algebraic equations of dimension (2 _M_ × 2 _M_ ) is obtained. This system can be presented in more compact matrix form: 



where: 



The equations of his system are as follows: 









(8.11d) 

The first and the last equation result from the boundary conditions, whereas the other ones represent Eqs. (8.6a) and (8.6b) discretized using the Preissmann scheme. 

306 

8 Numerical Integration of the System of Saint Venant Equations 

The system (8.10) must be solved using an iterative method. For this purpose one can use the Newton method presented in Section 2.3.2. The iteration process has the following form: 



where 



The Jacobian matrix is given as: 



where _N_ = 2 _M_ is the dimension of considered system of equations. 

One can notice that Eqs. (8.6a) and (8.6b) include the unknown values from neighboring nodes only. Therefore in each algebraic equation only 4 unknowns exist. This means that the coefficients related to other unknowns are equal to zero and consequently the Jacobian matrix is banded. Its structure depends on the imposed boundary conditions as shown in Fig. 8.2. 



<!-- Start of picture text -->
a) b)<br>J  = J  =<br><!-- End of picture text -->

**Fig. 8.2** Structure of matrix **J** for the system (8.10) corresponding to _M_ = 5 for various boundary conditions: ( **a** ) _δ_ 0= 1 and _δL_ = 0; ( **b** ) _δ_ 0= 0 and _δL_ = 1 

8.2 Solution of the Saint Venant Equations Using the Box Scheme 

307 

One can see that the bandwidth of the Jacobian matrix is equal to 5. 

The following two issues are related to the numercal solution of the nonlinear system (8.10): 

- initial evaluation of solution, 

- criterion for convergence. 

As the first approximation of searched solution **X**<sup>_(k_=</sup><sup>_0)_</sup> at the time level _n_ + 1 usually the solution obtained for previous level _n_ is assumed, i.e.: 



As a criterion for convergence one can use the following ones: 



where ε _Q_ is the assumed tolerance for the flow discharge _Q_ and _εh_ is the assumed tolerance for the water stage _h_ . Numerical experiments show that usually it is enough to perform 2 ÷ 3 iterations to obtain the accuracy satisfying for practical purposes. 

The Newton method requires that the system of linear algebraic equations is solved in each iteration. To this purpose a modified Gauss elimination or **LU** decomposition algorithm should be used, which takes advantage of the banded matrix. 

The Preissmann scheme involves the weighting parameter _θ_ , which generally ranges from 0 to 1. To recognize the influence of this parameter on the scheme properties a stability analysis is carried out. Since the system of Saint Venant equations is non-linear, then such analysis using Neumann approach is performed for the following linearized system of wave equations: 



where _H_ is a constant (average) depth. Such an analysis was carried out previously in Section 6.1.2 for the pure advection equation solved using the box scheme. In this case the stability analysis, although very similar, is slightly more difficult, because it deals with the system of equations. On the other hand, this analysis has been presented by others authors, e.g. Liggett and Cunge (1975), Cunge et al. (1980), Abbott and Basco (1989). For this reason only the final conclusions are presented here. The Preissmann scheme applied for solving the Saint Venant equations is stable for any Courant number defined as: 



8 Numerical Integration of the System of Saint Venant Equations 

308 

on condition that 



Since this scheme is stable for any Courant number, relation (8.19) constitutes the condition of absolute stability. 

In the afore-mentioned publications one can find analysis of the amplitude and phase errors as well. In next section we will take up an accuracy analysis using the modified equation approach. As we will see this approach can be consider as an alternative way of investigation of the numerical schemes. 

### **_8.2.2 Accuracy Analysis Using the Modified Equation Approach_** 

Accuracy analysis is performed for the linear equations (8.16) and (8.17). Approximation of these equations using the Preissmann scheme with uniformly spaced nodes leads to the following algebraic equations: 



Using the Taylor series expansion the nodal values of function _H_ and _U_ are expressed in terms of their values at node ( _j_ + 1, _n_ + 1) (Fig. 8.1). Taking into account the terms up to 3rd order one obtains: 



8.2 Solution of the Saint Venant Equations Using the Box Scheme 

309 



Similar formulas can be written for the nodal values of function _U_ . Substitution in Eqs. (8.20) and (8.21) and regrouping yields the following modified equations: 



In these equations written for node ( _j_ + 1, _n_ + 1), the node indices were omitted for simplicity. From wave equations (8.16) and (8.17) the following relations are derived: 





8 Numerical Integration of the System of Saint Venant Equations 

310 









These relations allow us to eliminate the time-derivatives of the order higher than one from Eqs. (8.23) and (8.24) and the modified equations take the final form: 



where the coefficient of numerical diffusion _Dn_ and the coefficients of numerical dispersion _En_ 1, _En_ 2 and _En_ 3 are given as follows: 





The Courant number _Cr_ is defined by Eq. (8.18). 

The modified equations (8.35) and (8.36) allow us to draw some conclusions on the numerical properties of the Preissmann scheme: 

1. This scheme applied for solving the unsteady flow equations leads to the system of algebraic equations which satisfies the consistency condition. We can see that for _�x_ , _�t_ →0 all terms at the right handside of Eqs. (8.35) and (8.36) tend to zero. Consequently in the limit the modified equations at each node of the numerical grid become the original wave equation. 

2. The initial-boundary value problem for the modified system of equations limited to the terms of second order (parabolic ones): 

8.2 Solution of the Saint Venant Equations Using the Box Scheme 

311 





is ill posed for _Dn_ <0 i.e. for _θ_ < 1/2. The solution does not exist, which means that the scheme is unstable. The solution problem is well posed if _Dn_ ≥ 0. This happens for _θ_ ≥ 0.5 only. Therefore in such a case the Preissman scheme is absolutely stable. Since at the same time it is consistent, then for _θ_ ≥ 0.5 the scheme is convergent. Note, that this conclusion on stability condition coincides with the conclusion presented previously using the stability analysis. 

3. The diffusive term disappears for _θ_ = 0.5. In such a case the scheme becomes an approximation of 2nd order and consequently it is dissipation free. Therefore in the modified equations at its right side hand the terms of 3rd order, connected with dispersion, dominate. Indeed, for _θ_ = 0.5 we obtain _Dn_ = 0 and simultaneously 





Consequently we can expect unphysical oscillations in the numerical solution. Note that for _Cr_ = 1 both dispersive terms disappear and the modified equations becomes the original equation. In such a case the Preissmann scheme is nondissipative and non-dispersive, producing an exact solution of the wave equations (8.16) and (8.17). 

4. The numerical diffusion will occur for _θ_ > 0.5 giving _Dn_ > 0. It means that the initial-boundary value problem for Eqs. (8.41) and (8.42) is well posed and its solution exists always. Therefore the scheme is absolutely stable regardless of the assumed mesh dimensions and average depth _H_ . However this scheme, being an approximation of 1st order, generates the numerical diffusion which will affect the numerical solution. Its magnitude depends on the values of mesh dimensions and the weighting parameter _θ_ . Therefore the scheme is dissipative. It eliminates the oscillations caused by dispersivity, but at the same time it gives rise to unphysical smoothing, especially significant when strong gradients occur in the solution. 

These conclusions are confirmed by the following numerical example. 

_Example 8.1_ Assume a straight horizontal channel in which the water stays initially at rest with constant depth _H_ ( _x, t_ ) = 0.85 m. At the boundary _x_ = 0 the following function is imposed: 

8 Numerical Integration of the System of Saint Venant Equations 

312 



This boundary condition generates a jump of depth propagating along the channel. The second boundary condition imposed far away from upstream end ( _L_ = 200 m) is: _H_ ( _x_ = _L_ , _t_ ) = 0.85 m. Additionally, it is assumed that _H_ = 0.90 m and _g_ = 10 m/s<sup>2</sup> . For these data the wave celerity is (g· _H_ )<sup>1/2</sup> = 3 m/s. A uniform grid with _�x_ = 1.50 m is used. The results of computations carried out for various values of the Courant number and for various values of the weighting parameter _θ_ are displayed in Figs. 8.3, 8.4 and 8.5. 

They agree with the conclusions resulting from the accuracy analysis. The Preissmann scheme provides exact solution for _Cr_ =1 and _θ_ = 0.5. For other Courant numbers oscillations appear in both _H_ ( _x_ , _t_ ) and _U_ ( _x_ , _t_ ) (Figs. 8.3 and 8.4). Such results could be expected, since for _θ_ = 0.5 and _Cr_ ̸ = 1 the scheme, being dissipation free, becomes dispersive. 



<!-- Start of picture text -->
H  [m]<br>Cr =1.50<br>0.95<br>Cr  =1.00<br>Cr  =0.50<br>0.90<br>0.85<br>0.80<br>0.0 40.0 80.0 120.0 x  [m]<br><!-- End of picture text -->

**Fig. 8.3** Depth _H_ ( _x_ ) at _t_ = 15 s calculated using the Preissmann scheme for _θ_ = 0.50 

**Fig. 8.4** Flow velocity _U_ ( _x_ ) at _t_ = 15 s calculated using the Preissmann scheme for _θ_ = 0.50 



<!-- Start of picture text -->
U [m/s]<br>0.40 Cr  =1.50<br>0.30 Cr =1.00<br>0.20 Cr  =0.50<br>0.10<br>0.00<br>−0.10<br>0.0 40.0 80.0 120.0 x [m]<br><!-- End of picture text -->

8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 

313 



<!-- Start of picture text -->
H  [m]<br>0.95<br>0.90 exact<br>Θ = 0.65 Θ = 1.00<br>0.85<br>0.80<br>0.0 40.0 80.0 120.0 x  [m]<br><!-- End of picture text -->

**Fig. 8.5** Depth _H_ ( _x_ ) at _t_ = 15 s calculated using the Preissmann scheme for _Cr_ = 0.5 

To eliminate the effect of dispersivity some numerical diffusion can be introduced into the solution. Indeed, as it is shown in Fig. 8.5, taking _θ_ = 0.65 we significantly reduce the oscillations, whereas _θ_ = 1.0 eliminates them completely. Obviously, due to this diffusion the sharp discontinuity in _H_ and _U_ gradually disappears. 

The results of calculations should be rather smooth, however without to strong smoothing. The experiences of many authors (for instance Cunge et al. 1980) suggest that the best results are given by the weighting parameter _θ_ close to 0.67, which ensures smooth solution in the case of gentle flood waves. 

### **8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method** 

### **_8.3.1 Spatial and Temporal Discretization of the Saint Venant Equations_** 

Although the finite difference method is dominating in modelling of 1D open channel flow, the finite element method can be applied as well. Moreover, it appears that this method can yield a scheme representing higher accuracy comparing with well known difference schemes. This approach previously used to solve the 1D transport equations in open channel (Szymkiewicz, 1995) can be applied to solve the unsteady flow equations as well. The modification deals with the process of integration and leads to a more general form of algebraic equations approximating the governing equations. 

In Section 6.4 the finite element method was used to solve the advection equation. However to obtain satisfying results the standard version of the finite element 

8 Numerical Integration of the System of Saint Venant Equations 

314 

method had to be modified. This approach yields a six-point implicit scheme with two weighting parameters. Its particular cases are the standard finite element method and the well-known finite difference schemes. An accuracy analysis carried out using the modified equation approach shows that by proper choice of the values of two weighting parameters an accuracy of 3rd order can be obtained. For better understanding the method let us remember some basic information presented previously in Section 6.4. 

Assume a channel reach of length _L_ , which using _M_ nodes is divided into _M_ − 1 elements. According to the Galerkin procedure, described in details by Zienkiewicz (1972) and previously presented in Section 6.4, solution of considered partial differential equation has to satisfy the following condition: 



where: 

_Φ_ – symbolic representation of solved equation, _fa_ – approximation of any function _f_ ( _x_ , _t_ ) occurring in equation, **N** ( _x_ ) – vector of linear basis functions, _L_ – length of channel reach, _j_ – index of node, _M_ – number of grid points. 

For the system of Saint Venant equations the condition (8.44) reads: 





In the standard approach the function _f_ ( _x_ , _t_ ) is approximated as follows: 



where _fj_ ( _t_ ) represents nodal value of function _f_ ( _x_ , _t_ ). When linear basis functions are applied in each element only two following integrals in Eq. (8.44) exist: 

315 

8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 



where _�xj_ is the distance between nodes. Integration of Eqs. (8.45a) and (8.45b) term by term gives a system of ordinary differential equations over time. This procedure has been described in details for the advection equation in Section 6.4. As we remember, such approach appears ineffective. The same is for the Saint Venant equations as well. The standard version of the finite element method does not ensure satisfactory results. Spatial oscillations of the type “2 _�x_ ” are usually observed in the water level and discharge. In Fig. 8.6 an example of oscillating results is displayed. This is a longitudinal profile of the water stages calculated using the standard form of the finite element method. The same can be observed for the discharges as well. Such oscillations are typical for approximation of the advective term using the central difference when the diffusion, physical or numerical, is too weak to counteract local convective instabilities. They should not be regarded as instability in the Neumann sense (Abbott and Basco 1989). The reason of these oscillations is the applied approximation, which for the non-linear terms generates a large number of products of the nodal values of dependent variable (Fletcher 1991). To eliminate the oscillations usually some numerical dissipativity is introduced (see Katopodes 1984). 

As it was shown in Section 6.4, the standard approach can be modified when the linear trial functions are assumed. Namely the integral of the product of approximation of function and basis function in an element can be expressed as a product 



<!-- Start of picture text -->
h  [m]<br>12<br>8<br>4<br>0 10 20 30 40 50 x  [km]<br><!-- End of picture text -->

**Fig. 8.6** Oscillating water level along channel computed using the standard finite element method 

316 

8 Numerical Integration of the System of Saint Venant Equations 

of certain average value of the function in the element and the integral of the basis function in this element. Therefore we have: 





The weighted average values of function _f_ ( _t_ ) in element _j_ are defined as follows: 





where _ω_ is weighting parameter ranging from 0 to 1. Note that assuming _ω_ = 2/3 one obtains the standard finite element method (Eqs. 8.47a and 8.47b), whereas _ω_ = 1/2 corresponds to approximation using the algebraic average taken from the nodal values in an element. This concept applied for open channel unsteady flow and transport equations (Szymkiewicz 1995) appeared effective, since it leads to the scheme having the numerical properties comparable with the finite difference Preissmann scheme. 

Calculation of one integral in expression (8.45a) over an element of length _�xj_ = _xj_ +1– _xj_ is carried out in the following way: 



8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 

317 



In these expressions the subscript _a_ denotes approximation according to formula (8.46) while the subscript _c_ denotes approximation by Eqs. (8.49a) and (8.49b). It can be seen that the proposed modification does not concern the derivatives with regard to _x_ , which are approximated using the standard approach. 

When all integrals in each element are summed up according to Eq. (8.44), the global system of ordinary differential equations over time is obtained: 

**–** for _j_ = 1 



318 8 Numerical Integration of the System of Saint Venant Equations 



**–** for _j_ = 2, _. . ._ , _M_ − 1 





**–** for _j_ = _M_ 



8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 319 



It can be rewritten in the matrix form, typical for the finite element method: 



where: 



The matrices **S** and **C** have dimensions of (2 _M_ ) × (2 _M_ ) with bandwidth equal to 8. 

The system (8.53) is integrated over time using the method (3.71): 



where: 

_θ_ – weighting parameter ranging from 0 to 1, _�t_ – time step, _n_ – index of time level. 

This leads to the system of non-linear algebraic equations: 



The system (8.55) has to be completed by the boundary conditions. They are as follows: 

- at the upstream end of a channel ( _j_ = 1) the water level _h_ 1( _t_ ) or the flow discharge _Q_ 1( _t_ ) for _t_ > 0 are imposed, 

- at the downstream end of a channel ( _j_ = _M_ ) the water level _hM_ ( _t_ ) or the flow discharge _QM_ ( _t_ ) for _t_ > 0 are imposed. 

8 Numerical Integration of the System of Saint Venant Equations 

320 

The system (8.55) has dimensions of (2 _M_ ) × (2 _M_ ), whereas its matrix of coefficients is banded with bandwidth equal to 8. To solve this non-linear system an iterative method like the Newton method has to be used. 

### **_8.3.2 Stability Analysis of the Modified Finite Element Method_** 

Stability analysis is carried out for the simplified linear form of the governing equations, i.e. for the wave equations (8.16) and (8.17). Approximation of this system for the equally spaced nodes ( _�x_ = const.) yields the following system of algebraic equations: 



Note that the considered method corresponds to the mesh presented in Fig. 8.7. The presented method involves two weighting parameters _ω_ and _θ_ . Taking _ω_ = 2/3 the finite element method in its standard form is obtained, whereas for _ω_ = 1 this method coincides with the finite difference one. When _θ_ = 1/2 the method becomes 



<!-- Start of picture text -->
t<br>1 − ω 1 − ω<br>2 ω 2<br>tn + 1<br>(1  ) −θ Δ t<br>Δ t<br>θΔ t<br>tn<br>Δ x Δ x<br>x                          x                           xj − 1                              j                                  j +1 x<br><!-- End of picture text -->

**Fig. 8.7** Numerical grid for the modified finite element method 

8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 321 

the Crank-Nicolson scheme (equivalent to the implicit trapezoidal rule), whereas with _θ_ = 1, it is the implicit Euler scheme. 

The stability analysis is carried out by the Neumann method (Potter 1973). As we know from Section 5.4.3, this approach requires expanding the unknown functions _H_ ( _x_ , _t_ ) and _U_ ( _x_ , _t_ ) in Fourier series and examining the behaviour of its components. Since the system of equations (8.52a) and (8.52b) is linear, then one can examine a single _k_ th component only. According to Eqs. (5.157) and (5.161), this component for both functions _U_ and _H_ are given as: 





where: 

_i_ = (−1)<sup>1/2</sup> , 

_m_ – wave number, 

_ϕ_ = _m_ · _�x_ – dimensionless wave number, _j_ – index of node, _�x_ – spatial mesh dimension. 

The variables _u_<sup>_n_</sup> _k_<sup>and</sup><sup>_hn_</sup> _k_<sup>arethecoefficientsof</sup><sup>_k_thcomponentsattimelevel</sup><sup>_n_.</sup> Since we assumed that only a single component is examined, then index _k_ can be omitted as it was done in Eqs. (8.57) and (8.58). 

Let us multiply both sides of Eqs. (8.56a) and (8.56b) by 2 _�t_ and rewrite them gathering the values from time level _n_ + 1 at left side and from time level _n_ at right side: 





Substitution of Eqs. (8.57) and (8.58) in Eqs. (8.59a) and (8.59b) yields: 

8 Numerical Integration of the System of Saint Venant Equations 

322 





After dividing both equations by the factor _e_<sup>_i_·</sup><sup>_ϕ_</sup> and appropriate transformations one obtains: 

� _(_ 1 − _ω) e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_</sup> + 2 _ω_ + _(_ 1 − _ω) e_<sup>_i_·</sup><sup>_ϕ_�</sup> _h_<sup>_n_+1</sup> + _θ_<sup>_<u>�</u>_</sup> _�_<sup>_<u>t</u>_·</sup> _xH_ <u>�−</u> _e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_</sup> + _e_<sup>_i_·</sup><sup>_ϕ_�</sup> _u_<sup>_n_+1</sup> = =� _(_ 1 − _ω) e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_</sup> + 2 _ω_ + _(_ 1 − _ω) e_<sup>_i_·</sup><sup>_ϕ_�</sup> _h_<sup>_n_</sup> − _(_ 1 − _θ)_<sup>_<u>�</u>_</sup> _�_<sup>_<u>t</u>_·</sup> _xH_ �− _e_<sup>−</sup><sup>_i_·</sup><sup>_ϕ_</sup> + _e_<sup>_i_·</sup><sup>_ϕ_�</sup> _u_<sup>_n_</sup> (8.61a) 



Using the following Euler relations (Korn and Korn 1968): 



Equations (8.61a) and (8.61b) are rewritten as: 



In matrix notation this system of equations can be written as follows: 

8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 

323 



where: 



or in alternative form as: 



The amplification matrix **G** is given by: 



To find this matrix at first let us calculate the inverse matrix **A**<sup>−1</sup> , which is defined as follows: 



where _a_ 11, _a_ 12, _a_ 21 and _a_ 22 are the elements of matrix **A** , whereas _D_ = _a_ 11 · _a_ 22 − _a_ 12 · _a_ 21 is its determinant. Using the Courant number defined by Eq. (8.18) this determinant is written as follows: 



The matrix **A**<sup>−1</sup> is given 



Multiplication **A**<sup>−1</sup> · **B** yields the following elements of matrix **G** : 

8 Numerical Integration of the System of Saint Venant Equations 

324 





The numerical scheme written in general form (8.67) will be stable if the modulus of the greatest eigenvalue of the amplification matrix **G** is not greater than unity. The eigenvalue of matrix **G** can be found directly from its definition (Potter 1973): 



where: 

_λ_ – eigenvalue **I** – identity matrix. 

Condition (8.73) rewritten as: 



leads to the following equation: 



This equation has two roots: 



Substitution of the appropriate expressions into Eq. (8.76) shows that both eigenvalues being complex numbers are identical: 



To rewrite Eq. (8.77) in a more compact form let us introduce a new variable _r_ defined as follows: 

325 

8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 



(8.78) 

Using this relation, after some appropriate manipulations the eigenvalue (8.77) can be reformed to the following form: 



The numerical stability requires (Potter 1972): 



Since _λ_ is a complex number, then the relation (8.80) takes the following form: 



Note that condition (8.81) will be satisfied if only we assume _θ_ ≥ 0.5. On the other hand one can see, that the factor _r_ given by Eq. (8.78) will have the denominator always different from zero for any dimensionless wave number (0 ≤ _ϕ_ ≤ _π_ ), if only _ω_ ≥ 0.5. Summarizing, one can find out that the modified finite element method applied for solution of the linear wave equations is stable for: 





As the relations (8.82) and (8.83) are satisfied for any Courant number, these conditions ensure unconditional stability. The amplitude and phase portraits for the method will be presented in the next subsection. 

### **_8.3.3 Numerical Errors Generated by the Modified Finite Element Method_** 

To examine more exactly the considered numerical method the modified equation approach is used. To carry out an accuracy analysis using this approach all nodal values of functions _U_ and _H_ in the algebraic equations (8.57a) and (8.57b) are replaced 

326 

8 Numerical Integration of the System of Saint Venant Equations 

by Taylor series expansions around the node ( _n_ , _j_ + 1) (Fig. 8.7). Next, the obtained relations are rearranged so that they contain only spatial derivatives. Finally the following system of equations is obtained: 





In Eqs. (8.84) and (8.85) the coefficient of numerical diffusion _Dn_ is given by the expression: 



whereas the coefficients of numerical dispersion _En_ 1 and _En_ 2 are defined as follows: 





The modified equations can be used to deduce practically full information on the numerical properties of the considered method, including consistency and the order of accuracy. 

From relations (8.84), (8.85), (8.86) and (8.87) results that the finite element method does not generate any numerical diffusion for _θ_ = 0.5, i.e. when it represents an approximation of the 2nd order with regard to _t_ . It can be shown that for _ω_ =0.5 and _Cr_ = 1 all terms of 3rd and higher order disappear. In this case the method ensures an exact solution. For _Cr_ ̸ = 1 unphysical oscillations can appear in the solution because of dispersivity ( _Dn_ = 0 and _En_ 1, _En_ 2̸ = 0). The method is unstable for _θ_ < 0.5. In this case we have _Dn_ < 0. It means that the initial-value problem for the system of Eqs. (8.84) and (8.85) limited to the terms of 2nd order is ill-posed and consequently its numerical solution does not exist. Modified finite element method ensures a stable solution for _θ_ > 0.5, because with _Dn_ > 0 the initial-boundary problem for Eqs. (8.84) and (8.85) is well posed and its solution exists always. However, it contains a dissipation error because in this case the method produces a numerical diffusion. It increases with the increase in _�t_ giving rise to smoothing solution and reduction of the pressure gradients. 

As it was shown before, the finite element method represents 2nd order of accuracy with regard to _x_ as well as with regard to _t_ for _θ_ = 0.5 only. For other values of _θ_ this method is only of 1st order of accuracy with regard to _t_ . However the order of accuracy can be further increased. For _θ_ = 0.5 the numerical diffusion is cancelled ( _Dn_ = 0), while the dispersion coefficients are: 

8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 

327 



Note that assuming: 



we obtain _En_ 1 = 0 and _En_ 2 = 0 as well. Therefore with _θ_ = 0.5 and _ω_ given by Eq. (8.89) the terms of 2nd and 3rd order in the system of modified equations (8.84) and (8.85) are cancelled. In this case the proposed version of the finite element method ensures 3rd order accuracy with regard to both _x_ and _t_ . This holds for _Cr_ ≤ 1 only because of the condition of stability (8.82). 

The conclusions presented above can be illustrated by plotting of the eigenvalue modulus of amplification matrix (8.81), which is also known as the amplitude portrait (Abbott and Basco 1989). Since _ϕ_ = _m�x_ = 2 _π_ � _N_ ( _N_ = number of computational intervals _�x_ per wavelength corresponding to the considered component of Fourier series – see Section 5.4.3), the modulus of eigenvalue is a function of _N_ : | _λ_ | = _f_ ( _N_ ). In Fig. 8.8 the moduli of eigenvalues of amplification matrix calculated for _ω_ = 1/2, _Cr_ = 1 and for various values of _θ_ are shown. One can notice that for _θ_ = 0.5 we obtain | _λ_ | = 1. It means that the considered scheme does not change the wave amplitude. It is neither damped nor amplified. For _θ_ < 0.5 one obtains | _λ_ | > 1. In this case the wave amplitude is amplified and consequently the scheme becomes unstable. Note that this situation corresponds to negative values of the coefficient of numerical diffusion _Dn_ . The consequences of this fact were discussed earlier. For _θ_ > 0.5 we obtain | _λ_ | < 1, what means that the amplitude of the propagating wave is 



<!-- Start of picture text -->
λ<br>1.20 Θ = 0.25<br>1.10 Θ = 0.50<br>1.00<br>0.90<br>Θ = 0.75<br>0.80<br>Θ = 1.00<br>0.70<br>0.60<br>0 2 4 6 8 10 12 14 16 18 20 22 24 N<br><!-- End of picture text -->

**Fig. 8.8** Amplitude portrait for different _θ_ 

8 Numerical Integration of the System of Saint Venant Equations 

328 

damped. Therefore the scheme ensures stable solution. However, at the same time it generates numerical diffusion, which affects the propagating wave. As one can see the shorter waves (small value of _N_ ) are more affected than the longer ones. 

The advantages of the proposed approach are better illustrated by the second coefficient of convergence _R_ ( _N_ ) called the phase portrait, which represents the dispersive properties of the scheme. For the considered modified finite element method the phase celerity of considered _k_ th Fourier component is expressed by the following equation: 



Therefore we can find _φ_ as: 



On the other hand, this component propagates with the following exact celerity: 



Then the coefficient of convergence _R_ 2 defined as the ratio of the two celerities, is: 



The factor _r_ given by formula (8.78) expressed in terms of the number of space intervals per wavelength is given as follows: 



Let us calculate the value of tan ( _φ_ ) given by Eq. (8.90) for _θ_ = 0.5, _ω_ = 0.5 and _Cr_ = 1. One obtains: 



Since the dimensionless wave number is _ϕ_ = _m_ � _�x_ then one can write that: 



8.3 Solution of the Saint Venant Equations Using the Modified Finite Element Method 

329 

This relation indicates that each Fourier component propagates with constant speed because the product _m_ · _�x_ is constant for the considered component. Therefore for this case no variation of the wave speed occurs. In other words, the scheme is not dispersive. As for _θ_ = 0.5 it is dissipation free as well, then the assumed set of the parameters: _θ_ =0.5, _ω_ =0.5 and _Cr_ = 1 ensures exact solution of the system of equations (8.16) and (8.17). For other values of _ω_ and _Cr_ the scheme becomes dispersive. 

The plots presenting dispersive properties are shown in Fig. 8.9. First of all one can see that indeed for _θ_ = 0.5, _ω_ = 0.5 and _Cr_ = 1 the coefficient of convergence _R_ 2 is equal to unity for any wave length. The graphs indicate that modification of the finite element method significantly improves its numerical properties. One can notice, that for _ω_ defined by Eq. (8.89) the wave speed of the shortest waves are affected only. There is a remarkable difference comparing with _ω_ = 2/3 (corresponding to the standard version of the finite element method) and with _ω_ = 1 (corresponding to the finite difference method). This is obvious, because the sixpoint implicit scheme with two weighting parameters ensures an approximation of 3rd order with regard to _x_ and to _t_ for _Cr_ ≤ 1. Therefore one can expect that this scheme is able to ensure higher accuracy of the solution, especially when large gradients occur. 

The analysis of numerical properties was carried out for a system of linear equations, while the Saint-Venant equations are nonlinear. Nevertheless, such an analysis seems very useful, since it provides some indications with regard to the stability, dissipation and dispersion of the nonlinear problem. In principle, it is recommended to perform the analysis of the linearized versions of equations to demonstrate the stability of numerical scheme (Fletcher 1991). In practice, the final verification of stability and accuracy can be carried out only by means of numerical experiments. 



<!-- Start of picture text -->
R 2 ω            θ= 0.5,    = 0.5,   Cr = 1.0<br>1.00<br>0.80 ω = 0.625<br>ω = 2/3<br>0.60<br>ω = 1.0<br>0.40<br>0.20<br>0.00<br>0 2 4 6 8 10 12 14 16 18 20 22 24 N<br><!-- End of picture text -->

**Fig. 8.9** Phase portraits for the modified finite element method with _θ_ = 0.5, _Cr_ = 0.5 and for different values of _ω_ 

8 Numerical Integration of the System of Saint Venant Equations 

330 

### **8.4 Some Aspects of Practical Application of the Saint Venant Equations** 

### **_8.4.1 Formal Requirements and Actual Possibilities_** 

When we undertake an attempt to apply the system of Saint Venant equations to model a real flow phenomenon in a river, it is immediately noticed that some requirements resulting from the formal analysis usually cannot be fulfilled directly. For instance, for subcritical flow at the downstream end of a channel the flow discharge or the water stage must be proscribed as boundary condition. However, if we consider a typical river reach this requirement can be fulfilled rather seldom. More often we must find some formulas relating both mentioned functions to use them as equivalent form of required boundary condition. On the other hand, except for artificial prismatic channels, we can have some difficulties with accurate and effective calculation of the cross-sectional parameters especially when they have complex forms and composite roughness. Another problem appears when we try to extrapolate the Saint Venant equations validity applying them beyond the acceptable limits. This happens for instance, when these equations are used to model the river flow, which is actually two dimensional or which is one-dimensional, but rapidly varied. Yet another challenge appear, when we consider unsteady flow in an open channel network with different hydraulic structures inside. One can say generally, that successful implementation of the Saint Venant equations for actual cases of river flow requires overcoming many various difficulties resulting from the difference between real physical worlds and idealized one, assumed during their derivation and solution. 

Many valuable information and recommendations dealing with practical aspects are coming from experiences owing to long time of application of the Saint Veneant equations in hydraulic engineering. For instance, comprehensive explanations and discussions of many practical aspects are given by Cunge et al. (1980). Similar helpful practical recommendations can be found in many chapters of the book edited by Mahmood and Yevjewich (1975). These publications covering practically whole area of the problem, although they were edited years ago, are still valid and valuable for engineers. Some practical advises are available in other publications as well. 

For these reasons below we only briefly discuss some practical questions connected with the implementation of the unsteady flow equations in form of the computer codes supporting hydraulic engineering practice. 

### **_8.4.2 Representation of the Channel Cross-Section_** 

Let us consider the simplest case of unsteady flow, which takes place in a single channel reach as shown in Fig. 8.10a. A natural feature of rivers is their irregular longitudinal and transversal shape. The cross-sections geometry can be measured in the field only at selected, suitable locations. Consequently, the computational crosssections are non-uniformly spaced along the channel axis (Fig. 8.10a). From this point of view both previously described numerical solution methods are suitable, 

8.4 Some Aspects of Practical Application of the Saint Venant Equations 

331 



<!-- Start of picture text -->
Δ x j<br>a)<br>1 j              j +1 M X<br>L<br>b) N<br>Z 1 B j<br>2<br>3<br>A<br>h<br>Z P<br>i<br>        datum<br>Y i Y<br><!-- End of picture text -->

**Fig. 8.10** Discretization of channel reach ( **a** ) and numerical representation of a cross-section ( **b** ) 

since they work on non-uniform grids. The river cross sections are defined numerically by sets of coordinate pairs ( _Yi_ , _Zi_ ) related to a local coordinate system as presented in Fig. 8.10b. 

Numerical solution of the Saint Venant equations requires that the wetted cross sectional area _A_ , wetted perimeter _P_ and top width _B_ are specified as functions of the water stage _h_ . A convenient approach is to tabulate the parameters in each crosssection for _h_ ranging from _Z_ min to _Z_ maxwith appropriate an interval _�h_ . During the computations the actual values of parameters are calculated via linear interpolation: 



where _f_ represents _A_ , _P_ , or _B_ . Sometimes, when the cross-sections are relatively regular, one can approximate them using the standard shapes such as trapezoidal or triangular. Another possible approach is to fit an analytical formula to the tabulated data using the least-square method. In such a situation we have: 



Very often in hydraulic practice compound channel cross-sections are encountered, for example if the river has flood plains as presented in Fig. 8.11. When the water stage exceeds the level of flood plain, the flow process becomes more complicated, since it takes place in parts of the channel having different hydraulic properties. If 1D Saint Venant equations are used to model the unsteady flow they 

8 Numerical Integration of the System of Saint Venant Equations 

332 



<!-- Start of picture text -->
B 0<br>B<br>Ain Ain<br>A<br><!-- End of picture text -->

**Fig. 8.11** Channel of compound section 

should be modified and special treatment of the cross-section is needed. Such modification proposed by Abbott and Ionescu (1967) bases on distinction of two parts of channel cross-section playing different roles in flow process. The first one called active, is connected with the main channel and it is involved in the dynamic equation. The second part of section is called inactive, since it serves as a reservoir, which stocks the water only. This part which together with the active part constitutes the whole area of section, is involved in the continuity equation. 

The original Saint Venant equations are modified as follows: 



It seems that nowadays such approaches for solving the unsteady flow in channel with flood plain became less interesting. Actually, such case of flow should be considered rather as a 2D process with the river bed being partially and temporarily dry. It can be modelled with one of the widely available computer codes for 2D unsteady flow. 

Very often the Saint Venant equations are solved for a storm sewer network. Such system is constituted by closed conduits where the flow is usually free-surface (Fig. 8.12a). However, every now and then, after heavy rain, the conduits are filled 



<!-- Start of picture text -->
a) b)<br>h<br>h<br>datum<br><!-- End of picture text -->

**Fig. 8.12** Flow in closed conduit: ( **a** ) with free surface, ( **b** ) pressurized 

8.4 Some Aspects of Practical Application of the Saint Venant Equations 

333 

**Fig. 8.13** The “Abbott slot” in a channel with dry bed 



<!-- Start of picture text -->
h<br>datum<br><!-- End of picture text -->

to the top and pressurized flow occurs. Since it happens only temporarily one can apply so called “Preissmann slot” (Cunge et al. 1980) shown in Fig. 8.12b. Owing to this concept it is possible to continue the computation using the same mathematical model, i.e. the system of Saint Venant equations. When the water level in conduit reaches its top, then further increasing of pressure does not cause increasing of the cross-section parameters. They are still constant, corresponding to the conduit entirely filled. Assumed width of slot should be relatively small (after Cunge et al. (1980) – of the order of 0.01 m) so that the mass balance remains not affected. 

A similar idea can be also applied in open channels with temporary dry bed. This can arise in the channels of watering systems or in the vicinity of a pump station removing water from the polder. We have to remember that the equations of unsteady flow are valid for positive values of depth. In such a case one can apply a concept opposite to the “Preissmann slot”, called “Abbott slot” (Abbott and Basco 1984). The slot goes down from the level of bottom as presented in Fig. 8.13. This technique allows us to continue the computations even if a channel bed becomes temporarily dry. 

### **_8.4.3 Initial and Boundary Conditions_** 

As explained previously the uniqueness of solution of the system of Saint Venant equations requires us to impose appropriate initial conditions and boundary conditions. 

The initial conditions give information on the state of channel flow at the beginning of the considered time interval, in which the equations will be solved. Their actual form can be different, depending on the considered situation: 

1. In the case of nearly horizontal channel (e.g. in the lower part of a river), one can assume the hydrostatic state. The water is at rest, so the water stages over the entire channel reach are constant, whereas the flow discharge is equal to zero. The flow starts due to the imposed boundary conditions. Such an initial condition is rather unrealistic, but its influence disappears after some time, depending of the celerity of the propagating wave. 

2. If the considered channel is prismatic, then the required water levels can be obtained via solution of the equation for steady uniform flow. For instance for 

8 Numerical Integration of the System of Saint Venant Equations 

334 

given flow discharge the Manning formulae is solved with regard to the normal depth. Alternatively, for given depth using the same formulae one can calculate the flow discharge. 

3. For channels with variable cross-sections the water levels are found via solution of the equations of steady gradually varied flow. This is carried out for flow discharge given at one end of the considered reach. 

4. The initial conditions can be given as the results of computation of unsteady flow carried out previously and stopped at the chosen moment to restart later. 

As far as the boundary conditions are considered, for subcritical flow in a single channel at each end either _Q_ ( _t_ ) or _h_ ( _t_ ) must be specified. It should be remember that specification of the same type of function ( _Q_ or _h_ ) at both ends is not recommended, since in such a case the solution strongly depends of the initial conditions (Cunge et al. 1980). 

At the end through which the water enters the channel reach one function _Q_ ( _t_ ) or _h_ ( _t_ ) must be imposed. They are obtained as the result of observation or as the effect of hydrological forecast for given time period. At the downstream end, through which the water leaves the channel reach, the situation is more complicated. There are only particular cases when the required functions _QL_ ( _t_ ) or _hL_ ( _t_ ) are available. 

If the considered river flows into the sea then at its downstream end one can specify the function _hL_ ( _t_ ) (Fig. 8.14). The water level in the sea is not determined by the river flow but rather by other factors acting on the sea surface, so _hL_ ( _t_ ) is independent information. In a particular case this condition can take the form _hL_ ( _t_ ) = const. 

If a dam is located at the downstream end (Fig. 8.15) then in this section neither flow rate _QL_ ( _t_ ) nor the water stage _hL_ ( _t_ ) are known. 

However we know discharge equation for the spillway, which relates both functions: 



where: 

_QL_ – discharge, _K_ – flow coefficient of the spillway, 



<!-- Start of picture text -->
x  =  L sea<br>Q  tL ( )<br>h L ( t )<br>datum<br><!-- End of picture text -->

**Fig. 8.14** Schematic of river flowing into the sea 

335 

8.4 Some Aspects of Practical Application of the Saint Venant Equations 



<!-- Start of picture text -->
h 0<br>hL hS<br>datum<br><!-- End of picture text -->

**Fig. 8.15** Flow over spillway of a dam 

_LS_ – length of the spillway, _hL_ – water level with respect to assumed datum, _hS_ – elevation of spillway crest above datum. 

Such relation is an appropriate boundary condition, since it closes the final system of algebraic equations, which must be solved to obtain the searched values at the next time level. 

Sometimes the river flows into a lake or reservoir having relatively small dimensions, so the inflow has a significant effect on the water stage in the recipient (Fig. 8.16). In such a case one can use the storage equation, which relates the unknown functions (see Section 1.7): 



where: 

_hL_ – water level in recipient above assumed datum, _F_ – area of recipient at the water level, 

_QL_ – inflow coming from river, 

_q_ – runoff from catchment, 



<!-- Start of picture text -->
E ( ) t P ( ) t F ( h )<br>Q  tL ( )<br>V ( h )<br>h ( t )<br>datum<br>q ( ) t<br><!-- End of picture text -->

**Fig. 8.16** River flowing into the lake 

336 

8 Numerical Integration of the System of Saint Venant Equations 

_E_ – evaporation from water surface, 

_P_ – rainfall at surface of recipient. 

Note, that in this case the additional relation has form of an ordinary differential equation. This equation, together with an appropriate initial condition of the type _hL_ ( _t_ = 0) = _hL0_ ( _hL0_ is given) must be solved simultaneously with the final system of algebraic equations given by the Preissmann difference scheme or by the finite element method. In the latter case this ordinary differential equation is simply incorporated into the system of ordinary differential equations obtained after spatial discretization of the governing equations. 

In most cases, however, the downstream end of the considered channel reach is an ordinary cross-section in which is impossible to know the required function _QL_ ( _t_ ) or _hL_ ( _t_ ). In such a case one can use relation between both mentioned functions in the form of rating curve 



However, such an approach gives rise to some problems. Relation (8.103) is available as single valued function, whereas during the unsteady flow the hysteresis of this function is generated. Therefore introducing of Eq. (8.103) as boundary condition at the downstream end _x_ = _L_ must be considered as a false independent information. To decrease or even to eliminate influence of inappropriate condition, the considered channel reach is artificially extended as in Fig. 8.17). 

Therefore the boundary condition in the form of rating curve instead of _x_ = _L_ is imposed at _x_ = _L_ 1 > _L_ . Singh et al. (1997) examined influence of the new position of downstream end on results computed at _x_ = _L_ . They related the required distance _L_ 1 – _L_ (Fig. 8.17) with the channel properties. 

Alternative relation, which can be used, is the Manning formulae: 



However, this implies the same problems as the previously used rating curve. Then Eq. (8.103) should be rather imposed at the end of extended channel reach. If we set this condition at _x_ = _L_ , variation of the energy line slope should be taken into account. This can be done accordingly to the recommendation given by Fread (1993). It is suggested to compute _S_ using an approximate form of the dynamic equation (8.1). With the finite difference approximation this equation can 

|_x_<br>= 0|_x_<br>_L_<br>=<br>control|_x_<br>_L_<br>=<br>_QL1_(_hL1_)<br>1|
|---|---|---|



**Fig. 8.17** Extending of river reach 

8.4 Some Aspects of Practical Application of the Saint Venant Equations 

337 

be expressed as: 



where: 

_n_ – index of time level, 



This approach accounts for the hysteresis of the relation _Q_ ( _h_ ) existing in the unsteady flow, since in Eq. (8.105) the terms responsible for this phenomenon are included. 

### **_8.4.4 Unsteady Flow in Open Channel Network_** 

Very often in engineering practice we face more complex problem dealing with flow through a channel network. The problem is similar to the one presented in Section 4.4 for the gradually varied flow. As an elementary example let us consider the simplest case of network presented in Fig. 8.18. It consists of 3 branches (a, b and c) and one junction. 

Assume that all branches have the same number of nodes which are numbered as presented. The total number of nodes is 15. 

In such a case, using the finite difference or finite element method, we can set up appropriate systems of algebraic equations for each branch, as it was done previously for a single channel. Next we have to specify the boundary conditions at all ends of the pendant branches of considered network (node 1, 6 and 15). However to obtain the global system for the whole network, which will be solvable, we must introduce additional equations for the channel junction (Fig. 8.19): 

**Fig. 8.18** Channel network containing three arms 



<!-- Start of picture text -->
6<br>7<br>8<br>9<br>b 10<br>11 12 13 14 15<br>5 c<br>a<br>4<br>3<br>2<br>1<br><!-- End of picture text -->

8 Numerical Integration of the System of Saint Venant Equations 

338 

**Fig. 8.19** Junction of three channels 





<!-- Start of picture text -->
j<br>k i<br><!-- End of picture text -->

**Fig. 8.20** Structure of matrix for system of equations for network presented in Fig. 8.18 



<!-- Start of picture text -->
a<br>b<br>c<br><!-- End of picture text -->





The first relation is the continuity equation, whereas latter ones represent a simplified form of energy equation written for junction with the assumption that the head velocities and the local loses are neglected. 

These additional equations close the global system of algebraic equations. For the Preissmann scheme the matrix of coefficients is shown in Fig. 8.20. 

The matrix contains three blocks corresponding to consecutive braches _a_ , _b_ and _c_ , which are linked by additional relations written for junction. Consequently it is very sparse and banded, however its bandwidth is much larger than the one obtained for a single channel (see Fig. 8.2). Note that the bandwidth depends on the numbering of nodes. 

_Example 8.2_ This example deals with unsteady flow through the network of channels shown in Fig. 8.21 (Szymkiewicz 1991). This network is composed of: 

8.4 Some Aspects of Practical Application of the Saint Venant Equations 

339 



<!-- Start of picture text -->
Vistula Lagoon<br>B<br>54 15' No<br>A<br>Jagiellonski<br>Channel E<br>D<br>C<br>lock<br>Michalowo<br>gauge station<br>0        2        4 km<br>Nogat Riv.<br>Lake<br>Druzno<br>o<br>19 30' E<br>Elbląg Riv.<br><!-- End of picture text -->

**Fig. 8.21** Channel network considered in example (Szymkiewicz 1991) 

1. The Elblag River of length 18.7 km, of width 35–64 m (at the water level) and of depth 2.0–4.25 m, connecting the Vistula Lagoon with Lake Druzno. 

2. The Nogat River of length 22.7 km, of width ∼125 m and depth ∼2.5 m, being regulated cut-off arm of the Vistula River. 

3. The Jagiellonski Channel of length 5.73 km, width 36 m and depth 2.70 m connecting both mentioned rivers. 

Unsteady flow in the network is generated mainly by the changes of water level in Vistula Lagoon. These changes caused by wind acting on water surface and having amplitudes of ∼3 m (±1.5 m from the mean sea level) give rise to the flow in variable directions: in or out the lake Druzno. 

The initial condition corresponds to the hydrostatic state of the channel system. For _t_ = 0, _h_ ( _x_ , _t_ ) = _h_ 0= const. and _Q_ ( _x_ , _t_ ) = 0 are assumed. The boundary conditions are specified as follows: 

- At points A and B the function _hL_ ( _t_ ) representing the water level elevation in the Vistula Lagoon is imposed: _hA_ ( _t_ ) = _hB_ ( _t_ ) = _hL_ ( _t_ ); 

- At point C a lock practically cuts off the flow, so _QC_ ( _t_ )∼0; 

8 Numerical Integration of the System of Saint Venant Equations 

340 

- At point D the Elblag River falls into Lake Druzno. At this point neither the function _hD_ ( _t_ ) nor _QD_ ( _t_ ) is known. However, for the lake one can assume equation relating both mentioned functions in the form of the storage equation (8.102). Neglecting the influence of evaporation and rainfall on the lake’s surface, this equation is rewritten as: 



where: 

_hD_ – water level in recipient above assumed datum, 

_F_ – area of Lake Druzno at the water level _hD_ , _QD_ – inflow coming from Elblag River, _q_ – runoff from catchment’s area, 

For Eq. (8.107) the following initial condition is imposed: _hD_ ( _t_ = 0) = _h0_ . 

Lake Druzno is very shallow (mean depth ∼1.20 m) and surrounded by flood banks. Its water surface area varies with water level accordingly to the following function: 



The largest area of the water surface occurs, when the water level in the lake reaches the foot of flood banks. This takes place for _hD_ = 0.30 m. 

The results of calculations for the set of hydrological data coming from time period 11.10.1985 to 18.10.1985 are displayed in Fig. 8.22. The system of Saint Venent equations was solved using the modified finite element method for the following numerical data: _�x_ = 0.700 ÷ 1.000 km, _�t_ = 1,800s. 

_Example 8.3_ This example deals with unsteady flow through the network of channels existing at a real polder in the delta of Vistula River. The considered network is composed of 5 channels as shown in Fig. 8.23. The channels are fed by many small drainage ditches. Next, the water gravitationally flows towards the end of channel number 5. At this point the pump station, equipped with 4 pump units, each of discharge 0.4 m<sup>3</sup> /s, removes the water out of polder. The pump station is controlled automatically When the pumps are working it sometimes happens that the water can be completely removed from some reaches of channels so their beds become partially dry. In such a situation it is necessary to use the “Abbott slot”. This afore mentioned technique allows us to continue the calculations even in the case when the water level temporarily is dropped below the channel bed. 

The initial condition is given by the hydrostatic state of the channel system. It is assumed that at _t_ = 0 the water is in rest with _h_ ( _x_ , _t_ ) = 4.75 _m_ = const. and _Q_ ( _x_ , _t_ ) = 0. The boundary conditions are specified as follows: 

- At the upstream ends of all pendant branches the condition _Q_ ( _t_ ) = 0 for _t_ ≥ 0 is imposed. 

8.4 Some Aspects of Practical Application of the Saint Venant Equations 

341 



<!-- Start of picture text -->
h  [m]<br>1,0<br>observed<br>0,8<br>0,6<br>0,4<br>0,2<br>points ,  A B<br>0,0<br>12               36               60               84               108             132           t   [h]<br>−<br>0,2<br>h  [m]<br>0,8<br>0,6<br>0,4<br>0,2<br>point  E<br>0,0<br>1 2                36               60               84               108             132 t   [h]<br>−<br>0,2<br>h  [m]<br>0,6<br>0,4<br>0,2<br>point  D<br>0,0<br>12               36                60   84   108              132 t   [h]<br>11.10.85 12.10.85 13.10.85 14.10.85 15.10.85 16.10.85 17.10.85<br><!-- End of picture text -->

**Fig. 8.22** Observed and calculated water surface level (Szymkiewicz 1991) 

- At the downstream end of channel number 5 the flow discharge is forced by the pump station, then at this node _Q_ ( _t_ )= _Q_ pump( _t_ ) is specified. This function can change with a jump equal to 0.40 m<sup>3</sup> /s ranging from 0 to 1.6 m<sup>3</sup> /s. 

- All channels are fed by lateral inflow caused by rainfall. 

The system of Saint Venent equations was solved using the finite element method for the following numerical data: _�x_ =0.700 ÷ 1.000 km, _�t_ = 360 s. 

8 Numerical Integration of the System of Saint Venant Equations 

342 

**Fig. 8.23** Polder’s open channel network 



<!-- Start of picture text -->
2 5<br>3<br>1<br>4<br><!-- End of picture text -->

The result of calculations displayed in Figs. 8.24 and 8.25 show the flow profiles in channels 2 and 4 plotted for selected times. One can see that working pumps remove systematically the water from polder so the water level is decreased. After 12 h the lower part of channel 4 becomes dry. The length of this part is increasing. The same is observed in the upper part of channel 2. However the computations are continued successfully thanks to the applied “Abbott slot”. 



<!-- Start of picture text -->
h  [m]<br>5.00<br>t  = 0<br>4.75<br>t  = 3 h<br>4.50<br>t  = 6 h<br>4.25<br>t  = 12 h<br>4.00 t  = 18 h<br>3.75<br>botom<br>3.50<br>−2.5 −2.0 −1.5 −1.0 −0.5 0.0 x  [km]<br><!-- End of picture text -->

**Fig. 8.24** The water profiles in channel 2 



<!-- Start of picture text -->
h [m]<br>5.0<br>t  = 0<br>4.5<br>t = 3 h<br>4.0 t = 6 h<br>t = 12 h<br>3.5<br>t  = 18 h<br>3.0<br>−1.25 −1.00 −0.75 −0.50 −0.25 0.00 x [km]<br>bottom<br><!-- End of picture text -->

**Fig. 8.25** The water profiles in channel 4 

8.5 Solution of the Saint Venant Equations with Movable Channel Bed 

343 

### **8.5 Solution of the Saint Venant Equations with Movable Channel Bed** 

### **_8.5.1 Full System of Equations for the Sediment Transport_** 

In preceding sections of this chapter we considered unsteady flow in open channel assuming that the channel bed is fixed. In fact there is mutual relation between the flowing water and the bed. Since in alluvial stream its bed is built of mineral grains then sufficiently large flow velocity forces their movement. They are washed away and, depending of their dimensions and the flow characteristics, they move as suspended in the water or they are transported along the bed in direction of flow (Fig. 8.26). The first kind of solid transport is called suspended-load, whereas the second one is called bed-load (Yalin and da Silva 2001). The motion of each kind of sediment is governed by different transport mechanisms. 

When the bed material is washed it is said the erosion takes place. If the forces which cause movement of the grains are decreasing, then they settle. In such a case it is said that deposition takes place. Both processes change the flow conditions in a stream influencing the sediment transport as well. This suggests that taking into account the sediment transport we improve description of the flow process in open channel. However as a matter of fact the problem of sediment transport is one of the most complicated and challenging tasks for both scientists and engineers. This is caused by 3D spatially and random character of main factors determining solid transport. The readers who are interested in this problem can find many important publications presenting theoretical and practical aspects of problem (Yalin and da Silva 2001, Chanson 2004 among others). Some software packages, sometimes very sophisticated, supporting engineering practice, are available as well. In this section we will present some basic aspects of computation unsteady flow in channels with moving bed. These considerations will be limited to the 1D case only. 

The modeling is based on the sediment transport continuity equation. In its general form this equation is derived from the mass conservation principle applied for control volume limited by control surface during two phase unsteady motion. The 

**Fig. 8.26** Schematic representation of sediment transport zones: from 0 to _a_ – bed load, from _a_ to _H_ – suspended load 



<!-- Start of picture text -->
z<br>H<br>qs suspended load<br>a<br>qb<br>bed load<br>0<br>x<br><!-- End of picture text -->

8 Numerical Integration of the System of Saint Venant Equations 

344 

one-dimensional form of this equation can be expressed as follows: 



where: 

_x_ – space co-ordinate, 

_t_ – time, 

_Z_ – bed elevation above the assumed datum, 

- _q_ – total (suspended and bed load) specific volumetric rate, 

- _p_ – porosity. 

For the first time this equation was derived by Exner (Cunge et al. 1980, Yalin and da Silva 2001) as a result of investigation of the bed forms. Equation (8.108) allows us to describe the evolution of the longitudinal bed profile in time, _Z_ ( _x_ , _t_ ). The variable _q_ represents the sediment discharge rate and depends on the bed material and flow parameters. In the derivation of Eq. (8.108) the following assumptions were made: 

- Lateral inflow of sediment does not exist, 

- Distribution of the flow velocity and sediment concentration is uniform over the cross-section (Fig. 8.27), 

- sediment travels in the direction of _x_ axis ( _q >_ 0) and sediment transport per unit channel width is uniform 



where _U, C_ are averaged flow velocity and concentration over cross-section, 



<!-- Start of picture text -->
a) b) c)<br>z z z<br>u ( z ) c ( z )<br>H ( x t , )<br>−<br>( 1 p )<br>Z ( x t , )<br>x u c<br>Q ( x , ) t<br>q ( x , t )<br><!-- End of picture text -->

**Fig. 8.27** Sketch of open channel reach: ( **a** ) longitudinal profile, ( **b** ) velocity distribution, ( **c** ) concentration distribution 

8.5 

345 

Solution of the Saint Venant Equations with Movable Channel Bed 

- total specific volumetric rate represents the combined effect of the suspended load _qs_ and the bed load _qb_ 



Generally this equation takes into account both suspended load and bed load although the time derivative of the suspended load was neglected (see for instance Yalin and da Silva 2001). 

There are many formulas for determining the bed load rate _qb_ (see for example: Chanson 2004). One of the most frequently used is the empirical formula of MeyerPeter and Muller, based on the results of field experiments: 



where: 

_qb_ – specific volumetric bed-load per 1 m of channel width [m<sup>3</sup> /s·m], γ _s_ , γ _w_ – specific weight of sediment and water respectively [N/m<sup>3</sup> ], 

_R_ – hydraulic radius , 

_S_ – energy grade line slope, 

_dm_ – typical grain size (usually _d_ 50), 

_kd_ – Strickler coefficient being the inverse of Manning coefficient _nM_ : 



_ks_ – granular roughness of bed surface given by: 



Let us integrate the Exner equation (8.108) over a channel reach of length _L_ : 



Note that the net flux of sediment material through the endpoints _x_ = 0 and _x_ = _L_ which bound channel reach causes changes of bed position (Fig. 8.28). Erosion will occur when the flux through the upstream end is less than one through the downstream end, i.e. 



346 

8 Numerical Integration of the System of Saint Venant Equations 

**Fig. 8.28** Erosion and deposition caused by the net sediment material flux 



<!-- Start of picture text -->
z<br>q(x = 0,t) q(x = L,t)<br>H(x,t)<br>+ deposition<br>z = 0<br>– erosion<br>Z(x,t)<br>x = 0 x = L x<br><!-- End of picture text -->

Conversely, deposition will take place when: 



Assume that the solution of the Exner equation is a continuous function. This allows us to express Eq. (8.108) as follows: 



Introduction of a new variable: 



gives an alternate form of Eq. (8.117): 



One can see that the Exner equation is a nonlinear advection equation with advective velocity _C_ ( _Z_ ). This velocity defines how quickly any disturbance of bed elevation propagates. Since the advection velocity is positive then each disturbance will propagate towards the downstream end. Of course for constant _C_ any bed form will travel without shape deformation. 

In the Exner equation the specific volumetric bed-load _q_ or the advective velocity _C_ depend on the hydraulic parameters of flowing stream, i.e. discharge rate and depth. These parameters are available from the solution of unsteady flow equations. For this purpose we must use the Saint Venant equations discussed previously. Neglecting the lateral inflow and introducing the depth _H_ ( _x_ , _t_ ) as dependent variable we obtain from Eqs. (1.87) and (1.88): 

8.5 Solution of the Saint Venant Equations with Movable Channel Bed 

347 



Note that in this case the bed elevation above the assumed datum _Z_ , being a function of _x_ co-ordinate and time _t_ , is an additional dependent variable. Therefore the system of Saint Venant equation must be completed with additional equation, i.e. with the previously presented Exner equation. In such a way one obtains a system of three partial differential equations. Simplified forms of the sediment transport model were also proposed – see e.g. Cunge et al. (1980). 

### **_8.5.2 Initial and Boundary Conditions for the Sediment Transport Equations_** 

The equations describing the unsteady sediment transport should be solved for appropriately imposed auxiliary conditions on the limits of the following domain of integration: 0 ≤ _x_ ≤ _L_ and _t_ ≥ 0. The auxiliary conditions for the sediment transport model can be properly specified on condition that the structure of characteristics of considered system is well recognized. To this end let us consider the system of Saint Venant equations in the form of Eqs. (1.77) and (1.78) completed by the Exner equation written in the form of Eq. (8.119). Then we have: 





A similar analysis was presented by Cunge et al. (1980). These authors used the Exner equation in the form of Eq. (8.108). We apply a slightly different approach, which will allow us to provide the equations of characteristic directions explicitly. 

To find of the characteristics it is required at first to rewrite the system (8.122) in matrix notation. This system should be presented in the form of Eq. (5.14). Next the condition (5.15) is used. For the system (8.122) this condition takes the following form: 



8 Numerical Integration of the System of Saint Venant Equations 

348 

Equation (8.123) leads to equation which determines the characteristics of system. Expanding the determinant (8.123) yields: 



This equation is of third degree with regard to _dx_ / _dt_ . Its roots determine the characteristics of system (8.122). To find all roots it is helpful to notice that the polynomial (8.124) has, among others, the following real root: 



Thus Eq. (8.124) can be expressed as a product of two polynomials of lower degrees. Dividing this polynomial by the following one: 



yields its equivalent form: 



The obtained polynomial of 2nd degree is well known. It has been obtained previously (Eq. 5.24), while analyzing the characteristics of the Saint Venant equations. Its two real roots are given by Eqs. (5.26a) and (5.26b). Therefore Eq. (8.127) can be rewritten in the following form: 



From this equation results that polynomial (8.124) has three following roots: 



These roots determine three families of characteristics of the considered system (8.122). Since all of them are real, the system is of hyperbolic type. 

The problem of solution of the system (8.122) will be well posed if appropriate initial and boundary conditions on the limits of solution domain are prescribed. In 

8.5 Solution of the Saint Venant Equations with Movable Channel Bed 

349 

Chapter 5 we found out, that for the hyperbolic equations the following rule is valid: at every boundary of the considered solution domain it is necessary to impose as many additional conditions as many characteristics enter the solution domain from this boundary. Taking into account this rule and Eqs. (8.129a), (8.129b) and (8.129c) for subcritical flow � _U <_<sup>√</sup> _<u>g</u>_ <u>·</u> _<u>H</u>_ <u>�</u> we must impose: 

- The initial conditions in the form of three functions: _H(x, t_ = 0 _)_ = _Hi(x_ ), _Q(x, t_ = 0 _)_ = _Qi(x)_ and _Z(x, t_ = 0 _)_ = _Zi(x)_ for 0 ≤ _x_ ≤ _L_ , since three characteristics are going through the time boundary _t_ = 0; 

- The boundary conditions in the form of two functions (one for flow and one for sediment transport) at the upstream channel end and one function (for flow only) at the downstream end. 

For supercritical flow � _U <_<sup>√</sup> _<u>g</u>_ <u>·</u> _<u>H</u>_ <u>�</u> the same initial conditions must be prescribed, whereas the boundary conditions are defined in another way. At the upstream end all three functions must be imposed while at the downstream end the boundary condition is not specified at all. 

If the sediment transport in open channel network is considered then additional equations have to be introduced for the junctions of channels. They are analogous to those presented in Section 4.4.2. 

### **_8.5.3 Numerical Solution of the Sediment Transport Equations_** 

There are two main ways of numerical treatment of the system of sediment transport equations (Cunge et al. 1980). In the first approach the system constituted by the Saint Venant equations (Eqs. 8.120 and 8.121) and the Exner equation (Eq. 8.119) is solved as three coupled equations, with imposed initial and boundary conditions. All three equations are approximated using the finite difference or element technique leading to the global system of algebraic equations. Usually the difference box scheme is applied. This scheme is particularly suitable for this purpose as it works well for both the Saint Venant equations (Preissmann scheme – see Section 8.2) and the pure advection equation (see Chapter 6). Of course the final system of algebraic equation given by this approach is larger than the one obtained for the Saint Venant equations. 

Another possible approach, allows us to decrease the computational effort by splitting the considered problem in each time step into two smaller problems. The governing system of equations is uncoupled and in each time step the equations for unsteady flow and one for the sediment transport are solved separately but simultaneously. Then we have to use directly the solution techniques presented in the preceding sections of this chapter for the unsteady flow as well as those for the pure advection equations described in Chapter 6. Usually for both problems the same grid points should be used. In such a way in each time step instead of one relatively large system of algebraic equations two much smaller systems are solved. 

350 

8 Numerical Integration of the System of Saint Venant Equations 



<!-- Start of picture text -->
a) b)<br>Z ( t ) Z ( t +Δ t )        datum Z ( t ) Z ( t +Δ t )<br><!-- End of picture text -->

**Fig. 8.29** Possible distribution of settled sediment over trapezoidal cross-section: deposition of sediment on the bottom only ( **a** ) and on the bottom and sides ( **b** ) 

The problem of great importance is the relation between the volumetric sediment rate which gives rise to erosion or deposition and time deformation of the shape of channel’s cross-sections. Various approaches are possible (Cunge et al. 1980). For the simplest case as in prismatic channel one can assume that the whole sediment is eroded from or deposed at the bottom only (Fig. 8.29a) or it is distributed over the bottom as well as over the channel sides (Fig. 8.29a). The problem of sediment distribution becomes more complex for an arbitrary shape of the channel cross-section. 

_Example 8.4_ A channel reach of length _L_ = _5_ 0 km and of bed slope _s_ = 0.4·10<sup>−3</sup> is ended by a dam. Assuming that the channel is rectangular of width _B_ = 50 m and of Manning roughness coefficient _nM_ = 0.025, compute the time evolution of the bed elevation _Z_ ( _x_ , _t_ ) in the reservoir caused by the transported sediment. 

The sediment flow rate is calculated using the Meyer-Peter formulae (8.111) for sand characterized by typical grain size _dm_ = 1 mm, whereas the porosity is assumed to be _p_ = 0.4. The system of Saint Venant equations (8.120) and (8.121) and the Exner equation (8.108), are solved uncoupled using the Preissmann scheme. 

The initial conditions at _t_ = 0 are determined assuming steady gradually varied flow with constant discharge _Qi(x)_ = 330 m<sup>3</sup> /s for 0 ≤ _x_ ≤ _L_ . The flow profile _h_ ( _x_ , _t_ = 0) is found from the solution of the steady gradually varied flow equation (Eq. 4.2) with the initial condition _h_ ( _x_ = _L_ ) = 10 m being the water level close to a dam. It enables us to define the initial flow depth _H_ ( _x_ , _t_ = 0) for the assumed initial bed profile _Zi_ ( _x, t_ = 0). 

At _x_ = 0 two following boundary conditions are assumed: 

**–** flow rate given by the formulae 



with _Qm_ = 1,150 m<sup>3</sup> /s and _tm_ = 25 days is imposed. **–** bed elevation during the transition of the flood wave given by 

351 

8.6 Application of the Saint Venant Equations for Steep Waves 



<!-- Start of picture text -->
H ,  Z  [m]<br>24<br>22<br>20<br>18<br>16<br>14<br>12 dam<br>10 t  = 300 days<br>8 t  = 200 days<br>6 initial bottom t  = 100 days<br>4<br>2<br>0<br>0 10 20 30 40 50 x  [km]<br><!-- End of picture text -->

**Fig. 8.30** Evolution of the bed elevation in reservoir due to transported sediment 



where the assumed peak value _Zm_ = 0.5 m corresponds to time _tm_ . 

At the downstream end _x_ = _L_ , where a dam exists, a constant water level _h_ ( _x_ = _L, t_ ) = 10 m is imposed. 

The channel reach is divided into intervals of constant length _�x_ = 1,000 m. The computations are performed for the time step _�t_ = 2,200 s with the value of weighting parameter _θ_ = 0.65 (see Sections 6.2 and 8.2). The computed results are displayed in Fig. 8.30. 

Note that the obtained results represent qualitative agreement with observed effects of grains settlement in the reservoir. Systematical decrease of the flow velocity in the reservoir towards a dam increases deposition of solid material transported by the river. Consequently the reservoir is loosing its usable storage with time, since it is continuously fulfilled by entering sediment. 

### **8.6 Application of the Saint Venant Equations for Steep Waves** 

### **_8.6.1 Problem Presentation_** 

The system of Saint Venant equations was derived with the assumption that the flow is gradually varied. However in many cases we face another type of flow. Sometimes the flow profile in open channel varies locally so rapidly that in fact a discontinuity occurs. Such very steep wave in the form of surge can occur in many circumstances. 

352 

8 Numerical Integration of the System of Saint Venant Equations 

**Fig. 8.31** Propagating wave with discontinuity 



<!-- Start of picture text -->
U<br>L<br>R<br>x  =0 x<br><!-- End of picture text -->

For instance, the wave of surge type can be generated by the operation of hydro– power plant, when the turbines are started or stopped suddenly. Another reason of surges can be sudden opening or closing of a gate. The water waves arising in such situations can be idealized as in Fig. 8.31. 

Similarly, very steep wave in the form of surge can occur when a tide enters the river mouth. Usually the surge generated by tide is termed a bore (Chanson 2004). The difference in nomenclature does not mean the differences in principles of propagation of bores and surges. Another type of shock wave occurs when a dam separating different water levels is suddenly removed. Analytical analysis of idealized propagation of bore and dam-break wave is given by Billingham and King (2000). 

For those types of steep waves the system of Saint Venant equations is formally not valid, since in its derivation the vertical acceleration has been omitted. Note that not every wave caused by dam-break has to be considered as strictly unsteady flow with discontinuities. Since the formation of the breach (the opening in a dam which forms as a dam fails) needs some time, the outflow from reservoir is more evenly distributed in time (French 1985). This fact makes reasonable using even such a simple model as the storage equation (1.120). Such approach was proposed and developed by Fread (1993). 

On the other hand, in hydraulic engineering when the main subject of interest is flow considered in large scale, the local untypical phenomena can be less important and their internal structure may be neglected. For instance, although the internal structure of the hydraulic jump can be effectively reproduced by solving the Reynolds averaged Navier-Stokes equations and continuity equation completed with the appropriate model of turbulence (Cippada et al. 1994), such approach is not applied in open channel flow modeling. As the length of the hydraulic jump is small comparing with the spatial dimension of practically applied grid, it is spatially reduced to a point, in which the water surface is discontinuous. It appears that with such approach the Saint Venant equations can be used as an effective model of flow. However some additional conditions are required. 

First of all the system of unsteady flow equations must be expressed in particular, so called conservative form. This means that the form of equations have to satisfy the 

353 

8.6 Application of the Saint Venant Equations for Steep Waves 

integral form of conservation principles, from which they were derived. Note that the system of Saint Venant equations can be written in integral form as well as in differential form (Chanson 2004, Cunge et al. 1980). Both representations are equivalent as long as smooth solutions are considered. The difference becomes noticeable when discontinuities occur. In Chapter 1 the Saint Venant equations have been derived directly from the fundamental differential equations of the fluid mechanics and we used them in the differential form. However one can expect that the differential equation does not hold near discontinuity in the solution (LeVeque 2002). 

The second condition concerns the applied numerical method. It is assumed that standard finite difference methods based on the Taylor series expansion, can break down near discontinuity arising in the solution (LeVeque 2002). An appropriate method should ensure required solution accuracy. Particularly it is expected that the considered conservation principles will be satisfied on the numerical grid. This requirement is satisfied particularly exactly by the finite volume method based on the equations written in integral form. However, to solve successfully some flow problems of shock wave type one can use the finite difference methods as well. The flow of shock wave type means that we consider flow with large gradients rather than containing pure discontinuity. 

### **_8.6.2 Conservative Form of the Saint Venant Equations_** 

Let us remember the system of the Saint Venant equations (1.77) and (1.78) obtained for a wide rectangular channel and written per unit width: 





where: 

_x_ – space co-ordinate, 

_t_ – time, 

_U_ – cross-sectional average flow velocity, 

_H_ – flow depth, 

_s_ – bed slope, 

_S_ – energy grade line slope’ 

_g_ – acceleration due to gravity. 

Equations (8.132) and (8.133) represent the mass and momentum conservation laws respectively. These so called the 1D shallow water equations with source term are written in the non-conservative form. It means that these equations do not satisfy the integral form of conservation law from which they were derived. 

354 

8 Numerical Integration of the System of Saint Venant Equations 

By a simple transformation the equations (8.132) and (8.133) can be reformed to the following equivalent conservative form: 





To show the difference between both forms of the Saint Venant equations let us integrate the continuity equation (8.132) with regard to _x_ over considered channel reach of length _L_ . Integration performed by parts leads to the following expression: 



Similar integration of Eq. (8.134) over considered channel reach this time gives: 



Comparing Eq. (8.136) with Eq. (8.137) we notice that although in both cases the continuity equation was integrated the obtained results differ significantly. Equation (8.137) expresses strictly the law of mass conservation, since it shows that time variation of water capacity stored by a channel reach of length _L_ is caused by the net flux through its endpoints only. We conclude that the continuity equation (8.134) is written in the conservative form. Conversely, Eq. (8.132) is not written in the conservative form since Eq. (8.136) obtained by its integration does not represent the mass conservation principle. Besides the first two terms at right hand side representing net flux through the channel endpoints, we have additional terms written in brackets. The same is for the dynamic equation. Consequently, if we integrate numerically the system (8.132) and (8.133) the errors in the mass and momentum balances can occur. These errors, being insignificant for smooth solution, can be appreciable when strong gradients occur, particularly when the discontinuities in solution arise. 

A rough evaluation of the difference between conservative and non-conservative forms of the 1-D shallow water equations can be carried on the example of the numerical solution of the dam break problem. We shall consider an idealized case of dam break when the vertical wall separating two different water levels in a channel is suddenly removed. For simplicity we will solve the homogeneous version of the 

355 

8.6 Application of the Saint Venant Equations for Steep Waves 

systems (8.132) and (8.133) as well as of (8.134) and (8.135). It means that the unsteady flow will take place in a horizontal and frictionless channel. 

_Example 8.5_ Let us solve subsequently the following systems of equations: 





and 





where _q_ = _U_ / _H_ is the flow rate per unit channel width. A wide rectangular channel reach of length _L_ is divided into two parts by the dam located at its mid-length _x_ = _L_ /2 (Fig. 8.32). 

Both systems will be solved for the same initial and boundary conditions corresponding to the dam-break problem. They are specified as follows: 

- at _t_ = 0 the water is at rest filling the channel up to _Hu_ = 3.0 m above the bottom at the left side of the dam (0 ≤ _x_ ≤ _L_ /2) and up to _Hd_ = 0.5 m above the bottom at its right side ( _L_ /2 < _x_ ≤ _L_ ); 

- at the upstream end _x_ = 0 the flow depth is constant and corresponds to the initially imposed value: _H_ ( _x_ = 0, _t_ ) = 3.0 m for _t_ ≥ 0; 



<!-- Start of picture text -->
dam<br>Hu<br>Hd<br>0 L / 2 L<br><!-- End of picture text -->

**Fig. 8.32** Initial water levels at both sides of the dam 

356 

8 Numerical Integration of the System of Saint Venant Equations 

- at the downstream end _x_ = _L_ a constant depth corresponding to the initial one _Hd_ is imposed: _H_ ( _x_ = _L_ , _t_ ) = 0.5 m for _t_ ≥ 0 ( _L_ is assumed large enough that the downstream end will not be reached by propagating wave). 

Both systems of equations are solved using the difference Preissmann scheme, which in Section 8.2 was applied for solving the system of Saint Venant equations for non-prismatic channel. The computations carried out for _L_ = 1,250 m, _�x_ = 0.5 m, _�t_ = 0.10 s and _θ_ = 0.67 confirmed that appreciable difference between the conservative and non-conservative forms of solved equations exists. Evaluation of this difference is performed in terms of the balance of the water volume stored in considered channel, which must be constant during the flow process. After very short time _t_ = 120 s the system written in the non-conservative form generates the balance error of magnitude ∼0.18%, whereas for the system in conservative form this error practically does not exist. 

The mass and momentum balance errors can be avoided on condition that the non-linear equations of unsteady flow will be written in proper conservative form. This is true for all non-linear transport equations. Comprehensive discussion on the solution of non-linear hyperbilic equations is presented for instance by LeVeque (2002), Gresho and Sani (2000) and by others. We will continue this issue in Chapter 9, while discussing the simplified forms of the unsteady flow equations. 

### **_8.6.3 Solution of the Saint Venant Equations with Shock Wave_** 

When in the considered case of flow discontinuities appear, the computation should be carried out very carefully. First of all, as it was stated previously, the Saint Venant equations must be expressed in the conservative form. Secondly, their solution needs a particular numerical approach. Cunge et al. (1980) present three possible techniques. 

The first approach, called the shock fitting method, treats the problem of discontinuity propagation and the unsteady flow between the discontinuities separately. Positions of the traveling discontinuities are calculated using the method of characteristics, whereas the Saint Venant equations which hold in the regions limited by discontinuities, are solved using the standard methods. 

The second possible approach, called pseudoviscosity method, requires introduction of a diffusive term into the dynamic equation. This term, having smoothing properties, allows us to control the solution near discontinuity. Its particular form relating intensity of generated diffusion with the wave steepness ensures that this extra term acts strongly only locally, being insignificant far away from the discontinuity. This approach is applicable for non-dissipative schemes. More information on the pseudoviscosity method is given by Potter (1973) and Cunge et al. (1980). 

The last possible approach listed by Cunge et al. (1980) bases on the solution using the dissipative methods. In this approach is assumed that the process of smoothing is ensured by the numerical diffusion generated by the applied scheme. 

357 

8.6 Application of the Saint Venant Equations for Steep Waves 

Controlling artificial diffusion one can obtain an acceptable solution. Such technique was applied in Example 8.5 in which the problem of propagation of the shock wave caused by the dam break has been solved using the Preissmann scheme. 

The disadvantage of the presented approaches is that they base on the differential equations. This can be avoided by using the finite volume method. The finite volume method has two important features. Firstly, it ensures very good conservation of the transported quantity since it uses the flow equations in the integral form. Secondly, it ensures a relatively simple discretization of complex domain of solution. Of course, in the 1D problem as considered here the last mentioned advantage is not appreciable, whereas it arises distinctly in 2D and 3D problems. 

The finite volume method appears effective tool for solving the propagation of shock waves particularly for extreme auxiliary conditions. However it deals with rather idealized situation, when the homogenous equations are solved. Unfortunately the method cannot be simply implemented for more realistic cases. Presence of the source terms in form of the bed and grade line energy slope requires applying of non-trivial approaches to overcome occurring difficulties. Interesting discussion on the finite volume method is presented by Gresho and Sani (2000). Detailed description of the method and its implementation for solution of the 1D shallow water equations is given by LeVeque (2002) among others. This rather complicated algorithm is not presented here, but at the end of this section an example of solution of the dam break problem using the finite volume method will be presented. 

The results presented in the last example were obtained using the Preissmann scheme. We know that this classical scheme is a reliable tool for solution of the Saint Venant equations when they are applied for unsteady gradually varied flow. On the other hand, as it was mentioned previously, the differential representation of the flow problem is not valid near a discontinuity. Nevertheless, the Saint Venant equations solved by the classical dissipative schemes are frequently applied (Cunge et al. 1980). As a consequence of this discrepancy the standard schemes appear less reliable than for gradually varied flow. Some computational aspects are illustrated by the presented example. 

_Example 8.6_ Solve the system of equations (8.140) and (8.141) in a wide rectangular channel of length _L_ for the initial and boundary conditions corresponding to surge propagation. They are specified as follows: 

**–** at _t_ = 0 the water is at rest filling the channel up to _H_ 0 = 0.75 m above the bottom; **–** at the upstream end _x_ = 0 the flow rate is suddenly increased from 0 to 5 m<sup>3</sup> /s/m: 



> **–** at the downstream end _x_ = _L_ a time constant depth corresponding to the initial one _H_ 0 is imposed: _H_ ( _x_ = _L_ , _t_ ) = _H_ 0 for _t_ ≥ 0 ( _L_ is assumed large enough that this end will not be reached by the propagating surge). 

358 

8 Numerical Integration of the System of Saint Venant Equations 



<!-- Start of picture text -->
H  [m]<br>1.75<br>1.50 t  = 1800 s t  = 3600 s<br>1.25<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0 5000 10000 15000 20000 x [m]<br><!-- End of picture text -->

**Fig. 8.33** Flow profiles during a surge propagation in horizontal frictionless channel 

The system of equations is solved using the difference Preissmann scheme, (see Section 8.2). The computations carried out for _L_ = 50 km, _�x_ = 100 m, _�t_ = 20 s and _θ_ = 0.67 furnished the results shown in Fig. 8.33. 

As far as the Preissmann scheme is considered, it can be successfully used for computation of the surge propagation in some circumstances only. First of all, the scheme cannot handle initially dry bed. Conversely, the initial depth should be enough large to avoid the failure of computations. Next the scheme does not accept too large and too sudden increase of the boundary condition at the upstream end. Increasing of the flow rate per unit width should not be forced immediately but during approximately (4 ÷ 6) _�t_ . This gives rise to some smearing of the steep front of wave. Elimination of the wiggles connected with scheme’s dispersivity requires that some numerical diffusion is introduced. This is performed by choosing of an appropriate value of the weighting parameter _θ_ . If the mentioned conditions are satisfied, the Preissmann scheme is capable to provide quite reasonable results as presented in Fig. 8.33. 

Slightly better numerical properties characterize the modified finite element method with upwind effect. To show this approach let us reconsider the system of Saint Venant equations in conservative and homogenous form 



Approximation of these equations on a uniform grid is carried out as follows: 

- At first the advective term in the momentum equation is approximated using difference formulae (5.104): 

359 

8.6 Application of the Saint Venant Equations for Steep Waves 



where _η_ = 0 corresponds to the forward difference, _η_ = 0.5 corresponds to the centred difference, whereas _η_ = 1 gives the backward difference. 

- Next other terms of both equations are approximated with regard to _x_ using the difference scheme basing on the modified finite element method (see Section 8.3.1). This yields the system of ordinary differential equations with regard to time: 

- for _j_ = 1 



• for _j_ = 2, 3, _. . ._ , _M_ − 1 



- for _j_ = _M_ 



where _M_ is total number of nodes. 

- The system of Eq. (8.145) is integrated over time using the formulae (8.54). Finally one obtains the following system of algebraic equations: 

- for _j_ = 1 



360 8 Numerical Integration of the System of Saint Venant Equations 



• for _j_ = 2, 3, _. . ._ , _M_ − 1 





• for _j_ = _M_ 





8.6 Application of the Saint Venant Equations for Steep Waves 

361 

This non-linear system of algebraic equations completed by the appropriate boundary conditions is solved using the Newton method. 

The properties of the presented method can be examined on the example of the linear wave equations (8.16) and (8.17), using the modified equation approach for accuracy analysis. Following this way finally we obtain the system of modified wave equations corresponding to the solved linear wave equations: 



In Eqs. (8.147) and (8.148) the coefficient of numerical diffusion _Dn_ is given by the expression: 



whereas the coefficients of numerical dispersion _En_ 1 and _En_ 2 are defined as follows: 



where _Cr_ is the Courant number defined by Eq. (8.18). Note that in this case the numerical diffusivity is controlled by two parameters: _θ_ and _η_ . The first one is related to the time integration, whereas the second one is related to the approximation of the convective term only. The latter parameter allows us to introduce into solution the upwind effect. 

Performing similar stability analysis as presented in Section 8.3.2, one can show that the following conditions: 







ensure absolute stability of the method. 

The numerical experiments dealing with propagation of a surge show that the described method seems more effective than the difference Preissmann scheme. It is possible to increase the flow rate at the boundary immediately from zero to a 

362 

8 Numerical Integration of the System of Saint Venant Equations 

relatively large amount. Two weighting parameters allow us to control the numerical diffusivity needed for suppressing the wiggles appearing at the steep front. Usually 3–5 iterations should be applied to obtain satisfying results. The mass balance error generated by the method is very low and usually it does not exceed 0.001%. Although the method is absolutely stable for linear problems, in the case of non-linear equations the assumed time step must be limited. Acceptable values of the Courant number varies depending on the circumstances, however it should not exceed 0.6–0.8. The main disadvantage of the method is that it fails for initially shallow water in considered channel, i.e. for dry bed. 

To show an example of solution let us apply the described method to solve the dam break problem. 

_Example 8.7_ Equations (8.142) and (8.143) are solved in a wide rectangular channel of length _L_ = 3,000 m for a discontinuous initial conditions caused by the dam as presented in Fig. 8.31. At the downstream the initial depth is _Hd_ = 0.50 m, whereas the upstream depth is _Hu_ = 10.0 m. At both channel ends the initially imposed depths are kept in time. Suddenly the dam is removed and the water from the reservoir is released. For the assumed auxiliary conditions the system of Eqs. (8.142) and (8.143) has analytical solution given by Wu et al. (1999). This solution is represented in Fig. 8.34 by the dotted line. The solid line represents the results of numerical solution obtained at _t_ = 120 s for _�x_ = 2.0 m and _�t_ = 0.1 s with the following values of the weighting parameters: _ω_ = 0.67, _θ_ = 0.70 and _η_ = 0.67. 

Both plots are in perfect agreement. Note that _ω_ = 0.67 corresponds to the standard finite element method. Therefore one can suppose that this method gives 



<!-- Start of picture text -->
H  [m]<br>10<br>8<br>6<br>4<br>2<br>0<br>0 1000 2000 3000 x [m]<br><!-- End of picture text -->

**Fig. 8.34** Flow profiles in the channel at _t_ = 120 s after removing the dam calculated numerically ( _solid line_ ) and analytically ( _dotted line_ ) 

8.6 Application of the Saint Venant Equations for Steep Waves 

363 

satisfactory results, when some additional dissipation is introduced into solution. In this case it was achieved with _θ_ = 0.70 and _η_ = 0.67. 

Although both discussed methods, i.e. the difference Preissmann scheme and the modified finite element method, appear effective for solving some cases of unsteady flow with discontinuities, they are not reliable for all possible forms of such kind of flow, particularly those corresponding to extreme situations. In such a situation it seems to be better to use the finite volume method, especially suitable for solving the hyperbolic equations with discontinuities. 

We will end this section by presentation of the results of dam break problem computed with the finite volume method. Equations (8.142) and (8.143) are solved in a wide horizontal channel described in Example 8.5 for the same data except the initial and boundary conditions down of the dam. A dry state is assumed ( _Hd_ ≈ 0.0 m). For assumed auxiliary conditions, when flow resistance is neglected the system of Eqs. (8.142) and (8.143) has analytical solution given by Ritter (Wu et al. 1999, Chanson 2004). This solution is represented in Fig. 8.35 by the dotted line. In the same figure the solid line represents the results of numerical solution at _t_ = 70 s given by the finite volume method. 

Comparing both graphs one can find out their perfect agreement. In contrast to the finite difference and element methods this takes place even in the vicinity of channel bed. 

Next solution deals with the dry state but taking into account the flow resistance. The results obtained for exactly the same data as assumed previously and for the Manning coefficient assumed to be equal _nM_ = 0.025 are displayed in Fig. 8.36. For comparison they are contrasted with solution from Fig. 8.35 for frictionless flow. Although in this case no exact solution exists, the computed flow profile qualitatively similar to the ones observed in the physical experiments (see Chanson 2004). 



<!-- Start of picture text -->
H [m]<br>10<br>t  = 0<br>8<br>6<br>4<br>t  = 70 s<br>2<br>0<br>0 1000 2000 3000 x [m]<br><!-- End of picture text -->

**Fig. 8.35** Flow profiles in frictionless channel at _t_ = 70 s after removing the dam calculated numerically ( _solid line_ ) and analytically ( _dotted line_ ) 

364 

8 Numerical Integration of the System of Saint Venant Equations 



<!-- Start of picture text -->
H  [m]<br>10<br>8<br>6<br>n M. = 0.025<br>4<br>2 n M. = 0.0<br>0<br>0 1000 2000 3000 x  [m]<br><!-- End of picture text -->

**Fig. 8.36** Comparison of the flow profiles in considered channel at _t_ = 70 s after removing the dam calculated using the finite volume method without friction and including friction 

### **References** 

- Abbott MB (1979) Computational hydraulics – Elements of the theory of free surface flow. Pitman, London 

- Abbott MB, Basco DR (1989) Computational fluid dynamics. Longman Scientific and Technical, New York 

- Abbott MB, Ionescu F (1967) On the numerical computation of nearly – horizontal flows. J. Hydr. Res. 5:97–117 

- Billingham J, King AC (2000) Wave motion. Cambridge University Press 

- Chanson H (2004) The hydraulics of open channel flow: An introduction, 2nd edn. Elsevier, Oxford 

- Cippada S, Ramswamy B, Wheeler MF (1994) Numerical simulation of hydraulic jump. Int. J. Numer. Meth. Eng. 37:1381–1397 

- Cunge J, Holly FM, Verwey A (1980) Practical aspects of computational river hydraulics. Pitman Publishing, London 

- Cooley RI, Moin SA (1976) Finie element solution of Saint Venant equations. J. Hydr. Div. ASCE HY6:759–775 

- Fread DL (1993) Flow routing. In: Maidment DR (ed.) Handbook of hydrology. McGraw-Hill, New York 

- French RH (1985) Open channel hydraulics. McGraw–Hill, New York 

- Gresho PM, Sani RL (2000) Incompressible flow and the finite-element method, vol. 1: Advectiondiffusion. Wiley, Chichester, England 

- LeVeque RJ (2002) Finite volume methods for hyperbolic problems. Cambridge University Press Liggett JA, Cunge JA (1975) Numerical methods of solution of the unsteady flow equations. In: 

   - Mahmood K, Yevjewich V (eds.) Unsteady flow in open channels. Water Resources Publishing, Fort Collins, CO, USA 

- Katopodes N (1984) A dissipative Galerkin scheme for open channel flow. J. Hydr. Engng. ASCE 110 (4):450–466 

- Korn GA, Korn TM (1968) Mathematical handbook for scientists and engineers, 2nd edn. McGraw–Hill, New York 

- Mahmood K, Yevjewich V (eds.) (1975) Unsteady flow in open channels. Water Resources Publishing, Fort Collins, CO, USA 

Potter D (1973) Computational physics. Wiley, London 

365 

References 

- Singh AK, Porey PD, Ranga Raju KG (1997) Criterion for location of downstream control for dynamic flood routing. J. Hydrol. 196:66–75 

- Szymkiewicz R (1991) Finite – element method for the solution of the Saint Venant equations in an open channel network. J. Hydrol. 122:275−287 

- Szymkiewicz R (1995) Method to solve 1D unsteady transport and flow equations. J. Hydr. Engng. ASCE 121 (5):396−403 

- Wu C, Huang G, Zheng Y (1999) Theoretical solution of dam-break shock wave. J. Hydr. Engng. ASCE 125 (11):1210–1215 

- Yalin MS, Ferreira da Silva AM (2001) Fluvial processes. International Association of Hydraulic Engineering and Research, Delft, The Netherlands 

Zienkiewicz OC (1972) The finite element method in engineering science. McGraw-Hill, London 

## **Chapter 9 Simplified Equations of the Unsteady Flow in Open Channel** 

### **9.1 Simplified Forms of the Saint Venant Equations** 

The system of Saint Venant equations derived in Chapter 1 in the form of Eqs. (1.77) and (1.78) or Eqs. (1.79) and (1.80) is called the dynamic wave model or the complete dynamic model. This model of unsteady open channel flow gives reliable results if the underlying assumptions are satisfied. On the other hand, the Saint Venant model requires rather complex methods of solution and relatively large number of data characterizing both the channel and the flow conditions. For this reasons hydrologists tried to simplify the system of Saint Venant equations to obtain models, which require less input information. 

Consider the dynamic equation (1.77): 



##### where: 

_t_ – time, 

_x_ – longitudinal coordinate, _H_ – water depth, _U_ – flow velocity, _g_ – gravitational acceleration, _s_ – channel bottom slope, 

_S_ – slope of energy line. 

One can notice that its terms have different orders of magnitude. Henderson (1966) showed, that even for a river with considerable longitudinal bed slope, for steep flood waves, i.e. when the inertial force should play relatively significant role, the values of the consecutive terms of Eq. (9.1) differ by about two orders of magnitude. Similar conclusions were presented by Cunge et al. (1980). Evaluation of subsequent terms of Eq. (9.1) carried out for flow with significant variability of its 

> R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2_9, ⃝C Springer Science+Business Media B.V. 2010 

367 

368 

9 Simplified Equations of the Unsteady Flow in Open Channel 

parameters both in time and in space, showed that the first and second terms of the left hand side are of the order of ∼1.0·10<sup>−4</sup> and ∼1.5·10<sup>−4</sup> respectively. At the same time the bed slope, being in this case of the order of 10<sup>−3</sup> causes, that the first term of the right side hand of Eq. (9.1) is of the order ∼10<sup>−2</sup> . If the differences in depth along the channel axis are small then the third term is relatively small comparing with _g_ · _s_ . Consequently, the term representing the friction force will be of order of the bed slope, i.e. _s_ = _S_ . This means that in the dynamic equation the friction force and the gravitational force dominate. In some cases the differences in orders of magnitude can be even greater than presented above. Thus, it is reasonable to neglect the terms of lesser importance. As a result, one obtains the equations in simpler forms. Simplified equations are still interesting for hydrological practice, since they can be more easily applied to the flood routing problem. There are two simplified forms of the system of Saint Venant equations: the kinematic wave model and the diffusive wave model. Both models base on the original continuity equation and on the appropriately simplified dynamic equation. The theory of the kinematic wave was given by Lighthill and Whitham (1955) whereas the diffusive wave theory was presented by Hayami (1951). The properties and applicability of both mentioned models have been discussed by many authors, e.g. Miller and Cunge (1975), Ponce, Li and Simmons (1978) and Ponce (1990). A comprehensive review is given by Singh (1996). Although not generally appropriate to adequately reproduce the real flood routing process, the linearized forms of the simplified models are applied very often. 

Let us recall the system of Saint-Venant equations, which with flow rate and depth as dependent variables, can be written as follows: 



where: 

_Q_ – flow discharge, 

_A_ – cross-sectional area of flow, 



The slope friction _S_ is expressed using the Manning formula: 



where: 

_nM_ – Manning roughness coefficient, _R_ – hydraulic radius. 

369 

9.1 Simplified Forms of the Saint Venant Equations 

The integer constants _k_ and _l_ can take the values of either 0 or 1. For _k_ = 1 and _l_ = 1 we have full momentum equation which corresponds to the dynamic wave, whereas for _k_ = 0 and _l_ = 1 Eqs. (9.2) and (9.3) become the diffusive wave model. The kinematic wave model is obtained when _k_ = 0 and _l_ = 0. 

First, let us consider the kinematic wave model. This model is derived when in the momentum equation only the gravitational and friction forces are taken into account. In such a case Eq. (9.3) becomes the equation for steady uniform flow: _s_ = _S_ . 

Then the kinematic wave model is constituted by the differential continuity equation (9.2) and the Manning equation (9.4), i.e.: 





The momentum equation (9.3) can be simplified in another way leading to the second simpler form of the unsteady flow equations. If apart from the friction and gravitational forces, as previously, we take into account the hydrostatic force as well, then the diffusive wave model will be obtained. It is constituted by the continuity equation (9.2) and simplified momentum equation (9.3): 



The meaning of the introduced assumptions can be illustrated using the so-called rating curve. This curve represents the relation between the water level (or depth) and the discharge rate in the considered channel cross-section. These variables are related via the Manning formula: 



In a particular case when the bed slope coincides with the energy line slope, i.e. for the uniform flow, Eq. (9.9) becomes Eq. (9.6). If we calculate the energy line slope _S_ from Eq. (9.1) and substitute in Eq. (9.9), we obtain (Chow et al. 1988): 



In a general case of unsteady flow the relation _Q_ ( _H_ ) is non-unique, because it depends on _∂Q_ / _∂t_ , _∂Q_ / _∂x_ , and _∂H_ / _∂x_ , Due to this non-uniqueness thewell-known 

9 Simplified Equations of the Unsteady Flow in Open Channel 

370 



<!-- Start of picture text -->
H<br>failling limb<br>rating curve<br>in steady flow<br>H<br>0<br>rising limb<br>Q      Q      Q 2          0          1 Q<br><!-- End of picture text -->

**Fig. 9.1** Hysteresis of the function _Q_ ( _H_ ) during the unsteady flow 

phenomenon of the rating curve hysteresis is observed during the passage of a flood wave. At the rising limb of flood wave (Fig. 9.1), where we have _∂H_ / _∂x_ < 0 and _∂Q_ / _∂x_ < 0, the flow rate for given depth _H_ 0 is greater comparing with the discharge for steady flow: _Q_ 1 > Q0. Conversely, at the failing limb, when _∂H_ / _∂x_ > 0 and _∂Q_ / _∂x_ > 0, the corresponding flow rate will be less than one for the steady flow. A unique relation between _Q_ and _H_ is possible only for steady uniform flow, when the derivatives over _x_ and _t_ disappear and Eq. (9.10) coincides with Eq. (9.6). The diffusive wave model obtained for _k_ = 0 and _l_ = 1 is able to reproduce to some extent the non-uniqueness of _Q_ - _H_ relation, since it takes into account the non-uniformity of flow, expressed by _∂H_ / _∂x_ . On the other hand, the kinematic wave model with _k_ = _l_ = 0 predicts the same relation _Q_ ( _H_ ), corresponding to the steady uniform flow, regardless of the actual flow conditions. 

In the following example are presented the relations _Q_ ( _H_ ) obtained for the complete system of Saint Venant equations and its both simplified forms. 

_Example 9.1_ In rectangular open channel of length _L_ = 80 km the unsteady flow is considered. Assume the following data: 

- bed width of channel is _b_ = 30 m, 

- bed slope is _s_ = 0.0005, 

- Manning coefficient is _nM_ = 0.035, 

- initial condition: 

at _t_ = 0 is determined by the steady uniform flow with _Q_ 0 = 20 m<sup>3</sup> /s, 

- boundary conditions: 

at _x_ = 0 the following hydrograph is imposed: 

9.1 Simplified Forms of the Saint Venant Equations 

371 



where: 

_Q_ 0 – baseflow discharge of the inflow, 

_Q_ max – peak discharge of the inflow, _t_ max – time of the peak flow, 

_α_ – parameter, 

at _x_ = _L_ the depth _H_ ( _x_ , _t_ ) = _Hn_ = const. ( _Hn_ is normal depth corresponding to _Q_ 0) is imposed. 

The rating curve is computed at the control cross-section located at mid-length of the channel. 

All the systems of equations (i.e. the dynamic, diffusive and kinematic wave models) are solved by the modified finite element method described in Chapter 8. The computations were performed for: _�t_ = 60 s, _�x_ = 400 m, _Q_ 0 = 20 m<sup>3</sup> /s, _Q_ max = 200 m<sup>3</sup> /s, _t_ max = 2 h and _α_ = 1.5. 

In Fig. 9.2 the relation _Q_ ( _H_ ) generated by the system of Saint Venant equation is displayed. The obtained curve has a loop of hysteresis typical for unsteady flow. 

The rating curves generated by the simplified forms of the unsteady flow equations are shown in Fig. 9.3. One can see that in the considered case the relation _Q_ ( _H_ ) for the diffusive wave differs slightly from the one obtained for the complete system of equations. For the kinematic wave the loop of hysteresis disappears and the rating curve becomes a unique relation as it is expected. 



<!-- Start of picture text -->
H  [m]<br>3.5<br>3.0<br>2.5<br>2.0<br>1.5<br>1.0<br>0 25 50 75 100 125 150 Q [m 3 /s]<br><!-- End of picture text -->

**Fig. 9.2** Hysteresis of the function _Q_ ( _H_ ) for the dynamic wave 

9 Simplified Equations of the Unsteady Flow in Open Channel 

372 



<!-- Start of picture text -->
H  [m]<br>3.5 b<br>3.0<br>a<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0 25 50 75 100 125 150 Q  [m 3 /s]<br><!-- End of picture text -->

**Fig. 9.3** Hysteresis of the function _Q_ ( _H_ ) for the diffusive wave model ( **a** ) and for the kinematic wave model ( **b** ) 

### **9.2 Simplified Flood Routing Models in the Form of Transport Equations** 

### **_9.2.1 Kinematic Wave Equation_** 

The kinematic wave model in the form of system of equations (9.5) and (9.6) can be reduced to one differential equation with regard to a single unknown function only. The equation for steady flow is rearranged to the following form: 



For the Chezy formula one obtains: 



whereas for the Manning formula we have: 



Simplified Flood Routing Models in the Form of Transport Equations 

9.2 

373 

If instead of the depth _H_ ( _x_ , _t_ ) the wetted flow area _A_ ( _x_ , _t_ ) is introduced as the dependent variable, then the system of equations describing the kinematic wave model takes the following form: 





Let us assume a wide and shallow channel for which the wetted perimeter can be considered constant. Differentiation of Eq. (9.16) with these assumptions yields: 



Substitution of Eq. (9.17) in Eq. (9.15) gives the following equation: 



Equation (9.18) can be rewritten in a more compact form: 



where: 



is the kinematic wave celerity. Substitution of the coefficients _a_ and _m_ given by Eqs. (9.14a) and (9.14b), in Eq. (9.20) yields: 



This means, that the kinematic wave moves faster than the water flows in the channel. 

### **_9.2.2 Diffusive Wave Equation_** 

Using a similar approach, the diffusive wave model in the form of system of equations (9.7) and (9.8) can be reduced to a single differential equation as well. For different assumptions one obtains various forms of the final equation where the dependent variable can be the depth _H_ ( _x_ , _t_ ), the water stage _h_ ( _x_ , _t_ ) or the flow rate _Q_ ( _x_ , _t_ ). We will derive the classical form of the diffusive wave equation with regard to flow rate. To this end the Manning equation (9.9) is rewritten as 

9 Simplified Equations of the Unsteady Flow in Open Channel 

374 



where: 



The coefficient _K_ , called conveyance, is a function of the cross-sectional parameters only. Substitution of Eq. (9.22) in Eq. (9.8) allows us to rewrite the diffusive wave model (9.7) and (9.8) as follows: 



In the next step the continuity equation is differentiated with regard to _x_ , whereas the dynamic equation is differentiated with regard to _t_ . Assuming constant width of the channel ( _B_ = const.), one obtains: 



Subtraction of Eq. (9.26) from Eq. (9.27) eliminates the cross derivatives of function _H_ ( _x_ , _t_ ), yielding: 



Since the conveyance _K_ is a function of the depth _H_ , then one can write: 



With the continuity equation (9.24) the above equation becomes: 



Substitution of Eq. (9.30) in Eq. (9.28) yields: 



375 

9.2 Simplified Flood Routing Models in the Form of Transport Equations 

Introducing new variables: 





Equation (9.31) is rewritten in the following final form: 



Equation (9.34) is the diffusive wave model in the form of advection-diffusion transport equation in which _C_ is the kinematic wave celerity and _D_ is the coefficient of hydraulic diffusivity. 

The most popular form of the diffusive wave model, proposed by Hyami in 1951 (Eagleson 1970), is a particular case of equation (9.30). It is obtained from Eq. (9.30) on condition that: 

- the slope of energy line is replaced by the bed slope ( _S_ = _s_ ), 

- the considered channel is wide and shallow so one can assume constant wetted perimeter ( _p_ = const.). 

Taking these assumptions into account one obtains: 



Equation (9.36) represents the kinematic wave celerity, previously derived for the kinematic wave equation (9.19). The diffusive wave model in the form of Eq. (9.34) in which the coefficients are given by Eqs. (9.35) and (9.36) is frequently used. 

To show the difference between the kinematic and diffusive wave models, i.e. to notice role of the diffusive term in Eq. (9.34), let us rout the same flood wave using both models. 

_Example 9.2_ In a rectangular straight channel of length _L_ = 100 km the propagation of the flood wave is considered. The auxiliary conditions are following: 

376 

9 Simplified Equations of the Unsteady Flow in Open Channel 

- initial condition at _t_ = 0 is determined by the steady uniform flow with flow discharge _Q_ 0, 

- boundary conditions: 

at _x_ = 0 a hydrograph in the form of Eq. (9.11) is imposed: 



for the diffusive wave equation at the downstream end _x_ = _L_ , additionally is imposed the function _H_ ( _x_ , _t_ ) = _H_ 0 = const., where _H_ 0 is normal depth corresponding to _Q_ 0. 

Assume the following data: 

- bed width of channel is _b_ = 25 m, 

- bed slope is _s_ = 0.0005, 

- Manning coefficient is _nM_ = 0.030, 

- baseflow _Q_ 0 = 5 m<sup>3</sup> /s, 

- peak flow _Q_ max = 100 m<sup>3</sup> /s, 

- time to peak _t_ max = 4 h, 

- _α_ = 1.0. 

Solve the linear kinematic and diffusive wave models to compare the results at the control cross-section located at _x_ = 75 km of the considered channel. Note that the boundary condition imposed at the downstream end for the diffusive wave equation does not disturb the flow in assumed control. 

Since the solved equations are non-linear ones then their linearization is needed. Linearization of Eq. (9.37) is carried out assuming constant values of the parameters _C_ and _D_ . They can be calculated accordingly to Eqs. (9.38) and (9.39) for a constant value of the flow rate taken as arithmetic average from its lowest and highest values i.e. _Q_ = _QC_ = ( _Q_ 0+ _Q_ max)/2. For _Qc_ = 52.5 m<sup>3</sup> /s one obtains _C_ = 1.88 m/s and _D_ = 2100.0 m<sup>2</sup> /s. The kinematic wave equation is solved using the box scheme applied in Chapter 6 for solving the advection equation, whereas the diffusive wave equation is solved with the modified finite element method applied for solving the advection-diffusion equation in Chapter 7. 

The computations performed for _�x_ = 1,000 m and _�t_ = 600 s i.e. with the advective Courant number equal to _Ca_ = 1.13 gave the results displayed in Fig. 9.4. They represent typical solutions of the pure advection equation and the advectiondiffusion equation with constant parameters. 

Note that the kinematic wave model produces practically exact solution ensuring nearly pure translation of the flood wave. On the other hand, as it could be expected, the diffusive term present in the diffusive wave equation attenuates the propagating wave giving rise to decreasing of its peak and to widening of its base. 

9.2 Simplified Flood Routing Models in the Form of Transport Equations 

377 



<!-- Start of picture text -->
Q  [m 3 /s] Q  ( x = 0,t)<br>QK  ( x = L , t )<br>100<br>QD  ( x = L , t )<br>80<br>60<br>40<br>20<br>0<br>0 12 24 36 48 60 t  [h]<br><!-- End of picture text -->

**Fig. 9.4** Results of wave routing by the linear kinematic ( _QK_ ( _x_ = 75 km, _t_ )) and diffusive ( _QD_ ( _x_ = 75 km, _t_ )) wave equations 

### **_9.2.3 Linear and Non-linear Forms of the Kinematic and Diffusive Wave Equations_** 

In the preceding section it was shown that neglecting the inertial terms the system of Saint Venant equations (9.2) and (9.3) can be transformed into the following advective – diffusive transport equation with the function _Q_ ( _x_ , _t_ ) as dependent variable: 



where: 

_C_ ( _Q_ ) – advective velocity, _D_ ( _Q_ ) – hydraulic diffusivity. 

For a wide and rectangular channel with the slope of energy line equal to the slope of the channel bottom _C_ ( _Q_ )) becomes the kinematic wave speed. In such a case the parameters of Eq. (9.37) are expressed as follows: 



9 Simplified Equations of the Unsteady Flow in Open Channel 

378 

where _m_ is the kinematic wave ratio ( _m_ = 3/5 for the Manning law friction). Equation (9.37) represents the diffusive wave – the kinematic wave is obtained for _D_ = 0. Parameter _α_ is given by Eq. (9.13). Both equations are non-linear since their parameters _C_ and _D_ depend on _Q_ . However, linearized versions of Eq. (9.37) with constant _C_ and _D_ are usually applied, for the sake of simplicity. To show the difference between linear and non-linear forms of this equation, let us consider the following example. 

_Example 9.3_ In the same channel and for the same data as assumed previously in Example 9.2, the flood wave propagation is considered. However, conversely to the preceding example, now the non-linear forms of the kinematic and diffusive waves are solved. 

The kinematic wave equation is solved using the box scheme, whereas the diffusive wave equation is solved with the modified finite element method. However, as the approximation of solved equation (9.37) leads to the non-linear systems of algebraic equations the iterative method must be used for its solution. For both models the Newton method generating convergent solution is applied. 

In Fig. 9.5 the results of solution of linear and non-linear forms of the kinematic wave equation are shown. The results for linear model are coming from Example 2. One can notice the effect typical for a non-linear equation. The front of the propagating wave becomes steeper, whereas its tail becomes longer. This property results from Eq. (9.38). The advection velocity _C_ increases with the flow rate _Q_ so the wave peak moves faster than the lower parts of the wave. Finally, the propagating wave can break down. More detailed analysis of this phenomenon, based on the theory of characteristics, is given for example by Abbott (1979). 

Similar, but less significant effects (see Fig. 9.6) are observed in the solution of the non-linear diffusive wave equation as well. However in this case the propagating wave is simultaneously damped due to the hydraulic diffusion, so its breakdown is rather impossible. Still, the differences between the linear and non-linear versions of the diffusive wave equation cannot be neglected. Therefore, we have to be aware that linearization of Eq. (9.37) while simplifying its numerical solution, changes significantly the results. 

While solving the non-linear partial differential equations representing transport of any scalar quantity, the form of solved equation is a problem of great importance. The equation must be written in conservative form. Otherwise one can expect errors in the balance of transported quantity in the numerical solution. As far as Eq. (9.37) is considered, it is a non-linear advection-diffusion transport equation written in the non-conservative form. Therefore one can expect that the presented numerical solutions should be affected by the errors. Indeed, if we thoroughly examine the function _Q_ ( _t_ ) obtained with non-linear models at the control cross-section, we will notice that the total volume of the water leaving the considered channel reach differs from that entering the reach, the difference exceeding 8 and 6% for the kinematic and diffusive waves, respectively. On the other hand, the numerical solutions of the linear equations satisfy the law of mass conservation perfectly for the non-linear diffusive and kinematic wave equations considered in Example 9.2. Then the numerical solution of Eq. (9.37) seems to be a non-trivial problem. 

9.2 Simplified Flood Routing Models in the Form of Transport Equations 

379 



<!-- Start of picture text -->
Q  [m 3 /s]<br>Q ( x = 0,  t )<br>100<br>QL ( x = L ,  t )<br>80<br>60<br>40<br>QN ( x = L ,  t )<br>20<br>0<br>0 12 24 36 48 60 t [h]<br><!-- End of picture text -->

**Fig. 9.5** Results of wave routing by the linear ( _QL_ ( _x_ = 75 km, _t_ )) and non-linear ( _QN_ ( _x_ = 75 km, _t_ )) kinematic wave equations 



<!-- Start of picture text -->
Q  [m 3 /s] Q  ( x = 0, t )<br>100<br>QL ( x = L , t )<br>80<br>60<br>40<br>QN ( x = L , t )<br>20<br>0<br>0 12 24 36 48 60 t [h]<br><!-- End of picture text -->

**Fig. 9.6** Result of wave routing by the linear ( _QL_ ( _x_ = 75 km, _t_ )) and non-linear ( _QN_ ( _x_ = 75 km, _t_ )) diffusive wave equations 

9 Simplified Equations of the Unsteady Flow in Open Channel 

380 

### **9.3 Mass and Momentum Conservation in the Simplified Flood Routing Models in the Form of Transport Equations** 

### **_9.3.1 The Mass and Momentum Balance Errors_** 

The system of Saint-Venant equations comprises the continuity and dynamic equations which are derived from the mass and momentum conservation principles, respectively. To avoid the mass and momentum balance errors in the numerical solution, both equations have to be written in conservative forms. This problem has been shortly discussed in Chapter 8. As we showed in the preceding section, the linearized forms of simplified models perfectly ensure mass conservation, whereas the non-linear forms of these models may give rise to mass balance error. The numerical calculations presented in Example 9.2 show that this error can be of order of 8%, but even 20% difference in volumes between upstream and downstream hydrograph may be obtained (Cappelaere 1997). 

Originally, all simplified models are written in the form of a system of differential equations (i.e. a continuity equation and a simplified momentum equation). Consequently, there are no doubts which quantities are the conservative ones. However the situation is changed at the moment when both equations are combined to obtain a single transport equation. It appears that similarly to other flow problems, the final form of the non-linear simplified models has a fundamental meaning for the mass and momentum conservation in their numerical solutions. On the other hand, one can expect that the non-linear simplified equations, derived from the continuity and dynamic equations, should also fulfil both mass and momentum conservation principles at the same time. For this reason the following question seems to be relevant: how should the simplified models be interpreted from the point of view of the conservation laws? To explain this question let us follow the idea presented by Gasiorowski and Szymkiewicz (2007). 

Let us consider a channel reach of length _L_ . Assuming that the flow takes place in a time interval _T_ , which is long enough (after the passing of the flood wave the discharge comes back to its initial value), the mass balance for constant water density takes the following form: 



It means that the total volumes passing through the two ends of the channel reach given by the formulas: 



9.3 Mass and Momentum Conservation in the Simplified Flood Routing Models 

381 



should be equal. The relative mass balance error can be defined as follows: 



where: 

_�Em_ – he mass error expressed in %, 

_m_ 0, _mL_ – olume of inflow and outflow respectively, within the time period of _T_ . 

The momentum balance can be represented similarly. The total variation of momentum over a channel reach of length _L_ in time interval _T_ must be equal to the difference of the momentum transported at upstream end _x_ = 0 and at the downstream end _x_ = _L_ respectively. If constant water density is assumed, the losses caused by friction, gravitation and pressure are neglected and the time interval _T_ is long enough, this balance will take the following simplified form: 



The total momentum of inflow and outflow is given by the formulas: 



where: 

_M_ 0, _ML_ – total momentum of inflow and outflow, respectively, within the time period of _T_ , divided by water density, 

_U_ – flow velocity, 

_A_ – cross-sectional area of flow. 

The relative momentum balance error can be calculated as follows: 



9 Simplified Equations of the Unsteady Flow in Open Channel 

382 

where: _�EM_ – the momentum error expressed in %. 

Equations (9.43), (9.44a) and (9.44b) hold for the system of Saint Venant equations when both functions _Q_ ( _x_ , _t_ ) and _A_ ( _x_ , _t_ ) are known. In the case of kinematic and diffusive wave equation the momentum balance can be rearranged using the Manning formula written in the form of Eq. (9.16). Consequently Eq. (9.43) can be rewritten as follows: 



Note that for the linear kinematic wave model with _U_ ( _x_ , _t_ ) = const., the momentum balance expressed by Eq. (9.43) takes the form of Eq. (9.40), which represents the mass balance. 

Numerical tests confirm that the mass balance error _�Em_ calculated for all considered models written in the form of the systems of conservative equations is very low (of the order of ∼10<sup>−2</sup> %), whereas the total momentum of the outflow appears to be less than the momentum of the inflow. It is reasonable, because the effects of friction, gravitation and pressure have been neglected in the momentum balance. 

As far as the linear kinematic and diffusive wave models in form of the advection and advection – diffusion equation are considered, one can find out that the mass and momentum principles are satisfied perfectly regardless of the flow conditions. Numerical test confirm that both errors _�Em_ and _�EM_ do not exceed the value of 0.01%. 

Comparison of the momentum balance errors in simplified models with those calculated for the full system of Saint-Venant equations reveals an interesting fact. The error _�EM_ ,which for the Saint-Venant system is of the order of a couple per cents, practically disappears for both linear advection and advection-diffusion transport equations. The way of derivation of the simplified equations changes the character of the momentum conservation law. This is due to an additional important hypothesis on the flow process, which is implicitly introduced when the simplified system of Saint Venant equations is transformed into the advection and advection-diffusion equations. The differentiation of the simplified momentum equation with respect to time means that the sum of all forces taken into account in the simplified model is assumed to be constant during the flow process. The value of this sum is determined by the boundary condition imposed at the upstream end of the channel reach. In other words the differentiation of Eq. (9.25) gives rise to an essential modification of the final equation. No losses of the momentum are represented in Eq. (9.37), since during the differentiation the friction force represented by the source term was replaced by a diffusive one. 

For the non-linear equations the total mass at the downstream end is not equal to those entering the channel reach. The balance errors _�Em_ and _�EM_ are usually of the order of several per cents. As it was afore-mentioned, Cappelaere (1997) reported this error can reach even about 20%. 

9.3 Mass and Momentum Conservation in the Simplified Flood Routing Models 

383 

### **_9.3.2 Conservative and Non-conservative Forms of the Non-linear Advection-Diffusion Equation_** 

To explain the problem of mass and momentum balance errors which appear for the non-linear flow routing models, let us begin with recalling the basic information on the conservative or non-conservative form in which the solved equations can be written. 

The 1-D advective or advective **-** diffusive transport equation without the source/sink term has the following form: 



in which 





where: 

_φA_ – advective flux, _φD_ – diffusive flux, _f_ – scalar function, _U_ – advective velocity, _D_ – coefficient of diffusion. 

Equation (9.47) has so-called divergence or conservative form because its integration over the domain of solution (0 ≤ _x_ ≤ _L_ ) gives directly the following global conservation law: 



The total energy (if _f_ represents temperature) or mass (if _f_ represents concentration of dissolved substance) changes only by the net flux of _f_ out the domain through the boundary _x_ = 0 and _x_ = _L_ . It should be mentioned that only the divergence form of transport equation assures global conservation (Gresho and Sani 2000). 

Comparing Eqs. (9.37) and (9.47) one can notice that Eq. (9.37) is written in a non-conservative form since this equation cannot be transformed into the global conservation law in form of Eq. (9.49). To show the consequences of this difference let us consider the non-linear advection equation of type of Eq. (9.37) with _D_ = 0: 

9 Simplified Equations of the Unsteady Flow in Open Channel 

384 



where: _a_ , _b_ – constant parameters. 

Integration by parts of Eq. (9.50) with regard to _x_ over a channel reach (0 ≤ _x_ ≤ _L_ ) leads to the following expression: 



where 



The extra term _RA_ results from the non-linearity of the advective term. Equation (9.52) does not represent a global conservation law, because the total quantity represented by function _f_ is changed not only by the net advective flux through the boundaries, as in Eq. (9.49), but by the additional term _RA_ as well. This term can be considered as the conservation error in the numerical solution. It can be avoided on condition that proper conservative form of the non-linear equation is applied. Obviously, if a constant kinematic speed is assumed ( _a_ · _f_<sup>_b_</sup> = const.), Eq. (9.50) will become conservative and consequently _RA_ will disappear. 

While discussing the conservative properties of the diffusive wave model it is worth to recall the way of its derivation. Let us assume that _f_ represents some conservative quantity as the mass of dissolved matter or energy. The governing equation (Eq. 9.47) for the transport of _f_ by the flowing stream, obtained via balance of conservative quantity for control volume, has the conservative form. Conversely to this equation, Eq. (9.37) was not derived directly from the mass or momentum conservation principle. It was obtained by manipulation on the continuity and momentum equations derived for unsteady open channel flow. Consequently Eq. (9.37) represents a non-conservative form. Equation (9.47) is consistent with Eq. (9.37) only when the advective velocity and the coefficient of diffusion are constant. Unfortunately we can never obtain Eq. (9.47) from Eq. (9.37) and consequently one can expect that Eq. (9.37) will never satisfy the global conservation law. 

### **_9.3.3 Possible Forms of the Non-linear Kinematic Wave Equation_** 

In order to emphasize the essential difference between conservative and nonconservative forms of the transport equation in the case of flood routing models, let us consider Eq. (9.37) with _D_ = 0: 

385 

9.3 Mass and Momentum Conservation in the Simplified Flood Routing Models 



It represents a non-conservative form of the non-linear kinematic wave equation. Equation (9.53) can be integrated over a channel reach of length _L_ : 



In the first term of the above expression the order of integration and differentiation is inversed, whereas the second term is integrated by parts. Consequently Eq. (9.54) is rewritten as follows: 



where: 

_Q_ 0 – discharge at the upstream end, _QL_ – discharge at the downstream end. 

The term _RA_ is defined by the following formula: 



Now let us consider again non-linear Eq. (9.53), but rewritten in another form: 



One can see that the coefficient in Eq. (9.57) is constant, because _α_ , _m_ = const., whereas the function _Q_ ( _x_ , _t_ ) is inserted into derivative. In this way Eq. (9.53), which represents a non-conservative form of non-linear kinematic wave, was transformed into a conservative form. As previously, Eq. (9.57) can be integrated over a channel reach: 



386 

9 Simplified Equations of the Unsteady Flow in Open Channel 

which leads to: 



From Eq. (9.59) results that the time-variation of the total quantity _Q_ inside the channel reach of length _L_ is caused only by net flux of _Q_<sup>2–</sup><sup>_m_</sup> through upstream and downstream ends of channel, whereas in Eq. (9.55) it depends not only on the net flux of _Q_<sup>2–</sup><sup>_m_</sup> through channel boundaries _x_ = 0 and _x_ = _L_ , but also on the extra term _RA_ . It means that the global conservation of the quantity represented by function _Q_ ( _x_ , _t_ ) is not fulfilled. 

Equation (9.59) is not the only possible conservative form of the kinematic wave equation. Another one can be derived directly from Eqs. (9.2) and (9.3) with _k_ = 0 and _l_ = 0. Combining these equations with earlier accepted assumption that _α_ = const., one obtains: 



An integration of Eq. (9.60) over a channel reach yields the following final result: 



Having three different forms of the non-linear kinematic wave equation one can compare their properties. First of all, it should be explained which conservative quantity they preserve. Since all equations were derived using the continuity and momentum equations for open channel flow, it is reasonable to expect that both conservation laws should be satisfied. To answer this question Eqs. (9.55), (9.59) and (9.61) must be integrated over time. 

The integration of Eq. (9.55) over the time interval ⟨0, _T_ ⟩: 



yields: 



9.3 Mass and Momentum Conservation in the Simplified Flood Routing Models 

387 

Making use of the assumption about the time interval _T_ , the integral over channel reach disappears and Eq. (9.63) becomes as follows: 



Following a similar way for the conservative forms of the kinematic wave equation one obtains: 

- for Eq. (9.59) 







The presented balance formulas allow us to suppose that: 

- Equation (9.60) represents the mass conservation principle since Eq. (9.66) coincides with Eq. (9.40); 

- Equation (9.57) represents the momentum conservation principle since Eq. (9.65) coincides with Eq. (9.46); 

- Equation (9.53) satisfies neither the mass conservation law nor the momentum conservation law since Eq. (9.64) contains an extra term. 

All possible forms of the kinematic wave equation are listed in Table 9.1. 

**Table 9.1** Forms of the kinematic wave equation 

|Possible form of equation|Conservation of mass|Conservation of momentum|
|---|---|---|
|_∂Q_<br>_∂t_ <sup>+</sup><sup>_C_ ·</sup> <sup>_∂Q_</sup><br>_∂x_ <sup>= 0 (</sup><sup>_C_ = const.)</sup><br>_∂Q_<br>_∂t_ <sup>+</sup> <sup>_Q_1−</sup><sup>_m_</sup><br>_α_·_m_ <sup>·</sup> <sup>_∂Q_</sup><br>_∂x_ <sup>= 0</sup><br>_∂Q_<br>_∂t_ <sup>+</sup><br>1<br>_α_·_m_·(2−_m_) <sup>·</sup> <sup>_∂Q_2−</sup><sup>_m_</sup><br>_∂x_<br>=0<br>_α_ <sup>_∂Qm_</sup><br>_∂t_<br>+ <sup>_∂Q_</sup><br>_∂x_ <sup>= 0</sup>|+<br>–<br>–<br>+|+<br>–<br>+<br>–|



9 Simplified Equations of the Unsteady Flow in Open Channel 

388 

One can conclude that among the possible forms of the kinematic wave model only the linear one respects both conservation laws, whereas the conservative forms of the non-linear equation represent either the mass or momentum conservation principle. 

The last considered form of the kinematic wave model (Eq. 9.60) seems suitable with regard to the mass conservation. The global conservation law (Eq. 9.66), corresponding to this equation, is identical with the one for the linear kinematic wave and consequently the mass balance error is always equal to zero. However this equation does not satisfy the momentum conservation principle. 

### **_9.3.4 Possible Forms of the Non-linear Diffusive Wave Equation_** 

The diffusive wave model in form of Eq. (9.37): 



is a non-linear advection-diffusion equation written in a non-conservative form. As it was shown earlier, such form of equation generates a significant mass error. To avoid this error it seems reasonable to transform Eq. (9.67) into a conservative form. For this purpose the following relations are used: 



Equation (9.67) becomes as follows: 



Its integration over channel reach yields: 



where _RD_ is an additional term defined as follows: 



9.3 Mass and Momentum Conservation in the Simplified Flood Routing Models 

389 

Since ( _∂Q_ / _∂x_ )<sup>2</sup> ≥ 0 the term _RD_ will decrease the transported quantity monotonically. The only reason of appearance of this term is diffusion. The term _RD_ acts as a sink and consequently one can expect that the function _Q_ will not be preserved during the advection-diffusion transport process. Consequently, an error in the balance of the transported quantity can be expected. 

The second form of the non-linear diffusive wave equation derived from Eq. (9.67) using Eq. (9.68b) is as follows: 



Integration of this equation with regard to _x_ yields: 



In this case the additional term _RD_ is as follows: 



Comparing both forms of the non-linear diffusive wave equation one can notice that in the corresponding balance formula the additional terms are always present. The integration of the non-conservative forms (Eqs. 9.69 and 9.72) with regard to _x_ , apart from the net flux through boundary, yields additional term _RD_ described by Eq. (9.71) or (9.74), respectively. Transformation of Eq. (9.67) into a conservative form eliminates only the effect resulting from the integration of the advective term. The additional term _RD_ resulting from the integration of the diffusive part of equation is always present. This explains the mass balance error observed in the numerical solutions. Taking into account these facts we can conclude that it is impossible to find a suitable form of the non-linear diffusive wave equation, which could satisfy the mass conservation principle. The reason for this is the way of derivation of the governing equation. Since the non-linear diffusive wave equation is obtained as a combination of the continuity and momentum equation, it cannot be written in a divergent form. The diffusive term in the form: 



existing in Eq. (9.67) cannot be converted into a term of the type: 



9 Simplified Equations of the Unsteady Flow in Open Channel 

390 

i.e. into a divergent form of the diffusive flux. Consequently the global mass conservation will be always affected. 

Equations (9.71) and (9.74) show that the balance errors depend on the derivatives of the flow discharge with regard to _x_ ( _∂Q_ / _∂x_ and _∂Q_<sup>_m_</sup> / _∂x_ ). Therefore one can expect that the generated error will be greater for a steep wave than for a smooth one. 

### **9.4 Lumped Flood Routing Models** 

### **_9.4.1 Standard Derivation of the Muskingum Equation_** 

Apart from the previously presented distributed models (i.e. the dynamic, diffusive and kinematic wave equations), a flood routing can be also carried out using lumped models. This family of models is obtained by elimination of the spatial variable _x_ , so they have the form of ordinary differential equations with regard to time. The standard way of derivation is based on spatial integration of the differential continuity equation (9.15): 



Let us consider a channel reach of length _�x_ as presented in Fig. 9.7. This segment is bounded by two cross-sections located at _xj–1_ and _xj_ . Equation (9.75) integrated over the reach: 



gives: 



The first term of Eq. (9.77) represents the variation in time of the water volume _S_ stored by the channel reach of length _�x_ since 



The second term of Eq. (9.77) represents the difference between the flow rates at the ends of the reach: 

9.4 Lumped Flood Routing Models 

391 



<!-- Start of picture text -->
h<br>Qj Qj  +1<br>t t<br>Q tj ( ) Q     tj  +1 ( )<br>datum<br>xj xj +1 x<br>Δ x<br>bottom<br><!-- End of picture text -->

**Fig. 9.7** Channel reach of length _�x_ considered as reservoir 



Substitution of Eqs. (9.78) and (9.79) in Eq. (9.77) yields the well known storage equation: 



where: 

_S_ – volume of water stored by channel reach of length _�x_ , _Qj–1_ ( _t_ ) – discharge entering a channel reach through end _xj–1_ , _Qj_ ( _t_ ) – discharge leaving a channel reach through end _xj_ . 

In the next step one function from storage equation is eliminated. For this purpose an additional equation relating storage, inflow and outflow is introduced. The most commonly used formula is (Chow 1959, 1964, Chow et al. 1988): 



where: 

_K_ – constant parameter expressed in time units, _ψ_ – weighting parameter ranging from 0 to 1. 

The parameter _K_ is interpreted as the time of traveling of the flood wave over the channel reach between the cross-sections _xj_ –1 and _xj_ . As the length of the reach is _�x_ = _xj_ – _xj_ –1, and the wave propagates with celerity _C_ , then the constant _K_ may be expressed as follows: 

9 Simplified Equations of the Unsteady Flow in Open Channel 

392 



Conversely to the parameter _K_ , the parameter _ψ_ has no physical interpretation. Equation (9.81) is differentiated with regard to time and next the obtained result is substituted in the storage equation. Finally one obtains the well known Muskingum model: 



Setting _ψ_ = 0 one obtains another very popular hydrological lumped model – the linear reservoir model: 



Rather than being represented by a single reservoir, the channel reach is usually conceptualized as a cascade of _N_ reservoirs as shown in Fig. 9.8. The water leaving the preceding reservoir enters the next one. Each reservoir operates according to Eq. (9.83), so in this equation the index of cross-section takes the values _j_ = 1, 2, 3, _. . ._ , _N_ . 

### **_9.4.2 Numerical Solution of the Muskingum Equation_** 

Equation (9.83) is an ordinary differential equation, which must be integrated using a numerical method. Since the considered channel reach is divided into _N_ reservoirs we obtain a system of _N_ such equations describing each reservoir. The input to the first reservoir _Q_ 0( _t_ ) for 0 ≤ _t_ ≤ _T_ represents the flood wave to be routed. Equation 



<!-- Start of picture text -->
x 1 x 2 x 3 x i  −1 x i x i +1 xN −1 x N x<br>I 1 I 2 I i − 1 I i IN − 1<br>Q 1 Q 2 Q 3 Qi Qi  +1 Q N<br>1 2 i −1 i N − 1<br><!-- End of picture text -->

**Fig. 9.8** Channel reach represented as a cascade of reservoirs 

9.4 Lumped Flood Routing Models 

393 

(9.83) is approximated using the implicit trapezoidal rule (3.21). This yields the following system of algebraic equations: 



where: 



Since in Eq. (9.85) only one unknown exists, then it can be split into separate equations, from which corresponding unknowns are calculated directly: 



The coefficients _α_ , _β_ and _γ_ are given by the following formulas: 







The flood wave _Q_ 0( _t_ ) specified as the input to the system is transformed using Eq. (9.86) with assumed values of the parameter _K_ and _ψ_ over the time interval ⟨0, _T_ ⟩. The output from the last reservoir is the solution of the considered flood routing problem. 

_Example 9.4_ The flood wave given by the following formula: 



where _Q_ 0 = 10 m3/s, _Q_ max = 75 m<sup>3</sup> /s, _t_ max = 4 h and _α_ = 0.85, propagates in an open channel. Using the Muskingum model with the following data: _N_ = 4, _K_ = 4 h, _�t_ = 0.5 h, let us examine the influence of the value of weighting parameter _ψ_ on the shape of hydrograph leaving the considered channel reach. 

The calculations were performed for a couple of values of the weighting parameter _Ψ_ . The results displayed in Fig. 9.9 show that they strongly depend on this parameter. Using the Muskingum model it is possible to obtain oscillating solution, even with negative discharge during the initial phase of wave. 

9 Simplified Equations of the Unsteady Flow in Open Channel 

394 



<!-- Start of picture text -->
Q  [m 3 /s]<br>80<br>Q  t 0 ( )<br>70<br>60 Ψ = 0.425<br>Ψ = 0.200<br>50<br>Ψ = 0.0<br>40<br>30<br>20<br>10<br>0<br>0 12 24 36 48 60 72 t  [h]<br><!-- End of picture text -->

**Fig. 9.9** Results of routing of the wave _Q_ 0( _t_ ) by the Muskingum model for various values of the parameter _ψ_ 

Note that for _�t_ = _K_ and for _ψ_ = 0.5 the coefficients of Eq. (9.86) take the following values: _α_ = 1, _β_ = 0, _γ_ = 0. Therefore this equation is reduced to a very simple relation: 



Let us remember that this formula coincides with the formula (6.117) given by the numerical solution of the linear advection equation using the method of characteristics or using the finite difference up-wind scheme (Eq. 5.108) with the advective Courant number equal to unity. Equation (9.88) ensures exact solution to the problem. Numerical tests confirm this conclusion. In Fig. 9.10 one can see pure translation of flood wave without any deformation of its shape. This property of the Muskingum model gives some insights into its nature. 

### **_9.4.3 The Muskingum–Cunge Model_** 

Comparing the Muskingum equation solved by the implicit trapezoidal rule (Eq. 9.85) and the pure advection equation solved by the difference box scheme one can notice their similarity. Equation (6.4) with _θ_ = 1/2 becomes: 

395 

9.4 Lumped Flood Routing Models 



<!-- Start of picture text -->
/s]<br>80<br>Q  t 0 ( ) Q  tN ( )<br>70<br>60<br>50<br>40<br>30<br>20<br>10<br>0<br>0 12 24 36 48 60 72 t  [h]<br><!-- End of picture text -->

##### _Q_ [m<sup>3</sup> /s] 

**Fig. 9.10** Pure translation of flood wave _Q_ 0( _t_ ) produced by the Muskingum model for _ψ_ = 0.5 and _�t_ = _K_ 



Taking into account the relation (9.82) we can see that Eq. (9.89) coincides with Eq. (9.85). For the first time this similarity was noticed by Cunge (1969), who concluded on the kinematic character of the Muskingum model and the numerical nature of the wave attenuation process. The accuracy analysis carried out for Eq. (9.89) using the modified equation approach shows that the applied approximation modifies the kinematic wave model to the form of advection-diffusion equation, known from Chapter 7: 



where _Dn_ is the coefficient of numerical diffusion defined as follows: 



Equation (9.90) indicates that the wave attenuation given by the Muskingum model has the same numerical roots as the kinematic wave equation. Simply, this effect is caused by the numerical diffusion. Cunge (1969) suggested to use such a value of the parameter _Ψ_ which ensures the numerical diffusivity (Eq. 9.91) equal 

396 

9 Simplified Equations of the Unsteady Flow in Open Channel 

to the hydraulic one present in the diffusive wave equation and given by Eq. (9.39), i.e. _D_ = _Dn_ . This condition implies that: 



or with the relation (9.82): 



where: 

Q – flow rate, _B_ – channel width, _s_ – bottom slope, _K_ – constant parameter, _C_ – kinematic celerity. 

In such a way Cunge related the value of weighting parameter _ψ_ not only to the flow rate and the kinematic celerity but to the channel parameters as well. Consequently the Muskingum model becomes capable to reproduce the solution of the linear diffusive wave model. This version of the Muskingum equation is commonly called Muskingum–Cunge model (see for instance Chow et al. 1988). However it should be remembered that Cunge’s approach does not change the character of the Muskingum model. The wave attenuation is not caused by the physical process but by the numerical error, although its intensity is determined by the parameter _ψ_ dependent on the channel parameters. 

Equivalence of the numerical solutions of the diffusive wave model and the Muskingum model is illustrated by the example presented below. 

_Example 9.5_ Consider a rectangular channel of length _L_ = 70 km, width _B_ = 50 m, bottom slope _s_ = 0.0004 and the Manning coefficient _nM_ = 0.040. The flood wave entering the upstream end is given by the following formula: 



where _Q_ 0 = 5 m<sup>3</sup> /s, _Q_ max = 50 m<sup>3</sup> /s, _t_ max = 6 h and _α_ = 1.0. Let us compare the form of hydrographs leaving the considered channel reach, calculated using the diffusive wave equation and the Muskingum–Cunge model. 

Assuming that the propagation is described by Eq. (9.34) with _C_ = const. and _D_ = const., the values of both parameters are calculated for the algebraic average values of flow discharge: _Q_ = ( _Q_ 0 + _Q_ max)/2. For the assumed data these parameters are as follows: 

9.4 Lumped Flood Routing Models 

397 





The auxiliary conditions are: 





Equation (9.34) is solved using the modified finite element method. Computations are performed for _�x_ = 2,000 m and _�t_ = 1,200 s. The obtained results _Q_ ( _L_ = 75 km, _t_ ) are shown in Fig. 9.11. 

The same wave propagation problem is next solved using the Muskingum–Cunge model (9.83). Equation (9.83) is solved using the implicit trapezoidal rule for the constant parameters _K_ and _Ψ_ given by Eqs. (9.82) and (9.93). As previously their values are calculated for the average flow discharge _Q_ : 





The hydrographs calculated at the downstream end for _�t_ = 1200 s are displayed in Fig. 9.11. 



<!-- Start of picture text -->
Q  [m 3 /s]<br>q ( t )<br>50<br>Q ( L , t )<br>40<br>30<br>20<br>10<br>0<br>0 24 48 72 t  [h]<br><!-- End of picture text -->

**Fig. 9.11** Comparison of the results given by the diffusive wave equation ( _solid line_ ) and the Muskingum–Cunge model ( _dotted line_ ) 

9 Simplified Equations of the Unsteady Flow in Open Channel 

398 

Note that both models indeed produce equivalent numerical solutions. Thus instead of the diffusive wave equation one can use the Muskingum–Cunge equation which is simpler to solve numerically 

### **_9.4.4 Relation Between the Lumped and Simplified Distributed Models_** 

The similarity of the approximated forms of the kinematic wave equation and the Muskingum equation presented in the preceding section allows us to deduce on the nature of the lumped models. In fact the Muskingum model should be regarded as a semi-discrete form of the kinematic wave equation. Moreover we can estimate directly from Eq. (9.83) the numerical diffusion generated by this model. To this end let us consider the linear kinematic wave model (Eq. 9.37 with _C_ = const. and _D_ = 0). This equation can be discretized in space only. The approximation carried out at point _P_ located between the nodes _j_ – 1 and _j_ (Fig. 9.12 and 9.13) gives: 



where _Qp_ represents the discharge at the point _P_ . 

The value of _Qp_ can be calculated by the linear interpolation between the nodes _j_ – 1 and _j_ : 





**Fig. 9.12** Discretization of the _x_ axis for numerical solution of the kinematic wave equation 

**Fig. 9.13** Linear interpolation between neighboring nodes applied for the kinematic wave equation 



<!-- Start of picture text -->
Q<br>Qp<br>x P x x<br>j  −1 j<br>(1−ψ) Δ x ψΔ x<br>Δ x<br><!-- End of picture text -->

9.4 Lumped Flood Routing Models 

399 

Equation (9.95) can be rewritten in the following form: 



where _ψ_ is defined as: 



Note that _ψ_ can be considered as a weighting parameter ranging from 0 to 1. Substituting Eq. (9.96) in Eq. (9.94) and including Eq. (9.82) yields the Muskingum model in the form of Eq. (9.83): 



The performed spatial discretisation of the kinematic wave equation introduces a numerical error caused by the truncation of the Taylor series. In order to estimate this error one can carry out the consistency analysis. The nodal values of _Q_ in Eq. (9.98) are replaced by the Taylor series expansion around point P: 



Substitution of Eqs. (9.99) and (9.100) in Eq. (9.98), including the terms of 2nd order, yields the modified equation in the form: 



According to the condition of consistency, which must be satisfied by any approximation of the partial differential equation, the modified equation should tend to the governing equation for _�x_ → 0 (Fletcher 1991). For _�x_ → 0 the time of wave translation along the channel reach of the length _�x_ simultaneously tends to zero ( _K_ → 0). Therefore we have 



and consequently for _�x_ → 0 Eq. (9.101) tends to the kinematic wave equation. This fact proves that the Muskingum model is an approximation of the kinematic wave. This approximation introduces a numerical diffusion. Its coefficient is: 

9 Simplified Equations of the Unsteady Flow in Open Channel 

400 



This expression coincides with Eq. (9.91) proposed by Cunge (1969). One can add that the numerical diffusion is caused by the spatial approximation only. An additional diffusion can be generated while integrating Eq. (9.98) over time by a method of the order lower than two. Usually the implicit trapezoidal rule is applied. It ensures an accuracy of 2nd order with regard to _t_ and consequently this approximation is dissipation free. 

Summarizing, one can say that the numerical solution of the Muskingum model is in fact equivalent to the numerical solution of the kinematic wave model by the method of lines. In this approach a solution of the partial differential equation is made in two stages. At first it is discretised in space leading to a system of ordinary differential equations over time. Next, this system is integrated using any well known method of the numerical solution of an initial problem for the ordinary differential equations. 

The classical derivation of the Muskingum model bases on the storage equation (9.80) completed by the relationship (9.81). Therefore it is interesting to show how numerical diffusion is introduced into this model. To explain this problem let us consider the Muskingum model (Eq. 9.98) rewritten in more general form: 



with _Qp_ defined by Eq. (9.96). 

We can show that this equation can be derived directly from the storage equation (9.80) without any additional formula relating storage, inflow and outflow (Szymkiewicz 2002). To do this we have to assume the following: 

- the storage _S_ is calculated numerically, 

- the equation for uniform steady flow is applied. 

Using both above assumptions one can transform Eq. (9.80) into (9.104). The storage _S_ can be calculated as follows: 



where _Ap_ , being a cross-sectional area at the point _P_ (Fig. 9.12), can be expressed as a function of _Qp_ using the Manning (or Chézy) formula: 



with _α_ and _m_ given by Eqs. (9.14a) and (9.14b), respectively. Therefore the left hand side of Eq. (9.80) can be rewritten as follows: 

9.5 Convolution Integral in Open Channel Hydraulics 

401 



After differentiating with _α_ = const. one obtains: 



Because the kinematic wave celerity at the point _P_ is defined as 



the right side of Eq. (9.107) takes the form: 



Finally the left hand side of Eq. (9.104) was obtained from the left hand side of Eq. (9.80). Therefore it seems reasonable to accept that an additional formula (9.81) used to derive the lumped models from the storage equation has double meaning. It can be interpreted as a result of the numerical integration of storage and of the application of the steady uniform flow equation. A numerical diffusion is introduced by the numerical calculation of the storage _S_ . Note that the kinematic wave model is based on the same equations i.e. the equation of continuity and the steady flow equation. 

As far as the conservative properties of the Muskingum model are considered, its linear version satisfies both mass and momentum conservation principles. However, sometimes the variable parameters _K_ and _ψ_ are introduced into the model. After Tang et al. (1999) this approach generates the mass balance error. Such error can be expected if the governing equation is not written in the appropriate conservative form. As it was shown earlier, the Muskingum model can be considered as the semidiscrete form of the kinematic wave equation. Consequently both models should have similar properties. 

### **9.5 Convolution Integral in Open Channel Hydraulics** 

### **_9.5.1 Open Channel Reach as a Dynamic System_** 

An open channel reach of length _L_ can be considered as a dynamic system, which is able to transform a flood wave appearing at the upstream end to the one observed at the downstream end (Fig. 9.14). 

In other words, an input to the system is turned into an output leaving this system, as it is shown in Fig. 9.15. Our goal is to identify the physical mechanism, which 

9 Simplified Equations of the Unsteady Flow in Open Channel 

402 



<!-- Start of picture text -->
Open channel I ( t )<br>Q ( t )<br>t<br>t<br>A B<br>input operator output<br>Ω<br>I ( t ) Q ( t )<br><!-- End of picture text -->

**Fig. 9.14** Open channel reach as a dynamic system 

**Fig. 9.15** Symbolic representation of the dynamic system 

determines the way of transformation, what means that we are looking for the operator _�_ representing this process. This operator allows us to compute the output of the system for any input _I_ ( _t_ ) entering this system, i.e.: 



The mechanism of transformation can be deduced via the analysis of flow process using the appropriate principles of conservation. Such an approach has been applied in the preceding chapters, in which various mathematical models of unsteady flow were derived. Then the operator _�_ took the forms of differential equations as the system of Saint Venant equations, the diffusive wave equation, the kinematic wave equation etc. 

In the case of lumped linear systems it is possible to describe their dynamic behavior using either the differential flow equations or an impulse response function, which is the reaction of the system to the input in form of unit quantity entering instantaneously. Both approaches are equivalent. If we consider the open channel flow as a linear process, then it can be described by the previously presented differential equations in linear forms or by an impulse response function. Application of the impulse response function has two advantages. Firstly, such an approach does not require physical analysis of the flow. Secondly, knowing an impulse response function one can compute an output for any input in a simple way, without the difficulties related to the numerical integration of differential equations. 

The system’s linearity means that the principles of proportionality and superposition are valid. Therefore, if input _I_ 1( _t_ ) causes output _Q_ 1( _t_ ), whereas _I_ 2( _t_ ) gives rise to reaction _Q_ 2( _t_ ), then input in the form _I_ ( _t_ ) = _C_ 1· _I_ 1( _t_ )+ _C_ 2· _I_ 2( _t_ ) will cause the following output _Q_ ( _t_ ) = _C_ 1· _Q_ 1( _t_ )+ _C_ 2· _Q_ 2( _t_ ), where _C_ 1 and _C_ 2 are arbitrary 

9.5 Convolution Integral in Open Channel Hydraulics 

403 

constants. These principles allow us to decompose a complex input into simpler components, compute the outputs corresponding to the subsequent components and add the results of computations to obtain the final output. 

Any lumped linear system can be described by the following ordinary differential equation of _m_ th order (Chow et al. 1988): 



where: 

_I_ ( _t_ ) – function entering the system, 

_Q_ ( _t_ ) – function leaving the system, 

_Ai_ ( _t_ ), _Bi_ ( _t_ ) ( _i_ = 0,1, _. . ._ , _m_ ) – time-variable coefficients describing dynamic properties of the system. 

Usually the scale of the time variation of the dynamic properties is incomparable with the one related to the flow process. In such a case one can assume that the coefficients _Ai_ and _Bi_ are constant in time. Then Eq. (9.112) takes the form: 



Equation (9.113) describes the time-invariant system, in which the way of transformation of _I_ ( _t_ ) into _Q_ ( _t_ ) is still the same. This means that the same flood wave at the upstream channel end will produce the same wave at the downstream end at any time. In other words, the dynamic properties of channel reach are constant in time. 

For the following initial conditions: _I_ ( _t_ = 0) = 0 and _Q_ ( _t_ = 0) = 0, Eq. (9.113) has the following solution (Korn and Korn 1968): 



_w_ ( _t_ ) – impulse response function, _τ_ – dummy parameter. 

The integral in Eq. (9.114) is called convolution integral. The function _w_ ( _t_ – _τ_ ) represents globally the dynamic properties of the considered system, since it determines the way of transformation an input into an output. This function is a reaction of the system to an input in the form of unit impulse. The unit impulse is a signal of short duration having unit magnitude: _X_ · _�t_ = 1. In the limit, when _�t_ tends to zero, _X_ tends to infinity and the impulse becomes the Dirac delta function given by the following expression (McQuarrie 2003): 

9 Simplified Equations of the Unsteady Flow in Open Channel 

404 



The Dirac delta function has the following properties: 



where _f_ ( _t_ ) is an arbitrary function. An essential feature of this function is that instead of any value of _f_ ( _t_ ) it is capable to introduce the value of _f_ ( _τ_ ): _f_ ( _t_ )→ _f_ ( _τ_ ). The function _w_ ( _t_ – _τ_ ), being the response of system to a unit impulse, is defined as follows (Fig. 9.16): 



<!-- Start of picture text -->
q Q<br>I( t ) = δ ( t −τ) Q ( t ) = h ( t −τ)<br>τ t τ p t<br><!-- End of picture text -->

**Fig. 9.16** Interpretation of the response function 

If 



then 



Therefore, the response function is an output of the system when an input has the form of Dirac delta function. If the system conserves the mass: 



then the function _w_ ( _t_ ) satisfies the following condition: 



9.5 Convolution Integral in Open Channel Hydraulics 

405 

Moreover this function: 

- has non-negative values only: _w_ ( _t_ ) ≥ 0 for _t_ ≥ 0, 

- has one extreme point (maximum), 

- is equal to zero for negative argument: _w_ ( _t_ ) = 0 for _t_ ≤ 0, 

- tends to zero as time tends to infinity: _w_ ( _t_ )→ 0 for _t_ →∞. 

If the functions _I_ ( _t_ ) and _Q_ ( _t_ ) represent the same quantity and they have the same dimension, the function _w_ ( _t_ ) is expressed in the inverted time units as s<sup>−1</sup> , h<sup>−1</sup> etc. 

In hydrology the function _w_ ( _t_ ) is called Instantaneous Unit Hydrograph (IUH). This term was introduced in the 1960 s as a generalization of the unit hydrograph theory proposed by Sherman in 1932 for direct runoff from catchments (Chow et al. 1988). 

For the convolution integral the principle of symmetry is valid. Accordingly to this rule, Eq. (9.114) can be rewritten as: 



Since an input from distant past does not influence the current output, then we can introduce the parameter _p_ representing “the system memory”. This is a time interval in which the ordinates of IUH differ significantly from zero (Fig. 9.17). 

As _w_ ( _t_ ) tends to zero for _t_ →∞, then the following condition will be satisfied: 



where _ε_ is a small positive number. One can notice, that for _t_ > _p_ the product under the integral (9.122) is close to zero. Then in Eq. (9.122) the upper integral limit can be changed as follows: 



<!-- Start of picture text -->
w<br>ε<br>p t<br><!-- End of picture text -->

**Fig. 9.17** Illustration of the system memory 

406 

9 Simplified Equations of the Unsteady Flow in Open Channel 



where _p_ is the system memory. Therefore, if we want to compute the function _Q_ at any moment _t_ , we must known the function _I_ ( _t_ ) not only at this moment, but also in the time interval ⟨ _t_ – _p_ , _t_ ⟩. 

As the value of _p_ is determined by the parameter _ε_ , then it is obvious that _w_ ( _t_ ) does not satisfy the condition (9.121). We have: 



and consequently the mass balance error will be generated because: 



where _T_ is time of flood wave duration. To eliminate this incompatibility, the ordinates of function _w_ ( _t_ ) should be rescaled. This can be done in the following way: 

**–** integrate numerically the function _w_ ( _t_ ) in interval ⟨0, _p_ ⟩ 



where _�t_ is time step, whereas _P_ = _p_ / _�t_ +1 is discrete memory; 

**–** calculate the value of correction corresponding to a unit ordinate of function _w_ ( _t_ ): 



**–** correct the ordinates of the function _w_ ( _t_ ) proportionally to their values: 



where _w_<sup>∗</sup> _j_<sup>is corrected value of</sup><sup>_wj_.</sup> 

9.5 Convolution Integral in Open Channel Hydraulics 

407 

### **_9.5.2 IUH for Hydrological Models_** 

Determination of the function _h_ ( _t_ ) for the considered system can be performed using two approaches. The first approach bases on the observed functions _I_ ( _t_ ) and _Q_ ( _t_ ) only. No additional information on the system is used. When the function _I_ ( _t_ ) and _Q_ ( _t_ ) are known, Eq. (9.124) is the Volterra integral equation of the first type with _w_ ( _t_ ) as a kernel function (Korn and Korn 1968). Solution of this equation gives the function _w_ ( _t_ ). There are many techniques to solve this problem. Some of them, oriented to model the direct runoff processes, were proposed by O’Donnell (1960), Chow (1964), Nash (1957), Rodriguez-Iturbe and Valdes (1979) among others. Since these methods are rather less useful for open channel flow modeling they will not be considered here. For the flood routing more suitable is the second possible way of determination of the function _w_ ( _t_ ). This approach can be applied on condition that the linear differential equation describing the considered system is known. In such a case one can solve this equation for such auxiliary conditions, which ensure solution in the form of impulse response function _w_ ( _t_ ). This approach is very popular and frequently used. 

The first example concerns the diffusive wave equation (9.34) derived in Section 9.2.2: 



With constant wave icelerity _C_ , constant hydraulic diffusivity _D_ and for some specified initial-boundary conditions Eq. (9.130) may be solved analytically. For instance assuming that: 

- _Q_ ( _x_ , _t_ = 0) = 0 for _x_ ≥ 0, 

- _Q_ ( _x_ = 0, _t_ ) = _δ_ ( _t_ ), 

- _Q_ ( _x_ = _L_ , _t_ ) = 0 for _L_ →∞, 

one obtains the following exact solution: 



Equation (9.131) holds for _t_ > 0 and for _x_ ≥ 0. This equation has been obtained by Hayami (Eagleson 1970). Since the assumed conditions correspond to the definition of the IUH, then Eq. (9.131) can be considered as the instantaneous unit hydrograph of a channel reach of length _L_ . Consequently one can write: 



Let us consider the second simplified model, i.e. the kinematic wave equation (9.19). It is well known that the linear advection equation 

9 Simplified Equations of the Unsteady Flow in Open Channel 

408 



implies that the flood wave occurring at the upstream end propagates along channel axis without any shape deformation. Taking into account Eq. (9.117) one can find out, that for the linear kinematic wave equation (9.133) implemented for a channel reach of length _L_ , IUH has the form of Dirac delta function: 



where _L_ is length of channel reach and _C_ is kinematic wave speed. The ratio _L_ / _C_ represents the lag time between the upstream end and considered cross-section. Note that the same result is obtained from Eq. (9.132). For _D_ = 0, IUH of the diffusive wave equation becomes the Dirac delta function, which is IUH of the kinematic wave equation. 

The flood routing can be carried out with hydrological lumped models as well. They were discussed in the preceding section. One of the most popular of them is the Muskingum equation: 



where: 

_I_ ( _t_ ) – inflow, _Q_ ( _t_ ) – outflow, 

_ψ_ – weighting parameter, 

_K_ – time of wave translation between the considered cross-sections. 

The IUH for the Muskingum model was proposed by Venetis (1969). This equation, obtained by the solution of Eq. (9.135) using the Laplace transformation approach, is following: 



The next example of determination of appropriate IUH concerns the linear reservoir described by Eq. (9.135) with _ψ_ = 0, i.e. by: 



Comparing this equation with Eq. (9.113), one can notice that they coincide, since _A_ 1 = 1, _A_ 0 = 1/ _K_ , _B_ 0 = 1/ _K_ , and other coefficients are equal to zero. Then the convolution integral is the solution of Eq. (9.137) as well. The IUH for this equation can be determined by its time integration performed for the following conditions: _Q_ ( _t_ ) = 0 for _t_ ≤ 0 and _I_ ( _t_ ) = _δ_ ( _t_ ). Following the developments presented for instance 

9.5 Convolution Integral in Open Channel Hydraulics 

409 



<!-- Start of picture text -->
w<br>0.2<br>0.1<br>0.0<br>2     4    6     8   10  12    14  16   18  20 t<br><!-- End of picture text -->

**Fig. 9.18** Graph of the function (9.138) for _K_ = 5 h 

by Chow et al. (1988), one obtains: 



An example of the function _w_ ( _t_ ) given by Eq. (9.138) is show in Fig. 9.18. Note that Eq. (9.136) with _ψ_ = 0 coincides with Eq. (9.138). 

Usually to obtain satisfying results it is necessary to apply multiple linear reservoirs in a cascade. The first reservoir is analysed as a single one, so its output is following: 



The second reservoir, having IUH in the form of Eq. (9.138), transforms _Q_ 1( _t_ ) into _Q_ 2( _t_ ) according to the convolution integral (9.122), i.e.: 



This function is transformed by 3rd reservoir etc. Application of the same procedure for consecutive reservoirs in series gives (Nash 1957): 



where _N_ is a number of the reservoirs in series, whereas _Γ_ ( _N_ ) is the gamma Euler function. This IUH was proposed by Nash (1957) and is called the Nash model (Chow et al. 1988). In Figs. 9.19 and 9.20 are displayed the graphs of function (9.141) calculated for various values of its parameters _K_ and _N_ . 

Unfortunately the IUHs in form of Eqs. (9.136) and (9.141) have some disadvantages which limit their application. Namely it is impossible to achieve satisfying agreement between the results of calculation and experimental data when the time 

9 Simplified Equations of the Unsteady Flow in Open Channel 

410 



<!-- Start of picture text -->
w  [h   ]−1<br>0.20<br>K = 2 h<br>0.15<br>0.10<br>K = 4 h<br>0.05 K = 8 h<br>0.00<br>0 10 20 30 40 50 t  [h]<br><!-- End of picture text -->

**Fig. 9.19** Function _w_ ( _t_ ) with _N_ = 2 for various values of _K_ 



<!-- Start of picture text -->
w  [h   ]−1<br>0.20<br>N = 2<br>0.15<br>N = 4<br>0.10<br>N = 6<br>0.05<br>0.00<br>0 10 20 30 40 50 t  [h]<br><!-- End of picture text -->

**Fig. 9.20** Function _w_ ( _t_ ) with _K_ = 2 h for various values of _N_ 

lag of the output is considerable. Both IUHs are unable to reproduce the effect of pure translation. For this reason very often the linear reservoir model is used jointly with the model of linear channel (Dooge 1959, Chow 1964). Moreover the IUH for Muskingum model can produce the negative ordinates. This is caused by the second term of Eq. (9.136) (Strupczewski et al. 1989). This feature disagrees with the definition of the instantaneous unit hydrograph which has to be always non–negative: _w_ ( _t_ ) ≥ 0 for _t_ ≥ 0. Consequently it can produce some unrealistic effects in form of the initial oscillations in the hydrograph calculated at the downstream end. Similar problems can be observed in the numerical solution of the Muskingum model in form of Eq. (9.135). 

It is well known that the Muskingum equation integrated in time by the method, which does not produce any numerical diffusion, is capable to ensure a pure translation of flood wave for _ψ_ = 0.5. For this reason it seems reasonable to expect the similar effect while using the IUH in form of Eq. (9.136). Therefore this equation should become the Dirac delta function for _ψ_ = 0.5. Unfortunately Eq. (9.136) does not fulfil this condition. The discrepancy is caused by the nature of Eq. (9.135). In fact this equation is a semi-discrete form of the kinematic wave equation obtained 

9.5 Convolution Integral in Open Channel Hydraulics 

411 

by its spatial discretization. For this reason it contains a numerical error introduced during the approximation. Because the IUH in form of Eq. (9.136) was derived by an analytical integration of Eq. (9.135) it contains implicitly this error as well. It has the form of numerical diffusion which disappears for _ψ_ = 0.5 i.e. when the approximation of spatial derivative is made by centred difference. 

### **_9.5.3 An Alternative IUH for Hydrological Lumped Models_** 

It is possible to derive a general instantaneous unit hydrograph for all lumped models which is free from the mentioned disadvantages (Szymkiewicz 2002). To this end the IUH for the diffusive wave (Eq. 9.132) can be applied. As it was obtained by an analytical solution of Eq. (9.130) then it does not contain any numerical error. On the other hand it is known, that the results given by the lumped models are similar to the ones given by the diffusive wave model due to the numerical diffusion. 

As it was showed in Section 9.4.4 the Muskingum model is an approximation of the kinematic wave. This approximation introduces a numerical error. The accuracy analysis carried out for the Muskingum equation showed that it modifies the kinematic wave model to the form similar to the diffusive wave model (9.130): 



where _Dn_ is the coefficient of numerical diffusion defined as follows: 



Let us remember that the kinematic character of the Muskingum model as well as the numerical nature of the wave attenuation process was noticed by Cunge (1969), who suggested such value of the parameter _Ψ_ which ensures the numerical diffusivity (Eq. 9.143) equal to the hydraulic one given by Eq. (9.35) i.e. _D_ = _Dn_ . Owing to this assumption the Muskingum model can reproduce the solution of the linear diffusive wave model. This version of the Muskingum model is known as Muskingum–Cunge one (Chow et al. 1988). 

If the lumped models, being semi-discrete forms of the kinematic wave model, are able to reproduce the solution of the diffusive wave, then one can expect that the reproduction of this solution using the instantaneous unit hydrograph will be possible as well. Therefore one can apply the IUH of the diffusive wave model for the lumped systems. For this purpose let us introduce the parameters typical for the lumped models into Eq. (9.132). The hydraulic diffusivity, the kinematic speed and the length of a channel can be replaced by the following expressions: 



9 Simplified Equations of the Unsteady Flow in Open Channel 

412 





where _N_ corresponds to the number of reservoirs. Substitution of Eq. (9.144) in Eq. (9.132) yields : 



This equation can be considered as an instantaneous unit hydrograph of the Muskingum model for a channel reach of length _L_ . With the parameter _ψ_ defined by Eq. (9.92) the formula (9.145) can be considered as an instantaneous unit hydrograph of the Muskingum – Cunge model. Of course, this will take place on condition that _ψ_ is assumed to be constant. 

The function (9.145) has the following properties: 

- it holds for _ψ_ ≤ 1/2 only, including the negative values as well; 

- for _ψ_ → 1/2 _w_ ( _t_ ) → _δ_ ( _t_ – _N_ · _K_ ); 

- _w_ ( _t_ ) ≥ 0 for _t_ > 0; 

- the parameter _N_ can be any positive number, not necessarily an integer. 

Some of the properties listed above are illustrated in the figures. In Fig. 9.21 the IUHs for _N_ = 2, _ψ_ = 0.4 and for various values of _K_ are plotted. In Fig. 9.22 the graphs of the IUHs for _K_ = 3 h, _ψ_ = 0 and for various values of parameter _N_ are plotted. 



<!-- Start of picture text -->
w<br>0.4<br>K = 2 h<br>0.3<br>0.2<br>K = 4 h<br>0.1 K = 6 h<br>0.0<br>0            10            20           30           40           50 t  [h]<br><!-- End of picture text -->

**Fig. 9.21** Instantaneous unit hydrographs of the Muskingum model for _N_ = 2, _ψ_ = 0.40 and for various values of _K_ 

9.5 Convolution Integral in Open Channel Hydraulics 

413 



<!-- Start of picture text -->
w<br>0.25<br>N = 2<br>0.20<br>N = 4<br>0.15<br>0.10<br>N = 6<br>0.05<br>0.00<br>0 10 20 30 40 50 t  [h]<br><!-- End of picture text -->

**Fig. 9.22** Instantaneous unit hydrographs of the Muskingum model for _K_ = 3 h, _ψ_ = 0 and for various values of _N_ 



<!-- Start of picture text -->
w<br>0.20<br>ψ = 0.45<br>0.16<br>0.12<br>ψ = 0.35<br>0.08<br>ψ = 0.0<br>0.04<br>0.00<br>0            10            20           30           40           50 t  [h]<br><!-- End of picture text -->

**Fig. 9.23** Instantaneous unit hydrographs of the Muskingum model for _N_ = 3, _K_ = 4 h and for various values of _ψ_ 

The shape of _w_ ( _t_ ) is mainly determined by parameter _ψ_ , whereas its position along the axis _t_ depends on the parameters _N_ and _K_ . With increasing _ψ_ the IUH becomes more and more steep (see Fig. 9.23). For the extreme case when _ψ_ = 0.5 its value tends to infinity at the point _t_ = _N_ · _K_ = 18. It becomes the Dirac delta function. 

Implementation of the IUH requires determining the values of the parameters _K_ , _N_ and _ψ_ . They can be computed using the method of moments or the method of optimisation. Both approaches need the hydrographs observed at the upstream and downstream ends of a channel. The subsequent moments are given by Szymkiewicz (2002): 

For _ψ_ = 0 Eq. (9.145) becomes an alternative IUH for a cascade of the linear reservoirs: 

414 9 Simplified Equations of the Unsteady Flow in Open Channel 



whereas for _N_ = 1 it becomes an alternative IUH for a single reservoir: 



Both hydrographs presented above differ from the classical ones given by Eqs. (9.138) and (9.141). This difference results from the manner of derivation of both types of IUHs. Classical IUH for the linear reservoir was obtained by integration of Eq. (9.137) resulting from a spatial discretisation of the kinematic wave model. Consequently a mechanism of numerical diffusion was included implicitly. Conversely, Eq. (9.132) represents an analytical solution of the diffusive wave model with regard to both variables _x_ and _t_ . It is interesting that although the classical IUH for a cascade of linear reservoirs in series and the IUH in form of Eq. (9.146) are different, they have the same first and second moments (Szymkiewicz 2002). 

_Example 9.6_ Using the Muskingum model solved by both the finite difference approximation (Eq. 9.86) and the convolution approach with the IUH given by Eq. (9.145), let us carry out flood routing of the following wave imposed at the upstream: 



with _qb_ = 5 m<sup>3</sup> /s, _qm_ = 75 m<sup>3</sup> /s, _tm_ = 6 h. 

In Fig. 9.24 the results of flood routing using the convolution integral are presented. They are obtained for _K_ = 6 h and _N_ = 3 and for various values of the parameter _ψ_ . Note that the wave attenuation depends on the value of _ψ_ . The wave damping becomes more pronounced for decreasing _ψ_ . On the other hand, for increasing value of _ψ_ the attenuation of the calculated output is reduced. For _ψ_ = 0.49 damping is so small that practically pure translation of the wave is obtained. In this case the lag time of wave centres of gravity is equal to _N_ · _K_ = 18 h. Regardless of the assumed set of data smooth solution is obtained always. 

Conversely, while solving numerically the Muskingum model physically unrealistic results can be very often obtained. Such a situation is presented in Fig. 9.25. For the same flood wave impose at the upstream end the Muskingum model with _N_ = 3, _K_ = 6 h and _ψ_ = 0.40 solved numerically using the classical scheme of the finite difference method (Eq. 9.86) produces the discharge lower than one imposed at upstream end. It takes even negative values. 

The examples presented above show considerable flexibility of the IUH in the form of Eq. (9.145). An appropriate set of the parameters _K_ , _N_ and _ψ_ ensure both required effects, i.e. the wave translation and its attenuation. Note that the parameter _ψ_ can take a negative value as well. On the other hand, the parameter _N_ does not have to be an integer. Using IUH and the convolution approach one can avoid 

415 

References 



<!-- Start of picture text -->
q ,  Q<br>[m  /s]3<br>q ( ) t<br>80<br>Q ( t ) with Ψ = 0.45<br>Q ( t ) with Ψ = 0.20<br>60<br>40<br>20<br>0<br>0 12 24 36 48 60 72 t  [h]<br><!-- End of picture text -->

**Fig. 9.24** An example of food routing by the Muskingum model using the convolution integral for _N_ = 3, _K_ = 6 h and for various values of the parameter _ψ_ 



<!-- Start of picture text -->
q ,  Q<br>[m  /s]3<br>80 q ( t )<br>Q ( t ) with IUH<br>60 Q ( t ) with Muskingum<br>40<br>20<br>0<br>0 12 24 36 48 60 72 t  [h]<br><!-- End of picture text -->

**Fig. 9.25** A comparison of the solutions of the Muskingum model by the finite difference method and by the convolution integral with the IUH for _N_ = 3, _K_ = 6 h and _ψ_ = 0.40 

all negative numerical effects arising while solution of the ordinary differential equations. 

### **References** 

- Abbott MB (1979) Computational hydraulics-Elements of the theory of free surface flow. Pitman, London 

Cappelaere B (1997) Accurate diffusive wave routing. J. Hydr. Engng. ASCE 123 (3):174–181 Chow VT (1964) Handbook of applied hydrology. McGraw-Hill, New York Chow VT (1959) Open channel hydraulics. Mc Graw-Hill, New York 

Chow VT, Maidment DR, Mays LW (1988) Applied hydrology. McGraw-Hill, New York 

416 

9 Simplified Equations of the Unsteady Flow in Open Channel 

Cunge JA (1969) On the subject of a flood propagation computation method (Muskingum method). J. Hydr. Res. 7 (2):205—229 

Cunge J, Holly FM, Verwey A (1980) Practical aspects of computational river hydraulics. Pitman Publishing, London 

Dooge JCI (1959) A general theory of the unit hydrograph. J. Geophys. Res. 64 (1):205—230 Eagleson PS (1970) Dynamic hydrology. McGraw-Hill, New York 

Fletcher CAJ (1991) Computational techniques for fluid dynamics, vol. I. Springer-Verlag, Berlin Gasiorowski D, Szymkiewicz R (2007) Mass and momentum conservation in the simplified flood routing models. J. Hydrol. 346:51–58 

Gresho PM, Sani RL (2000) Incompressible flow and the finite–element method, vol. 1: advectiondiffusion. Wiley, Chichester, England 

Hayami S (1951). On the propagation of flood waves. Kyoto Univ. Disaster Prevent. Res. Inst. Bull. 1:1–16 

Henderson FM (1966) Open channel flow. Macmillan Company, New York 

Korn GA, Korn TM (1968) Mathematical handbook for scientists and engineers, 2nd edn. McGraw-Hill, New York 

- Lighthill MJ, Whitham GB (1955) On kinematic waves, I: flood movement in long rivers. Proc. R. Soc. London, Ser. A 229:281–316 

- McQuarrie DA (2003) Mathematical methods for scientists and engineers. University Science Books, Sausalito, CA 

Miller WA, Cunge JA (1975) Simplified equations of unsteady flow. In: Mahmood K, Yevjewich V (eds) Unsteady flow in open channels. Water Resources Publishing, Fort Collins, CO 

Nash JE (1957) The form of Instantaneous Unit Hydrograph. IASH Publication no. 45, 3–4: 114–121 

O’Donnell T (1960) Instantaneous unit hydrograph derivation by harmonic analysis. IASH Publication no. 51:546–557 

- Ponce VM (1990) Generalized diffusion wave with inertial effects. Water Resour. Res. 26 (5):1099–1101 

- Ponce VM, Li RM, Simmons DB (1978) Applicability of kinematic and diffusion models. J. Hydr. Div. ASCE 104 (3):353–360 

- Rodriguez-Iturbe I, Valdes JB (1979) The geomorpholigic structure of hydrologic response. Water Resour. Res. 15 (6):1409–1420 

- Singh VP (1996) Kinematic wave modeling in water resources: surface water hydrology. Wiley, New York 

- Strupczewski WG, Napiórkowski JJ, Dooge JCI (1989) The distributed Muskingum model. J. Hydrol. 111:235–257 

- Szymkiewicz R (2002) An alternative IUH for the hydrologic lumped models. J. Hydrol. 259:246—253 

- Tang X, Knight DW, Samuels PG (1999) Variable parameters Muskingum–Cunge method for flood routing in a compound channel. J. Hydr. Res. 37 (5):591—614 

## **Index** 

###### **A** 

Accuracy analysis, 231, 251, 308 Advection, 35 Advection equation, 161, 170, 194, 219, 235, 239, 253, 375, 383, 395, 407 Advection-diffusion equation, 43, 49, 178, 237 Advective Courant number, 196, 264 Amplification factor, 215 Amplification matrix, 323 Amplitude error, 225 Approximation of the derivatives, 88, 185 Average flow velocity, 3 A-stability, 103 

###### **B** 

Backward difference, 88 Banded matrix, 71 Biochemical oxygen demand, 287 Bisection method, 54 Boundary conditions, 169, 333, 349 Boundary value problem, 107 Box scheme, 219, 302 

Concentration, 34 Consistency, 211 Convergence, 209 Convolution integral, 291, 403 Coriolis coefficient, 6 Correction factor of the energy, 6, 18 Correction factor of the momentum, 18, 23 Crank-Nicolson scheme, 250, 268–269 Critical depth, 7 Critical flow, 7 Critical slope, 8 

###### **D** 

Dam-break problem, 355, 362 Depth of flow, 1 Deviation of the flow velocity, 19 Diffusion equation, 175, 178, 203 Diffusive Courant number, 215, 264, 268 Diffusive wave equation, 369, 373, 411 Dimensionless wave number, 214 Discharge, 3 Dissolved oxygen, 287 Donea approach, 244 

###### **C** 

Centered difference, 89 CFL condition, 216 Characteristics, 161, 165, 171, 174, 347 Ch´ezy coefficient, 8 Ch´ezy equation, 8 Coefficients of convergence, 226 Coefficients of dispersion, 39 Coefficients of hydraulic diffusivity, 375 Coefficients of molecular heat conductivity, 45 Coefficients of numerical dispersion, 236, 242, 252, 268, 310, 326, 361 Coefficients of numerical diffusion, 236, 242, 252, 268, 310, 326, 361, 411 Coefficients of turbulent heat conductivity, 45 Coefficient of turbulent viscosity, 11 

###### **E** 

Error of approximation, 99 Euler-Cauchy method, 95 Exner equation, 344 Explicit Euler method, 89, 91, 250 

###### **F** 

False position method, 56 Fick’s Ist law of diffusion, 35 Finite difference method, 183, 219, 265 Finite differences, 87 Finite element method, 197, 239 Flow area, 2 Forward difference, 88 Froude number, 7 

R. Szymkiewicz, _Numerical Modeling in Open Channel Hydraulics_ , Water Science and Technology Library 83, DOI 10.1007/978-90-481-3674-2, ⃝C Springer Science+Business Media B.V. 2010 

417 

Index 

418 

###### **G** 

Galerkin method, 199 Gauss elimination method, 72 Gradually varied flow, 9 

###### **H** 

Holly-Preissmann method, 256 Hybrid methods, 66 Hydraulic depth, 2 Hydraulic radius, 3 Hyperbolic equations, 160, 162, 165 

###### **I** 

Implicit Euler method, 90, 92, 250 Implicit trapezoidal rule, 90, 93 Improved Euler method, 95 Initial conditions, 169, 333, 349 Initial-value problem, 85, 104, 116 Instantaneous Unit Hydrograph, 405 

###### **K** 

Kinematic wave equation, 369, 372 Kinematic wave celerity, 373 

###### **L** 

Longitudinal bed slope, 2 LU decomposition method, 76 Lumped models, 392 

###### **M** 

Manning equation, 8 Manning roughness coefficient, 8 Mass conservation law, 10 Mass transport equation, 33 Method of characteristics, 253 Mild slope, 8 Modified equation approach, 231, 242, 308, 399 Modified finite element method, 246, 279, 313, 358 Momentum conservation law, 10 Muskingum equation, 392 Muskingum-Cunge model, 394 

###### **N** 

Navier-Stokes equations, 11 Newton method, 58, 80, 135, 139, 306 Non-linear algebraic equations, 53, 305 Non-uniform flow, 8 Numerical diffusion, 236, 272, 395 Numerical dispersion, 225, 235 Numerical dissipation, 225, 235 Numerical stability, 102, 222 

**O** One dimensional continuity equation, 20 One dimensional dynamic equation, 12 Open channel, 1 Open channel network, 147, 297, 337 Ordinary differential equations, 27–28, 50, 85 

###### **P** 

Parabolic equations, 160, 162, 165, 172 Partial differential equations, 50, 159 Peclet number, 263, 272 Phase error, 225 Picard method, 82, 141 Preissmann scheme, 303 

**Q** QUICKEST scheme, 277 

###### **R** 

Rapidly varied flow, 9 Rating curve, 336, 370 Region of stability, 103 Reynolds equations, 11 Reynolds number, 264 Ridders method, 66 Riemann invariants, 169 Runge-Kutta methods, 93 

###### **S** 

Saint Venant equations, 23, 165, 301, 353, 356 Secant method, 61 Sediment transport, 343 Shape functions, 201 Shooting method, 108, 144 Simple fixed-point iteration, 62 Slope of energy grad line, 7, 9 Specific energy, 5 Spline function, 258 Splitting technique, 283 Stability analysis, 212, 222, 250, 320 Steady flow, 7 Steady flow in ice-covered channel, 131 Steady gradually varied flow, 9, 24 Steady gradually varied flow equation, 26, 111, 118, 147 Steep slope, 8 Steep wave, 351 Steffensen method, 67 Step method, 114 Storage equation, 30, 97, 391 Subcritical flow, 7 Sudden change of cross-section, 128 Supercritical flow, 7 Systems of non-linear equations, 79 Systems of linear algebraic equations, 69 

Index 

419 

###### **T** 

Thermal energy transport equation, 43 Thomas method, 79 Top width, 2 Total energy, 5 Total load of dissolved matter, 33 Triangular matrix, 70–71 Tri-diagonal matrix, 77 Truncation error, 88, 232 Turbulent diffusion, 12, 36, 37 

###### **U** 

Uniform flow, 8 Unsteady flow, 7, 21, 301, 367 

Unsteady gradually varied flow, 9, 21 Up-winding effect, 265, 358 Upwind scheme, 195, 222 

###### **V** 

Velocity head, 5 Volume flux, 5 

###### **W** 

Water stage, 1 Wave equation, 167, 174, 177 Wave number, 214 Wetted perimeter, 3 Wind-generated stresses, 19 

