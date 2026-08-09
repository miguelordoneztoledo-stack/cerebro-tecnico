---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Flujo No Permanente\02 Bibliografia\HAMMER_V8i.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]



HAMMER V8i, Transient Analysis and Design (metric) 

Version V8i (SELECTseries 3) 

_Bentley Institute Course Guide_ 



TRN018120-1/0001 

##### **Trademark Notice** 

Bentley and the "B" Bentley logo are either registered or unregistered trademarks or service marks of Bentley Systems, Incorporated. All other marks are the property of their TRN018110-1/0001respective owners. 

AccuDraw, MDL, MicroStation, and SmartLine are registered trademarks; PopSet and Raster Manager are trademarks. 

AutoCAD is a registered trademark of Autodesk, Inc. 

##### **Copyright Notice** 

Copyright ©2012, Bentley Systems, Incorporated. All Rights Reserved. 

2 HAMMER V8i, Transient Analysis and Design (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



## **Table of Contents** 

|**Agenda ____________________________________________6**|
|---|
|Day 1 ____________________________________________6|
|Day 2 ____________________________________________6|
|**Introduction to HAMMER V8i __________________________7**|
|**Theory of Unsteady Flow _____________________________18**|
|**Modeling Unsteady Flow _____________________________42**|
|**Transients in an Unprotected Pipeline (metric) ___________55**|
|Module Overview _____________________________________55|
|Module Prerequisites __________________________________55|
|Module Objectives_____________________________________55|
|Problem Statement ____________________________________56|
|Water System Description ___________________________56|
|Creating the Model ____________________________________57|
|Project Setup______________________________________57|
|Prototypes________________________________________57|
|Network Layout____________________________________59|
|Data Entry ________________________________________61|
|Wave Speed Calculator______________________________64|
|Configuring the HAMMER Project_________________________69|
|Calculation Options_________________________________69|
|Profiles___________________________________________71|
|Analysis without Surge Protection Equipment _______________75|
|Reviewing your Results _________________________________79|
|Visualizing Simulated Results _________________________81|
|Generate Report-Ready Graphs _______________________83|
|**Transients in an Unprotected Pipeline - Q and A __________88**|
|Results Tables ________________________________________88|
|Workshop Review _____________________________________90|
|Questions ________________________________________90|



3 Copyright © 2012 Bentley Systems, Incorporated 

Table of Contents 

Mar-12 

Table of Contents 

|Answers__________________________________________92|
|---|
|**Causes of Transients _________________________________94**|
|**Surge Protection: Tanks and Valves _____________________109**|
|**Pipeline Protection (metric) ___________________________119**|
|Module Overview _____________________________________119|
|Module Prerequisites __________________________________119|
|Module Objectives_____________________________________119|
|Problem Statement ____________________________________120|
|Description _______________________________________120|
|Adding Surge-Protection Equipment_______________________121|
|Adding a Hydropneumatic Tank _______________________123|
|Adding an Air Valve_________________________________131|
|Adding a Simple Surge Tank with Check Valve____________138|
|Adding a Simple Surge Tank without Check Valve _________146|
|Adding a Surge Relief Valve __________________________150|
|**Pipeline Protection - Q and A __________________________157**|
|Results Tables ________________________________________157|
|Workshop Review _____________________________________159|
|Questions ________________________________________159|
|Workshop Results __________________________________160|
|Answers__________________________________________161|
|**Transients in Pipe Networks ___________________________162**|
|**Network Risk Reduction (metric) _______________________174**|
|Module Overview _____________________________________174|
|Module Prerequisites __________________________________174|
|Module Objectives_____________________________________174|
|Importing and Verifying the Initial Steady-States_____________175|
|Discussion ________________________________________176|
|Configuring the Transient Analysis ________________________177|
|<br>Analysis without Surge Protection ________________________186|
|**Network Risk Reduction - Q and A ______________________195**|
|Workshop Review _____________________________________195|
|Questions ________________________________________195|
|Answers__________________________________________199|



4 Copyright © 2012 Bentley Systems, Incorporated 

Table of Contents 

Mar-12 

Table of Contents 

|**Modeling Objectives _________________________________201**|
|---|
|**Skeletonization for Transients _________________________208**|
|**Advanced Surge Protection ___________________________232**|
|**Multipoint Network Protection (metric) _________________239**|
|Module Overview _____________________________________239|
|Module Prerequisites __________________________________239|
|Module Objectives_____________________________________239|
|Analysis with Surge-Protection Equipment__________________240|
|Color-Coding Maps, Profiles and Point Histories _____________251|
|Color Coding ______________________________________251|
|Transient Thematic Viewer (TTV) ______________________254|
|Reviewing Results _____________________________________257|
|**Multipoint Network Protection - Q and A ________________262**|
|Workshop Review _____________________________________262|
|Questions ________________________________________262|
|Answers__________________________________________263|
|**ModelBuilder _______________________________________264**|
|**Hydropower and Mining System Applications ____________279**|
|**Sewer System Applications ___________________________283**|
|**Reference Material __________________________________288**|
|Contact Information for Reference Material:_____________288|
|Ottawa HPTM ________________________________________289|
|Avenue & Rosehill Watermain Class EA ____________________290|
|Alliston to Beeton Transmission Lines______________________291|
|Thunder Bay Water Network & Crossings___________________293|
|Ellesmere Pump Station ________________________________295|
|West Dundas Water Supply Investigation___________________296|
|Western Beaches Storage Tunnel _________________________297|
|Jackson Trails Sewage PS________________________________298|
|Pit River Penstocks_____________________________________299|
|Barrick Roaster Plant & Tailings Lines ______________________300|



5 

Table of Contents 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 



# **Agenda** 

#### **Day 1** 

- **7:30 - Begin** 

   - **Overview: Why use HAMMER?** 



###### **Theory of Unsteady Fluid Flow** 



- **Demo:** HAMMER Validation for rapid valve closure 

**Modeling Unsteady Fluid Flow -** How do we Model Transients 



- **Demo:** Simulation ofpower failure 

- **Case Study** : Breaks due to Sub-Atmospheric Pressures 



###### **Causes of Transients -** 

Pumps and Flow Control Valves 

- **12:00 - Lunch** 



**Workshop** - Transients in an Unprotected Pipeline 

###### **Surge Protection using Tanks and Valves** 





**Workshop** - Pipeline Protection using a Tank or Air Valve 

- **5:00 - Q & A Session / Adjourn** 



Workshop 



Lecture 

#### **Day 2** 

######  **8:00 - Begin** 

###### **Transients in Pipe Networks** 



- **Case Study** - City of Thunder Bay (3 zones and 2 water supplies) 



**Workshop** - Network Risk Reduction 

###### **Modeling Objectives** 



- Case Study - Nuisance transients and other interesting puzzles 

###### **Skeletonization for Transients** 



- **12:00 - Lunch** 

   - **Advanced Surge Protection Devices** 





**Workshop** - Multi-point Network Protection 



###### **ModelBuilder** 

###### **Hydropower and Mining System Applications** 



Optional - **Sewer System Applications -** Mass Oscillation and Air Expulsion 



   - **Case Study** - Transients in deep pressurized sewer with mass oscillation, flow reversal and air expulsion 

- **5:00 - Q & A Session / Adjourn** 

6 

Mar-12 

Agenda 

Copyright © 2012 Bentley Systems, Incorporated 



# **Introduction to HAMMER V8i** 



7 

Mar-12 

Introduction to HAMMER V8i 

Copyright © 2012 Bentley Systems, Incorporated 





8 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





9 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





10 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





11 Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Introduction to HAMMER V8i 





12 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





13 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





14 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





15 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





16 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





17 Introduction to HAMMER V8i Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Theory of Unsteady Flow** 



18 

Theory of Unsteady Flow 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





19 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





20 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





21 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





22 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





23 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





24 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





25 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





26 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





27 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





28 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





29 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





30 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





31 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





32 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





33 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





34 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





35 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





36 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





37 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





38 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





39 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





40 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





41 Theory of Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Modeling Unsteady Flow** 



42 

Mar-12 

Modeling Unsteady Flow 

Copyright © 2012 Bentley Systems, Incorporated 





43 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





44 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





45 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





46 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





47 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





48 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





49 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





50 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





51 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





52 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





53 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





54 Modeling Unsteady Flow Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Transients in an Unprotected Pipeline (metric)** 

### **Module Overview** 

In this workshop you will use HAMMER to perform a numerical simulation of hydraulic transients in a water transmission main to determine the effect of a pump shutdown. 

- **Note:** This course material has been developed for the HAMMER V8i (SELECTseries 3) platform, specifically the software version 08.11.03.17.  Users currently using versions prior to version 08.11.03.17 may experience slight differences in course material. 

### **Module Prerequisites** 

- Fundamental knowledge of hydraulic transients 

### **Module Objectives** 

After completing this module, you will be able to: 

- Understand and use prototypes in model layout to save time 

- Use the Wave Speed Calculator to determine the wave speed for a pipe or set of pipes 

- Modify the transient calculation options 

- Create a profile 

- Model a power failure using the transient properties for a pump 

- Review and animate your results using the Transient Results Viewer 

- Format the appearance of graphs generated by the Transient Results Viewer 

55 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Problem Statement 

### **Problem Statement** 

Analyze the system as it was designed (without any surge-protection equipment) to determine its vulnerability to transient events. 

Present your results graphically to gain an understanding of the transient phenomenon and develop a set of possible remediation strategies. 

#### **Water System Description** 

A water-pumping station draws water from a nearby reservoir (383 mnormal water level) and conveys 1682 m<sup>3</sup> along a dedicated transmission pipeline to a reservoir (456 m normal water level) for a total static lift of 456 - 383 = 73 m.  The elevation of the constant-speed pump is 363 m and its speed is 1760 rpm. The other data for the transmission main nodes and links will be discussed in the following pages as you add or modify each hydraulic element in the system. 



56 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

### **Creating the Model** 

In this section you will walk through setting up your model and laying out your HAMMER network. 

#### **Project Setup** 

To create a hydraulic model using the HAMMER interface follow the next exercise. 

- **Exercise: Creating a new project** 

   - 1 Start HAMMER V8i from the Start Menu > All Programs > Bentley or from the desktop icon. 

   - 2 Select Create New Project on the Welcome dialog, or select File > New. 

   - 3 Select File > Save As to select a directory and save your file with a name such as **Transients.wtg** .(HAMMER file names are not case sensitive.) 

   - 4 Select Tools > Options > Units. 

   - 5 Select Reset Defaults > System International and click OK. 

#### **Prototypes** 

Before we begin laying out the model, we want to assess the data for our elements to see if there are common properties among them.  If there are, we will create Prototypes for each element in order to decrease the amount of data entry that we will need to do in the long run. 

Our pipes will have many common values for their properties--such as Diameter, Material, Hazen-Williams C, etc.  Therefore, it makes sense for us to use a prototype in this situation.  We can create a prototype for the pipes that will have these common properties when we draw them. 

57 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Creating the Model 

######  **Exercise: Setting up prototypes** 

- 1 Select View > Prototypes. 



- 2 Select Pipe. 



- 3 Click the New button in the top left corner of the dialog to create a new prototype. 

The new prototype will automatically be named Pipe Prototype – 1. 

- 4 Right click on Pipe Prototype – 1 and select Rename. 

- 5 Rename the prototype to **DI 600 mm pipe** . 



- 6 Double click on DI 600 mm pipe to bring up the Properties manager. 

- 7 Set the following parameters for your prototype: 

Diameter (mm): 600 

Material: Ductile Iron 

Hazen-Williams C: 130 

Has User Defined Length?: True 



58 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

#### **Network Layout** 

We are now ready to begin laying out the model that was shown at the beginning of the workshop. 

######  **Exercise: Laying out a network** 



- 1 Click the Reservoir button from the Layout toolbar. 

- 2 Move the cursor over the drawing pane, and left click to insert a reservoir. 

**Note:** HAMMER automatically names this reservoir R-1. 



   - 3 After you have added the reservoir, click the Select button or hit the ESC key on your keyboard to deselect the Reservoir tool. 

- **Warning:** Be careful not to select the element with the Reservoir tool activated as this will create a new element on top of the old one if you have the Sticky Tool Palette option set in the Global Options.  You need to click the Select button or hit ESC before selecting an element. 

**Hint:** To disable the Sticky Tool Palette, do the following: 

   - Select Tools > Options. 

   - In the Options dialog, click on the Global tab. 

   - Uncheck the checkbox in front of the Sticky Tool Palette field at the bottom of the dialog. 

   - Click OK. 

- 4 Double click on the reservoir to bring up the Properties manager. 

**Note:** You can click in the view customization dropdown box at the top of the Properties manager which currently has <Show All> listed.  To only show the properties needed for a Transient analysis, you can change the view to Transient (Predefined). 

59 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Creating the Model 

- 5 Rename the reservoir to **Res1** in the Label field. 



Next we need to add a junction, a pump, and another junction to the right of Res1. 



- 6 Click on the Pipe button from the Layout toolbar. 

**Note:** Your cursor should change to a crosshair with a junction next to it. 

- 7 Click on Res1 and move your mouse to the right. 

- 8 Left click to place a junction. 

- 9 Move your mouse to the right, right click, and on the submenu that comes up select Pump. 



- 10 Left click to place the pump in the drawing. 

- 11 Continue this process to lay out the network as shown below: 





- 12 Once the network is drawn out, right click on an empty area of the drawing pane and select Done to finish adding the pipes and then click the Select button. 

- 13 Click on each element and change the Label of each in the Properties manager to match the screen shot above. 

- 14 Move around the labels to you can view them easier. 

60 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Creating the Model 

- **Note:** You can place the network by selecting each different element layout tool and place them in the drawing.  Then once those elements are drawn out, you can select the Pipe tool to connect all of them together. 

#### **Data Entry** 

We will now enter the data for the nodes and pipes. 

######  **Exercise: Entering element data** 

- 1 Select the individual nodes from the drawing pane (reservoirs, junctions and pump) to set their Elevations as shown in the tables below and on the next page. 

**Note:** To view and edit node data in a tabular form, select View > FlexTables. Select the appropriate FlexTable for the elements for which you wish to enter data— for example, use the Junction Table to enter data for the junctions.  You may need to add the Notes field to the FlexTables if it is not already there by selecting the Edit button.  You will then choose the field from the Available Columns side and click the Add button and then click OK to apply the changes. Changes made in a FlexTable are automatically reflected in the drawing pane. 

**Hint:** If you have trouble entering decimals for any values (for example, if the value is automatically rounded), then right click on the units (or column heading) and select Units and Formatting to change the Display Precision. 

###### **Junction Data Table** 

|**Label**|**Elevation (m)**|**Notes**|
|---|---|---|
|PJ1|363.0|Suction|
|PJ2|363.0|Pump Discharge|
|J1|408.0|Feeder main|
|J2|395.0|Feeder main|
|J3|395.0|Feeder main|
|J4|386.0|Feeder main|
|J5|380.0|Feeder main|
|J6|420.0|Feeder main|



###### **Pump Data Table** 

|**Label**|**Elevation (m)**|**Notes**|
|---|---|---|
|PMP1|363.0|Pump|



61 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

###### **Reservoir Data Table** 

|**Label**|**Elevation (m)**|**Elevation (Inlet/Outlet Invert) (m) **|**Notes**|
|---|---|---|---|
|Res1|383.0|377.0|Source Reservoir|
|Res2|456.0|450.0|Receiving Reservoir|



Below are screenshots of the data entry for J1, PMP1, and Res2. 







- 2 Set the values for each pipe according to those shown in the Pipe Data Table on the next page. 

62 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

- **Note:** You may use the FlexTables to enter the values if you want.  The Wave Speed can be left blank for now and we will calculate it afterwards.  If your Start Node and Stop Node are not correct, you can click in the Node Reversal field in the pipe properties for that pipe to reverse the Start Node and Stop Node. 

- **Warning:** Elevations are extremely important in hydraulic transient modeling.  This is because slopes determine how fast water columns will slow down (or speed up) as their momentum changes during a transient event.  Therefore, defining the profile of a pipeline is a key requirement prior to undertaking any hydraulic transient analysis with HAMMER. 

###### **Pipe Data Table** 

|**Label**|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|
|---|---|---|---|---|---|---|---|
|PS1|Res1|PJ1|True|50|600|Ductile Iron|130|
|PMP1S|PJ1|PMP1|True|40|600|Ductile Iron|130|
|PMP1D|PMP1|PJ2|True|20|600|Ductile Iron|130|
|P1|PJ2|J1|True|20|600|Ductile Iron|130|
|P2|J1|J2|True|380|600|Ductile Iron|130|
|P3|J2|J3|True|300|600|Ductile Iron|130|
|P4|J3|J4|True|250|600|Ductile Iron|130|
|P5|J4|J5|True|400|600|Ductile Iron|130|
|P6|J5|J6|True|250|600|Ductile Iron|130|
|P7|J6|Res2|True|175|600|Ductile Iron|130|



63 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

The screenshot below shows the data entry for PS1. 



#### **Wave Speed Calculator** 

Next, we will need to calculate the wave speed for these pipes.  To do that, Bentley HAMMER provides a tool called the Wave Speed Calculator. 

######  **Exercise: Using the Wave Speed Calculator** 



- 1 Select Tools > Wave Speed Calculator, or click the icon on the toolbar. 

64 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 



On the Wave Speed Calculator dialog, you should see four sections: Liquid, Material, Miscellaneous, and Features.  Also, note that there is an ellipsis button to the right of the fields in the Liquid and Material sections. 



- 2 To change the unit system to bars right click directly on the unit and choose Units and Formatting.  You can manually change the Unit to bars. 



- 3 Click on the ellipsis button in the Bulk Modulus of Elasticity field. 

65 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

This will open up the Liquid Engineering Library. 



- 4 Click the + sign in front of Liquid Libraries and the + sign in front of LiquidLibrary.xml to expand them. 

You should now see a list of different liquids. 

- 5 Click on Water at 4C(39F) to highlight it and click Select. 



**Note:** Back on the Wave Speed Calculator dialog, the Bulk Modulus of Elasticity and Specific Gravity fields should now have values in them. 

- 6 Click on the ellipsis button in the Young’s Modulus field. 

This will open up the Material Engineering Libraries. 

- 7 Click the + sign in front of Material Libraries and the + sign in front of MaterialLibrary.xml. 

You should now see a list of different materials. 

66 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

- 8 Scroll down the list and click on Ductile Iron and then click Select. 



**Note:** Back on the Wave Speed Calculator dialog, the Young’s Modulus and Poisson’s Ratio fields should now be filled in. 

- 9 Enter a Wall Thickness of 17.8 mm. 

Your Wave Speed Calculator should now look like this: 



10 Click OK. 

67 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Creating the Model 

This will calculate the wave speed and apply it to all of the pipes in the model. 

**Note:** After the calculation is complete, a Calculation Complete dialog will open. 



- 11 Click OK to close it. 

- 12 Look at the properties of the pipes, for example here is PS1: 



**Note:** The Wave Speed field for all pipes should now have a value of 1,252.33 m/s. 

13 Click File > Save to save your model. 

68 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Configuring the HAMMER Project 

### **Configuring the HAMMER Project** 

Before running the HAMMER model you have created, you need to set certain run-time parameters such as the fluid properties, piping system properties, run duration, and output requirements. 

First, we will need to set the calculation options. 

#### **Calculation Options** 

- **Exercise: Setting the calculation options** 

   - 1 Select Analysis > Calculation Options to bring up the Calculation Options manager. 



- 2 Double click on the Base Calculation Options under the Transient Solver folder to bring up its properties in the Properties manager. 

- 3 Set the following in the Summary section: 

Run Duration Type: Time 

Run Duration (Time) (sec): 140 sec 

Pressure Wave Speed (m/s): 0 (default value) 

Vapor Pressure (bars): –1 (default value) 

Generate Animation Data: True 

Run Extended CAV: True 

- 4 In the Reporting section, set the following: 

Show Pocket Opening/Closing: True 

Generate Detailed Reports?: True 

- 5 Click the Report Points field and choose Selected Points from the dropdown menu. 

- 6 In the Report Points Collection field, click on the ellipsis button and select the following points to report and output the transient history (or 

69 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Configuring the HAMMER Project 

temporal variation of flow, head, and air or vapor volumes) at the pump and nearby nodes: 

###### **PMP1D:PMP1** 

**P1:J1 P2:J1** 

**Note:** You can add other points of interest, such as P7:Res2, if you desire). 



