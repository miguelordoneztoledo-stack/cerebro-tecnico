---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Rotura de Presas\01 Información\Parametros a Calcular.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

# **Prediction of Embankment Dam Breach Parameters** 

_A Literature Review and Needs Assessment_ 

# **DSO-98-004** 



##### **Water Resources Research Laboratory** 

**July 1998** 

# **Prediction of Embankment Dam Breach Parameters** 

_A Literature Review and Needs Assessment_ 

# **DSO-98-004** 

**Dam Safety Research Report** 

**_by Tony L. Wahl Water Resources Research Laboratory_** 

#### **U.S. Department of the Interior Bureau of Reclamation Dam Safety Office** 

**July 1998** 

## **ACKNOWLEDGMENTS** 

The Bureau of Reclamation Dam Safety Office and the Pacific Gas & Electric Company provided funding for this work. 

Wayne Graham, with Reclamation’s Sedimentation and River Hydraulics Group, and Rod Wittler, with the Water Resources Research Laboratory, made initial contributions to the literature survey and case study database.  They, as well as Bob Dewey, Jeff Farrar, Jim Melena, Dan Mares, Brent Mefford, and Phil Burgi, have provided many helpful comments in review of the document.  Robert Rood and Larissa Casey assisted with the editing and final preparation of the manuscript and made many significant improvements to the final product. 

Darrel Temple, of the Agricultural Research Service, Stillwater, Oklahoma, assisted with the organization and hosting of the February 1998 technical workshop on dam breach processes and also provided many helpful source documents for the literature review. 

i 

### CONTENTS 

|**EXECUTIVE SUMMARY**.........................................................................................................................1|
|---|
|**INTRODUCTION**.......................................................................................................................................2|
|**DAM-BREAK FLOOD FORECASTING**................................................................................................4|
|HISTORY........................................................................................................................................................4|
|GENERALPROCEDURES.................................................................................................................................5|
|IMPORTANCE OFBREACHPARAMETERS........................................................................................................6<br>|
|_Loss of Life Estimates.............................................................................................................................._7|
|**BREACH PARAMETER PREDICTION**................................................................................................7|
|BREACHPARAMETERDEFINITIONS...............................................................................................................7|
|EXISTINGMETHODS FORPREDICTINGBREACHPARAMETERS......................................................................9|
|**LITERATURE REVIEW**.........................................................................................................................10|
|CASESTUDIES.............................................................................................................................................10<br>|
|_Sources of Recent Dam Failure Data...................................................................................................._11|
|_Predicting Breach Parameters from Case Study Data ........................................................................_13|
|_Predicting Peak Outflows from Case Study Data ................................................................................_16|
|PHYSICALLY-BASEDDAMBREACHPREDICTIONMODELS...........................................................................17|
|MECHANICS OFEMBANKMENTEROSIONDURINGOVERTOPPINGFLOW....................................................19|
|HEADCUTEROSION.....................................................................................................................................22|
|_The NRCS SITES Model......................................................................................................................._22|
|_Physical Model Testing of Headcut Erosion........................................................................................._25|
|_Deterministic Headcut Advance Models..............................................................................................._26|
|_Ongoing ARS Research.........................................................................................................................._27|
|EROSIONMODELSBASED ONENERGYDISSIPATIONRATE.........................................................................27|
|_STARS and GSTARS ............................................................................................................................_27|
|EMBANKMENTARMORINGFAILURE............................................................................................................28|
|LATERALEROSIONMODELS........................................................................................................................31|
|**DAM FAILURES CASE STUDY DATABASE**.....................................................................................32|
|OBSERVEDBREACHPARAMETERS INCASESTUDIES..................................................................................33|
|_Breach Width ........................................................................................................................................._33|
|_Time of Failure......................................................................................................................................._34|
|COMPARINGPEAKFLOWRELATIONS TOCASESTUDIES.............................................................................37|
|**DEVELOPMENT OF A NEW DAM BREACH MODEL**....................................................................43|
|**BIBLIOGRAPHY**.....................................................................................................................................44|
|**NOTATION**...............................................................................................................................................52|
|**APPENDIX:  DAM FAILURES CASE STUDY DATABASE**............................................................55|



ii 

FIGURES 

|Figure 1. — Parameters of an idealized dam breach .............................................................. 7|
|---|
|Figure 2. — Progressive headcutting breach of a cohesive soil embankment...................... 20|
|Figure 3. — Schematic of the breaching process for a fuse plug embankment.................... 20|
|Figure 4. — Flow and erosion regimes in embankment overtopping ................................... 21|
|Figure 5. — Flow over an idealized headcut with and without aeration of the nappe ........ 23|
|Figure 6. — Schematic of a headcut in layered materials .................................................... 26|
|Figure 7. — Lateral erosion of fuse plug embankments ....................................................... 31|
|Figure 8. — Distribution of height and volume parameters for dam breach case<br>studies and embankment dams in DSIS database .................................................... 32|
|Figure 9. — Observed breach height and width.................................................................... 33|
|Figure 10. — Predicted vs. observed breach widths.............................................................. 34|
|Figure 11. — Predicted and observed volume of eroded material ........................................ 35|
|Figure 12. — Predicted and observed time of failure............................................................ 36|
|Figure 13. — Comparison of case study data and proposed relations for peak outflow<br>as a function of height parameters............................................................................. 37|
|Figure 14. — Comparison of case study data and proposed relations for peak outflow<br>as a function of storage parameters ........................................................................... 38|
|Figure 15. — Comparison of case study data and proposed relations for peak outflow<br>as a function of the product of height and storage parameters................................. 39|
|Figure 16. — Predicted and observed peak discharges using Froehlich (1995a) ................. 40|



### TABLES 

|Table 1. — Compilations of dam-failure case studies and guidance for predicting<br>breach parameters and peak breach outflow ............................................................. 11|
|---|
|Table 2. — Breach parameter relations based on dam-failure case studies......................... 13|
|Table 3. — Physically-based embankment dam breach models ........................................... 18|
|Table 4. — Additional dams analyzed using Froehlich’s 1995 peak flow prediction<br>equation....................................................................................................................... 41|
|Table A1. — Dam failures case study database .................................................................... 56|
|Table A2. — Dam failure database references and footnotes ............................................... 60|



iii 

iv 

# PREDICTION OF EMBANKMENT DAM BREACH PARAMETERS 

_A LITERATURE REVIEW AND NEEDS ASSESSMENT_ 

## **EXECUTIVE SUMMARY** 

This peer-reviewed report examines the role, importance, and methods for predicting embankment dam breach parameters needed for analysis of potential dam-failure floods. Special emphasis is given to dam breach analysis within the context of the risk assessment process used by the Bureau of Reclamation (Reclamation).  Current methods for predicting embankment dam breach parameters and numerically modeling dam breach events are reviewed, and the needs and opportunities for developing improved technologies are discussed.  Recent technical advances that could contribute to improvements in dam breach simulation are identified.  In addition to this literature review, Reclamation and the Agricultural Research Service (ARS) cosponsored an international workshop on dam breach processes February 10-11, 1998, attended by about 35 leading professionals working in this field.  The workshop provided an opportunity to review and discuss the state-of-theart, ongoing research, and future needs for dam breach analysis tools.  Key findings from this literature review and the workshop include: 

- There is presently both a need and opportunity to achieve significant improvements in technology used to analyze embankment dam breach processes.  The potential benefits to be achieved from this effort may significantly aid risk assessment studies, in which thresholds of dam failure, probabilities of failure, and consequences of failure are all of prime importance. 

- When population centers are located close to dams, accurate prediction of breach parameters is crucial to development of effective emergency action plans, design of early warning systems, and characterization of threats to lives and property. 

- Warning time is the most important parameter affecting potential loss of life due to dam failure. 

- The primary benefits of improved prediction of breach initiation and formation times will accrue to the population within a few kilometers of the structure, but this is also the region which historically has the greatest risk for loss of life. 

- The distinction between breach _initiation time_ and breach _formation time_ has not been clearly made in the literature or the available case study data; this impacts the ability to accurately predict warning time. 

- Although breach initiation time is critical to the determination of loss of life, there is little guidance in the literature for its prediction.  Numerical dam breach models have the potential to predict breach initiation times, but are not widely used and are not based on observed breach erosion mechanisms. 

- Breach parameter prediction equations based on analyses of dam failure case studies have significant uncertainty, breach formation time is especially difficult to predict. 

1 

- The case study database used to develop most existing breach parameter prediction equations contains a disproportionately small number of examples of high dams and/or large reservoirs compared to the population of embankment dams to which the equations are being applied. 

- The primary mechanism of embankment dam failure is headcut erosion that initiates at the toe of the downstream slope and advances headward until it breaches the crest of the dam.  This mechanism is not modeled in any of the available dam breach simulation models. 

- The Agricultural Research Service (ARS) and Natural Resources Conservation Service (NRCS) have developed effective procedures for numerically modeling headcut erosion in natural earth spillways.  This technology shows great promise for adaptation to embankment dam breach problems. 

- Erosion models based on relations between hydraulic energy dissipation rate and erodibility indices based on excavability show promise for simulation of high energy erosion processes in widely variable materials. 

- Past research on breaching of fuse plug spillway embankments may be relevant to latter stages of embankment dam breach events. 

- The principal of minimum energy dissipation rate, as applied in the GSTARS and GSTARS-2 models, may be useful for simulating simultaneous width and depth adjustments of the breach opening during an embankment dam failure. 

- Recent research by Reclamation, ARS, and others has improved the technology for modeling the stability of riprap and vegetated surfaces.  Combining this technology with recent improvements in headcut erosion modeling may yield better tools for determining if a dam will breach. 

- Much valuable information is available from embankment failures that continue to occur each year, but it is often lost because local authorities have other pressing needs during a crisis and are not aware of the type of data that would be of most use to dam breach researchers.  The formation of a standing forensic team that could promptly investigate incidents of dam failure and dam survival of extreme events (e.g., overtopped but not failed) would be extremely valuable. 

## **INTRODUCTION** 

Dams provide many benefits for our society, but floods resulting from the failure of constructed dams have also produced some of the most devastating disasters of the last two centuries.  When dams fail, property damage is certain, but loss of life can vary dramatically with the extent of the inundation area, the size of the population at risk, and the amount of warning time available.  Costa (1985) reports that sixty percent of the more than 11,100 fatalities associated with all dam failures worldwide have occurred in just three failures: Vaiont, Italy, 1963 (2,600 dead; overtopping of concrete arch dam by landslide-generated wave); Johnstown Dam, Pennsylvania, 1889 (2,200 dead; overtopping of embankment dam); and Machhu II, India, 1974 (2,000+ dead; overtopping of embankment dam during construction).  In each of these cases, large populations were given little or no warning.  In fact, Costa reports that the average number of fatalities per 

2 

dam failure is 19 times greater when there is inadequate or no warning.  Major causes of failures identified by Costa are overtopping due to inadequate spillway capacity (34 percent), foundation defects (30 percent), and piping and seepage (28 percent). 

Simulation of embankment dam breach events and the resulting floods are crucial to characterizing and reducing threats due to potential dam failures.  For the Bureau of Reclamation (Reclamation), the increasing use of the risk assessment process as a planning and decision-making tool has highlighted the need for improved embankment breach analysis tools.  Risk assessment analyses of Reclamation dams consider all possible loadings and failure scenarios for a dam, the probability of those loadings and sequences of events needed to cause failure (i.e., event trees), and the consequences of failure.  Key questions related to embankment breach that must be anwered in the course of a risk assessment are: 

- Will dam failure occur?  What are the loading thresholds that cause failure, and what is the probability of failure given a particular loading? 

- What are the consequences of failure in terms of loss of life and property damages? 

To answer the second question, detailed information about the failure is needed, such as the amount of warning time, and inundation levels and velocities at downstream locations. The development of effective emergency action plans and design of early warning systems that might reduce or eliminate consequences of failure also require such information. 

Analyzing the failure of an embankment dam can be viewed as a two-step process.  First, the actual breach of the dam must be analyzed, and second, the outflow from the breach must be routed through the downstream valley to determine the resulting flood at population centers.  If the population at risk is located well downstream from a dam, details of the breaching process have little effect on the result; travel time, attenuation, and other routing effects predominate.  The National Weather Service (NWS) DAMBRK model and its successor FLDWAV are appropriate tools for such an analysis.  However, in a growing number of cases, the location of population centers near a dam makes accurate prediction of breach parameters (e.g., breach width, depth, initiation time, and rate of development) crucial to the analysis.  If breach parameters cannot be predicted with reasonable accuracy, increased conservatism with associated increased costs may be required. 

Unfortunately, breach simulation and breach parameter prediction contain the greatest uncertainty of all aspects of dam-break flood forecasting (Wurbs, 1987).  Most approaches rely either on case study data from past dam failures or numerical models that do not simulate the erosion mechanisms and flow regimes that are relevant to a dam breach. Case study data provide only limited information (i.e., ultimate depth, width, and shape; peak discharge; maximum overtopping depth; total time to fully fail embankment or drain reservoir), based on a relatively small database of dam failures, primarily of small dams. Case study data are especially weak for making predictions of the time needed to initiate a breach, the rate of breach formation, and the total time required for failure.  This is due to the difficulty of defining the exact point of failure and the variations in interpretation of failure by the lay person who often is the only eyewitness to a dam failure. 

3 

Physically-based numerical models (e.g., NWS-BREACH) offer the potential to provide more detailed information but at this time are recognized as having limited accuracy. Currently available models rely on sediment transport relations that are not applicable or are untested in the regime of flow conditions applicable to a dam breach.  Furthermore, many of the available models simply do not simulate the failure mechanics observed in case studies and laboratory tests. 

As a result, Reclamation has initiated a cooperative research effort with the objective of developing a new, physically-based, state-of-the-art numerical model for simulating the process of embankment dam breach.  The new model should be applicable to embankment dams breached by overtopping or piping.  This model will promote improved analysis of dam-break floods that will lead to better characterization of dam safety risks and more cost-effective solution of dam safety problems.  Early cooperators in this effort include the Department of Interior/Reclamation Dam Safety Program, the National Weather Service, and the Pacific Gas & Electric Company (PG&E).  The Agricultural Research Service is also pursuing similar objectives and has already been a technical partner in this effort. 

The first step in this research effort was to conduct a survey of the existing literature to identify current breach prediction methods, case histories, and related technologies, and to focus the future research efforts for maximum benefit.  This report presents the results of the literature survey.  The report begins by examining dam-break flood forecasting in general and the importance of dam breach parameter prediction.  The report then reviews previously documented dam failure case studies, new case studies, and the breach parameter prediction methods based on those data.  Important mechanisms in breach formation and development are identified from the documented case studies and previous laboratory testing, and existing physically-based dam breach models are reviewed in this context.  Finally, a framework is outlined for a new dam breach model, components of the model are identified, and research needs are summarized. 

## **DAM-BREAK FLOOD FORECASTING** 

#### **History** 

The 1964 failure of Baldwin Hills Dam, near Los Angeles, California, and the near failure of Lower Van Norman (San Fernando) Dam in 1971 prompted the State of California to enact statutes requiring dam owners to prepare dam failure inundation maps.  The need for developing procedures for estimating the breach hydrograph was thus born.  Prior to the enactment of the California statutes, very little was published regarding procedures for estimating dam breach outflow hydrographs. 

The numerous dam failures that occurred in the mid-1970's, including Buffalo Creek coal waste dam (West Virginia, 1972), Teton Dam (Idaho, 1976), Laurel Run Dam and Sandy Run Dam (Pennsylvania, 1977), and Kelly Barnes Dam (Georgia, 1977), led to comprehensive reviews of Reclamation's dam safety program.  Many of the reviews recommended that emergency preparedness planning with inundation maps be emphasized.  The Federal Guidelines for Dam Safety, dated June 25, 1979, stated that 

4 

inundation maps should be prepared.  These events highlighted the need for developing procedures for estimating dam breach outflow hydrographs. 

#### **General Procedures** 

There are numerous tools available today for analyzing dam failures and their resulting outflow hydrographs.  Some of the best-known and most widely used are the National Weather Service (NWS) Dam-Break Flood Forecasting Model (DAMBRK); the U.S. Army Corps of Engineers Hydrologic Engineering Center Flood Hydrograph Package, HEC-1 (Hydrologic Engineering Center, 1981); and the NWS Simplified Dam-Break Flood Forecasting Model, SMPDBK (Wetmore and Fread, 1983).  Of these models, DAMBRK is the most widely used.  The National Weather Service has recently released FLDWAV (Fread, 1993), the successor to DAMBRK.  Wurbs (1987) discussed and compared the stateof-the-art models available at that time and recommended the use of DAMBRK or SMPDBK, depending on the level of accuracy required and resources and input data available.  Westphal and Thompson (1987) also compared DAMBRK and SMPDBK and recommended the use of SMPDBK as a screening tool and DAMBRK for more detailed analyses.  All these models treat the routing of the dam-break flood in much greater detail than the actual breaching process.  The National Weather Service BREACH model (Fread, 1988) and other similar models simulate the breach formation process in greater detail. 

The two primary tasks in the analysis of a dam breach are the prediction of the reservoir outflow hydrograph and the routing of that hydrograph through the downstream valley. Predicting the outflow hydrograph can be further subdivided into predicting the breach characteristics (e.g., shape, depth, width, rate of breach formation) and routing the reservoir storage and inflow through the breach.  The routing tasks—through the breach and through the downstream valley—are handled in most of the widely used computer models with various one-dimensional routing methods.  However, the programs differ widely in their treatment of the breach simulation process.  Many models do not directly simulate the breach; rather, the user determines the breach characteristics independently and provides that information as input to the routing model. 

Reclamation (1988) grouped the analysis methods into four categories: 

1. **Physically based methods** - Predict the development of a breach and the resulting breach outflows using an erosion model based on principles of hydraulics, sediment transport, and soil mechanics (e.g., NWS-BREACH). 

2. **Parametric models** - Use case study information to estimate time to failure and ultimate breach geometry, then simulate breach growth as a time-dependent linear process and compute breach outflows using principles of hydraulics. 

3. **Predictor equations** - Estimate peak discharge from an empirical equation based on case study data and assume a reasonable outflow hydrograph shape. 

4. **Comparative analysis** - If the dam under consideration is very similar in size and construction to a dam that failed, and the failure is well documented, appropriate breach parameters or peak outflows may be determined by comparison. 

5 

The last three approaches are the most straightforward, but they all rely heavily on case study data, and selection of appropriate equations requires data for case studies similar to the dam under consideration.  In general, the database of well-documented dam failure case studies is small, and contains few examples of very high dams or very large storage volumes.  Identifying similar case studies for use in a comparative analysis or for developing more focused predictor equations may be impossible for large dams or those of unique construction.  Also, the assumption of linear growth rate of breach dimensions is probably not realistic in most cases. 

#### **Importance of Breach Parameters** 

Singh and Snorrason (1984) used the DAMBRK and HEC-1 models to study the effects of breach parameter variations on the predicted peak outflow for eight hypothetical breached dams.  They varied the breach width, depth, failure time, and overtopping head within ranges identified from their analysis of 20 actual dam-failure case studies.  Large changes in peak flow were produced by varying the failure time on reservoirs with relatively small storage.  A 50 percent reduction in failure time during the PMF hydrograph produced increases in peak discharge of 13-83 percent.  For large reservoirs, the peak outflow was insensitive to the same change in failure time, showing a variation of only 1-5 percent. 

Conversely, changes in breach width produced larger changes (35-87%) in peak outflow for large reservoirs and smaller changes (6-50%) in peak outflow for small reservoirs. Sensitivity to breach depth was relatively small in the 20 case studies considered by Singh and Snorrason; there was only about a 20 percent change in peak outflow over the range of simulated breach depths, and the change in peak flow showed no apparent relationship to reservoir size. 

Petrascheck and Sydler (1984) also demonstrated the sensitivity of discharge, inundation levels, and flood arrival time to changes in the breach width and breach formation time. For locations near the dam, both parameters can have a dramatic influence.  For locations well downstream from the dam, the timing of the flood wave peak can be altered significantly by changes in breach formation time, but the peak discharge and inundation levels are insensitive to changes in breach parameters. 

Clearly, accurate prediction of breach parameters is necessary to make reliable estimates of peak outflow and resulting downstream inundation in close proximity to the dam. Wurbs (1987) concluded that breach simulation contains the greatest uncertainty of all aspects of dam-breach flood wave modeling.  The importance of different parameters varies with reservoir size.  In large reservoirs, the peak discharge occurs when the breach reaches its maximum depth and width.  Changes in reservoir head are relatively slight during the breach formation period.  In these cases, accurate prediction of breach geometry is most critical.  For small reservoirs, there is significant change in reservoir level during the formation of the breach, and as a result, the peak outflow occurs before the breach has fully developed.  For these cases, the breach formation rate is the crucial parameter. 

6 

###### **_Loss of Life Estimates_** 

Warning and evacuation time can dramatically influence the loss of life from dam failure. When establishing hazard classifications, preparing emergency action plans, or designing early warning systems, good estimates of warning time are crucial.  Warning time is the sum of the breach initiation time (defined below), breach formation time, and flood wave travel time from the dam to a population center.  Case history-based procedures developed by the Bureau of Reclamation indicate that the loss of life can vary from 0.02 percent of the population-at-risk when the warning time is 90 minutes to 50 percent of the population-atrisk when the warning time is less than 15 minutes (Brown and Graham, 1988).  More recent work by DeKay and McClelland (1991) shows similar extreme sensitivity to warning time.  Costa (1985) reported that the average number of fatalities per dam failure is 19 times greater when there is inadequate or no warning. 

## **BREACH PARAMETER PREDICTION** 

