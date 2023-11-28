
import pandas as pd

def clean_gender_column(df: pd.DataFrame)->pd.DataFrame:
    
    df2 = df.copy()
    if "gender" not in df2.columns:
        return df2
    else:
        df2['gender'] = df2['gender'].apply(lambda x: str(x)[0].upper() if str(x)[0].upper() in ['M', 'F'] else "U")
        return df2
     
def clean_state_column(df: pd.DataFrame)->pd.DataFrame:
    df2 = df.copy()
    df2['state'] = df2['state'].fillna("Unknown")
    replacements = {'Cali': 'California', 'AZ': 'Arizona', 'WA': 'Washington'}
    df2['state'] = df2['state'].replace(replacements)
    return df2

def clean_education_column(df: pd.DataFrame)-> pd.DataFrame:
   
    df2 = df.copy()
    df2['education'] = df['education'].fillna("Unknown")
    replacements = {'Bachelors': 'Bachelor'}
    df2['education'] = df2['education'].replace(replacements)
    
    return df2

def clean_customerlifetimevalue_column(df: pd.DataFrame)->pd.DataFrame:
    
    df2 = df.copy()
    df2['customer_lifetime_value'] = df2['customer_lifetime_value'].fillna('0.')
    df2['customer_lifetime_value'] = df2['customer_lifetime_value'].str.replace('%','')
    df2['customer_lifetime_value'] = pd.to_numeric(df2['customer_lifetime_value'])
    return df2

def clean_vehicle_class_column(df: pd.DataFrame)->pd.DataFrame:
    df2 = df.copy()
    df2['vehicle_class'] = df2['vehicle_class'].fillna("Unknown")
    replacements = {'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'}
    df2['vehicle_class'] = df2['vehicle_class'].replace(replacements)
    return df2

def correct_open_complaints(df: pd.DataFrame)-> pd.DataFrame:
    
    df2 = df.copy()
    df2['number_of_open_complaints'] = df2['number_of_open_complaints'].fillna('0')
    df2['number_of_open_complaints'] = df2['number_of_open_complaints']\
    .apply(lambda value: value.split("/")[1] if "/" in value else value)
    df2['number_of_open_complaints'] = pd.to_numeric(df2['number_of_open_complaints'])
    return df2

def fill_nan_dataframe(df: pd.DataFrame)-> pd.DataFrame:
    df2= df.copy()
    
    df2['customer'] = df2['customer'].fillna("Unknown")
    df2['income']= df2['income'].fillna(df2['income'].median())
    df2['monthly_premium_auto']= df2['monthly_premium_auto'].fillna(df2['monthly_premium_auto'].mean())
    df2['policy_type'] = df2['policy_type'].fillna("Unknown")
    df2['total_claim_amount']= df2['total_claim_amount'].fillna(df2['total_claim_amount'].median())
    return df2

def drop_duplicates(df: pd.DataFrame)-> pd.DataFrame:
    df2= df.copy()
    df2= df2.drop_duplicates(keep='first')
    return df2

