# National Survery on Drug and Health (2015)

## IMPUTED DEMOGRAPHICS  (p.580)

(1) AGE CATAG6 Len : 1 RC-AGE CATEGORY RECODE (6 LEVELS) Freq Pct 
1 = 12-17 Years Old.............................................................................................. 13585 23.77 
2 = 18-25 Years Old.............................................................................................. 14553 25.47 
3 = 26-34 Years Old.............................................................................................. 9084 15.90 
4 = 35-49 Years Old.............................................................................................. 11169 19.54 
5 = 50-64 Years Old.............................................................................................. 5157 9.02 
6 = 65 or Older...................................................................................................... 3598 6.30 

(2) GENDER (QD01) 
IRSEX Len : 1 IMPUTATION REVISED GENDER Freq Pct 
1 = Male ............................................................................................................... 26736 46.79 
2 = Female ........................................................................................................... 30410 53.21 

(3) MARITAL 
IRMARITSTAT Len : 2 MARITAL STATUS - IMPUTATION REVISED Freq Pct 
1 = Married ........................................................................................................... 18062 31.61 
2 = Widowed ......................................................................................................... 1692 2.96 
3 = Divorced or Separated .................................................................................... 4856 8.50 
4 = Never Been Married ........................................................................................ 25897 45.32 
99 = LEGITIMATE SKIP Respondent is <= 14 years old ....................................... 6639 11.62 
  
(4) EDUCATION (IREDUHIGHST2) 
EDUHIGHCAT Len : 1 RC-EDUCATION CATEGORIES Freq Pct 
1 = Less high school (IREDUHIGHST2=1-7 & AGE2=7-17) .................................. 6299 11.02 
2 = High school grad (IREDUHIGHST2=8 & AGE2=7-17) ..................................... 11782 20.62 
3 = Some coll/Assoc Dg (IREDUHIGHST2=9-10 & AGE2=7-17) .......................... 14504 25.38 
4 = College graduate (IREDUHIGHST2=11 & AGE2=7-17) .................................. 10976 19.21 
5 = 12 to 17 year olds (AGE2=1-6) ....................................................................... 13585 23.77 
  
(5) EMPLOYMENT STATUS (AGE2, IRWRKSTAT) p.588  
IRWRKSTAT18 Len : 2 EMPLOYMENT STATUS 18+ - IMPUTATION REVISED Freq Pct 
1 = Employed full time .......................................................................................... 22179 38.81 
2 = Employed part time ......................................................................................... 7004 12.26 
3 = Unemployed ................................................................................................... 2857 5.00 
4 = Other (incl. not in labor force) .......................................................................... 11521 20.16 
99 = 12-17 year olds ............................................................................................. 13585 23.77 

(6) METRO/COUNTY - P.611 RECODE this variable to 0, 1, 2
COUTYP2 Len : 1 COUNTY METRO/NONMETRO STATUS (3-LEVEL) Freq Pct 
1 = Large Metro .................................................................................................... 25381 44.41 
2 = Small Metro .................................................................................................... 19889 34.80 
3 = Nonmetro ........................................................................................................ 11876 20.78 
 
 


PAIN RELIEVERS p.111
Following questions ask about using prescription pain relievers in any way a doctor did not direct you to use them. When you answer these questions, please think only about your use of the drug in any way a doctor did not direct you to use it, including: 
· Using it without a prescription of your own 
· Using it in greater amounts, more often, or longer than you were told to take it 
· Using it in any other way a doctor did not direct you to use it 
 
Have you ever, even once, used any prescription pain reliever in any way a doctor did not direct you to use it? 
 
(1) EVER USE PRL? (PRL01, PRL02) 
PNRNMLIF Len : 2 EVER USED PAIN RELIEVER NOT DIRECTED BY DR Freq Pct 
1 = Yes ................................................................................................................. 3138 5.49 
2 = No ................................................................................................................... 25720 45.01 
5 = Yes LOGICALLY ASSIGNED (from skip pattern) ............................................ 3181 5.57 
85 = BAD DATA Logically assigned ...................................................................... 60 0.10 
91 = NEVER USED/MISUSED PAIN RELIEVERS ................................................ 24507 42.88 
94 = DON'T KNOW ............................................................................................... 30 0.05 
97 = REFUSED .................................................................................................... 18 0.03 
98 = BLANK (NO ANSWER) ................................................................................. 492 0.86 

(2) USE PRL PAST 30 (PRM01) 
PNRNM30D Len : 2 USED PAIN RLVR NOT DIRECTED BY DR PAST 30 DAYS Freq Pct 
1 = Yes ................................................................................................................. 862 1.51 
2 = No ................................................................................................................... 2223 3.89 
5 = Yes LOGICALLY ASSIGNED (from PR30ANYINIT=1).................................... 80 0.14 
83 = DID NOT MISUSE PAIN RELIEVERS PST 30 DYS Log assn ...................... 44 0.08 
85 = BAD DATA Logically assigned ...................................................................... 4 0.01 
91 = NEVER USED/MISUSED PAIN RELIEVERS ................................................ 50227 87.89 
93 = DID NOT MISUSE PAIN RELIEVERS IN THE PAST 30 DAYS .................... 3380 5.91 
94 = DON'T KNOW ............................................................................................... 4 0.01 
97 = REFUSED .................................................................................................... 12 0.02 
98 = BLANK (NO ANSWER) ................................................................................. 310 0.54 
During the past 30 days, on how many days did you use [PRNAMEFILL] in any way a doctor did not direct you to use [PRNUMFILL]?  

(3) USE PRL >RX (PRYWAYS2) 
PNRWYGAMT Len : 2 USED PAIN RLVR IN GREATER AMTS THAN RX PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 659 1.15 
2 = No (not entered).............................................................................................. 2408 4.21 
83 = DID NOT USE PAIN REL IN THE PAST 12 MOS Log assn .......................... 12 0.02 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED/MISUSED PAIN RELIEVERS ................................................ 50227 87.89 
93 = DID NOT MISUSE PAIN RELIEVERS IN THE PAST 12 MOS ...................... 3412 5.97 
94 = DON'T KNOW ............................................................................................... 53 0.09 
97 = REFUSED .................................................................................................... 61 0.11 
98 = BLANK (NO ANSWER) ................................................................................. 311 0.54 
DRUG USE  						Codebook Creation Date: 10/20/2016……….136 
 
PAIN RELIEVERS - MISUSE
NOTE: The following 10 variables refer to the misuse of prescription drugs. p. 149 
Misuse of prescription drugs is defined as use in any way not directed by a doctor, including use without a prescription of one's own medication; use in greater amounts, more often, or longer than told to take a drug; or use in any other way not directed by a doctor. 
p.175
 
(4) PRL EVER MISUSE (IRPNRNMREC) 
PNRNMFLAG Len : 1 RC-PAIN RELIEVERS - EVER MISUSED Freq Pct 
0 = Never misused (IRPNRNMREC = 9) ............................................................... 50803 88.90 
1 = Ever misused (IRPNRNMREC = 1-3) .............................................................. 6343 11.10 
 
(5) PRL PAST YEAR MISUSE (IRPNRNMREC) 
PNRNMYR Len : 1 RC-PAIN RELIEVERS - PAST YEAR MISUSE Freq Pct 
0 = Did not misuse in the past year (IRPNRNMREC = 3,9) ................................... 53934 94.38 
1 = Misused within the past year (IRPNRNMREC = 1,2) ....................................... 3212 5.62 RECODED 
 
(IRPNRNMREC) 
(6) PRL PAST MONTH MISUSE
PNRNMMON Len : 1 RC-PAIN RELIEVERS - PAST MONTH MISUSE Freq Pct 
0 = Did not misuse in the pst mon (IRPNRNMREC = 2-3,9) .................................. 56183 98.31 
1 = Misused within the past month (IRPNRNMREC = 1) ....................................... 963 1.69 
 
(7) OXYC PAST YEAR MISUSE (IROXCNNMYR) 
OXYCNNMYR Len : 1 RC-OXYCONTIN - PAST YEAR MISUSE Freq Pct 
0 = Did not misuse in the past year (IROXCNNMYR = 3,9) ................................... 56621 99.08 
1 = Misused within the past year (IROXCNNMYR = 1,2) ....................................... 525 0.92 
 
(8)  PRL DEPENDENCE PAST YEAR (IRDEPENDPNR) 
DEPNDPYPNR Len : 1 RC-PAIN RELIEVER DEPENDENCE - PAST YEAR Freq Pct 
0 = No (IRDEPENDPNR=0,91,93) ........................................................................ 56756 99.32 
1 = Yes (IRDEPENDPNR=1) ................................................................................ 390 0.68 

(9) PRL ABUSE - PAST YEAR (DEPNDPYPNR, IRABUPOSPNR) 
ABUSEPYPNR Len : 1 RC-PAIN RELIEVER ABUSE - PAST YEAR Freq Pct 
0 = No (IRABUPOSPNR=0,91,93 or DEPNDPYPNR=1) ....................................... 57020 99.78 
1 = Yes (IRABUPOSPNR=1 and DEPNDPYPNR=0) ............................................ 126 0.22 
 
Now think about the last time you used [PRLASTFILL2] in any way a doctor did not direct you to use it/them. What were the reasons you used [PRLASTFILL2] the last time? 
  
(10) USE PRL TO GET HIGH (PRYMOTV4) 
PNRRSHIGH Len : 2 USED LAST PAIN RLVR (NOT DIRECTED) TO GET HIGH Freq Pct 
1 = Yes ................................................................................................................. 766 1.34 
2 = No (not entered).............................................................................................. 2368 4.14 
3 = Yes LOGICALLY ASSIGNED ......................................................................... 6 0.01 
83 = DID NOT USE PAIN RELIEVERS PST 12 MOS Log assn ............................ 2 0.00 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED/MISUSED PAIN RELIEVERS ................................................ 50227 87.89 
93 = DID NOT MISUSE PAIN RELIEVERS IN THE PAST 12 MOS ...................... 3422 5.99 
94 = DON'T KNOW ............................................................................................... 19 0.03 
97 = REFUSED .................................................................................................... 22 0.04 
98 = BLANK (NO ANSWER) ................................................................................. 313 0.55   

NOTE: The variable PNRNMREC is a recoded variable that was created from PNRNMLIF, the 12-month misuse variables of specific pain relievers, and PNRLVNM30DY. 
 
