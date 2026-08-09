---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Rotura de Presas\01 Información\TD-39_Using HEC-RAS for Dam Break Studies.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]



# **Using HEC-RAS for Dam Break Studies** 

#### **August 2014** 

TD-39 

Approved for Public Release.  Distribution Unlimited. 



<!-- Start of picture text -->
REPORT DOCUMENTATION PAGE Form Approved OMB No. 0704-0188<br>The public reporting burden for this collection of information is estimated to average 1 hour per response, including the time for reviewing instructions,<br>searching existing data sources, gathering and maintaining the data needed, and completing and reviewing the collection of information.  Send comments<br>regarding this burden estimate or any other aspect of this collection of information, including suggestions for reducing this burden, to the Department of<br>Defense, Executive Services and Communications Directorate (0704-0188).  Respondents should be aware that notwithstanding any other provision of<br>law, no person shall be subject to any penalty for failing to comply with a collection of information if it does not display a currently valid OMB control<br>number.<br>PLEASE DO NOT RETURN YOUR FORM TO THE ABOVE ORGANIZATION.<br>1.  REPORT DATE  (DD-MM-YYYY) 2.  REPORT TYPE  3.  DATES COVERED (From - To)<br>August 2014  Training Document<br>4.  TITLE AND SUBTITLE 5a.  CONTRACT NUMBER<br>Using HEC-RAS for Dam Break Studies  5b.  GRANT NUMBER<br>5c.  PROGRAM ELEMENT NUMBER<br>6.  AUTHOR(S) 5d.  PROJECT NUMBER<br>Gary Brunner<br>5e.  TASK NUMBER<br>5F.  WORK UNIT NUMBER<br>7.  PERFORMING ORGANIZATION NAME(S) AND ADDRESS(ES) 8.  PERFORMING ORGANIZATION REPORT NUMBER<br>U.S. Army Corps of Engineers  TD-39<br>Institute for Water Resources<br>Hydrologic Engineering Center (CEIWR-HEC)<br>609 Second Street<br>Davis, CA  95616-4687<br>9.  SPONSORING/MONITORING AGENCY NAME(S) AND ADDRESS(ES)  10.  SPONSOR/ MONITOR'S ACRONYM(S)<br>11.  SPONSOR/ MONITOR'S REPORT NUMBER(S)<br>12.  DISTRIBUTION / AVAILABILITY STATEMENT<br>Approved for Public Release.  Distribution Unlimited.<br>13.  SUPPLEMENTARY NOTES<br>14.  ABSTRACT<br>This document provides information on how to use the HEC-RAS (River Analysis System) software when performing<br>a dam break analysis. The document presents the unique hydraulic modeling aspects that are required, plus routing the<br>inflow flood through a reservoir; estimating dam breach characteristics; and, downstream routing/modeling issues.<br>15.  SUBJECT TERMS<br>HEC-RAS; hydraulic; model; terrain data; hydrologic; boundary conditions; terrain roughness; hydraulic structures;<br>calibration; unsteady flow; dam break; routing; inflow flood; reservoir; dam breach; downstream; modeling; flood<br>hydrograph; one-dimensional; Saint Venant equations; two-dimensional; level pool routing; scenarios; water surface<br>slope; pool; breach; dam; dynamic wave routing<br>16. SECURITY CLASSIFICATION OF:  17. LIMITATION   18. NUMBER  19a.  NAME OF RESPONSIBLE PERSON<br>a.  REPORT  b.  ABSTRACT  c.  THIS PAGE  OF  OF<br>ABSTRACT PAGES<br>U  U  U<br>UU  74  19b.  TELEPHONE NUMBER<br><!-- End of picture text -->

**Standard Form 298** (Rev. 8/98) Prescribed by ANSI Std. Z39-18 

# **Using HEC-RAS for Dam Break Studies** 

### **August 2014** 

U.S. Army Corps of Engineers Institute for Water Resources Hydrologic Engineering Center 609 Second Street Davis, CA  95616 

(530) 756-1104 (530) 756-8250 FAX <u>www.hec.usace.army.mil</u> 

TD-39 

_Table of Contents_ 

## **Table of Contents** 

|List of Figures ......................................................................................................................................_iii_|
|---|
|List of Tables ........................................................................................................................................_v_|
|Abbreviations ......................................................................................................................................_vii_|
|**Overview**.............................................................................................................................................. 1|
|**Routing the Inflow Flood through a Reservoir**................................................................................ 1|
|Full Dynamic Wave Routing ............................................................................................................. 3|
|Level Pool Routing ............................................................................................................................ 4|
|**Estimating the Dam Breach Characteristics**.................................................................................... 6|
|Causes and Types of Dam Failures ................................................................................................... 7<br>|
|Estimating Breach Parameters ........................................................................................................... 8|
|User Entered Data Method ............................................................................................................. 8|
|Simplified Physical Breaching Method ........................................................................................ 23|
|Physically-Based Breach Computer Models ................................................................................ 24|
|Peak Flow Equations and Envelope Curves .................................................................................... 26|
|Site Specific Data and Engineering Analysis .................................................................................. 28|
|Recommended Approach ................................................................................................................ 29|
|Example Application ....................................................................................................................... 31|
|**Downstream Flood routing/Modeling Issues**.................................................................................. 35|
|Cross Section Spacing and Hydraulic Properties ............................................................................ 36|
|Computational Time Step ................................................................................................................ 38|
|Manning's Roughness Coefficients ................................................................................................. 41|
|Downstream Storage, Tributaries, and Levees ................................................................................ 44|
|Modeling Bridge and Culvert Crossings ......................................................................................... 47|
|Modeling Steep Streams .................................................................................................................. 48|
|Drops in the Bed Profile .................................................................................................................. 50|
|Initial Conditions and Low Flow ..................................................................................................... 51|
|Downstream Boundary Conditions ................................................................................................. 53|
|Using Two-Dimensional Flow Areas for Dam Break Analysis ...................................................... 54|
|**References**.......................................................................................................................................... 57|



_i_ 

_Table of Contents_ 

ii 

_List of Figures_ 

## **List of Figures** 

###### **Figure Number** 

###### **Page** 

|1|Error in Level Pool Routing Compared to Full Dynamic Wave Routing. ................................ 3|
|---|---|
|2|Cross Section Layout for One-Dimensional Full Dynamic Routing Through a Reservoir. ...... 4|
|3|Reservoir Pool and Downstream Area Modeled with Two-Dimensional Flow Areas. ............ 5|
|4|Storage Area and Cross Section Layout for Level Pool Routing .............................................. 6|
|5|Example Breach Process for an Overtopping Failure ............................................................. 11|
|6|Example Breach Process for a Piping Failure ......................................................................... 12|
|7|Description of the Breach Parameters ..................................................................................... 14|
|8|Summary of Regression Equations for Breach Size and Failure Time (Wahl, 1998) ............. 16|
|9|HEC-RAS Simplified Physical Breach Option. ...................................................................... 24|
|10<br>|Envelope of Experienced Outflow Rates from Breached Dams ............................................. 28<br>|
|11|Dam Break Flood Wave Progression Downstream ................................................................. 30|
|12|Example Cross Section Layout (Ackerman, 2014) ................................................................. 36|
|13|Numerical Error Due to Cross Section Spacing ...................................................................... 37|
|14|Example Model Instability Due to Very Short Cross Section Spacing. .................................. 39|
|15|Example of Varying Computational Time Step ...................................................................... 40|
|16|Significant Turbulence and Sediment Load During the Teton Dam Failure (Olsen, 1976) .... 43|
|17|Cross Section Layout for a Tributary Coming Into a Main Stem River (Ackerman, 2014) ... 45|
|18|Example of Using Storage Areas and Lateral Weirs to Account for Flow Reversals up<br>Tributaries (Ackerman, 2014) ................................................................................................. 46|
|19|Tributary Storage Modeled as Cross Section Ineffective Flow Areas (Ackerman, 2014) ...... 46|
|20|Example of Using Lateral Structures and a Storage Area to model a Protected Area ............ 47|
|21|High Ground (Road or Levee) Represented as Part of the Cross Section ............................... 48|
|22|Example Bridge with Pre-Processed Bridge Curves ............................................................... 49|
|23|Model Instability Due to a Drop in the Bed Profile ................................................................ 51|
|24|Example of Initial Conditions for a Reservoir and Lateral Structures Connected to<br>Storage Areas .......................................................................................................................... 52|
|25|Example Model Due to Bad Downstream Boundary Condition ............................................. 54|
|26|Example of a Storage Area Connected to a Two-Dimensional Flow Area ............................. 55|



_iii_ 

_List of Figures_ 

iv 

_List of Tables_ 

## **List of Tables** 

###### **Table** 

|**Numb**|**er**|**Page**|
|---|---|---|
|1|Possible Failure Modes for Various Dam Types ................................................|....................... 8|
|2|Dam Breach Weir and Piping Coefficients ........................................................|..................... 13|
|3|Ranges of Possible Values for Breach Characteristics .......................................|..................... 15|
|4|Physically-Based Embankment Dam Breach Computer Software .....................|..................... 25|
|5|Summary of Erosion Process Models Currently Under Development ...............|..................... 26|
|6|Summary of Breach Parameter Estimates ..........................................................|..................... 35|



_v_ 

_List of Tables_ 

vi 

_Abbreviations_ 

## **Abbreviations** 

- ARS Agricultural Research Service C weir coefficient FERC Federal Energy Regulatory Commission FT Froude Number Threshold H:V horizontal/vertical HEC Hydrologic Engineering Center HEC-HMS Hydrologic Modeling System software HEC-RAS River Analysis System software LPI Local Partial Inertia Technique m exponent NOAA National Oceanic and Atmospheric Administration NWS National Weather Service PMF probable maximum flood SCS Soil Conservation Service USACE U.S. Army Corps of Engineers USBR U.S. Bureau of Reclamation 

_vii_ 

_Abbreviations_ 

viii 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

## **Using HEC-RAS for Dam Break Studies** 

#### **Overview** 