- 7 Select each point of interest in the left window pane and click the Add button from the middle of the dialog to move the selected point to the right pane. 

Your final selection should look like this: 



- 8 Click OK. 

- 9 Click in the Report Times field and select Periodically. 

10 Set the Report Period to 10. 

- **Note:** This only affects the frequency of output data for plotting and animation. HAMMER will calculate each time step and show the complete and correct maximum and minimum transient envelopes whatever the Report Period. 

70 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Configuring the HAMMER Project 

Your Properties manager should now look like this: 



11 Close the Calculation Options dialog. 

#### **Profiles** 

Next, we will need to specify the path of the profile along which we want to see the graphical plot and animation of the HGL during the transient run. 

######  **Exercise: Setting the path of a profile** 

- 1 Select View > Profiles. 



- 2 Click the New button in the upper left corner to create a new profile. 

- 3 On the Profile Setup dialog that comes up, click on Select From Drawing. 

- 4 In the drawing, click on the pipes PMP1D, P1, P2, P3, P4, P5, P6 and P7 to highlight and select them (along with their connected nodes). 



- 5 After you have selected all of the listed pipes, click the Done button on the Select toolbar. 

71 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Configuring the HAMMER Project 

- **Note:** All of the pipes and nodes that you have selected will now be listed in the left side of the Profile Setup dialog. 



- 6 Click the Open Profile button to view your profile. 

- 7 Click OK on the Profile Series Options dialog that opens up. 

72 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Configuring the HAMMER Project 

You should now see the profile shown below. 



- **Note:** The plot of the HGL (in Blue) will not show values, as we have not calculated the initial conditions. 

   - 8 Click the red X in the top right corner to close the Profile dialog. 

   - 9 Back on the Profiles manager, right  click Profile – 1 and select Rename. 

   - 10 Rename the profile to **Main** . 

Next, we need to set this profile as a Transient Report Path for HAMMER. 

73 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Configuring the HAMMER Project 

- 11 Right click on Main and make sure that there is a checkmark in front of Transient Report Path as in the screenshot below. 



- 12 If there is not a checkmark, then simply click on the Transient Report Path option from the right click menu. 

**Note:** If you look closely at the icon in front of Main in the Profiles manager, you will notice a picture of a hammer in the top right corner of the icon.  This signifies that this profile is a HAMMER report path. 

- 13 Close the Profiles manager. 

- 14 Save using File > Save. 

You are now ready to run your HAMMER model. 

74 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Analysis without Surge Protection Equipment 

### **Analysis without Surge Protection Equipment** 

In this part you will perform a hydraulic transient analysis of the system after a sudden power failure without surge protection (other than the pump’s check valve). 

######  **Exercise: Setting up a sudden power failure** 

   - 1 Double click on the pump node (PMP1) to bring up its Properties manger. 

   - 2 In the Transient (Operational) section, click in the Pump Type (Transient) field and select Shut Down After Time Delay from the dropdown menu. 

- **Note:** You should now be presented with more options under that Pump Type (Transient) field. 

   - 3 Set the following pump parameters: 

Diameter (Pump Valve) (mm): 600 

- **Note:** This is the inside diameter of the pump’s intake flange. 

Time (Delay until Shut Down) (sec): 5 

- **Note:** For convenience, it is assumed that the power failure occurs after 5 seconds so that point histories will show the initial steady state during this period. 

Pump Valve Type: Check Valve 

**Note:** The power failure is assumed to be instantaneous and the check valve is allowed to close without any delay (zero) to protect the pump from damage. 

- 4 Click in the Pump Definition field (under the Physical section). 

- 5 On the dropdown menu in the Pump Definition field, select Edit Pump Definitions. 

This will open up the Pump Definitions manager. 

   - 6 Click the New button in the top left corner. 

   - 7 Set the Name of the pump definition to **PMP1** since we will be using this definition for pump PMP1. 

   - 8 In the right side of the Pump Definitions manager, click on the Head tab. 

   - 9 Change the Pump Definition Type to Design Point (1 Point). 

- **Note:** Right click the Flow column heading and select Units and Formatting to change Units to m<sup>3</sup> /h and Display Precision to 2. 

75 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Analysis without Surge Protection Equipment 

- 10 Enter the following points in the Design row: 

Flow: 1,682 m<sup>3</sup> /h 

Head: 81.4 m 



- 11 Click on the Efficiency tab and set the following values: 

Pump Efficiency: Constant Efficiency 

Pump Efficiency: 85 % 



- 12 Click on the Transient tab and set the following values: 

Inertia (Pump and Motor): 169.00 N.m<sup>2</sup> 

- **Note:** This is the combined pump, shaft, and motor inertia…this can be obtained from the manufacturer or estimated from its power rating. 

76 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Analysis without Surge Protection Equipment 

Speed (Full): 1760.0 rpm 

Specific Speed: SI=25, US=1280 

**Note:** Based on the pump’s rotation speed (1760 rpm).  See Appendix B for an explanation of how to determine a pump’s specific speed. 

Reverse Spin Allowed?: Uncheck the box 

**Note:** Not allowing reverse spin assumes there is a check valve on the discharge side of the pump or that the pump has a non-reverse ratchet mechanism. 

- 13 Click Close to close the Pump Definitions manager. 

- 14 Back in the PMP1 Properties manager, click in the Pump Definition field and select PMP1 from the dropdown menu. 

- 15 Select File > Save to save your changes. 



- 16 Select Analysis > Compute Initial Conditions or click the Compute Initial Conditions button on the toolbar. 

**Note:** This will compute the initial steady state conditions that will be the basis of our transient run.  After the steady state computations are completed, a Calculation Summary dialog will open.  If there were warnings or errors in our model, the messages would appear in the bottom half of the Calculation Summary dialog. 

You should not have any error messages. 

- 17 Close the Calculation Summary dialog. 



- 18 Click the Compute button on the main toolbar or select Analysis > Compute to run the model. 

A HAMMER run status dialog opens and displays the progress of the elapsed run. 

**Note:** If you suspect that a data entry error may have occurred, you can select Analysis > Validate before clicking Compute to perform a short run that detects errors before a (much longer) full run. 

When the calculations are completed, the Transient Calculation Summary dialog opens automatically. 

- 19 Take a moment to review the Summary, Initial Conditions, and Extreme Pressure and Heads tabs. 

- 20 If you have a printer installed on your computer, you may click the Report button if you wish to view this Summary in a detailed report format. 

77 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Analysis without Surge Protection Equipment 

- 21 Click Close when you are done, and if the User Notifications dialog comes up, close that as well. 

- 22 Select View > Profiles. 

- 23 Double click on Main to open the profile again. 

You should see the following: 



- 24 Close the Profile dialog and save your model. 

78 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

### **Reviewing your Results** 

To review your results graphically, you will use the Transient Results Viewer.  The Transient Results Viewer lets you view graphs and animate the hydraulic transient heads and flows. 

- **Exercise: Using the Transient Results Viewer** 

   - 1 Select Analysis > Transient Results Viewer. 



**Note:** By default, HAMMER does not generate output for every location or every time step since this may result in very large file sizes (tens or hundreds of megabytes). 

For the specific points or paths (e.g., profiles) you specified prior to the run, you can generate several types of graphs and animate them to visualize the results. 

The Profiles tab allows you to view profile results from transient simulations.  You are given the following information: 

- Profile - Select the Profile path you want to plot or animate. Only Profile paths marked as Transient Report Paths will be available from this menu. 

- Graph Type - Select the attribute(s) that will be displayed on the plot/ animation. 

- Profile button - Opens the Transient Profile Viewer dialog box. 

79 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Reviewing your Results 

Additionally, this tab reports the following Profile Point Statistics: 

- Count - This field displays the number of points along the profile path. 

- Length - This field displays the length of the profile path. 

- From Point - This field displays the start point of the profile path. 

- To Point - This field displays the end point of the profile path. 

The Time Histories tab allows you to plot a graph of the transient results at report points and consists of the following controls: 

- Working Scenario - Automatically displays the active scenario. 

- Additional Scenarios - If you have already run other scenarios for this model, you can compare results across multiple scenarios. Select which scenarios you want to compare. 

- Time History - Select the Report Point. 

- Graph Type - Select the attribute(s) that will be displayed on the plot. 

- Plot - Click this button to open the Transient Results Graph Viewer dialog box. 

Additionally, this tab reports the following Time History Point Statistics: 

   - End Point - This field displays the report point of the Time History. 

   - Count - This field displays the number of time steps in the transient simulation. 

- 2 On the Profiles tab, set the Graph Type to Hydraulic Grade and Air/Vapor Volume. 

80 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

- 3 Click Profile for the graph shown below. 



- 4 Leave this graph open while you move onto the next section. 

#### **Visualizing Simulated Results** 

HAMMER provides many ways to visualize the simulated results using a variety of graphs and animation layouts.  You must specify which points and paths (profiles) are of interest, as well as the frequency to output prior to a run, or HAMMER will not generate this output to avoid creating excessively large output files (.HOF). For small systems, you can specify each point and every time step, but this is not advisable for large water networks. 

For the same reason, HAMMER only generates the Animation Data (for on-screen animations) if you select this option in the Transient Solver Calculation Options as 

81 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

we previously did in Configuring the HAMMER Project - Calculation Options – Step #3. 

While you are still evaluating many different types or sizes of surge-protection equipment, you can often compare their effectiveness just by plotting the maximum transient head envelopes for most of your HAMMER runs.  At any time, or once you feel you are close to a definitive surge-control solution, you can generate animation data by performing the following steps. 

######  **Exercise: Generating animation data** 