PNRNMREC Len : 2 RC - MOST RECENT PAIN RELIEVER MISUSE (RECODE) Freq Pct 
1 = Within the past 30 days ................................................................................... 942 1.65 
2 = More than 30 days ago but within the past 12 mos ......................................... 2223 3.89 
3 = More than 12 months ago ............................................................................... 3092 5.41 
8 = Misused at some point in past 12 mos LOG ASSN ......................................... 16 0.03 
9 = Misused at some point in lifetime LOG ASSN ................................................. 46 0.08 
83 = DID NOT MISUSE PST 12 MOS (LIFETIME UNK) Log assn ........................ 332 0.58 
91 = NEVER USED/MISUSED PAIN RELIEVERS ................................................ 50227 87.89 
98 = BLANK (NO ANSWER) ................................................................................. 268 0.47 

NOTE: PNRNMINIT is "reverse coded" from the answers in PRL03. PRL03=1 (yes) was recoded to 2 in PNRNMINIT because this answer means that the respondent misused pain relievers before the past 12 months (and therefore is not a past year initiate for misuse of pain relievers). PRL03=2 (no) was recoded to 1 in PNRNMINIT because this answer means that the respondent did not misuse pain relievers before the past 12 months (and therefore is a past year initiate for misuse of pain relievers). Earlier questions were about the past 12 months. This question is about any time before then, that is, any time in your life before [DATEFILL]. At any time before [DATEFILL], did you ever use any prescription pain reliever in a way a doctor did not direct you to use it? 
 


 RECODED DRUG USE				Codebook Creation Date: 10/20/2016……….p.181
 
The following variable for any past year use of Hydrocodone Products, HYDCPDAPYU, was assigned a positive response if a respondent indicated any past year use of Vicodin, Lortab, Norco, Zohydro ER, generic hydrocodone, or past year misuse of other pain relievers that contain hydrocodone.
 
(1) HYDROCODONE PAST YEAR USE
HYDCPDAPYU Len : 1 RC-HYDROCODONE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 46262 80.95
1 = Yes (See comment above) .............................................................................. 10884 19.05
  
The following variable for any past year use of Oxycodone Products, OXYCPDAPYU, was assigned a positive response if a respondent indicated any past year use of OxyContin (OXCNANYYR=1, 3, 5), Percocet, Percodan, Roxicet, Roxicodone, or generic oxycodone, or past year misuse of other pain relievers that contain oxycodone.
 
(2) OXY PRODUCTS PAST YEAR USE (OXCNANYYR)
OXYCPDAPYU Len : 1 RC-OXYCODONE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 51448 90.03
1 = Yes (See comment above) .............................................................................. 5698 9.97
 
(3) OXYCONTIN - PAST YEAR USE (OXCNANYYR)
OXCNANYYR2 Len : 1 RC-OXYCONTIN - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 55189 96.58
1 = Yes (OXCNANYYR=1,3,5) .............................................................................. 1957 3.42
 
The following variable for any past year use of Tramadol Products, TRAMPDAPYU, was assigned a positive response if a respondent indicated any past year use of Ultram, Ultram ER, Ultracet, generic tramadol, or generic extended-release tramadol, or past year misuse of other pain relievers that contain tramadol.
 
(4) TRAMADOL PRODUCTS - ANY PAST YEAR USE
TRAMPDAPYU Len : 1 RC-TRAMADOL PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 53935 94.38
1 = Yes (See comment above) .............................................................................. 3211 5.62
 
The following variable for any past year use of Morphine Products, MORPPDAPYU, was assigned a positive response if a respondent indicated any past year use of Avinza, Kadian, MS Contin, generic morphine, or generic extended-release morphine, or past year misuse of other pain relievers that contain morphine.

(5) MORPHINE PRODUCTS - PAST YEAR USE
MORPPDAPYU Len : 1 RC-MORPHINE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 55629 97.35
1 = Yes (See comment above) .............................................................................. 1517 2.65
 
The following variable for any past year use of Fentanyl Products, FENTPDAPYU, was assigned a positive response if a respondent indicated any past year use of Actiq, Duragesic, Fentora, or generic fentanyl, or past year misuse of other pain relievers that contain fentanyl.
 
(6) FENTANYL PRODUCTS - ANY PAST YEAR USE
FENTPDAPYU Len : 1 RC-FENTANYL PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 56758 99.32
1 = Yes (See comment above) .............................................................................. 388 0.68
 
The following variable for any past year use of Buprenorphine Products, BUPRPDAPYU, was assigned a positive response if a respondent indicated any past year use of Suboxone, generic buprenorphine, or past year misuse of other pain relievers that contain buprenorphine.

(7) BUPRENORPHINE PRODUCTS - ANY PAST YEAR USE
BUPRPDAPYU Len : 1 RC-BUPRENORPHINE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 56564 98.98
1 = Yes (See comment above) .............................................................................. 582 1.02
 
The following variable for any past year use of Oxymorphone Products, OXYMPDAPYU, was assigned a positive response if a respondent indicated any past year use of Opana, Opana ER, generic oxymorphone, generic extended-release oxymorphone, or past year misuse of other pain relievers that contain oxymorphone.

(8) OXYMORPHONE PRODUCTS - ANY PAST YEAR USE 
OXYMPDAPYU Len : 1 RC-OXYMORPHONE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 56867 99.51
1 = Yes (See comment above) .............................................................................. 279 0.49
 
The following variable for any past year use of Demerol Products, DEMEPDAPYU, was assigned a positive response if a respondent indicated any past year use of Demerol, or past year misuse of other pain relievers that contain Demerol.

(9) DEMEROL PRODUCTS - ANY PAST YEAR USE
DEMEPDAPYU Len : 1 RC-DEMEROL PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 56862 99.50
1 = Yes (See comment above) .............................................................................. 284 0.50
 
The following variable for any past year use of Hydromorphone Products, HYDMPDAPYU, was assigned a positive response if a respondent indicated any past year use of Dilaudid or generic hydromorphone, Exalgo or generic extended-release hydromorphone, or past year misuse of other pain relievers that contain hydromorphone.

(10) HYDROMORPHONE - PAST YEAR USE
HYDMPDAPYU Len : 1 RC-HYDROMORPHONE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 56722 99.26
1 = Yes (See comment above) .............................................................................. 424 0.74
 




 (RPRYLAST) 
PNRNMLAST Len : 2 LAST PAIN RLVR USED NOT DIRECTED BY DR PST 12 MOS Freq Pct 
1 = Vicodin ............................................................................................................ 385 0.67 
2 = Lortab ............................................................................................................. 145 0.25 
3 = Norco .............................................................................................................. 169 0.30 
4 = Zohydro ER .................................................................................................... 2 0.00 
5 = Hydrocodone (generic) ................................................................................... 528 0.92 
6 = OxyContin ....................................................................................................... 151 0.26 
7 = Percocet ......................................................................................................... 309 0.54 
8 = Percodan ........................................................................................................ 4 0.01 
9 = Roxicet ........................................................................................................... 13 0.02 
10 = Roxicodone ................................................................................................... 28 0.05 
11 = Oxycodone (generic) ..................................................................................... 163 0.29 
12 = Ultram ........................................................................................................... 19 0.03 
13 = Ultram ER ..................................................................................................... 3 0.01 
14 = Ultracet ......................................................................................................... 2 0.00 
15 = Tramadol (generic)........................................................................................ 209 0.37 
16 = Extended-release tramadol (generic) ............................................................ 3 0.01 
17 = Tylenol with codeine 3 or 4 ........................................................................... 536 0.94 
18 = Codeine pills (generic) .................................................................................. 54 0.09 
19 = Avinza ........................................................................................................... 2 0.00 
20 = Kadian .......................................................................................................... 1 0.00 
21 = MS Contin ..................................................................................................... 2 0.00 
22 = Morphine (generic) ........................................................................................ 33 0.06 
23 = Extended-release morphine (generic) ........................................................... 10 0.02 
24 = Actiq ............................................................................................................. 1 0.00 
26 = Fentora ......................................................................................................... 2 0.00 
27 = Fentanyl (generic) ......................................................................................... 7 0.01 
28 = Suboxone ..................................................................................................... 93 0.16 
29 = Buprenorphine (generic) ............................................................................... 12 0.02 
30 = Opana ........................................................................................................... 11 0.02 
31 = Opana ER ..................................................................................................... 1 0.00 
32 = Oxymorphone (generic) ................................................................................ 1 0.00 
33 = Extended-release oxymorphone (generic) .................................................... 2 0.00 
34 = Demerol ........................................................................................................ 4 0.01 
35 = Dilaudid or hydromorphone .......................................................................... 10 0.02 
37 = Methadone .................................................................................................... 51 0.09 
38 = Some other pain reliever ............................................................................... 187 0.33 
83 = DID NOT MISUSE IN THE PST 12 MOS Logically assigned......................... 45 0.08 
85 = BAD DATA Logically assigned ...................................................................... 9 0.02 
91 = NEVER USED/MISUSED PAIN RELIEVERS ................................................ 50227 87.89 
93 = DID NOT MISUSE PAIN RELIEVERS IN THE PAST 12 MOS ...................... 3379 5.91 
94 = DON'T KNOW ............................................................................................... 17 0.03 
97 = REFUSED .................................................................................................... 6 0.01 
98 = BLANK (NO ANSWER) ................................................................................. 310 0.54 

 
 
 
HEROIN 

p. 311
 
(DEPNDHER, HERFMCTD, HERFMFPB, HERLAWTR, HERPDANG, HERSERPB) 
ABUSEHER Len : 1 RC-HEROIN ABUSE - PAST YEAR Freq Pct 
0 = No/Unknown (Otherwise) ................................................................................ 57138 99.99 
1 = Yes (Any one of above criteria and DEPNDHER=0) ....................................... 8 0.01 
 
p. 313
 
(ABUSEHER, DEPNDHER) 
ABODHER Len : 1 RC-HEROIN DEPENDENCE OR ABUSE - PAST YEAR Freq Pct 
0 = No/Unknown (ABUSEHER=0 and DEPNDHER=0) ......................................... 56995 99.74 
1 = Yes (ABUSEHER=1 or DEPNDHER=1) .......................................................... 151 0.26 
 
p. 152
 