The development of an HEC-RAS (Hydrologic Engineering Center's (HEC), River Analysis System) hydraulic model requires an accurate representation of the terrain data and the hydrologic inputs used as boundary conditions.  Additionally, appropriate model parameters for terrain roughness and hydraulic structures must be estimated and then calibrated in order to have confidence in the model results.  The guidelines in this document are focused on the development and use of unsteady flow models for dam break studies.  Discussions of basic data requirements, hydraulic parameter estimates, and model calibration/validation are not covered in this document.  The HEC-RAS User's Manual (HEC, 2014) contains information describing model input, data requirements, parameter estimation, and model calibration. 

This document presents hydraulic modeling aspects that are unique to performing a dam break analysis.  Topics include: routing the inflow flood through a reservoir; estimating dam breach characteristics; and downstream routing/modeling issues. 

#### **Routing the Inflow Flood through a Reservoir** 

HEC-RAS can be used to route an inflowing flood hydrograph through a reservoir with any of the following three methods: 

- one-dimensional unsteady flow routing (full Saint Venant equations); 

- two-dimensional unsteady flow routing (Full Saint Venant equations or Diffusion wave equations); or 

- with level pool routing 

In general, full unsteady flow routing (one- or two-dimensional) will be more accurate for both the with and without breach scenarios.  The unsteady flow routing method can capture the water surface slope through the pool as the inflowing hydrograph arrives, as well as the change in water surface slope that occurs during a breach of the dam.  Reservoirs with long narrow pools will exhibit greater water surface slope upstream of the dam than reservoirs that are wide and short.  Therefore, the most accurate modeling technique to capture pool elevations and outflows of long narrow reservoirs is full dynamic wave (unsteady flow) routing.  For wide and short reservoirs, level pool routing may be appropriate. 

Several items must be taken into account before choosing the appropriate flood routing technique for a given study: 

- In situations where the population is at risk and any damage centers are far enough downstream, differences in peak outflow and the shape of the breach hydrograph may not be significant by the time the flood wave reaches the downstream locations.  Two hydrographs that have the same volume, but different peak flows and shape, will tend to converge as they 

1 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

are routed downstream through the river and floodplain.  In this situation, the reservoir can be modeled with either full unsteady flow routing or level pool routing. 

- The ability to acquire accurate cross section data (or terrain data for two-dimensional routing) through the pool can be problematic.  Detailed bathymetric surveys may be required to accurately describe the elevation-volume relationship of the reservoir pool.  If detailed bathymetric data are not available, and full unsteady-flow routing is still desired, cross section data can be modified to match the published elevation-volume curve of the reservoir pool.  This can be accomplished by running a series of steady flow profiles from the dam to the upstream end of the pool, using a small flow and varying the downstream starting condition for different pool elevations.  HEC-RAS will compute the volume under each profile.  The elevation-volume curve computed by HEC-RAS can then be compared to the published curve.  Start with the lowest elevations.  If the computed volume does not match the published volume, the cross sections should be modified to increase or decrease the volume required.  The **Channel Design/Modification Editor** in HEC-RAS may prove very useful for this task. 

- Capturing the full reservoir volume upstream of the dam will require the modeler to extend cross sections far enough upstream, such that the invert elevation of the most upstream cross section is higher than the highest elevation that will be modeled in the dam during the largest event.  Rough guidance would be to add a few feet to the top of the dam, and then extend the model upstream far enough so that the most upstream cross section's invert is higher than the highest elevation of the dam. 

- If there are significant numbers of tributaries, or some large tributaries upstream of the dam that enter the pool directly, then storage volume due to backwater up the tributaries must be accounted for as well as their inflows.  For one-dimensional unsteady flow routing, tributaries can be modeled in several manners.  One option is to model all of the significant tributaries as separate river reaches, using cross sections.  A second option is to model the tributaries as storage areas, and connect those storage areas to the main pool with a lateral structure (weir).  This will allow water to back up into the tributary as a level pool of water, thus accounting for its volume. A third option is to extend the reservoir cross sections up the tributaries and define that portion of the reservoir cross section as an ineffective flow area. 

The differences between level pool routing and full unsteady flow routing through a reservoir can be very difficult to quantify.  In order to decide if level pool routing is adequate, it is helpful to estimate the potential error in the peak flow of the routed outflow hydrograph, due to the use of level pool routing.  Dr. Danny Fread (National Weather Service, NWS) performed several numerical experiments in which Dr. Fread compared both full dynamic wave routing to level pool routing (Fread, 2006).  From these experiments, Dr. Fread developed a set of equations and a graph that can be used to estimate the error in using level pool routing for a given reservoir and flood event.  The graph and equations are shown in Figure 1 (Fread, 2006). 

###### where: 

- Dr = the average depth of water in the reservoir (feet); approximated as Dmax/2. 

- Lr = the length of the reservoir pool in feet 

- Tr = the time of rise if the inflowing hydrograph in hours 

2 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 1.** Error in Level Pool Routing Compared to Full Dynamic Wave Routing 

In order to compute the error in level pool routing (Figure 1), the user must calculate σl, σv, and σt.  Once these three parameters are calculated, a percent error in the rising limb/peak flow of the outflow hydrograph can be estimated.  This error represents the difference in the answers between using level pool routing and full dynamic wave routing. 

##### **Full Dynamic Wave Routing** 

As discussed previously, full dynamic wave (unsteady flow) routing through the reservoir pool is the most accurate methodology and therefore should be performed for dam break analyses of USACE (U.S. Army Corps of Engineers) dams whenever practical.  To model the reservoir using full dynamic wave routing with HEC-RAS, the user can either model the pool with onedimensional cross sections throughout the entire reservoir, as would be done for a normal river reach, or they can model the reservoir pool as a single two-dimensional flow area.  The dam is modeled with the **Inline Structure** option in HEC-RAS.  An example plot of modeling the pool with one-dimensional cross sections is shown in Figure 2. 

The inflow hydrographs (computed with HEC-HMS (Hydrologic Modeling System) can be entered as boundary conditions at the upper end of the pool (flow hydrograph), and at any of the locations within the reservoir pool (lateral inflow hydrographs). 

When modeling the pool with cross sections, the engineer should be aware that after a dam breach occurs, the upper reach will no longer be fully inundated from the reservoir pool, thus acting more like a normal river reach.  If the inflowing hydrograph recedes to a very low flow at the tail of the event, there could be some potential model instabilities resulting from the 

3 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 2** .  Cross Section Layout for One-Dimensional Full Dynamic Routing through a Reservoir 

combination of a low flow and irregular channel geometry.  One way around this is to increase the base flow on the recession of the upstream hydrographs.  Another approach is to smooth out any major irregularities in the channel invert for the cross sections upstream of the dam. Sometimes, the combination of these two suggestions may be necessary to keep a stable solution above the dam for the tail end of the hydrograph. 

If the reservoir pool is modeled with a two-dimensional flow area, then it can go completely dry without any model stability issues when the two-dimensional cells dry out.  An example of modeling a reservoir with a two-dimensional flow area is shown in Figure 3. 

##### **Level Pool Routing** 

If it is not possible, necessary, or reasonable to perform full dynamic wave routing though the reservoir, or if the presumed difference between level pool routing and dynamic routing is small, then level pool routing can be performed with HEC-RAS.  To model a reservoir using level pool routing in HEC-RAS, the pool area is modeled with a storage area (HEC-RAS option for modeling an area with level pool routing).  That storage area is connected to a downstream river reach, and that river reach must have a cross section that is inside the reservoir pool.  The first cross section in the reach is tied to the storage area by the fact that it will always have the same water surface elevation during the computations.  The dam is modeled as an inline structure, which requires one cross section upstream of the inline structure.  However, the cross section upstream of the inline structure is tied to the inline structure boundary condition, and it cannot be the first cross section of the reach.  Because of this limitation in HEC-RAS, the result is that the model must have two cross sections upstream of the inline structure: one cross section for the connection to the storage area, and the second cross section for the inline structure boundary condition.  Both of the upstream cross sections should be representative of the reservoir area 

4 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 3.** Reservoir Pool and Downstream Area Modeled with Two-Dimensional Flow Areas 

immediately upstream of the dam.  The distance between these two cross sections should be short (ten to twenty feet), so that the storage volume between the two cross sections is small.  An example diagram of modeling the reservoir with a storage area in HEC-RAS is shown in Figure 4. 

The engineer must enter an elevation-volume curve as part of the storage-area data describing the reservoir.  The minimum elevation of the two upstream cross sections should be roughly equal to the minimum elevation specified for the storage area in order to prevent any instability once the storage area is emptied. 

When a dam break is modeled, the breach discharge will be computed by using the same equations as the full dynamic wave method.  The only difference is that the water supplied to the dam will come from the storage area, and the storage area elevation will drop as a level pool as water flows out of the breach.  As noted above, when a rapidly forming breach occurs, the water surface upstream of the dam will often have a significant slope to it.  With the level pool routing method, the water surface in the reservoir is always horizontal.  This may or may not produce 

5 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 4.** Storage Area and Cross Section Layout for Level Pool Routing 

significant differences in the outflow hydrograph, depending on many factors as outlined in this Section. 

#### **Estimating the Dam Breach Characteristics** 

The estimation of a dam breach location, dimensions, and development time are crucial in any assessment of a dam's potential risk.  This is especially true in a risk assessment where dams will be ranked based on the potential for loss of life and property damage.  The breach parameters will directly affect the estimate of the peak flow coming out of the dam, as well as any possible warning time available to downstream locations.  Unfortunately, the breach location, size, and formation time, are often the most uncertain pieces of information in a dam failure analysis. 

When performing a dam breach analysis, one must first estimate the characteristics of the breach. Once the breaching characteristics are estimated, then HEC-RAS can be used to compute the outflow hydrograph from the breach and perform the downstream routing. 

The breach dimensions and development time must be estimated for every failure scenario that will be evaluated.  This requirement includes different failure modes as well as different hydrologic events.  The breach parameters associated with a PMF (probable maximum flood) hydrologic event will be greatly different than the breach parameters for a sunny day failure at a normal pool elevation.  Therefore, for each combination of pool elevation (hydrologic event) and failure scenario, a corresponding set of breach parameters must be developed. 

A dam's potential breach characteristics can be estimated in several ways, including: comparative analysis (comparing your dam to historical failures of dams of similar size, materials, and water volume); regression equations (equations developed from historical dam failures in order to estimate peak outflow or breach size and development time); utilization of velocity (or shear stress) vs. erosion rates; and physically based computer models (software that attempts to model the physical breaching process by using sediment transport/erosion equations, soil mechanics, and principles of hydraulics).  All of these methods are viable techniques for estimating breach 

6 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

characteristics.  However, each of these methods has strengths and weaknesses and should be considered as a way of "estimating" the parameters and not utilized as absolute values. 

In addition to the methods described above, site specific information, structural, and geotechnical analyses should be used to refine and support the estimates of the breach parameters for each failure scenario/hydrologic event.  Historic breach information, regression equations, and physically based computer models all have limitations that must be well understood when they are applied.  In any dam safety study it is important to consider a range of parameter estimates for the breach size and development time for each failure scenario/event, and then perform a sensitivity analysis of the breach parameters to identify their affect on the outflow hydrograph, downstream stages and flows, and warning time to any population at risk. 

The following section will cover causes and types of dam failures; estimating breach parameters; recommended approach; and an example application. 

As with many aspects of dam failure modeling in risk assessment studies, the level of effort in estimating breach parameters should be consistent with the type of risk assessment.  In general, the level of effort and detail will increase from dams that are classified as "Low Hazard", to dams that are classified as "High Hazard". 

##### **Causes and Types of Dam Failures** 

Historically, all types of dams have experienced failures due to one or more type of event/loading.  However, by far the majority of dam failures that have occurred have been earthen dams, caused by some level of flood.  The types of dams that are commonly built and found in the field are: 

- Earthen embankment/rockfill 

- Concrete arch and multi arch 

- Concrete gravity 

- Buttress (combination of concrete gravity and arch dam) 

- Steel, timber, and composite materials 

There are many mechanisms that can be the driving force of a dam failure.  The following is a list of mechanisms that can cause dam failures: 

- Flood event 

- Piping/seepage (internal and underneath the dam) 

- Landslide 

- Earthquake 

- Foundation failure 

- Equipment failure/malfunction (gates, etc.) 

- Structural failure 

- Upstream dam failure 

- Rapid drawdown of pool 

- Sabotage 

- Planned removal 

7 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Given the different mechanisms that cause dam failures, there can be several possible ways a dam may fail for a given driving force/mechanism.  Table 1 shows a list of dam types versus possible modes of failure (Costa, 1985; Atallah, 2002). 

Costa (1985) reports that of all dam failures as of 1985, 34 percent were caused by overtopping, thirty percent due to foundation defects, 28 percent from piping and seepage, and eight percent from other modes of failure.  Costa (1985) also reports that for earth/embankment dams only, 35 percent have failed due to overtopping, 38 percent from piping and seepage, 21 percent from foundation defects; and six percent from other failure modes. 

**Table 1** .  Possible Failure Modes for Various Dam Types 

|**Failure Mode**|**Earthen/**<br>**Embankment**|**Concrete**<br>**Gravity**|**Concrete**<br>**Arch**|**Concrete**<br>**Buttress**|**Concrete**<br>**Multi-Arch**|
|---|---|---|---|---|---|
|Overtopping|X|X|X|X|X|
|Piping/Seepage|X|X|X|X|X|
|Foundation Defects|X|X|X|X|X|
|Sliding|X|X||X||
|Overturning||X|X|||
|Cracking|X|X|X|X|X|
|Equipment failure|X|X|X|X|X|



##### **Estimating Breach Parameters** 

The estimation of the breach location, size, and development time are crucial in order to make an accurate estimate of the outflow hydrographs and downstream inundation.  However, these parameters are some of the most uncertain in the entire analysis.  Currently within HEC-RAS, the user has two breaching methodologies to choose from, either " **User Entered Data** " or " **Simplified Physical** ".  The **User Entered Data** method requires the user to enter all of the breach information (i.e., breach size, breach development time, breach progression, etc.).  The **Simplified Physical** breaching method allows the user to enter velocity versus breach downcutting and breach widening relationships, which are then used dynamically to figure out the breach progression versus the actual velocity being computed through the breach, on a time step by time step basis. 

###### **User Entered Data Method** 

When using the **User Entered Data** option in HEC-RAS, the software requires the user to enter the following information to describe a breach: 

**Location** : centerline stationing of the breach in the dam 

**Failure Mode** : overtopping or piping 

**Shape** : bottom elevation, bottom width, left and right side slopes H:V 

**Time** : critical breach development time 

**Trigger Mechanism** : pool elevation; pool elevation plus duration; or clock time 

8 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

**Weir and Piping Coefficients** : weir coefficients are used to compute overtopping/weir flow, and an orifice coefficient is used to compute piping/pressure flow. 

**Failure Location.** The breach failure location is based on many factors (type and shape of dam, failure type, mode, and driving force of the failure).  In general, one should consider all factors about the dam, including any historical knowledge of seepage and foundation problems, and place the breach location in the most probable location for each failure type. The geotechnical engineer should be involved in determining the appropriate placement of the breach. 

**Failure Mode.** While HEC-RAS hydraulic computations are limited to overtopping and piping failure modes, all other failure modes can be simulated with one of these two methods.  Failure mode is the mechanism for starting and growing the breach.  Overtopping failures start at the top of the dam and grow to maximum extents, while a piping failure mode can start at any elevation/location and grow to the maximum extents.  The ultimate breach size and breach formation time are much more critical in the estimation of the outflow hydrograph, than the actual failure initiation mode. 

**Critical Breach Development Time.** HEC-RAS requires the user to enter what is called the "critical breach development time".  The critical breach development time for HEC-RAS can be described as follows: 

**Overtopping Failure:** The HEC-RAS breach start time is considered to be when the erosion process has migrated to the upstream face of the dam (this is the start of a breach for HEC-RAS).  This is the point at which the outflow from the dam will start to increase due to the breach.  This condition is depicted in Figure 5C-D.  The end of the breach development time for HEC-RAS is when the breach is fully formed and significant erosion has stopped. The breach development ending time should not include the time to completely drain the reservoir pool. 

**Piping Failure:** The HEC-RAS breach starting time for a piping failure is considered to be when a significant amount of flow and material are coming out of the piping failure hole.  The breach ending time is considered to be when the breach is, for the most part, fully formed (significant erosion has stopped, not the time until the reservoir pool is emptied). 

The estimation of the critical breach development time must be done outside of the HECRAS software and entered as input data.  Descriptions on how to estimate this time are provided. 

**Breach Weir and Piping Flow Coefficients.** Weir and piping coefficients must be entered by the user in HEC-RAS.  These coefficients directly affect the magnitude of the peak outflow hydrograph for any given breach.  Unfortunately, exact knowledge of the magnitude of these coefficients for a dam failure (overtopping or piping failure) is not known. 

9 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

In order to estimate the weir and piping flow coefficients, it is necessary to understand the basic failure process.  The following is a generalized description of the breach process for an overtopping failure of an earthen dam.  This description may not be true for all earthen dams, as the breach process is a function of many parameters, such as: height of the dam; volume of water behind the dam (including the inflowing hydrograph); materials that the dam is constructed of; depth and duration of overtopping; outer protective cover on the downstream and upstream side of the embankment; and other parameters. 

**Overtopping Failure.** In general, during an overtopping failure (Figure 5) of an earthen dam, a headcut erosion process will first start on the downstream side of the dam embankment (Figure 5A).  While water is going over the dam crest, the dam crest acts like a broad-crested weir.  The headcut will erode back towards the center of the dam and widen over time (Figure 5B).  As the headcut begins to cut into the dam crest, the weir crest length will become shorter, and the appropriate weir coefficient will trend towards a sharp-crested weir value (Figure 5C).  The time for breach initiation used in HEC-RAS is shortly after what is depicted in Figure 5C.  When the headcut reaches the upstream side of the dam crest, a mass failure of the upstream crest may occur, and the hydraulic control section will act very much like a sharp-crested weir (Figure 5D).  The headcut will continue to erode upstream through the dam embankment, as well as erode down through the dam and widen at the same time (Figure 5E).  During this process, the appropriate weir coefficient will begin to trend back towards a broad-crested weir coefficient.  As the downward cut reaches the natural river bed elevation, and the breach is more in a widening phase, the appropriate weir coefficient is more in the range of a broad-crested weir value. 

**Piping Failure.** A general description of a piping failure (Figure 6) is as follows.  Water is seeping through the dam at a significant enough rate, such that it is internally eroding material and transporting it out of the dam.  As the material is eroded, a larger hole is formed, thus able to carry more water and erode more material (Figure 6A).  The movement of water through the dam during this process is modeled as a pressurized orifice type of flow.  During the piping flow process, erosion and headcutting will begin to occur on the downstream side of the dam (Figure 6B) as a result of flow exiting the pipe.  As the piping hole grows larger, material above the hole will begin to slough off and fall into the moving water (Figure 6C).  The headcutting and material sloughing processes will continue to move back towards the upstream side of the dam, while the piping hole continues to grow simultaneously (Figure 6D).  If the piping hole is large enough, the weight of the material above the hole may be too great to be maintained, and a mass caving of material will occur.  This will result in a large rise in the outflow through the breach and will accelerate the breaching process.  Also at this point, the hydraulics of the flow transitions from a pressure/orifice type flow to an open air weir type flow.  The headcutting and erosion process then continues back through the dam, as well as downward (Figure 6E).  Additionally, the breach will be widening.  Depending on the volume of water behind the dam, the breach may continue to cut down and widen until the natural channel bed is reached.  Then the breach will go into a widening phase. 

10 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 5.** Example Breach Process for an Overtopping Failure 

11 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 6.** Example Breach Process for a Piping Failure 

12 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

As you can imagine from the description of the breach processes, as well as other factors and complications that may occur in the real world, estimating these parameters can be difficult. Currently in software such as HEC-RAS, the user is only allowed to enter a single value for the breach weir coefficient and for the piping coefficient.  Because the estimate of the peak flow is so important in this process, one should try to estimate these coefficients based on the phase of the breach process in which they think the largest flows will most likely occur.  For example, earthen dams with medium to very large storage volumes upstream, will most likely have failed all the way down to the natural stream bed elevation, and be in the breach widening phase when the peak outflow occurs.  This would suggest using a weir coefficient (C) that is typical of a broad-crested weir with a long crest length (i.e., C = 2.6).  However, for dams with a relatively low volume of water in comparison to the height of the dam, the peak flow may occur during the phase of the breach in which the breach is still cutting down through the dam.  For this case, a weir coefficient typical of a sharp-crested weir would be more appropriate (i.e., C = 3.2).  Other factors to consider are the material types of the dam.  Dams that have a clay core, and are generally constructed of clay material, will tend to have a much more pronounced headcut process.  While dams that are more in the sand and gravel range will have a less pronounced headcut process.  This may lead to using higher weir coefficients for a clay dam (i.e., C = 3.2, sharp-crested weir) versus a gravel/sand dam (i.e., C = 2.6, broad-crested weir). 

During a piping failure breach, the rate of water flowing through the dam is modeled with an orifice pressure flow equation.  This equation also requires a discharge coefficient, which is a measure of how efficiently the flow can get into the pipe orifice.  Because a piping failure is not a hydraulically designed opening, it is assumed that the entrance is not very efficient. Recommended values for the piping/pressure flow coefficients are in the range of 0.5 to 0.6. Guidelines for selecting breach weir and piping flow coefficients are provided in Table 2. 

**Table 2.** Dam Breach Weir and Piping Coefficients 

|**Dam Type**|**Overflow/Weir**<br>**Coefficients**|**Piping/Pressure Flow**<br>**Coefficients**|
|---|---|---|
|Earthen Clay or Clay Core|2.6–3.3|0.5–0.6|
|EarthenSand andgravel|2.6–3.0|0.5–0.6|
|ConcreteArch|3.1 –3.3|0.5–0.6|
|Concrete Gravity|2.6 – 3.0|0.5 – 0.6|



**Breach Shape Definitions.** For the purposes of these guidelines, the physical description of the breach will consist of the height of the breach, breach width, and side slopes in H:V (side slopes are expressed in units of distance horizontal to every one unit in the vertical).  These values represent the maximum breach size.  A diagram describing the breach is shown in Figure 7. 

The breach width is described as the average breach width (Bave) in many equations, while HECRAS requires the breach bottom width (Wb) for input.  The breach height (hb) is the vertical extent from the top of the dam to the average invert elevation of the breach.  Many publications and equations also use the height of the water (hw), which is the vertical extent from the maximum water surface to the invert elevation of the breach.  The side slopes are expressed in H:V. 

The breach dimensions, as well as the breach formation time must be estimated outside of the HEC-RAS software, and entered into the program.  Many case studies have been performed on 

13 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 7.** Description of the Breach Parameters 

data from historic dam failures, leading to guidelines, regression equations, and computer modeling methodologies for prediction of the dam breach size and time.  One of the most comprehensive summaries of the literature on historic dam failures is a U.S. Bureau of Reclamation (USBR) report written by Mr. Tony Wahl titled " _Prediction of Embankment Dam Breach Parameters - A Literature Review and Needs Assessment_ " (Wahl, 1998).  This report discusses all types of dams, however the report focuses on earthen/embankment dams for the discussion of estimating breach parameters.  Much of what is presented in this section of the guidelines was extracted from that report.  Guidelines for breach parameters for concrete (arch, gravity, buttress, etc.), steel, timber, and other types of structures, is very sparse, and is limited to simple ranges. 

**Federal Agency Guidelines.** Many federal agencies have published guidelines in the form of possible ranges of values for breach width, side slopes, and development time.  Table 3 summarizes some of these guidelines. 

The guidelines shown in Table 3 should be used as minimum and maximum bounds for estimating breach parameters.  More specific ways to estimate breach characteristics are addressed below. 

**Regression Equations.** Several researchers have developed regression equations for the dimensions of the breach (width, side slopes, volume eroded, etc.), as well as the failure time. These equations were derived from data for earthen dams, earthen dams with impervious cores (i.e., clay, concrete, etc.), and rockfill dams.  Therefore, these equations do not directly apply to concrete dams or earthen dams with concrete cores.  The report by Wahl (1998) describes several equations that can be used for estimating breach parameters.  Summarized in Figure 8 are the regression equations developed to predict breach dimensions and failure time from the USBR report (Wahl, 1998). 

Since the report by Wahl (1998), additional regression equations have been developed to estimate breach width and breach development time.  In general, several of the regression equations should be used to make estimates of the breach dimensions and failure time.  These estimates should then be used to perform a sensitivity analysis, as discussed later in this 

14 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

**Table 3.** Ranges of Possible Values for Breach Characteristics 

|**Dam Type**|**Average**<br>**Breach Width**<br>(Bave)|**Horizontal**<br>**Component of**<br>**Breach Side**<br>**Slope (H)**<br>(H:V)|**Failure**<br>**Time, tf**<br>(hours)|**Agency**|
|---|---|---|---|---|
||(0.5 to 3.0) x HD|0 to 1.0|0.5 to 4.0|USACE 1980|
|Eth/Rkfill|(1.0 to 5.0) x HD|0 to 1.0|0.1 to 1.0|FERC|
|arenoc|(2.0 to 5.0) x HD|0 to 1.0 (slightly larger)|0.1 to 1.0|NWS|
||(0.5to5.0)x HD*|0to 1.0|0.1 to 4.0*|USACE 2007|
||Multiple Monoliths|Vertical|0.1 to 0.5|USACE 1980|
|Ct Git|Usually ≤ 0.5 L|Vertical|0.1 to 0.3|FERC|
|oncree ravy|Usually ≤ 0.5 L|Vertical|0.1 to 0.2|NWS|
||Multiple Monoliths|Vertical|0.1 to 0.5|USACE 2007|
||Entire Dam|Valley wall slope|≤ 0.1|USACE 1980|
|C Ah|Entire Dam|0 to valley walls|≤ 0.1|FERC|
|oncrete rc|(0.8 x L) to L|0 to valley walls|≤ 0.1|NWS|
||(0.8 x L) to L|0 to valley walls|≤ 0.1|USACE 2007|
|Sl/Rf|(0.8 x L) to L|1.0 to 2.0|0.1 to 0.3|FERC|
|ageuse|(0.8 x L)to L||≤ 0.1|NWS|



* **Note:** Dams that have very large volumes of water, and have long dam crest lengths, will continue to erode for long durations (i.e., as long as a significant amount of water is flowing through the breach), and may therefore have longer breach widths and times than what is shown in Table 3.  HD = height of the dam; L = length of the dam crest; FERC - Federal Energy Regulatory Commission; NWS - National Weather Service 

document.  The user should try to pick regression equations that were developed with data that is representative of the study dam.  In many cases this may not be possible, due to the fact that most of the historic dam failures for earthen dams have occurred on smaller structures.  In fact, out of the 108 historic dam breaches listed in the USBR report (Wahl, 1998), only thirteen of the dams are over 100 feet (30.5 meters) high and only five of the dams had a storage volume greater than 100,000 acre-feet (123.4x10<sup>6</sup> cubic meters) at the time of failure.  Additionally, most of the regression equations were developed from a smaller subset of this data (20 to 50 dams), and the dams included in the analysis are a mixture of homogenous earthen dams and zoned earthen dams (dams with clay cores, or varying materials).  Therefore, the use of any of the regression equations should be done with caution, especially when applying them to larger dams that are outside the range of data for which the equations were developed.  The use of regression equations for situations outside of the range of the data they for which were developed for may lead to unrealistic breach dimensions and development times. 

The following regression equations have been used for several dam safety studies found in the literature (except the Xu and Zhang equations, which are presented because of their wide range of historical data values), and are presented in greater detail in this document: 

- Froehlich (1995a) 

- Froehlich (2008) 

- MacDonald and Langridge-Monopolis (1984) 

- Von Thun and Gillette (1990) 

- Xu and Zhang (2009) 

15 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

**Table 2 - Breach Parameter relations based on dam-failure case studies. For explanations of symbols see the Notation section at the end of this report.** 

|**Reference**|**Number of**<br>**CaseStudies**|**Relations Proposed**<br>**(S.I. units, meters, m**<sup>**3**</sup>**/s, hours)**|
|---|---|---|
|Johnson and Illes(1976)||_0.5hd_ ≤ _B_ ≤ _3hd_for earthfill dams|
|Singh and Snorrason<br>(1982, 1984)|20|_2hd ≤ B ≤hd _<br>0.15 meters ≤_dovtop_≤0.61 meters<br>0.25 hours≤ _tf_ ≤1.0 hours|
|MacDonald and<br>Langridge-Monopolis<br>(1984)|42|Earthfill dams:<br>_Ver_= 0.0261(_Vout*hw_)<sup>0.769</sup><br>[best-fit]<br>_tf_= 0.0179(_Ver_)<sup>0.564</sup><br>[upper envelope]<br>Non-earthfill dams:<br>_Ver_= 0.00348(_Vout*hw_)<sup>0.852</sup><br>[best-fit]|
|FERC (1987)||_B_is normally 2-4 times_hd_<br>_B_can range from 1-5 times_hd_<br>_Z_= 0.25 to 1.0<br>[engineered, compacted dams]<br>_Z_= 1 to 2<br>[non-engineered, slag or refuse dams]<br>_tf_= 0.1-1 hours<br>[engineered, compacted earth dams]<br>_tf_= 0.1-0.5 hours<br>[non-engineered, poorlycompacted]|
|Froehlich (1987)|43|𝐵<br>~~∗~~= 0.47Ko(S*)0.25<br>_Ko_= 1.4 overtopping; 1.0 otherwise<br>𝑍 = 0.75𝐾𝑐(ℎ𝑤<br>∗)1.57�𝑊<br>∗�<br>0.73<br>_Kc_= 0.6 with corewall; 1.0 without a corewall<br>𝑡𝑓<br>∗_= 79(S*)0.47_|
|Reclamation (1988)||_B = (3)hw _<br>_tf =(0.011)B _|
|Singh and Scarlatos<br>(1988)|52|Breach geometry and time of failure tendencies<br>_Btop/Bbottom_averages 1.29|
|Von Thun and Gillette<br>(1990)|57|_B, Z, tf_guidance (see discussion)|
|Deweyand Gillette(1993)|57|Breach initiation model; _B, Z, tf_ guidance|
|Froehlich (1995b)|63|𝐵<br>= 0.1803𝐾𝑜𝑉𝑤<br>0.32ℎ𝑏<br>0.19<br>𝑡𝑓= 0.00254𝑉𝑤<br>0.55ℎ𝑏<br>(−0.90)<br>Ko= 1.4 for overtopping;1.0 otherwise|



**Figure 8.** Summary of Regression equations for Breach size and Failure Time (Wahl 1998) 

These regression equations have been used on several dam break studies and have been found to give a reasonable range of values for earthen, zoned earthen, earthen with a core wall (i.e., clay), and rockfill dams.  The following is a brief discussion of each equation set. 

**Froehlich (1995a):** Froehlich utilized 63 earthen, zoned earthen, earthen with a core wall (i.e., clay), and rockfill data sets to develop as set of equations to predict average breach width, side slopes, and failure time.  The data that Froehlich used for his regression analysis had the following ranges: 

- **Height of the dams:** 3.66 – 92.96 meters (12 – 305 feet) (with 90% < 30 meters, and 76% < 15 meters) 

- **Volume of water at breach time:** 0.0130 – 660.0 m<sup>3</sup> x 10<sup>6</sup> (11 - 535,000 acre-feet) (with 87% < 25.0 m<sup>3</sup> x 10<sup>6</sup> , and 76% < 15.0 m<sup>3</sup> x 10<sup>6</sup> ) 

16 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Froehlich's regression equations for average breach width and failure time are: 



where: 

Bave = average breach width (meters) 

Ko = constant (1.4 for overtopping failures, 1.0 for piping) 

- Vw = reservoir volume at time of failure (cubic meters) 

hb = height of the final breach (meters) tf = breach formation time (hours) 

Froehlich states that the average side slopes should be: 

1.4H:1V overtopping failures 

0.9H:1V otherwise (i.e., piping/seepage) 

While not clearly stated in Froehlich's paper, the height of the breach is normally calculated by assuming the breach goes from the top of the dam all the way down to the natural ground elevation at the breach location. 

**Froehlich (2008):** In 2008, Dr. Froehlich updated his breach equations based on the addition of new data.  Dr. Froehlich utilized 74 earthen, zoned earthen, earthen with a core wall (i.e., clay), and rockfill data sets to develop as set of equations to predict average breach width, side slopes, and failure time.  The data that Froehlich used for his regression analysis had the following ranges: 

- **Height of the dams:** 3.05 – 92.96 meters (10 – 305 feet) (with 93% < 30 meters,  and 81% < 15 meters) 

- **Volume of water at breach time:** 0.0139 – 660.0 m<sup>3</sup> x 10<sup>6</sup> ( 11.3 - 535,000 acre-feet) (with 86% < 25.0 m<sup>3</sup> x 10<sup>6</sup> , and 82% < 15.0 m<sup>3</sup> x 10<sup>6</sup> ) 

Froehlich's regression equations for average breach width and failure time are: 



where: 



- Bave = average breach width (meters) 

- Ko = constant (1.3 for overtopping failures, 1.0 for piping) 

- Vw = reservoir volume at time of failure (cubic meters) hb = height of the final breach (meters) g = gravitational acceleration (9.80665 meters per second squared) tf = breach formation time (seconds) 

17 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Froehlich's 2008 paper states that the average side slopes should be: 

- 1.0 H:1V overtopping failures 

0.7 H:1V otherwise (i.e., piping/seepage) 

While not clearly stated in Froehlich's paper, the height of the breach is normally calculated by assuming the breach goes from the top of the dam all the way down to the natural ground elevation at the breach location. 

**MacDonald and Langridge–Monopolis (1984):** MacDonald and Langridge-Monopolis utilized 42 data sets (predominantly earthfill dams, earthfill dams with a clay core, rockfill dams) to develop a relationship for what they call the "Breach Formation Factor".  The Breach Formation Factor is a product of the volume of water coming out of the dam and the height of water above the dam.  MacDonald and Langridge-Monopolis then related the breach formation factor to the volume of material eroded from the dam's embankment.  The data that MacDonald and Langridge-Monopolis used for their regression analysis had the following ranges: 

- **Height of the dams:** 4.27 – 92.96 meters (14 – 305 feet) (with 76% < 30 meters, and 57% < 15 meters) 

- **Breach Outflow Volume:** 0.0037 – 660.0 m<sup>3</sup> x 10<sup>6</sup> (3 - 535,000 acre-feet) (with 79% < 25.0 m<sup>3</sup> x 10<sup>6</sup> , and 69% < 15.0 m<sup>3</sup> x 10<sup>6)</sup> 

The following is the MacDonald and Langridge-Monopolis equation for volume of material eroded and breach formation time, as reported by Wahl (1998): 

For earthfill dams: 

.0769 _Veroded_ = .00261 _V_ * _h_ ( _out w_ ) .0364 _tf_ = .00179 ( _Veroded_ ) 

For earthfill with clay core or rockfill dams: 

.0852 _Veroded_ = .000348 _V_ * _h_ ( _out w_ ) 

where: 

- Veroded = volume of material eroded from the dam embankment (cubic meters) Vout = volume of water that passes through the breach (cubic meters); for example, storage volume at time of breach plus volume of inflow after breach begins, minus any spillway and gate flow after breach begins. 

- hw = depth of water above the bottom of the breach (meters). 

- tf = breach formation time (hours). 

The value of the Vout parameter is not exactly known before performing the breach analysis, as it is the volume of water that passes through the breach (not including flow from gates, spillways, and overtopping of the dam away from the breach area).  A good first estimate is the volume of water in the reservoir at the time the breach initiates.  Once a set of parameters 

18 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

are estimated, and a breach analysis is performed, the user should go back and try to make a better estimate of the actual volume of water that passes through the breach.  Then recalculate the parameters with that volume.  The recalculation of the volume makes the method iterative.  The actual breach dimensions are a function of the volume eroded. MacDonald and Langridge-Monopolis stated that the breach should be trapezoidal with side slopes of 0.5H:1V.  The breach size is computed by assuming the breach erodes vertically to the bottom of the dam and it erodes horizontally until the maximum amount of material has been eroded or the abutments of the dam have been reached.  The base width of the breach can be computed from the dam geometry with the following equation (State of Washington, 1992): 



where: 

- Wb = bottom width of the breach (meters) 

- hb = height from the top of the dam to bottom of breach (meters) C = crest width of the top of dam (meters) 

- Z3 = Z1 + Z2 

- Z1 = average slope (Z1:1) of the upstream face of dam Z2 = average slope (Z2:1) of the downstream face of dam 

- Zb = side slopes of the breach (Zb:1), 0.5 for the MacDonald method 

**Note:** MacDonald and Langridge-Monopolis stated that the equation for the breach formation time is an envelope of the data from the earthfill dams.  An envelope equation implies that the equation will tend to give high estimates (too long) of the actual breach time (for homogenous earthfill dams).  Wahl's study states this method will over predict times in some cases, while many equations will under predict. 

**Von Thun and Gillette (1990):** Von Thun and Gillette used 57 dams from both the Froehlich (1987) paper and the MacDonald and Langridge-Monopolis (1984) paper to develop their methodology.  The method proposes to use breach side slopes of 1.0H:1.0V, except for dams with cohesive soils, where side slopes should be on the order of 0.5H:1V to 0.33H:1V.  The data that Von Thun and Gillette used for their regression analysis had the following ranges: 

- **Height of the dams:** 3.66 – 92.96 meters (12 – 305 feet) (with 89% < 30 meters, and 75% < 15 meters) 

- **Volume of water at breach time:** 0.027 – 660.0 m<sup>3</sup> x 10<sup>6</sup> ( 22 - 535,000 acre-ft) (with 89% < 25.0 m<sup>3</sup> x 10<sup>6</sup> , and 84% < 15.0 m<sup>3</sup> x 10<sup>6</sup> ) 

The Von Thun and Gillette equation for average breach width is: 

_Bave_ = 2.5 _h_ + _C w b_ 

where: 

- Bave = average breach width (meters) hw = depth of water above the bottom of the breach (meters) Cb = coefficient, which is a function of reservoir size, see the following table. 

19 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

|**Reservoir Size**|**Cb**|**Reservoir Size**|**Cb**|
|---|---|---|---|
|(cubic meters)|(meters)|(acre-feet)|(feet)|
|< 1.23<sup>∗</sup>10<sup>6</sup>|6.1|<1,000|20|
|1.23<sup>∗</sup>10<sup>6 </sup>−6.17<sup>∗</sup>10<sup>6</sup><br>|18.3|1,000 - 5,000|60|
|6.17<sup>∗</sup>10<sup>6 </sup>−1.23<sup>∗</sup>10<sup>7</sup>|42.7|5,000 - 10,000|140|
|> 1.23<sup>∗</sup>10<sup>7</sup>|54.9|> 10,000|180|



Von Thun and Gillette developed two different sets of equations for the breach development time.  The first set of equations shows breach development time as a function of water depth above the breach bottom: 



where: 

- tf = breach formation time (hours) hw = depth of water above the bottom of the breach (meters) 

The second set of equations shows breach development time as a function of water depth above the bottom of the breach and average breach width: 





where: 

Bave = average breach width (meters) 

**Note:** Von Thun and Gillette's breach formation time equations are presented for both "erosion resistant" and "easily erodible" dams.  Von Thun and Gillette's paper states: "It is suggested that these limits be viewed as upper and lower bounds corresponding respectively to well-constructed dams of erosion resistant materials and poorly-constructed dams of easily eroded materials". 

**Xu and Zhang (2009):** In 2009 a paper was published by Dr.'sY. Xu and L.M. Zhang in the Journal of Geotechnical and Geo-Environmental Engineering.   The database gathered by Dr.'s Xu and Zang contained 182 earth and rockfill dams from the United States and China, with nearly 50 percent of the dams greater than 15 meters in height.  However, their final equations are based on a much smaller subset of these dams due to missing data.  Their paper shows details for 75 dams that were comprised of homogeneous earth fill, zoned-filled, dams with corewalls, and concrete faced dams.  Their final equation for the average breach width is based on 45 dam failures, and their equation for the time of failure is based on only 28 dam 

20 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

failures.  The data that Xu and Zhang used for their regression analysis had the following ranges: 

- **Height of the dams:** 3.2 – 92.96 meters (10 – 305 feet) (with 78% < 30 meters,  and 58% < 15 meters) 

- **Volume of water at breach time:** 0.105 – 660.0 m<sup>3</sup> x 10<sup>6</sup> (11.3 - 535,000 acre-feet) (with 80% < 25.0 m<sup>3</sup> x 10<sup>6</sup> , and 67% < 15.0 m<sup>3</sup> x 10<sup>6</sup> ) 

Xu and Zhang’s regression equation for average breach width is: 



where: 

- Bave = average breach width (meters) 

- Vw = reservoir volume at time of failure (cubic meters) 

- hb = height of the final breach (meters) 

- hd = height of the Dam (meters) 

- hr = fifteen meters, is considered to be a reference height for distinguishing large dams from small dams 

- hw = height of the water above the breach bottom elevation at time of breach (meters) 

- B3 = b3+b4+b5 coefficient that is a function of dam properties 

- b3 = -0.041, 0.026, and -0.226 for dams with corewalls, concrete faced dams, and homogeneous/zoned-fill dams, respectively 

- b4 

   - = 0.149 and -0.389 for overtopping and seepage/piping, respectively. 

- b5 = 0.291, -0.14, and -0.391 for high, medium, and low dam erodibility, respectively 

**Height of the Breach (hb).** While Xu and Zhang present an equation for the height of the breach (hb), the coefficient of determination, R<sup>2</sup> was only 0.35 for their best equation.  This is a very poor correlation, and therefore it is suggested to assume the breach height goes from the top of the dam all the way down to the natural ground elevation at the breach location (i.e., set hb = hd).  Additionally, Xu and Zhang's equation for breach height can produce breach heights greater than the height of the dam, which implies a scour hole forming.  While this can happen, it is not appropriate to use this as the breach height in a model like HEC-RAS, as it is applying the weir equation to the full breach shape.  If the scour hole is included in the breach height, you would over predict the outflow out of the dam, as the middle of the scour hole is not the hydraulic control for water leaving the dam, and thus too large of a flow area would be used in the computations. 

The Xu and Zhang paper does not provide estimates for side slopes directly.  Instead, they provide an equation to estimate the top width of the breach, which can then be used with the average breach width, to compute the corresponding side slopes.  Here is their equation for the breach top width: 

21 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



###### where: 

- Bt = breach top width (meters) 

- B2 = b3+b4+b5 coefficient that is a function of dam properties 

- b3 = 0.061, 0.088, and -0.089 for dams with corewalls, concrete faced dams, and homogeneous/zoned-fill dams, respectively. 

- b4 = 0.299 and -0.239 for overtopping and seepage/piping, respectively. 

- b5 = 0.411, -0.062, and -0.289 for high, medium, and low dam erodibility, respectively. 

Breach side slopes can be computed with the following equation: 



**Important Note:** Xu and Zhang data used in the development of the equation for breach development time include s more of the initial erosion period and post erosion period than what is generally used in HEC-RAS for the critical breach development time.  In general, this equation will produce breach development times that are greater than the other four equations described above.  Because of this fact, the Xu and Zhang equation for breach development time should not be used in HEC-RAS.  However, it is shown here for completeness of their method: 



###### where: 

- Tf = breach formation time (hours) 

- Tr = 1 hour (unit duration) 

- Vw = reservoir volume at time of failure (cubic meters) 

- hd = height of the dam (meters) 

- hr = fifteen meters, which is considered to be a reference height for distinguishing large dams from small dams 

- hw = height of the water above the breach bottom elevation at time of breach (meters) 

- B5 = b3+b4+b5 coefficient that is a function of dam properties 

- b3 = -0.327, -0.674, and -0.189 for dams with corewalls, concrete faced dams, and homogeneous/zoned-fill dams, respectively 

- b4 = -0.579 and -0.611 for overtopping and seepage/piping, respectively 

- b5 = -1.205, -0.564, and 0.579 for high, medium, and low dam erodibility, respectively 

22 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

###### **Simplified Physical Breaching Method** 

The **Simplified Physical** breaching method in HEC-RAS allows the user to enter velocity versus breach down-cutting and breach widening relationships, which are then used dynamically to figure out the breach progression versus the actual velocity being computed through the breach, on a time step by time step basis.  The main data requirement differences between this method and the "User Entered Data" breach method are the following: 

**_Max Possible Bottom Width_** - This field is now used to enter a maximum possible breach bottom width.  This does not mean this will be the final breach bottom width; it is really being used to limit the breach bottom width growth to this amount.  The actual bottom width will be dependent on the velocity verses erosion rate data entered, and the hydraulics of flow through the breach.  This field is used to prevent breaches from growing larger than this user set upper limit during the run. 

**_Min Possible Bottom Elev_** - This field is used to put a limit on how far down the breach can erode during the breaching process.  This is not necessarily the final breach bottom elevation; it is a user entered limiter (i.e., the breach cannot go below this elevation).  The final breach elevation will be dependent on the velocity verses erosion rate data entered, and the hydraulics of flow through the breach. 

**_Starting Notch Width or Initial Piping Diameter_** - If the overtopping failure mode is selected, the user will be asked to enter a starting notch width.  The software will use this width at the top of the dam to compute a velocity, from the velocity it will get a down cutting erosion rate (based on user entered data), which will be used to start the erosion process.  If a piping failure model is selected, the user must enter an initial piping diameter.  Once the breach is triggered to start, the initial breach hole will show up immediately.  A velocity will be computed through it, and then the down cutting and widening process will begin based on user entered erosion rate data. 

**_Mass Wasting Feature_** - This option allows the user to put a hole in the dam or the levee at the beginning of the breach, in a very short amount of time.  This option would probably most often be used in a levee evaluation, in which a section of the levee may give way (Mass Wasting), then that initial hole would continue to erode and widen based on the erosion process.  The required data for this option is a width for the mass wasting hole; duration in hours that the mass wasting occurs over (this would normally be a short amount of time); and, finally the bottom elevation of the initial mass wasting hole (it is assumed that the hole is open all the way to the top of the levee or dam if this option is used). 

**Velocity versus. Downcutting and Widening Erosion Rates -** When using the **Simplified Physical** breaching option, the user is required to enter "Overtopping Downcutting" (velocity vs. downcutting erosion rates), as well as "Widening Relationship" (velocity vs. erosion widening rates).  An example of the required data input for this method is shown in Figure 9. 

As shown in Figure 9, the user is required to enter "Overtopping Downcutting " and " Widening Relationship".  This data is often very difficult to come by.  Users will need to consult with geo-technical engineers to come up with reasonable estimates of this data for a 

23 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 9.** HEC-RAS Simplified Physical Breach Option 

simulating a historic levee or dam breach, and adjusting the velocity versus erosion rate data until the model simulates the correct breach width and time.  This is obviously an iterative process, and may require the user to perform this at multiple locations to see if there is a consistent set or erosion rates that will provide a reasonable model for simulating levee breaches (or dams) in your geographical area.   We realize that this data is not readily available for any specific levee or dam.  The hope is that over time we will be able to develop guidelines for these erosion rates based on analyzing historical levee and dam breaches. 

###### **Physically-Based Breach Computer Models** 

Several computer models have been developed that attempt to model the breach process using sediment transport theories, soil slope stability, and hydraulics.  Mr. Wahl summarized some of these models in his report (Wahl, 1998).  A table from Wahl's (1998) report, which summarizes the physically based computer models he reviewed, is shown in Table 4. 

In general, all of the models listed in Table 4 rely on the use of bed-load sediment transport equations, which were developed for riverine sediment transport processes.  The use of these models should be viewed as an additional way of "estimating" the breach dimensions and breach development time. 

Of all the models listed in Table 4, the BREACH model developed by Dr. Danny Fread (1988) has been used the most for estimating dam breach parameters.  Dr. Fread's model can be used for constructed earthen dams as well as landslide formed dams.  The model can handle forming breaches from either overtopping or piping/seepage failure modes.  The software uses weir and orifice equations for the hydraulic computation of flow rates.  The Meyer-Peter and Muller sediment transport equation is used to compute transport capacity of the breach flow.  Breach 

24 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

**Table 4** .  Physically-Based Embankment Dam Breach Computer Models 

|**Model and Year**|**Sediment**<br>**Transport**|**Breach**<br>**Morphology**|**Parameters**|**Other**<br>**Features**|
|---|---|---|---|---|
|Cristofano (1965)|Empirical formula|Constant breach<br>width|Angle of repose,<br>others||
|Harris and Wagner<br>(1967)<br>BRDAM (Brown<br>and Rogers,1977)|Schoklitsch<br>formula|Parabolic breach<br>shape|Breach<br>dimensions,<br>sediments||
|Lou (1981);<br>Ponce and<br>Tsivoglou (1981)|Meyer-Peter and<br>Müller formula|Regime type<br>relation|Critical shear<br>stress, sediment|Tailwater effects|
|BREACH (Fread,<br>1988)|Meyer-Peter and<br>Müller modified by<br>Smart|Rectangular,<br>triangular, or<br>trapezoidal|Critical shear,<br>sediment|Tailwater effects,<br>dry slope stability|
|BEED (Singh and<br>Scarlatos, 1985)|Einstein Brown<br>formula|Rectangular or<br>trapezoidal|Sediments, others|Tailwater effects,<br>saturated slope<br>stability|
|FLOW SIM 1 and<br>FLOW SIM 2<br>(Bodine, undated)|Linear<br>predetermined<br>erosion;<br>Schoklitsch<br>formula option|Rectangular,<br>triangular, or<br>trapezoidal|Breach<br>dimensions,<br>sediments||



enlargement is governed by the rate of erosion, as well as the collapse of material from slope failures.  Dr. Fread's model can handle up to three material layers (inner core, outer portion of the dam, and a thin layer along the downstream face).  The material properties that must be described are: internal friction angle; cohesive strength, grain size of the material (D50), unit weight, porosity, ratio of D90 to D30, and Manning's _n_ .  This software has been tested on a limited number of data sets, but has produced reasonable results. 

Additional research on the erosion process of earthen embankments that are overtopped is being conducted in the United States as well as Europe.  The Agricultural Research Service (ARS) has been testing earthen embankment failures at sizes ranging from small scale laboratory models to near prototype scale dams (up to seven feet high) for several years (Hanson, et al., 2003; Hassan, et al., 2004).  Similar tests have been performed in Norway for earthen dams, five to six meters high, constructed of rock, clay, and glacial moraine (Vaskinn, et al., 2004).  The hope is that this research work will lead to the development of improved computer models of the breach process. A dam safety interest group made up of U.S. Government agencies (USBR, ARS, USACE), private industry, and Canadian and European research partners is currently evaluating new technologies for simulating the breach process.  The goal of this effort is to develop computer simulation software that can model the dam breach process by progressive erosion for earthen dams initiated by either overtopping flow or seepage. Computer models that are currently being evaluated are: WinDAM (Temple, et al., 2006); HR-BREACH (Mohammed, 2002); and FIREBIRD (Wang and Kahawita, 2006).  Table 5 provides a summary of these models capabilities (Wahl, 2009): 

25 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

**Table 5.** Summary of Erosion Process Models Currently Under Development 

|**Model**<br>**and**<br>**Year**|**Embankment**<br>**Types**|**Failure**<br>**Modes**|**Erosion Processes**|
|---|---|---|---|
|WinDAM|Homogeneous with<br>varying levels of<br>cohesiveness|Overtopping|Headcut formation on downstream face,<br>deepening, and upstream advancement;<br>lateralwidening|
|HR-BREACH|Homogeneous cohesive,<br>or simple composite<br>embankments with<br>noncohesive zones,<br>surface protection<br>(grass or rock), and<br>cohesive cores|Overtopping<br>Piping|Variety of sediment transport/erosion<br>equations and multiple methods of<br>application. Discrete breach growth using<br>bending, shear, sliding and overturning<br>failure of soil masses.|
|FIREBIRD|Homogeneous cohesive<br>or noncohesive|Overtopping|Coupled equations for hydraulics and<br>sediment transport.|



##### **Peak Flow Equations and Envelope Curves** 

Several researchers have developed peak flow regression equations from historic dam failure data.  The peak flow equations were derived from data for earthen, zoned earthen, earthen with impervious core (i.e., clay, concrete, etc.) and rockfill dams only, and do not apply to concrete dams.  In general, the peak flow equations should be used for comparison purposes. 

Once a breach hydrograph is computed in HEC-RAS, the computed peak flow from the model can be compared to these regression equations as a test for reasonableness.  However, one should use great caution when comparing results from these equations to model predictions.  First, the user should go back to the original paper for each equation and evaluate the data sets and assumptions that were used to develop that equation.  Many of the equations were developed from limited data sets, and most were for smaller dams.  Also, when using these equations to compare against model results, the event being studied can have a significant impact on the model results peak flow.  For example, studies being performed with PMF inflows may have larger computed peak outflows than what will be predicted by some of the peak flow equations. This is due to the fact that none of the historic data sets were experiencing a PMF level flood when they failed. 

Shown below is a summary of some of the peak flow equations (all equations are in metric form) that have been developed from historic dam failures: 

 **USBR (1982):** Q = 19.1(hw)<sup>1.85</sup> (envelope equation) 





26 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

- **Xu and Zhang (2009):** 



- **Kirkpatrick (1977):** Q = 1.268(hw+0.3)<sup>1.24</sup> 

      - 1.85 

- **Soil Conservation Service (SCS,1981):** Q=16.6hw 

- **Hagen (1982):** Q=0.54(S hd)<sup>0.5</sup> 

- **Singh & Snorrason (1984):** Q = 13.4(hd)<sup>1.89</sup> Q = 1.776(S)<sup>0.47</sup> 

- **Costa (1985)** : 

   - Q = 1.122(S)<sup>0.57</sup> Q = 0.981(S hd)<sup>0.42</sup> Q = 2.634(S hd)<sup>0.44</sup> (envelope equation) 

- **Evans (1986):** Q = 0.72Vw0.53 

- **Walder and O'Connor (1997):** Q estimated by computational and graphical method using relative erodibility of dam and volume of reservoir. 

where: 

- Q = peak breach outflow (cubic meters per second) 

- hw = depth of water above the breach invert at time of breach (meters) 

- Vw = volume of water above breach invert at time of failure (cubic meters) 

- S = reservoir storage for water surface elevation at breach time (cubic meters) 

- hd = height of dam (meters) 

- hr = fifteen meters, which is considered to be a reference height for distinguishing large dams from small dams. 

- B4 = b3+b4+b5 coefficients that are a function of dam properties 

- b3 = -0.503, -0.591, and -0.649 for dams with corewalls, concrete faced dams, and homogeneous/zoned-fill dams, respectively 

- b4 = -0.705 and -1.039 for overtopping and seepage/piping, respectively 

- b5 

- = -0.007, -0.375, and -1.362 for high, medium, and low dam erodibility, respectively 

In addition to the peak flow equations, one can also compare computed model peak outflows to envelope curves of historic failures.  One such curve is shown in Figure 10 (HEC, 1980). 

When comparing computed results to the envelope curve shown in Figure 9, keep in mind that this envelope curve was developed from only fourteen data sets, and may not be a true upper bound of peak flow versus hydraulic depth. 

27 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 10.** Envelope of Experienced Outflow Rates from Breached Dams 

##### **Site Specific Data and Engineering Analysis** 

Site specific information about the dam should always be collected and evaluated.  Site specific information that may be useful in this type of analysis includes: materials/soil properties used in building the dam; if the dam includes an impervious core/filter or not; material used for impervious core/filter; embankment protection materials (rock, concrete, grass, etc.); embankment slopes of the dam; historic seepage information; known foundation or abutment problems; known problems/issues with gates and spillways; etc. 

Whenever possible a geo-technical analysis of the dam should be performed.  Geo-technical evaluations can be useful in the selection of dam breach parameters.  Specifically, geotechnical analyses can be used to estimate appropriate breach side slopes based on soil material properties. Additionally, a geo-technical analysis can be used to make a qualitative assessment of the breach parameters estimated by the various methods described above (historic comparisons, regression equations, and physically based model results). 

Consideration of structural features such as spillway gates should also be considered for determination of the appropriate breach geometry for failure modes involving gate malfunction, blockage, or loss of the structure. 

28 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

##### **Recommended Approach** 

In general, several methods should be used to predict a range of breach sizes and failure times for each failure mode/hydrologic event.  It is recommended that the modeler select several regression equations to estimate breach parameter values.  Care must be taken when selecting regression equations, such that the equations are appropriate for the dam being investigated. Regression equations that have been used for earthen, zoned earth, earth with a clay core, and rockfill dams are: Froehlich (1995a), Froehlich (2008), MacDonald and Langridge-Monopolis (1984), Von Thun and Gillette (1990), and Xu and Zhang (2009).  If the dam under investigation is outside the range of data used in the development of the regression equations, resulting breach parameter estimates should be scrutinized closely for reasonableness. **Note:** Never mix and match breach parameters from multiple regression equations.  In other words, use the average breach width and time of failure from the same equation set.  Do not use a breach width from one equation set and a time of failure from another.  The breach widths and times are interrelated, as they are derived from a specific data set. 

In addition to the regression equations, physically based computer models should also be utilized if appropriate for the level of study (NWS-BREACH, WinDAM, and HR-BREACH models are currently recommended).  Whenever possible, geotechnical analyses of the dam should be used to assist in estimating the breach parameters (i.e., side slopes of the breach), or at least used as a qualitative assessment of the estimates.  Additionally, breach parameter estimates should be compared to the government agency ranges provided in Table 3.  If values are outside the recommended ranges, those estimates may need to be adjusted, unless there is compelling physical evidence that the values are appropriate.  This will lead to a range of values for the breach size and failure times.  A sensitivity analysis of breach parameters and times should be performed by running all of the parameter estimates within a HEC-RAS model. 

Each set of breach parameters and failure times will produce a different outflow hydrograph. However, once these hydrographs are routed downstream, they will tend to converge towards each other.  There are two main reasons for this convergence:  (1) the total volume of water in each of the different hydrographs is basically the same (being the stored water behind the dam at the time of failure, plus whatever inflow occurs); (2) as the hydrographs move downstream, a sharp hydrograph will attenuate much more quickly than a flat hydrograph.  Hydrographs from different assumed breach parameters can converge to produce similar peak flow and stage in a surprisingly short distance.  An example flow versus time plot from a study performed with HEC-RAS is shown in Figure 11.  However these differences could be huge for loss-of-life calculations if a population at risk is immediately downstream of the dam. 

In the example shown in Figure 10, three different sets of breach parameters were used for the same model.  The hydrographs coming out of the dam are very different in magnitude of peak flow, but they have the same volume of water.  In this example, as the hydrographs move downstream they have substantially converged within four miles and are almost the same peak flow by River Mile 10.  The rate at which the hydrographs will converge is dependent on many factors: steepness in the rise of the outflow hydrograph, volume of the outflow hydrograph, slope of the downstream reach, roughness of the downstream reach, available storage in the downstream floodplain, etc.  The user will need to route all of the breach outflow hydrographs 

29 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 11.** Dam Break Flood Wave Progression Downstream 

downstream through the entire study area in order to fully evaluate the affect of the breach parameters on the resulting flood hydrographs and inundation levels. 

For a risk assessment study, the user must select the set of breach parameters that are considered to be most likely for each event/pool elevation.  This will require engineering judgment.  If all of the breach estimates, for a given event/pool elevation, end up converging to the same flow and stage before getting to any population at risk and potential damage areas, then the selection of a final set of breach parameters should not affect the computations and a simple mean value should be used.  However, if the various sets of breach parameters produce significantly different flow and stage values at downstream locations (population at risk locations and potential damage zones), then engineering judgment will need to be used to pick a set of values that are considered most likely.  Conservatively high or low values should not be used, as this will bias the overall results. 

Once a final set of breach parameters is selected for a given event/failure mode, the computed peak outflow from the breach can be compared to some of the peak flow equations as a check of reasonableness.  Keep in mind the limitations of the peak flow equations, as discussed in the **Peak Flow Regression Equations** section (see page 26). 

Another check for reasonableness should be done by evaluating the breach flow and velocities through the breach, during the breach formation process.  This can be accomplished by reviewing the detailed output for the inline structure (dam) and reviewing the flow rate and velocities going through the breach.  This output is provided on the HEC-RAS detailed output table for the inline structure.  There are two things to check for here: 

- 1) if the model reaches the full breach development time and size, and there are still very high flow rates and velocities going through the breach, this is a sign that either the 