Use HAMMER to generate the animation data files before you run the model by setting the Generate Animation Data option to True in the Transient Calculation Options, as we did in Configuring the HAMMER Project - Calculation Options - Step #3.  After the run, start the HAMMER Transient Results Viewer by selecting Analysis > Transient Results Viewer. Once you have generated the animation data files, you will be able to display the animations without running HAMMER again.  This saves a lot of time when comparing the results of several surge-control alternatives.  You can load the animation data files using the HAMMER Transient Results Viewer. 

Since we already have our graph open, we can jump right into the animation. 

Back in the graph dialog, you will see animation controls at the top of the dialog. 



**Note:** The three buttons from left to right are: Go to Start, Pause/Stop, and Play. 



1 Click the Play button to start the animation. 

82 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

- 2 At a certain time (19.5676 s), the animation dialog should look similar to the following figure: 



- 3 Close out of this graph when you are done viewing the animation. 

#### **Generate Report-Ready Graphs** 

Using the HAMMER Transient Results Viewer, you can plot a transient history at any point in the system to display the temporal variation of selected parameters (such as pressures and flow).  You can also plot a profile of selected variables along a particular path to display the spatial extent of transient phenomena. Finally you can compare the results of two similar graphs generated with or without protection, for example.  Let us start with the simulated results without protection. 

83 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

######  **Exercise: Viewing transient history** 

- 1 Select Analysis > Transient Results Viewer if you do not already have it open from before. 

- 2 Select the Time Histories tab. 

- 3 Select the following: 

Time History: P1:J1 

Graph Type: Hydraulic Grade and Flow 

- 4 Click Plot to display this transient history.  It should look similar to this: 



- 5 Keep this graph open and move on to the next exercise. 

84 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

######  **Exercise: Formatting the graphs** 



- 1 Click the Chart Setting icon to bring up the Chart Options dialog. 



**Note:** Here is where you can change all the properties of the graph. 

- 2 Click on Series at the top of the dialog. 



**Note:** Notice that you have a drop down menu containing the variables the graph is displaying, and below that you have all the options to change the way it looks. 

85 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline (metric) 

Mar-12 

Reviewing your Results 

- 3 Select Flow from the drop down menu. 



- 4 With Flow selected in the drop down menu click on Color. 

- 5 On the Color Editor change the color to any Green. 

- 6 Click OK. 



**Note:** You will see that the Flow display on the graph changed to a Green line. 



- 7 Back on the Chart Options dialog click the advance right button until you see Themes. 

86 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Reviewing your Results 

- 8 Click on Themes. 



- 9 Scroll through the list of available themes to see the available choices. 

- 10 Select the Business theme and view what the graph would look like in the Preview pane. 



- 11 As you can see, there are many settings you can change to make your graph appear the way you would like. Try changing other settings. 

- 12 Close all of the open windows until you get back to the drawing pane. 

- 13 Save your file. 

- 14 Complete the tables at the end of the workshop using the Properties manager and answer the questions. 

87 Transients in an Unprotected Pipeline (metric) Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Transients in an Unprotected Pipeline - Q and A** 

### **Results Tables** 

||**Alternatives**||||||
|---|---|---|---|---|---|---|
||**Without**<br>**Protection**|**HT-1**|**Air Valve**|**Surge Tank**<br>**with Check**<br>**Valve**|**Surge Tank**<br>**no Check**<br>**Valve**|**SRV**|
|Pressure (Maximum Transient) @ PJ2<br>(bars)|||||||
|Pressure (Minimum Transient) @ PJ2<br>(bars)|||**To be co**<br>**Pi**|**mpleted in W**<br>**peline Protect**|**orkshop:**<br>**ion**||
|Vapor Volume (Maximum Transient)<br>@ P2 (L)|||||||
|Head (Maximum Transient) @ P5 (m)|||||||



|**Alternatives**|**Junction**|**Pressure (Maxi**|**mum Transient**|**) (bars)**|||
|---|---|---|---|---|---|---|
||**PJ2**|**J2**|**J3**|**J4**|**J5**|**J6**|
|Steady State Pressure|**9.8**|**6.5**|**6.4**|**7.2**|**7.6**|**3.6**|
|Max. Allowable Pressure|**14**|**14**|**14**|**14**|**14**|**14**|
|Without Protection|||||||
|Hydropneumatic Tank(HT-1)|||||||
|Air Valve||**To b**|**e completed in**|**Workshop: Pip**|**eline Protection**||
|Surge Tank with Check<br>Valve|||||||



88 

Transients in an Unprotected Pipeline - Q and A 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Results Tables 

|**Alternatives**|**Junction**|**Pressure (Maxi**|**mum Transient**|**) (bars)**|||
|---|---|---|---|---|---|---|
||**PJ2**|**J2**|**J3**|**J4**|**J5**|**J6**|
|Steady State Pressure|**9.8**|**6.5**|**6.4**|**7.2**|**7.6**|**3.6**|
|Max. Allowable Pressure|**14**|**14**|**14**|**14**|**14**|**14**|
|Surge Tank no Check Valve||**To b**|**e completed in**|**Workshop: Pip**|**eline Protection**||
|SRV|||||||



89 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline - Q and A 

Mar-12 

Workshop Review 

### **Workshop Review** 

Now that you have completed this workshop, let’s measure what you have learned. 

#### **Questions** 

- **1** Where does the largest vapor pocket occur and what is its maximum volume?  Explain the mechanism behind the development of this vapor pocket. 

Enter your answer below: 

- **2** Select the Time History for P1:J1and click on “Animate”.  When does the vapor cavity at junction J1start to form and when does it close? 

Enter your answer below: 

- **3** What happens to the flow at J1 at about 13.5 sec and what effect does this have on the vapor cavity? 

Enter your answer below: 

**Hint** : In the Transient Results Graph you can click on the Data tab for easier viewing of graph values. 

90 Transients in an Unprotected Pipeline - Q and A Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Workshop Review 

- **4** Considering your answers to the previous questions and the role of the vapor cavity in the transient event, what are some of the possible strategies for reducing the upsurge? 

Enter your answer below: 

###### **5** Why is the pump (PMP1) not subjected to the transient upsurge? 

Enter your answer below: 

91 Copyright © 2012 Bentley Systems, Incorporated 

Transients in an Unprotected Pipeline - Q and A 

Mar-12 

Workshop Review 

#### **Answers** 

||**Alternatives**||||||
|---|---|---|---|---|---|---|
||**Without**<br>**Protection**|**HT-1**|**Air Valve**|**Surge Tank**<br>**with Check**<br>**Valve**|**Surge Tank**<br>**no Check**<br>**Valve**|**SRV**|
|Pressure (Maximum Transient) @ PJ2<br>(bars)|31||||||
|Pressure (Minimum Transient) @ PJ2<br>(bars)|-1.0||**To be co**<br>**Pi**|**mpleted in W**<br>**peline Protect**|**orkshop:**<br>**ion**||
|Vapor Volume (Maximum Transient)<br>@ P2 (L)|446||||||
|Head (Maximum Transient) @ P5 (m)|723||||||



|**Alternatives**|**Junction**|**Pressure (Maxi**|**mum Transient**|**) (bars)**|||
|---|---|---|---|---|---|---|
||**PJ2**|**J2**|**J3**|**J4**|**J5**|**J6**|
|Steady State Pressure|**9.8**|**6.5**|**6.4**|**7.2**|**7.6**|**3.6**|
|Max. Allowable Pressure|**14**|**14**|**14**|**14**|**14**|**14**|
|Without Protection|31|27|27|28|31|26|
|Hydropneumatic Tank(HT-1)|||||||
|Air Valve|||||||
|Surge Tank with Check<br>Valve||**To be co**|**mpleted in Wor**|**kshop: Pipeline**|**Protection**||
|Surge Tank no Check Valve<br>SRV|||||||



92 Transients in an Unprotected Pipeline - Q and A Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

Workshop Review 

- **1** Where does the largest vapor pocket occur and what is its maximum volume?  Explain the mechanism behind the development of this vapor pocket. 

The largest vapor pocket occurs at J1 with a maximum volume of 446.4 L. Water is being pumped up a steep rise to a well-defined vertical bend or “knee” at node J1, after which the pipe turns about 90 degrees to level out with a slight fall.  After the pump trips and the vapor pocket forms, water being pumped up the rise decelerates at a much faster rate than the water in the more level pipeline after the knee.  This causes the vapor pocket to expand at the knee (J1) as these columns of water separate. 

- **2** Select the Time History for P1:J1and Animate it.  When does the vapor cavity at junction J1start to form and when does it close? 

The first vapor cavity opens at about 8.8 sec (when flow reaches zero) and closes just after about 13.8 sec., when a large pressure rise occurs. 

**Note: Transient Tip** : The first vapor pocket at a well-defined knee (J1) usually opensup as flow in the upstream segment (P1) reaches zero: the departing liquid column in the downstream pipe (P2) actually leaves a vacuum behind at J1. This allows you to correlate the flow and volume graphs to get the approximate start time of 8.8 seconds. 

- **3** What happens to the flow at J1 at about 13.8 sec and what effect does this have on the vapor cavity? 

Flow returns from Res2 and results in a negative flow, or flow reversal, at J1.  This in turn causes the vapor pocket to collapse and results in a high pressure upsurge. 

- **4** Considering your answers to the previous questions and the role of the vapor cavity in the transient event, what are some of the possible strategies for reducing the upsurge? 

Mitigating the formation of the vapor cavity is at the heart of the solution. This could be achieved by installing a surge tank or gas vessel to ensure that water is supplied to the area where the cavity would form “without surge protection”. 

- **5** Why is the pump (PMP1) not subjected to the transient upsurge? 

The time history at the pump shows that the check valve closes before these pressure waves reach the pump (zero flow), effectively isolating it from the system and protecting it against damage. 

93 Transients in an Unprotected Pipeline - Q and A Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Causes of Transients** 



94 

Causes of Transients 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





95 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





96 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





97 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





98 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





99 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





100 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





101 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





102 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





103 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





104 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





105 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





106 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





107 Causes of Transients 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





108 Causes of Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Surge Protection: Tanks and Valves** 



109 

Surge Protection: Tanks and Valves 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





110 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





111 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





112 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





113 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





114 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





115 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





116 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





117 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





118 Surge Protection: Tanks and Valves Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Pipeline Protection (metric)** 

### **Module Overview** 

You will use the model you created in _Workshop: Transients in a Simple Pipeline_ , to investigate surge protection strategies.  You will use alternatives and scenarios to lay out different surge protection devices and review the transient effects they have on the network. 

### **Module Prerequisites** 

- Fundamental knowledge of hydraulic transients 

- Basic Transient Modeling 

- Completion of the previous module 

### **Module Objectives** 

After completing this module, you will be able to: 

- Add and define different surge protection equipment to a model 

- Create multiple surge protection strategies within a single file using alternatives and scenarios 

- Review and analyze the effect surge equipment can have on a model 

119 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Problem Statement 

### **Problem Statement** 

Using the model that you created in _Workshop: Transients in an Unprotected Pipeline_ , you will use HAMMER to investigate surge protection strategies.  You can do this using the following steps: 

- 1 Select and model different surge-protection equipment to control transient pressures and predict the time required for friction to attenuate the transient energy. 

- 2 Present your results graphically to explain your surge-control strategy and recommendations for detailed design. 

#### **Description** 

Certain protective equipment such as a hydropneumatic tank (also known as a gas vessel or air chamber), air valve, or a one-way surge tank can be installed at local high points to control hydraulic transients. 

It is clear that high pressures are caused by the sudden collapse of a vapor pocket at junction J1.  You could install a Hydropneumatic Tank at junction J1 to supply flow into the pipeline upon the power failure, keeping the upstream water column moving and minimizing the size of the vapor pocket at the high point (or even preventing it from forming).  You can test this theory by simulating the system again using HAMMER and comparing the results with those of the unprotected run. 

**Note:** In the upcoming exercises, you could morph J1 into each different type of surge protection equipment and save each model as a different file.  However, using that method, you will end up with multiple similar files.  To better manage our data, we will be using Bentley HAMMER’s ability to create multiple scenarios and alternatives within the same file. 

120 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

### **Adding Surge-Protection Equipment** 

In this workshop you will go through adding different types of surge-protection equipment to your model.  You will also be graphing the results of the system after the new equipment has been added. 

######  **Exercise: Getting started** 

   - 1 Select File > Open. 

   - 2 Browse to where you saved Transients.wtg and open it. 

- **Note:** If you did not complete Transients.wtg, open TransientsSolutionSI.wtg found in C:\Bentley Workshop\HAMMER V8i metric\Solutions. 

   - 3 Select File > Save As and save the file with a name of **PipelineProtection.wtg** . 

We are doing this so you have a back-up of the first workshop. 

We will start this workshop by creating the alternatives. 

######  **Exercise: Creating new alternatives** 

- 1 Select Analysis > Alternatives. 

We will be creating a new Active Topology Alternative for the new hydropneumatic tank and adjoining pipes. 

- 2 In the Alternatives manager, click the + sign in front of Active Topology. 

You should see the Base Active Topology that we were previously using. 

- 3 Right click on Base Active Topology and select New > Child Alternative. 

This will create a new child alternative beneath Base Active Topology named Active Topology Alternative - 1. 

- 4 Right click on Active Topology Alternative – 1 and select Rename. 

- 5 Rename the alternative to **Without Surge Protection** . 

- 6 Right click on Without Surge Protection and select New > Child Alternative to create a new child alternative. 

121 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

- 7 Rename this new child alternative to **With Hydropneumatic Tank** . 



**Note:** Notice that Base Active Topology has a red checkmark in front of it; this means that it is still the current alternative that is being used. 

We will now need to create some scenarios to utilize these new alternatives that we just created. 

######  **Exercise: Creating active topology scenarios** 

- 1 Select Analysis > Scenarios to bring up the Scenarios manager. 

- 2 In the Scenarios manager, right click on Base and select New > Child Scenario. 

- 3 Name this new scenario **Existing Without Surge Protection** . 

- 4 Double click on Existing Without Surge Protection to bring up the Properties manager. 

- 5 Change the Active Topology alternative to Without Surge Protection. 



- 6 Back in the Scenarios manager, right click on Existing Without Surge Protection and select New > Child Scenario. 

- 7 Rename the new scenario to **With Hydropneumatic Tank** . 

- 8 Double click on the With Hydropneumatic Tank scenario to bring up the Properties manager if it is not already up. 

122 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 9 Change the Active Topology alternative to With Hydropneumatic Tank. 





- 10 Make sure that Base still has a checkmark in the folder icon as shown in the screenshot above.  If Base does not have the checkmark, right click on Base and select Make Current. 

- 11 Close the Scenarios manager. 

#### **Adding a Hydropneumatic Tank** 

Back in the drawing pane, we are now ready to add in the new Hydropneumatic tank. 

- **Exercise: Laying out a hydropneumatic tank** 



- 1 Click the Hydropneumatic Tank button in the Layout toolbar and place the tank just below junction J1. 

The default name HT-1 should be fine. 

123 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 2 Select the Pipe tool, draw a pipe from PJ2 to HT-1 and from HT-1 to J2. 





   - 3 Right click, select Done, and then click the Select tool. 

   - 4 Rename the new pipes to match the screen above. 

   - 5 To have the next set of pipes come in named correctly, select Tools > Options > Labeling. 

   - 6 Set the Next number for Pipe to 10 and click OK to save. 

