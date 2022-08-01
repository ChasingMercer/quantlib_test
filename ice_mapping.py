import time
import xml.etree.ElementTree as ET
from datetime import date
from dictionaries.ICE_dictionary import *
import pandas as pd
import QuantLib as ql


pd.options.display.max_columns = 20
pd.options.display.max_rows = 20

start = time.perf_counter()

# Defining Lists for intermediary data storage
# No Mapping Needed
cusip = []
isin = []
country_code = []
issue_date = []
maturity_date = []
original_coupon_rate = []
nom_val_bond = []
redemption_percentage = []
call_indicator = []

# Mapping Needed
instrument_type = []
coupon_type = []
business_day_convention_type = []
payment_freq = []
accrual_compounding_method = []
interest_basis = []

file = 'data/init.xml'


def run(data):

    tree = ET.parse(file)
    root = tree.getroot()

    root_find = root.findall("./payload/instrument")

    for each in root_find:
        # #No Mapping
        try:
            cusip.append(
                each.find('./master_information/instrument_xref/xref/[@type="CUSIP"]').text)
        except:
            cusip.append(None)
        try:
            isin.append(
                each.find('./master_information/instrument_xref/xref/[@type="ISIN"]').text)
        except:
            isin.append(None)
        try:
            country_code.append(each.find(
                "./global_information/country_information/instrument_country_information/country_code").text)
        except:
            country_code.append(None)
        try:
            issue_date.append(pd.to_datetime(
                each.find("./master_information/instrument_master/issue_date").text))
        except:
            issue_date.append(None)
        try:
            maturity_date.append(pd.to_datetime(
                each.find("./debt/fixed_income/maturity_date").text))
        except:
            maturity_date.append(None)
        try:
            original_coupon_rate.append(
                each.find("./debt/fixed_income/original_coupon_rate").text)
        except:
            original_coupon_rate.append(None)
        try:
            nom_val_bond.append(
                each.find("./debt/fixed_income/nominal_value").text)
        except:
            nom_val_bond.append(None)
        try:
            redemption_percentage.append(
                each.find("./debt/fixed_income/maturity_redemption_percentage").text)
        except:
            redemption_percentage.append(None)
        try:
            call_indicator.append(each.find(
                "./debt/fixed_income/call_indicator").text)
        except:
            call_indicator.append(None)

        # Need Mapping
        try:
            coupon_type.append(coupon_type_dict[int(
                each.find('./debt/fixed_income/coupon_type').text)])
        except:
            coupon_type.append(None)
        try:
            instrument_type.append(instrument_type_dict[int(
                each.find('./master_information/instrument_master/instrument_type').text)])
        except:
            instrument_type.append(None)
        try:
            business_day_convention_type.append(business_day_convention_type_dict[
                int(each.find('./debt/fixed_income/business_day_convention_code').text)])
        except:
            business_day_convention_type.append(None)
        try:
            payment_freq.append(payment_frequency_dict[int(
                each.find('./debt/fixed_income/original_interest_payment_frequency').text)])
        except:
            payment_freq.append(None)
        try:
            interest_basis.append(interest_basis_dict[int(
                each.find("./debt/coupon_payment_feature/interest_basis").text)])
        except:
            interest_basis.append(None)
        try:
            accrual_compounding_method.append(accrual_compounding_method_dict[int(
                each.find("./debt/coupon_payment_feature/interest_basis").text)])
        except:
            accrual_compounding_method.append(None)

    full_df = pd.DataFrame()

# Assigning lists to DF
    full_df["CUSIP"] = cusip
    full_df["ISIN"] = isin
    full_df["Coupon Type"] = coupon_type
    full_df["Instrument Type"] = instrument_type
    full_df["Country Code"] = country_code
    full_df["Issue Date"] = issue_date
    full_df["Maturity Date"] = maturity_date
    full_df["Interest Payment Frequency"] = payment_freq
    full_df["Original Coupon Rate"] = original_coupon_rate
    full_df["Nominal Value"] = nom_val_bond
    full_df["Accrual Compounding Method"] = accrual_compounding_method
    full_df["Business Day Convention Code"] = business_day_convention_type
    full_df["Interest Basis"] = interest_basis
    full_df["Redemption Percentage"] = redemption_percentage
    full_df["Call Indicator"] = call_indicator

    # Filtering
    full_df = full_df[full_df["Coupon Type"] == "Fixed Rate"]
    full_df = full_df[full_df["Maturity Date"].notnull() &
                      full_df["Issue Date"].notnull()]
    full_df = full_df[full_df["Maturity Date"] > pd.to_datetime(date.today())]
    full_df = full_df[full_df["Call Indicator"] == "true"]

    print(full_df)
    print(f"Null Percent: {(len(full_df.isnull())/ full_df.size)}%")
    full_df.to_csv("data\ICE_DF.csv")


run(file)


end = time.perf_counter()
print(f"Function Run Time: {(end-start)} Seconds")