30 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

breach is too small, or the development time is to short (unless there are some physical constraints limiting the size of the breach); 

- 2) if the flow rate and the velocities through the breach become very small before the breach has reached its full size and development time, then this is an indicator that the breach size may be too large, or the breach time may be too long. 

Additional factors affecting this could be the breach progression curve and the hydraulic coefficients (weir and piping) used.  When you get into the situation described above in either Scenario 1 or 2, the breach size and development time should be re-evaluated to improve the estimates for that particular structure. 

The level of effort in estimating breach parameters should be consistent with the type of risk assessment.  In general, the level of effort and detail will increase from Type 1 (Low Hazard Potential) through Type 3 (High Hazard Potential).  For Type 1 analyses a basic estimate of breach parameters consistent with the range of values in Table 3 could be appropriate.  Type 2 (Significant Hazard Potential) and Type 3 analyses will typically require a greater level of detail and accuracy incorporating most if not all of the methods are provided in this section. 

##### **Example Application** 

In order to demonstrate how to estimate breach parameters, an example application for a fictitious dam is provided below.  The event being evaluated in the example is a PMF scale event.  This same process needs to be performed for each failure mode/event (fully modeled hydrologic event or pool elevation for sunny day failures).  The following is the necessary information required about a dam in order to develop breach parameter estimates as outlined in these guidelines. 