- **Note:** The two pipes will have almost exactly the same properties as P1 and P2, respectively. 

   - 7 Enter the following for P-8 and P-9 using FlexTables or the Properties dialog: 

|**Label **|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User**<br>**Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|**Wave Speed**<br>**(m/s)**|
|---|---|---|---|---|---|---|---|---|
|P-8|PJ2|HT-1|True|20|600|Ductile Iron|130|1,252.33|
|P-9|HT-1|J2|True|380|600|Ductile Iron|130|1,252.33|



124 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 



- 8 Enter the following data for the HT-1: 

Elevation (Base) (m): 408 Operating Range Type: Elevation HGL (Initial) (m): 464 Liquid Volume (Initial) (m<sup>3</sup> ): 14.15 

**Note:** Make sure you change the units before entering the above data. Right click the units and select Units and Formatting. 

Elevation (m): 408 Volume (Tank) (m<sup>3</sup> ): 20 Tank Calculation Model: Gas Law Model Hydropneumatic Tank Type: Sealed Diameter (Tank Inlet Orifice) (mm): 300 Ratio of Losses: 2.5 Gas Law Exponent: 1.2 Has Bladder?: True Pressure (Gas-Preset) (bars): 0.0 

125 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

Minor Loss Coefficient (Outflow): 1.0 



Your drawing should now look something like this when looking at the Base scenario: 



We now need to switch to each of our scenarios and set the elements that do not belong in that scenario to an inactive status. 

######  **Exercise: Creating new active topology selections** 

- 1 Click in the Scenarios toolbar which is currently showing Base and select Existing Without Surge Protection from the dropdown box: 



126 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 



- 2 Select Tools > Active Topology Selection or click the Active Topology Selection tool from the toolbar. 

This will bring up the Select toolbar. 





- 3 Make sure that the Add button is selected. 

- 4 In the drawing select HT-1 and notice that P-8 and P-9 get selected automatically. 



- 5 Click the green Done button from the Select toolbar. 

**Note:** Those 3 elements should now have turned gray in the drawing to signify that they are inactive and the drawing should look like this: 



**Note:** If you do not wish to see the inactive elements, you do not have to display them.  To not display the inactive elements, select Tools > Options.  On the Options dialog select the Global tab, uncheck the checkbox in front of the Display Inactive Topology field.  Click OK to close the Options dialog. 

Next, we will need to set P1, J1, and P2 inactive for the With Hydropneumatic Tank scenario. 

- 6 Click in the Scenarios dropdown menu (which is currently showing Existing Without Surge Protection) and select With Hydropneumatic Tank. 

- 7 Select Tools > Active Topology Selection. 



- 8 On the Select toolbar, click on the Remove button. 

- 9 In the drawing, click on P-8 and P-9 to deselect them as well as HT-1; you will notice that they are no longer highlighted. 

- 10 On the Select toolbar, click on the Add button. 

- 11 In the drawing, click on J1 to highlight P1, P2, and J1 at the same time and click Done. 

127 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

Your drawing should now look like this: 



We will now need to create a profile that includes the new pipes. 

######  **Exercise: Creating profiles** 

- 1 Select View > Profiles to bring up the Profiles manager. 



**Note:** Notice that there is already a profile named Main listed in the magager from the previous workshop, but this profile does not include the new pipes. 



- 2 Click the New button to create a new profile. 

- 3 On the Profile Setup dialog that comes up, click on Select From Drawing. 

- 4 In the drawing, click on the pipes PMP1D, P-8, P-9, P3, P4, P5, P6 and P7 to highlight and select them (along with their connected nodes). 

- 5 After you have selected all of the listed pipes, click Done on the Select toolbar. 

**Note:** All of the pipes and nodes that you have selected will now be listed in the Profile Setup dialog. 

- 6 Click the Open Profile button to view your profile. 

128 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 7 Click OK on the Profile Series Options dialog that opens up. 



- 8 Click the red X in the top right corner to close the Profile. 

- 9 Back on the Profiles manager, right-click on Profile – 1 and select Rename. 

- 10 Rename the profile to **Main with HT-1** . 

- 11 Right click on Main with HT-1 and make sure that there is a checkmark in front of Transient Report Path. 

- 12 If there is not a checkmark, then simply click on the Transient Report Path option from the right click menu. 



129 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

13 Close the Profiles manager. 

14 Click File > Save to save your model. 

######  **Exercise: Computing** 

- 1 Make sure that the With Hydropneumatic Tank scenario is the active scenario and then select Analysis > Compute Initial Conditions to compute the initial steady state values. 

**Note:** You can choose to always compute initial conditions by selecting that option from the bottom of the Analysis menu. When it is selected you should see a checkmark in front of Always Compute Initial Conditions. 

- 2 Close the Calculation Summary dialog after the calculations are completed. 



- 3 Click the Compute button or select Analysis > Compute to compute the network. 

- 4 Close the Transient Calculation Summary and User Notification dialogs if they open up. 



- 5 Select Analysis > Transient Results Viewer or click the Transient Results Viewer button on the toolbar. 

- 6 On the Transient Results Viewer, set the Profile to Main with HT-1 and click Profile to view the Maximum Transient Envelope. 

130 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

If you have done everything correctly, the maximum transient head envelope for the With Hydropneumatic Tank scenario should look as follows: 



- 7 Animate the profile to review the results. 

- 8 Close out of the plot and the Transient Results Viewer, and fill in the results table at the end of this workshop. 

#### **Adding an Air Valve** 

######  **Exercise: Creating the air valve active topology alternative** 

We will need to create a new alternative and scenario to add an air valve to our model. 

- 1 Select Analysis > Alternatives to open the Alternatives manager. 

131 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 2 In the Alternatives manager, under the Active Topology alternatives, right click on Without Surge Protection and select New > Child Alternative. 

- 3 Rename this alternative to **With Air Valve** . 



- 4 Select Analysis > Scenarios to open the Scenarios manager. 

- 5 Right click on Existing Without Surge Protection and select New > Child Scenario. 

- 6 Name the scenario **With Air Valve** . 

- 7 Double click With Air Valve to bring up the Properties manager. 

- 8 Change the Active Topology alternative to With Air Valve. 



- 9 Close the Alternatives and Scenarios managers. 

- 10 Back in the drawing pane; change the active scenario to Base in the Scenarios dropdown menu. 

######  **Exercise: Adding an air valve** 



- 1 Click on the Air Valve tool in the Layout toolbar to select it. 

- 2 Lay out an air valve in the drawing under HT-1. 

The default name of AV-1 is fine. 

- 3 Click on the Pipe tool in the Layout toolbar and draw a pipe from PJ2 to AV-1 and from AV-1 to J2. 

- 4 Right click, select Done, and then click the Select tool. 

132 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

The pipes should be named P-10 and P-11. 



- 5 Enter these values into the properties of P-10 and P-11: 

|**Label **|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User**<br>**Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|**Wave Speed**<br>**(m/s)**|
|---|---|---|---|---|---|---|---|---|
|P-10|PJ2|AV-1|True|20|600|Ductile Iron|130|1,252.33|
|P-11|AV-1|J2|True|380|600|Ductile Iron|130|1,252.33|





- 6 Enter these values for the properties of AV-1: 

Elevation (m): 408 

Air Valve Type: Triple Acting 

Trigger to Switch Outflow Orifice Size: Transition Volume 

Transition Volume (L): 42.5 

133 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

Air Flow Calculation Method: Orifice Diameter Diameter (Small Air Outflow Orifice) (mm): 5.0 Diameter (Large Air Outflow Orifice) (mm): 13 

Diameter (Air Inflow Orifice) (mm): 102 



We will now need to set the elements that do not belong in each scenario inactive again. 

######  **Exercise: Creating another active topology selection** 

- 1 Change the scenario to Existing Without Surge Protection. 

- 2 Select Tools > Active Topology Selection. 

- 3 Click on AV-1 to select P-10, AV-1 and P-11 at the same time, and then click Done. 

Your drawing should look similar to the one below if you have your inactive topology set to display. 



134 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

   - 4 Change the scenario to With Hydropneumatic Tank. 

- **Note:** Notice that P-10, AV-1 and P-11 are already inactive in this scenario.  This is because this scenario’s Active Topology alternative, With Hydropneumatic Tank is a child of the Without Surge Protection active topology alternative. This means that With Hydropneumatic Tank inherits its properties from its parent—which in this case is Without Surge Protection.  This ability of child alternatives and scenarios to inherit the properties of their parents can be very powerful and save you a lot of data entry. 

   - 5 Change the scenario to With Air Valve. 

- **Note:** Notice that this scenario currently looks exactly like Existing Without Surge Protection. As we just mentioned, this is because it inherited all of its current attributes from its parent. 

   - 6 Select Tools > Active Topology Selection. 

   - 7 On the Select toolbar, click on the Remove button. 

   - 8 In the drawing, click on P-10 and P-11, to deselect P-10, AV-1, and P-11; you will notice that they are no longer highlighted. 

   - 9 On the Select toolbar, click on the Add button. 

   - 10 In the drawing, click on J1 to highlight P1, P2, and J1 at the same time and click Done. 

Your drawing should now look like this: 



######  **Exercise: Creating profiles** 

- 1 Select View > Profiles to bring up the Profiles manager. 



- 2 Click the New button to create a new profile. 

- 3 On the Profile Setup dialog that comes up, click on Select From Drawing. 

- 4 In the drawing, click on the pipes PMP1D, P-10, P-11, P3, P4, P5, P6 and P7 to highlight and select them (along with their connected nodes). 

- 5 After you have selected all of the listed pipes, click Done on the Select toolbar. 

135 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- **Note:** All of the pipes and nodes that you have selected will now be listed in the Profile Setup dialog. 

   - 6 Click the Open Profile button to view your profile. 

   - 7 Click OK on the Profile Series Options dialog that opens up. 



- 8 Click the red X in the top right corner to close the Profile. 

- 9 Back on the Profiles manager, right-click on Profile – 1 and select Rename. 

- 10 Rename the profile to **Main with AV-1** . 

- 11 Right click on Main with AV-1 and make sure that there is a checkmark in front of Transient Report Path. 

- 12 If there is not a checkmark, then simply click on the Transient Report Path option from the right click menu. 

- 13 Close the Profiles manager. 

- 14 Click File > Save to save your model. 

######  **Exercise: Computing the network** 

- 1 Select Analysis > Compute Initial Conditions to compute the initial conditions. 

- 2 Close the Calculation Summary dialog when it comes up. 

136 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 3 Select Analysis > Compute to compute the model. 

- 4 Close the Transient Calculation Summary and User Notification dialogs if they open up. 



- 5 Select Analysis > Transient Results Viewer or select the icon from the toolbar. 

- 6 On the Profiles Tab of the Transient Results Viewer dialog, make sure the Profile is set to Main with AV-1 and click Profile. 

Your maximum transient envelope should look like this: 



- 7 Click File > Save to save the file. 

- 8 Fill in the results table at the end of this workshop. 

137 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

#### **Adding a Simple Surge Tank with Check Valve** 

We will need to create new alternatives and a new scenario to add a simple surge tank to the model. 

- **Exercise: Creating new alternatives for the surge tank with check valve** 

   - 1 Select Analysis > Alternatives. 

   - 2 Right click on the Without Surge Protection active topology alternative and select New > Child Alternative. 

   - 3 Rename this alternative to **With Surge Tank** . 

**Note:** Because in the next part of this workshop, we will be analyzing this surge tank without a check valve, we will also need to create new Physical, Initial Settings, and Transient alternatives. 

- 4 Under the Physical alternatives category, right click on Base Physical and select New > Child Alternative. 

- 5 Rename the new Physical alternative to **Surge Tank with Check Valve** . 

- 6 Under the Initial Settings alternatives, right click on Base Initial Settings and select New > Child Alternative. 

- 7 Rename the new Initial Settings alternative to **Surge Tank with Check Valve** . 

- 8 Under the Transient alternatives, right click on Base Transient and select New > Child Alternative. 

138 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 9 Rename the new Transient alternative to **Surge Tank with Check Valve** . 



######  **Exercise: Assigning the new alternatives to a new scenario** 

- 1 Select Analysis > Scenarios. 

- 2 In the Scenarios manager, right click on Existing Without Surge Protection and select New > Child Scenario. 

- 3 Name the new scenario **With Surge Tank with Check Valve** . 

- 4 Double click on With Surge Tank with Check Valve to bring up the Properties manager. 

- 5 Set the following alternatives for this scenario: 

Active Topology: With Surge Tank 

Physical: Surge Tank with Check Valve 

Initial Settings: Surge Tank with Check Valve 

139 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

Transient: Surge Tank with Check Valve 



- 6 Close the Alternative and Scenario dialogs. 

######  **Exercise: Laying out the surge tank** 

- 1 Change the current scenario to Base. 



- 2 Click on the Surge Tank icon in the Layout toolbar. 

- 3 Layout the surge tank below AV-1 in the drawing. 

- 4 Click on the Pipe icon in the layout toolbar and draw a pipe from PJ2 to ST1 and from ST-1 to J2. 

- 5 Right click and select Done. 



140 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

######  **Exercise: Entering data for the new pipes and surge tank** 

- 1 Enter the following data for pipes P-12 and P-13: 

|**Label **|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User**<br>**Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|**Wave Speed**<br>**(m/s)**|
|---|---|---|---|---|---|---|---|---|
|P-12|PJ2|ST-1|True|20|600|Ductile Iron|130|1,252.33|
|P-13|ST-1|J2|True|380|600|Ductile Iron|130|1,252.33|





2 Enter the following data for ST-1: Operating Range Type: Elevation Elevation (Base) (m): 408 Elevation (Minimum) (m): 408 Elevation (Initial) (m): 414 Elevation (Maximum) (m): 415 Use High Alarm?: True Elevation (High Alarm) (m): 414.75 Elevation (m): 408 

141 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

Section: Circular 

Diameter (m): 1.5 Surge Tank Type: Simple Has Check Valve?: True 

Diameter (Orifice) (mm): 200 Headloss Coefficient: 1 



######  **Exercise: Setting new active topology alternative** 

We need to set the elements that are not needed for the Existing Without Surge Protection and With Surge Tank With Check Valve scenarios to an inactive status. 

- 1 Change the scenario to Existing Without Surge Protection. 

- 2 Select Tools > Active Topology Selection to bring up the Select toolbar. 

- 3 Make sure the Add button is selected on the Select toolbar. 

142 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 



- 4 Click on ST-1 to select P-12, ST-1, and P-13 at the same time, and then click Done on the Select toolbar. 

Your Existing Without Surge Protection scenario drawing should look like the following screen: 



- 5 Change the scenario to With Surge Tank with Check Valve. 

- 6 Select Tools > Active Topology Selection. 



- 7 On the Select toolbar, click on the Remove. 

- 8 In the drawing, click on P-12 and P-13, to deselect P-12, ST-1, and P-13 and then click Done. 

You will notice that they are no longer highlighted. 

- 9 On the Select toolbar, click on the Add button. 

- 10 In the drawing, click on J1 to highlight P1, P2, and J1 at the same time and click Done. 