(HERYRTOT) 
IRHERFY Len : 3 HEROIN FREQUENCY PAST YEAR - IMPUTATION REVISED Freq Pct 
RANGE = 1 - 365 .................................................................................................. 223 0.39 
991 = NEVER USED HEROIN .............................................................................. 56190 98.33 
993 = DID NOT USE HEROIN PAST YEAR ......................................................... 733 1.28 
 
 
 p.162
 p. 75
 
HEROIN 
These next questions are about heroin. 
Have you ever, even once, used heroin? 
(HE01, HEREF) 
HEREVER Len : 2 EVER USED HEROIN Freq Pct 
1 = Yes ................................................................................................................. 956 1.67 
2 = No ................................................................................................................... 56153 98.26 
94 = DON'T KNOW ............................................................................................... 34 0.06 
97 = REFUSED .................................................................................................... 3 0.01 
 
 
How long has it been since you last used heroin? 
(HELAST3, HERECDK, HERECRE) 
HERREC Len : 2 TIME SINCE LAST USED HEROIN Freq Pct 
1 = Within the past 30 days ................................................................................... 85 0.15 
2 = More than 30 days ago but within the past 12 mos ......................................... 116 0.20 
3 = More than 12 months ago ............................................................................... 727 1.27 
8 = Used at some point in the past 12 mos LOG ASSN ........................................ 17 0.03 
9 = Used at some point in the lifetime LOG ASSN ................................................ 10 0.02 
11 = Used in the past 30 days LOGICALLY ASSIGNED ....................................... 1 0.00 
91 = NEVER USED HEROIN ................................................................................ 56153 98.26 
97 = REFUSED .................................................................................................... 3 0.01 
98 = BLANK (NO ANSWER) ................................................................................. 34 0.06 
 
(TOTHERO) 
HERYRTOT Len : 3 TOTAL # OF DAYS USED HEROIN IN PAST 12 MONTHS Freq Pct 
RANGE = 1 - 365 .................................................................................................. 201 0.35 
985 = BAD DATA Logically assigned .................................................................... 15 0.03 
991 = NEVER USED HEROIN .............................................................................. 56153 98.26 
993 = DID NOT USE HEROIN IN THE PAST 12 MOS.......................................... 727 1.27 
994 = DON'T KNOW ............................................................................................. 1 0.00 
997 = REFUSED .................................................................................................. 5 0.01 
998 = BLANK (NO ANSWER) ............................................................................... 44 0.08 
 
 
On how many days in the past 12 months did you use heroin? 
 
(HEYRAVE) 
HRDAYPYR Len : 3 # DAYS USED HEROIN PAST 12 MONTHS Freq Pct 
RANGE = 1 - 365 .................................................................................................. 95 0.17 
985 = BAD DATA Logically assigned .................................................................... 2 0.00 
991 = NEVER USED HEROIN .............................................................................. 56153 98.26 
993 = DID NOT USE HEROIN IN THE PAST 12 MOS.......................................... 727 1.27 
994 = DON'T KNOW ............................................................................................. 1 0.00 
997 = REFUSED .................................................................................................. 4 0.01 
998 = BLANK (NO ANSWER) ............................................................................... 57 0.10 
999 = LEGITIMATE SKIP ..................................................................................... 107 0.19 
 
On average, how many days did you use heroin each month during the past 12 months? 
 
(HEMONAVE) 
HRDAYPMO Len : 2 # DAYS PER MONTH USED HEROIN PAST 12 MONTHS Freq Pct 
RANGE = 1 - 30 .................................................................................................... 48 0.08 
85 = BAD DATA Logically assigned ...................................................................... 4 0.01 
91 = NEVER USED HEROIN ................................................................................ 56153 98.26 
93 = DID NOT USE HEROIN IN THE PAST 12 MOS ........................................... 727 1.27 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 4 0.01 
98 = BLANK (NO ANSWER) ................................................................................. 55 0.10 
99 = LEGITIMATE SKIP ....................................................................................... 154 0.27 

On average, how many days did you use heroin each week during the past 12 months? 
 
(HEWKAVE) 
HRDAYPWK Len : 2 # DAYS PER WEEK USED HEROIN PAST 12 MONTHS Freq Pct 
RANGE = 1 - 7 ...................................................................................................... 58 0.10 
85 = BAD DATA Logically assigned ...................................................................... 9 0.02 
91 = NEVER USED HEROIN ................................................................................ 56153 98.26 
93 = DID NOT USE HEROIN IN THE PAST 12 MOS ........................................... 727 1.27 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 5 0.01 
98 = BLANK (NO ANSWER) ................................................................................. 50 0.09 
99 = LEGITIMATE SKIP ....................................................................................... 143 0.25 
 
 
DEPNDHER Len : 1 RC-HEROIN DEPENDENCE - PAST YEAR Freq Pct 
0 = No/Unknown (Otherwise) ................................................................................ 57003 99.75 
1 = Yes (See comment above DEPNDALC) ......................................................... 143 0.25 
 
 The following variable for any past year use of Methadone Products, MTDNPDAPYU, was assigned a positive response if a respondent indicated any past year use of Methadone, or past year misuse of other pain relievers that contain methadone.
 
MTDNPDAPYU Len : 1 RC-METHADONE PRODUCTS - ANY PAST YEAR USE Freq Pct
0 = No/Unknown (Otherwise) ................................................................................ 56818 99.43
1 = Yes (See comment above) .............................................................................. 328 0.57
 

 
p.344
DRUG TREATMENT 
The values in this section may be inconsistent with values for variables in other sections of the interview. Items in this section were edited when respondents legitimately skipped out of these items based on prior answers in earlier sections. Otherwise, variables in one section of the interview generally were not edited to make them consistent with variables in another section of the interview. This note applies to variables in this section marked by a1. 
 
NOTE: Respondents were not asked questions in the SUBSTANCE TREATMENT module if they did not report lifetime use of alcohol, marijuana, cocaine, heroin, hallucinogens, inhalants, methamphetamine, or lifetime misuse of prescription psychotherapeutics (pain relievers, tranquilizers, stimulants, or sedatives). Codes of 91 in the edited SUBSTANCE TREATMENT variables indicate that the questions did not apply because respondents never used (or misused) any of these substances. 
 
These next questions deal with treatment for alcohol and drug problems, not including cigarettes. Please report treatment or counseling designed to help you reduce or stop your alcohol or drug use. Please include detoxification and any other treatment for medical problems associated with your alcohol or drug use. 
 
Have you ever received treatment or counseling for your use of alcohol or any drug, not cigarettes? 
(TX01) 
TXEVRRCVD1 Len : 2 EVER RECEIVED ALCOHOL OR DRUG TREATMENT Freq Pct 
1 = Yes ................................................................................................................. 2956 5.17 
2 = No ................................................................................................................... 40365 70.63 
85 = BAD DATA Logically assigned ...................................................................... 17 0.03 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 42 0.07 
97 = REFUSED .................................................................................................... 81 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 750 1.31 
During the past 12 months, that is since [DATEFILL] have you received treatment or counseling for your use of alcohol or any drug, not counting cigarettes? 
(TX02) 
TXYRRECVD1 Len : 2 EVER RECEIVED ALCOHOL OR DRUG TRMT PAST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 828 1.45 
2 = No ................................................................................................................... 2037 3.56 
3 = Yes LOGICALLY ASSIGNED ......................................................................... 86 0.15 
4 = No LOGICALLY ASSIGNED ........................................................................... 2 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 2 0.00 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 809 1.42 
99 = LEGITIMATE SKIP (TXEVRRCVD=2) .......................................................... 40365 70.63 
During the past 12 months when you received treatment, was the treatment for alcohol use only, drug use only, or both alcohol and drug use? 
(TX03) 
TXYRALDGB1 Len : 2 TRMT FOR ALC, DRUG OR BOTH PAST 12 MONTHS Freq Pct 
1 = Alcohol use only.............................................................................................. 237 0.41 
2 = Drug use only ................................................................................................. 294 0.51 
3 = Both alcohol and drug use .............................................................................. 235 0.41 
4 = Alcohol (drug trmt unknown) LOGICALLY ASSIGNED .................................... 2 0.00 
5 = Drugs (alcohol trmt unknown) LOGICALLY ASSIGNED .................................. 2 0.00 
11 = Alcohol only (but last tmt for drugs reported) ................................................. 25 0.04 
12 = Drugs only (but last tmt for alc reported) ....................................................... 28 0.05 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 85 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 DRUG TREATMENT 
Codebook Creation Date: 10/20/2016……….302 
 
During the past 12 months, have you received treatment for your [TXFILL1] in a hospital overnight as an inpatient? 
(TX04A) 
TXYRHOSOV1 Len : 2 RCVD TXFILL1 TRMT IN HOSP/OVERNIGHT PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 169 0.30 
2 = No ................................................................................................................... 652 1.14 
5 = Yes LOGICALLY ASSIGNED (from TXLTYMNPL2)........................................ 3 0.01 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 
Was the treatment you received in a hospital overnight as an inpatient for your alcohol use, your drug use, or both? 
(TX04A1) 
TXYRHOSAD1 Len : 2 HOSP/OVERNIGHT TRMT FOR ALC, DRUGS, OR BOTH Freq Pct 
1 = Alcohol use ..................................................................................................... 4 0.01 
2 = Drug use ......................................................................................................... 9 0.02 
3 = Both alcohol and drug use .............................................................................. 39 0.07 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 920 1.61 
99 = LEGITIMATE SKIP ....................................................................................... 43156 75.52 
During the past 12 months, have you received treatment for your [TXFILL1] in a residential drug or alcohol rehabilitation facility where you stayed overnight? 
(TX04B) 
TXYRRESOV1 Len : 2 RCVD TXFILL1 TRMT REHAB CENTR/OVERNIGHT PST 12 MO Freq Pct 
1 = Yes ................................................................................................................. 200 0.35 
2 = No ................................................................................................................... 599 1.05 
5 = Yes LOGICALLY ASSIGNED (from TXLTYMNPL2)........................................ 25 0.04 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 
Was the treatment you received in a residential drug or alcohol rehabilitation facility where you stayed overnight for your alcohol use, your drug use, or both? 
(TX04B1) 
TXYRRESAD1 Len : 2 RES ALC/DRG REH TRMT FOR ALC, DRUGS, OR BOTH Freq Pct 
1 = Alcohol use ..................................................................................................... 1 0.00 
2 = Drug use ......................................................................................................... 8 0.01 
3 = Both alcohol and drug use .............................................................................. 65 0.11 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 935 1.64 
99 = LEGITIMATE SKIP ....................................................................................... 43119 75.45 DRUG TREATMENT 
Codebook Creation Date: 10/20/2016……….303 
 
