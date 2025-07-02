def transform_ericsson_volte(df):
    df[["Origin-Host"]] = (
        df["Session-Id"].str.split(";", n=1, expand=True)[0].astype("string")
    )
    df.loc[df["Vendor-Id"].notna(), ["Vendor", "Type"]] = ["HUAWEI", "TAS"]
    df.loc[df["Origin-Host"].str.startswith("pcscf"), ["Vendor", "Type"]] = [
        "ERICSSON",
        "SBG",
    ]
    df.loc[df["Origin-Host"].str.startswith("scscf"), ["Vendor", "Type"]] = [
        "ERICSSON",
        "IMS",
    ]
    slice = df["Origin-Host"].str.startswith("tas") & df["Vendor-Id"].isna()
    df.loc[slice, ["Vendor", "Type"]] = ["ERICSSON", "TAS"]
    df["Accounting-Record-Type"] = df["Accounting-Record-Type"].map(
        {1.0: "EVENT", 2.0: "START", 3.0: "INTERIM", 4.0: "STOP"}
    )
    return df.drop(["Vendor-Id"], axis=1)