Your drawing should now look like this 



######  **Exercise: Creating a new profile** 

- 1 Select View > Profiles to bring up the Profiles manager. 



- 2 Click the New button to create a new profile. 

- 3 On the Profile Setup dialog that comes up, click on Select From Drawing. 

143 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 4 In the drawing, click on the pipes PMP1D, P-12, P-13, P3, P4, P5, P6 and P7 to highlight and select them (along with their connected nodes). 

- 5 After you have selected all of the listed pipes, click Done on the Select toolbar. 

**Note:** All of the pipes and nodes that you have selected will now be listed in the Profile Setup dialog. 

- 6 Click the Open Profile button to view your profile. 

- 7 Click OK on the Profile Series Options dialog that opens up. 



- 8 Click the red X in the top right corner to close the Profile. 

- 9 Back on the Profiles manager, right-click on Profile – 1 and select Rename. 

- 10 Rename the profile to **Main with ST-1** . 

- 11 Right click on Main with ST-1 and make sure that there is a checkmark in front of Transient Report Path. 

- 12 If there is not a checkmark, then simply click on the Transient Report Path option from the right click menu. 

- 13 Close the Profiles manager. 

- 14 Click File > Save to save your model. 

144 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

######  **Exercise: Computing** 

- 1 Make sure that the current scenario is set to With Surge Tank With Check Valve. 

- 2 Select Analysis > Compute Initial Conditions. 

- 3 Close the Calculation Summary dialog when it comes up. 

- 4 Select Analysis > Compute. 

- 5 Close the Transient Calculation Summary and User Notification dialogs after the calculation is complete. 

- 6 Select Analysis > Transient Results Viewer. 

- 7 Plot the Main with ST-1 profile. 



- 8 Click File > Save to save the model. 

- 9 Fill in the results table at the end of this section. 

145 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

#### **Adding a Simple Surge Tank without Check Valve** 

- **Exercise: Creating new alternatives for the surge tank without check valve** 

We will need to create new Physical and Transient alternatives and a new scenario to change the properties of the surge tank ST-1 in the model. 

- 1 Select Analysis > Alternatives. 

- 2 In the Alternatives manager, under the Physical alternatives category, right click on Surge Tank with Check Valve and select New > Child Alternative. 

- 3 Rename the new physical alternative **Surge Tank – No Check Valve** . 

- 4 Under the Initial Settings alternatives, right click on Surge Tank with Check Valve and select New > Child Alternative. 

- 5 Rename the new alternative to **Surge Tank—No Check Valve** . 

- 6 Under the Transient alternatives, right click on Surge Tank with Check Valve and select New > Child Alternative. 

- 7 Rename the new Transient alternative **Surge Tank – No Check Valve** . 



######  **Exercise: Assigning the new alternatives to a new scenario** 

- 1 Select Analysis > Scenarios. 

- 2 In the Scenarios manager, right click on With Surge Tank with Check Valve and select New > Child Scenario. 

146 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 3 Name the new scenario **Surge Tank – No Check Valve** . 

- 4 Double click on the Surge Tank – No Check Valve scenario to bring up the Properties manager. 

- 5 Set the following: 

Physical: Surge Tank – No Check Valve 

Initial Settings: Surge Tank – No Check Valve 

Transient: Surge Tank – No Check Valve 



######  **Exercise: Entering new data for the surge tank** 

- 1 Close the Alternative and Scenario managers. 

- 2 Change the current scenario to Surge Tank – No Check Valve. 

- 3 Double click on ST-1 to bring up its Properties manager. 

- 4 Enter the following data for ST-1: 

Operating Range Type: Elevation Elevation (Base) (m): 408 Elevation (Minimum) (m): 408 Elevation (Initial) (m): 464 Elevation (Maximum) (m): 469 Use High Alarm?: True 

147 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

Elevation (High Alarm) (m): 468 Elevation (m): 408 Section: Circular Diameter (m): 1.5 Surge Tank Type: Simple Has Check Valve?: False Weir Coefficient ((m^0.5)/s): 1.38 Weir Length (m): 0.3 Diameter (Orifice) (mm): 200 Ratio of Losses: 2.5 Headloss Coefficient: 1 



- 5 Select File > Save to save the model. 

148 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

######  **Exercise: Computing** 

- 1 Make sure that the Scenario is set to Surge Tank – No Check Valve. 

- 2 Select Analysis > Compute Initial Conditions to compute the initial conditions. 

- 3 Close the Calculation Summary dialog when it comes up. 

- 4 Select Analysis > Compute to compute the model. 

- 5 Close the Transient Calculation Summary and User Notification dialogs after the calculation is complete. 

- 6 Select Analysis > Transient Results Viewer. 

- 7 Click No on the Transient Results Viewer message dialog that comes up. We want to open the old TRV dialog. 

- 8 Plot the Main with ST-1 path. 



###### 9 Click File > Save to save the model. 

149 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

- 10 Fill in the results table at the end of this section. 

#### **Adding a Surge Relief Valve** 

- **Exercise: Creating new alternatives** 

   - 1 Select Analysis > Alternatives. 

We will be creating a new Active Topology Alternative for the new surge relief valve and adjoining pipes. 

- 2 In the Alternatives manager, click the + sign in front of Active Topology. 

- 3 Right click on Without Surge Protection and select New > Child Alternative. 

- 4 Right click on Active Topology Alternative – 1 and select Rename. 

- 5 Rename the alternative to **With SRV** . 



We will now need to create a new scenariosome scenarios to utilize these new alternatives that we just created. 

######  **Exercise: Creating active topology scenarios** 

- 1 Select Analysis > Scenarios to bring up the Scenarios manager. 

- 2 In the Scenarios manager, right click on Existing Without Surge Protection and select New > Child Scenario. 

- 3 Name this new scenario **With SRV** . 

- 4 Double click on With SRV to bring up the Properties manager. 

150 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

- 5 Change the Active Topology alternative to With SRV. 



- 6 Close the Scenarios manager. 

We are now ready to add in the new surge relief valve. 

- **Exercise: Laying out a surge relief valve** 

   - 1 Make sure the current scenario is Base. 



- 2 Click the Surge Valve button in the Layout toolbar and place the valve just above junction J1. 

The default name SV-1 should be fine. 

- 3 Select the Pipe tool, draw a pipe from PJ2 to SV-1 and from SV-1-1 to J2. 





- 4 Right click, select Done, and then click the Select tool. 

151 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Adding Surge-Protection Equipment 

- 5 Enter the following for P-14 and P-15 using FlexTables or the Properties dialog: 

|**Label **|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User**<br>**Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|**Wave Speed**<br>**(m/s)**|
|---|---|---|---|---|---|---|---|---|
|P-14|PJ2|SV-1|True|20|600|Ductile Iron|130|1,252.33|
|P-15|SV-1|J2|True|380|600|Ductile Iron|130|1,252.33|





- 6 Enter the following data for the SV-1: 

Elevation (m): 408 SAV/SRV Type: Surge Relief Valve Threshold Pressure (SRV) (bars): 6 

Diameter (SRV) (mm): 203 

152 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

###### Spring Constant (SRV) (N/mm): 80 



- 7 Save your model. 

We now need to switch to each of our scenarios and set the elements that do not belong in that scenario to an inactive status. 

######  **Exercise: Creating new active topology selections** 

- 1 Select Existing Without Surge Protection as the current scenario. 



- 2 Select Tools > Active Topology Selection or click the Active Topology Selection tool from the toolbar. 

This will bring up the Select toolbar. 



- 3 Make sure that the Add button is selected. 

- 4 In the drawing select SV-1 to select P-14, SV-1, and P-15 at the same time. 



- 5 Click the green Done button from the Select toolbar. 

Next, we will need to set P1, J1, and P2 inactive for the With SRV scenario. 

- 6 Click in the Scenarios dropdown menu and select With SRV. 

- 7 Select Tools > Active Topology Selection. 



- 8 On the Select toolbar, click on the Remove button. 

- 9 In the drawing, click on P-14 and P-15 to deselect them as well as SV-1. 

- 10 On the Select toolbar, click on the Add button. 

- 11 In the drawing, click on J1 to highlight P1, P2, and J1 at the same time and click Done. 

153 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

Your drawing should now look like this: 



We will now need to create a profile that includes the new pipes. 

######  **Exercise: Creating profiles** 

- 1 Select View > Profiles to bring up the Profiles manager. 



- 2 Click the New button to create a new profile. 

- 3 On the Profile Setup dialog that comes up, click on Select From Drawing. 

- 4 In the drawing, click on the pipes PMP1D, P-14, P-15, P3, P4, P5, P6 and P7 to highlight and select them (along with their connected nodes). 

- 5 After you have selected all of the listed pipes, click Done on the Select toolbar. 

**Note:** All of the pipes and nodes that you have selected will now be listed in the Profile Setup dialog. 

- 6 Click the Open Profile button to view your profile. 

154 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 7 Click OK on the Profile Series Options dialog that opens up. 



- 8 Click the red X in the top right corner to close the Profile. 

- 9 Back on the Profiles manager, right-click on Profile – 1 and select Rename. 

- 10 Rename the profile to **Main with SV-1** . 

- 11 Right click on Main with SV-1 and make sure that there is a checkmark in front of Transient Report Path. 

- 12 If there is not a checkmark, then simply click on the Transient Report Path option from the right click menu. 

- 13 Close the Profiles manager. 

- 14 Click File > Save to save your model. 

######  **Exercise: Computing** 

- 1 Make sure that the Scenario is set to With SRV. 

- 2 Select Analysis > Compute Initial Conditions to compute the initial conditions. 

- 3 Close the Calculation Summary dialog when it comes up. 

- 4 Select Analysis > Compute to compute the model. 

155 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection (metric) 

Mar-12 

Adding Surge-Protection Equipment 

- 5 Close the Transient Calculation Summary and User Notification dialogs after the calculation is complete. 

- 6 Select Analysis > Transient Results Viewer. 

- 7 Plot the Main with SV-1 profile. 



- 8 Click File > Save to save the model. 

- 9 Fill in the results table and answer the questions at the end of this workshop. 

156 

Pipeline Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 



# **Pipeline Protection - Q and A** 

### **Results Tables** 

||**Alternative**|**s**|||||
|---|---|---|---|---|---|---|
||**Without**<br>**Protection**|**HT-1**|**Air Valve**|**Surge Tank**<br>**with Check**<br>**Valve**|**Surge Tank**<br>**no Check**<br>**Valve**|**SRV**|
|Pressure (Maximum Transient) @ PJ2<br>(bars)|31||||||
|Pressure (Minimum Transient) @ PJ2<br>(bars)|-1.0||||||
|Vapor Volume (Maximum Transient)<br>@ P2/P-9/P-11/P-13/P-15 (L)|446||||||
|Head (Maximum Transient) @ P5 (m)|723||||||



|**Alternatives**|**Junction**|**Pressure (Maxi**|**mum Transient**|**) (bars)**|||
|---|---|---|---|---|---|---|
||**PJ2**|**J2**|**J3**|**J4**|**J5**|**J6**|
|Steady State Pressure|**9.8**|**6.5**|**6.4**|**7.2**|**7.6**|**3.6**|
|Max. Allowable Pressure|**14**|**14**|**14**|**14**|**14**|**14**|
|Without Protection|31|27|27|28|31|26|
|Hydropneumatic Tank(HT-1)|||||||
|Air Valve|||||||
|Surge Tank with Check<br>Valve|||||||



157 

Pipeline Protection - Q and A 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Results Tables 

|**Alternatives**|**Junction**|**Pressure (Maxi**|**mum Transient**|**) (bars)**|||
|---|---|---|---|---|---|---|
||**PJ2**|**J2**|**J3**|**J4**|**J5**|**J6**|
|Steady State Pressure|**9.8**|**6.5**|**6.4**|**7.2**|**7.6**|**3.6**|
|Max. Allowable Pressure|**14**|**14**|**14**|**14**|**14**|**14**|
|Surge Tank no Check Valve|||||||
|SRV|||||||



158 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection - Q and A 

Mar-12 

Workshop Review 

### **Workshop Review** 

Now that you have completed this workshop, let’s measure what you have learned. 

#### **Questions** 

- **1** What effect does placing the gas vessel at J1 have on the formation of the vapor cavity and the transient pressure spike? 

Enter your answer below: 

- **2** Based on your investigation of other protection equipment, what might be the most effective strategy for protecting the pipeline from transient pressures? 

Enter your answer below: 

- **3** How effective is the SRV in reducing the formation of vapor cavities? 

Enter your answer below: 

159 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection - Q and A 

Mar-12 

Workshop Review 

#### **Workshop Results** 

|||**Alternativ**|**es**|||||
|---|---|---|---|---|---|---|---|
|||**Without**<br>**Protection**|**HT-1**|**Air Va**|**lve**|**Surge Tank**<br>**with Check**<br>**Valve**<br>**Surge Tank**<br>**no Check**<br>**Valve**|**SRV**|
|Pressure (Maximum Transi<br>(bars)|ent) @ PJ2|31|15|31||13<br>10|12|
|Pressure (Minimum Transi<br>(bars)|ent) @ PJ2|-1.0|6|4||4<br>8|3|
|Vapor Volume (Maximum<br>@ P2/P-9/P-11/P-13/P-15|Transient)<br>(L)|446|0|0||0<br>0|379|
|Head (Maximum Transient|) @ P5 (m)|723|486|603||489<br>460|530|
|**Alternatives**|**Junction Pr**|**essure (Ma**|**ximum Trans**|**ient) (ba**|**rs)**|||
||**PJ2**|**J2**|**J3**||**J4**|**J5**|**J6**|
|Steady State Pressure|**9.8**|**6.5**|**6.4**||**7.2**|**7.6**|**3.6**|
|Max. Allowable Pressure|**14**|**14**|**14**||**14**|**14**|**14**|
|Without Protection|31|27|27||28|31|26|
|Hydropneumatic Tank(HT-1)|15|11|10||10|9|4|
|Air Valve|31|22|21||21|22|14|
|Surge Tank with Check<br>Valve|13|10|9||10|11|6|
|Surge Tank no Check Valve|10|7|6||7|8|4|
|SRV|12|11|13||14|15|11|



160 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection - Q and A 

Mar-12 

Workshop Review 

#### **Answers** 

- **1** What effect does placing the gas vessel at J1 have on the formation of the vapor cavity and the transient pressure spike? 

The gas vessel effectively stops the formation of a vapor cavity at J1 and other locations along the pipeline.  The high pressure spike resulting from the collapse of the vapor cavity is therefore eliminated. 

- **2** Based on your investigation of other protection equipment, what might be the most effective strategy for protecting the pipeline from transient pressures? 

The simple surge tank might seem like the most favorable alternative but the construction of a 60 m tall tower would definitely rule this out as a practical/economical option. The simple surge tank with check valve would be a better option provided the system can accommodate a short period of relatively low pressure that occurs just after pump shut down. Alternatively the hydropneumatic tank is an excellent option in terms of controlling transients, though, as a pressure vessel, the construction and maintenance costs are likely to be higher than a simple tank. A cost benefit analysis on these options is required to come up with the final decision. 