During the past 12 months, have you received treatment for your [TXFILL1] in a drug or alcohol rehabilitation facility as an outpatient? 
(TX04C) 
TXYROUTPT1 Len : 2 RCVD TXFILL1 TRMT REHAB CENTR/OUTPT PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 340 0.59 
2 = No ................................................................................................................... 448 0.78 
3 = Yes LOGICALLY ASSIGNED ......................................................................... 1 0.00 
5 = Yes LOGICALLY ASSIGNED (from TXLTYMNPL2)........................................ 35 0.06 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 
Was the treatment you received in a drug or alcohol rehabilitation facility as an outpatient for your alcohol use, your drug use, or both? 
(TX04C1) 
TXYROUTAD1 Len : 2 OUTPATIENT TRMT FOR ALC, DRUGS, OR BOTH Freq Pct 
1 = Alcohol use ..................................................................................................... 3 0.01 
2 = Drug use ......................................................................................................... 9 0.02 
3 = Both alcohol and drug use .............................................................................. 88 0.15 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 940 1.64 
99 = LEGITIMATE SKIP ....................................................................................... 43087 75.40 
During the past 12 months, have you received treatment for your [TXFILL1] in a mental health center or facility as an outpatient? 
(TX04D) 
TXYRMHCOP1 Len : 2 RCVD TXFILL1 TRMT MNT HEALTH CNTR/OUTPT PST 12 MO Freq Pct 
1 = Yes ................................................................................................................. 251 0.44 
2 = No ................................................................................................................... 531 0.93 
5 = Yes LOGICALLY ASSIGNED (from TXLTYMNPL2)........................................ 40 0.07 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 2 0.00 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 
Was the treatment you received in a mental health center or facility as an outpatient for your alcohol use, your drug use, or both? 
(TX04D1) 
TXYRMHCAD1 Len : 2 MNT HEALTH CNTR TRMT FOR ALC, DRUGS, OR BOTH Freq Pct 
1 = Alcohol use ..................................................................................................... 2 0.00 
2 = Drug use ......................................................................................................... 7 0.01 
3 = Both alcohol and drug use .............................................................................. 49 0.09 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 938 1.64 
99 = LEGITIMATE SKIP ....................................................................................... 43131 75.48 DRUG TREATMENT 
Codebook Creation Date: 10/20/2016……….304 
 
During the past 12 months, have you received treatment for your [TXFILL1] in an emergency room? 
(TX04E) 
TXYREMRGN1 Len : 2 RCVD TXFILL1 TRMT IN EMERGENCY ROOM PAST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 86 0.15 
2 = No ................................................................................................................... 719 1.26 
3 = Yes LOGICALLY ASSIGNED ......................................................................... 18 0.03 
5 = Yes LOGICALLY ASSIGNED (from TXLTYMNPL2)........................................ 1 0.00 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 
Was the treatment you received in an emergency room for your alcohol use, your drug use, or both? 
(TX04E1) 
TXYREMRAD1 Len : 2 EMERGENCY ROOM TRMT FOR ALC, DRUGS, OR BOTH Freq Pct 
2 = Drug use ......................................................................................................... 6 0.01 
3 = Both alcohol and drug use .............................................................................. 10 0.02 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 924 1.62 
99 = LEGITIMATE SKIP ....................................................................................... 43187 75.57 
During the past 12 months, have you received treatment for your [TXFILL1] in a private doctor's office? 
(TX04F) 
TXYRDRPRV1 Len : 2 RCVD TXFILL1 TRMT IN PRIV DR.'S OFFICE PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 164 0.29 
2 = No ................................................................................................................... 644 1.13 
3 = Yes LOGICALLY ASSIGNED ......................................................................... 1 0.00 
5 = Yes LOGICALLY ASSIGNED (from TXLTYMNPL2)........................................ 14 0.02 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 897 1.57 
99 = LEGITIMATE SKIP ....................................................................................... 42404 74.20 
Was the treatment you received in a private doctor's office for your alcohol use, your drug use, or both? 
(TX04F1) 
TXYRDRPAD1 Len : 2 PRIV DR.'S OFFICE TRMT FOR ALC, DRUGS, OR BOTH Freq Pct 
1 = Alcohol use ..................................................................................................... 1 0.00 
2 = Drug use ......................................................................................................... 10 0.02 
3 = Both alcohol and drug use .............................................................................. 17 0.03 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 917 1.60 
99 = LEGITIMATE SKIP ....................................................................................... 43183 75.57 
 
 
 
 
(TX07) 
TXCURRENT1 Len : 2 CURRENTLY RECEIVING TRMT/COUNSELING FOR TXFILL1 Freq Pct 
1 = Yes ................................................................................................................. 388 0.68 
2 = No ................................................................................................................... 441 0.77 
4 = No LOGICALLY ASSIGNED ........................................................................... 1 0.00 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
89 = LEGITIMATE SKIP Logically assigned .......................................................... 2 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 82 0.14 
98 = BLANK (NO ANSWER) ................................................................................. 894 1.56 
99 = LEGITIMATE SKIP ....................................................................................... 42402 74.20 
 
p.348
(TX10) 
NDMORTHER1 Len : 2 NEED ADDL TRMT FOR USE OF HEROIN PAST 12 MOS Freq Pct 
1 = Response entered .......................................................................................... 14 0.02 
6 = Response not entered ..................................................................................... 36 0.06 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
97 = REFUSED .................................................................................................... 2 0.00 
98 = BLANK (NO ANSWER) ................................................................................. 979 1.71 
99 = LEGITIMATE SKIP ....................................................................................... 43180 75.56 
 
Are you currently receiving treatment or counseling for your use of prescription pain relievers? 
(TX32) 
TXLTYPNRL1 Len : 2 LAST/CURRENT TRMT FOR PRESCRIPTION PAIN RELIEVERS Freq Pct 
1 = Yes ................................................................................................................. 194 0.34 
2 = No ................................................................................................................... 237 0.41 
3 = Yes LOGICALLY ASSIGNED ......................................................................... 9 0.02 
6 = NEVER USED PAIN RELIEVERS (TXEVRRCVD = 1).................................... 434 0.76 
89 = LEGITIMATE SKIP Logically assigned (TXEVRRCVD=2) ............................. 1 0.00 
91 = NEVER USED ALCOHOL OR DRUGS ......................................................... 12935 22.64 
94 = DON'T KNOW ............................................................................................... 2 0.00 
97 = REFUSED .................................................................................................... 83 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 848 1.48 
99 = LEGITIMATE SKIP (TXEVRRCVD=2/TXYRRECVD=2,4) ............................. 42403 74.20 
 
p. 391
The following variable, TXYRNOSPIL, is defined as needing illicit drug treatment in the past year, but not receiving illicit drug treatment at a specialty facility. This treatment measure is referred to as a treatment gap. 
(TXYRNDILL, TXYRSPILL) 
TXYRNOSPIL Len : 1 RC-NEEDED TRT FOR ILL DRG USE, NOT RCVD TRT SPC FAC - PST YR Freq Pct 
0 = No/Unknown (Otherwise) ................................................................................ 55096 96.41 
1 = Yes (TXYRNDILL=1 and TXYRSPILL=0) ........................................................ 2050 3.59 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p. 395
 
HEALTH Variables

During the past 12 months, have you stayed overnight or longer as an inpatient in a hospital? 
(HLTH17) 
INHOSPYR Len : 2 STAYED OVERNIGHT AS INPNT IN HOSP PAST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 4763 8.33 
2 = No ................................................................................................................... 52107 91.18 
85 = BAD DATA Logically assigned ...................................................................... 4 0.01 
94 = DON'T KNOW ............................................................................................... 132 0.23 
97 = REFUSED .................................................................................................... 128 0.22 
98 = BLANK (NO ANSWER) ................................................................................. 12 0.02 
 
During the past 12 months, did any doctor or other health care professional talk to you about your use of [MARIJUANA/COCAINE/CRACK/HEROIN/INHALANTS/HALLUCINOGENS/METHAMPHETAMINE]? 
(HLTH23) 
HPDRGTALK Len : 2 HEALTH PROF DISCUSSED MY DRUG USE WITH ME Freq Pct 
1 = Yes ................................................................................................................. 1721 3.01 
2 = No ................................................................................................................... 6773 11.85 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
91 = NEVER USED MJ/COC/HER/HALL/INH/METH ............................................ 30641 53.62 
93 = DID NOT USE MJ/COC/HER/HAL/INH/METH IN PST 12 MOS .................... 15059 26.35 
94 = DON'T KNOW ............................................................................................... 18 0.03 
97 = REFUSED .................................................................................................... 12 0.02 
98 = BLANK (NO ANSWER) ................................................................................. 683 1.20 
99 = LEGITIMATE SKIP ....................................................................................... 2236 3.91 
 
These next questions are about certain medical conditions. During the past 12 months, did you have a sexually transmitted disease such as chlamydia, gonorrhea, herpes or syphilis? 
(HLTH24) 
STDANYYR1 Len : 2 HAD SEXUALLY TRANSMITTED DISEASE PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 1286 2.25 
2 = No ................................................................................................................... 55548 97.20 
85 = BAD DATA Logically assigned ...................................................................... 5 0.01 
94 = DON'T KNOW ............................................................................................... 124 0.22 
97 = REFUSED .................................................................................................... 170 0.30 
98 = BLANK (NO ANSWER) ................................................................................. 13 0.02 
 
(HLTH2505) 
HEPBCEVER1 Len : 2 EVER TOLD HAD HEPATITIS B OR C Freq Pct 
1 = Yes ................................................................................................................. 384 0.67 
2 = No (not entered).............................................................................................. 15992 27.98 
85 = BAD DATA Logically assigned ...................................................................... 7 0.01 
94 = DON'T KNOW ............................................................................................... 373 0.65 
97 = REFUSED .................................................................................................... 298 0.52 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 40075 70.13 
 
(HLTH2508) 
HIVAIDSEV1 Len : 2 EVER TOLD HAD HIV OR AIDS Freq Pct 
1 = Yes ................................................................................................................. 84 0.15 
2 = No (not entered).............................................................................................. 16292 28.51 
85 = BAD DATA Logically assigned ...................................................................... 7 0.01 
94 = DON'T KNOW ............................................................................................... 373 0.65 
97 = REFUSED .................................................................................................... 298 0.52 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 40075 70.13 
(HLTH2509) 
 
