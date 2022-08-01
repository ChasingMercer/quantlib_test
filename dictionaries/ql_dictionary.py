import QuantLib as ql

day_count_ql = {"Actual/360": ql.Actual360, "Actual/364" : ql.Actual364, "Actual365Fixed" : ql.Actual365Fixed,
                "Actual/Actual" : ql.ActualActual, "Bus/252" : ql.Business252, "30/360" : ql.Thirty360, 
                "30/365" : ql.Thirty365 }

country_ql = {"BR" : ql.Brazil, "CA" : ql.Canada, "CZ" : ql.CzechRepublic, "FR" : ql.France, "DE": ql.Germany,
            "HK" : ql.HongKong, "IS" : ql.Iceland, "IN" : ql.India, "ID" : ql.Indonesia, "IL" : ql.Israel,
            "IT" : ql.Italy, "MX" : ql.Mexico, "RU" : ql.Russia, "SA" : ql.SaudiArabia, "SG" : ql.Singapore,
            "SK" : ql.Slovakia, "KR" : ql.SouthKorea, "TW" : ql.Taiwan, "UA" : ql.Ukraine, "GB" : ql.UnitedKingdom,
            "US" : ql.UnitedStates}

tenor_ql = {"Semi Annual" : ql.Semiannual, "Annually" : ql.Annual, "Weekly" : ql.Weekly, "Quarterly" : ql.Quarterly}

payment_frequency_ql = {"Semi Annual" : 2, "Annually" : 1, "Weekly" : 52, "Quarterly" : 4}

business_convention_ql = {"Following Business Day Convention" : ql.Following, "Preceding Business Day Convention" : ql.Preceding, "Modified Following Business Day Convention" : ql.ModifiedPreceding, "No Adjustment" : ql.Unadjusted}