- **3** How effective is the SRV in reducing the formation of vapor cavities? 

The SRV is effective in confining the occurrence of sub-atmospheric pressures to a small portion of the pipeline adjacent to SV-1 and Res2, however a sizable vapor cavity is allowed to form near SV-1.  The reason for this is that the SRV works to control the symptoms (high pressures) and not the cause.  Other strategies are directed at restricting the formation of the vapor cavity. 

161 Copyright © 2012 Bentley Systems, Incorporated 

Pipeline Protection - Q and A 

Mar-12 



# **Transients in Pipe Networks** 



162 

Mar-12 

Transients in Pipe Networks 

Copyright © 2012 Bentley Systems, Incorporated 





163 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





164 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





165 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





166 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





167 Transients in Pipe Networks 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





168 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





169 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





170 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





171 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





172 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





173 Transients in Pipe Networks Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Network Risk Reduction (metric)** 

### **Module Overview** 

In this workshop, you will import a simple water-distribution network connected to the same pipeline introduced in _Workshop: Transients in a Simple Pipeline_ . You will then perform a more advanced hydraulic transient analysis by following these steps: 

- 1 Import a steady-state WaterCAD model into HAMMER and verify it. 

- 2 Select a transient event to analyze and run the HAMMER model. 

- 3 Based on a review of the results of the transient analysis described you will develop a surge protection strategy. 

### **Module Prerequisites** 

- Fundamental knowledge of hydraulic transients 

- Basic Transient Modeling 

- Pipeline Protection 

### **Module Objectives** 

After completing this module, you will be able to: 

- Import a WaterCAD/GEMS model into HAMMER 

- Analyze a network and develop a surge protection strategy 

174 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Importing and Verifying the Initial Steady-States 

### **Importing and Verifying the Initial Steady-States** 

Follow the next steps to import model data and steady-state results from WaterCAD or WaterGEMS into HAMMER. 

- 1 Start HAMMER V8i. 

- 2 On the Welcome dialog, click Open Existing Project or select File > Open. 

- 3 Browse to C:\Bentley Workshop\HAMMER V8i metric\Starter and open the file Lesson3-WtrGems-SI.wtg. 



- **Note:** The WaterCAD and WaterGEMS file formats are exactly the same as the HAMMER file format.  This makes it very simple to import your WaterCAD/ WaterGEMS results into HAMMER. 

   - 4 Select File > Save As and save the file as **RiskReduction.wtg** . 

   - 5 Double click on VLV1 to open its Properties manager. 



175 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Importing and Verifying the Initial Steady-States 

- 6 Make sure that the following properties are set: 

Status (Initial): Inactive Valve Type: Globe Operating Rule: Fixed 

- 7 Enter the following missing data for the reservoirs: Res1: Elevation (Inlet/Outlet Invert) (m): 377 Res2: Elevation (Inlet/Outlet Invert) (m): 450 

**Note:** There is currently only one scenario in this model—the Base scenario. 

######  **Exercise: Computing** 

- 1 Select Analysis > Compute Initial Conditions to compute the initial conditions and verify that the steady state model is working. 

- 2 Close the Calculation Summary dialog when it comes up if there are no error messages. 

#### **Discussion** 

Inspecting the steady-state model results using Bentley HAMMER V8i reveals that the water transmission main now carries only 865 m<sup>3</sup> /hr of water from the pumping station to reservoir Res2 at elevation 450 m. A local main takes water from the transmission main at a tee located about 37 m from the pumping station, distributing 954 m<sup>3</sup> /hr to a nearby subdivision. The part of the subdivision close to the pumping station has lower ground (and therefore water main) elevations, while the far end has higher ground elevations.  Your goal is to identify transient issues for this system and recommend surge protection alternatives. 

**Note:** By default, HAMMER selects a Constant Speed - No Pump Curve to represent the pump in the Pump Type (Transient) field for PMP-1. 

176 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

### **Configuring the Transient Analysis** 

First, we will need to calculate the Wave Speed for the pipes in the model.  To do that, Bentley HAMMER V8i provides a tool called the Wave Speed Calculator. 

######  **Exercise: Calculating wave speed** 

- 1 Select Tools > Wave Speed Calculator. 



On the Wave Speed Calculator dialog, you should see four sections: Liquid, Material, Miscellaneous, and Features.  Also, note that there is an ellipsis button to the right of the fields in the Liquid and Material sections. 



- 2 Click on the ellipsis button in the Bulk Modulus of Elasticity field. 

This will open up the Liquid Engineering Libraries dialog. 

- 3 Click the + sign in front of Liquid Libraries and LiquidLibrary.xml to expand them. 

You should now see a list of different liquids. 

177 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

- 4 Click on Water at 4C(39F) to highlight it and click Select. 



- 5 Back on the Wave Speed Calculator dialog, the Bulk Modulus of Elasticity and Specific Gravity fields should now have values in them. 

- 6 Click on the ellipsis button in the Young’s Modulus field. 

This will open up the Material Engineering Libraries dialog. 

- 7 Click the + sign in front of Material Libraries and MaterialLibrary.xml to open them. 

- 8 Select Ductile Iron from the list and then click Select. 



- 9 Back on the Wave Speed Calculator dialog, the Young’s Modulus and Poisson’s Ratio fields should now be filled in. 

- 10 Enter a Wall Thickness of 17.8 mm. 

178 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

Your Wave Speed Calculator dialog should look like this now: 



**Note:** In the Features section, we could have selected either Selection or Selection Set (if we have already defined a selection set of pipes) in which to apply the calculated wave speed to only a set of similar pipes; however, in the interest of expediency in this exercise, we will leave All selected. 

- 11 Click OK. 

This will calculate the wave speed and apply it to all of the pipes in the model. 

- 12 After the calculation is complete, a Calculation Complete dialog will open. Click OK to close it. 

179 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

- 13 Open the Pipe FlexTable to look at the properties of the pipes; the Wave Speed field should now have values in them. 



Next, we need to set the calculation options. 

######  **Exercise: Setting the calculation options** 

- 1 Close the FlexTable and select Analysis > Calculation Options to bring up the Calculation Options manager. 



- 2 Double click on Base Calculation Options under the Transient Solver folder to bring up the Properties manager and set the following: 

Show Pocket Opening/Closing: True 

Generate Detailed Reports: True 

Run Duration Type: Time 

Run Duration (Time) (sec): 160 

Pressure Wave Speed (m/s): 0 (default value) 

Vapor Pressure (bars): –1 (default value) 

180 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

Generate Animation Data: True 

Run Extended CAV: True 

Report Points: Selected Points 

- 3 Click in the Report Points Collection field and click the ellipsis button. 

**Note:** HAMMER plots time histories at a pipe’s end points, defined as the point on a pipe closest to a node and labeled Pipe_End_Point:Node.  To obtain a complete picture of what is occurring at any given node, you must inspect every end point connected to that node (e.g., in this example, plot histories at end points P1:J1 and P2:J1 for node J1). 



- 4 Select each point of interest in the Available Items pane and click the single Add button to move the selected point to the Selected Items pane. PMP1D:PMP1 

P1:J1 P2:J1 P2:J2 

P8:J2 

P27:J19 P28:J19 P47:J34 

181 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

###### P50:J37 



- 5 Click OK to close the dialog. 

- 6 Set the Report Times field to Periodically and set the Report Period to 10. 

182 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

- **Note:** This only affects the frequency of output data for plotting and animation. HAMMER will calculate each time step and show the complete and correct maximum and minimum transient envelopes whatever the Report Period. 



- 7 Close the Calculation Options manager. 

Next, we will need to specify the path of the profile along which we want to see the graphical plot and animation of the HGL during the transient run. 

######  **Exercise: Viewing profiles** 

- 1 Select View > Profiles to bring up the Profiles manager. 

**Note:** Notice that there is already a profile named Path1 listed in the magager. 

183 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Configuring the Transient Analysis 

- 2 Double click on Path1 to open the profile. 



- 3 Close the profile. 

We need to set this profile as a Transient Report Path for HAMMER. 

- 4 Right click on Path1 and make sure that there is a checkmark in front of Transient Report Path. 

- 5 If there is not a checkmark, then simply click on the Transient Report Path option from the right click menu. 

**Note:** If you look closely at the icon in front of Path1 in the Profiles manager, you will notice a picture of a hammer in the top right corner of the icon.  This signifies that this profile is a HAMMER report path. 



- 6 Click the New button to create a new profile. 

- 7 On the Profile Setup dialog that comes up, click on Select From Drawing. 

- 8 In the drawing, click on the pipes PMP1D, P1, P2, P8, VLV1U, VLV1D, P9, P10, P14, P48, P49 and P50 to highlight and select them (notice that when you select a pipe, its connecting nodes are automatically selected as well). 

- 9 After you have selected all of the listed pipes, click the Done button on the Select toolbar. 

184 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Configuring the Transient Analysis 

- **Note:** All of the pipes and nodes that you have selected will now be listed in the left side of the Profile Setup dialog. 

   - 10 Click the Open Profile button to view your profile. 

   - 11 Click OK on the Profile Series Options dialog that opens up. 

   - 12 Close the profile and then rename it to **Path2** . 

   - 13 Repeat steps 6 through 12 above for the following path: 

|**Path Name**|**Pipes Selected**|
|---|---|
|Path3|PMP1D, P1, P2, P8, VLV1U, VLV1D, P9, P15, P22, P24, P28, P30, P46, P47|



- 14 Once you have completed creating all three paths and have set them to be Transient Report Paths, close the Profiles manager. 



   - 15 Select File > Save to save the file. 

- **Hint:** <u>Transient Tip: When you import a steady-state model using WaterObjects, the</u> Friction Coefficient and Wave Velocity fields of individual pipes may be left empty (not zero) or have a default value.  This does not affect the results, since HAMMER calculates the friction factor prior to every run and because it uses the global Wave Velocity (in the System tab of the Model Settings dialog).  If the pressure wave speed differs for individual pipes, you must enter a Wave Speed value for each pipe in your system. 

185 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis without Surge Protection 

### **Analysis without Surge Protection** 

In _Workshop: Transients in a Simple Pipeline_ , you simulated the transient pressures resulting from a sudden power failure.  In this workshop you will learn how to simulate transient pressures in a water distribution network triggered by an emergency pump shutdown and restart.  Although a power failure often results in the worst-case conditions, restarting before friction has dissipated the transient energy can cause higher extreme pressures than the initial power failure. 

In order to generate transient events for a rapid but controlled emergency pump shutdown and restart, you need to set appropriate pump characteristics to control the speed at which this pump can shut down and restart.  One of the ways to do this is to install a variable-frequency drive (VFD), also known as a variablespeed pump. 

For this analysis, we will need to create an alternative and scenario. 

######  **Exercise: Creating a new active topology alternative** 

- 1 Select Analysis > Alternatives. 

We will be creating a new Active Topology alternative. 

- 2 Click the + sign in front of Active Topology. 

You should see the Base-Active Topology alternative that we were previously using. 

- 3 Right click on Base Active Topology and select New > Child Alternative. 

This will create a new child alternative beneath Base Active Topology. 

- 4 Right click on Active Topology Alternative – 1 and select Rename. 

- 5 Rename the alternative to **Existing System** . 

Your Alternatives manager should now look like this: 



**Note:** Notice that the Base Active Topology has a red checkmark in front of it.  This means that it is still the current alternative that is being used. 

186 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis without Surge Protection 

We will now need to create some scenarios to utilize these new alternatives that we just created. 

######  **Exercise: Creating a new scenario** 

- 1 Select Analysis > Scenarios to bring up the Scenarios manager. 

- 2 In the Scenarios manager, right click on Base and select New > Child Scenario. 

- 3 Name this new scenario **Existing System** . 



- 4 After renaming the scenario, double click on Existing System to bring up the Properties manager. 

- 5 Change the Active Topology alternative to Existing System. 



- 6 Make sure that Base still has a checkmark in the folder icon as shown in the screenshot above. 

- 7 If Base does not have the checkmark, right click Base and select Make Current. 

- 8 Close the Scenarios manager. 

######  **Exercise: Entering the VFD pump data** 

- 1 Double click on PMP1 to open its Properties manager. 

**Note:** You can use either Speed or Torque to control the VFD pump ramp times.  In this lesson, you will learn how to control the pump using Speed. 

- 2 In the Transient (Operational) section, click in the Pump Type (Transient) field and select Variable Speed/Torque from the dropdown menu. 

187 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Analysis without Surge Protection 

You should now be presented with more options. 

- 3 Set the following pump parameters in the Transient (Operational) section: Diameter (Pump Valve) (mm): 575 

Time (For Valve to Operate) (sec): 0 

Control Variable: Speed 

- 4 Click in the Operating Rule box; it is currently set to Fixed. 

- 5 In the dropdown menu in that field, select <Edit…>. 

This will open the Patterns manager which will allow us to enter the operating pattern for pump PMP1.  We need to create a new Operational (Transient, Pump) pattern. 

- 6 Right click on Operational (Transient, Pump) and select New. 



- 7 Name this new pattern **PMP1** . 

- 8 Click on PMP1 to select it and in the right window pane, set the Starting Multiplier to 1. 

- 9 On the Transient tab, enter the following data: 

|**Time from Start (sec) **|**Relative Speed Multiplier**|
|---|---|
|5|1|
|10|0|
|25|0|
|30|1|



188 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis without Surge Protection 

Your Patterns manager should now look like this: 



- 10 Click Close to close out of this dialog. 

- 11 Back in the PMP1 Properties manager, click in the Operating Rule field and select the PMP1 pattern from the dropdown menu. 

- 12 In the Physical section, set the Elevation (m) to 363. 

- 13 Click in the Pump Definition field. 

It is currently set to PJ1-PJ2 (PMP1). 

- 14 On the dropdown menu in the Pump Definition field, select Edit Pump Definitions. 

This will open up the Pump Definitions dialog. 

- 15 In the Pump Definitions dialog, click the PJ1-PJ2 (PMP1) pump definition to select it. 

- 16 In the right side of the Pump Definitions dialog, click on the Head tab. 

189 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Analysis without Surge Protection 

Notice that this tab’s data is already completed and looks like this: 



- 17 Click on the Efficiency tab and set the following values: 

Pump Efficiency: Constant Efficiency 

190 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Analysis without Surge Protection 

Pump Efficiency: 85 % 



- 18 Click on the Transient tab and set the following values: 

Inertia (Pump and Motor): 169 N.m<sup>2</sup> 

- **Note:** This is the combined pump, shaft, and motor inertia and can be obtained from the manufacturer or estimated from its power rating. 

Speed (Full): 1760.0 rpm 

Specific Speed: SI=25, US=1280 

- **Note:** This is based on the pump’s rotation speed (1760 rpm).  See Appendix B for an explanation of how to determine a pump’s specific speed. 

   - 19 Check the box for Reverse Spin Allowed?. 

   - 20 Click Close to close the Pump Definitions dialog. 

191 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Analysis without Surge Protection 

- 21 Back in the PMP1 Properties manager; make sure that PJ1-PJ2 (PMP1) is still selected in the Pump Definition box. 



######  **Exercise: Computing** 