#### **Breach Parameter Definitions** 

For the purposes of this discussion, the term breach parameters will include the parameters needed to physically describe the breach (breach depth, breach width, and side slope angles) as well as parameters that define the time required for breach initiation and development.  The physical parameters are shown graphically in Figure 1 and are briefly summarized below. 

- **Breach depth** - Also referred to as breach height in many publications.  This is the vertical extent of the breach, measured from the dam crest down to the invert of the breach.  Some publications cite the reservoir head on the breach, measured from the reservoir water surface to the breach invert. 

- **Breach width** - The ultimate breach width and the rate of breach width expansion can dramatically affect the peak flowrate and resulting inundation levels downstream from the dam.  Case studies typically report either the average breach width or the breach width at the top and bottom of the breach opening. 

- **Breach side slope factor** - The breach side slope factor along with the breach width and depth fully specifies the shape of the breach opening. Accurately predicting the breach side slope angles is generally of secondary importance to predicting the breach width and depth. 



Figure 1. — Parameters of an idealized dam breach. 

7 

The time-related parameters of interest are the breach initiation time and breach formation time (sometimes referred to as breach development time).  Identifying two distinct parameters recognizes that embankment dam failures are not normally instantaneous and that there are two phases in which the mechanics and rate of erosion can be dramatically different.  In the breach initiation phase, the dam has not yet failed, and outflow from the dam is slight; outflow may consist of a slight overtopping of the dam or a small flow through a developing pipe or seepage channel.  During the breach initiation phase, it may be possible for the dam to survive if the overtopping or seepage flow is stopped.  During the breach formation phase, outflow and erosion are rapidly increasing, and it is unlikely that the outflow and the failure can be stopped. 

It is important to recognize and account for the two phases because the breach initiation time directly affects the amount of advance warning time available for evacuating downstream populations.  Prior research (case studies, empirical prediction equations, numerical models, etc.) has been focused primarily on the breach formation time, although several investigators have acknowledged the existence of a breach initiation phase through their definitions of the breach formation time.  Despite this, breach initiation times have generally not been reported as a distinct parameter for the majority of dam failure case studies.  Furthermore, breach initiation time is not an input to DAMBRK or FLDWAV, nor should it be, since it does not affect the actual routing of the flood.  There is little guidance presently available for the selection of breach initiation times.  Physically-based breach simulation models (e.g., BREACH) simulate the breach initiation phase as a tractive-force erosion problem, which is not consistent with the erosion mechanics observed in laboratory testing and documented case studies. 

When breach formation times are reported in case studies, there is often some question as to whether the reported times are only for the breach formation phase, or if they might also include some portion of the breach initiation phase.  Distinguishing between the two during (or after) a failure is a difficult task, even for a trained observer.  In the interest of promoting more accurate reporting of breach initiation and breach formation times, the following definitions are offered: 

- **Breach initiation time** - The breach initiation time begins with the first flow over or through a dam that will initiate warning, evacuation, or heightened awareness of the potential for dam failure.  The breach initiation time ends at the start of the breach formation phase (see next item). 

- **Breach formation time** - The breach formation time has been defined in various ways by different investigators; however, all definitions are similar to that used by DAMBRK: 

_The time of failure as used in DAMBRK is the duration of time between the first breaching of the upstream face of the dam until the breach is fully formed.  For overtopping failures the beginning of breach formation is after the downstream face of the dam has eroded away and the resulting crevasse has progressed back across the width of the dam crest to reach the upstream face._ 

8 

#### **Existing Methods for Predicting Breach Parameters** 

The analysis of the consequences of a potential dam-break has generally been subdivided into three distinct problems: 

1. Prediction of the outflow hydrograph 

2. Routing of the hydrograph through the downstream valley, using a model such as DAMBRK 

3. Prediction of damages and loss of life due to the flood. 

The prediction of the outflow hydrograph is our primary interest here; this task has been further subdivided into simulating the dam breach formation process and computing the outflow through the breach from principles of hydraulics. 

Simplified approaches that entirely neglect the breaching process use case study data to develop direct predictions of peak outflow and time required for failure.  These predictions may be based on comparisons with one or more very similar dams that have failed (comparative analysis), or they may be based on regression relations that predict peak outflow and time of failure from relevant hydraulic parameters, such as dam height, reservoir storage, and embankment volume (predictor equations).  The peak outflow hydrograph predicted using these methods serves as the input to the river routing analysis. 

A more rigorous approach is to simulate the breach of the dam and the resulting reservoir outflow internally in DAMBRK using a parametric approach.  Final breach geometry and time of breach formation are specified, and the breach enlargement is then simulated as a simplified time-dependent process (e.g., linear increase of breach dimensions).  This approach is commonly used today.  The new FLDWAV model that will replace DAMBRK in future years uses the same parametric approach (improvements are primarily in the river routing portion of the analysis). 

There are numerous methods for predicting the breach parameters that serve as input to an analysis using DAMBRK or similar models.  Three basic approaches can be identified. Comparative analysis of similar case studies, and the use of predictor equations based on numerous case studies are the two simplest approaches.  The third approach is the use of a physically based dam breach simulation model that uses principles of hydraulics and sediment transport to simulate the development of the breach.  This approach is more difficult, but also offers the potential for more detailed results, such as prediction of breach initiation time and prediction of intermediate breach dimensions as well as ultimate breach parameters.  The National Weather Service BREACH model (Fread, 1988) is the most widely used physical model. 

All three approaches have shortcomings.  Comparative analysis suffers from a lack of accurate and comprehensive case study data on a wide variety of dams, especially very large dams.  Predictor equations suffer from similar problems, and regression relations based on the available data have high uncertainty.  Physically based models suffer from a poor understanding of the mechanisms of breach development and an inability to model those mechanisms and the high energy erosion processes that dominate dam breach. 

9 

Numerous predictor equations for peak discharge and breach parameters have been developed and are summarized in this report.  The available equations vary widely depending on the analyst and the types of dam failures studied.  In general, predictions of breach side slopes have high uncertainty, although this is of secondary importance, since breach outflows are relatively insensitive to side slopes.  Predictions of breach formation time also have very high uncertainty due to a lack of reliable case study data; many dams fail without eyewitnesses, and the problem of distinguishing between breach initiation and breach formation phases has likely tainted much of the data. 

## **LITERATURE REVIEW** 

#### **Case Studies** 

Sources of individual case study data for breached dams are numerous.  However, many of the historic dam failures took place before the need was recognized to fully document the breach process and breach characteristics.  Babb and Mermel (1968) summarized over 600 dam incidents throughout the world, but high quality, detailed information was lacking in most cases.  During the 1980s, several authors compiled databases of well-documented case studies in efforts to develop predictive relations for breach parameters or peak breach outflows (SCS, 1981; Singh and Snorrason, 1982; MacDonald and Langridge-Monopolis, 1984; Costa, 1985; Froehlich, 1987, 1995a, 1995b; and Singh and Scarlatos, 1988).  Other researchers have used these compilations to develop further guidance on breach parameters and outflows (FERC, 1987; Reclamation, 1988; and Von Thun and Gillette, 1990).  Table 1 summarizes the case study compilations and the types of relations proposed by the various authors.  (Note:  In the tables that follow in this report, all dimensional relations are given in metric units.)  In more recent years, individual case studies have been published in newsletters and conference proceedings of major dam safety organizations, most notably the Association of State Dam Safety Officials (ASDSO) in the United States. 

The literature search undertaken for this study produced a single database containing all case studies cited in the references mentioned above, as well as several case studies documented separately in more recent publications, a total of 108 embankment dam failures.  This database is provided in table A1 of the appendix.  References to individual case studies are included in the _Bibliography_ only when they refer to case studies not already documented in the compilations listed above.  For specific information on any individual dam failure contained in the compilations, the reader should refer to the references cited in the papers listed above. 

A more complete discussion of the past case study compilations follows later in this report, but a quick review shows that different investigators have proposed numerous relations for estimating breach parameters or peak discharges.  Most proposed relations have been based on databases of about 20-50 dams, most of which were relatively small.  Dam failure data are rare for dams higher than about 20 meters (75 ft).  Substantial data do exist for the failure of dams between 6 and 15 meters high (20-50 ft).  Graham (1983) has summarized the breach data for six dams with large storage to dam height ratios, but the 

10 

Table 1. — Compilations of dam-failure case studies and guidance for predicting breach parameters and <u>peak breach outflow.  For explanations of symbols see the</u> _Notation_ <u>section at the end of this report.</u> 

|**Reference**|**Case Studies**|**Relations Proposed**|**Notes**|
|---|---|---|---|
|Babb and Mermel (1968)|>600 incidents||Many cases not well-<br>documented|
|Kirkpatrick (1977)|16 (plus 5<br>hypothetical<br>failures)|_Qp = f(hw) _||
|SCS(1981)|13|_Qp =f(hw)_||
|Hagen(1982)|6|_Qp =f(hw*S)_||
|Reclamation(1982)|21|_Qp =f(hw)_||
|Graham (1983)|6||dams with large<br>storage-to-height<br>ratios|
|Singh and Snorrason (1982,<br>1984)|20 real failures<br>and 8 simulated<br>failures|Guidance for _B_,_dovtop_,and _tf_<br>_Qp = f(S); Qp = f(hd) _|Qprelations based on<br>simulations|
|Graham(undated)|19|_Qp =f(hw,S)_||
|MacDonald and Langridge-<br>Monopolis (1984)|42|_Ver = f(Vout*hw) _<br>_tf = f(Ver) _<br>_Qp =f(Vout*hw)_||
|Costa (1985)|31 constructed<br>dams|_Qp = f(hd) _<br>_Qp = f(S)_<br>_Qp =f(hd*S)_|Includes information<br>on natural dam<br>failures|
|Evans(1986)||_Qp =f(Vw)_||
|FERC(1987)||Guidancefor_B, Z, tf_||
|Froehlich(1987)|43|_B, Z, tf _relations||
|Reclamation(1988)||_B, tf  _guidance||
|Singh and Scarlatos(1988)|52|Guidancefor_B, Z, tf_||
|Von Thun and Gillette (1990)|57|_Z_ guidance<br>_B = f(hw, S)_<br>_tf =f(hw,_ erosion resistance_)_||
|Froehlich(1995b)|63|_B, Z, tf _relations||
|Froehlich(1995a)|22|_Qp =f(Vw, hw)_||



quality of the data in four of these cases was rated as suspect.  One can generally conclude that a limited sample of dam failures serves as the basis for all these relations, especially with respect to large dams.  It is likely that the proposed relations have been shaped to a large degree by the character of the dam failure database.  Different procedures, especially for larger dams, may have been proposed if information was available for a different set of failed dams. 

###### **_Sources of Recent Dam Failure Data_** 

The most recent publications reporting large amounts of case study data were published in 1988.  Since that time, there have been several major flood events in the U.S. that have caused large numbers of dam failures.  Some of the most notable events are the flooding in the upper Mississippi and lower Missouri Basins in 1993, dam failures in Georgia caused by Tropical Storm Alberto in 1994, and dam failures in North Carolina during September 

11 

1996.  Inquiries were made regarding these flood events and related dam failures.  ASDSO newsletters through February 1995 were also reviewed to identify additional case studies. 

Flooding in the upper Mississippi and lower Missouri River Basins in 1993 was of epic proportions, both in intensity and duration (Wahl, Vining, and Wiche, 1993).  The most notable failures caused by this flooding were of levees, although numerous small dams also failed (ASDSO Newsletters).  In many cases, peak flows occurred well after dam failure events as precipitation and flood waters continued to rise over a three-month period. Parrett, Melcher, and James (1993) summarized peak flood discharges at stations throughout the upper Mississippi River Basin and cited no notable cases in which peak flows were caused by dam or levee failures.  Also, the magnitude of the flooding damage in many areas probably prevented much detailed or immediate investigation of the numerous small-dam and levee failures. 

Flooding caused by Tropical Storm Alberto in 1994 led to the failure of over 200 dams in Georgia, but most were small structures (1-8 hectares [2-20 acres] surface area) and many failed with high tailwaters and minimal head differential across the dams.  The enormity of the damage in the area and the difficulty of gaining access to the sites prevented detailed investigation of most of these failures by local officials.  Several federal agencies and dam safety organizations (e.g., USBR, TVA, ICODS) explored the possibility of conducting more detailed field studies but were not able to mobilize quickly enough to make the effort worthwhile.  In September 1995 the author visited several of the breached dams in the vicinity of Americus, Georgia, but by that time high water marks were no longer visible and many dams were being or had been reconstructed.  Froehlich (written communication) investigated eight dam failures in Georgia and reported breach dimensions, reservoir, and hydraulic data.  He evaluated these failures using the relations proposed in his 1995 paper and obtained good agreement with the predicted average breach width. 

Hurricane Fran caused widespread flooding and dam failures in North Carolina during September 1996.  The author visited numerous dams in this area during December 1996. Although quantitative information was not gathered, the failures were notable for the consistency of the erosion mechanisms that were evident.  Nearly all failures appeared to begin with headcuts at the toe of the downstream slope that advanced upstream until they caused the complete failure of the dam.  Several dams had experienced partial damage, with headcuts that had not advanced completely back to the reservoir.  These sites were especially interesting because they revealed the intermediate conditions that could only be assumed for the fully failed dams. 

ASDSO newsletters and conference proceedings contained information on numerous dam failures.  However, most of the dam failures were small and not extensively documented. Only the failure of Kendall Lake Dam, documented in the 1993 ASDSO conference proceedings (Ballentine, 1993), provided enough information to be of additional value in the case study database.  The National Performance of Dams Program (NPDP) is a new program for reporting dam incidents, including dam failures, and is being administered by Stanford University in cooperation with ASDSO (McCann, 1995).  The NPDP program is actively seeking dam failure case study data as well as data on all types of dam incidents through an Internet site located at http://npdp.stanford.edu/.  The data available is 

12 

generally only qualititative or visual in nature.  The digital image database is especially interesting. 

###### **_Predicting Breach Parameters from Case Study Data_** 

Table 2 summarizes the relations proposed by previous investigators for predicting breach parameters (e.g., geometry, time of formation) from case study data.  The earliest contributions were made by Johnson and Illes (1976), who published a classification of failure shapes for earth, gravity, and arch dams.  For earth dams, the breach shape was described as varying from triangular to trapezoidal as the breach progressed.  The great majority of earth dam breaches are described as trapezoidal in the literature. 

Table 2. — Breach parameter relations based on dam-failure case studies. For explanations <u>of symbols see the</u> _Notation_ <u>section at the end of this report.</u> 

|**Reference**|**Number of**<br>**Case Studies**|**Relations Proposed**<br>**(S.I. units, meters, m**<sup>**3**</sup>**/s, hours)**|
|---|---|---|
|Johnson and Illes(1976)||0.5_hd _≤ _B_ ≤3_hd_for earthfill dams|
|Singh and Snorrason (1982,<br>1984)|20|2_hd_ ≤ _B_ ≤5_hd_<br>0.15m≤ _dovtop_ ≤ 0.61m<br>0.25hr≤ _tf_ ≤1.0hr|
|MacDonald<br>and Langridge-Monopolis<br>(1984)|42|Earthfill dams:<br>_Ver _= 0.0261(_Vout*hw_)<sup>0.769</sup><br>[best-fit]<br>_tf_= 0.0179(_Ver_)<sup>0.364</sup><br>[upper envelope]<br>Non-earthfill dams:<br>_Ver_=0.00348(_Vout*hw_)<sup>0.852</sup><br>[bestfit]|
|FERC (1987)||_B_is normally 2-4 times_hd_<br>_B_can range from 1-5 times_hd_<br>_Z _= 0.25 to 1.0<br>[engineered, compacted dams]<br>_Z _= 1 to 2<br>[non-engineered, slag or refuse dams]<br>_tf_= 0.1-1 hours [engineered, compacted earth dam]<br>_tf_= 0.1-0.5 hours<br>[non-engineered, poorly<br>compacted]|
|Froehlich (1987)|43|( )<br>_B_<br>_K_<br>_S_<br>_o_<br>*<br>*<br>.<br>.<br>=0 47<br>0 25<br>_Ko_= 1.4 overtopping; 1.0 otherwise<br>_Z_<br>_K h_<br>_W_<br>_c_<br>_w_<br>=0 75<br>1 57<br>0 73<br>.<br>(<br>)<br>(<br>)<br>*<br>.<br>*<br>.<br>_Kc_ = 0.6 with corewall; 1.0 without a corewall<br>_tf* =_79(_S*_)0.47|
|Reclamation (1988)||_B_= (3)_hw _<br>_tf_=(0.011)_B_|
|Singh and Scarlatos (1988)|52|Breach geometry and time of failure tendencies<br>_Btop/Bbottom_ averages1.29|
|Von Thun and Gillette(1990)|57|_B, Z, tf_ guidance (see discussion)|
|Deweyand Gillette(1993)|57|Breach initiation model; _B, Z, tf_ guidance|
|Froehlich (1995b)|63|_B_<br>_K V_<br>_h_<br>_o_<br>_w_<br>_b_<br>=01803<br>0 32<br>0 19<br>.<br>.<br>.<br>_tf =_0.00254_Vw_0.53_hb_(-0.90)<br>_Ko_=1.4forovertopping; 1.0 otherwise|



13 

Singh and Snorrason (1982) provided the first quantitative guidance on breach width. They plotted breach width versus dam height for 20 dam failures and found that breach width was generally between 2 and 5 times the dam height.  The failure time, from inception to completion of breach, was generally 15 minutes to 1 hour.  They also found that for overtopping failures, the maximum overtopping depth prior to failure ranged from 0.15 to 0.61 meters (0.5 to 2.0 ft). 

MacDonald and Langridge-Monopolis (1984) proposed a breach formation factor, defined as the product of the volume of breach outflow (including initial storage and concurrent inflow) and the depth of water above the breach invert at the time of failure.  They related the volume of embankment material removed to this factor for both earthfill and nonearthfill dams (e.g., rockfill, or earthfill with erosion-resistant core).  Further, they concluded from analysis of the 42 case studies cited in their paper that the breach side slopes could be assumed to be 1h:2v in most cases; the breach shape was triangular or trapezoidal, depending on whether the breach reached the base of the dam.  An envelope curve for the breach formation time as a function of the volume of eroded material was also presented for earthfill dams; for non-earthfill dams the time to failure was unpredictable, perhaps because, in some cases, failure may have been caused by structural instabilities rather than progressive erosion.  The authors described iterative procedures for estimating breach parameters, simulating breach outflows using DAMBRK or other models, and revising breach parameter estimates as necessary. 

Froehlich (1987) developed nondimensional prediction equations for estimating average breach width, average side-slope factor, and breach formation time.  The predictions were based on characteristics of the dam, including reservoir volume, height of water above the breach bottom, height of breach, width of the embankment at the dam crest and breach bottom, and coefficients that account for overtopping vs. non-overtopping failures and the presence or absence of a corewall.  Froehlich also concluded that, all other factors being equal, breaches caused by overtopping are wider and erode laterally at a faster rate than breaches caused by other means. 

Froehlich revisited his 1987 analysis in a 1995 paper, using data from a total of 63 case studies.  Eighteen of these failures had not been previously documented in the literature reviewed for this report.  Froehlich developed new prediction equations for average breach width and time of failure.  In contrast to his 1987 relations, the new equations are not dimensionless.  Both 1995 relations had better coefficients of determination than did the 1987 relations, although the difference for the time of failure relation was very slight. Froehlich did not suggest a prediction equation for the average breach side slopes in his 1995 paper, but simply suggested assuming breach side slope factors of _Z_ = 1.4 for overtopping failures or _Z_ = 0.9 for other failure modes.  He noted that the average side slope factor for the 63 case studies was nearly 1.0.  The data set showed that there are some significant outliers in this regard. 

Reclamation (1988) provided guidance for selecting ultimate breach width and time of failure to be used in hazard classification studies using the SMPDBK model.  The suggested values are not intended to yield accurate predictions of peak breach outflows, but rather are intended to produce conservative, upper bound values that will introduce a factor of safety into the hazard classification procedure.  For earthen dams, the recommended breach width is 3 times the breach depth, measured from the initial 

14 

reservoir water level to the breach bottom elevation (usually assumed to be the streambed elevation at the toe of the dam).  The recommended time for the breach to develop (hours) is 0.011 times the breach width (meters). 

Singh and Scarlatos (1988) documented breach geometry characteristics and time of failure tendencies from a survey of 52 case studies.  They found that the ratio of top and bottom breach widths, _Btop/Bbottom,_ ranged from 1.06 to 1.74, with an average value of 1.29 and standard deviation of 0.180.  The ratio of the top breach width to dam height was widely scattered.  The breach side slopes were inclined 10-50° from vertical in most cases.  Also, most failure times were less than 3 hours, and 50 percent of the failure times were less than 1.5 hours. 

Von Thun and Gillette (1990) and Dewey and Gillette (1993) used the data from Froehlich (1987) and MacDonald and Langridge-Monopolis (1984) to develop guidance for estimating breach side slopes, breach width at mid-height, and time to failure.  They proposed that breach side slopes be assumed to be 1:1 except for dams with cohesive shells or very wide cohesive cores, where slopes of 1:2 or 1:3 (h:v) may be more appropriate. 

Von Thun and Gillette proposed the following relationship for average breach width: 



with _hw_ being the depth of water at the dam at the time of failure, and _Cb_ a function of reservoir storage as follows: 

|Reservoir Size,m<sup>3</sup><br>|_Cb_,meters|Reservoir Size,acre-feet|_Cb_,feet|
|---|---|---|---|
|< 1.23*10<sup>~~6~~</sup><br>1.23*10<sup>6</sup>- 6.17*10<sup>6</sup><br>|6.1<br>18.3|< 1,000<br>1,000-5,000|20<br>60|
|6.17*10<sup>6</sup>- 1.23*10<sup>7</sup><br>|42.7|5,000-10,000|140|
|> 1.23*10<sup>7</sup>|54.9|>10,000|180|