CANCEREVR1 Len : 2 EVER TOLD HAD CANCER Freq Pct 
1 = Yes ................................................................................................................. 1584 2.77 
2 = No (not entered).............................................................................................. 14792 25.88 
85 = BAD DATA Logically assigned ...................................................................... 7 0.01 
94 = DON'T KNOW ............................................................................................... 373 0.65 
97 = REFUSED .................................................................................................... 298 0.52 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 40075 70.13 
 
BMI2 was created from the variables WTPOUND2 and HTINCHE2 according to the formula of 703 times WTPOUND2 divided by the square of HTINCHE2. BMI2 was set to a SAS missing value (unknown) if WTPOUND2 had a value of 9985, 9994, 9997, or 9998 or if HTINCHE2 had a value of 985, 994, 997, or 998. 
BMI2 Len : 12 RC-BODY MASS INDEX (BMI) Freq Pct 
RANGE = 9.3733333333 - 68.557024793 ............................................................. 54607 95.56 
. = Unknown (See comment above) ...................................................................... 2539 4.44 
 
(ADMT01, ADMTREF1) 
AUINPYR1 Len : 2 STAY OVNT IN HOSP FOR MH TRMT PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 465 0.81 
2 = No ................................................................................................................... 42948 75.15 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
94 = DON'T KNOW ............................................................................................... 47 0.08 
97 = REFUSED .................................................................................................... 85 0.15 
98 = BLANK (NO ANSWER) ................................................................................. 13 0.02 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
 
(ADMT13, ADMTREF2) 
AUOPTYR1 Len : 2 RCVD OUTPATIENT MH TRMT PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 3314 5.80 
2 = No ................................................................................................................... 40044 70.07 
3 = Yes LOGICALLY ASSIGNED (from AUALOTS2) ............................................ 3 0.01 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
94 = DON'T KNOW ............................................................................................... 85 0.15 
97 = REFUSED .................................................................................................... 98 0.17 
98 = BLANK (NO ANSWER) ................................................................................. 14 0.02 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
 
(ADMT14) 
AUOPTHER1 Len : 2 MH TRMT IN PRIV THERAPIST'S OFC PST 12 MOS Freq Pct 
1 = Response entered .......................................................................................... 1890 3.31 
3 = Response entered LOGICALLY ASSIGNED ................................................... 1 0.00 
6 = Response not entered ..................................................................................... 1404 2.46 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 13 0.02 
97 = REFUSED .................................................................................................... 103 0.18 
98 = BLANK (NO ANSWER) ................................................................................. 105 0.18 
99 = LEGITIMATE SKIP ....................................................................................... 53629 93.85 
 
Did you receive treatment, counseling or support from any other sources such as these during the past 12 months? 
(ADMT29A) 
AUALTYR1 Len : 2 RCVD ALTERNATIVE MENT HLTH TRMT PAST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 4067 7.12 
2 = No ................................................................................................................... 39260 68.70 
3 = Yes LOGICALLY ASSIGNED (from AUOPYRS2) ........................................... 7 0.01 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
94 = DON'T KNOW ............................................................................................... 90 0.16 
97 = REFUSED .................................................................................................... 119 0.21 
98 = BLANK (NO ANSWER) ................................................................................. 15 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
From what source did you receive other treatment, counseling or support for problems with your emotions, nerves or mental health in the past 12 months? 
 
(ADMT29B) 
AUALACUP1 Len : 2 RCVD ALT MH TMT FROM ACUPUNCTURIST PST 12 MOS Freq Pct 
1 = Response entered .......................................................................................... 445 0.78 
6 = Response not entered ..................................................................................... 3590 6.28 
85 = BAD DATA Logically assigned ...................................................................... 3 0.01 
94 = DON'T KNOW ............................................................................................... 17 0.03 
97 = REFUSED .................................................................................................... 134 0.23 
98 = BLANK (NO ANSWER) ................................................................................. 112 0.20 
99 = LEGITIMATE SKIP ....................................................................................... 52845 92.47 
 
(ADMT29B) 
AUALCHIR1 Len : 2 RCVD ALT MH TMT FROM CHIROPRACTOR PST 12 MOS Freq Pct 
1 = Response entered .......................................................................................... 1688 2.95 
3 = Response entered LOGICALLY ASSIGNED ................................................... 1 0.00 
6 = Response not entered ..................................................................................... 2346 4.11 
94 = DON'T KNOW ............................................................................................... 17 0.03 
97 = REFUSED .................................................................................................... 134 0.23 
98 = BLANK (NO ANSWER) ................................................................................. 115 0.20 
99 = LEGITIMATE SKIP ....................................................................................... 52845 92.47 
 
 
RECODED ADULT MENTAL HEALTH SERVICE UTILIZATION 
Codebook Creation Date: 10/20/2016……….388 
NOTE: The following seven variables contain information about the location of outpatient mental health treatment/counseling received in the past year. These variables were revised for the 2009 NSDUH to include those respondents who reported receiving NO outpatient mental health treatment (AMHOUTP3=2) in the No category for the location. This differs from the variables named similarly in the past as they were only defined for those respondents who reported having received outpatient mental health treatment in the past year (AMHOUTP3=1) and those respondents who reported No outpatient mental health treatment were previously defined as system missing. 
Only respondents who reported having received outpatient mental health treatment/counseling (AMHOUTP3=1) can be defined as having received it at the location. A respondent was allowed to report any of five specific locations or "Some Other Place". If a respondent reported "Some Other Place," they were asked to provide a description of the other location in a follow-up question. The first five variables below were created by examination of the variables containing information on the five specific locations, while the last two variables were created by examination of the variables containing information on the other-specify locations which were grouped into two main categories. 
(AMHOUTP3, AUOPMENT) 
MHLMNT3 Len : 1 RC-RCVD OUTP MH TRT AT MH CLINIC/CENTER IN PST YR Freq Pct 
. = Unkwn MH Trt/Unkwn Source/Aged 12-17 (Otherwise) .................................... 13842 24.22 
0 = No (AMHOUTP3=2 or [AMHOUTP3=1 and AUOPMENT=6]) .......................... 42398 74.19 
1 = Yes (AMHOUTP3=1 and AUOPMENT=1,3) .................................................... 906 1.59 
(AMHOUTP3, AUOPTHER) 
MHLTHER3 Len : 1 RC-RCVD OUTP MH TRT AT PRIV THERAPIST OFC IN PST YR Freq Pct 
. = Unkwn MH Trt/Unkwn Source/Aged 12-17 (Otherwise) .................................... 13841 24.22 
0 = No (AMHOUTP3=2 or [AMHOUTP3=1 and AUOPTHER=6]) .......................... 41414 72.47 
1 = Yes (AMHOUTP3=1 and AUOPTHER=1,3) .................................................... 1891 3.31 
(AMHOUTP3, AUOPDOC) 
MHLDOC3 Len : 1 RC-RCVD OUTP MH TRT AT NON CLINIC DR OFFCE IN PST YR Freq Pct 
. = Unkwn MH Trt/Unkwn Source/Aged 12-17 (Otherwise) .................................... 13841 24.22 
0 = No (AMHOUTP3=2 or [AMHOUTP3=1 and AUOPDOC=6]) ............................ 42813 74.92 
1 = Yes (AMHOUTP3=1 and AUOPDOC=1,3) ...................................................... 492 0.86 
 
(AMHOUTP3, AUOPCLNC) 
MHLCLNC3 Len : 1 RC-RCVD OUTP MH TRT AT MEDICAL CLINIC IN PST YR Freq Pct 
. = Unkwn MH Trt/Unkwn Source/Aged 12-17 (Otherwise) .................................... 13841 24.22 
0 = No (AMHOUTP3=2 or [AMHOUTP3=1 and AUOPCLNC=6]) .......................... 43100 75.42 
1 = Yes (AMHOUTP3=1 and AUOPCLNC=1,3) .................................................... 205 0.36 
 
(AMHOUTP3, AUOPDTMT) 
MHLDTMT3 Len : 1 RC-RCVD OUTP MH TRT AT DAY HOSP OR TRT PGM IN PST YR Freq Pct 
. = Unkwn MH Trt/Unkwn Source/Aged 12-17 (Otherwise) .................................... 13841 24.22 
0 = No (AMHOUTP3=2 or [AMHOUTP3=1 and AUOPDTMT=6]) .......................... 43235 75.66 
1 = Yes (AMHOUTP3=1 and AUOPDTMT=1,3) .................................................... 70 0.12 
 
MENTAL HEALTH 
Codebook Creation Date: 10/20/2016……….417 
 
 
MENTAL HEALTH 
The values in this section may be inconsistent with values for variables in other sections of the interview. Items in this section were edited when respondents legitimately skipped out of these items based on prior answers in earlier sections. Otherwise, variables in one section of the interview generally were not edited to make them consistent with variables in another section of the interview. This note applies to variables in this section marked by a1. 
 
These questions ask how you have been feeling during the past 30 days. 
During the past 30 days, how often did you feel nervous? 
(NERVE30) 
DSTNRV301 Len : 2 HOW OFTEN FELT NERVOUS PAST 30 DAYS Freq Pct 
1 = All of the time .................................................................................................. 1141 2.00 
2 = Most of the time .............................................................................................. 2194 3.84 
3 = Some of the time ............................................................................................. 8669 15.17 
4 = A little of the time ............................................................................................ 15281 26.74 
5 = None of the time ............................................................................................. 15989 27.98 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 123 0.22 
97 = REFUSED .................................................................................................... 145 0.25 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
 
During the past 30 days, how often did you feel hopeless? 
(HOPE30) 
DSTHOP301 Len : 2 HOW OFTEN FELT HOPELESS PAST 30 DAYS Freq Pct 
1 = All of the time .................................................................................................. 801 1.40 
2 = Most of the time .............................................................................................. 1245 2.18 
3 = Some of the time ............................................................................................. 4276 7.48 
4 = A little of the time ............................................................................................ 8039 14.07 
5 = None of the time ............................................................................................. 28912 50.59 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 118 0.21 
97 = REFUSED .................................................................................................... 151 0.26 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
DSTNGD301 Len : 2 HOW OFT FELT DOWN/WTHLSS/NO GOOD PST 30 DYS Freq Pct 
1 = All of the time .................................................................................................. 848 1.48 
2 = Most of the time .............................................................................................. 1440 2.52 
3 = Some of the time ............................................................................................. 4031 7.05 
4 = A little of the time ............................................................................................ 8167 14.29 
5 = None of the time ............................................................................................. 28788 50.38 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 112 0.20 
97 = REFUSED .................................................................................................... 156 0.27 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
 
