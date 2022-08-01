import QuantLib as ql
import pandas as pd
from datetime import date
from dictionaries.ql_dictionary import *
import time

start = time.perf_counter()

df = pd.read_csv("data\ICE_DF.csv")

df = df.drop(axis=1, index=0)

#Filters DF by mapped codes
df = df[df["Country Code"].isin(country_ql.keys()) & df["Interest Basis"].isin(day_count_ql.keys()) & df["Interest Payment Frequency"].isin(tenor_ql.keys()) & df["Business Day Convention Code"].isin(business_convention_ql)]
df["Accrual Date"] = pd.to_datetime(df["Accrual Date"])
df["Maturity Date"] = pd.to_datetime(df["Maturity Date"])
todays_date = pd.to_datetime(date.today())




for index, row in df.iterrows():
        # Analysis Variables

    ## General Settings for Analysis and QuantLab

    qL_calendar 		=  country_ql[row["Country Code"]]()



    qL_dayCount 		=  day_count_ql[row["Interest Basis"]]()
    qL_analysisDate     = ql.Date(todays_date.day, todays_date.month, todays_date.year)
    qL_settlementDays 	= 0
    currentParPrice 	= float(row["Nominal Value"])
    qL_interpolation 			= ql.Linear()
    qL_compounding 				= ql.Compounded
    ql_paymentFrequency 	=  payment_frequency_ql[row["Interest Payment Frequency"]]
    qL_spotRates = qL_coupons
    qL_spotDates = qL_schedule



    ## Reference Data
    try:

        try:
            bondName          	= row["ISIN"]
            qL_issuanceDate	  	= ql.Date(row["Accrual Date"].day, row["Accrual Date"].month, row["Accrual Date"].year) #dd/mm/YY
            qL_maturityDate   	= ql.Date(row["Maturity Date"].day, row["Maturity Date"].month, row["Maturity Date"].year) #dd/mm/YY
        except:
            print("Date Failure")
        try:
            qL_tenor			= ql.Period(tenor_ql[row["Interest Payment Frequency"]]) #actually means coupon frequency ie 6M
        except:
            print("Tenor Failure")
        try:
            qL_couponRate 	  	= float(row["Original Coupon Rate"])/100
        except:
            print("Coupon Rate Failure")
        try:
            qL_coupons			= [qL_couponRate]
        except:
            print("Coupons Failure")
        try:
            qL_faceValue		= float(row["Nominal Value"])
        except:
            print("Face Value Failure")
    except:
        print("First Stage Failure\n")
        
    
        

    # DEFINING BOND CHARACTERISTICS FOR ANALYSIS -- QuantLib
    try:
        ## PAYMENT SCHEDULE CALCULATION
        ### Some settings I'm not sure what they mean
        qL_businessConvention 	= business_convention_ql[row["Business Day Convention Code"]]
        ql_terminationDateConvention = business_convention_ql[row["Business Day Convention Code"]]
        qL_dateGeneration 		=  ql.DateGeneration.Backward
        qL_monthEnd 			= True
    except:
        print("Second Stage Failure\n")

    try:
    ### Creating Payment Schedule
        qL_schedule = ql.Schedule(qL_issuanceDate, \
                                    qL_maturityDate, \
                                    qL_tenor, \
                                    qL_calendar, \
                                    qL_businessConvention, \
                                    ql_terminationDateConvention, \
                                    qL_dateGeneration, \
                                    qL_monthEnd)
        

        # print(f"Schedule: {qL_schedule}\n")
    except:
        print("Schedule Failure\n")
    try:
        ### !! Creating a bond object for analysies
        qL_fixRateBond	= ql.FixedRateBond(qL_settlementDays, \
                                        qL_faceValue, \
                                        qL_schedule, \
                                        qL_coupons, \
                                        qL_dayCount)
    

        
        # print(f"Fix Rate Bond: {qL_fixRateBond}\n")
    except:
        print("Failed to Create Fixed Rate Bond Object\n")



    # CALCULATIONS
    try:

    ## Zero Yield Curve
    ### Some settings I don't understand
        ql.Settings.instance().evaluationDate = qL_analysisDate

        ### Attributes for zeroSpotCurve calculation

        curve = ql.ZeroCurve([ql.Date(31, 7, 2022), ql.Date(1, 1, 2027)], [0.01, 0.02], ql.Actual360(), qL_calendar, ql.Linear(), qL_compounding, ql_paymentFrequency)
        handle = ql.YieldTermStructureHandle(curve)
        bondEngine = ql.DiscountingBondEngine(handle)

        qL_interestRate = ql.InterestRate(qL_couponRate, qL_dayCount, qL_compounding, ql_paymentFrequency)
        print(qL_interestRate)
        
        print(qL_fixRateBond.NPV())
        yield_rate = qL_fixRateBond.bondYield(qL_fixRateBond.NPV(), qL_dayCount, qL_compounding, ql_paymentFrequency, qL_maturityDate)
        print('YTM:', yield_rate)

    except:
        print("Calculations Failed\n")
        pass