They noted that this relationship more accurately fits the full range of historical case study data than do the eroded embankment volume relations based on the breach formation factor proposed by MacDonald and Langridge-Monopolis.  The volume of eroded embankment is useful, however, as a check on the reasonableness of breach geometries predicted by other means.  Von Thun and Gillette presented a plot of eroded embankment volume versus water outflow volume and the depth of water above the breach invert, with contours indicating upper bounds of reasonable breach geometry estimates.  They also noted that the small database of large-dam failures tends to indicate 150 meters (500 ft) as a possible upper bound for breach width. 

Von Thun and Gillette proposed two methods for estimating breach formation time.  Plots of breach formation time versus depth of water above the breach invert suggested upper and lower bound prediction equations for erosion resistant and easily eroded materials of: 



where _tf_ is in hours and _hw_ is in meters. 

15 

Von Thun and Gillette also developed equations for breach formation time based on observations of average lateral erosion rates (the ratio of final breach width to breach formation time) versus depth of water above the breach invert.  They found a stronger correlation between the lateral erosion rate and depth than for the total breach formation time versus depth.  Tests of fuse plug embankments intended to erode easily suggest upper bounds on the lateral erosion rate.  Using lateral erosion rate data, Von Thun and Gillette put forth two additional equations: 



with _hw_ and _B_ both given in meters.  Each of these equations requires an assumption or prediction of the average breach width. 

These equations reflect both case study data and results of controlled laboratory tests of fuse plug embankments (Pugh, 1985) using both highly erodible and slightly cohesive materials. 

###### **_Predicting Peak Outflows from Case Study Data_** 

In lieu of determining breach parameters and then routing inflow and reservoir storage through the breach, many investigators have used the case study data to develop empirical equations relating peak breach outflow to dam height, reservoir storage volume, or combinations of the two.  These relations are summarized in Table 1 and discussed in more detail below.  Figures 13 through 15 also graphically show these relations compared to the case study data. 

Kirkpatrick (1977) presented data from 13 embankment dam failures and 6 additional hypothetical failures, and proposed a best-fit relation for peak discharge as a function of the depth of water behind the dam at failure.  This analysis included data from the failure of St. Francis Dam, California, which was a concrete gravity structure.  St. Francis Dam was originally thought to have failed due to piping through the right abutment, but a recent study suggests that it may have failed due to a combination of overturning of a concrete gravity section and landslide failure of the left abutment, and thus may not be appropriate for inclusion in the analysis (Rogers and McMahon, 1993). 

The Soil Conservation Service (1981) used the 13 case studies cited by Kirkpatrick to develop a power law equation relating the peak dam failure outflow to the depth of water at the dam at the time of failure.  This appears to be an enveloping curve, although three data points are slightly above the curve.  Reclamation (1982) extended this work and proposed a similar envelope equation for peak breach outflow using case study data from 21 dams. 

16 

Singh and Snorrason (1982 and 1984) presented  relations for peak dam failure outflow as functions of dam height and reservoir storage.  These relations were developed using the results of eight simulated dam failures analyzed using DAMBRK and HEC-1.  In their 1984 paper, only the storage-peak outflow relation was presented, as it exhibited the lowest standard error. 

Graham (undated) summarized breach and peak outflow data for 19 dams and compared estimated actual outflows to those predicted using the Reclamation equation (1982), the envelope equation of Hagen (1982), and a best-fit relation for peak outflow as a combined power function of reservoir storage and depth of water at time of failure. 

MacDonald and Langridge-Monopolis (1984) developed best-fit and envelope curves for peak outflow from breached earthfill dams as a function of the breach formation factor described earlier.  These curves were used to verify reasonable results from breach simulations carried out using breach parameters predicted from the breach formation factor.  Similar relations were sought for non-earthfill dams (e.g., rockfill, erosion resistant cores, etc.), but the data were too scattered to fit any single relation. 

Costa (1985) presented a comprehensive summary of flood discharges resulting from the failures of all types of constructed and natural dams.  He presented envelope curves and regression equations for peak flow from breached constructed dams as functions of dam height, storage volume at time of failure, and the product of these two parameters.  Costa included data for the failure of St. Francis Dam (a concrete gravity structure) in his analysis, but this does not appear to have dramatically influenced the results. 

Froehlich (1995a) developed a best-fit regression equation for prediction of peak discharge based on reservoir volume and head, using data from 22 case studies for which peak discharge data were available.  He also presented a computational procedure for determining confidence intervals and identifying hidden extrapolation in the estimates. Froehlich’s approach differed from those of previous investigators; he permitted an additional degree of freedom in the regression analysis by allowing the exponents on the volume and head terms to be independent of one another. 

#### **Physically-Based Dam Breach Prediction Models** 

Numerous authors have proposed and developed physically-based, numerical dam breach models in the past 30 years.  Table 3 lists the major models commonly referenced in the literature, their associated sediment transport models, and other characteristics (Singh and Scarlatos, 1988; Wurbs, 1987).  These models are described in more detail below. 

Cristofano (1965) proposed the first physically based dam breach model.  The model related the rate of erosion of the breach channel to the water flowrate through the breach, using an equation that accounted for the shear strength of soil particles and the force of the flowing water.  The model assumed a trapezoidal breach of constant bottom width; side slopes of the breach were determined by the angle of repose of the material, and the bottom slope of the breach channel was equal to the internal angle of friction of the material.  An empirical coefficient was critical to the model’s performance (Fread, 1988). 

17 

Table 3. — Physically-based embankment dam breach models <u>(Singh and Scarlatos, 1988; Wurbs, 1987).</u> 

|**Model and Year **|**Sediment**<br>**Transport**|**Breach**<br>**Morphology**|**Parameters**|**Other**<br>**Features**|
|---|---|---|---|---|
|Cristofano (1965)|Empirical<br>formula|Constant breach<br>width|Angle of<br>repose, others||
|Harris and Wagner (1967);<br>BRDAM (Brown and Rogers,<br>1977)|Schoklitsch<br>formula|Parabolic<br>breach shape|Breach<br>dimensions,<br>sediments||
|DAMBRK (Fread, 1977)|Linear pre-<br>determined<br>erosion|Rectangular,<br>triangular, or<br>trapezoidal|Breach<br>dimensions,<br>others|Tailwater<br>effects|
|Lou (1981);<br>Ponce and Tsivoglou (1981)|Meyer-Peter<br>and Müller<br>formula|Regime type<br>relation|Critical shear<br>stress,<br>sediment|Tailwater<br>effects|
|BREACH (Fread, 1988)|Meyer-Peter<br>and Müller<br>modified by<br>Smart|Rectangular,<br>triangular, or<br>trapezoidal|Critical shear,<br>sediment|Tailwater<br>effects, dry<br>slope stability|
|BEED (Singh and Scarlatos,<br>1985)|Einstein-<br>Brown formula|Rectangular or<br>trapezoidal|Sediments,<br>others|Tailwater<br>effects,<br>saturated<br>slope stability|
|FLOW SIM 1 and FLOW SIM 2<br>(Bodine, undated)|Linear pre-<br>determined<br>erosion;<br>Schoklitsch<br>formula option|Rectangular,<br>triangular, or<br>trapezoidal|Breach<br>dimensions,<br>sediments||



Harris and Wagner (1967) applied the Schoklitsch sediment transport equation to dam breach flows.  They assumed breach erosion to begin immediately upon overtopping, and to proceed until the breach reached the bottom of the dam.  Brown and Rogers (1977, 1981) presented a breach model, BRDAM, based on Harris and Wagner’s work, which was applicable to overtopping and piping induced breaches. 

Lou (1981) and Ponce and Tsivoglou (1981) presented a model that linked the Meyer-Peter and Müller sediment transport equation to the one-dimensional differential equations of unsteady flow and sediment conservation.  The differential equations were solved with a four-point implicit finite difference scheme that was computationally complex and prone to problems of numerical instability.  Flow resistance in the breach channel was represented using Manning’s _n_ .  The breach width was empirically related to the flow through the breach.  The model accounted for reservoir storage depletion in its upstream boundary condition. 

The DAMBRK model (Fread, 1977) contains a breach simulation routine in which the breach is initiated at the top of the dam and grows uniformly downward and outward to reach ultimate breach dimensions at a user-specified time.  Fread (1988) developed the physically-based BREACH model to more realistically simulate breaches initiated by overtopping or piping.  The model uses the Meyer-Peter and Müller sediment transport equation as modified by Smart (1984) for steep channels.  The model permits specification of three different embankment materials:  an inner core, an outer portion (downstream 

18 

shell), and a vegetated cover or riprap protective layer on the downstream face of the dam. Flow through the breach section is determined by orifice or weir equations, and flow down the face of the dam is modeled as a quasi-steady uniform flow with roughness determined from the Strickler equation for Manning’s _n_ .  The model uses a much simpler computational algorithm than that of Ponce and Tsivoglou (1981).  The model accounts for spillway flows around man-made dams and includes the effect of tailwater depth on breach outflows.  The model introduces two structural mechanisms that may contribute to breach formation:  the breach shape may be impacted by slope stability of the breach sideslopes, and possible collapse of the upper portion of the dam by shear and sliding is analyzed. 

Today, the BREACH model is probably the best known physically based model.  The most commonly applied breach prediction method in practice is probably the use of the uniform breach formation rate routines contained in DAMBRK and other models, with reference to the numerous case study investigations discussed earlier in this report.  However, there are several recently developed and less commonly used models. 

The FLOW SIM 1 and FLOW SIM 2 models are primarily flood routing models, but also contain uniform breach formation routines similar to that in DAMBRK.  Both FLOW SIM models also have optional breach formation routines based on the Schoklitsch bed load formula. 

The BEED (Breach Erosion of Embankment Dams) model developed by Singh and Scarlatos (1985) is a physically-based model simulating breach evolution, flood routing, and sediment routing.  Erosion and sediment transport are computed using the equations of Einstein-Brown and Bagnold.  Singh and Quiroga (1988) point out that the use of these equations requires making assumptions of their utility far beyond the original ranges stipulated for them. 

Macchione and Sirangelo (1988, 1990) have recently proposed a dam breach model based on the Meyer-Peter and Müller formula. 

In general, most of the available numerical dam breach models rely on bed-load type erosion formulas that imply assumptions of gradually varied flow and relatively large flow depth in comparison to the size of roughness elements.  These formulations may be appropriate for some stages of the breach process, but are not consistent with the mechanics of much of the breaching process as observed in the field and in the laboratory. 

#### **Mechanics of Embankment Erosion During Overtopping Flow** 

Ralston (1987) provided a good description of the mechanics of embankment erosion.  For cohesive soil embankments, breaching takes place by headcutting.  A small headcut is typically formed near the toe of the dam and then advances upstream until the crest of the dam is breached (Figure 2).  In some cases a series of stairstep headcuts forms on the downstream face of the dam.  This action is similar to that described by Dodge (1988) for model testing of embankment overtopping.  The relevant processes are headcut initiation and advance by hydrodynamic and geotechnical mass wasting.  Erosion analysis using a tractive stress procedure is not consistent with these mechanics. 

19 

Ralston noted that the failure of noncohesive soil embankments can be modeled with a tractive stress analysis, but only if the embankment does not contain a cohesive core. Seepage through the embankment exiting on the eroding face will also increase the rate of erosion.  If the embankment contains a cohesive core that is symmetrical about the axis of the dam, the core will be eroded in a manner similar to that for a cohesive embankment.  If the core is sloped such that the downstream shell provides structural support for the core, as in the fuse plug model tests of Pugh (1985), the core will fail structurally as the downstream shell is eroded away (Figure 3).  It should be emphasized that this design is not common in embankment dams, but was designed specifically to produce reliable, Figure 2. — Progressive headcutting breach of a cohesive controlled breaching of a fuse plug soil embankment (Powledge et al., 1989b). embankment. 

Powledge et al. (1989a,b) summarized ongoing research efforts of several entities aimed at developing new methods for protecting embankments from erosion during overtopping flow, and for predicting erosion of protected and unprotected embankments.  Research in several small-scale facilities was considered to be qualitative due to the difficulty of adequately reproducing the complex processes of erosion and sediment transport in steep, shallow flows at small scales; research in large-scale facilities was considered more quantitative.  All of the studies indicate that embankment erosion is a multivariable, multidisciplinary problem.  Random influences can be substantial, and thus, repetition of model tests is critical. 

Powledge et al. (1989b) described three hydraulic flow regimes and erosion zones for flow overtopping an embankment (Figure 4).  In the subcritical flow region on the dam crest, energy slopes, velocities, and tractive stresses are relatively low and erosion will occur only if the crest materials are highly erodible.  A transition to supercritical flow occurs on the 



Figure 3. — Schematic of the breaching process for a specially designed fuse plug embankment with a downstream-sloped core section (Pugh, 1985). 

20 

downstream portion of the crest.  Energy slopes and tractive stresses are higher in this region, and erosion is sometimes observed at the knickpoint at the downstream edge of the crest.  When the crest is paved, uplift of the paving materials is also possible if the pavement is underlain by permeable materials.  The third zone of erosion is the downstream face of the dam, on which the flow accelerates at supercritical depths until reaching uniform flow conditions.  Tractive stresses are very 



Figure 4. — Flow and erosion regimes in embankment overtopping (Powledge et al., 1989b). 

high, and changes in slope or surface discontinuities can concentrate stresses and initiate erosion.  Analyses based on tractive stress are probably only applicable until erosion is initiated, whereafter surface discontinuities make tractive stress analyses questionable. Erosion may initiate at any point on the slope, but the toe is the most common location for initiation of erosion.  Once erosion has been initiated, a headcutting behavior is generally observed in which the scour hole moves upstream and widens.  In cohesive embankments, the overfall perimeter of the scour hole will assume a semi-circular shape which improves stability of the headcut through arching of the soil mass. 

Powledge summarized by noting six factors affecting embankment erosion: 

1. Embankment configuration, materials, and densities of fill. 

2. Maximum velocity attained by flow. 

3. Discontinuities, cracks, or voids in the slope, and appurtenances or anomalies at the toe. 

4. Presence and depth of tailwater on the downstream slope. 

5. Flow concentration at low points along the embankment or at abutment groins. 

6. Toe drains, blanket drains, or highly erodible materials in the abutments or foundation that will cause undercutting of cohesive fill materials and accelerate headcut advance. 

Previous physical model testing efforts relevant to the problem of dam breaching have been undertaken by Reclamation.  Pugh (1985) studied the breaching and washout of specially designed fuse plug embankments for control of emergency spillways.  The embankments tested were designed to breach quickly and then erode laterally at controlled rates.  The rate of lateral erosion was related to the height of the fuse plug embankment and the depth of flow through the breach.  Von Thun and Gillette (1990) incorporated these results into their erosion rate-based method for estimating breach width. 

Dodge (1988) reported on the results of early tests by Reclamation of overtopping flows over model embankment dams.  The tests were designed to evaluate the effectiveness of various crest and embankment face protection schemes that would permit overtopping flow without causing dam breach.  Although none of the tested embankments were fully breached, the observations of flow characteristics and review of relevant erosion models are enlightening.  In all cases, flow over the  embankments was initially described as a plane 

21 

shear flow, but eventually reached a point at which the flow was described as a chute-andpool flow.  The chute-and-pool flow was characterized by reduced erosion rates compared to plane shear flow.  Soil placement conditions had a dramatic effect on the erosion process. A literature review concluded that there was a lack of verified governing equations for sediment transport and hydraulic behavior of steep shallow flows. 

Reclamation has actively pursued the development of embankment protection measures that would permit safe overtopping of embankment dams.  Tests conducted by Simons, Li, and Associates in Fort Collins, Colorado (Clopper and Chen, 1988) evaluated grass cover, soil cement, gabions, cable-tied concrete block systems, and two proprietary systems, Enkamat® (a three-dimensional nylon and monofilament fabric structure) and Geoweb® (a cellular grid confinement system).  Recent efforts have been focused on concrete wedge block systems (Frizell et al., 1994) and large riprap armoring (Frizell and Ruff, 1995). Testing on these options is being conducted in a large-scale outdoor facility where discharge up to 1.4 m<sup>3</sup> /s/m (15 ft<sup>3</sup> /s/ft) can be achieved in a 15.2-m (50-ft) high, 3-m (10-ft) wide flume on a 2h:1v slope.  The large riprap tests may be especially relevant to predicting initial failure of riprap protection that would lead to breach development. 

#### **Headcut Erosion** 

The observations of Ralston (1987) and Powledge et al. (1989a,b), and the testing by Pugh (1985) and Dodge (1988) indicate that headcut formation and advance are critical processes in embankment dam breach.  Similar mechanisms are important in the erosion of earth and rock spillways.  The mechanics of headcut erosion causing breach of an earth spillway are discussed in detail by Temple (1989).  The U.S. Army Corps of Engineers also conducted an extensive investigation of rock erosion in emergency spillways, summarized in five volumes published between 1986 and 1990.  The fourth volume of this series (May, 1989) describes laboratory testing to define mechanisms of headcut advance and the influence of discharge, tailwater depth, and nappe aeration.  This testing showed that the primary mechanism of upstream headcut advance was progressive scouring of supporting material from the lower portion of the face of a free overfall (Figure 5).  This leads to tension failure of the overhanging material.  Nappe aeration appeared to be a critical feature.  Aerated nappes tend to spring free from the overfall, directing erosive energy to the floor of the downstream channel, away from the base of the overfall.  Non-aerated nappes remain attached to the downstream face of the overfall, thereby concentrating erosion on the material at the base of the overfall.  This creates the greatest potential for rapid headward advance.  This study concluded that periods of relatively low discharge which may produce non-aerated nappes can produce the most dramatic headcutting.  High flows may have relatively low headcut advance rates in erosion resistant materials. 

###### **_The NRCS SITES Model_** 

In recent years the Natural Resources Conservation Service (NRCS; formerly the Soil Conservation Service), and the Agricultural Research Service (ARS) have made some of the most notable quantitative contributions to the modeling of headcut erosion.  This work has been performed primarily in connection with the analysis of vegetated earth spillways.  A headcut erosion model based on this work is being incorporated into the NRCS Structure 

22 

Site Analysis program (SITES), recently released for public distribution.  This program was formerly known as DAMS2. 

The SITES model is an integrated design program for the hydraulic and hydrologic analysis of dams.  Temple et al. (1994) described the features of the model and changes from the previous DAMS2 model.  The most extensive changes and those of interest here are related to analysis of the stability and integrity of vegetated earth spillways.  The NRCS has assisted in the construction of over 23,000 structures of this type in the United States (Cato and Mathewson, 1989).  Breaching of these structures may lead to complete loss of a reservoir, as in the 1983 failure of the spillway at Black Creek Site 53 in the Black Creek watershed of the Yazoo Basin in Mississippi (Temple, 1989).  The new technology in the SITES model will allow the use of designs based on allowable erosionally effective stresses established in Agriculture Handbook 667 (Temple et al., 1987).  The new procedure will replace previous permissible velocity design procedures contained in SCS-TP-61  (SCS, 1947). 



Figure 5. — Flow over an idealized headcut with and without aeration of the nappe (May, 1989). 

In 1983, the SCS and ARS launched an extensive effort to better understand the processes of vegetated earth spillway failure and develop new tools and technology for design and analysis of such spillways.  This effort included laboratory research and extensive field investigations of spillways experiencing significant flows or erosion damage.  Laboratory research and field data collection are continuing. 

Erosion of vegetated earth spillways is modeled in three phases by the SITES program (Temple et al., 1994).  The three phases are cover failure, headcut formation, and headcut advance.  Details of the technology are given by Temple and Hanson (1994), and Temple and Moore (1994).  The model is two-dimensional. 

The phase 1 and phase 2 erosion processes are simulated with a detachment rate model of the form: 



where: ε! = rate of soil detachment (mass/time) 

_kd_ = detachment rate coefficient τ _e_ = erosionally effective stress τ _c_ = critical shear stress 

Phase 1 consists of erosion of soil through the vegetal cover leading to cover failure.  Under the assumption that τ _e_ >> τ _c_ , the critical shear stress is assumed to be zero, and the erosionally effective stress is integrated through time until the integral reaches a value associated with failure.  The erosionally effective stress is the estimated effective stress on 

23 

the soil particles contained within the soil and vegetal root matrix.  It is computed from a tractive stress relation incorporating a vegetal cover factor, the soil grain roughness of the underlying soil expressed in terms of Manning’s coefficient, and the Manning’s _n_ of the channel as a whole.  The failure threshold is related to the plasticity index of the soil. 

Once phase 1 failure has occurred, erosion continues into the material below the vegetated cover.  In this phase, critical stress is determined from Shields criteria.  The detachment rate coefficient is determined from a relation based on regression analysis of ten documented studies of 98 fine-grained materials.  The relation incorporates the dry unit weight and percent clay for the soil material.  Alternatively, the coefficient may be determined from a direct measurement of soil erodibility using a jet-index test described by Hanson (1991).  Phase 2 erosion continues until the depth of erosion is sufficient to permit headcut advance to begin.  This occurs when erosion reaches a depth at which the flow plunges and impacts near the base of a vertical or near-vertical face.  This concentrates stress and flow energy dissipation at the base of the overfall.  Temple and Hanson (1994) approximate this condition as the point at which the tailwater depth is equal to or less than critical depth. 

