instrument_type_dict = {
    0: "None", 1: "Depository Receipt", 2: "Commodity Spot Rate", 3: "Debt", 4: "Equity",
    5: "Future",
    6: "Hybrid", 7: "Interest Rate", 8: "Unknown", 9: "Option", 10: "Exchange Rate",
    11: "Composite Unit", 12: "Fund",
    13: "Other Derivatives", 14: "Entitlement", 15: "Index", 16: "Strategy"
}

coupon_type_dict = {
    0: "Unknown", 1: "Short Term Discount", 2: "Fixed Rate - Unconfirmed", 3: "Adjustable Rate",
    4: "Zero Coupon",
    5: "Floating Rate", 6: "Index Linked", 7: "Stepped Coupon", 8: "Fixed Rate",
    9: "Stripped Convertible",
    10: "Deferred Interest", 11: "Floating Rate @ Floor", 12: "Stripped Tax Credit",
    13: " Inverse Floating",
    14: "Stripped Coupon Principal", 15: "Linked Inverse Floater", 16: "Flexible Rate",
    17: "Original Issue Discount",
    18: "Stripped Principal", 19: "Reserve CUSIP", 20: "Variable Rate", 21: "Stripped Coupon",
    22: "Floating Auction Rate",
    23: "Tax Credit", 24: "Tax Credit OID", 25: "Stripped Coupon Payment",
    26: "Stepped Up Stepped Down", 27: "Credit Sensitive",
    28: "Pay in Kind", 29: "Range", 30: "Digital", 31: "Reset"
}

accrual_compounding_method_dict = {
    1: "Annual", 2: "Daily", 3: "Simple Interest", 4: "Monthly", 5: "Quarterly",
    6: "Semi-Annually", 7: "Weekly"
}

frequency_type_dict = {
    0: "Unknown", 1: "Semiannually", 2: "Monthly", 3: "Annually", 4: "Weekly", 5: "Quarterly",
    6: "Every 2 Years", 7: "Every 3 Years", 8: "Every 4 Years", 9: "Every 5 Years", 10: "Every 7 Years",
    11: "Every 8 Years", 12: "Biweekly", 13: "Changeable", 14: "Daily", 15: "Term Mode", 16: "Interest at Maturity",
    17: "Bimonthly",
    18: "Every 13 Weeks", 19: "Irregular",
    20: "Every 28 Days", 21: "Every 35 Days", 22: "Every 26 Weeks", 23: "Not Applicable", 24: "Tied to Prime",
    25: "One Time", 26: "Every 10 Years",
    27: "Frequency to be Determined", 28: "Mandatory Put", 29: "Every 52 Weeks",
    30: "When interest adjusts-commercial paper", 31: "Zero Coupon",
    32: "Certain Years Only", 33: "Under Certain Circumstances", 34: "Every 15 Years", 35: "Custom",
    36: "Single Interest-Payment"
}
payment_frequency_dict = {
    1: "Annually", 2: "Semi Annual", 3: "Quarterly", 4: "Monthly", 5: "Weekly", 6: "Daily", 7: "Every x Days",
    8: "Every x Weeks", 10: "Every x Years",
    11: "At Maturity", 12: "Single Date", 13: "Single Interest Payment", 14: "Flexible (Issuer's Option)",
    15: "Not Applicable"
}

interest_basis_dict = {
    1: "Actual/Actual", 2: "Actual/360", 3: "30/360", 5: "Actual/365 (Fixed)",
    7: "Actual/365 (366 Leap Year - ISDA)", 8: "30/360 (Compounded Interest)", 9: "30/365",
    10: "Future Data - Not Available", 11: "Historical Data - Not Available",
    12: "30/360 (ICMA)", 13: "Actual/365 (366 Leap Year)", 14: "Actual/364",
    15: "Bus/252", 16: "365/365", 17: "Actual/Actual (ICMA)",
    19: "30/360 US", 20: "30/360 US (NASD)", 21: "30/360 BMA",
    22: "30/360 (ISDA)", 23: "30/360 IT", 24: "30/360 SIA", 25: "30E/360",
    26: "30E/360 (ISDA)", 27: "30E+/360", 28: "NL/365 (No Leap Year)"
}

business_day_convention_type_dict = {1:"Floating Rate Convention", 2:"Modified Following Business Day Convention",
                                    3: "No Adjustment", 4:"Preceding Business Day Convention",
                                    5:"Following Business Day Convention"}