The last questions asked about how you have been feeling during the past 30 days. Now think about the past 12 months. Was there a month in the past 12 months when you felt more depressed, anxious, or emotionally stressed than you felt during the past 30 days? 
 
(WORST30) 
DSTWORST1 Len : 2 MON IN PST 12 MOS FELT WORSE THAN PST 30 DYS Freq Pct 
1 = Yes ................................................................................................................. 13657 23.90 
2 = No ................................................................................................................... 29583 51.77 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 145 0.25 
97 = REFUSED .................................................................................................... 157 0.27 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 MENTAL HEALTH 
Codebook Creation Date: 10/20/2016……….419 
 
Think of one month in the past 12 months when you were the most depressed, anxious, or emotionally stressed. 
During that month, how often did you feel nervous? 
(DSNERV1) 
DSTNRV121 Len : 2 HOW OFT FELT NERVOUS IN WORST MONTH, PST 12 MOS Freq Pct 
1 = All of the time .................................................................................................. 1698 2.97 
2 = Most of the time .............................................................................................. 3436 6.01 
3 = Some of the time ............................................................................................. 4598 8.05 
4 = A little of the time ............................................................................................ 3062 5.36 
5 = None of the time ............................................................................................. 828 1.45 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 27 0.05 
97 = REFUSED .................................................................................................... 165 0.29 
98 = BLANK (NO ANSWER) ................................................................................. 162 0.28 
99 = LEGITIMATE SKIP ....................................................................................... 43168 75.54 
During that same month when you were at your worst emotionally... 
how often did you feel hopeless? 
(DSHOPE) 
DSTHOP121 Len : 2 HOW OFTEN FELT HOPELESS IN WORST MONTH Freq Pct 
1 = All of the time .................................................................................................. 1446 2.53 
2 = Most of the time .............................................................................................. 2441 4.27 
3 = Some of the time ............................................................................................. 3364 5.89 
4 = A little of the time ............................................................................................ 3125 5.47 
5 = None of the time ............................................................................................. 3261 5.71 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 12 0.02 
97 = REFUSED .................................................................................................... 165 0.29 
98 = BLANK (NO ANSWER) ................................................................................. 162 0.28 
99 = LEGITIMATE SKIP ....................................................................................... 43168 75.54 
 
 
During that same month when you were at your worst emotionally... 
how often did you feel so sad or depressed that nothing could cheer you up? 
(DSNOCHR) 
DSTCHR121 Len : 2 HOW OFTEN COULDN'T BE CHEERED UP IN WORST MONTH Freq Pct 
1 = All of the time .................................................................................................. 1470 2.57 
2 = Most of the time .............................................................................................. 2370 4.15 
3 = Some of the time ............................................................................................. 3224 5.64 
4 = A little of the time ............................................................................................ 3212 5.62 
5 = None of the time ............................................................................................. 3352 5.87 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 19 0.03 
97 = REFUSED .................................................................................................... 167 0.29 
98 = BLANK (NO ANSWER) ................................................................................. 162 0.28 
99 = LEGITIMATE SKIP ....................................................................................... 43168 75.54 
 
During that same month when you were at your worst emotionally... 
how often did you feel that everything was an effort? 
(DSEFFORT) 
DSTEFF121 Len : 2 HOW OFT FELT EVERYTHING AN EFFORT IN WORST MON Freq Pct 
1 = All of the time .................................................................................................. 1867 3.27 
2 = Most of the time .............................................................................................. 2697 4.72 
3 = Some of the time ............................................................................................. 3522 6.16 
4 = A little of the time ............................................................................................ 3272 5.73 
5 = None of the time ............................................................................................. 2233 3.91 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 53 0.09 
97 = REFUSED .................................................................................................... 170 0.30 
98 = BLANK (NO ANSWER) ................................................................................. 162 0.28 
99 = LEGITIMATE SKIP ....................................................................................... 43168 75.54 
 
During that same month when you were at your worst emotionally... 
how often did you feel down on yourself, no good, or worthless? 
(DSDOWN) 
DSTNGD121 Len : 2 HOW OFTEN FELT NO GOOD IN WORST MONTH Freq Pct 
1 = All of the time .................................................................................................. 1495 2.62 
2 = Most of the time .............................................................................................. 2150 3.76 
3 = Some of the time ............................................................................................. 2913 5.10 
4 = A little of the time ............................................................................................ 2983 5.22 
5 = None of the time ............................................................................................. 4081 7.14 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 21 0.04 
97 = REFUSED .................................................................................................... 171 0.30 
98 = BLANK (NO ANSWER) ................................................................................. 162 0.28 
99 = LEGITIMATE SKIP ....................................................................................... 43168 75.54 
 
During that one month when your emotions, nerves or mental health interfered most with your daily activities... 
how much difficulty did you have remembering to do things you needed to do? 
(LIREMEM) 
During that one month when your emotions, nerves or mental health interfered most with your daily activities... 
how much difficulty did you have concentrating on doing something important when other things were going on around you? 
(LICONCEN) 
IMPCONCN1 Len : 2 DIFFICULTY CONCENTRATING ONE MO IN PST 12 MOS Freq Pct 
1 = No difficulty ..................................................................................................... 15692 27.46 
2 = Mild difficulty ................................................................................................... 11554 20.22 
3 = Moderate difficulty ........................................................................................... 4984 8.72 
4 = Severe difficulty .............................................................................................. 1531 2.68 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 120 0.21 
97 = REFUSED .................................................................................................... 87 0.15 
99 = LEGITIMATE SKIP ....................................................................................... 23176 40.56 
 
During that one month when your emotions, nerves or mental health interfered most with your daily activities... 
how much difficulty did you have going out of the house and getting around on your own? 
(LIGOOUT1) 
IMPGOUT1 Len : 2 DIFFICULTY GOING OUT ONE MO IN PST 12 MO Freq Pct 
1 = No difficulty ..................................................................................................... 22964 40.18 
2 = Mild difficulty ................................................................................................... 5621 9.84 
3 = Moderate difficulty ........................................................................................... 3136 5.49 
4 = Severe difficulty .............................................................................................. 1299 2.27 
5 = You didn't leave the house on your own .......................................................... 746 1.31 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 106 0.19 
97 = REFUSED .................................................................................................... 96 0.17 
99 = LEGITIMATE SKIP ....................................................................................... 23176 40.56 
 
Did problems with your emotions, nerves, or mental health keep you from leaving the house on your own? 
(LIGOOUT2) 
IMPGOUTM1 Len : 2 EMOTIONAL PROBLEMS KEEP YOU FROM LEAVING HOUSE Freq Pct 
1 = Yes ................................................................................................................. 425 0.74 
2 = No ................................................................................................................... 319 0.56 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 97 0.17 
98 = BLANK (NO ANSWER) ................................................................................. 108 0.19 
99 = LEGITIMATE SKIP ....................................................................................... 56196 98.34 
 
 
During that one month when your emotions, nerves or mental health interfered most with your daily activities... 
how much difficulty did you have dealing with people you did not know well? 
(LISTRAN1) 
IMPPEOP1 Len : 2 DIFFICULTY DEALING W STRANGERS ONE MO IN PST 12 M Freq Pct 
1 = No difficulty ..................................................................................................... 20298 35.52 
2 = Mild difficulty ................................................................................................... 7170 12.55 
3 = Moderate difficulty ........................................................................................... 3655 6.40 
4 = Severe difficulty .............................................................................................. 1545 2.70 
5 = You didn't deal with people you did not know well ........................................... 1093 1.91 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 110 0.19 
97 = REFUSED .................................................................................................... 97 0.17 
99 = LEGITIMATE SKIP ....................................................................................... 23176 40.56 MENTAL HEALTH 
Codebook Creation Date: 10/20/2016……….422 
 
Did problems with your emotions, nerves, or mental health keep you from dealing with people you did not know well? 
(LISTRAN2) 
IMPPEOPM1 Len : 2 EMOTIONAL PROBLEMS KEEP YOU FROM DEALING W STRAGR Freq Pct 
1 = Yes ................................................................................................................. 533 0.93 
2 = No ................................................................................................................... 549 0.96 
94 = DON'T KNOW ............................................................................................... 9 0.02 
97 = REFUSED .................................................................................................... 99 0.17 
98 = BLANK (NO ANSWER) ................................................................................. 112 0.20 
99 = LEGITIMATE SKIP ....................................................................................... 55844 97.72 
 
Did problems with your emotions, nerves, or mental health keep you from participating in social activities? 
(LISOC2) 
IMPSOCM1 Len : 2 EMOTIONAL PROBS KEEP YOU FROM PART IN SOCIAL Freq Pct 
1 = Yes ................................................................................................................. 851 1.49 
2 = No ................................................................................................................... 624 1.09 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 102 0.18 
98 = BLANK (NO ANSWER) ................................................................................. 92 0.16 
99 = LEGITIMATE SKIP ....................................................................................... 55476 97.08 
 
Did problems with your emotions, nerves, or mental health keep you from taking care of household responsibilities? 
(LIHHRES2) 
IMPHHLDM1 Len : 2 EMOTIONL PROBS MAKE KEEP YOU FRM TAKING CARE HOUS Freq Pct 
1 = Yes ................................................................................................................. 294 0.51 
2 = No ................................................................................................................... 149 0.26 
94 = DON'T KNOW ............................................................................................... 2 0.00 
97 = REFUSED .................................................................................................... 94 0.16 
98 = BLANK (NO ANSWER) ................................................................................. 88 0.15 
99 = LEGITIMATE SKIP ....................................................................................... 56519 98.90 MENTAL HEALTH 
Codebook Creation Date: 10/20/2016……….423 
 