Phase 3 erosion consists of the upstream advance of the headcut.  Stein and Julien (1993) note two modes of headcut advance and present a parameter to distinguish between modes. If downward erosion of the upstream brink dominates, a rotating headcut is produced that tends to flatten as it migrates.  If headward erosion of the downstream scour hole dominates, undercutting of the headcut face is produced and a stepped headcut is produced in which the headcut retains a vertical face as it moves upstream.  Stepped headcuts occur routinely in the field during high energy erosion of rock and noncohesive soils. 

In the SITES model headcut advance is assumed to occur in the stepped mode.  The headward advance is modeled using a relation based on hydraulic energy dissipation rate and a headcut erodibility index characterizing the geologic resistance of the spillway materials (Temple and Moore, 1994).  The hydraulic attack is modeled using the flow energy dissipation rate (power) per unit width of headcut, 



where: _E_<sup>!</sup> = energy dissipation rate per unit width 

_q_ = unit discharge γ = unit weight of water _H_ = change in energy gradeline elevation through the headcut, approximated as the height of headcut 

The headcut erodibility index is essentially that presented by Kirsten (1988) for use in evaluating resistance to excavation by ripping.  The index varies from 0.01 for noncohesive sand to values greater than 10,000 for hard, massive rock.  It correlates geologic parameters with drawbar power required for excavation.  This index has also been used in the determination of support ratios for span design in mining and tunneling operations. The index is computed by the relation: 



where: _Kh_ = headcut erodibility index 

24 

_Ms_ = earth mass strength number 

_RQD_ = rock quality designation 

_Jn_ = joint set number _Js_ = relative ground structure number 

_Jr_ = joint roughness number 

_Ja_ = joint alteration number 

Temple and Moore (1994) provide additional details on each of these parameters.  Kirsten (1988) and Annandale (1995) provide aids for use in their determination.  The parameters can be readily assessed in the field using simple identification tests and measurements. The mass strength number, _Ms_ , represents the strength of an intact representative sample of the material.  The ratio _RQD/Jn_ represents the mean block or fragment size based on the relative spacing of joints within the mass.  The ground structure number, _Js_ , incorporates the effect of orientation of the material structure relative to the flow direction. The ratio _Jr/Ja_ represents the shearing strength of joints within the mass, or the shear strength of interparticle bonds. 

There are two components in the headcut advance model.  A threshold relation determines whether headcut advance occurs.  An advance rate relation then determines the rate of headcut advance.  Both the threshold and the rate are correlated with the headcut erodibility index.  Empirical constants in the relations were determined by fitting to field data collected at NRCS dams between 1983 and 1994.  This data collection effort was quite extensive, and only the best-documented case studies were included in the data set used to calibrate the model.  The threshold relation was calibrated against 46 data points for which headcut advance could be described qualitatively.  The advance rate relation was correlated using data from 33 headcuts for which advance rates could be estimated.  The value of one constant was determined based on a simplified theoretical analysis (Temple, 1989 and 1992) and confirmed by fitting with the field data.  Conservative assumptions and procedures were used in the development of the model, although the model is intended to provide a best estimate of the headcut advance rate. 

The headcut advance model was tested against a data set containing 10 additional headcuts not included in the calibration analysis (Temple and Moore, 1994).  In only three of these cases were the results heavily dependent on phase 3 erosion (headcut advance). For two of these spillways constructed in weaker materials, the model predicted erosion consistent with that observed.  For one spillway constructed in stronger materials, the model underpredicted the observed erosion.  The authors felt in this case that the determination of the headcut erodibility index for the eroded materials was questionable. 

###### **_Physical Model Testing of Headcut Erosion_** 

Robinson and Hanson (1993, 1995) reported the results of large-scale tests of twodimensional headcut erosion on two different soil types (red sandy clay [CL) and silty sand [SM]) under constant hydraulic conditions (drop height, discharge, and tailwater level). Soil properties were further varied by placing materials at different moisture and density conditions.  The influence of an underlying sand layer was also studied.  Figure 6 shows a schematic of a headcut with an erosion resistant upper layer and less resistant lower layer. The tests were performed in a flume facility constructed by ARS at their Plant Science and 

25 

Water Conservation Research Laboratory in Stillwater, Oklahoma.   Headcut advance rates were heavily dependent on soil placement conditions, varying by a factor of more than 100.  Advance rates declined as soil unconfined compressive strengths increased. When the overlying material was erosion resistant, the underlying sand layer permitted undercutting of the overlying material and dramatically increased the advance rate.  When overlying materials were highly erodible, the sand layer had little influence (Robinson and Hanson, 1994c). 

Robinson and Hanson (1994b, 1996a) also presented results of model testing to determine headcut advance rates for a single cohesive soil (the red sandy clay, CL) with variable overfall heights and discharges.  These tests indicated that uniform headcut advance rates could be produced during individual tests, but advance rates varied significantly between tests due to variations of the placed-soil  properties, primarily density and moisture content.  These variations overshadowed the effects of drop height and discharge when analyzing headcut advance rates. 

Robinson and Hanson (1996b) reported on the influence of backwater levels on headcut advance rates.  They found that the maximum advance rate occurred at a backwater to overfall height ratio of about 0.8.  This compared well with predicted stresses on the vertical headcut face (Robinson, 1992), which peak at the same backwater to overfall height ratio.  Variations of backwater level changed the headcut advance rates by factors ranging from 2.6 to 7.5 over the range of soil conditions tested. 

###### **_Deterministic Headcut Advance Models_** 

Robinson and Hanson (1994a) proposed a more complex computer model for headcut advance, combining stress prediction and mass wasting models.  The location of the overfall nappe is predicted, and hydraulic stresses on the boundary of an overfall (floor and vertical face) are estimated using relations developed from laboratory testing by Robinson (1992).   The mass failure component balances forces on the predicted failure mass to determine when the headcut becomes unstable.  A time lag in the model allows for the transport of material out of the scour hole following a mass failure.  The model has been tested against two observed spillway headcutting events, and results have been promising. 



Figure 6. — Schematic of a headcut in layered materials at Lake Brownwood Spillway, Texas.  Erosion resistant limestone overlies a weaker layer of shale with thin interbedded sandstone layers (May, 1989). 

26 

###### **_Ongoing ARS Research_** 

The ARS laboratory in Stillwater, Oklahoma, is currently pursuing the extension of their headcut erosion models to embankment breach problems.   Sectional model testing of six vegetated embankment sections is planned for Spring 1997.  The ARS lab is also conducting tests to establish discharge coefficients for flow through breach openings of varying dimensions and shapes.  Both of these efforts have direct application to the development of improved dam breach prediction models. 

#### **Erosion Models Based on Energy Dissipation Rate** 

The NRCS SITES model uses the energy dissipation rate as the primary measure of hydraulic attack causing headcut erosion.  Energy and energy dissipation are also important concepts in more traditional low-energy erosion and sediment transport processes.  Turbulence is important to many detachment and transport processes and can be correlated with energy dissipation within the flow.  Annandale (1995) discussed the use of energy dissipation per unit width for estimating erosion thresholds related to headcuts, hydraulic jumps, grade changes, and gradually-varied open channel flows.  Annandale presented a continuous relation between energy dissipation rate and erosion thresholds for real data spanning a continuum of earth materials from 0.1-mm diameter cohesionless soils to jointed and fractured rock.  These materials span a range of 15 orders of magnitude of the headcut erodibility index. 

Bagnold (1966) defined stream power as the product of bed shear stress and average velocity, yielding a parameter with dimensions of power (energy dissipation) per unit bed area.  This variable has proven to be useful in developing relations for total sediment discharge in streams.  Yang (1972) defined unit stream power as the product of velocity and energy slope; this parameter expresses the rate of potential energy dissipation per unit weight of water.  Yang and Molinas (1982) provided theoretical justification for a relation between unit stream power and turbulence energy production and showed that total sediment transport relations based on this parameter are generally superior to relations based solely on water discharge, flow velocity, energy slope, or shear stress.  However, the data used to test the relations are restricted to river environments with slopes not greater than about 1 percent.  Dimensionless unit stream power is the unit stream power divided by the terminal fall velocity of a sediment particle.  Yang developed sand (1973) and gravel (1984) transport relations based on this parameter. 

###### **_STARS and GSTARS_** 

The STARS (Sediment Transport and River Simulation) model is a one-dimensional, steady state, water and sediment-routing model based on a streamtube concept in which a threedimensional river reach is subdivided into streamtubes, each comprising a subvolume of the river reach between two cross sections.  Within each streamtube, erosion and deposition take place based on numerous optional sediment transport equations, including those of Yang, Ackers and White, and Engelund and Hansen.  The model has been documented by Orvis and Randle (1987) who noted potential applications of the model for long term degradation and aggradation studies, armoring of rivers, scour due to channel 

27 

constrictions, and scour and deposition patterns as they relate to problems of locating water intakes and diversion structures. 

GSTARS (Generalized Stream Tube model for Alluvial River Simulation) is a moregeneralized implementation of the STARS model (Yang et al., 1988).  The GSTARS model allows for supercritical/subcritical flow transitions, and both width and depth adjustments of a channel.  The latest versions of the GSTARS model also contain routines for bank stability and local scour at a headcut, two potentially important mechanisms in dam breach erosion (Song et al., 1995; Yang, 1996). 

The width and depth adjustments in the GSTARS model are made using the principle of minimum rate of energy dissipation (Yang and Song, 1979).  This principle states that a stream will change its channel geometry in a manner that tends toward producing a minimum rate of energy dissipation.  In application, the model determines, at each time step, the rates of energy dissipation that would be produced by changes in channel width versus changes in channel bed elevation.  Erosion of the channel proceeds in the direction that produces the minimum rate of energy dissipation. 

The bank stability routine maintains bank slopes at or below a critical slope determined from field surveys.  The local scour routine relates the sediment transport below a free overfall to the stream power dissipated in the drop, _q_ γ _H_ .  This routine simulates only vertical erosion of the streambed below the headcut.  It does not allow for scouring back into the downstream face of the overfall or for headward advance of the overfall.  In this respect, the GSTARS headcut module is less robust than that in the SITES model.  The GSTARS model has been used to simulate a deepening, but stationary, headcut forming downstream from the control sill in the spillway channel at Willow Creek Dam spillway. The model has also effectively modeled erosion downstream from a concrete cutoff wall in the spillway at Lake Mescalero Dam. 

#### **Embankment Armoring Failure** 

The first phase of failure of an embankment dam via overtopping is the initial failure of the protective cover (vegetation, riprap, or some other protective material) on the downstream face of the dam.  High-velocity, highly turbulent flow over the downstream face of the dam will erode the cover material, leading to flow concentration, gullying, and increased erosion.  Coarse-grained cobble fills are the most common cover material for Reclamation’s embankment dams, and studies performed on riprap may apply.  Stability of riprap has been an active research problem for many years, although testing of large material (>10 cm diameter), on steep slopes, under high unit discharges is difficult and expensive. 

Hartung and Scheuerlein (1970) considered the problem of designing rockfill dams to permit overflow during extreme floods.  They proposed a relation for fully-developed flow velocity over the downstream face of a rockfill dam as a function of the flow depth, slope, rock size, a particle packing factor, and an aeration factor.  This analysis does not consider the possibility of failure near the crest (where flow is not fully developed) or in a hydraulic jump at the toe of the dam.  The velocity down the slope is given by: 

28 



where: _v_ = flow velocity _ym_ = mean water depth normal to the slope θ = angle of the slope λ = a surface flow resistance factor analogous to Darcy-Weisbach’s _f_ given by: 



_d s_ where: _dm_ = mean roughness height (approximated by ) 3 _ds_ = equivalent stone diameter, d50 

_c_ = a coefficient depending on aeration and particle packing: 



where: σ = aeration factor defined as the specific weight of the air-water mixture divided by the specific weight of pure water β = packing factor, defined as the height of one roughness element divided by the distance between roughness elements 

The aeration factor is given by: 



This set of equations may be used to determine the flow depth and velocity corresponding to different unit discharges down the slope. 

Hartung and Scheuerlein also developed a relation for the critical velocity, _vc_ , required to dislodge a given particle: 



where: δ = angle of repose of the stones 

γ _s_ = unit weight of stones γ _w_ = unit weight of water 

Knauss (1979) compared the design formulas of Hartung and Scheuerlein and an earlier formula proposed by Olivier (1967) based on experimental work by Linford and Saunders (1967).  Knauss concluded that the formula of Hartung and Scheuerlein was preferable, although he proposed some simplifications to make the procedure more amenable to numerical solution. 

Dewey and Oaks (1990) used the equations of Hartung and Scheuerlein to develop an analysis procedure for determining whether dam breach would initiate due to overtopping. They assumed the unit discharge on the downstream slope to be given by a broad-crested 

29 

weir equation applied to the dam crest.  They developed a nomograph that indicated the threshold of failure (in terms of overtopping head) for a given rock size, dam slope, and riprap type (angular vs. rounded).  This was accomplished by iteratively solving equations 9 through 13 to determine the overtopping head that produces flow velocity equal to the threshold failure velocity. 

Once the failure threshold is exceeded, Dewey and Oaks proposed a second analysis to determine whether the duration and intensity of overtopping flow conditions is sufficient to develop a breach that will lead to failure of the dam.  This analysis uses the work of Riley (1986), who developed criteria for permissible duration of overtopping flow (volume and depth) on vegetated embankment dams, adapted from SCS criteria (1973) for flow duration in vegetated earth spillways.  Dewey and Oaks note that similar criteria are needed for nonvegetated dams.  The new NRCS SITES software discussed earlier provides tools for evaluating the permissible duration of flow over both vegetated and nonvegetated surfaces. These techniques offer the potential for further improvement and more generalized application of the method described by Dewey and Oaks. 



where: _T_ = Shields parameter τ = bed shear stress α = bed slope δ = angle of repose of the bed material. 

For large boundary Reynolds numbers (>10<sup>3</sup> ), most investigators have found the critical value of Shields parameter at incipient motion to be a constant, although the exact value has been widely debated.  Shields found the critical value to be 0.60.  Gessler (1967) interpreted the Shields parameter as a measure of the probability of motion and asserted that the critical value reported by other investigators corresponds to a 50 percent probability of particle motion.  Gessler adjusted Shields’ data to account for shear due to bedforms and found the critical value of Shields parameter to be 0.047.  All of this work was done for relatively deep flows on shallow slopes. 

Based on testing of shallow flows on rough, steep slopes, other investigators have proposed critical values of Shields parameter ranging upwards to 0.25.  Wittler (1994) argued that the differences in the reported critical value of Shields parameter were due to aeration bulking of the flow and its effect on the calculation of Shields parameter.  Accounting for the effects of aeration, Wittler hypothesized that the correct critical value of Shields parameter is 0.047, even for shallow, highly aerated flows down rough, steep slopes. Wittler (1994) and Abt et al. (1987, 1988) also studied the influence of riprap gradation uniformity.  They found that well graded mixtures (less uniform) had significantly lower failure thresholds and quantified this difference through the use of a coefficient of uniformity and a coefficient of stability. 

30 

Recent testing of flow over large riprap on a 2h:1v slope at Colorado State University may shed additional light on these issues.  Testing at this facility includes measurement of velocity, air concentration, and interstitial flow.  This testing is aimed primarily at developing methods for protecting embankment dams from failure due to overtopping flows, but will also lead to better understanding of failure thresholds (Frizell and Ruff, 1995). 

#### **Lateral Erosion Models** 

Most breaches have been observed to erode vertically down to the base of the dam, then laterally if significant reservoir storage is remaining.  For large reservoirs impounded by relatively small dams, the reservoir level does not change significantly during the early stages of the embankment breach, and lateral erosion can take place while the reservoir head remains high.  As a result, the peak breach outflow can occur during the lateral erosion phase, as the breach opening continues to enlarge under a relatively constant reservoir head.  For this reason, lateral erosion is an important factor that should be included in a dam breach simulation model. 

Pugh (1985) reported on model tests of the breach and subsequent lateral erosion of engineered fuse plug embankments designed for use as control structures on auxiliary spillways.  The mechanics of the breach process were observed and were found to be similar to those described by other investigators and discussed earlier.  The unique feature of these embankments was the use of an impervious core section inclined adverse to the flow direction as was shown in Figure 3.  Once the downstream shell material was washed away, this core section failed structurally in the manner of a cantilevered beam. The breaching behavior was consistent and repeatable. 



Figure 7. — Lateral erosion of fuse plug embankments (Pugh, 1985). 

Once breached, the embankments eroded laterally, with flow as shown in Figure 7.  Pugh related the lateral erosion rate _EL_ to the embankment height _H_ , and provided an equation to predict the lateral erosion rate for embankments of similar geometry to those tested, in the height range of 3 to 9 m (10 to 30 ft). 



Empirical factors were also provided to correct for variations of the ratios of flow depth to embankment base width and flow depth to embankment height.  For cases with relatively more or less downstream shell material, Pugh recommended adjusting the erosion rate inversely to the difference in volume of shell material, as compared with the reference embankments tested in the study. 

31 



<!-- Start of picture text -->
Distribution of Height Parameters Distribution of Volume Parameters<br>25% 15%<br>Height of Dams in Case Study Database Storage of Case Study Dams<br>Structural Height of DSIS Embankment Dams Maximum Storage of DSIS Embankment Dams<br>20%<br>10%<br>15%<br>10%<br>5%<br>5%<br>0% 1 10 Height, meters 100 1000 0%10 3 10 4 10 5 Storage, cubic meters10 6 10 7 10 8 10 9 10 10<br>Distribution of Storage/Height Ratios Distribution of Breach Formation Factors<br>10% 15%<br>9% Dam Failure Case Study Database 14% Dam Failure Case Study Database<br>Embankment Dams in DSIS Database 13% Embankment Dams in DSIS Database<br>8% 12%<br>11%<br>7%<br>10%<br>6% 9%<br>8%<br>5%<br>7%<br>4% 6%<br>5%<br>3%<br>4%<br>2% 3%<br>2%<br>1%<br>1%<br>0% 0%<br>10 3 10 4 10 5 10 6 10 7 10 8 10 9 10 5 10 6 10 7 10 8 10 9 10 10 10 11 10 12<br>Storage to Height Ratio, m 2 Breach Formation Factor, m 4<br>Cases Cited Cases Cited<br>Cases Cited Cases Cited<br><!-- End of picture text -->

Figure 8. — Distribution of height and volume parameters for dam breach case studies and embankment dams in DSIS database. 

## **DAM FAILURES CASE STUDY DATABASE** 

The case study database assembled from the references described previously contains information on 108 embankment dam breaches.  The type, amount and quality of data available for individual case studies varies dramatically.  There are several instances of significant discrepancies between similar data reported by multiple investigators. 

As one means of assessing the applicability of the case study database, Reclamation’s Dam Safety Information System (DSIS) was queried to determine the characteristics of the embankment dams to which a new breach model might be applied within Reclamation. The DSIS database contains information on more than 1,200 dams that are under the authority of the Dam Safety program.  The database is still under construction, so there are many dams for which all data are not available.  Only 301 dams in the database could be positively identified as embankment dams. 

Figure 8 shows the distribution of height, storage, storage-to-height ratios, and breach formation factors for the dams cited in the 108 dam breach case studies, and for the 301 embankment dams identified in the DSIS database.  It should be noted that the DSIS database contains information on only the structural height of the dam, whereas many of 

32 



<!-- Start of picture text -->
125<br>100<br>75<br>50<br>25<br>0<br>0 50 100 150 200 250<br>Breach Width (meters)<br>5(hb )=B<br>4(hb )=B<br>3(hb )=B<br>0.5(hb )=B hb=B 2(hb )=B<br>Breach Height (meters)<br><!-- End of picture text -->

Figure 9. — Observed breach height and width for 84 dams in the case study database. 

the dam failure case studies report other variations on the height parameter.  The figures show that in general the dams in the DSIS database have larger heights and greater reservoir storage than the dams in the case study set.  The DSIS dams also have greater storage-to-height ratios and breach formation factors.  This suggests that the set of case studies may under-represent the large reservoir case, in which the peak outflow can occur after the breach reaches the base of the dam and during the phase of lateral erosion and expansion of the breach width.  However, there is also the possibility that large dams and reservoirs are presently over-represented in the DSIS database, since the database is still incomplete, and the largest, most significant dams have probably been entered into the database first. 

#### **Observed Breach Parameters in Case Studies** 

The most commonly reported breach parameters in the case study database are the depth and width of breach, and the angle of the breach side slopes.  The time of failure was reported in less than half of the cases, and often with great uncertainty.  Ultimate breach depth can be estimated to a reasonable degree of accuracy for most cases, since breach depth is usually on the order of the original dam height.  However, ultimate breach width and time of failure exhibit great variability. 

###### **_Breach Width_** 

Figure 9 shows the observed average breach width versus the observed breach height for 84 dams from the case study database.  Guidance from numerous sources discussed earlier in the report suggests that the breach width should be in the range of 2 to 5 times the dam height or breach height (which usually approximates the dam height).  Figure 9 shows that even with the enlarged case study database, this suggested range is reasonable, but probably cannot be refined much further without resorting to a multi-parameter relation. 

33 



<!-- Start of picture text -->
Von Thun & Gillette (1990) Froehlich (1995) Reclamation (1988)<br>300 300 300<br>250 250 250<br>200 200 200<br>150 150 150<br>100 100 100<br>50 50 50<br>0 0 0<br>0 50 100 150 200 250 300 0 50 100 150 200 250 300 0 50 100 150 200 250 300<br>Observed Breach Width (meters) Observed Breach Width (meters) Observed Breach Width (meters)<br>Line of Agreement<br>Predicted Breach Width (meters)<br><!-- End of picture text -->

Figure 10. — Predicted vs. observed breach widths using three different prediction equations. 