- 1 Click in the scenario dropdown menu and select Existing System. 

- 2 Select Analysis > Compute Initial Conditions. 

**Note:** This will compute the initial steady state conditions that will be the basis of our transient run.  After the steady state computations are completed, a Calculation Summary dialog will open.  If there were warnings or errors in our model, the messages would appear in the bottom half of the Calculation Summary dialog. 

You should not have any error messages. 

- 3 Close the Calculation Summary dialog. 



- 4 Click the Compute button or select Analysis > Compute. 

- 5 Close the Transient Calculation Summary and User Notification dialogs if they open up. 

192 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Analysis without Surge Protection 

######  **Exercise: Plotting the results** 

- 1 Select Analysis > Transient Results Viewer to open the Transient Results Viewer from which you can plot and animate your results. 

- 2 Click the Time Histories tab on the Transient Results Viewer. 

- 3 Select PMP1D:PMP1 (i.e., the discharge side of the pump) from the Time History dropdown menu and click Plot. 

It should look like the following figure: 



- 4 Close the time history when you are done reviewing it. 

- 5 Click the Profiles tab and plot the maximum and minimum transient head envelopes along paths 1, 2, and 3. 

193 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction (metric) 

Mar-12 

Analysis without Surge Protection 

The Path3 envelopes should look like the following figure: 



6 Answer the workshop questions. 

194 