###### **Reservoir Data** 

|**Important Pool Elevations**|**Elevation**<br>(meters)|**Volume**<br>(m<sup>3</sup>)|
|---|---|---|
|Stream Bed|1678.0|0.0<br>|
|MultipurposePool|1692.1|15.81x10<sup>~~6~~</sup>|
|Top of Flood Control|1710.0|151.64x10<sup>~~6~~</sup><br>|
|Top of Dam|1720.9|327.01x10<sup>~~6~~</sup><br>|
|PMF Max Water Surface|1722.26|357.98x10<sup>~~6~~</sup>|



###### **Dam Embankment Data** 

Crest Length: 4360 meters Crest Width: 9.15 meters Maximum Height above river bed: 42.9 meters Average Upstream Embankment slope: 3.3H:1V Average Downstream Embankment slope: 3.3H:1V Embankment Material: Rolled earth, zoned Embankment Core: Impervious core, clay 

31 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Upstream slope Protection: 18" riprap Downstream slope protection: Topsoil and grass 

###### **Regression Equations** 

For this example, the Froehlich (1995a), Froehlich (2008), MacDonald and LangridgeMonopolis (1984), Von Thun and Gillette (1990), and Xu and Zhang (2009) regression equations for predicting breach size and development time were used.  This dam is within the range of the data used to develop these regression equations, therefore the equations are considered to be an appropriate methodology for estimating the breach parameters.  During the PMF event for this dam it is overtopped by 1.36 meters.  The mode of failure for this example will be assumed as an overtopping failure.  The failure location is assumed to be at the main channel centerline.  The breach bottom elevation is assumed to be at an elevation of 1,678 meters (invert of the main channel).  The water surface elevation at the initiation of the breach will be at an elevation of 1,722.26 meters (maximum pool for PMF event).  The following are the calculations for each method. 