The relations proposed by Reclamation (1988), Von Thun and Gillette (1990), and Froehlich (1995b), were discussed earlier in this report.   Figure 10 compares the predicted and observed breach widths for each of these relations, using data from the case study database.  The figure shows 78 cases compared to the Von Thun and Gillette relation, 77 cases compared to the Froehlich equation, and 80 cases compared to the Reclamation equation.  (Von Thun and Gillette used 57 of these cases to develop their relation; Froehlich used 60 of these cases.)  Froehlich’s relation appears to be the best predictor for the cases with observed breach widths less than 50 meters. 

###### **_Time of Failure_** 

Several investigators have attempted to relate the elapsed time required for failure to basic geometric, hydrologic, and hydraulic parameters, as discussed previously in this report. Some of these relations have predicted the time of failure directly from parameters that may be estimated with reasonable accuracy prior to a dam failure, such as the hydraulic head above the assumed breach invert, the breach height, or the reservoir storage.  Other relations depend on knowledge of the breach width or volume of eroded material.  These are parameters that can be determined following a breach, but they cannot be estimated with great certainty prior to a breach.  These relations may be less useful as predictors of the time of failure. 

MacDonald and Langridge-Monopolis (1984) predicted the lower envelope of the time of failure as a function of the volume of material eroded from the embankment during the breach.  The volume of eroded material was predicted as a function of the breach formation factor (product of the volume of water outflow and initial depth of water above the breach invert).  Figure 11 shows the results of predicting the eroded material volume for 60 of the dam failure cases contained in the database assembled for this study.  Thirty-eight of these cases were used in the initial development of the relation. 

34 

Unfortunately, the specific parameters that form the breach formation factor were not documented for many cases, although similar parameters were available.  For this analysis, these other similar parameters were substituted for the strictly defined parameters used to compute the breach formation factor.  In place of the total outflow through the breach, the total reservoir storage or the storage above the breach bottom were used when they were reported.  In place of the head above the breach bottom, the height of the dam or the depth of breach were used when they were available. 

Figure 12 shows the predicted and observed times of failure for dams in the case study database, using the relations proposed by Von Thun and Gillette (1990), Froehlich (1995b), MacDonald and Langridge-Monopolis (1984), and Reclamation (1988).  For some case studies, different investigators reported differing times of failure or a range of possible values.  These data are plotted on the figure using horizontal error bars to indicate the range of uncertainty.  The figure demonstrates the inaccuracy of the currently available prediction equations.  Most equations tend to underpredict the failure time, although even the envelope equation proposed by MacDonald and Langridge-Monopolis overpredicts the failure time in some cases. 

#### **MacDonald & Langridge-Monopolis** 

**_Prediction of Embankment Material Eroded_** 



<!-- Start of picture text -->
10 7<br>10 6<br>10 5<br>10 4<br>10 3<br>10 2<br>10 2 10 3 10 4 10 5 10 6 10 7<br>Observed Volume of Material Eroded (m3)<br>+1 order of magnitude prediction errorLine of Agreement<br>-1 order of magnitude prediction error<br>3Predicted Volume of Material Eroded (m)<br><!-- End of picture text -->

Figure 11. — Predicted and observed volume of eroded material for 60 dam failures, using the relation proposed by MacDonald and Langridge-Monopolis (1984). 

35 



<!-- Start of picture text -->
10 Froehlich (1995)<br>Horizontal bars indicate a range<br>1<br>of reported failure times. Predictions<br>using Von Thun and Gillette equations<br>include judgment of erodible vs.<br>erosion-resistant embankment,<br>0.1 based on embankment description.<br>0.01<br>0.01 0.1 1 10<br>Von Thun and Gillette (1990) Von Thun and Gillette (1990)<br>10 10<br>tf=f(hw) tf=f(B, hw)<br>1 1<br>0.1 0.1<br>0.01 0.01<br>0.01 0.1 1 10 0.01 0.1 1 10<br>MacDonald and Langridge-Monopolis (1984)<br>10 10 Reclamation (1988)<br>1 1<br>0.1 0.1<br>0.01 0.01<br>0.01 0.1 1 10 0.01 0.1 1 10<br>Observed Time of Failure (hours) Observed Time of Failure (hours)<br>Line of Agreement<br>Predicted Time of Failure (hours)<br>Predicted Time of Failure (hours)<br>Predicted Time of Failure (hours)<br><!-- End of picture text -->

Figure 12. — Predicted and observed time of failure for dams in the case study database. 

36 

#### **Comparing Peak Flow Relations to Case Studies** 

As discussed previously, numerous investigators have attempted to relate the peak breach outflow to measures of height or head (e.g., dam height, breach height, or depth of water above breach bottom), storage or outflow volume, or a product of height and volume. Figures 13 through 15 compare these relations to the case study data.  Admittedly, each of these relations was developed from a smaller dataset and in many cases data restricted to a particular subset of dams.  Still, the figures show the degree of variability in the case study data when examined as a function of any simple combination of the relevant parameters.  The observed peak outflows vary by at least one order of magnitude through most of the range of the available data. 

### Peak Discharge vs. Height Parameters 



<!-- Start of picture text -->
100000<br>Observed peak outflow vs.  hw<br>Observed peak outflow vs.  hd<br>Kirkpatrick, 1977 (based on  hw )<br>SCS, 1981 (based on  hw )<br>10000<br>Reclamation, 1982<br>     (envelope eqn. based on  hw )<br>Singh & Snorrason, 1984 (based on  hw )<br>1000<br>100<br>10<br>1<br>1 10 100<br>Height of Dam ( hd ) or Depth of Water at Dam at Failure ( hw ) -- (meters)<br>Peak Outflow (m3/sec)<br><!-- End of picture text -->

Figure 13. — Comparison of case study data and proposed relations for peak outflow as a function 

of height parameters. 

37 

## Peak Discharge vs. Storage Parameters 



<!-- Start of picture text -->
1000000<br>O b served peak  o utflow vs.   S<br>O b served peak  o utflow vs.   Vw<br>S i ngh and Snorr a son, 1984 (ba s ed on   S  )<br>100000<br>C o sta, 1985 (en v elope eqn. ba s ed on  S  )<br>E v ans, 1986 (ba s ed on   Vw )<br>10000<br>1000<br>100<br>10<br>1<br>10 3 10 4 10 5 10 6 10 7 10 8 10 9<br>Total Reservoir Storage ( S  ) or Storage Above Breach Invert ( Vw ) -- (m 3 )<br>Peak Outflow (m3/sec)<br><!-- End of picture text -->

Figure 14. — Comparison of case study data and proposed relations for peak outflow as a function of storage parameters. 

Froehlich (1995a) related the peak outflow to a power equation of both the breaching head and outflow volume, using case study data for 22 dam failures: 



Figure 16 shows the results of using Eq. 16 to predict peak outflows for a total of 32 case studies, including the 22 used in the development of the equation.  The ten additional data points fit the relation well; details of these 10 case studies are summarized in Table 4.  The slope-area measurements for Schaeffer and Swift Dams were made significantly 

38 

#### Peak Discharge vs. (Volume*Height) Parameters 

Observed peak outflow vs. _S*hd_ Observed peak outflow vs. _Vout*hw_ Hagen, 1982 (envelope eqn. based on _S*hd_ ) Costa, 1985 (based on _S*hd_ ) Costa, 1985 (envelope eqn. based on _S*hd_ ) MacDonald & Langridge-Monopolis, 1984 (based on _Vw*hw_ ) MacDonald & Langridge-Monopolis, 1984 (envelope eqn. based on _Vw*hw_ ) 



<!-- Start of picture text -->
10 5<br>10 4<br>10 3<br>10 2<br>10 1<br>10 0<br>10 3 10 4 10 5 10 6 10 7 10 8 10 9 10 10 10 11<br>( S*hd ) or ( Vout*hw ) -- (m 4 )<br>Peak Outflow (m3/sec)<br><!-- End of picture text -->

Figure 15. — Comparison of case study data and proposed relations for peak outflow as a function of the product of height and storage parameters. 

downstream of the dams, so the observed flows close to the dams were likely higher than those indicated, which would lead to an even better match between the predicted and observed flows. 

The five case studies at the bottom of Table 4 did not fit the relation well and are not shown in the figure.  Details of each of these failures and the method of peak flow determination are given below: 

- South Fork Tributary - This was a very small dam and reservoir whose failure was caused by the upstream failure of the much larger North Branch Tributary Dam. 

39 



<!-- Start of picture text -->
Froehlich (1995a) relation to predict peak discharge<br>100000<br>Case studies used to develop<br>Froehlich relation<br>Additional case studies<br>91 101<br>10000<br>Predicted<br>Peak 93<br>Flow 52<br>(m 3 /s) 71<br>1000<br>7<br>56<br>60<br>92<br>100<br>82<br>10<br>10 100 1000 10000 100000<br>Observed Peak Flow (m 3 /s)<br>Line of agreement<br><!-- End of picture text -->

Figure 16. — Predicted and observed peak discharges for dams in the case study database, using Froehlich’s equation (1995a). 

Observed peak outflow was much larger than that predicted by equation 16, as would be expected. 

- North Branch Tributary - The peak outflow was determined using a slope-area measurement (Costa, 1985), but the location and other details of the measurement are not given.  In addition, Singh and Scarlatos (1988) reported a peak flow of 290 m<sup>3</sup> /s, ten times greater than that reported by MacDonald and Langridge-Monopolis (1984) and Costa (1985). 

- Goose Creek, Frankfurt, and Davis Reservoir Dams - The method and details of peak flow determination are unknown. 

Based on this analysis, it appears the Froehlich relation is one of the better available methods at this time for direct prediction of peak breach discharge. 

40 

Table 4. — Additional dams analyzed using Froehlich’s 1995 peak flow prediction equation.  Shaded lines <u>are case studies not included on Figure 16.  See table A2 for key to references.</u> 

||Dam|Predicted Peak<br>Flow,m<sup>3</sup>/s|Observed Peak<br>Flow,m<sup>3</sup>/s|Method of Peak Flow<br>Determination|References<br>(Qpeakref in**bold**)|
|---|---|---|---|---|---|
|7|Buffalo Creek|762|1420|slope-area measurement|f,**g**,h,q|
|52|Lake Avalon|2540|2320|unknown|**h**,k|
|56|Lake Latonka|525|290|unknown|**h**,i,k|
|60|Lawn Lake|354|510|dam-break model|**g**,i,k,q|
|71|Martin Cooling<br>PondDike|2170|3115|unknown|**p**,**q**|
|82|Otto Run|74.2|60|slope-area measurement|f,**g**,h|
|91|Salles Oliveira|11600|7200|unknown|f,**h**|
|92|SandyRun|219|435|unknown|**f**,**h**,**q**|
|93|Schaeffer|3840|4500|slope-area measurement 13 km<br>downstream; twice average outflow<br>during½ hrto drain reservoir|d,f,**g**,h,i,k,q|
|101|Swift|12600|24900|slope-area measurement 27 km<br>downstream|d,f,**g**,q|
|98|South Fork<br>Tributary|14.5|122|slope-area measurement|f,**g**,h|
|78|North Branch<br>Tributary|96.0|29.4|slope-area measurement|f,**g**,h|
|30|Goose Creek|106|565|unknown|**f**,g,h|
|25|Frankfurt|358|79|unknown|f,**h**|
|17|Davis|2470|510|unknown|**f**,g|



Webby (1996), in his discussion of Froehlich (1995a), used dimensional analysis techniques to develop a similar equation for peak outflow using Froehlich’s data.  In dimensional form, this equation is: 



and in non-dimensional form: 



These relations have a slightly poorer fit to the data than Froehlich’s equation but offer the desirable feature of dimensional consistency. 

Walder and O’Connor (1997) presented a relatively simple, physically-based model of dambreach formation and used it to show that dimensionless peak breach outflow, * 1/2 / 1/2 7 2 _Qp_ = _Qp_ / _g d_ 5 2 is primarily a function of a dimensionless parameter, η = _kV_ 0 / _g d_ / , where _Qp_ is the peak breach outflow, _g_ is the acceleration of gravity, _d_ is the drop in reservoir level, _V_ 0 is the water volume released, and _k_ is the mean vertical erosion rate of the breach. 

For values of η >> 1, the dimensionless peak outflow asymptotically approaches a maximum value as η increases.  This maximum value is a weak function of the ratio of breach width to breach depth, the side slope angle of the breach opening, and the initial water level as a fraction of the dam height.  Physically, this is the case of relatively fast 

41 

breach formation or large reservoir volume, in which the peak outflow occurs when the breach reaches maximum depth, and prior to any significant drawdown of the reservoir. 

For values of η << 1, the dimensionless peak outflow is primarily a power function of η , _Qp_<sup>_*_</sup> _=_ αη<sup>β</sup> , where α and β are weak functions of reservoir and breach geometry parameters. Physically, this is the case of relatively slow breach formation or small reservoir volume, in which the peak outflow occurs well before the breach reaches maximum depth; there is little head remaining in the reservoir by the time the breach reaches its maximum depth. 

Walder and O’Connor recommend a simple procedure for rapidly estimating the breach hydrograph as follows: 

- Compute values of η for plausible values of _d_ , _V_ 0, and _k_ .  They suggest that _k_ is typically between 10 m/hr and 100 m/hr, based on actual case study data.  The drop in the water surface, _d_ , is typically 50 to 100% of dam height, tending toward 100% of dam height for engineered structures. 

- For values of η outside of the range 0.6 to 5, use the following predictive relations (in dimensional form): 



where _Dc_ is the height of the dam crest relative to the dam base. 

- For values of η between 0.6 and 5, the dimensionless peak outflow can be determined graphically, using a figure given in Walder and O’Connor’s paper that shows the asymptotic approach of the dimensionless peak outflow to the relations given in equations 19 and 20. 

- Time to peak breach outflow, _tp_ , can also be determined through a similar procedure, using relations and a figure provided in the electronic supplement to Walder and O’Connor’s paper.  The approximate breach hydrograph can then be assumed as triangular, with a peak value _Qp_ at time _tp_ , and terminating at an elapsed time of 2 _V_ 0 _/Qp_ . 

This set of procedures offers the advantage of a thoeretical foundation that accounts for the differences and limitations imposed by the large- and small-reservoir cases.  It should be a valuable tool for making reconnaissance level estimates of breach hydrographs. 

42 

## **DEVELOPMENT OF A NEW DAM BREACH MODEL** 

A new dam breach model should address the following questions: 

- For a given set of conditions, will a dam breach? 

- How much time is required to initiate a breach? 

- How will the breach develop once it is initiated (ultimate dimensions, rate of development, total time to reach ultimate dimensions, etc.)? 

The model should be applicable to both overtopping and piping- or seepage-induced failures, although the initial focus of model development should be on the more tractable problem of overtopping failures.  The model should also be applicable to widely varying embankment designs, ranging from homogeneous fills to landslide dams to highly engineered zoned fills. 

Recent advances in technology for analyzing headcut erosion, riprap stability, erosion of vegetated surfaces, and high energy erosion of resistant earth materials have come about through extensive large-scale physical modeling efforts and collection of case study data from prototype structures.  Similarly, large-scale physical modeling will be required to address complicating factors in embankment breaching processes such as: 

- Variable embankment and foundation configurations, materials, and densities of fill 

- Effect of discontinuities, singularities, and flow concentrations 

- Presence and depth of tailwater on the downstream slope 

- Unique embankment features (e.g., toe drains, blanket drains, erodible filter zones) 

- The three-dimensional nature of real embankments and flow through breach openings 

Physical hydraulic model testing may include both two-dimensional modeling of embankment sections and three-dimensional modeling of entire embankments.  Physical model testing will improve understanding of the fundamental mechanics of embankment breach events and will also provide opportunities to calibrate and verify new models. 

Physical modeling should be performed at large scales to overcome the problems of simultaneous scaling of hydraulic conditions and material properties.  Although hydraulic modeling at small scales is a well-developed science, material properties do not scale uniformly and can be difficult to reproduce at small scales.  Using large-scale models allows the use of near-prototype size materials, making results more reliable and easier to interpret.  It will, of course, be impossible to conduct true full-scale testing for larger dams, but scales should be sufficiently large to allow the use of prototype embankment materials. The tests should produce erosive mechanisms and conditions comparable to those encountered in a prototype condition.  A variety of embankment designs, foundation configurations, and headwater and tailwater conditions should be studied. 

Because large-scale physical model testing is inherently expensive, it will also be economical to make use of data obtained from real-world case studies of past and future dam failures.  This report has highlighted some of the gaps in the existing case study data. The formation of a standing forensic team that can quickly investigate failures or incidents of dam survival of extreme events (e.g., overtopped, but not failed) would be extremely valuable. 

43 

## **BIBLIOGRAPHY** 

- Abt, S.R., R.J. Wittler, J.F. Ruff, D.L. LaGrone, M.S. Khattak, J.D. Nelson, N.E. Hinkle, and D.W. Lee, 1988, _Development of Riprap Design Criteria by Riprap Testing in Flumes: Phase I_ , U.S. Nuclear Regulatory Commission, NUREG/CR-4651, ORNL/TM-10100/V1, vol. 1, 1987. 

- Abt, S.R., R.J. Wittler, J.F. Ruff, D.L. LaGrone, M.S. Khattak, J.D. Nelson, N.E. Hinkle, and D.W. Lee, 1988, _Development of Riprap Design Criteria by Riprap Testing in Flumes: Phase II. Followup Investigations_ , U.S. Nuclear Regulatory Commission, NUREG/CR-4651, ORNL/TM-10100/V2, vol. 2, September 1988. 

- Annandale, G.W., 1995, “Erodibility,” _Journal of Hydraulic Research_ , vol. 33, no. 4, 1995. 

- Babb, A.O. and T.W. Mermel, 1968, _Catalog of Dam Disasters, Failures and Accidents_ , Bureau of Reclamation, Washington, DC. 

- Bagnold, R.A., 1966, _An Approach to the Sediment Transport Problem from General Physics_ , Geological Survey Professional Paper 422-I, GPO, Washington, DC. 

- Baker, M., and M. Bliss, 1996, _Trip Report for Dams on Mescalero Indian Reservation_ , U.S. Bureau of Reclamation, Technical Service Center, Denver, Colorado. 

- Ballentine, George D., 1993, “Failure and Rehabilitation of Kendall Lake Dam,” _Dam Safety ’93_ , Proceedings of the 10th Annual ASDSO Conference, Kansas City, Missouri, September 26-29, 1993, p. 89-91. 

- Bodine, B.R., undated, _Users Manual for FLOW SIM 1, Numerical Method for Simulating Unsteady and Spatially Varied Flow in Rivers and Dam Failures_ , U.S. Army Corps of Engineers, Southwestern Division, Dallas, Texas. 

- Brown, C.A., and W.J. Graham, 1988, “Assessing the Threat to Life from Dam Failure,” _Water Resources Bulletin_ , vol. 24, no. 6, December, 1988. 

- Brown, Richard J., and David C. Rogers, 1977, “A Simulation of the Hydraulic Events During and Following the Teton Dam Failure,” _Proceedings of the Dam-Break Flood Routing Workshop_ , Water Resources Council, p. 131-163. 

- Brown, Richard J., and David C. Rogers, 1981, _Users Manual for Program BRDAM_ , U.S. Bureau of Reclamation, Denver, Colorado, April 1981, 73 p. 

- Brua, Stan A., 1978, _Floods of July 19-20, 1977 in the Johnstown Area, Western Pennsylvania_ , USGS Open-File Report 78-963, 62 p. 

- Cato, K.D., and C.C. Mathewson, 1989, _Rock Material Performance During Emergency Spillway Flows_ , ASAE Paper No. 89-2649, St. Joseph, Michigan. 

- Chen, Y.H., and B.A. Anderson, 1986, “Development of a Methodology for Estimating Embankment Damage Due to Flood Overtopping,” _Final Report_ , Simons, Li and Assoc., Inc., Federal Highway Administration, and Forest Service, Contract number DTFH61-82-C-00104, SLA Project Number DC-FHA-01. 

- Clopper, Paul E., and Yung-Hai Chen, 1987, “Predicting and Minimizing Embankment Damage Due to Flood Overtopping,” in _Hydraulic Engineering_ , Proceedings of the 1987 ASCE National Conference on Hydraulic Engineering, Williamsburg, Virginia, August 3-7, 1987, p. 751-756. 

- Clopper, Paul E., and Yung-Hai Chen, 1988, _Minimizing Embankment Damage During Overtopping Flow_ , Report No. FHWA-RD-88-181, Federal Highway Administration, McLean, Virginia, 214 p. 

- Costa, John E., 1985, _Floods from Dam Failures_ , U.S. Geological Survey Open-File Report 85-560, Denver, Colorado, 54 p. 

44 

- Cristofano, E.A., 1965, _Method of Computing Erosion Rate for Failure of Earthfill Dams_ , U.S. Bureau of Reclamation, Denver, Colorado. 

- Dekay, M.L., and G.H. McClelland, 1991, _Setting Decision Thresholds for Dam Failure Warnings: A Practical Theory-Based Approach_ , CRJP Technical Report No. 328, Center for Research on Judgment and Policy, University of Colorado, Boulder, Colorado. 

- Dewey, Robert L., and Ronald A. Oaks, 1990, _The Determination of Failure of an Embankment Dam During Overtopping_ , draft Technical Memorandum No. MISC-3620-1, Bureau of Reclamation, Denver, Colorado, May 1989, revised April 1990. 

- Dewey, Robert L., and David R. Gillette, 1993, “Prediction of Embankment Dam Breaching for Hazard Assessment,” _Proceedings_ , ASCE Specialty Conference on Geotechnical Practice in Dam Rehabilitation, Raleigh, North Carolina, April 25-28, 1993. 