Network Risk Reduction (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 



# **Network Risk Reduction - Q and A** 

### **Workshop Review** 

Now that you have completed this workshop, let’s measure what you have learned. 

#### **Questions** 

- **1** Select Path1 in the viewer and click animate.  When does the vapor cavity open and collapse? 

Enter your answer below: 

- **2** What causes the vapor cavity to collapse and what happens to the local pressure when it does? 

Enter your answer below: 

195 

Network Risk Reduction - Q and A 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Workshop Review 

- **3** Why is the upsurge resulting from the pump restart less than that for the initial pump shutdown? 



<!-- Start of picture text -->
Enter your answer below:<br><!-- End of picture text -->

- **4** How long does it take the system to return to near steady state conditions? 



<!-- Start of picture text -->
Enter your answer below:<br><!-- End of picture text -->

- **5** Apart from the area adjacent to junction J1 where else in the network do you find appreciable formation of vapor cavities? 



<!-- Start of picture text -->
Enter your answer below:<br><!-- End of picture text -->

196 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction - Q and A 

Mar-12 

Workshop Review 

- **6** Given that the subdivision may contain older pipes, what can you say about the transient pressures that are experienced in the network, especially along Path3? 

Enter your answer below: 

- **7** What effect has the addition of the subdivision had to the transient pressures in the main transmission line (Path1)?  Set up the pump trip as per Lesson 1 and compare the results to those obtained in that lesson to confirm your answer. 

Enter your answer below: 

- **8** Experiment to learn the sensitivity of this system to an automatic, emergency shutdown and restart: 

   - Set different shutdown and restart ramp times for the pump.  For example, try 10 second ramp times for the pump.  How fast does the flow decrease to zero?  Why? 

Enter your answer below: 

197 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction - Q and A 

Mar-12 

Workshop Review 

- Select different time delays between the pump shutdown and restart. What happens if you try to restart the pump when pressure is at its lowest, rising, or highest? 

Enter your answer below: 

- **9** What are the fastest ramp times and shortest time delay which do not result in unacceptable transient pressures anywhere in the system?  Since the maximum transient envelopes depend on these two variables, several valid solutions are possible. 

Enter your answer below: 

198 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction - Q and A 

Mar-12 

Workshop Review 

#### **Answers** 

- **1** Select Path1 in the viewer and click animate.  When does the vapor cavity open and collapse? 

The vapor cavity begins to open and about 8 seconds and collapses at 16 seconds. 

- **2** What causes the vapor cavity to collapse and what happens to the local pressure when it does? 

The flow returning to the pump station causes the vapor cavity to collapse and results in a large pressure upsurge at junction PJ2. 

- **3** Why is the upsurge resulting from the pump restart less than that for the initial pump shutdown? 

The flow generated by the pump restart helps to prevent subsequent formation (and therefore collapse) of vapor cavities.  The pump restarts at 25 seconds or 20 seconds after the start of the emergency pump shutdown, just as the high-pressure pulse from the collapse of a vapor pocket at node J1 is reaching the pump station.  This pulse closes the check valve against the pump for a while, until it reaches its full speed and power at around 30 seconds. 

- **4** How long does it take the system to return to near steady state conditions? 

The system approaches a new steady state after 50 seconds and it has essentially stabilized to a new steady state by 90 seconds. 

- **5** Apart from the area adjacent to junction J1 where else in the network do you find appreciable formation of vapor cavities? 

There is appreciable vapor formation at the localized high point in the network at junction J19. 

- **6** Given that the subdivision may contain older pipes, what can you say about the transient pressures that are experienced in the network, especially along Path3? 

Maximum transient pressure heads are of the order of 100% above steady-state pressures along the majority of Path3.  This is likely to be very significant compared to the pipes’ surge-tolerance limit. 

199 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction - Q and A 

Mar-12 

Workshop Review 

- **7** What effect has the addition of the subdivision had to the transient pressures in the main transmission line (Path1)?  Set up the pump trip as per Lesson 1 and compare the results to those obtained in that lesson to confirm your answer. 

The subdivision has the effect of dampening the transient pressures. (Pump Shutdown scenario in Lesson3_Workshop 3_answer.wtg) 

- **8** Experiment to learn the sensitivity of this system to an automatic, emergency shutdown and restart: 

   - Set different shutdown and restart ramp times for the pump.  For example, try 10 s ramp times for the pump.  How fast does the flow decrease to zero?  Why? 

   - Select different time delays between the pump shutdown and restart. What happens if you try to restart the pump when pressure is at its lowest, rising, or highest? 

With a 10 second ramp time, the flow decreases to zero in 7.3 seconds after the pump shutdown starts (versus 4.3 seconds for a 5 second ramp time).  With different time delays, there are only minor differences in the results. 

- **9** What are the fastest ramp times and shortest time delay which do not result in unacceptable transient pressures anywhere in the system?  Since the maximum transient envelopes depend on these two variables, several valid solutions are possible. 

The pump needs to ramp down slowly in order to avoid negative pressures at J19, so the ramp down time should be 140 seconds or more. The resulting gradual ramp down means the delay before ramping up can be very short (5 seconds or less), since the system doesn’t need extra time to stabilize. The pump can ramp back up to full speed relatively quickly (approx. 5-10 seconds) without causing significant high pressure transients. 

200 Copyright © 2012 Bentley Systems, Incorporated 

Network Risk Reduction - Q and A 

Mar-12 



# **Modeling Objectives** 



201 

Modeling Objectives 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





202 Modeling Objectives Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





203 Modeling Objectives Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





204 Modeling Objectives Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





205 Modeling Objectives Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





206 Modeling Objectives Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



207 Modeling Objectives Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Skeletonization for Transients** 



208 

Skeletonization for Transients 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





209 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





210 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





211 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





212 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





213 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





214 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





215 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





216 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





217 Skeletonization for Transients 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





218 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





219 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





220 Skeletonization for Transients 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





221 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





222 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





223 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





224 Skeletonization for Transients 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





225 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





226 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





227 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





228 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





229 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





230 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





231 Skeletonization for Transients Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Advanced Surge Protection** 



232 

Advanced Surge Protection 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





233 Advanced Surge Protection Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





234 Advanced Surge Protection Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





235 Advanced Surge Protection Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





236 Advanced Surge Protection Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





237 Advanced Surge Protection Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





238 Advanced Surge Protection Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Multipoint Network Protection (metric)** 

### **Module Overview** 

In this workshop you will assess the efficiency of alternative protection equipment, noting how protection for the pipeline affects conditions in the network and vice versa. 

### **Module Prerequisites** 

- Basic Transient Modeling 

- Pipeline Protection 

- Network Risk Reduction 

### **Module Objectives** 

After completing this module, you will be able to: 

- Add protective equipment to a network 

- Use the Transient Thematic Viewer to color code subpipe sections 

- Review and animate your results using the Transient Results Viewer 

- Format the appearance of graphs generated by the Transient Results Viewer 

239 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis with Surge-Protection Equipment 

### **Analysis with Surge-Protection Equipment** 

You can select from an array of protective equipment to control high and low transient pressures in the pipeline (Path1) and distribution network (Path2 and Path3).  Using HAMMER, you can assess the efficiency of alternative protection equipment, noting how protection for the pipeline affects conditions in the network and vice versa.  In this example you will try to protect this entire system with two surge-control devices: 

- A hydropneumatic tank (also called a gas vessel or air chamber) at node J1 similar to the protection used in _Workshop: Pipeline Protection_ .  Due to the connected pipe network, transient pressure pulses fragment and attenuate more rapidly and there is much less flow in the pipeline; therefore a 5 m<sup>3</sup> gas vessel is adequate.  This is a significant reduction compared with the 20 m<sup>3</sup> gas vessel in _Workshop: Pipeline Protection_ . 

- A simple flow-through surge tank or standpipe at the node J19.  A combination air valve could also be considered for this location if freezing or land-acquisition costs are a concern. 

######  **Exercise: Creating a new alternative for the hydropneumatic tank** 

- 1 Open HydropneumaticTank_SI.wtg found in C:\Bentley Workshop\HAMMER V8i metric\Starter. 

In this workshop you will add some surge protection equipment to this system. 

Your model should look like this when you open it: 



240 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis with Surge-Protection Equipment 

We will be following the same procedure as we did in _Workshop: Pipeline Protection_ .  First, we will need to create a new alternative and scenario to add the new hydropneumatic tank. 

- 2 Select Analysis > Alternatives. 

We will be creating a new Active Topology alternative for the new hydropneumatic tank and adjoining pipes. 

- 3 On the Alternatives manager, click the + sign in front of Active Topology to expand the category. 

You should see the Base Active Topology and Existing System alternatives that we were previously using. 

- 4 Right click on Existing System and select New > Child Alternative to create a new child alternative. 

- 5 Rename this new child alternative to **With Hydropneumatic Tank** . 



**Note:** Notice that Base Active Topology has a red checkmark in front of it.  This means that it is still the current alternative that is being used. 

We will now need to create some scenarios to utilize this new alternative that we just created. 

######  **Exercise: Creating a new scenario** 

- 1 Select Analysis > Scenarios. 

- 2 In the Scenarios manager, right click on Existing System and select New > Child Scenario. 

- 3 Rename the new scenario to **With Hydropneumatic Tank** . 

- 4 Double click on the With Hydropneumatic Tank scenario to bring up the Properties manager if it is not already up. 

- 5 Change the Active Topology alternative to With Hydropneumatic Tank. 

241 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis with Surge-Protection Equipment 

The Properties manager should look like this: 





- 6 Make sure that Base still has a checkmark in the folder icon as shown in the screenshot above.  If Base does not have the checkmark, right click Base and select Make Current. 

- 7 Close the Scenarios manager. 

Back in the drawing pane, we are now ready to add in the new hydropneumatic tank. 

######  **Exercise: Adding a hydropneumatic tank to the network** 



- 1 Click the Hydropneumatic Tank icon in the Layout toolbar and place the tank just below junction J1. 

The default name HT-1 should be fine. 

- 2 Using the Pipe tool, draw a pipe from PJ2 to HT-1 and from HT-1 to J2, right click and select Done and then click the Select tool. 

- 3 Name the two pipes P1-1 and P2-1 respectively. 

They will have almost exactly the same properties as P1 and P2 respectively. 

242 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Analysis with Surge-Protection Equipment 

Your drawing should now look something like this when looking at the Base scenario: 



- 4 Enter these values into the Properties manager for P1-1 and P2-1: 

|**Label **|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|**Wave Speed**<br>**(m/s)**|
|---|---|---|---|---|---|---|---|---|
|P1-1|J1|HT-1|True|20|600|Ductile Iron|130|1,252.33|
|P2-1|HT-1|J2|True|380|600|Ductile Iron|130|1,252.33|



5 Enter the following data for the hydropneumatic tank HT-1: Elevation (Base) (m): 412 Operating Range Type: Elevation HGL (Initial) (m): 463.13 Liquid Volume (Initial) (m<sup>3</sup> ): 2.8 Elevation (m): 412 Volume (Tank) (m<sup>3</sup> ): 5 Tank Calculation Model: Gas Law Model Diameter (Tank Inlet Orifice) (mm): 300 Ratio of Losses: 2.5 Gas Law Exponent: 1.2 Has Bladder?: True Pressure (Gas-Preset) (bars): 0.00 Minor Loss Coefficient (Outflow): 1.0 

Next, we will need to add in a surge tank at J19. 

######  **Exercise: Adding a surge tank to the network** 



- 1 Click on the Surge Tank tool in the Layout toolbar and draw a surge tank southwest of J19. 

243 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis with Surge-Protection Equipment 

The default name of ST-1 is fine. 

- 2 Click on the Pipe tool and draw pipes from J15 to ST-1, from J20 to ST-1, from ST-1 to J24, from J23 to ST-1, and from ST-1 to J18. 

- 3 Click the Select tool when you are done. 

- 4 Rename these pipes to P25-1, P28-1, P27-1, P26-1, and P24-1 respectively. 



###### 5 Enter the pipe properties as follows: 

|**Label**|**Start**<br>**Node**|**Stop**<br>**Node**|**Has User Defined**<br>**Length?**|**Length (User**<br>**Defined) (m)**|**Diameter**<br>**(mm)**|**Material**|**Hazen-**<br>**Williams C**|**Wave Speed**<br>**(m/s)**|
|---|---|---|---|---|---|---|---|---|
|P24-1|ST-1|J18|True|200|300|Ductile Iron|130|1,351.70|
|P25-1|J15|ST-1|True|250|300|Ductile Iron|130|1,351.70|
|P26-1|J23|ST-1|True|300|200|Ductile Iron|130|1,390.48|
|P27-1|ST-1|J24|True|300|200|Ductile Iron|130|1,390.48|
|P28-1|J20|ST-1|True|220|200|Ductile Iron|130|1,390.48|



**Note:** The quickest method is to use the Pipe FlexTable and edit the columns to match the table above and then sort the table ascending on the Label column. 

- 6 Next, enter the following data for ST-1: 

Operating Range Type: Elevation 

244 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis with Surge-Protection Equipment 

Elevation (Base) (m): 435 Elevation (Minimum) (m): 435 Elevation (Initial) (m): 454.5 Elevation (Maximum) (m): 457 Use High Alarm?: True Elevation (High Alarm) (m): 456 Elevation (m): 435 Section: Circular Diameter (m): 0.61 Surge Tank Type: Simple Has Check Valve?: False Weir Coefficient (m^(1/2)/s): 1.38 Weir Length (m): 0.3 Diameter (Orifice) (mm): 200 Ratio of Losses: 2.5 Headloss Coefficient: 1 

We now need to switch to each of our scenarios and set the elements that do not belong in that scenario to an inactive status. 

######  **Exercise: Creating an active topology alternative for Existing System** 

- 1 Select Existing System from the Scenarios dropdown menu to make it the active scenario. 



- 2 Select Tools > Active Topology Selection or click the Active Topology Selection icon from the toolbar. 

This will bring up the Select toolbar. 

- 3 Make sure that the Add button is selected. 

- 4 In the drawing select HT-1 and ST-1, and then click the Done button from the Select toolbar. 

**Note:** Notice that the pipes connected to both HT-1 and ST-1 are automatically selected when you click on HT-1 and ST-1. 

245 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Analysis with Surge-Protection Equipment 

Those elements should now have turned gray in the drawing to signify that they are inactive (or disappeared if you have the inactive topology set to not display) and the drawing should look like the figure below: 



######  **Exercise: Creating an active topology alternative for With Hydropneumatic Tank** 

- 1 Set With Hydropneumatic Tank as the current scenario. 

- 2 Select Tools > Active Topology Selection. 



- 3 On the Select toolbar, click on the Remove button. 

- 4 In the drawing, click on P1-1, P2-1, P24-1, P25-1, P26-1, P27-1, and P28-1. to deselect them. 





- 5 On the Select toolbar, click on the Add button. 

- 6 In the drawing, click on J1 and J19 and click Done on the Select toolbar. Notice that HT-1 and ST-1 are active in the With Hydropnematic Tank scenario. 

######  **Exercise: Creating new profiles** 

- 1 Select View > Profiles to bring up the Profiles manager. 



- 2 Click the New button in the upper left corner to create a new profile. 

- 3 On the Profile Setup window that comes up, click on Select From Drawing. 

246 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Analysis with Surge-Protection Equipment 

   - 4 In the drawing, click on the pipes PMP1D, P1-1, P2-1, P3, P4, P5, P6 and P7 to highlight and select them (notice that when you select a pipe, its connecting nodes are automatically selected as well). 

   - 5 After you have selected all of the listed pipes, click the Done button on the Select toolbar. 

- **Note:** All of the pipes and nodes that you have selected will now be listed in the left side of the Profile Setup window. 



- 6 Click the Open Profile button to view your profile. 

- 7 Click OK on the Profile Series Options window that opens up. 

247 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Analysis with Surge-Protection Equipment 

You should now see the profile below (if the HGL is not plotted in your profile, that is fine for now; it will be plotted when you calculate the initial conditions): 



- 8 Close the Profile. 

- 9 Back on the Profiles manager, right-click on Profile – 1 and select Rename. 

- 10 Rename the profile to **Path1-1** . 

Next, we need to set this profile as a Transient Report Path for Hammer. 

######  **Exercise: Creating transient report paths** 

- 1 Right click on Path1-1 and make sure that there is a checkmark in front of Transient Report Path.  If there is not a checkmark, then simply click on the Transient Report Path option from the right-click menu. 

- 2 Repeat steps 2 to 10 from the previous exercise for the following two paths: 

Path Name: **Path2-1** 

Pipes selected: PMP1D, P1-1, P2-1, P8, VLV1U, VLV1D, P9, P10, P14, P48, P49, and P50 

Path Name: **Path3-1** 

248 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Analysis with Surge-Protection Equipment 

Pipes selected: PMP1D, P1-1, P2-1, P8, VLV1U, VLV1D, P9, P15, P22, P241, P28-1, P30, P46, and P47 



- 3 Once you have completed creating all three paths and have set them to be Transient Report Paths, close the Profiles manager. 

- 4 Click in the scenario dropdown menu and select Base as the current scenario. 

- 5 Click on HT-1 and drag it over the top of J1. 

- 6 Click on ST-1 and drag it over the top of J19 so that the junctions/ protection equipment and pipes match up. 

We will want to do this in order for the X and Y coordinates of the nodes and protective equipment to match up.  The X and Y coordinates are important if we want to do a transient force calculation. 

**Note:** A Transient Force Calculation would calculate the forces caused by the transients at each of the junctions.  The force would be listed with their complete X, Y, and Z components.  A transient force calculation has fundamental implications for the design of thrust blocks and restraints for the pipes.  We won’t be doing a force calculation in this workshop; however, it is good practice to make sure that your nodal coordinates are correct if you might need to do such calculations later. 

- 7 Select File > Save to save the file. 

######  **Exercise: Computing** 

- 1 Set the current scenario to With Hydropneumatic Tank. 



- 2 Select Analysis > Compute Initial Conditions to compute the initial conditions. 

- 3 Close the Calculation Summary dialog when it comes up. 



- 4 Click the Compute button or select Analysis > Compute. 

- 5 Close the Transient Calculation Summary and User Notification dialogs if they open up. 

249 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Analysis with Surge-Protection Equipment 

######  **Exercise: Viewing transient results** 

- 1 Select Analysis > Transient Results Viewer to open the Transient Results Viewer from which you can plot and animate your results. 

- 2 Select Path1-1, Path2-1, and Path3-1 in sequence and click Plot to generate graphs of their transient head envelopes. 

The envelope along Path3-1 with surge protection should look like the following figure: 



- 3 Select File > Save to save your model. 

- 4 Answer the questions at the end of the workshop. 

250 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Color-Coding Maps, Profiles and Point Histories 

### **Color-Coding Maps, Profiles and Point Histories** 

In the design of a surge-control strategy for a water distribution network, the extreme states are usually of the greatest interest.  HAMMER has built-in capabilities to visualize maximum and minimum simulated flows, heads, pressures, and volumes (vapor or air) throughout the pipe system.  You can colorcode nodes and pipes according to these different parameters.  HAMMER can also display line thicknesses in proportion to the pipes’ diameter. 

#### **Color Coding** 

In this part of the lesson, you will learn how to use HAMMER’s color-coding features to make your presentation more intuitive and compelling to your audiences. 

######  **Exercise: Color coding pipes for head** 

- 1 Make the With Hydropneumatic Tank the current scenario. 

- 2 Set up the pipe color coding by selecting View > Element Symbology. 

- 3 Right click on Pipe and select New > Color Coding. 

- 4 Select the following in the Properties area on the left side of the Color Coding Properties dialog. 

Field Name: Head (Maximum, Transient) 

Selection Set: <All Elements> 

- 5 Click the Calculate Range button and then select Full Range to calculate the range of values. 

- 6 Select Color for the Options dropdown menu. 

- 7 Click the Initialize button (third button from the left). 



- **Note:** You could manually change the colors and values in the table.  However, for the purpose of this exercise, we will accept the defaults. 

251 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Color-Coding Maps, Profiles and Point Histories 

The Color Coding Properties – Pipe dialog should now look like this: 



- 8 Click Apply and then OK. 

Next, set up junction element color coding based on the maximum pressure that occurred during the transient run. 

######  **Exercise: Color coding junctions for maximum pressure** 

- 1 Select View > Element Symbology. 

- 2 Right click on Junction and select New > Color Coding. 

- 3 Set the following values: 

Field: Pressure (Maximum, Transient) 

Selection Set: <All elements> 

- 4 Click the Calculate Range button and select Full Range to calculate the range. 

- 5 Select Color in the Options dropdown menu. 

252 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Color-Coding Maps, Profiles and Point Histories 

- 6 Click the Initialize button. 



###### 7 Click Apply and then OK. 





253 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Color-Coding Maps, Profiles and Point Histories 

- **Note:** Color-coding a map for selected variables provides an overview of extreme conditions in the entire system.  This map can be compared with profiles and histories (or their corresponding animations). 

#### **Transient Thematic Viewer (TTV)** 

Next, we will take a look at the model using the Transient Thematic Viewer (TTV). The Transient Thematic Viewer is similar to the regular color coding in the Element Symbology manager.  The difference is that the Transient Thematic Viewer will be able to display different colors for each subpipe section. 

During the computations, each pipe is divided into many subpipe sections and the pressures and vapors, etc, are calculated at every internal subpipe section in order to give a complete picture of what is happening in the system even in the middle of pipes and not just at the nodes.  The Transient Thematic Viewer will display the pressures in the partial pipes. 

######  **Exercise: Using the Transient Thematic Viewer** 

- 1 With the scenario still on With Hydropneumatic Tank, select Analysis > Transient Thematic Viewer. 

**Note:** Notice that the TTV dialog looks very similar to the Element Symbology Color Coding dialog. 

- 2 Select the Pipes tab at the top of the dialog and enter the following: 

Field Name: Maximum Head Values 

Selection Set: <All Elements> 

- 3 Click the Calculate Range button and select Full Range. 

- 4 The Minimum, Maximum and Steps fields should have been filled in with the following values: 

Minimum: 383.0 m Maximum: 556.18 m Steps: 5 

254 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Color-Coding Maps, Profiles and Point Histories 

- 5 On the right side of the TTV dialog in the Color Maps section, click on the Initialize button which is the third icon from the left.  This will initialize the color coding for the pipes in the model. 



   - 6 Click Apply.  Do **NOT** click Close. 

- **Warning:** The Transient Thematic Viewer color coding in the drawing does not persist and will only last as long as the TTV dialog remains open. 

   - 7 Move the TTV dialog out of the way of the drawing. 



255 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Color-Coding Maps, Profiles and Point Histories 

- **Note:** Notice that most of the pipes are blue—meaning that those pipe sections have max head values between 452.27 m and 486.91 m. 

   - 8 Now zoom into pipe P4. 

**Note:** Notice that part of the pipe is red and the other part is magenta signifying that the right half of the pipe has max head values between 486.91 m and 521.54 m and the left half of the pipe has max head values between 521.54 m and 556.18 m. 



- 9 After reviewing your results, click Close on the TVV dialog to exit. 

Some parts in the subdivision also experience high pressures.  For example, the color-coded map and the Results section of the Properties manager indicate that the point with the highest elevation in the subdivision, node J19, experiences the lowest minimum transient pressure, while the lowest point in the network, node J37, experiences the largest maximum transient pressure. 

10 Save your file. 

256 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Reviewing Results 

### **Reviewing Results** 

In this part of the workshop, you will learn how to compare scenarios using the Transients Results Viewer. You will view the results for the existing system versus the system with the hydropneumatic tank. 

######  **Exercise: Comaring scenarios** 

- 1 Make sure Existing System and With Hydropneumatic Tank scenarios have both been computed. 

- 2 Make Existing System the current scenario. 

- 3 Select Analysis > Transient Results Viewer. 

- 4 Click the Time Histories tab. 

- 5 Click the ellipsis button for Additional Scenarios. 

- 6 Select the With Hydropneumatic Tank scenario and click OK. 

- 7 Set the Time History to PMP1D:PMP1. 



257 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Reviewing Results 

###### 8 Click Plot. 



- 9 Review the results and close the Time History graph when you are done. 

######  **Exercise: Animating results** 

To visualize the system interactively, do the following: 

- 1 With the Transient Results Viewer for the Excisting System scenario still open, switch the current scenario to With Hydropneumatic Tank scenario. 

- 2 Select Analysis > Transient Results Viewer. 

258 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Reviewing Results 

- **Note:** You should now have two Transient Results Viewer dialogs open. One for Existing System and one for With Hydropneumatic Tank. 

   - 3 Select Profile Path3 for Existing System and select Profile Path3-1 for With Hydropneumatic Tank. 





- 4 Click Profile on both Transient Results Viewer dialogs to open the profiles. 



- 5 Animate both profiles by clicking Play on each window and review the difference between the scenarios with and without protection. 

259 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Reviewing Results 





260 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection (metric) 

Mar-12 

Reviewing Results 

**Note:** The previous images are showing the profiles animated at 18.21130 seconds. 

- 6 Review the differences between each scenario. 

- 7 Save your file. 

261 

Multipoint Network Protection (metric) 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 



# **Multipoint Network Protection - Q and A** 

### **Workshop Review** 

Now that you have completed this workshop, let’s measure what you have learned. 

#### **Questions** 

- **1** Do vapor cavities or subatmospheric pressures occur in the protected system? 

Enter your answer below: 

- **2** Are high transient pressures experienced in the subdivision network? 



<!-- Start of picture text -->
Enter your answer below:<br><!-- End of picture text -->

262 

Multipoint Network Protection - Q and A 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Workshop Review 

#### **Answers** 

- **1** Do vapor cavities or subatmospheric pressures occur in the protected system? 

No sub-atmospheric pressures occur anywhere in the distribution network. 

- **2** Are high transient pressures experienced in the subdivision network? 

High transient pressures are comparable to the steady-state pressures for the downstream half of Path3-1. Keeping transient water pressures within a narrow band reduces complaints and it could be important for certain industries. 

263 Copyright © 2012 Bentley Systems, Incorporated 

Multipoint Network Protection - Q and A 

Mar-12 



# **ModelBuilder** 



264 

Mar-12 

ModelBuilder 

Copyright © 2012 Bentley Systems, Incorporated 





265 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





266 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





267 ModelBuilder 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





268 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





269 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





270 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





271 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





272 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





273 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





274 ModelBuilder 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





275 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





276 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





277 ModelBuilder Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



278 Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 

ModelBuilder 



# **Hydropower and Mining System Applications** 



279 

Hydropower and Mining System Applications 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





280 Hydropower and Mining System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





281 Hydropower and Mining System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





282 Hydropower and Mining System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Sewer System Applications** 



283 

Sewer System Applications 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 





284 Sewer System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





285 Sewer System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





286 Sewer System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 





287 Sewer System Applications Copyright © 2012 Bentley Systems, Incorporated 

Mar-12 



# **Reference Material** 

#### **Contact Information for Reference Material:** 

**Jean-Luc Daviau:** 

jean.luc.daviau@genivar.com 

###### **GENIVAR’s Hydraulics Department Web Page:** 

http://www.genivar.com/en/expertises/expertise.asp?nocompetences=24 

288 

Reference Material 

Mar-12 

Copyright © 2012 Bentley Systems, Incorporated 

Ottawa HPTM 

### **Ottawa HPTM** 

(Water Transmission Line & Network) 



289 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Avenue & Rosehill Watermain Class EA 

### **Avenue & Rosehill Watermain Class EA** 

(Route Selection for Large Mains) 



290 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Alliston to Beeton Transmission Lines 

### **Alliston to Beeton Transmission Lines** 

(Two Regional Water Pipelines) 



291 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Alliston to Beeton Transmission Lines 



292 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Thunder Bay Water Network & Crossings 

### **Thunder Bay Water Network & Crossings** 

(Multi-zone Transients) 



293 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Thunder Bay Water Network & Crossings 



294 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Ellesmere Pump Station 

### **Ellesmere Pump Station** 

(Hydraulic Transients and Pump Tests incl. NPSH) 



295 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

West Dundas Water Supply Investigation 

### **West Dundas Water Supply Investigation** 

(Field Checks including Transients) 



296 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Western Beaches Storage Tunnel 

### **Western Beaches Storage Tunnel** 

(Mass Oscillations & Overflows) 



297 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Jackson Trails Sewage PS 

### **Jackson Trails Sewage PS** 

(Transients in Forcemains) 



298 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Pit River Penstocks 

### **Pit River Penstocks** 

(Hydropower Transients) 



299 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

Barrick Roaster Plant & Tailings Lines 

### **Barrick Roaster Plant & Tailings Lines** 

(Slurry Transients) 



300 Copyright © 2012 Bentley Systems, Incorporated 

Reference Material 

Mar-12 

