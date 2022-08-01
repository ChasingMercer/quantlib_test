import QuantLib as ql
from datetime import date
import pandas as pd
from dictionaries.ql_dictionary import *

df = pd.read_csv("data/ICE_DF.csv")
df = df[df["Country Code"].isin(country_ql.keys()) & df["Interest Basis"].isin(day_count_ql.keys(
)) & df["Interest Payment Frequency"].isin(tenor_ql.keys()) & df["Business Day Convention Code"].isin(
    business_convention_ql) & df["Nominal Value"].notnull()]
df["Accrual Date"] = pd.to_datetime(df["Accrual Date"])
df["Maturity Date"] = pd.to_datetime(df["Maturity Date"])
df = df[df["Country Code"] == "US"]
todays_date = date.today()

for index, row in df.iloc[:10].iterrows():
    try:
        print("---NEW BOND---")
        valuationDate = ql.Date(
            todays_date.day, todays_date.month, todays_date.year)

        coupon = float(row["Original Coupon Rate"]) / 100
        settlementDays = 0

        ql.Settings.instance().evaluationDate = valuationDate
        compounding = ql.Compounded
        calendar = country_ql[row["Country Code"]]()

        couponFrequency = tenor_ql[row["Interest Payment Frequency"]]

        issueDate = ql.Date(
            row["Accrual Date"].day, row["Accrual Date"].month, row["Accrual Date"].year)  # dd/mm/YY
        maturityDate = ql.Date(
            row["Maturity Date"].day, row["Maturity Date"].month, row["Maturity Date"].year)  # dd/mm/YY

        businessConvention = ql.Following

        dayCount = day_count_ql[row["Interest Basis"]]()

        faceValue = row["Nominal Value"]
        redemptionValue = row["Nominal Value"]

        schedule = ql.Schedule(
            issueDate, maturityDate, ql.Period(couponFrequency), calendar,
            businessConvention, businessConvention, ql.DateGeneration.Forward, True)

        fixedRateBond = ql.FixedRateBond(settlementDays, ql.TARGET(), faceValue,
                                         issueDate, maturityDate, ql.Period(couponFrequency), [coupon], dayCount)

        yield_rate = fixedRateBond.bondYield(98,
                                             dayCount, compounding, couponFrequency)

        print(row["ISIN"], yield_rate)


    except Exception as e:
        print(e)
        print("\n")