###### **Froehlich (1995a):** 

Bave = 0.1803 Ko Vw0.32 hb0.19 Bave = 0.1803 (1.4) (357.98x10<sup>6</sup> )<sup>0.32</sup> (42.9)<sup>0.19</sup> **Bave = 281.5** meters tf = 0.00254 Vw0.53 hb-0.90 tf = 0.00254 (357.98x10<sup>6</sup> )<sup>0.53</sup> (42.9)<sup>-0.90</sup> **tf = 2.95** hours 

The Froehlich (1995a) method assumes a side slope of 1.4H:1V for an overtopping breach. Given the breach height of 42.9 meters, this yields a bottom width for the breach of **Wb = 221.4** meters. 

###### **Froehlich (2008):** 

Bave = 0.27 Ko Vw0.32 hb0.04 Bave = 0.27 (1.3) (357.98x10<sup>6</sup> )<sup>0.32</sup> (42.9)<sup>0.04</sup> **Bave =  222.76** meters 

tf = 63.2 ( Vw /(ghb2))0.5 tf = 63.2 (357.98x10<sup>6</sup> /(9.80665 x (42.9)<sup>2</sup> ))<sup>0.5</sup> **tf = 2.47** hours 

The Froehlich (2008) method assumes a side slope of 1.0H:1V for an overtopping breach. Given the breach height of 42.9 meters, this yields a bottom width for the breach of **Wb = 179.86** meters. 

**MacDonald and Langridge-Monopolis (1984):** The MacDonald and Langridge-Monopolis equation for an earthfill dam with a clay core is: 

32 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Veroded = 0.00348 (Vout * hw)<sup>0.852</sup> 

Since the outflow volume through the breach is unknown before performing the analysis, a good starting estimate is the volume of water in the dam at the peak stage of the event. 

Veroded = 0.00348 (357.98x10<sup>6</sup> * 44.26 )<sup>0.852</sup> Veroded = 1.70556x10<sup>6</sup> cubic meters of material 

To compute the bottom width of the breach, the method says to use side slopes of 0.5H:1V. The user must also estimate an average side slope for both the upstream and downstream embankment of the dam.  For this example average side slopes of 3.3H:1V were used for both upstream and downstream.  The bottom width equation (State of Washington, 1992) is: 



where: 

Wb = (1.70556x10<sup>6</sup> – 42.9<sup>2</sup> (9.15*0.5 + 42.9*0.5*6.6/3))/(42.9(9.15 + 42.9*6.6/2)) **Wb = 249.0** meters tf = 0.0179 (Veroded)<sup>0.364</sup> tf = 0.0179 (1.70556x10<sup>6</sup> )<sup>0.364</sup> **tf = 3.32** hours 

**Note:** Once an actual breach hydrograph is computed with the MacDonald and LangridgeMonopolis parameters, the volume of water coming out of the breach should be calculated, and the parameters should be re-estimated using that volume of water for Vout. 

**Von Thun and Gillette (1990):** The Von Thun and Gillette equation for the breach average width is: 

Bave = 2.5 * hw + Cb Bave = 2.5 * 44.26 + 54.9 **Bave = 165.6 m** 

Von Thun and Gillette suggest using breach side slopes of 0.5H:1V for earthen dams with a clay core.  Given the dam height of 42.9 meter, the Breach bottom width will be **Wb = 144.2** meters **.** 

Von Thun and Gillette show two equations for predicting the breach failure time.  One equation is a function of the depth of water only, while the other is a function of depth of water and the computed average breach width.  Both equations are used below. 

tf = 0.02 * hw + 0.25 tf = Bave/(4*hw) tf = 0.02 * 44.26 + 0.25 tf = 166/(4*44.26) tf = 1.14 hours tf = 0.94 hours 

33 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Both of the Von Thun and Gillette equations yield similar answers for the breach time. Reviewing the Von Thun and Gillette paper showed that the data they used in their experiments were mostly earthen embankments with slightly cohesive materials.  Given that the example dam we are studying has an engineered clay core, the longer time estimate is probably more appropriate.  Therefore the selected failure time is **tf = 1.14** hours **.** 

**Xu and Zhang (2009):** <u>The Xu and Zhang equation for the breach average width is:</u> 



Bave = (42.9)(0.787)(42.9/15)<sup>0.133</sup> ((357.98x10<sup>6</sup> )<sup>1/3</sup> /44.26)<sup>0.652</sup> e<sup>-0.283</sup> **Bave = 178.67** meters 



Bt = (42.9)(1.062)(42.9/15)<sup>0.092</sup> ((357.98x10<sup>6</sup> )<sup>1/3</sup> /44.26)<sup>0.508</sup> e<sup>0.071</sup> **Bt = 220.64** meters 

Based on the computation of Bave and Bt abobe, the breach bottom width for this method is **Wb = 136.7** and the side slopes are **Z = 0.98H:1V.** 

The breach development time from the Xu Zhang equation is as follows: 



Tf = (1.0)(0.304)(42.9/15)<sup>0.707</sup> ((357.98x10<sup>6</sup> )<sup>1/3</sup> /44.26)<sup>1.228</sup> e<sup>-0.327</sup> **Tf = 13.92** hours* 

- ***Note:** Please see note about the Xu Zhang method over estimating the breach time under the method description above. 

###### **Physically-Based Breach Computer Models** 

For this example, only Dr. Fread's NWS-BREACH model was run to make an estimate of breach parameters from a physically based computer model.  The physical dimensions of the dam, the soil properties, and the hydrologic event data were entered into the BREACH model.  The results from the BREACH model for this example are: 

Breach Bottom Width Wb 238 meter Breach side slopes 0.9H:1V Breach Failure Time tf 4.2 hours 

34 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

###### **Summary Results for Breach Parameters** 

Shown in Table 6 is a summary of the breach parameters computed from the regression equations and the NWS-BREACH model. 

**Table 6.** Summary of Breach Parameter Estimates 

|**Method**|**Breach**<br>**Bottom**<br>**Width**<br>(meters)|**Breach**<br>**Side**<br>**Slopes**<br>(H:1V)|**Breach**<br>**Failure**<br>**Time**<br>(hours)|
|---|---|---|---|
|Froehlich(1995a)|221.4|1.40|2.95|
|Froehlich(2008)|179.9|1.00|2.47|
|MacDonald and Langridge-Monopolis|253.0|0.50|3.32|
|Von Thun and Gillette|144.2|0.50|1.14|
|Xu and Zhang (2009)|136.7|0.98|13.92*|
|NWS-BREACH Computer Model|238.0|0.90|4.2|



***Note:** the data Xu and Zhang used in the development of their equation for breach development time includes more of the initial erosion period and post erosion period than what is generally used in HEC-RAS for the critical breach development time.  In general, this equation will produce breach development times that are greater than the other four equations described above.  Because of this fact, the Xu Zhang equation for breach development time should not be used in HEC-RAS. 

From here, all six sets of parameters should be entered into the HEC-RAS software and run as separate breach plans.  This will result in six different breach outflow hydrographs.  However, once the hydrographs are routed downstream, they will begin to converge towards each other. The selection of a final set of breach parameters for this event should be based on guidance provided in the **Recommended Approach** section (see page 29). 

#### **Downstream Flood Routing/Modeling Issues** 

The modeling of a dam break flood wave is one of the most difficult unsteady flow problems to solve.  Previous discussions in this document have focused on modeling the reservoir pool, the dam itself, and estimating breach parameters to be used in computing the breach outflow hydrograph.  However, the most difficult part of performing a dam safety study is routing the dam break flood wave downstream. 

Within HEC-RAS, the user can model the downstream area in the following manner: as a combination of one-dimensional streams and storage areas; a combination of one-dimensional streams, storage areas, and two-dimensional flow areas; or as a single two-dimensional flow area.  There are many things that the hydraulic modeler must consider to get an accurate estimate of the downstream flood stages and flows.  The following is a list of things that should be considered when developing an unsteady flow model for a dam break application.  Most of these issues are concerns for one-dimensional river reach modeling with cross sections. 

- Cross Section Spacing and Hydraulic Properties 

- Computational Time Step 

- Manning's Roughness Coefficients 