Did problems with your emotions, nerves, or mental health keep you from working or going to school? 
(LIWKRES2) 
IMPRESPM1 Len : 2 DID EMOTIONAL PROBS KEEP YOU FROM WORK/SCHOOL Freq Pct 
1 = Yes ................................................................................................................. 375 0.66 
2 = No ................................................................................................................... 1091 1.91 
94 = DON'T KNOW ............................................................................................... 8 0.01 
97 = REFUSED .................................................................................................... 116 0.20 
98 = BLANK (NO ANSWER) ................................................................................. 107 0.19 
99 = LEGITIMATE SKIP ....................................................................................... 55449 97.03 
 
You mentioned having difficulty with or being unable to do such things as [FILL]. During the past 12 months, about how many weeks did you have any of these difficulties because of your emotions, nerves, or mental health? If you can't remember the exact number, just give your best estimate. 
 
(IMWEEK1) 
IMPWEEKS1 Len : 2 NUM WEEKS HAVE DIFFICULTIES BECAUSE OF MENTL HLTH Freq Pct 
RANGE = 1 - 52 .................................................................................................... 22797 39.89 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 770 1.35 
97 = REFUSED .................................................................................................... 235 0.41 
98 = BLANK (NO ANSWER) ................................................................................. 163 0.29 
99 = LEGITIMATE SKIP ....................................................................................... 33180 58.06 MENTAL HEALTH 
Codebook Creation Date: 10/20/2016……….424 
 
During that/those [IMWEEK1FILL] week/weeks did you have these kinds of difficulties every day, most days, or only one or two days a week? 
(IMDAYS) 
IMPDYFRQ1 Len : 2 HOW MANY DAYS IN WEEK DID YOU HAVE DIFFICULTIES Freq Pct 
1 = Every day ....................................................................................................... 1369 2.40 
2 = Most days ....................................................................................................... 6778 11.86 
3 = Only one or two days a week .......................................................................... 14606 25.56 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 34 0.06 
97 = REFUSED .................................................................................................... 245 0.43 
98 = BLANK (NO ANSWER) ................................................................................. 933 1.63 
99 = LEGITIMATE SKIP ....................................................................................... 33180 58.06 
 
About how many days out of 365 in the past 12 months were you totally unable to work or carry out your normal activities because of your emotions, nerves or mental health? 
You can use any number between 0 and 365 to answer. 
(LIAD68) 
IMPYDAYS1 Len : 3 HOW MANY DAY IN PAST YR YOU WERE UNABLE TO WORK Freq Pct 
RANGE = 0 - 365 .................................................................................................. 23291 40.76 
985 = BAD DATA Logically assigned .................................................................... 1 0.00 
994 = DON'T KNOW ............................................................................................. 352 0.62 
997 = REFUSED .................................................................................................. 159 0.28 
998 = BLANK (NO ANSWER) ............................................................................... 163 0.29 
999 = LEGITIMATE SKIP ..................................................................................... 33180 58.06 
 
The next few questions are about thoughts of suicide. At any time in the past 12 months, that is from [DATEFILL] up to and including today, did you seriously think about trying to kill yourself? 
(SUI01) 
SUICTHNK1 Len : 2 SERIOUSLY THINK ABOUT KILLING SELF PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 2399 4.20 
2 = No ................................................................................................................... 40916 71.60 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 55 0.10 
97 = REFUSED .................................................................................................... 172 0.30 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
 
During the past 12 months, did you make any plans to kill yourself? 
(SUI02) 
SUICPLAN1 Len : 2 MAKE PLANS TO KILL YOURSELF PST 12 MOS Freq Pct 
1 = Yes ................................................................................................................. 744 1.30 
2 = No ................................................................................................................... 1650 2.89 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
94 = DON'T KNOW ............................................................................................... 1 0.00 
97 = REFUSED .................................................................................................... 176 0.31 
98 = BLANK (NO ANSWER) ................................................................................. 72 0.13 
99 = LEGITIMATE SKIP ....................................................................................... 54501 95.37 
During the past 12 months, did you try to kill yourself? 
(SUI03) 
SUICTRY1 Len : 2 TRY TO KILL YOURSELF PAST 12 MONTHS Freq Pct 
1 = Yes ................................................................................................................. 389 0.68 
2 = No ................................................................................................................... 2009 3.52 
85 = BAD DATA Logically assigned ...................................................................... 2 0.00 
97 = REFUSED .................................................................................................... 173 0.30 
98 = BLANK (NO ANSWER) ................................................................................. 72 0.13 
99 = LEGITIMATE SKIP ....................................................................................... 54501 95.37 
 
 
ADULT DEPRESSION 
The values in this section may be inconsistent with values for variables in other sections of the interview. Items in this section were edited when respondents legitimately skipped out of these items based on prior answers in earlier sections. Otherwise, variables in one section of the interview generally were not edited to make them consistent with variables in another section of the interview. This note applies to variables in this section marked by a1. 
 
NOTE: All of the respondents aged 18 or older were asked the questions in the Adult Depression module in this current survey year. In the 2004 survey, a subset of the adults was asked these questions. 
 
Have you ever in your life had a period of time lasting several days or longer when most of the day you felt sad, empty or depressed? 
(ASC21) 
ADDPREV1 Len : 2 SEVERAL DAYS OR LNGR WHEN FELT SAD/EMPTY/DPRSD Freq Pct 
1 = Yes ................................................................................................................. 13437 23.51 
2 = No ................................................................................................................... 29862 52.26 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 78 0.14 
97 = REFUSED .................................................................................................... 166 0.29 
98 = BLANK (NO ANSWER) ................................................................................. 17 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 13585 23.77 
 
Have you ever had a period of time lasting several days or longer when most of the day you were very discouraged about how things were going in your life? 
(ASC22) 
ADDSCEV1 Len : 2 SEVERAL DAYS OR LNGR FELT DISCOURAGED ABT LIFE Freq Pct 
1 = Yes ................................................................................................................. 3425 5.99 
2 = No ................................................................................................................... 26434 46.26 
94 = DON'T KNOW ............................................................................................... 74 0.13 
97 = REFUSED .................................................................................................... 173 0.30 
98 = BLANK (NO ANSWER) ................................................................................. 18 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 27022 47.29 
 
Have you ever had a period of time lasting several days or longer when you lost interest in most things you usually enjoy like work, hobbies, and personal relationships? 
(ASC23) 
ADLOSEV1 Len : 2 EVER HAD PER OF TIME LST INTRST IN ENJOYABLE THGS Freq Pct 
1 = Yes ................................................................................................................. 1216 2.13 
2 = No ................................................................................................................... 25234 44.16 
94 = DON'T KNOW ............................................................................................... 70 0.12 
97 = REFUSED .................................................................................................... 161 0.28 
98 = BLANK (NO ANSWER) ................................................................................. 18 0.03 
99 = LEGITIMATE SKIP ....................................................................................... 30447 53.28 
 
During times when you felt sad, empty, or depressed most of the day, did you ever feel discouraged about how things were going in your life? 
(AD01) 
ADDPDISC1 Len : 2 FEEL DISCRGD ABOUT LIFE WHEN SAD/EMPTY/DEPRESSED Freq Pct 
1 = Yes ................................................................................................................. 12195 21.34 
2 = No ................................................................................................................... 1230 2.15 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 8 0.01 
97 = REFUSED .................................................................................................... 4 0.01 
98 = BLANK (NO ANSWER) ................................................................................. 211 0.37 
99 = LEGITIMATE SKIP ....................................................................................... 43497 76.12 ADULT DEPRESSION 
Codebook Creation Date: 10/20/2016……….432 
 
During the times when you felt sad, empty, or depressed, did you ever lose interest in most things like work, hobbies, and other things you usually enjoy? 
(AD01A, AD01B) 
ADDPLSIN1 Len : 2 EVER LOSE INT IN THINGS WHEN SAD/EMPTY/DEPRESSED Freq Pct 
1 = Yes ................................................................................................................. 10658 18.65 
2 = No ................................................................................................................... 2760 4.83 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 14 0.02 
97 = REFUSED .................................................................................................... 5 0.01 
98 = BLANK (NO ANSWER) ................................................................................. 211 0.37 
99 = LEGITIMATE SKIP ....................................................................................... 43497 76.12 
 
Think about the times when you [FEELFILL]. Did you ever have a period of time like this that lasted most of the day, nearly every day, for two weeks or longer? 
(AD12) 
ADDPR2WK1 Len : 2 TIME WHEN [FEELFILL] LSTD EVRYDY 2 WKS OR LNGR Freq Pct 
1 = Yes ................................................................................................................. 10281 17.99 
2 = No ................................................................................................................... 6528 11.42 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 36 0.06 
97 = REFUSED .................................................................................................... 17 0.03 
98 = BLANK (NO ANSWER) ................................................................................. 226 0.40 
99 = LEGITIMATE SKIP ....................................................................................... 40057 70.10 
 
Think of times lasting two weeks or longer when [NUMPROBS] with your mood [WASWERE] most severe and frequent. During those times, how long did your [FEELNOUN] usually last? 
(AD16) 
ADWRHRS1 Len : 2 TIME THAT MOST SEVERE/FREQUENT MOOD LASTED Freq Pct 
1 = Less than 1 hour ............................................................................................. 791 1.38 
2 = At least 1 hour but no more than 3 hours ........................................................ 2373 4.15 
3 = At least 3 hours but no more than 5 hours....................................................... 2623 4.59 
4 = 5 hours or more .............................................................................................. 4578 8.01 
85 = BAD DATA Logically assigned ...................................................................... 1 0.00 
94 = DON'T KNOW ............................................................................................... 87 0.15 
97 = REFUSED .................................................................................................... 20 0.03 
98 = BLANK (NO ANSWER) ................................................................................. 308 0.54 
99 = LEGITIMATE SKIP ....................................................................................... 46365 81.13
 
Still thinking of times lasting two weeks or longer when [NUMPROBS] with your mood [WASWERE] most severe and frequent, how severe was your emotional distress during those times? 
(AD17) 
ADWRDST1 Len : 2 HOW SEVERE WAS EMOTIONAL DISTRESS DURING 2 WKS Freq Pct 
1 = Mild ................................................................................................................. 1080 1.89 
2 = Moderate ........................................................................................................ 3933 6.88 
3 = Severe ............................................................................................................ 3270 5.72 
4 = Very Severe .................................................................................................... 1350 2.36 
94 = DON'T KNOW ............................................................................................... 30 0.05 
97 = REFUSED .................................................................................................... 18 0.03 
98 = BLANK (NO ANSWER) ................................................................................. 309 0.54 
99 = LEGITIMATE SKIP ....................................................................................... 47156 82.52 
 
 
Did you ever have any of these problems during a period of time when you [FEELFILL] for two weeks or longer? 
(AD21) 
ADDPPROB1 Len : 2 EVER HAVE OTH PRBLMS DURING 2 WKS OR LONGER Freq Pct 
1 = Yes ................................................................................................................. 7771 13.60 
2 = No ................................................................................................................... 1664 2.91 
94 = DON'T KNOW ............................................................................................... 12 0.02 
97 = REFUSED .................................................................................................... 15 0.03 
98 = BLANK (NO ANSWER) ................................................................................. 309 0.54 
99 = LEGITIMATE SKIP ....................................................................................... 47375 82.90
 
