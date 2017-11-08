## HID335: Project Proposal 
## Title: > 
    Big Data and Health Analytics: Using Machine Learning 
    to Predict Opiate Addiction and Overdose.  
## Abstract: >
   Abuse of prescription medication in North America over the past two decades 
   has lead to increased rates of opioid addiction, drug overdose, and death. Big data 
   health analytics may help to identify individuals susceptible to addiction and overdose, 
   possibly leading to improved treatment and prevention outcomes. This project will explore 
   how machine learning classification methods (logistic regression, decision trees, SVM) 
   applied to public health data can be used to predict opioid addiction and drug overdose. 
   Differences between the ML classification methods will be discussed. 

## Data: 2015 NATIONAL SURVEY ON DRUG USE AND HEALTH
* Substance Abuse and Mental Health Services Administration Center for Behavioral Health Statistics and Quality
* Rockville, Maryland 20857, October 27, 2016
* http://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893
   
# 1.11. PRESCRIPTION PAIN RELIEVERS 
To be defined with prescription pain reliever dependence, DEPNDPYPNR, a respondent must have met three or more of these pain reliever dependence criteria: 
(1) Spent a great deal of time over a period of a month or more getting, using, or getting over the effects of pain relievers (PNRLLOTTM=1 or PNRLGTOVR=1) 
(2) Used pain relievers more often than intended or was unable to keep set limits on pain reliever use (PNRLKPLMT=2) 
(3) Needed to use pain relievers more than before to get desired 
effects or noticed that same amount of pain reliever use had less effect than before (PNRLNDMOR=1 or PNRLLSEFX=1) 
(4) Inability to cut down or stop using pain relievers every time tried or wanted to (PNRLCUTEV=2) 
(5) Continued to use pain relievers even though they were causing problems with emotions, nerves, mental health, or physical problems (PNRLEMCTD=1 or PNRLPHCTD=1) 
(6) Pain reliever use reduced or eliminated involvement or participation in important activities (PNRLLSACT=1) 
(7) Reported experiencing three or more pain reliever withdrawal symptoms at the same time that lasted longer than a day after pain reliever use was cut back or stopped. Symptoms include (i) feeling kind of blue or down; (ii) vomiting or feeling nauseous; (iii) having cramps or muscle aches; (iv) having teary eyes or a runny nose; (v) feeling sweaty, having enlarged pupils, or having body hair standing up on skin; (vi) having diarrhea; (vii) yawning; (viii) having a fever; and (ix) having trouble sleeping. (PNRLWDSMT=1). 
This recode was created using the edited dependence variable (DEPENDPNR) and imputing it so that all past year users were either defined with dependence or defined without dependence. Then the imputed dependence variable (IRDEPENDPNR) was converted to the 

# 1.7. HEROIN
To be defined with heroin dependence, DEPNDHER, a respondent must have met three or more of these heroin dependence criteria:
(1) Spent a great deal of time over a period of a month or more getting, using, or getting over the effects of heroin (HERLOTTM=1 or HERGTOVR=1)
(2) Used heroin more often than intended or was unable to keep set limits on heroin use (HERKPLMT=2)
(3) Needed to use heroin more than before to get desired effects or noticed that same amount of heroin use had less effect than before (HERNDMOR=1 or HERLSEFX=1)
(4) Inability to cut down or stop using heroin every time tried or wanted to (HERCUTEV=2)
(5) Continued to use heroin even though it was causing problems with emotions, nerves, mental health, or physical problems (HEREMCTD=1 or HERPHCTD=1)
(6) Heroin use reduced or eliminated involvement or participation in important activities (HERLSACT=1)
(7) Reported experiencing three or more heroin withdrawal symptoms at the same time that lasted longer than a day after heroin use was cut back or stopped. Symptoms include (i) feeling kind of blue or down; (ii) vomiting or feeling nauseous; (iii) having cramps or muscle aches; (iv) having teary eyes or a runny nose; (v) feeling sweaty, having enlarged eye pupils, or having body hair standing up on skin; (vi) having diarrhea; (vii) yawning; (viii) having a fever; and (ix) having trouble sleeping. (HERWDSMT=1).
This recoded variable's unknown values are included in the "no" response, and it is comparable with similarly named variables from prior years.
Note: A respondent could answer the dependence questions if he or she reported injecting with a needle, smoking, sniffing, or snorting heroin in the past year in the special drugs section, even if he or she reported not using heroin in the past year in the heroin section. Thus, cases may exist where a respondent was classified as dependent on heroin, even though he or she had not used heroin in the past year according to the imputed recency variable (HERYR