- Dodge, Russell A., 1988, _Overtopping Flow on Low Embankment Dams — Summary Report of Model Tests_ , REC-ERC-88-3, U.S. Bureau of Reclamation, Denver, Colorado, August 1988, 28 p. 

- Evans, Steven G., 1986, “The Maximum Discharge of Outburst Floods Caused by the Breaching of Man-Made and Natural Dams,” _Canadian Geotechnical Journal_ , vol. 23, August 1986. 

- Federal Energy Regulatory Commission, 1987, _Engineering Guidelines for the Evaluation of Hydropower Projects_ , FERC 0119-1, Office of Hydropower Licensing, July 1987, 9 p. 

- Fischer, Gary R., 1996, “Breach Characteristics of Dams in Montana,” _Dam Safety ’96_ , Proceedings of the 1996 ASDSO Conference, Seattle, Washington. 

- Fread, D.L., 1977, “The Development and Testing of a Dam-Break Flood Forecasting Model,” in _Proceedings of the Dam-Break Flood Routing Model Workshop_ , Bethesda, Maryland, p. 164-197. 

- Fread, D.L., 1984, _DAMBRK: The NWS Dam-Break Flood Forecasting Model_ , National Weather Service, Office of Hydrology, Silver Spring, Maryland. 

- Fread, D.L., 1988 (revised 1991), _BREACH: An Erosion Model for Earthen Dam Failures_ , National Weather Service, National Oceanic and Atmospheric Administration, Silver Spring, Maryland. 

- Fread, D.L., 1993, “NWS FLDWAV Model: The Replacement of DAMBRK for Dam-Break Flood Prediction,” _Dam Safety ’93_ , Proceedings of the 10th Annual ASDSO Conference, Kansas City, Missouri, September 26-29, 1993, p. 177-184. 

- Frizell, Kathleen H., and James F. Ruff, 1993, “Large-Scale Embankment Overtopping Protection Tests,” in _Hydraulic Engineering ‘93_ , Proceedings of the 1993 ASCE Hydraulics Division Specialty Conference, San Francisco, California, July 25-30, 1993, p. 1951-1956. 

- Frizell, Kathleen H., Douglas H. Smith, and James F. Ruff, 1994, “Stepped Overlays Proven for Use in Protecting Overtopped Embankment Dams,” _Dam Safety ‘94_ , Proceedings of the 1994 ASDSO Conference, Boston, Massachusetts, September 11-14, 1994. 

- Frizell, Kathleen H., and James F. Ruff, 1995, “Embankment Overtopping Protection—Concrete Blocks or Riprap,” _Water Resources_ , Proceedings of the 1995 ASCE Water Resources Engineering Division Specialty Conference, San Antonio, Texas, August 14-18, 1995, p. 10211025. 

- Froehlich, David C., 1987, “Embankment-Dam Breach Parameters,” _Hydraulic Engineering_ , Proceedings of the 1987 ASCE National Conference on Hydraulic Engineering, Williamsburg, Virginia, August 3-7, 1987, p. 570-575. 

- Froehlich, David C., 1995a, “Peak Outflow from Breached Embankment Dam,” _Journal of Water Resources Planning and Management_ , vol. 121, no. 1, p. 90-97. 

45 

- Froehlich, David C., 1995b, “Embankment Dam Breach Parameters Revisited,” _Water Resources Engineering_ , Proceedings of the 1995 ASCE Conference on Water Resources Engineering, San Antonio, Texas, August 14-18, 1995, p. 887-891. 

- Froehlich, David C., 1996, closure to discussion of “Peak Outflow from Breached Embankment Dam” (1995a), _Journal of Water Resources Planning and Management_ , vol. 122, no. 4, p. 317-319. 

- Gerodetti, M., 1981, “Model Studies of an Overtopped Rockfill Dam,” _International Water Power & Dam Construction_ , September 1981, p. 25-31. 

- Gessler, J., 1967, _The Beginning of Bedload Movement of Mixtures Investigated as Natural Armoring in Channels_ , W.M. Keck Laboratory of Hydraulics and Water Resources, California Institute of Technology, Pasadena, California, 1965-1967. 

- Graham, Wayne J., 1983, _Physical and Breach Parameters for Dams with Large Storage to Height Ratios_ , unpublished internal document, U.S. Bureau of Reclamation, Denver, Colorado, 1 p. 

- Graham, Wayne J., undated, _Actual and Equation Derived Dam Failure Flood Peaks_ , unpublished internal document, U.S. Bureau of Reclamation, Denver, Colorado, 1 p. 

- Hagen, Vernon K., 1982, “Re-evaluation of Design Floods and Dam Safety,” _Proceedings_ , 14th Congress of International Commission on Large Dams, Rio de Janeiro. 

- Hagen, Vernon K., 1996, discussion of “Peak Outflow from Breached Embankment Dam” (Froehlich, 1995a), _Journal of Water Resources Planning and Management_ , vol. 122, no. 4, p. 314-316. 

- Hanson, G.J., 1990a, “Surface Erodibility of Earthen Channels at High Stresses Part I - Open Channel Testing,” _Transactions of the ASAE_ , vol. 33, no. 1, 1990, p. 127-131. 

- Hanson, G.J., 1990b, “Surface Erodibility of Earthen Channels at High Stresses Part II - Developing an In Situ Testing Device,” _Transactions of the ASAE_ , vol. 33, no. 1, 1990, p. 132-137. 

- Hanson, G.J., 1991, “Development of a Jet Index to Characterize Erosion Resistance of Soils in Earthen Spillways,” _Transactions of the ASAE_ , vol. 34, no. 5, 1991, p. 2015-2020. 

- Harris, G.W., and D.A. Wagner, 1967, _Outflow from Breached Earth Dams_ , University of Utah, Salt Lake City, Utah. 

- Hartung, F., and H. Scheuerlein, 1970, “Design of Overflow Rockfill Dams,” in _Proceedings_ , International Commission on Large Dams, Tenth International Congress on Large Dams, Q.36, R.35,  Montreal, Canada, June 1-5, 1970, p. 587-598. 

- Hollick, M., 1976, “Towards a Routine Test for the Assessment of the Critical Tractive Forces of Cohesive Soils,” _Transactions of the ASAE_ , vol. 19, 1976, p. 1076-1081. 

- Hydrologic Engineering Center, 1981, _HEC-1 Flood Hydrograph Package, Users Manual_ , U.S. Army Corps of Engineers, Davis, California. 

- Jansen, R.B., 1983, _Dams and Public Safety_ , U.S. Dept. of  the Interior, Bureau of Reclamation, Denver, Colorado. 

- Johnson, F.A., and P. Illes, 1976, “A Classification of Dam Failures,” _International Water Power and Dam Construction_ , December 1976, p. 43-45. 

- Kirkpatrick, Gerald W., 1977, “Evaluation Guidelines for Spillway Adequacy,” _The Evaluation of Dam Safety_ , Engineering Foundation Conference, Pacific Grove, California, ASCE, p. 395414. 

- Kirsten, H.A.D., 1988, “Case Histories of Groundmass Characterization for Excavatability,” _Rock Classification Systems for Engineering Purposes_ , ASTM, STP 984, edited by L. Kirkaldie, pp. 102-120. 

46 

- Knauss, J., 1979, “Computation of Maximum Discharge at Overflow Rockfill Dams,” _Proceedings_ , International Commission on Large Dams, Thirteenth International Congress on Large Dams, Q.50, R.9,  New Delhi, India, 1979, p. 143-160. 

- Latray, Dean A., and Otto R. Stein, 1997, “Headcut Advance in Stratified Soils,” _Proceedings_ , 27th IAHR Congress, San Francisco, California, August 10-15, 1997, 5 p. 

- Linford, A. and D.H. Saunders, 1967, _A Hydraulic Investigation of Through and Overflow Rockfill Dams_ , Report RR 888, British Hydromechanics Research Association. 

- Lou, W.C., 1981, _Mathematical Modeling of Earth Dam Breaches_ , Thesis, presented to Colorado State University, at Fort Collins, Colorado, in partial fulfillment of the requirements for the degree of Doctor of Philosophy. 

- McCann, Martin, 1995, “National Performance of Dams Program,” _Dam Safety ’95_ , Proceedings of the 1995 ASDSO Annual Conference, September 17-20, 1995. 

- Macchione, F., and B. Sirangelo, 1988, “Study of Earth Dam Erosion Due to Overtopping,” _Proceedings of the Technical Conference on Hydrology of Disasters_ , WMO, Geneva, Switzerland, p. 212-219. 

- Macchione, F., and B. Sirangelo, 1990, “Floods Resulting from Progressively Breached Dams,” _Hydrology in Mountainous Regions. II - Artificial Reservoirs; Water and Slopes_ , Proceedings of Lausanne Symposia, IAHS Publication No. 194, August 1990, p. 325-332. 

- MacDonald, Thomas C., and Jennifer Langridge-Monopolis, 1984, “Breaching Characteristics of Dam Failures,” _Journal of Hydraulic Engineering_ , vol. 110, no. 5, p. 567-586. 

- McMahon, George F., 1981, “Developing Dam-Break Flood Zone Ordinance,” _Journal of the Water Resources Division, Proceedings of the ASCE_ , vol. 107, no. WR2, p. 461-478. 

- May, James H., 1989, _Geotechnical Aspects of Rock Erosion in Emergency Spillway Channels; Report 4: Geologic and Hydrodynamic Controls on the Mechanics of Knickpoint Migration_ , Technical Report REMR-GT-3, Corps of Engineers ,Waterways Experiment Station, Vicksburg, Mississippi. 

- Miller, S. Paul, and David C. Ralston, 1987, “Embankment Overtopping - Case Histories,” _Hydraulic Engineering_ , Proceedings of the 1987 ASCE National Conference on Hydraulic Engineering, Williamsburg, Virginia, August 3-7, 1987, p. 739-744. 

- Molinas, A., and C.T. Yang, 1985, “Generalized Water Surface Profile Computation,” _Journal of Hydraulic Engineering_ , vol. 111, no. 3, March 1985, p. 381-397. 

- Moore, John S., Darrel M. Temple, and H.A.D. Kirsten, 1994, “Headcut Advance Threshold in Earth Spillways,” _Bulletin of the Association of Engineering Geologists_ , vol. XXXI, no. 2, June 1994, p. 277-280. 

- Moore, Walter L., and Frank D. Masch, Jr., 1962, “Experiments on the Scour Resistance of Cohesive Sediments,” _Journal of Geophysical Research_ , vol. 67, no. 4, April 1962, p. 1437-1449. 

- Olivier, H., 1967, “Through and Overflow Rockfill Dams — New Design Techniques,” _Proceedings I.C.E._ , 36, Paper No. 7012. 

- Orvis, Curtis J., and Timothy J. Randle, 1987, _STARS: Sediment Transport and River Simulation Model_ , Technical Guideline, Bureau of Reclamation, Denver, Colorado, July 1987, 212 p. 

- Parrett, Charles, Nick B. Melcher, and Robert W. James, Jr., 1993, _Flood Discharges in the Upper Mississippi River Basin, 1993_ , U.S. Geological Survey Circular 1120-A, 14 p. 

- Petrascheck, A.W., and P.A. Sydler, 1984, “Routing of Dam Break Floods,” _International Water Power and Dam Construction_ , vol. 36, p. 29-32. 

47 

- Ponce, Victor M., 1982, _Documented Cases of Earth Dam Breaches_ , San Diego State University Series No. 82149, San Diego, California. 

- Ponce, Victor M., and Andrew J. Tsivoglou, 1981, “Modeling Gradual Dam Breaches,” _Journal of the Hydraulics Division, Proceedings of the ASCE_ , vol. 107, no. 7, p. 829-838. 

- Powledge, George R., D.C. Ralston, P. Miller, Y.H. Chen, P.E. Clopper, and D.M. Temple, 1989a, “Mechanics of Overflow Erosion on Embankments. I: Research Activities,” _Journal of Hydraulic Engineering_ , vol. 115, no. 8, August 1989, p. 1040-1055. 

- Powledge, George R., D.C. Ralston, P. Miller, Y.H. Chen, P.E. Clopper, and D.M. Temple, 1989b, “Mechanics of Overflow Erosion on Embankments. II: Hydraulic and Design Considerations,” _Journal of Hydraulic Engineering_ , vol. 115, no. 8, August 1989, p. 1056-1075. 

- Pugh, Clifford A., 1985, _Hydraulic Model Studies of Fuse Plug Embankments_ , REC-ERC-85-7, U.S. Bureau of Reclamation, Denver, Colorado, December 1985, 33 p. 

- Ralston, David C., 1987, “Mechanics of Embankment Erosion During Overflow,” _Hydraulic Engineering_ , Proceedings of the 1987 ASCE National Conference on Hydraulic Engineering, Williamsburg, Virginia, August 3-7, 1987, p. 733-738. 

- Riley, R.C., 1986, “A Procedure for Evaluating Permissible Limits of Overtopping of Vegetated Earthen Embankments,” _Dam Safety ’86_ , Proceedings of the 1986 ASDSO Annual Meeting, Austin, Texas, October 1986. 

- Robinson, K.M., 1992, “Predicting Stress and Pressure at an Overfall,” _Transactions of the ASAE_ , vol. 35, no. 2, March/April 1992, p. 561-569. 

- Robinson, K.M., and G.J. Hanson, 1993, “Large-Scale Headcut Erosion Testing,” presented at the _1993 ASAE International Winter Meeting_ , Paper No. 93-2543, Chicago, Illinois, December 1417, 1993, 13 p. 

- Robinson, K.M., and G.J. Hanson, 1994a, “A Deterministic Headcut Advance Model,” _Transactions of the ASAE_ , vol. 37, no. 5, 1994, p. 1437-1443. 

- Robinson, K.M., and G.J. Hanson, 1994b, “Gully Headcut Advance,” presented at the _1994 ASAE International Winter Meeting_ , Paper No. 94-2577, Atlanta, Georgia, December 13-16, 1994, 15 p. 

- Robinson, K.M., and G.J. Hanson, 1994c, “Influence of a Sand Layer on Headcut Advance,” _Hydraulic Engineering ’94_ , Proceedings of the 1994 ASCE National Conference on Hydraulic Engineering, Buffalo, New York, August 1-5, 1994, 5 p. 

- Robinson, K.M., and G.J. Hanson, 1995, “Large-Scale Headcut Erosion Testing,” _Transactions of the ASAE_ , vol. 38, no. 2, p. 429-434. 

- Robinson, K.M., and G.J. Hanson, 1996a, “Gully Headcut Advance,” _Transactions of the ASAE_ , vol. 39, no. 1, p. 33-38. 

- Robinson, K.M., and G.J. Hanson, 1996b, “Influence of Backwater on Headcut Advance,” _North American Water & Environment Congress,_ Anaheim, California, June 22-28, 1996. 

- Rogers, J. David, and David J. McMahon, 1993, “Reassessment of the St. Francis Dam Failure,” _Dam Safety ’93_ , 10th Annual ASDSO Conference, Kansas City, Missouri, September 26-29, 1993, p. 333-339. 

- Singh, Krishan P., and Arni Snorrason, 1982, _Sensitivity of Outflow Peaks and Flood Stages to the Selection of Dam Breach Parameters and Simulation Models_ , SWS Contract Report 288, Illinois Department of Energy and Natural Resources, State Water Survey Division, Surface Water Section at the University of Illinois, 179 p. 

48 

- Singh, Krishan P., and Arni Snorrason, 1984, “Sensitivity of Outflow Peaks and Flood Stages to the Selection of Dam Breach Parameters and Simulation Models,” _Journal of Hydrology_ , vol. 68, p. 295-310. 

- Singh, V.P., and P.D. Scarlatos, 1985, _Breach Erosion of Earthfill Dams and Flood Routing: BEED Model_ , Research Report, Army Research Office, Battelle, Research Triangle Park, North Carolina, 131 p. 

- Singh, V.P., and C.A. Quiroga, 1988, “Dimensionless Analytical Solutions for Dam-Breach Erosion,” _Journal of Hydraulic Research_ , vol. 26, no. 2, p. 179-197. 

- Singh, V.P., and P.D. Scarlatos, 1988, “Analysis of Gradual Earth-Dam Failure,” _Journal of Hydraulic Engineering_ , vol. 114, no. 1, p. 21-42. 

- Singh, V.P., 1996, _Dam Breach Modeling Technology_ , Kluwer Academic Publishers, Boston, Massachusetts. 

- Soil Conservation Service, 1947 (revised 1954), _Handbook of Channel Design for Soil and Water Conservation_ , USDA, SCS-TP-61. 

- Soil Conservation Service, 1973, _A Guide for Design and Layout of Earth Emergency Spillways as Part of Emergency Spillway Systems for Earth Dams_ , USDA, SCS-TR-52. 

- Soil Conservation Service, 1981, _Simplified Dam-Breach Routing Procedure_ , Technical Release No. 66 (Rev. 1), December 1981, 39 p. 

- Smart, Graeme M., 1984, “Sediment Transport Formula for Steep Channels,” _Journal of Hydraulic Engineering_ , vol. 110, no. 3, March 1984, p. 267-276. 

- Song, Charles C.S., Yifan Zheng, and Chih Ted Yang, 1995, “Modeling of River Morphologic Changes,” _International Journal of Sediment Research_ , vol. 10, no. 2, August 1995, 20 p. 

- Stein, O.R., and P.Y. Julien, 1993, “Criterion Delineating the Mode of Headcut Migration,” _Journal of Hydraulic Engineering_ , vol. 119, no. 1, January 1993, p. 37-50. 

- Stern, Gerald M., 1976, _The Buffalo Creek Disaster_ , Vintage Books, New York. 

- Susilo, Ken J., Phillip R. Mineart, and Thomas C. MacDonald, 1997, “Considerations When Selecting Parameters for Dam Breach Analyses,” _Dam Safety ’97_ , Proceedings of the 1997 ASDSO Conference (CD-ROM), Pittsburgh, Pennsylvania, September 7-10, 1997. 

- Temple, Darrel M., 1987, “Vegetal Protection of Embankments and Spillways,” _Hydraulic Engineering_ , Proceedings of the 1987 ASCE National Conference on Hydraulic Engineering, Williamsburg, Virginia, August 3-7, 1987, p. 745-750. 

- Temple, Darrel M., 1989, “Mechanics of an Earth Spillway Failure,” _Transactions of the ASAE_ , vol. 32, no. 6, November-December 1989, p. 2015-2021. 

- Temple, Darrel M., 1992, “Estimating Flood Damage to Vegetated Deep Soil Spillways,” _Applied Engineering in Agriculture_ , vol. 8, no. 2, March 1992, American Society of Agricultural Engineers, p. 237-242. 

- Temple, D.M., K.M. Robinson, R.M. Ahring, and A.G. Davis, 1987, _Stability Design of Grass-Lined Open Channels_ , USDA Agriculture Handbook No. 667, 167 p. 

- Temple, D.M., and G.J. Hanson, 1994, “Headcut Development in Vegetated Earth Spillways,” _Applied Engineering in Agriculture_ , vol. 10, no. 5, 1994, American Society of Agricultural Engineers, p. 677-682. 

- Temple, Darrel M., and John S. Moore, 1994, “Headcut Advance Prediction for Earth Spillways,” presented at the _1994 ASAE International Winter Meeting_ , Paper No. 94-2540, Atlanta, Georgia, December 13-16, 1994, 19 p. 

49 

- Temple, Darrel M., H.H. Richardson, J.A. Brevard, and G.J. Hanson, 1994, “The New DAMS2,” presented at the _1994 ASAE International Winter Meeting_ , Paper No. 94-2544, Atlanta, Georgia, December 13-16, 1994, 7 p. 

- U.S. Bureau of Reclamation, 1982, _Guidelines for Defining Inundated Areas Downstream from Bureau of Reclamation Dams_ , Reclamation Planning Instruction No. 82-11, June 15, 1982. 

- U.S. Bureau of Reclamation, 1988, _Downstream Hazard Classification Guidelines_ , ACER Technical Memorandum No. 11, Assistant Commissioner-Engineering and Research, Denver, Colorado, December 1988, 57 p. 

- Von Thun, J. Lawrence, and David R. Gillette, 1990, _Guidance on Breach Parameters_ , unpublished internal document, U.S. Bureau of Reclamation, Denver, Colorado, March 13, 1990, 17 p. 

- Wahl, Kenneth L., Kevin C. Vining, and Gregg J. Wiche, 1993, _Precipitation in the Upper Mississippi River Basin, January 1 through July 31, 1993_ , U.S. Geological Survey Circular 1120-B, 13 p. 

- Wahl, Tony L., 1997, "Predicting Embankment Dam Breach Parameters - A Needs Assessment," _Proceedings_ , 27th IAHR Congress, San Francisco, California, August 10-15, 1997. 

- Walder, Joseph S., and Jim E. O’Connor, 1997, “Methods for Predicting Peak Discharge of Floods Caused by Failure of Natural and Constructed Earth Dams,” _Water Resources Research_ , vol. 33, no. 10, October 1997, 12 p. 

- Webby, M. Grant, 1996, discussion of “Peak Outflow from Breached Embankment Dam” (Froehlich, 1995a), _Journal of Water Resources Planning and Management_ , vol. 122, no. 4, p. 316-317. 

- Westphal, Jerome A., and David B. Thompson, 1987, “NWS Dambreak or NWS Simplified Dam Breach?” _Computational Hydrology ‘87_ , Proceedings of the First International Conference, Anaheim, California, July 1987, p. H17-H23. 

- Westrich, B., R. Scharf, and V. Schürlein, 1997, “Measurement of Cohesive Sediment Erodibility in a Laboratory Flume,” _Proceedings_ , 27th IAHR Congress, San Francisco, California, August 1015, 1997, 6 p. 

