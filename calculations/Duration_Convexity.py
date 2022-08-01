import math
import datetime
import QuantLib as ql
import pandas as pd
from datetime import date


df = pd.read_csv("ICE_DF.csv")

print(df.head())

day_count_ql = {"Actual/360": ql.Actual360, "Actual/364" : ql.Actual364, "Actual365Fixed" : ql.Actual365Fixed,
                "Actual/Actual" : ql.ActualActual, "Bus/252" : ql.Business252, "30/360" : ql.Thirty360, "30/360 (ICMA)" : ql.Thirty360,
                "30/365" : ql.Thirty365 }

country_ql = {"BR" : ql.Brazil, "CA" : ql.Canada, "CZ" : ql.CzechRepublic, "FR" : ql.France, "DE": ql.Germany,
            "HK" : ql.HongKong, "IS" : ql.Iceland, "IN" : ql.India, "ID" : ql.Indonesia, "IL" : ql.Israel,
            "IT" : ql.Italy, "MX" : ql.Mexico, "RU" : ql.Russia, "SA" : ql.SaudiArabia, "SG" : ql.Singapore,
            "SK" : ql.Slovakia, "KR" : ql.SouthKorea, "TW" : ql.Taiwan, "UA" : ql.Ukraine, "GB" : ql.UnitedKingdom,
            "US" : ql.UnitedStates}

tenor_ql = {"Semi Annual" : ql.Semiannual, "Annually" : ql.Annual, "Weekly" : ql.Weekly, "Quarterly" : ql.Quarterly}

payment_frequency_ql = {"Semi Annual" : 2, "Annually" : 1, "Weekly" : 52, "Quarterly" : 4}

country_keys = []

for i in country_ql.keys():
    country_keys.append(i)

df = df[df["Country Code"].isin(country_ql.keys()) & df["Interest Basis"].isin(day_count_ql.keys()) & df["Interest Payment Frequency"].isin(tenor_ql.keys())]
df["Accrual Date"] = pd.to_datetime(df["Accrual Date"])
df["Maturity Date"] = pd.to_datetime(df["Maturity Date"])
todays_date = pd.to_datetime(date.today())
print

# if __name__ == "__main__":
    
for index, row in df[3:4].iterrows():
	print(row)
		# Analysis Variables

	## General Settings for Analysis and QuantLab
	
	qL_calendar 		=  country_ql[row["Country Code"]]()


	
	qL_dayCount 		=  day_count_ql[row["Interest Basis"]]()
	
	
	## Analysis Variables
	qL_analysisDate     = ql.Date(todays_date.day, todays_date.month, todays_date.year)
	qL_settlementDays 	= 0

	## Market Detail
	currentParPrice 	= float(row["Nominal Value"])


# Bond Definitions #

	
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
		qL_businessConvention 	= ql.Unadjusted
		ql_terminationDateConvention = ql.Unadjusted
		qL_dateGeneration 		=  ql.DateGeneration.Backward
		qL_monthEnd 			= False
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
		
	
		print(f"Schedule: {qL_schedule}\n")
	except:
		print("Schedule Failure\n")
	try:
		### !! Creating a bond object for analysies
		qL_fixRateBond	= ql.FixedRateBond(qL_settlementDays, \
										qL_faceValue, \
										qL_schedule, \
										qL_coupons, \
										qL_dayCount)

		
		print(f"Fix Rate Bond: {qL_fixRateBond}\n")
	except:
		print("Failed to Create Fixed Rate Bond Object\n")



# CALCULATIONS
	try:

	## Zero Yield Curve
	### Some settings I don't understand
		ql.Settings.instance().evaluationDate = qL_analysisDate

		### Attributes for zeroSpotCurve calculation
		qL_interpolation 			= ql.Linear()
		qL_compounding 				= ql.Compounded
		ql_paymentFrequency 	=  payment_frequency_ql[row["Interest Payment Frequency"]]

		qL_spotRates = qL_coupons
		qL_spotDates = qL_schedule

		qL_interestRate = ql.InterestRate(qL_couponRate, qL_dayCount, qL_compounding, ql_paymentFrequency)
		print(qL_interestRate)



		### Calculations
		durationSimple	= ql.BondFunctions.duration(qL_fixRateBond, qL_interestRate, ql.Duration.Simple)
		durationModified= ql.BondFunctions.duration(qL_fixRateBond, qL_interestRate, ql.Duration.Modified)
		durationMacaulay= ql.BondFunctions.duration(qL_fixRateBond, qL_interestRate, ql.Duration.Macaulay)
		convexitySimple	= ql.BondFunctions.convexity(qL_fixRateBond, qL_interestRate)

	except:
		print("Calculations Failed\n")

#
# DISPLAY
	
	def display():
		print("\n \n NEW BOND\n \n")
		print("### Bond Detail ###")
		print(f"Calendar: {qL_calendar}")
		print(f"Day Count: {qL_dayCount}")
		print("Analysis Date: %s" % qL_analysisDate)
		print("Bondname: %s" % bondName)
		print("Issuance Date: %s" % qL_issuanceDate)
		print("Maturity Date: %s" % qL_maturityDate)

		print("Tenor (QuantLib calculated): %s" % qL_tenor)
		print("Coupon Rate: %s" % qL_couponRate)
		print("Coupons: %s" % qL_coupons)
		print("Face Value (FV): %s" % qL_faceValue)

		print("\n")

		print("### Payment Schedule settings and calculation ###")
		print("Business Convention (QuantLib setting): %s" % qL_businessConvention)
		print("Date Generation (QuantLib setting): %s" % qL_dateGeneration)
		print("Month End (QuantLib setting): %s" % qL_monthEnd)
		print("Payment Schedule (QuantLib calculated): %s" % list(qL_schedule))

		print("\n")

		print("### Detail for Analysis ###")
		print("Analysis Date: %s" % qL_analysisDate)
		print("Settlment Days: %s" % qL_settlementDays)
		print("Current Par Price: %s" % currentParPrice)
		print("Spot Dates: %s" % qL_spotDates)
		print("Spot Rates: %s" % qL_spotRates)
		print("Day Count Format (QuantLib setting): %s" % qL_dayCount)
		print("Calendar Format (QuantLib setting): %s" % qL_calendar)
		print("Compounding (QuantLib setting): %s" % qL_compounding)
		print("Compounding Frequency (QuantLib setting): %s" % ql_paymentFrequency)

		print("\n")

		print("### Calculations ###")
		print("Interest Rates: %s" % qL_interestRate)
		print("Duration Simple: %s" % durationSimple)
		print("Duration Modified: %s" % durationModified)
		print("Duration Macaulay: %s" % durationMacaulay)
		print("Convexity: %s" % convexitySimple)

	display()
	