- Downstream Storage, Tributaries, and Levees 

- Modeling Bridge and Culvert Crossings 

- Modeling Steep Streams 

35 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

- Drops in the bed Profile 

- Initial Conditions (low flow) 

- Downstream Boundary Conditions 

##### **Cross Section Spacing and Hydraulic Properties** 

Cross-sectional cut lines should be created to capture the entire extent of flooding anticipated by the dam break scenario.  As in any hydraulic modeling study, cross sections must be laid out to accurately describe the channel and floodplain geometry.  Cross sections are laid out perpendicular to the anticipated flow lines of both the channel and the floodplain, during high flow conditions.  There must be enough cross sections to describe: contractions and expansions of the channel and/or floodplain; changes in bed slope; changes in roughness; and significant changes in discharge.  Cross sections also need to be added immediately upstream and downstream of:  tributary inflow locations; dams and other inline structures (weirs, drop structures, or natural drops in the bed profile); bridge and culvert crossings; levees and other types of lateral hydraulic structures.  An example of a cross section layout is shown in Figure 12. 



**Figure 12.** Example Cross Section Layout (Ackerman, 2014) 

In addition to describing the physical changes and hydraulic structures within the channel and floodplain, there are also numerical considerations for adding or removing cross sections. 

**Cross Sections Spaced To Far Apart.** In general, cross sections spaced too far apart will cause additional numerical diffusion of the floodwave, due to the derivatives with respect to distance being averaged over to long of a distance. See an example of artificial numerical diffusion in Figure 13.  Figure 13 shows an upstream inflow hydrograph and two downstream hydrographs after they have been routed through the river system.  In this example, the channel is a rectangular channel on a constant slope, with a constant Manning's roughness.  The only change in the example is the cross section spacing. 

36 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 13.** Numerical Error Due to Cross Section Spacing 

Additionally, when cross sections are spaced far apart, and the changes in hydraulic properties are great, the solution can become unstable.   Instability can occur when the distance between cross sections is so great, such that the Courant number becomes much greater than 1.0, and numerical errors grow to the point of the model becoming unstable.  Another way to say this is that the cross section spacing is not commensurate with the hydrograph being routed and the computational time step being used (i.e., the cross section spacing is much further than the flood wave can travel within the computational time step being used). 

**Maximum Cross Section Spacing.** A good starting point for estimating maximum cross section spacing  are two empirically derived equations by Dr. Danny Fread (Fread, 1993) and P.G. Samuels (Samuels, 1989).  These two equations represent very different methods for coming up with spacing.  Samuels' equation implies that smaller streams and steeper streams will require tighter cross section spacing.  In general, Samuels' equation was derived for typical flood studies, in which the modeler is developing a steady state model for a typical floodplain study of the twoyear through 100 year events.  For dam break flood studies, Samuels' equation may be too strict, in that it requires much tighter cross section spacing than needed.  Samuels' equation is as follows: 



where: 

- ∆x = the cross section spacing distance (feet) 

- D 

   - = the average main channel bankfull depth (feet) 

- S0 = the bed slope (feet/feet) 

**Note:** Samuels' equation was derived from data with slopes ranging from two to fifty feet/miles. 

Dr. Fread's equation implies smaller streams and steeper hydrographs will require tighter cross sections.  Fread's equation is one set of three conditions he presented in his paper for determining spacing.  The equation is a theoretical derivation of spacing based on the inherent numerical 

37 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

errors involved with linearizing the St. Venant Equations into a four-point implicit finitedifference scheme.  The other two involve a check of the change in cross sectional area from one cross section to the next, and the other accounts for changes in slope.  Consequently, the spacing determined by Fread’s equation may be too coarse, depending on the bed slope changes, the contraction and expansion characteristics and other non-linear data.  Dr. Fread's equation is as follows: 



where: 

- ∆x = the cross section spacing distance (feet) 

- C 

   - = the wave speed (feet per second) 

- Tr = time of rise (from low flow to peak) of the hydrograph (seconds) 

Samuels' and Dr. Fread's equations are rough estimates of cross section spacing - a good place to start.  However, over time and practice, the modeler should be able to determine a good first estimate based on experience. 

**Cross Sections Too Close Together.** If the cross sections are too close together, then the derivatives with respect to distance may be overestimated, especially on the rising side of the flood wave.  This can cause the leading edge of the flood wave to over steepen, to the point at which the model may become unstable.  An example of this is shown in Figure 14.  In this example, the only change made to the model was that cross sections were interpolated at very short intervals (five feet).  If it is necessary to have cross sections at such short intervals, then much smaller time steps will need to be used in order for the numerical computations to solve the equations over such short distances.  In general, for most dam break flood studies, cross sections should not be spaced at intervals closer than about 50 feet, unless you can use very small time steps (i.e., a few seconds or less).  However, cross sections can be placed at closer distances at hydraulic structures, such as bridges/culverts, dams, and inline weirs, due to the fact that the model does not solve the unsteady flow equations through these structures.  Rather it uses hydraulic equations specifically defined for those structures. 

##### **Computational Time Step** 

In the development of any unsteady flow model, stability and numerical accuracy can be improved by selecting a time step that satisfies the Courant Condition.  This is very important for a dam break model.  Too large a time step will cause numerical diffusion (attenuation of the peak) and possibly model instability.  Too small of a time step can lead to very long computation times, as well as possible model instability. 

**Too large of a time step** :  When the solution scheme solves the unsteady flow equations, derivatives are calculated with respect to distance and time.  If the changes in hydraulic properties at a given cross section are changing rapidly with respect to time, too large of a time step may cause over estimation (too steep) of the time based derivatives, causing the program to go unstable.  The solution to this problem in general is to decrease the time step.  Even if the program does not go unstable, too large of time steps will cause numerical attenuation of the hydrograph that is not physically related.  An example of a model with varying time steps is shown in Figure 15.  In this example, all things in the model were exactly identical, except one 

38 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 14.** Example Model Instability due to Very Short Cross Section Spacing 

run was done with a one minute time step (appropriate for this model), and the other was done with a ten minute time step (too large for this model).  As shown in Figure 15, the run with the ten minute time step has a ten percent lower peak flow, and the flood wave is much more spread out (diffused) than the run with the one minute time step. 

**Too Small of a Time Step.** If a time step is selected that is much smaller than what the Courant Condition would suggest for a given flood wave, then model runs times will be much longer than necessary, and this can also cause model stability problems.  In general to small of a time step will cause the leading edge of the flood wave to steepen, possible to the point of oscillating and going unstable.  Extremely small time steps (less than one second) can cause round off errors when storing numbers in the computer, which in turn can lead to numerical errors which can grow over time. 

**Time Step Selection.** As mentioned above, the best way to estimate a computational time step for HEC-RAS is to use the Courant Condition.  This is especially important for dam break flood studies.  The Courant Condition is the following: 



and therefore: 



39 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



<!-- Start of picture text -->
River: Test   Reach: 1   RS: 0<br>120000<br>Legend<br>10 min DT<br>1 min DT<br>100000<br>80000<br>60000<br>40000<br>20000<br>0<br>0200 0300 0400 0500 0600 0700 0800<br>01Jan2007<br>Time<br>Flow (cfs)<br><!-- End of picture text -->

**Figure 15.** Example of Varying Computational Time Step 

where: 

- C = courant number 

- ΔT = time step (seconds) 