Is there one particular time like this that stands out in your mind as the worst one you ever had? 
(AD22) 
ADWRPROB1 Len : 2 ONE PARTICULAR TIME THAT IS THE WORST ONE EVER Freq Pct 
1 = Yes ................................................................................................................. 5388 9.43 
2 = No ................................................................................................................... 2347 4.11 
94 = DON'T KNOW ............................................................................................... 24 0.04 
97 = REFUSED .................................................................................................... 12 0.02 
98 = BLANK (NO ANSWER) ................................................................................. 336 0.59 
99 = LEGITIMATE SKIP ....................................................................................... 49039 85.81 
How old were you when that worst period of time started? 
 
Then think of the most recent time when you [FEELFILL] for two weeks or longer and you also had the largest number of these other problems at the same time. 
 
During that [TIMEFILL] period of time, did you feel discouraged about how things were going in your life most of the day nearly every day? 
(AD24C) 
ADWRDISC1 Len : 2 WHEN PRBLMS WORST FELT DISCRGED ABT LIFE EVERYDAY Freq Pct 
1 = Yes ................................................................................................................. 6269 10.97 
2 = No ................................................................................................................... 1472 2.58 
94 = DON'T KNOW ............................................................................................... 16 0.03 
97 = REFUSED .................................................................................................... 14 0.02 
98 = BLANK (NO ANSWER) ................................................................................. 336 0.59 
99 = LEGITIMATE SKIP ....................................................................................... 49039 85.81 ADULT DEPRESSION 
Codebook Creation Date: 10/20/2016……….435 
 
During that [TIMEFILL] period of time, did you lose interest in almost all things like work and hobbies and things you like to do for fun? 
(AD24E) 
ADWRLSIN1 Len : 2 WHEN PRBLMS WORST LOSE INTRST IN ENJOYABLE THINGS Freq Pct 
1 = Yes ................................................................................................................. 5980 10.46 
2 = No ................................................................................................................... 1769 3.10 
94 = DON'T KNOW ............................................................................................... 10 0.02 
97 = REFUSED .................................................................................................... 12 0.02 
98 = BLANK (NO ANSWER) ................................................................................. 336 0.59 
99 = LEGITIMATE SKIP ....................................................................................... 49039 85.81 
 
During that [TIMEFILL] period of time, did you lose the ability to take pleasure in having good things happen to you, like winning something or being praised or complimented? 
(AD24F) 
ADWRPLSR1 Len : 2 WHEN PRBLMS WORST LOSE PLSURE IN GOOD THINGS Freq Pct 
1 = Yes ................................................................................................................. 5142 9.00 
2 = No ................................................................................................................... 2594 4.54 
94 = DON'T KNOW ............................................................................................... 20 0.03 
97 = REFUSED .................................................................................................... 15 0.03 
98 = BLANK (NO ANSWER) ................................................................................. 336 0.59 
99 = LEGITIMATE SKIP ....................................................................................... 49039 85.81 
 
 
p.489
(ADDPPROB, ADDPR2WK, ADDPREV, ADDSCEV, ADLOSEV, ADLSI2WK, ADSMMDEA, ADWRCHR, ADWRDST, ADWRHRS, ADWRIMP) 
AMDELT Len : 1 RC-ADULT: LIFETIME MAJOR DEPRESSIVE EPISODE (MDE) Freq Pct 
. = Aged 12-17/Unknown (Otherwise) ................................................................... 14001 24.50 
1 = Yes (ADSMMDEA=1) ..................................................................................... 6541 11.45 
2 = No (See comment above) ............................................................................... 36604 64.05 
 
(ADPB2WK, AMDELT) 
AMDEYR Len : 1 RC-ADULT: PAST YEAR MAJOR DEPRESSIVE EPISODE (MDE) Freq Pct 
. = Aged 12-17/Unknown (Otherwise) ................................................................... 14064 24.61 
1 = Yes (AMDELT=1 & ADPB2WK=1) .................................................................. 3571 6.25 
2 = No (AMDELT=2 or [AMDELT=1 & ADPB2WK=2]) .......................................... 39511 69.14 
 
 
INTERVIEW INFORMATION 
LANGVER Len : 2 LANGUAGE VERSION Freq Pct 
1 = English ............................................................................................................ 54715 95.75 
2 = Spanish .......................................................................................................... 2431 4.25 
 
NOTE: After a respondent has entered his/her birthdate in the first part of the questionnaire, he/she has multiple opportunities to change his/her age in response to consistency checks throughout the questionnaire. It is therefore possible for the age recorded by the respondent at the beginning of the questionnaire to be different than the age at the end of the questionnaire. The final age variable is determined using these two constituent age variables, in addition to the age calculated from the raw birthdate and the final edited interview date, the age entered in the questionnaire roster (if it exists), and the pre-interview screener age. 
AGE2 Len : 2 RECODE - FINAL EDITED AGE Freq Pct 
1 = Respondent is 12 years old ............................................................................. 2070 3.62 
2 = Respondent is 13 years old ............................................................................. 2222 3.89 
3 = Respondent is 14 years old ............................................................................. 2347 4.11 
4 = Respondent is 15 years old ............................................................................. 2368 4.14 
5 = Respondent is 16 years old ............................................................................. 2318 4.06 
6 = Respondent is 17 years old ............................................................................. 2260 3.95 
7 = Respondent is 18 years old ............................................................................. 1860 3.25 
8 = Respondent is 19 years old ............................................................................. 1714 3.00 
9 = Respondent is 20 years old ............................................................................. 1732 3.03 
10 = Respondent is 21 years old ........................................................................... 1734 3.03 
11 = Respondent is 22 or 23 years old .................................................................. 3605 6.31 
12 = Respondent is 24 or 25 years old .................................................................. 3908 6.84 
13 = Respondent is between 26 and 29 years old ................................................. 4081 7.14 
14 = Respondent is between 30 and 34 years old ................................................. 5003 8.75 
15 = Respondent is between 35 and 49 years old ................................................. 11169 19.54 
16 = Respondent is between 50 and 64 years old ................................................. 5157 9.02 
17 = Respondent is 65 years old or older .............................................................. 3598 6.30 
 
 
 
 
This question is about your overall health. Would you say your health in general is excellent, very good, good, fair, or poor? 
(QD12) 
HEALTH Len : 2 OVERALL HEALTH Freq Pct 
1 = Excellent ......................................................................................................... 14752 25.81 
2 = Very good ....................................................................................................... 21887 38.30 
3 = Good............................................................................................................... 14999 26.25 
4 = Fair ................................................................................................................. 4622 8.09 
5 = Poor ................................................................................................................ 880 1.54 
94 = DON'T KNOW ............................................................................................... 4 0.01 
97 = REFUSED .................................................................................................... 2 0.00 
 
(HEALTH) 
HEALTH2 Len : 1 RC-OVERALL HEALTH RECODE Freq Pct 
. = Unknown (Otherwise) ...................................................................................... 6 0.01 
1 = Excellent (HEALTH=1) .................................................................................... 14752 25.81 
2 = Very Good (HEALTH=2) ................................................................................. 21887 38.30 
3 = Good (HEALTH=3) ......................................................................................... 14999 26.25 
4 = Fair/Poor (HEALTH=4,5) ................................................................................. 5502 9.63 
 
 
 
p.
 
1.11. PRESCRIPTION PAIN RELIEVERS 
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
 
1.7. HEROIN 
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

(TRQNMREC) 
IRTRQNMREC Len : 1 TRANQUILIZER MISUSE RECENCY - IMPUTATION REVISED Freq Pct 
1 = Within the past 30 days ................................................................................... 525 0.92 
2 = More than 30 days ago but within the past 12 mos ......................................... 1070 1.87 
3 = More than 12 months ago ............................................................................... 994 1.74 
9 = NEVER MISUSED TRANQUILIZERS ............................................................. 54557 95.47 RECENCY OF DRUG USE 
Codebook Creation Date: 10/20/2016……….110 
 
(TRQNMREC) 
IITRQNMREC Len : 1 TRANQUILIZER MISUSE RECENCY - IMPUTATION INDICATOR Freq Pct 
1 = Questionnaire data ......................................................................................... 56690 99.20 
3 = Statistically imputed data - any use rec imputed .............................................. 194 0.34 
4 = Stat imp data - any use rec known, misuse unknown ...................................... 13 0.02 
5 = Statistically imputed data - edited recency = 9 ................................................ 2 0.00 
6 = Statistically imputed data - edited recency = 8 ................................................ 2 0.00 
7 = Stat imp data - did not misuse py, life unknown............................................... 245 0.43 
(STMNMREC) 
(SEDNMREC) 
IRSEDNMREC Len : 1 SEDATIVE MISUSE RECENCY - IMPUTATION REVISED Freq Pct 
1 = Within the past 30 days ................................................................................... 109 0.19 
2 = More than 30 days ago but within the past 12 mos ......................................... 229 0.40 
3 = More than 12 months ago ............................................................................... 800 1.40 
9 = NEVER MISUSED SEDATIVES ..................................................................... 56008 98.01 
 
(SEDNMREC) 
IISEDNMREC Len : 1 SEDATIVE MISUSE RECENCY - IMPUTATION INDICATOR Freq Pct 
1 = Questionnaire data ......................................................................................... 56736 99.28 
3 = Statistically imputed data - any use rec imputed .............................................. 207 0.36 
4 = Stat imp data - any use rec known, misuse unknown ...................................... 9 0.02 
5 = Statistically imputed data - edited recency = 9 ................................................ 5 0.01 
6 = Statistically imputed data - edited recency = 8 ................................................ 1 0.00 
7 = Stat imp data - did not misuse py, life unknown............................................... 188 0.33 