- Wetmore, J.N., and D.L. Fread, 1983, _The NWS Simplified Dam-Break Model Executive Brief_ , National Weather Service, Office of Hydrology, Silver Spring, Maryland. 

- Wittler, Rodney J., 1994, _Mechanics of Riprap in Overtopping Flow_ , dissertation submitted to Colorado State University in partial fulfillment of the requirements for the degree of Doctor of Philosophy, Fort Collins, Colorado, Fall 1994. 

- Woosley, Dallon Thomas, 1994, “The Great Floods of 1994,” _Dam Safety ‘94_ , Proceedings of the 1994 ASDSO Conference, Boston, Massachusetts, September 11-14, 1994, p. 31-33. 

- Wurbs, Ralph A., 1987, "Dam-Breach Flood Wave Models," _Journal of Hydraulic Engineering_ , vol. 113, no. 1, p. 29-46. 

- Yang, C.T., 1972, “Unit Stream Power and Sediment Transport,” _Journal of the Hydraulics Division_ , ASCE, vol. 98, no. HY10, October 1972, p. 1805-1826. 

- Yang, C.T., 1973, “Incipient Motion and Sediment Transport,” _Journal of the Hydraulics Division_ , ASCE, vol. 99, no. HY10, October 1973, p. 1679-1704. 

- Yang, C.T., 1984, “Unit Stream Power Equation for Gravel,” _Journal of Hydraulic Engineering_ , vol. 110, no. 12, December 1984, p. 1783-1797. 

- Yang, C.T., 1996, “Generalized Stream Tube Model for Alluvial River Simulation (GSTARS-2),” _Proceedings, Sixth Federal Interagency Sedimentation Conference_ , Las Vegas, Nevada, March 10-14, 1996, 5 p. 

- Yang, C.T. and C.C.S. Song, 1979, “Theory of Minimum Rate of Energy Dissipation,” _Journal of the Hydraulics Division_ , ASCE, vol. 105, no. HY7, July 1979. 

50 

- Yang, Chih Ted, and Albert Molinas, 1982, “Sediment Transport and Unit Stream Power Function,” _Journal of the Hydraulics Division_ , ASCE, vol. 108, no. HY6, June 1982, p. 774-793. 

- Yang, Chih Ted, Albert Molinas, and Charles C.S. Song, 1988, “GSTARS - Generalized Stream Tube Model for Alluvial River Simulation,” _Twelve Selected Stream Sedimentation Models Developed in the United States_ , U.S. Interagency Advisory Committee on Water Data, Subcommittee on Sedimentation, published by the Federal Energy Regulatory Commission, December 31, 1988. 

51 

## **NOTATION** 

β Particle packing factor, ratio of roughness height to roughness spacing _B_ Breach width (general) _B_ Average breach width ( _Btop_ + _Bbottom_ ) / 2 * _B_ Dimensionless average breach width ( _B_ / _hb_ ) _Btop_ Breach width at top of breach _Bbottom_ Breach width at bottom of breach _Bavg_ Average breach width _Cb_ Constant in Von Thun and Gillette breach width relation _c_ Coefficient in equation for λ , dependent on aeration and particle packing factors δ Angle of repose _d_ Drop in reservoir level through a breach (Walder and O’Connor, 1997) _dm_ Mean roughness height _dovtop_ Depth of overtopping flow at failure _ds_ Equivalent stone diameter _Dc_ Height of dam crest relative to dam base (Walder and O’Connor, 1997) ε! Erosion rate, mass/time _EL_ Lateral erosion rate, distance/time _f_ Darcy’s friction factor _g_ Acceleration of gravity γ _s_ Unit weight of solid material γ _w_ Unit weight of water η Dimensionless parameter relating breach erosion rate and reservoir size (Walder and O’Connor, 1997) _hb_ Height of breach _hd_ Height of dam _hw_ Hydraulic depth of water at dam at failure, above breach bottom _hw*_ Dimensionless height of water above breach bottom, ( _hw/hb_ ) _Ja_ Joint alteration number _Jn_ Joint set number _Jr_ Joint roughness number _Js_ Relative ground structure number _Kc_ Core wall correction factor (0.6 if dam contains a core wall; 1.0 otherwise) _k_ Mean vertical erosion rate of breach (Walder and O’Connor, 1997) _kd_ Erosion detachment rate coefficient 

- _Kh_ Headcut erodibility index _Ko_ Overtopping correction factor (1.4 if failure mode is overtopping; 1.0 otherwise) 

- λ Surface flow resistance factor (analogous to Darcy’s _f_ ) _Ms_ Earth mass strength number _Qp_ Peak breach outflow _Qp*_ Dimensionless peak breach outflow, _Qp_ / _g_<sup>1/2</sup> _d_<sup>5/2</sup> , (Walder and O’Connor, 1997) _RQD_ Rock quality designation σ Aeration factor, specific weight of air-water mixture divided by specific 

52 

weight of pure water _S_ Storage _S_<sup>_*_</sup> Dimensionless storage, ( _S/hb_<sup>3</sup> ) Τ Shields parameter τ _c_ Critical shear stress τ _e_ Erosionally effective stress _tf_ Breach formation time, hours _* tf_ Dimensionless breach formation time, _t f_ / _ghb_ ( _tf, g,_ and _hb_ must be in units that produce a dimensionless _tf_<sup>_*_</sup> .) θ Downstream embankment slope angle _v_ Flow velocity down embankment slope _vc_ Critical velocity to dislodge riprap particles _Ver_ Volume of embankment material eroded _V_ 0 _, Vout_ Volume of water discharged through breach (initial storage + inflow during failure) _Vw_ Volume of water above breach invert elevation at time of breach _W_ * Dimensionless average embankment width ( _Wcrest+Wbottom_ )/(2 _hb_ ) _ym_ Mean water depth normal to embankment slope _Z_ Breach opening side slope factor ( _Z_ horizontal:1 vertical) _Ze/u_ Upstream embankment face slope factor _Ze/d_ Downstream embankment face slope factor 

53 

54 

#### **_APPENDIX: DAM FAILURES CASE STUDY DATABASE_** 

55 

_Table A1. – Dam failures case study database.  Footnotes and reference keys are given in Table A2._ 

||||||||EMBANKMENT|DIMENSIONS||BREACH OUTFLOW|
|---|---|---|---|---|---|---|---|---|---|---|
||||||Dam<br>Height<br>_h_d|Crest<br>Width<br>_W_c|Base<br>Width<br>Average<br>Width<br>_W_b<br>_W_|Upstream<br>Slope<br>_Z_e/u|Downstream<br>Slope<br>Length<br>_Z_e/d<br>_L_|Peak<br>Outflow<br>Method of Determining Peak Outflow<br>_Q_p<br>|
|Dam and Location|Built|Failed<br>Failure Mode|Construction|References|m|m|m<br>m|_Z_:1(h:v)|_Z_:1(h:v)<br>m|m<sup>3</sup>/s|
|1 Apishapa, Colorado<br>|1920<br>|1923<br>Piping<br> <br>|Homogeneous earthfill, fine sand<br>|fghijkq<br>|34.14<br>|4.88<br>|160.<br>82.4<br> <br>|3.<br>|2.<br> <br>|6,850.15-min reservoir drawdown<br>|
|2 Baldwin Hills, California|1951|1963<br>Piping|Homogeneous earthfill|efghijkq|71.|19.2|100.<br>59.6|2.|1.8<br>198.|1,130.15-min reservoir drawdown|
|3 Bearwallow Lake, North Carolina|1963|1976<br>Sliding|Homogeneous earthfill|ik||3.1|14.||||
|4 Bradfield, England|1863|1864<br>Piping|Rockfill/earthfill|dh|28.96||50.||382.|1,150.unknown|
|5 Break Neck Run,USA|1877|1902||h|7.0||86.|||9.2unknown|
|6 Buckhaven No. 2, Tennessee||Overtopping||k|||37.||||
|7 Buffalo Creek, West Virginia|1972|1972<br>Seepage|Homogeneous fill, coal waste|fghq|14.02|128.|128.|1.6|1.3|1,420.slope-area measurement|
|8 Bullock Draw Dike, Utah|1971|1971<br>Piping|Homogeneous earthfill|fhik|5.79|4.3|18.6|2.|3.||
|9 Butler, Arizona||1982<br>Overtopping|Homogeneous earthfill|jk|||9.63|||810.slope-area 600 m downstream|
|10 Canyon Lake,USA|1938|1972<br>Overtopping||dh|6.1||||152.||
|11 Castlewood, Colorado|1890|1933<br>Overtopping|Earth/rockfill with masonry wall|fgijkq|21.34|4.9|47.4|3.|1.|3,570.15-min reservoir drawdown|
|12 Caulk Lake, Kentucky||Piping or Sliding||k|||32.0||||
|13 Cheaha Creek, USA|1970|1970<br>Overtopping|Zoned earthfill|fh|7.01|4.3||3.|2.5||
|14 Clearwater Lake Dam, Georgia<br>|1965<br>|1994<br>Overtopping<br> <br>|Homogeneous earthfill<br>|m<br>|||15.0||||
|15 Coedty,England|1924|1925<br>Overtopping|Earthfill with corewall|dhik|10.97|3.1|||262.||
|16 Cougar Creek, Alberta||Overtopping||k|||21.7||||
|17 Davis Reservoir, California|1914|1914<br>Piping|Earth with concrete facing|fg|11.89|6.1||2.|2.|510.unknown|
|18 DMAD, Utah||1983|Earthfill|g|8.8|||||793.drawdown rate|
|19 East Fork Pond River, Kentucky<br>||Piping<br> <br>||k<br>|||38.9<br>||||
|20 Elk City,Oklahoma|1925|1936<br>Overtopping|Rolled sandyclayfill with concrete corewall|dhik|9.14|4.9|50.4|3.|2.<br>564.||
|21 Emery, California||Piping||k|||22.2||||
|22 Erindale, Canada|1910|1912<br>Overtopping|Earthfill with concrete masonry corewall|dh|10.67||||213.||
|23 Euclides de Cunha, Brazil|1958|1977<br>Overtopping|<br>Earthfill|fh|53.04|||||1,020.unknown|
|24 Fogelman, Tennessee<br>||Piping<br> <br>||k<br>|||21.3||||
|25 Frankfurt,Germany|1975|1977<br>Piping|Earthfill|fh|9.75|||||79.unknown|
|26 Fred Burr, Montana||1948<br>Piping|Homogeneous earthfill|gjq|10.4||30.8|||654.slope-area "short distance downstream"|
|27 French Landing, Michigan<br>|1925<br>|1925<br>Piping<br> <br>|Homogeneous earthfill<br>|fghijk<br>|12.19<br>|2.4<br>|34.3<br>|2.<br>|2.5<br>|929.1-hr reservoir drawdown<br>|
|28 Frenchman Creek, Montana|1952|1952<br>Piping|Homogeneous earthfill|fghijk|12.5|6.1|37.3|3.|2.|1,420.unknown|
|29 Frias, Argentina|1940|1970<br>Overtopping|Homogeneous rockfill|dh||||1.|1.<br>62.2||
|30 Goose Creek,South Carolina|1903|1916<br>Overtopping|Earthfill|fgh|6.1|3.0||1.5|1.5|565.unknown|
|31 Grand Rapids, USA|1874|1900<br>Overtopping|Earthfill with clay corewall|dhk|7.62|3.7|14.8|1.5|1.5<br>441.||
|32 Granite Creek Alaska||1971||c||||||1841.discharge 8 km downstream, unknown method|
|,<br>33 Haas Pond, Connecticut<br>34 Ht Mihi|1920|<br>Piping<br>1986<br>Pii|H thfill|k<br>ik||43|16.7<br>311|||,|
|ar, cgan||<br>png|omogeneous ear|||.|.||||
|35 Hatchtown,Utah|1908|1914<br>Pipingor foundation d|efect<br>Zoned earthfill|dfghijkq|19.2|6.1|44.8|2.|2.5<br>238.|3,080.1-hr reservoir drawdown|
|36 Hatfield, USA|1908|1911||h|6.8|||||3,400.unknown|
|37 Hebron, USA|1913|1914<br>Piping|Earthfill|fh|11.58|3.7||3.|1.5||
|38 Hell Hole, California|1964|1964<br>Piping|Rockfill|fgijkq|67.06|21.3|103.2|1.5|1.5|7,360.1-hr reservoir drawdown|
|39 Herrin, Illinois||1935<br>Overtopping|Zoned earthfill|ik||4.6|28.8||||
|40 Horse Creek,Colorado<br>|1911<br>|1914<br>Piping<br> <br>|Homogeneous earthfill,with concrete facing<br>|dfik|12.19|4.9|26.8<br>|1.5|2.<br>701.||
|41 Hutchinson Lake Dam, Georgia|1960|1994<br>Overtopping|Homogeneous earthfill|m|||14.0||||
|42 Iowa Beef Processors Washington|1971|1993<br>Piping|Earthfill|kr|457||||305||
|,<br>43 Ireland No. 5, Colorado||<br><br>1984<br>Piping|Homogeneous earthfill|ijk|.|2.4|18.0||.|110.slope-area "short distance downstream "|
|44 Jacobs Creek, Pennsylvania||Piping||k|||||||
|45 Johnston City,Illinois<br>46 Johnstown (South Fork Dam, Penn.)|1921<br>1853|1981<br>Piping<br>1889<br>Overtopping|Homogeneous earthfill<br>Zoned earth and rockfill|fhik<br>dfgijkq|4.27<br>38.1|1.8<br>3.05|21.5<br>64.|4.75<br>2.|2.75<br>1.5<br>284.|8,500.30-min reservoir drawdown|
|<br>47 Kaddam, India|1957|1958<br>Overtopping|Earthfill|abdhp|12.5||||||
|48 Kelly Barnes, Georgia<br>|1948<br>|1977<br>Piping<br> <br>|Homogeneous earthfill<br>|fghijkq<br>|11.58<br>|6.1|19.4|1.|1.<br>|680.slope-area 250 m downstream|
|49 Kendall Lake Dam, South Carolina<br>50 Kraftsmen's Lake Dam,Georgia<br>|1900<br>|1990<br>Overtopping<br>1994<br>Overtopping<br> <br>|Earthfill<br>Homogeneous earthfill<br>|n<br>m<br>|5.49||8.10<br>||128.||
|51 La Fruta, Texas|1930|1930<br>Piping|Homogeneous earthfill|ik||4.9|40.0||||
|<br>52 Lake Avalon, New Mexico<br>53 Lake Barcroft USA|1894<br>1913|1904<br>Piping<br>1972<br>Overtopping|<br>Earthfill<br>Earthfill|hk<br>dh|14.5<br>2103||42.7|||2,320.unknown|
|,<br>54 Lake Frances, California|<br>1899|<br><br>1899<br>Piping|Homogeneous earthfill|fhik|.<br>15.24|4.9|47.4|3.|2.||



_Table A1. – Dam failures case study database.  Footnotes and reference keys are given in Table A2._ 

||||||Dam<br>Height<br>_h_d|Crest<br>Width<br>B<br>W<br>_W_c<br>|EMBANKMENT<br>ase<br>idth<br>Average<br>Width<br>_W_b<br>_W_|DIMENSIONS<br>Upstream<br>Slope<br>_Z_e/u|<br>Downstream<br>Slope<br>Length<br>_Z_e/d<br>_L_|BREACH OUTFLOW<br>Peak<br>Outflow<br>Method of Determining Peak Outflow<br>_Q_p|
|---|---|---|---|---|---|---|---|---|---|---|
|Dam and Location|Built|Failed<br>Failure Mode|Construction|Referenc|es<br>m|m|m<br>m|_Z_:1(h:v)|_Z_:1(h:v)<br>m|m<sup>3</sup>/s|
|55 Lake Genevieve, Kentucky<br>||Piping<br> <br>|Earthfill<br>|k<br>|||19.8<br>||||
|56 Lake Latonka, Pennsylvania|1966|1966<br>Piping|Homogeneous earthfill|hik|13.0|6.1|28.0|||290.unknown|
|57 Lake Philema Dam Georgia|1965|1994<br>Overtopping|Homogeneous earthfill|m|||28.||||
|,<br>58 Lambert Lake, Tennessee||<br><br>Piping|<br>Earthfill|k|||53.9||||
|<br>59 Laurel Run,Pennsylvania||1977<br>Overtopping|Earthfill|fghijkq|12.8|6.1|40.5|||1,050.slope-area 1.6 km downstream|
|60 Lawn Lake, Colorado|1903|1982<br>Piping|Homogeneous earthfill|gikq|7.9|2.4|14.2|||510.dam-break model|
|61 Lily Lake, Colorado|1913|1951<br>Piping|Homogeneous earthfill|ijk||||||71.slope-area at unknown location|
|62 Little Deer Creek, Utah|1962|1963<br>Piping|Homogeneous earthfill|fghijkq|26.21|6.1|63.1|||1,330.slope-area at unknown location|
|63 Long Branch Canyon, California||Piping||k|||11.3||||
|<br>64 Lower Latham,Colorado||1973<br>Piping|Homogeneous earthfill|ijkp||4.6|25.7|||340.slope-area at unknown location|
|65 Lower Otay California|1897|1916<br>Overtopping|Rockfill with concrete/steel corewall|dfik|41.15|3.7|53.3|1.|1.<br>172.||
|,<br>66 Lower Two Medicine, Montana|<br>1913|<br><br>1964<br>Piping|<br>Homogeneous earthfill|fghijkq|<br>11.28|<br>3.7||||<br>1,800.slope-area 4 km downstream|
|67 Lyman, Arizona|1913|1915<br>Piping|Zoned earthfill|fhi|19.81|3.7||2.|2.||
|68 Lynde Brook, Massachusetts|1871|1876<br>Piping|Earthfill with corewall|fik|12.5|15.2|41.8|2.|2.3||
|69 Machhu II,India||1979<br>Seepage|Earthfill|dhp|60.05|6.0||3.|2.<br>4180.||
|70 Mammoth, USA<br>|1916|1917<br>Seepage<br> <br>||h|21.3|||||2,520.unknown<br>|
|71 Martin Cooling Pond Dike, Florida||1979<br>Foundation Defect||pq||||||3,115.unknown|
|72 Melville, Utah|1907|1909<br>Piping|Zoned earthfill|fhik|10.97|3.0|25.1|3.|1.5||
|73 Merimac (Upper) Lake Dam, Georgia|1939|1994<br>Overtopping|Homogeneous earthfill|m|||17.5||||
|<br>74 Mill River,Massachusetts||1874|<br>Earth and masonry|g|13.1|||||1,645.unknown|
|75 Mossy Lake Dam, Georgia|1963|1994<br>Overtopping|Homogeneous earthfill|m|||14.3||||
|76 Nanaksagar, India|1962|1967||hp|15.85|||||9,700.unknown|
|77 Nahzille, New Mexico||1996<br>Overtopping|Homogeneous earthfill|o|5.49|||3.|2.<br>130.||
|78 North Branch Tributary Pennsylvania||1977|Earthfill|fgh|5.5|||||29.4slope-area measurement|
|,<br>79 Oakford Park,USA||<br>1903<br>Overtopping|Earthfill with corewall|dh|<br>6.1|2.6|||107.|<br>|
|80 Oros, Brazil<br>|1960|1960<br>Overtopping<br>|Zoned earthfill and rockfill<br>|fghijkpq<br>|35.36|5.0|110.<br>|||9,630.unknown|
|81 Otter Lake, Tennessee||Piping|Earthfill|k|||20.6||||
|82 Otto Run, USA||1977|Earthfill|fgh|5.8|||||60.slope-area measurement|
|83 Pierce Reservoir Wyoming||1986<br>Piping|Homogeneous earthfill|ik||3.1|||||
|,<br>84 Potato Hill Lake,North Carolina|1947|<br><br>1977<br>Overtopping|<br>Homogeneous earthfill|ik||<br>7.3|23.5||||
|85 Prospect, Colorado<br>|1914|1980<br>Piping<br>|Homogeneous earthfill<br>|ijk<br>||4.3|13.1|||116.reservoir drawdown, unknown time period|
|86 Puddingstone, California|1926|1926<br>Overtopping|Homogeneous earthfill|ijk||||||480.15-min reservoir drawdown|
|<br>87 Quail Creek, Utah|1986|1989<br>Piping|<br>Homogeneous earthfill|jk|||56.6|||3,110.15-min reservoir drawdown|
|88 Rainbow Lake, Michigan||1986<br>Overtopping|Homogeneous earthfill|ik||11.3|28.2||||
|<br>89 Renegade Resort Lake,Tennessee||Overtopping||k|||11.0||||
|90 Rito Manzanares, New Mexico||1975<br>Piping|Homogeneous earthfill|fhik|7.32|3.7|13.3|1.34|1.34||
|91 Salles Oliveira, Brazil|1966|1977<br>Overtopping|Earthfill|fh|35.05|||||7,200.unknown|
|<br>92 Sandy Run, Pennsylvania||1977<br>Overtopping|Earthfill|fhq|8.53|||||<br>435.unknown<br>l- 13 k dt ti  tfl di|
|93 Schaeffer, Colorado||1921<br>Overtopping|Earthfill with concrete corewall|dfghikq|30.5|4.6|80.8|3.|2.<br>335.|<br>4,500.<br>sopearea  m ownsream; wce avg ouow urng<br>1/2 hr required to drain reservoir|
|94 Scott Farm Dam No. 2,Alberta||Piping||k|||39.3||||
|95 Sheep Creek, USA|1969|1970<br>Seepage|Earthfill|fh|17.07|6.1||3.|2.||
|<br>96 Sherburne, USA|1892|1905<br>Seepage|Earthfill with corewall|dh|10.36||||91.4|<br>960.unknown|
|97 Sinker Creek, USA<br>|1910|1943<br>Seepage<br>|Earthfill<br>|fh<br>|21.34<br>||||||
|98 South Fork Tributary, Pennsylvania||1977|Earthfill|fgh|1.8|||||122.slope-area measurement|
|<br>99 SpringLake,Rhode Island|1887|1889<br>Piping|Homogeneous earthfill,clayandgravel|fhi|5.49|2.4||0.75|0.75||
|100 Statham Lake Dam, Georgia|1955|1994<br>Overtopping|Homogeneous earthfill|m|||12.6||||
|<br>101 Swift, Montana|1914|1964<br>Overtopping|<br>Rockfill with concrete facing|dfgq|57.61||||226.|<br>24,947.slope-area 27 km downstream|
|102 Teton, Idaho<br>|1975|1976<br>Piping<br>|Zoned earthfill|fghijkq<br>|92.96|10.7|250.<br>|3.|2.5|65,120.slope-area 4 km downstream|
|103 Trial Lake, Utah||Piping||k|||7.62||||
|<br>104 Trout Lake,North Carolina||Overtopping||k|||21.6||||
|105 Upper Pond, Connecticut||Overtopping||k|||||||
|<br>106 Wheatland No. 1, Wyoming<br>107 Wilkinson Lake Dam Georia|1893<br>1956|1969<br>Piping<br>1994<br>Piin|Homogeneous earthfill<br>Homoeneous earthfill with corewall|fhik<br>m|13.6|6.1|132||||
|, g<br>108 Winston, North Carolina|<br>1904|<br>pg<br>1912<br>Overtopping|g<br>Earthfill with corewall; earth with rubble cor|e<br>dfik|7.32|2.1|.<br>7.76|1.|1.<br>133.||