- Δx = distance step in feet (average cross section spacing or two-dimensional cell size) Vw = wave speed (feet per second 

The flood wave speed is based on capturing the speed of the rising side of the flood wave as it propagates downstream.  Flood wave speed is most accurately calculated in the area of the initial rise of the flood wave, where there is the largest change in discharge with respect to the change in cross sectional area (this is the leading edge of the dam break flood wave).  The equation for calculating flood wave speed is: 



where: 

- Vw = flood wave speed (feet per second) 

- dQ = the change in discharge over a short time interval (Q2 – Q1) 

- dA = the change in cross section area over a short time interval (A2 – A1) 

**Note:** dQ/dA can be approximated by calculating the change in discharge and flow area at a single cross section over a single computational time step.  This should be done while the flood wave initial abrupt rise is occurring at that cross section. 

40 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

For practical applications of the Courant Condition, the user can take maximum average velocity from HEC-RAS and multiply it by 1.5, to get a rough estimate of flood wave speed in natural cross sections. 

For medium to large rivers the Courant Condition may yield time steps that are too restrictive (i.e., a larger time step could be used and still maintain accuracy and stability).  A practical time step can be estimated as: 



However, treat this estimate as an upper limit.  Remember that for dam break models, typical time steps are in the range of one to sixty seconds due to the short time of rise and very fast flood wave velocities. 

##### **Manning's Roughness Coefficients** 

Roughness coefficients represent the resistance to flow in channels and floodplains.  Roughness is usually presented in the form of a Manning's _n_ value in HEC-RAS.  There is extensive research and literature on methods to determine _n_ values; however most of this work is representative of only main channels and not floodplains.  Additionally, the literature on Manning's _n_ values is for historically experienced floods, which are much lower than the flood resulting from a dam break.  The actual selection of _n_ values to be used for each dam assessment will require judgment by the engineer responsible for hydraulic model development. 

A proper perspective is required before establishing a range of _n_ values to be used in USACE risk assessment studies.  The following general guidelines of factors that affect _n_ values should be considered in developing representative values. 

- **_Base Surface roughness_ :** Often represented by the size and shape of surface or channel and floodplain material that produces a friction effect on flow. 

- **_Stage and Discharge_ :** The _n_ value in most streams decreases with increase in stage and discharge. However, this is not always the case.  If the channel bed is of lesser roughness than the channel banks, then the composite channel _n_ values will increase with channel stage.  Once the stage gets higher than the main channel banks, the roughness coefficient could begin to decrease.  The main point here is that the variation of Manning's _n_ with stage is site specific. 

- **_Obstructions_ :** Objects constructed in the channel or in overbanks such as bridge piers or buildings can potentially cause increases in n value.  It is especially difficult to estimate Manning's roughness coefficients to represent buildings in the floodplain, as there are many factors to consider: the area obstructed and the density of the buildings, direction of the flow in relation to the layout of the structures, roughness of all of the other boundaries, slope of the terrain, velocities of the flow, etc. 

- **_Irregularities_ :** Variations in cross-section size and shape along the floodplain. Irregularities are often caused by natural constrictions and expansions, sand deposition 

41 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

and scour holes, ridges, projecting points and depressions, and holes and humps on the channel bed.  Gradual and uniform changes will generally not appreciably affect _n_ value. Whereas, areas that have lots of sharp channel irregularities will tend to have higher Manning's roughness coefficients. 

- **_Channel alignment_ :** Smooth curvature with large radius will generally not increase roughness values, whereas sharp curvature with severe meandering will increase the roughness. 

- **_Vegetation_ :** Dependent on height, density, distribution, and type of vegetation.  Heavily treed areas can have a significant affect for dam failures.  In general a lower average depth results in a higher _n_ value.  High velocities can potentially flatten the vegetation and lowering _n_ values. 

- **_Silting, Scouring, and Debris_ :** Silting may change a very irregular channel into a comparatively uniform one and decrease _n_ and scouring may do the reverse.  During a dam break flood wave, there will be a tremendous amount of scouring occurring, as well as lots of debris in the flow.  The increase sediment load and debris will cause the flow to bulk up (increase in stage).  One way to account for this increased sediment load and debris is to increase the Manning's _n_ values. 

The resulting maximum water surface profile associated with the failure of a dam will often be much higher than any historically observed flood profile.  In such cases, there is no historical based model data to calibrate to floods of this magnitude.  It is therefore incumbent upon the engineer to determine reasonable roughness coefficients for flows and stages that will be higher than ever experienced.  To gain a perspective on how each modeling parameter affects results, a bounding type sensitivity analysis can be performed regardless of the methods used to establish _n_ values. 

Historical regional knowledge of channels and floodplains should be used along with published guidelines in establishing a base level set of _n_ values.   Guidelines for establishing base level Manning's _n_ values can be found in Chapter 3 of the HEC-RAS Hydraulic Reference Manual (HEC, 2014a). The base level _n_ values should be adjusted up or down based on factors addressed previously. Calibration to the largest historical events of record should be done whenever possible.  Once adjusted roughness coefficients are established, uncertainty analyses should be performed by varying all values (two additional computational runs) by plus or minus twenty percent.  In general, channel _n_ values for risk assessment may be in the range of 0.025 to 0.075. The overbank _n_ values may range between 0.04 and 0.25.  Note that higher _n_ values can be used in areas to allow for storage embayments with little to no conveyance. 

**Manning's** **_n_ Values Immediately below Dam** .  Significant turbulence, sediment load and debris should be expected for the immediate reach downstream of a failed dam.   This is obvious when viewing the photo of the Teton Dam failure shown in Figure 16.  Because HEC-RAS does not directly account for high volumes of sediment in the flow, and the extreme turbulence in the water surface caused by the breach, it is often a good idea to increase the Manning's _n_ values just downstream of the dam.  The increased sediment and turbulence will cause higher water surfaces to occur.   The only way to mimic this is by increasing the roughness coefficients.  Proper 

42 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 16.** Significant Turbulence and Sediment Load during the Teton Dam Failure (Olsen, 1976) 

modification and variation of _n_ values is one of the many uncertainties in dam failure modeling. An accurate assessment can be confidently attained only after previous knowledge of a particular dam failure event.  A reasonable modeling approach may be to assume double the normal n value directly downstream of the dam and transition to normal roughness coefficients where failure induced turbulence, sediment load, and debris transport are expected to recede. 

**Roughness Coefficients for Steep Streams.** Many of our dams are located in mountainous regions, where the slopes of the stream are significantly steep. It is very common to underestimate Manning's n values for steep terrain.  Underestimation of the roughness coefficients can cause water surface elevations to be too low, increased velocities, and possibly even supercritical flow.  In addition to this, abrupt changes in n values or underestimation of n values can cause the model to go unstable.  Dr. Robert Jarrett (Jarrett, 1984) collected some extensive field data on steep streams (slopes greater than 0.002 feet/feet) in the Rocky Mountains.  Dr. Jarrett measured cross sectional shape, flow rates, and water surface elevations at 21 locations for a total of 75 events.  From this data Dr. Jarrett performed a regression analysis and developed an equation to estimate the Manning's roughness coefficient of the main channel. 

.038 − .016 _n_ = .039 _S R_ 

43 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

where: 

- n = Manning's roughness coefficient of the main channel 

   - S = energy slope (slope of the energy grade line, feet/feet) 

- R = hydraulic radius of the main channel (feet). 

While Dr. Jarrett's equation is not necessarily applicable to all locations, it is often a useful check for reasonableness of the Manning's _n_ values in steep terrain. 

##### **Downstream Storage, Tributaries, and Levees** 

Accounting for downstream storage in the floodplain below the dam is crucial in order to get a reasonable estimate of the flood wave propagation and attenuation as it moves downstream. General floodplain storage (areas that get wet but have little to no velocity) can often be modeled as part of the normal cross section by using ineffective flow areas.  If a portion of a cross section is wet, but it will have a very low velocity, high Manning's _n_ values are another approach to modeling that area of the cross section. 

**Modeling Tributaries.** Tributaries that come into the main river downstream may have flow reversals during the passing of the flood wave.  Significant size tributaries need to be accounted for, since they may represent a large amount of storage volume taken out of the flood wave. Further, the resultant inundation maps will need to include the flooding extent up the tributaries. These factors require scrutiny when developing geometric data for HEC-RAS and can be addressed in three different ways when laying out data for tributaries.  A tributary may be modeled using: (1) a separate one-dimensional river reach, (2) a two-dimensional flow area, (3) a storage area, or (4) an extension of the main river cross sections. 

The most comprehensive way to model the effects of a tributary to the main river is to model the tributary with one-dimensional cross sections or a two-dimensional flow area.  If the computed water surface along the tributary results in a sloped water surface, then modeling the tributary as a separate river reach is the preferred modeling method.  Tributaries that have significant inflows to the overall flood hydrograph are strong candidates to be modeled as separate one-dimensional reaches, or part of a two-dimensional flow area that is being used to model the downstream area. 

When adding a tributary to the main stem of a river, it is important to differentiate between the contributing area of the main stem cross sections versus the contributing area of the tributary cross sections.  At the stream junction, if flow from the two reaches will mix, a decision will need to be made as to the line that represents the separation point of the tributary and the main stem flows.  Cross sections from one reach should end just where the cross sections of the other reach begin, to insure complete inundation mapping.  Cross sections should not overlap.  Figure 17 depicts a tributary included in the model as a separate reach.  As shown in Figure 17, the user must identify the point at which to end the main stem cross sections and begin the tributary cross sections. 

The next best option for accounting for tributary storage is to model the tributary as a storage area, and connect the storage area to the main river with a lateral structure.  The lateral structure can be a weir, in which the weir geometry is represented with a cross section from the tributary. 

44 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 17.** Cross Section Layout for a Tributary Coming into a Main Stem River (Ackerman, 2014) 

This will allow water from the flood wave to back up and fill the storage area as a level pool of water.  An example of modeling tributaries with storage areas and lateral structures is shown in Figure 18. 

The third option is to extend the normal cross sections up into the tributary, and use ineffective flow areas for that portion of the cross sections.  This option is depicted in Figure 19. 

**Modeling Levees and Major Roads.** Downstream levees and major roads, that normally prevent water from getting into protected areas, must also be considered.  In general it is best to model the area behind the levees separately as a two-dimensional flow area, a storage area, a series of interconnected storage areas, or another routing reach.  The details of modeling an area behind a levee will depend on the terrain and details of the interior area.  A lateral structure (weir) should be used to model the top of the levees and major roads.  When using a Lateral structure to model a levee in HEC-RAS, this allows the model to evaluate levee overtopping, breaching, and the filling of the interior area separate from the main river and floodplain.  An example of modeling a levee and protected area with a single storage area is shown in Figure 20. 

If a levee or road is only a small obstruction to the flow, such that it will be completely overwhelmed during the routing of the dam break flood wave, then it may be better to model that 

45 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 18** . Example of Using Storage Areas and Lateral Weirs to Account for Flow Reversals up Tributaries (Ackerman, 2014) 



**Figure 19.** Tributary Storage Modeled as Cross Section Ineffective Flow Areas (Ackerman, 2014) 

46 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 20.** Example of Using Lateral Structures and a Storage Area to Model a Protected Area 

levee/road as part of the general cross sections.  This means using cross sections to model both the interior and exterior area around the levee, and using the HEC-RAS cross section levee option to keep flow in the river side of the levee until the levee is overtopped.  This should only be done for small levees/roads, in which the area behind these levees is not a significant area/storage volume.  An example of this type of modeling is shown in Figure 21. 

##### **Modeling Bridge and Culvert Crossings** 

Bridges and culvert crossings can often be a source of model instability problems in a dam break study.  Many downstream bridges will be overtopped, and may even be washed away.  If it is almost certain that a downstream bridge/culvert will be washed away, then it probably does not need to be included in the model.  Additionally, if a structure is so high above the stream that the water surface will not hit the low chord of the bridge deck (which may be the case for very large highway bridges that are far downstream from the dam), then that bridge will also not need to be modeled.  However, if the road embankment, and the bridge/culvert will cause a backwater (i.e., a significant rise in the water surface), then it should be included in order to obtain the correct stages upstream of the structure, and the increased storage behind the structure.  If the impact of the structure is unknown, then in general it should be modeled.  Then once the model is up and running, the structure could be evaluated for both its impact on the water surface and whether or not it is expected to remain in place due to the forces placed on it during the event. 

47 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



<!-- Start of picture text -->
High Ground<br><!-- End of picture text -->

**Figure 21.** High Ground (Road or Levee) Represented as Part of the Cross Sections 

Bridge/culvert crossings are a common source of model stability problems when performing a dam break analysis.  Many bridges will be overtopped during such an event.  Many of those bridges may in fact be washed out during such an event.  Common problems at bridges/culverts are the extreme rapid rise in stages when flow hits the low chord of the bridge deck or the top of the culvert.  Modelers need to check the computed family of rating curves closely and make sure they are reasonable.  One solution to this problem is to use smaller time steps, such that the rate of rise in the water surface is smaller for a given time step.  Modelers may also need to change hydraulic coefficients to get curves that have more reasonable transitions. 

Just as with cross sections, HEC-RAS pre-processes bridges/culverts into a family of rating curves.  Users must ensure that these curves go high enough to capture all possible water surface elevations and flows.  An additional source of instability can arise when the curves do not go high enough, and the program extrapolates from the last two points in the curve.  This extrapolation can cause problems when it is not consistent with the cross section geometry upstream and downstream of the structure.  The extrapolation is basically assuming that the changes in conveyance, area, and other hydraulic parameters are linear with respect to increased stage.  However, these hydraulic properties are very non-linear.  Therefore the extrapolation can cause the unsteady flow equations to have difficulty in solving the equations.  An example bridge crossing and set of preprocessed curves is shown in Figure 22. 

##### **Modeling Steep Streams** 

Steep streams are very difficult to model with an unsteady flow model in general.  Modeling a dam break flood wave through a steep stream system is even more difficult.  Steep streams tend to have very high velocities and rapid changes in depth, area, and velocity, which makes it more challenging to obtain a stable model solution through these areas. 

48 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 





**Figure 22.** Example Bridge with Pre-Processed Bridge Curves 

The default solution methodology for the one-dimensional unsteady flow routing option within HEC-RAS is generally for gradually varied flow.  Areas of rapidly varied flow, such as flow 

profiles transitioning from subcritical to supercritical flow, and hydraulic jumps, tend to cause the one-dimensional solution scheme to have difficulties in remaining stable.  Additionally, the assumption of a hydrostatic flow distribution may not be valid.  As Froude number approaches 1.0 (critical depth), the inertial terms of the St. Venant equations and their derivatives tend to cause model instabilities (generally in rapid flow areas the derivatives are over estimated). However, the HEC-RAS software does have an option to run the one-dimensional solution scheme in a mixed flow regime mode, which allows it to solve through these types of flow transitions. 

**Manning's n Values** .  If you are running the software in the default mode ( mixed flow option not turned on), and if the program goes down to critical depth at a cross section, the changes in area, depth, and velocity are very high.  This sharp increase in the water surface slope will often cause the program to overestimate the depth at the next cross section upstream, and possible underestimate the depth at the next cross section downstream (or even the one that went to critical depth the previous time step).  One solution to this problem is to increase the Manning's _n_ value in the area where the program is first going to critical depth, and the steeper portions of the reach.  This will force the solution to a subcritical answer and allow it to continue with the run. It is common for people to underestimate the magnitude of the Manning's roughness coefficient for steep streams.  Additionally, it is common to have pool and riffle sequences in steep streams. In a pool and riffle sequence, Manning's _n_ values will often be higher in the steeper riffle areas, and lower in the flatter pool areas.  This level of detail for modifying Manning's _n_ values is often not done, and can be a contributor to the instability of the model. 

**Mixed Flow Regime Option.** If you feel that the true water surface should go to critical depth, or even to an extended supercritical flow regime, then the mixed flow regime option should be turned on when using one-dimensional river reaches to model steep areas.  In order to solve the 

49 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

stability problem for a mixed flow regime system, Dr. Danny Fread (Fread, 1986) developed a methodology called the "Local Partial Inertia Technique" (LPI).  The LPI method has been adapted to HEC-RAS as an option for solving mixed flow regime problems when using the unsteady flow analysis portion of HEC-RAS.  This methodology applies a reduction factor to the two inertia terms in the momentum equation as the Froude number goes towards a user defined threshold. 

The default values for the methodology are Froude Number Threshold (FT) = 0.8 and m (exponent) = 4.  When the Froude number is greater than the threshold value, the factor is set to zero.  The user can change both the Froude number threshold and the exponent.  As you increase the value of both the threshold and the exponent, you decrease stability but increase accuracy. As you decrease the value of the threshold and/or the exponent, you increase stability but decrease accuracy.  To learn more about the **Mixed Flow Regime** option in HEC-RAS, please see the HEC-RAS User's Manual (HEC, 2014). 

**Increased Baseflow.** Another solution to the problem of flow going from subcritical to supercritical flow and back again, is to increase the base flow in the hydrographs, as well as the base flows used for computing the initial conditions.  Increased base flow will often dampen out any water surfaces going towards or through critical depth due to low flows that are in a pool riffle sequence. 

**Modified Puls Routing.** HEC-RAS has an option that will allow the user to define any portion of a model to be solved with the Modified Puls routing method instead of the full unsteady flow equations.  This allows the user to define problem areas, such as very steep reaches, as Modified Puls Routing reaches.  A Modified Puls Routing reach can be defined at the upstream end of a HEC-RAS river reach, at the downstream end, in the middle of a reach, or even defined for the entire reach.  The computations are performed in conjunction with the unsteady flow equations on a time step by time step basis.  Additionally, reaches that are defined as Modified Puls reaches can contain bridges, culverts, and even lateral structures.  The hydraulics of these structure types are accounted for during the Modified Puls routing.  To use this option, please review the HEC-RAS User's Manual (HEC, 2014). 

**Two-Dimensional Flow Areas.** The new two-dimensional flow area option in HEC-RAS allows user to model areas with either the Full Saint Venant equations in two-dimensions, or the diffusion wave form of the equations in two-dimensions.  The new two-dimensional solver uses a finite volume solution algorithm, which can handle subcritical, supercritical, and mixed flow regime (including hydraulic jumps), much more robustly then the current one-dimensional finite difference solution scheme.  This makes it very easy to use two-dimensional flow areas to model steep streams. 

##### **Drops in the Bed Profile** 

Significant drops in the bed profile can also be a source of model stability problems, especially at low flows.  Significant drops in the elevation of the channel bed can cause flow to pass through critical depth and results in an unstable model solution.  An example of this type of problem is shown in Figure 23. 

50 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 23.** Model Instability due to a Drop in the Bed Profile. 

If the drop is very small, then usually an increase in baseflow will drown out the drop, thus preventing the model from passing through critical depth.  If the drop is significant, then it should be modeled with an inline structure using a weir profile at the top of the drop.  This will allow the model to use a weir equation for calculating the upstream water surface for a given 

flow, rather than using the unsteady flow equations.  This produces a much more stable model, as the program does not have to model the flow passing through critical depth with the unsteady flow equations.  HEC-RAS automatically handles submergence on the weir, so this is not a problem.  An additional solution to this problem is to use the cross section rating curve option at the top of the drop, which causes the program to interpolate the water surface from the rating curve, rather than solving the unsteady flow equations through the drop in the bed profile. 

##### **Initial Conditions and Low Flow** 

**Initial Conditions.** In order for the unsteady flow model to run, the user must establish the initial conditions in the entire system.  This means that it must have a flow and a stage at every cross section, as well as a stage in every storage area/two-dimensional flow area (storage areas and two-dimensional flow areas can start dry).  The most common way to establish the initial conditions is for the user to enter a set of initial flows for all the reaches, and the software performs a steady flow backwater profile to get the corresponding stages.  The initial condition flows entered by the user must be consistent with the all of the boundary condition flows at time zero (the start of the unsteady flow run). 

Initial reservoir elevations and gate settings must also be consistent with the initial condition flows, such that the flow computed out of the reservoir at the first time step is consistent with 

51 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

what the user entered to perform the initial conditions profile (Figure 24).  If the user enters a low flow for the initial conditions backwater profile, and then at the first unsteady flow time step the program calculates a much larger flow coming out of the reservoir (due to gate settings an initial reservoir stages), this can cause an instability in the area just below the dam. 



<!-- Start of picture text -->
Bald Eagle Creek Example Dam Break Study       Plan: PMF - Froehlich Breach Parameters    10/28/2008<br>Bald Eagle Cr. Lock Haven<br>Legend<br>680<br>EG  03JAN1999 0300<br>WS  03JAN1999 0300<br>Crit  03JAN1999 0300<br>Ground<br>660<br>640<br>620<br>600<br>580<br>70000 75000 80000 85000<br>Main Channel Distance (ft)<br>Elevation (ft)<br><!-- End of picture text -->

**Figure 24.** Example of Initial Conditions for a Reservoir and Lateral Structures connected to Storage Areas. 

Another possible source of initial conditions causing the model to go unstable right away, are the initial storage area elevations.  It is up to the user to enter an initial storage area water surface elevation for all storage areas; even if it is to start out dry (water surface is set to the lowest elevation of the storage area).  When a storage area is hydraulically connected to a river reach (this is normally done with a lateral structure), and the initial water surface in the river reach is at an elevation that will cause a flow interaction with a storage area (water surface is above the lateral structure weir profile, or culverts, or gates), then that storage area needs to have an initial water surface elevation set equal to the computed initial stage in the river.  If the storage area is set much higher or lower than the elevation of the river section it is connected to, then a large discharge may be computed at the hydraulic structure that connects them.  This large discharge across the lateral structure will either take a lot of flow from the river (if the river stage is higher than the storage area), or it will have a large inflow into the river (if the storage area stage is much higher than the connected river stage).  Either of these two cases can cause the model to go unstable at the initial start of the unsteady flow computations.  By setting the storage area elevations to the same as the initial water surface of the cross section it is connected to, then the computed flow across the lateral structure will be close to zero.  Shown in Figure 24 are two lateral structures, which are connected to storage areas.  The initial condition water surface elevation is higher than the downstream lateral structure.  Therefore, the storage area connected to this structure must be set to the initial condition water surface elevation in this area.  Because the initial water surface is lower than the most upstream lateral structure, the water surface 

52 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

elevation for that connected storage area can be set to dry, or whatever elevation is appropriate below the minimum elevation of the lateral structure. 

**Low Flow Conditions.** Low flows can often be very difficult to model with an unsteady flow model.  Medium to steeper slope streams will often have a pool and riffle sequence at low flow, and the water surface will generally pass through critical depth at the upper end of the riffle (bottom of the pool).  In addition to this, the depths of water are very shallow.  Once the flood wave begins the water surface will change quickly, and there will be a large change in depth with respect to distance and time.  The leading edge of a dam break flood wave will be very steep, and can often be a source of model instability as it propagates down the river system.  The finite difference solution to the equations will generally have the most trouble balancing during the initial dramatic rise at the beginning of the flood wave.  The fact that the initial conditions may be very low flows and depths can make it even more difficult to solve through those shallow and steep riffle regions. 

There are several things the modeler can do to allow the program to solve through this situation. The easiest solution is to increase the base flow for the initial conditions.  This will provide more initial depth of water in general, and it may also drown out the pool and riffle sequence.  A general "rule of thumb" is to start out by trying a base flow around one percent of the peak flow that will be routed.  Increase the base flow if necessary, but never go above ten percent of the peak flow.  If you artificially use a base flow that is ten percent or more of the peak, the computed peak flow and stage will be higher than it would have been otherwise. 

If you have increased the base flow to a reasonable level, and are still having model stability problems at the leading edge of the flood wave, then try adding a pilot for the reach in which the model is having stability issues.  A pilot channel is an option in which you can add some depth without adding much flow area or conveyance.  The pilot channel is an option in HEC-RAS, and it is only used during low flow, once the cross sections get to some appreciable depth, the program automatically removes it from the cross section.  To learn more about the use of pilot channels, please review the section on Pilot Channels in Chapter 6 of the HEC-RAS User’s Manual (HEC, 2014). 

One other option that can help stabilize the model during the initial rise of the flood wave is turning on the **Mixed Flow Regime Option** .  This option drops the acceleration terms when the Froude number gets greater than a user defined threshold, which is often the case on the leading edge of the flood wave. 

##### **Downstream Boundary Conditions** 

Downstream boundary conditions are important for all hydraulic models, especially unsteady flow models.  Downstream boundary conditions can often be a source of model error, as well as model instability.  More often than not, the true stage for a given flow at the downstream end of our models is not known.  Because of this we often use either normal depth (Manning's equation), or a rating curve computed from a steady flow model.  The normal depth boundary condition requires the user to enter a single energy slope, which is then in turn used in Manning's equation to compute the downstream stage for any flow occurring.  Occasionally this forced slope or even a single valued rating curve can end up with stages that are not correct for the given flow at a given point on the flood hydrograph.  In general, the best solution is to make sure 

53 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

that the downstream boundary condition is downstream from any of the locations in which stages are being used to compute damages or loss of life, such that the error in the water surface elevation at the boundary condition does not affect the area of interest. 

Additionally, if a boundary condition is ill posed (rating curves with not enough points, or the user entered stages are too low for a given flow rate; and normal depth boundaries where the user has entered to steep of a slope for the energy gradeline), this can be a source of model instability. In other words, the downstream boundary condition may be causing abrupt drops or rises in the computed water surface near the location of the boundary condition.  An example of what can happen when using a normal depth boundary condition, and entering to steep of an energy slope is shown in Figure 25.  In this case, the steep energy slope caused the program to compute lower stages than appropriate for a given flow, which in turn caused the model to over steepen the flood wave at the downstream end of the model. 



**Figure 25.** Example Model Error Due to Bad Downstream Boundary Condition 

##### **Using Two-Dimensional Flow Areas for Dam Break Analyses** 

The latest version of HEC-RAS (5.0 or later) now has the ability to perform two-dimensional flow routing.  For a dam break study, the user can model the downstream area entirely with onedimensional elements (cross sections and storage areas); as a combination of one- and twodimensional elements (cross sections, storage areas, and two-dimensional flow areas); or the entire downstream area can be modeled as a two-dimensional flow area. 

Two-dimensional flow areas can be directly connected to storage areas by using a hydraulic structure called a storage area or two-dimensional flow area hydraulic connector ("SA/2D Area Conn").  See the example in Figure 26. 

In the example shown in Figure 26, the storage area is upstream of the two-dimensional flow area, so the positive flow direction is from the storage area to the two-dimensional flow area. When defining the hydraulic structure that connects the two areas, the storage area will be 

54 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 



**Figure 26.** Example of a Storage Area connected to a Two-Dimensional Flow Area 

considered the headwater side, and the two-dimensional flow area will be considered the tailwater side.  In the example shown in Figure 25, a storage area is being used to represent a reservoir pool.  The hydraulic connection between the storage area and the two-dimensional flow area is used to model the dam.  The two-dimensional flow area is being used to model the 

hydraulics of the flow downstream of the dam.  Additionally, the user could model the reservoir pool with a one-dimensional river reach, or a two-dimensional flow area. 

Using the approach shown in Figure 26 is a very quick way to get a dam break model up and running.  However, modeling the downstream area with a two-dimensional flow area does not necessarily make this a detailed model.  Downstream areas will often have bridges, culverts, roads that are barriers to flow, levees protecting urban areas, etc.  The types of areas require detailed modeling to get accurate answers, whether you are modeling them as two-dimensional flow areas or one-dimensional river reaches.  Developing a detailed model for the downstream 

55 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

area requires detailed terrain, hydraulic structure information, and the time to model those areas correctly.  If a two-dimensional flow area is used, it still requires lots of work to make the computational mesh respect all of the barriers to flow (bridges, culverts, roads, levees, etc.). Developing a detailed computational mesh that respects all of the flow barriers, and includes all of the hydraulic structures is the most time consuming part of developing a model, but it is necessary to get good answers downstream.  If you do not take the time to do this, and you just through in a two-dimensional flow area with a nominal grid size, do not assume you have "accurate" answers just because you a doing two-dimensional modeling. 

56 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

#### **References** 

###### **Ackerman, 2014.** 

Ackerman, Cameron T., 2014. Adapted from lecture material provided during HEC-RAS training courses. 

###### **Atallah, 2002.** 

Atallah, Tony A., 2002. _A Review on Dams and Breach Parameters Estimation_ .  Master of Science in Hydrosystems Engineering, Virginia Polytechnic Institute & State University, Blacksburg, VA, January 2002. 

###### **Brown and Rogers, 1977.** 

Brown, R. J. and Rogers, D. C., 1977. _A simulation of the hydraulic events during and following the Teton Dam failure_ .  Proceedings of Dam-Break Flood Routing Model Workshop, Bethesda, MD, pages 131 - 163; 18 – 20 October,. 

###### **Costa, 1985.** 

Costa, John E., 1985. _Floods from Dam Failures_ .  United States Department of the Interior, Geological Survey, Open-File Report 85-560, Denver, CO. 

###### **Cristofano, 1965** . 

Cristofano, Eugene A., 1965. _Method of Computing Erosion rate for Failure of Earthfill Dams_ . U.S. Bureau of Reclamation, Engineering and Research Center, Denver CO; 1965. 

###### **Dewey and Gillette, 1993.** 

Dewey, R. and Gillette, D., 1993. _Prediction of Embankment Dam Breaching for Hazard Assessment_ .  ASCE Specialty Conference on Geotechnical Practice in Dam Rehabilitation, Raleigh, North Carolina, 25-28 April 1993. 

###### **Evans, 1986.** 

Evans, Stephen. G., 1986. _The maximum discharge of outburst floods caused by the breaching of man-made and natural dams_ .  Canadian Geotechnical Journal, 1986, 23(3), pages 385 - 387. 

###### **FERC, 1988.** 

United States Federal Energy Regulatory Commission (FERC) - Notice of Revised Emergency Action Plan Guidelines, 22 February 1988. 

###### **Fread, 1986.** 

Fread, Dr. Danny L., 1986. _Local Partial Inertia Technique (LPI)_ . 

###### **Fread, 1988.** 

Fread, Dr. Danny L., 1988 (revised 1991). _BREACH: An Erosion Model for Earth Dam Failures_ .  Hydrologic Research Laboratory, National Weather Service, National Oceanic and Atmospheric Administration (NOAA), Silver Springs, MD, July 1988 (revised August 1991). 

57 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

###### **Fread, 1993.** 

Fread, Dr. Danny L., 1993. _NWS FLDWAV model: The replacement of DAMBRK for dam-break flood prediction_ .  10<sup>th</sup> Annual Conference of the Association of State Dam Safety Officials, Kansas City, MO, 26 - 29 September 1993, pages 177–184. 

###### **Fread, 2006.** 

Fread, Dr. Danny L., 2006.  Course notes on " _Dam Break Floods_ ". 

###### **Froehlich, 1987.** 

Froehlich, David C., 1987. _Embankment-Dam Breach Parameters_ .  Hydraulic Engineering, Proceedings of the 1987 National Conference, ASCE, Williams burg, VA, pages 570 - 575. 

###### **Froehlich, 1995a** . 

Froehlich, David C., 1995. _Embankment Dam Breach Parameters Revisited_ .  First International Conference, Water Resources Engineering, Environmental and Water Resources Institute (EWRI), 14 - 18 August 1995.  ASCE, Water Resources Engineering Proceeding,  pages 887 - 891. 

###### **Froehlich, 1995b** . 

Froehlich, David C., 1995.  " _Peak Outflow from Breached Embankment Dam_ ".  ASCE Journal of Water Resources Planning and Management, Volume 121, Issue 1, January 1995, pages 90 - 97. 

###### **Froehlich, 2008.** 

Froehlich, David C., 2008. _Embankment Dam Breach Parameters and Their Uncertainties_ . ASCE, Journal of Hydraulic Engineering, Vol. 134, No. 12, December 2008, pages 1708-1721. ISSN 0733-9429. 

###### **Hagen, 1982** . 

Hagen, V. K., 1982. _Re-evaluation of design floods and dam safety_ .  Proceedings of 14th ICOLD Congress, Rio De Janeiro, Brazil. Vol. 1, pages 475 - 491, 1982. 

###### **Hanson, et al., 2003.** 

Hanson, Gregory J., Cook, K.R., and Britton, S.L., 2003.  " _Observed Erosion Processes During Embankment Overtopping Tests_ .  American Society of Agricultural Engineers (ASAE), Annual Meeting, Proceedings, Paper No. 03-2066, July 2003. 

###### **Harris and Wagner, 1967.** 

Harris ,G.W. and Wagner, D.A., 1967. _Outflow from Breached Earth Dams_ .  University of Utah, Salt Lake City, UT. 

###### **Hassan, et al., 2004.** 

Hassan, M., Morris, M., Hanson, G.J., and Lakhal, K., 2004. _Breach formation: Laboratory and numerical modeling of breach formation_ .  Proceedings of the Annual Conference of the Association of State Dam Safety Officials (ASDSO), Phoenix, AZ, 2004, pages 1321-1337. 

58 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

###### **HEC, 1980.** 

Hydrologic Engineering Center, 1980. _Flood Emergency Plans - Guidelines for Corps Dams_ , RD-13, June 1980.  U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. 

###### **HEC, 2014.** 

Hydrologic Engineering Center, 2014. _HEC-RAS River Analysis System_ , _User's Manual_ , CPD68.  U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. 

###### **HEC, 2014a.** 

Hydrologic Engineering Center, 2014. _HEC-RAS River Analysis System_ , _Hydraulic Reference Manaual_ , CPD-69.  U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. 

###### **Jarrett, 1984** . 

Jarrett, Dr. Robert D, 1984. _Hydraulics of High-Gradient Streams_ .  ASCE, Journal of Hydraulics, Volume 110, No. HY 11, pages 1519 - 1539; November 1984. 

###### **Johnson and Illes, 1976.** 

Johnson, F.A. and Illes, P., 1976. _A Classification of Dam Failures_ .  Water Power and Dam Construction, pages 43 - 45; December 1976 

###### **Kirkpatrick, 1977.** 

Kirkpatrick, Gerald. W., 1977. _Evaluation guidelines for spillway adequacy, The Evaluation of Dam Safety_ .  Engineering Foundation Conference, ASCE, New York, pages 395 - 414, 1977. 

###### **MacDonald and Langridge-Monopolis, 1984.** 

MacDonald, Thomas C., and Langridge-Monopolis, J, 1984. _Breaching characteristics of dam failures_ .  ASCE Journal of Hydraulic Engineering, Vol. 110, No. 5, May 1984, pages 567 - 586. 

###### **Mohamed, 2002.** 

Mohamed, M.A.A., 2002. _Embankment Breach Formation and Modeling Methods_ .  The Open University, England, UK. 

###### **Olsen, 1976.** 

Olsen, Eunice, 1976.  Photos of the Teton Dam Failure, St. Anthony, ID, June 1976. 

###### **Ponce and Tsivoglou, 1981.** 

Ponce, Victor M., and Tsivolgou , Andrew J., 1981. _Modeling Gradual Dam Breaches_ .  ASCE Journal of the Hydraulics, Proceedings, Volume107, No. 7, pages 829 - 838. 

###### **Samuels, 1989.** 

Samuels, P.G., 1989. _Backwater lengths in rivers_ .  Proceedings of the Institution of Civil Engineers, Part 2, Volume 87, pages 571 - 582. 

59 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

###### **Singh and Scarlatos, 1985.** 

Singh, V. P. and Scarlatos, P. D., 1985b. _Breach erosion of earth-fill dams and flood routing: BEED Model_ .  Military Hydrology Report, page 131; U.S. Army Engineer Waterways Experiment Station, Environmental Laboratory, Vicksburg, MS. 

###### **Singh and Scarlatos, 1988.** 

Singh, V.P., Scarlatos, P.D., Collins, J.G. and Jourdan, M.R., 1988. _Breach Erosion of Earthfill Dams (BEED) Model_ .  Natural Hazards, Volume 1, pages 161 - 180. 

###### **Singh and Snorrason, 1982.** 

Singh, Krishan P. and Snorrason A., 1982. _Sensitivity of Outflow Peaks and Flood Stages to the Selection of Dam Breach Parameters and Simulation Models_ .  University of Illinois, State Water Survey Division, Surface Water Section, Champaign, IL, 179 pages; June1982. 

###### **Singh and Snorrason, 1984.** 

Singh, Krishan P., and Snorrason, A., 1984. _Sensitivity of outflow peaks and flood stages to the selection of dam breach parameters and simulation models_ .  Journal of Hydrology, Vol 68, Issues 1-4, February 1984, pages 295 - 310. Global Water: Science and Engineering The Ven Te Chow Memorial Volume 

###### **SCS, 1981** . 

SCS, 1981. _Simplified Dam-Breach Routing Procedure_ .  United States Department of Agriculture, Soil Conservation Service (SCS), Technical Release No. 66 (Rev. 1), 39. 

###### **Temple, et al., 2006.** 

Temple, Darrel M., G.J. Hanson, and Neilsen, M.L., 2006. _WINDAM – Analysis of Overtopping Earth Embankment Dams_ .  ASABE Annual International Meeting Proceedings, Paper No. 062105; 9 - 12 July 2006, Portland, OR. 

###### **USBR, 1982.** 

USBR, 1982. _Guidelines for defining inundated areas downstream from Bureau of Reclamation dams_ . Reclamation Planning Instruction, No. 82-11; 15 June 1982, U.S. Bureau of Reclamation. 

###### **Vaskinn, et al., 2004.** 

Vaskinn, Kjetil A., Lovoll, M.A., Hoeg, K., Morris, M., Hanson, G., and Hassan, M., 2004. _Physical Modeling of Breach Formation; Large Scale Field Tests_ .  State Dam Safety Officials Association Proceedings.  Phoenix, AZ, September 2004. 

###### **Von Thun and Gillette, 1990** . 

Von Thun, J. Lawrence, and Gillette, D. R., 1990. _Guidance on breach parameters_ . Unpublished internal document, U.S. Bureau of Reclamation, Denver, CO.  March 1990, 17 pages. 

###### **Wahl, 1998.** 

Wahl, Tony L., 1998. _Prediction of Embankment Dam Breach Parameters - A Literature Review and Needs Assessment_ .  Dam Safety Research Report, DSO-98-004.  Water Resources Research Laboratory, U.S. Dept. of the Interior, Bureau of Reclamation, Dam Safety Office (DSO), July 1998. 

60 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

###### **Wahl, 2009.** 

Wahl, Tony L., 2009.  " _Evaluation of New Models for Simulating Embankment Dam Breach_ . Association of State Dam Safety Officials (ASDO) Conference, Hollywood, Florida,  27 September - 1 October 2009. 

###### **Walder and O'Connor, 1997.** 

Walder, Joseph S. and O'Connor, J. E., 1997. _Methods for predicting peak discharge of floods caused by failure of natural and constructed earth dams_ .  Water Resources Research, Vol. 33 Issue 10, pages 2337 - 2348. October 1997. 

###### **Wang and Kahawita, 2006.** 

Wang, P., Kahawita, R., Mokhtari, A., Phat, T.M. and Quach, T.T., 2006. _Modelling breach formation in embankments due to overtopping_ .  ICOLD Conference, Barcelona, Spain, June 2006. 

###### **Xu and Zhang, 2009.** 

Xu, Y. and Zhang , L. M., 2009. _Breaching Parameters for Earth and Rockfill Dams_ .  ASCE Journal of Geotechnical and Geoenvironmental Engineering, Volume 135, No. 12, pages 1957 - 1970, December 2009. 

#### **Additional References** 

CEATI (Centre for Energy Advancement through Technological Innovation) International Inc., Dam Safety Interest Group (DSIG), <u>http://www.ceati.com/.</u> 

Fread, Dr. Danny L., 1984. _DAMBRK: The NWS dam-break flood forecasting model_ .  U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. CPD40 

Hanson, G. J., Temple, D. M., Morris, M., Hassan, M., Cook, K., 2005). _Simplified breach analysis model for homogeneous embankments:  Part II, Parameter inputs and variable scale model comparisons_ U.S. Society on Dams Annual Meeting and Conference, Proceedings, Salt Lake City, UT, June 2005, pages 163 - 174. 

Hydrologic Engineering Center, 2010a. _HEC-RAS River Analysis System_ , _Hydraulic Reference Manual_ , CPD-69.  U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. 

Hydrologic Engineering Center, 2011. _HEC-GeoRAS_ , _User's Manual_ , CPD-83 U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. 

Hydrologic Engineering Center, 2010. _HEC-HMS Hydrologic Modeling System_ , _User's Manual,_ CPD-74A _._ U.S. Army Corps of Engineers, Hydrologic Engineering Center, 609 Second Street, Davis, CA. 

Wahl, Tony L., 2004. _Uncertainty of Predictions of Embankment Dam Breach Parameters_ ", ASCE, Journal of Hydraulic Engineering, Volume 130, No. 5, pages 389 - 397, May 2004. 

61 

_Using HEC-RAS for Dam Break Studies_ 

_Training Document No. 39_ 

Wahl, Tony L., Hanson, G.J., Courivaud J., Morris, M., Kahawita, R., McClenathan, J.T., and Gee, D.M., 2008. _Development of Next-Generation Embankment Dam Breach Models_ .  United States Society on Dams Proceedings, pages 767 - 779; Portland, OR; 28 April - 2 May 2008. 

Washington State Dept. of Ecology, 1992.  Dam Safety Guidelines, Technical Note 1, _Dam Break Inundation Analysis and Downstream Hazard Classification_ .  Water Resources Program, Dam Safety Office, P.O. Box 47600, Olympia, WA 98504-7600, July 1992 (revised October 2007), <u>https://fortress.wa.gov/ecy/publications/publications/9255e.pdf</u> 

62 