_Table A1. – Dam failures case study database [continued]._ 

|||HYD|RAULIC CHARACTERI|STICS||||BREACH|CHARAC|TERISTIC|S<br>||TIME P|ARAMETERS<br>Mi||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||Reservoir<br>Storage<br>_S_<br>|Surface Area<br>V<br>_A_<br>|olume Stored Above<br>Breach Invert<br>D<br>_V_w<br>|epth Above<br>Breach<br>B<br>_h_w|reach Formation<br>Factor<br>_V_w_h_w<br><br>|Breach|Height<br>_h_b|Top<br>Width<br>_B_top|Bottom<br>Width<br>_B_bottom|Average<br>Width<br>_B_|Average<br>Side<br>Slopes<br>_Z_|Eroded<br>Volume<br>_V_er<br>|Formation<br>Time<sup>1</sup><br>Failure<br>Time<sup>2</sup><br> <br>_t_f<br>_t_f|axmum<br>Development<br>Time<sup>3</sup><br>_t_f|Breach and<br>Empty Time<sup>4</sup><br>_t_f|
|Dam and Location|m<sup>3</sup>|m<sup>2</sup>|m<sup>3</sup>|m|m<sup>4</sup>|Shape|m|m|m|m|_Z_:1(h:v)|m<sup>3</sup>|hr<br>hr|hr|hr|
|1 Apishapa, Colorado<br>|22,500,000<br>|2,590,000<br>|22,200,000<br>|28.0<br>|622,000,000 tr<br>|apezoid<br>|31.1<br>|91.5|81.5|93.0<br>|0.44<br>|238,000<br>|0.75<br>2.5<br> <br>|2.5<br>||
|2 Baldwin Hills, California|1,100,000|76,900|910,000|12.2|11,100,000 tr|iangular|21.3|||25.0|0.31|31,700|0.33<br>1.3|1.3||
|3 Bearwallow Lake, North Carolina<br>|||49,300|5.79|285,000||6.40|||12.2|1.43|1,090||||
|4 Bradfield, England|3,200,000||||||||||||<0.5||0.75|
|<br>5 Break Neck Run,USA|49,000||||||7.|||30.5|||3.|||
|6 Buckhaven No. 2, Tennessee|||24,700|6.10|151,000||6.10|||4.72|0.73|1,070||||
|<br>7 Buffalo Creek, West Virginia|484,000|52,600|<br>484,000|14.02|<br>6,780,000 tr|apezoid|14.|153.|97.|125.|2.|<br>319,000|0.5|0.5||
|8 Bullock Draw Dike, Utah|1,130,000||740,000|3.05|2,260,000 tr|apezoid|5.79|13.6|11.0|12.5|0.21|1,350||||
|9 Butler, Arizona|||2,380,000|7.16|17,000,000||7.16|||62.5|0.85|4,310||||
|<br>10 Canyon Lake,USA|985,000||||||||||||0.1|||
|11 Castlewood, Colorado|4,230,000|809,000|6,170,000|21.6|133,000,000 tr|apezoid|21.3|54.9|33.5|44.2|0.50|55,700|0.5|0.33||
|12 Caulk Lake, Kentucky|||698,000|11.1|7,750,000||12.2|||35.1|1.38|13,700||||
|13 Cheaha Creek, USA|69,000|||||||||||15,500|5.5|5.5||
|14 Clearwater Lake Dam, Georgia|||466,000|4.05|1,890,000||3.78|||22.8|1.03|1,290||||
|15 Coedty,England|310,000||311,000|>11.0|3,420,000||11.0|67.|18.2|42.7|2.22||0.25<br>short||short|
|16 Cougar Creek, Alberta|||29,800|11.1|331,000||10.4|||||||||
|17 Davis Reservoir, California|58,000,000|12,900,000|58,000,000|11.58|671,000,000 tr|apezoid|11.9|21.3|||0.25|6,470||7.||
|18 DMAD, Utah|19,700,000||19,700,000|||||||||||||
|19 East Fork Pond River, Kentucky|||1,870,000|9.80|18,300,000||11.4|||17.2|0.44|7,630||||
|20 Elk City,Oklahoma|740,000||1,180,000|9.44|11,100,000||9.14|45.5|27.7|36.6|1.00|16,900||||
|21 Emery, California|||425,000|6.55|2,780,000||8.23|||10.8|0.35|1,970||||
|22 Erindale, Canada|||||||4.6|39.5|||||<0.5|||
|<br>23 Euclides de Cunha, Brazil|13,600,000|||58.22|tr|apezoid|53.|131.||||726,000|7.3|7.3||
|24 Fogelman, Tennessee<br>|||493,000<br>|11.1<br>|5,470,000<br>||12.6<br>|||7.62<br>|0.36<br>|2,050<br>||||
|25 Frankfurt,Germany|350,000||352,000|8.23|2,890,000 tr|apezoid|9.75|9.2|4.6|6.9|0.4|1,290|2.5|0.25||
|26 Fred Burr, Montana|752,000||750,000|10.2|7,650,000||10.4|||||||||
|27 French Landing, Michigan|||3,870,000|8.53|33,000,000 tr|apezoid|14.2|41.|13.8|27.4|0.97|13,800|0.58<br>0.58|0.58||
|<br>28 Frenchman Creek, Montana|21,000,000||16,000,000|10.8|<br>173,000,000 tr|<br>apezoid|12.5|67.|54.4|54.6|0.50|28,400||||
|29 Frias, Argentina|||||||15.|62.|||||0.25|||
|30 Goose Creek,South Carolina|10,600,000||10,600,000|1.37|14,500,000 tr|apezoid|4.1|30.5|22.3|26.4|0.5|1,070|<0.5|0.5||
|31 Grand Rapids, USA|220,000||25,500|6.40|163,000||6.40|12.2|6.0|19.0|2.26|1,800|0.5||short|
|32 Granite Creek Alaska||||||||||||||||
|,<br>33 Haas Pond, Connecticut|||23,400|2.99|70,000||3.96|||10.7|0.38|708||||
|34 Hart, Michigan|||6,350,000|10.7|67,900,000||10.8|||73.9|3.03|24,800||||
|35 Hatchtown,Utah|14,800,000||14,800,000|16.8|249,000,000 tr|apezoid|18.3|180.|140.|151.|2.42|161,000|1.0<br>3.|3.|1.|
|36 Hatfield, USA|12,300,000||||||6.8||6.1|91.5||||||
|37 Hebron, USA<br>||||12.19|tr|apezoid|15.3|61.|30.4|45.7|0.5|30,800|2.25|2.25||
|38 Hell Hole, California|30,600,000||30,600,000|35.1|1,070,000,000 tr|apezoid|56.4|||121.0|0.96|555,000|0.75|5.||
|39 Herrin, Illinois||||>10.7|||10.7|||47.2|1.14|14,500||||
|40 Horse Creek,Colorado<br>|21,000,000|4,860,000|12,800,000<br>|7.01<br>|89,700,000 tr<br>|apezoid|12.8<br>|76.2|70.|73.1<br>|0.83<br>|20,500<br>||||
|41 Hutchinson Lake Dam, Georgia|||1,170,000|4.42|5,170,000||3.75|||33.4|1.14|1,750||||
|42 Iowa Beef Processors Washinton|333000|150000|333000|442|1470000||457|||168|033|||||
|, g<br>43 Ireland No. 5, Colorado<br>|,|,|,<br>160,000<br>|.<br>3.81<br>|,,<br>610,000<br>||.<br>5.18<br>|||.<br>13.5<br>|.<br>0.38<br>|1,260|0.5|||
|44 Jacobs Creek, Pennsylvania<br>45 Johnston CityIllinois|575000||423,000<br>575000|20.1<br>3.05|8,500,000<br>1750000 tr|apezoid|21.3<br>5.18|13.4|2.|17.5<br>8.23|0.61<br>1.00|673||||
|, <br>46 Johnstown (South Fork Dam, Penn.)|, <br>18,900,000|1,650,000|, <br>18,900,000|<br>24.6|,, <br>465,000,000 tr|<br>apezoid|<br>24.4|<br>128.|61.|<br>94.5|<br>1.38|<br>68,800|0.75|3.5|3.5|
|<br>47 Kaddam, India|214,000,000||||||15.2|30.||137.2|||1.|||
|48 Kelly Barnes, Georgia|505,000|170,000|777,000|11.3|8,780,000 tr|apezoid|12.8|35.|18.|27.3|0.85|9,940|0.5|||
|<br>49 Kendall Lake Dam, South Carolina|<br>728,000|<br>166,000||||||||||||||
|50 Kraftsmen's Lake DamGeorgia|||177000|366|648000||320|||145|148|376||||
|, <br>51 La Fruta, Texas|||, <br>78,900,000|.<br>7.90|, <br>623,000,000||.<br>14.0|||.<br>58.8|.<br>0.30|<br>32,900||||
|52 Lake Avalon, New Mexico<br>53 Lake Barcroft USA|7,750,000<br>3120000||31,500,000|13.7|432,000,000||14.6<br>11|23||130.|0.52|81,000|2.<br>>1||lon|
|,<br>54 Lake Frances, California|,,<br>865,000|174,000|789,000|14.0|11,000,000 tr|apezoid|.<br>17.1|.<br>30.|10.4|18.9|0.65|12,400|.<br>1.|1.|g|



_Table A1. – Dam failures case study database [continued]._ 

|||HYD|RAULIC CHARACTERI|STICS||||BREACH|CHARAC|TERISTIC|S<br>Average||TIME|PARAMETERS<br>Maximum||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||Reservoir|V|olume Stored Above<br>D|epth Above|Breach Formation|||Top|Bottom|Average|<br>Side|Eroded|Formation<br><br>Failure<br>|Development<br>|Breach and<br>|
||Storage<br> <br>_S_|Surface Area<br>_A_|Breach Invert<br>_V_w|Breach<br>_h_w|Factor<br>_V_w_h_w|Breach|Height<br>_h_b|Width<br>_B_top|Width<br>_B_bottom|Width<br>_B_|Slopes<br>_Z_|Volume<br>_V_er|Time<sup>1</sup><br>Time<sup>2</sup><br>_t_f<br>_t_f|Time<sup>3</sup><br>_t_f|Empty Time<sup>4</sup><br>_t_f|
|Dam and Location|m<sup>3</sup>|m<sup>2</sup>|m<sup>3</sup>|m|m<sup>4</sup>|<br>Shape|m|m|m|m|_Z_:1(h:v)|m<sup>3</sup>|hr<br>hr|hr|hr|
|55 Lake Genevieve, Kentucky<br>|||680,000<br>|6.71<br>|4,560,000<br>||7.92<br>|<br>||16.8<br>|1.54<br>|2,630<br>||||
|56 Lake Latonka, Pennsylvania<br>|1,590,000||4,090,000<br>|6.25<br>|25,600,000<br>||8.69<br>|<br>||39.2<br>|1.18<br>|9,540<br>|3.|||
|57 Lake Philema Dam, Georgia|||4,780,000|9.00|43,000,000||8.53|||47.2|0.33|11,300||||
|58 Lambert Lake, Tennessee|||296,000|12.8|3,790,000||14.3|||7.62|0.21|5,870||||
|59 Laurel Run,Pennsylvania|385,000||555,000|14.1|7,830,000||13.7|||35.1|2.40|19,500||||
|60 Lawn Lake, Colorado|||798,000|6.71|5,350,000||7.62|||22.2|0.96|2,400||||
|61 Lily Lake, Colorado|||92,500|3.35|310,000||3.66|||10.8|0.13|||||
|62 Little Deer Creek, Utah|1,730,000||1,360,000|22.9|31,100,000|trapezoid|27.1|<br>23.||29.6|0.75|50,600|0.33<br>0.33|0.33||
|63 Long Branch Canyon, California|||284,000|3.17|900,000||3.66|||9.14|0.4|378||||
|<br>64 Lower Latham,Colorado|7,080,000||7,080,000|5.79|41,000,000||7.01|||79.2|6.30|14,300|1.5|||
|65 Lower Otay, California|49,300,000||49,300,000|>39.6|1,950,000,000|trapezoid|39.6|<br>172.|93.8|133.0|1.00|107,000|1.0<br>0.25|0.33|2.5|
|66 Lower Two Medicine, Montana|19,600,000||29,600,000|11.3|334,000,000|trapezoid|11.3|||67.0|1.50|||||
|67 Lyman, Arizona|49,500,000||35,800,000|16.2|580,000,000|trapezoid|19.8|<br>107.|87.|97.|1.00|71,900||||
|68 Lynde Brook, Massachusetts|2,520,000|534,000|2,880,000|11.6|33,400,000|trapezoid|12.5|<br>45.7|<br>15.3|30.5|1.22|15,300||3.||
|69 Machhu II,India|110,000,000||||||60.|540.|||||2.0|||
|70 Mammoth USA|13600000||||||213|||92|||3|||
|,<br>71 Martin Cooling Pond Dike, Florida|,,<br>136,000,000||136,000,000|8.53|1,160,000,000||.|||.<br>186.|||.|||
|72 Melville, Utah|||24,700,000|7.92|196,000,000|trapezoid|9.75|<br>40.|25.6|32.8|0.70|10,600||||
|73 Merimac (Upper) Lake Dam, Georgia|||69,600|3.44|239,000||3.05|||14.2|0.41|758||||
|<br>74 Mill River,Massachusetts|2,500,000||<br>2,500,000|||||||||||||
|75 Mossy Lake Dam, Georgia<br>|||4,130,000|4.41|18,200,000||3.44<br>|||41.5<br>|1.24|2,040||||
|76 Nanaksagar, India|210,000,000||||||16.|||46.|||12.|||
|<br>77 Nhill N Mi||||||id|503|<br>671|<br>671|671|0|||||
|aze, ew exco<br>78 North Branch Tributary, Pennsylvania|||22,200|5.49|122,000|rapezo|.|<br>.|<br>.|.|.|||||
|<br>79 Oakford Park,USA|||||||4.6|<br>23.|||||1.|||
|80 Oros, Brazil|650,000,000||660,000,000|35.8|23,600,000,000|trapezoid|35.5|<br>200.|130.|165.0|1.00|765,000|8.5|||
|81 Otter Lake, Tennessee|||109,000|5.00|545,000||6.10|||9.30|1.28|1,170||||
|82 Otto Run, USA|||7,400|5.79|42,900|||||||||||
|83 Pierce Reservoir, Wyoming|||4,070,000|8.08|32,900,000||8.69|||30.5|0.77||1.0|||
|<br>84 Potato Hill Lake,North Carolina|||105,000|>7.77|816,000||7.77|||16.5|1.25|3,010||||
|85 Prospect, Colorado<br>|||3,540,000<br>|1.68<br>|5,950,000<br>||4.42<br>|<br>||88.4|0.69|5,120|2.5<br>|||
|86 Puddingstone, California|||617,000|>15.2|9,380,000||15.2||||||0.25|||
|<br>87 Quail Creek, Utah|||30,800,000|16.7|514,000,000||21.3|||70.0|0.10|84,400|1.0|||
|88 Rainbow Lake, Michigan|||6,780,000|10.0|67,800,000||9.54|||38.9|2.52|10,500||||
|<br>89 Renegade Resort Lake,Tennessee|||<br>13,900|3.66|<br>50,900||3.66|||2.29|0.63|<br>92||||
|90 Rito Manzanares, New Mexico|24,700||24,700|4.57|113,000|trapezoid|7.32|<br>19.|7.6|13.3|0.77|1,290||||
|91 Salles Oliveira, Brazil|25,900,000||71,500,000|38.4|2,750,000,000|trapezoid|35.|||168.||440,000|2.|2.||
|92 Sandy Run, Pennsylvania|56,800||56,700|8.53|484,000|||||||||||
|93 Schaeffer, Colorado|3,920,000||4,440,000|>30.5|135,000,000|trapezoid|30.5|<br>210.|64.|137.|2.25|227,000|0.5<br>0.5|0.5|0.5|
|94 Scott Farm Dam No. 2,Alberta|||86,000|10.4|894,000||11.9|<br>15.|15.|15.0|0.00|7,020||||
|95 Sheep Creek, USA|1,430,000|344,000|2,910,000|14.02|40,800,000|trapezoid|17.1|<br>30.5|<br>13.5|22.|0.5|18,300||||
|<br>96 Sherburne, USA|42,000|||||||46.|||||2.|||
|<br>97 Sinker Creek, USA|<br>3,330,000||3,330,000|21.34|71,100,000|trapezoid|21.3|<br>92.|49.2|70.6|0.5|84,100|2.|2.||
|<br>98 South Fork Tributary, Pennsylvania|||<br>3,700|1.83|<br>6,770|||||||||||
|<br>99 SpringLake,Rhode Island|135,000|72,800|136,000|5.49|747,000|trapezoid|5.49|<br>20.|9.|14.5|1.00|612||||
|100 Statham Lake Dam, Georgia|||564,000|5.55|3,130,000||5.12|||21.0|0.54|1,350||||
|<br>101 Swift, Montana|37,000,000||<br>37,000,000|47.85|<br>1,770,000,000|trapezoid|57.6|<br>225.|225.|225.|0.|<br>206,000|short|0.25||
|102 Teton Idaho|356000000||310000000|774|24000000000|raezoid|869|||1510|100|3060000|125<br>4|6||
|,<br>103 Trial Lake, Utah|,,||,,<br>1,480,000|.<br>5.18|,,,<br>7,670,000|p|.<br>5.18|<br>||.<br>21.0|.<br>0.82|,,<br>829|.<br>.|.||
|104 Trout Lake,North Carolina|||493,000|8.53|4,210,000||8.53|||26.2|1.79|4,830||||
|105 Upper Pond, Connecticut|||222,000|5.18|1,150,000||5.18|||16.5|1.71|||||
|<br>106 Wheatland No. 1, Wyoming<br>107 Wilkinson Lake Dam Georia|11,500,000||<br>11,600,000<br>533000|12.2<br>357|<br>142,000,000<br>1900000|trapezoid|13.7<br>372|<br>46.<br>|41.|35.4<br>290|0.75<br>174|14,600<br>1420|1.5<br>1.5|1.5||
|, g<br>108 Winston, North Carolina|664,000||,<br>662,000|.<br>6.40|,,<br>4,240,000|trapezoid|.<br>6.10|<br> <br>21.3|<br>18.3|.<br>19.8|.<br>0.20|,<br>1,480|5.|5.|5.|



_Table A2. — Dam failure database references and footnotes (from Table A1)._ 

|a|Babb,1968|
|---|---|
|b|ICOLD,1974|
|c|SCS,1981|
|d|Singh and Snorrason,1982|
|e|Jansen,1983|
|f|MacDonald and Langridge-Monopolis,1984|
|g|Costa,1985|
|h|Singh and Scarlatos,1988|
|i|Froehlich,1987|
|j|Froehlich,1995a|
|k|Froehlich,1995b|
|m|Froehlich,written communication|
|n|Ballentine,1993|
|o|Baker and Bliss,1996|
|p|Graham,1983|
|q|Graham,undated|
|r|Washington State Department of Ecology Dam Safety Section, written communication<br>(http://www.wa.gov/ecology/wr/dams/iowa.html)|



##### Notes regarding time parameters 

- 1 Breach formation times provided by Froehlich (1987, 1995b).  Considered to be “the time from the beginning of rapid growth of a breach, to the time when significant lateral erosion of the embankment had stopped.” 

- 2 Dam failure times provided by Singh and Snorrason (1982), and Singh and Scarlatos (1987).  Singh and Snorrason define the failure time as “from inception to completion of breach”. 

- 3 Maximum breach development times provided by MacDonald and Langridge-Monopolis (1984).  These are “estimates of the maximum times that it could have taken for the breaches to develop.”  MacDonald and Langridge-Monopolis go on to say that many of these times were reported in the literature as “the time to drain the reservoir.” 

- 4 Times to breach and empty reservoir provided by Singh and Snorrason (1982) 

60 

