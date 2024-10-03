import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def preprocess_sector_data(sector,sector_name,stat):
    #read in productivity dagta
    df = pd.read_csv('National_aggregation_quarterly/36100207.csv')
    print(df.head())
    print(df.info())
    #get all sectors
    print(df['North American Industry Classification System (NAICS)'].unique())
    print(df['Labour productivity measures and related variables'].unique())
    
    #get Mining and oil and gas extraction 
    sector_df = df[(df['North American Industry Classification System (NAICS)'] == sector) &
                    (df['Labour productivity measures and related variables'] == stat)]
    
    #total productivity
    total_df = df[(df['North American Industry Classification System (NAICS)'] == 'Total economy') &
                  (df['Labour productivity measures and related variables'] == stat)]
    
    #geography
    print(sector_df.head())
    print(sector_df.info())

    

    #drop null values
    #total_df = total_df.dropna()
    sector_df = sector_df.dropna(subset=['VALUE'], axis=0)

    #plot production data
    
    #select columns
    sector_df = sector_df[['REF_DATE', 'Labour productivity measures and related variables','North American Industry Classification System (NAICS)','VALUE']]
    total_df = total_df[['REF_DATE', 'Labour productivity measures and related variables','North American Industry Classification System (NAICS)','VALUE']]

    print(len(sector_df))
    print(sector_df)
    print(sector_df.index)
    print(total_df['REF_DATE'].values)
    print(sector_df['REF_DATE'].values)
    #get all the matching time values 
    print(total_df[total_df['REF_DATE'].isin(sector_df['REF_DATE'])])

   # total_df = total_df[total_df['REF_DATE'].isin(mining_df['REF_DATE'])]

    #convert ref date to date time
    sector_df['REF_DATE'] = pd.to_datetime(sector_df['REF_DATE'], format='%Y-%m')
    total_df['REF_DATE'] = pd.to_datetime(total_df['REF_DATE'], format='%Y-%m')
    
    plt.plot(sector_df['REF_DATE'], sector_df['VALUE'])
    plt.plot(total_df['REF_DATE'], total_df['VALUE'])
    plt.show()

    #tag data by quarters
    sector_df['quarter'] = sector_df['REF_DATE'].dt.quarter
    total_df['quarter'] = total_df['REF_DATE'].dt.quarter

    #calculate perctange chage veruses previous quarter
    sector_df['pct_change'] = sector_df['VALUE'].pct_change().fillna(0)*100
    total_df['pct_change'] = total_df['VALUE'].pct_change().fillna(0)*100

    #export to csv
    sector_df.to_csv("canadain_" + sector_name + "_productivity.csv", index=False)  
    total_df.to_csv('canadain_total_productivity.csv', index=False)
    print(total_df.head())

    print(sector_df['VALUE'].pct_change().fillna(0))


def multi_factor_productivity(sector,sector_name):
    df = pd.read_csv('Canadian_multifactor_productivity/36100208.csv')
    print(df.head())
    print(df.info())  
    print(df['North American Industry Classification System (NAICS)'].unique())


    print(df['Multifactor productivity and related variables'].unique())

    sector_df = df[(df['North American Industry Classification System (NAICS)'] == sector) &
                    (df['Multifactor productivity and related variables'] == 'Multifactor productivity')]
    
    sector_df['REF_DATE'] = pd.to_datetime(sector_df['REF_DATE'], format='%Y')

    plt.plot(sector_df['REF_DATE'], sector_df['VALUE'])
    plt.show()

    sector_df['quarter'] = sector_df['REF_DATE'].dt.quarter
    sector_df.to_csv("canadain_" + sector_name + "_multifactor.csv", index=False)  

    print(sector_df.head())


def preprocess_anaual_data(sector,stat,geo,sector_name): 

    #read in productivity data
    df = pd.read_csv('provinical_aggregation_annually/36100480.csv')

    print(df.head())
    print(df.info())

    print(df['Labour productivity and related measures'].unique())

    #get Mining and oil and gas extraction 
    sector_df = df[(df['Labour productivity and related measures'] == stat) &
                    (df['Industry'] == sector)]
    
    # #geography
    sector_df = sector_df[(sector_df['GEO'] == geo)]

    print(sector_df.head())

    sector_df = sector_df[['GEO','REF_DATE', 'Labour productivity and related measures','VALUE']]

    sector_df['REF_DATE'] = pd.to_datetime(sector_df['REF_DATE'], format='%Y')

    sector_df['pct_change'] = sector_df['VALUE'].pct_change().fillna(0)*100

    # #tag data by quarters
    sector_df['quarter'] = sector_df['REF_DATE'].dt.quarter

    #export to csv
    sector_df.to_csv("canadain_" + sector_name + "_annual.csv", index=False) 

    


    # #calculate perctange chage veruses previous quarter
    # sector_df['pct_change'] = sector_df['VALUE'].pct_change().fillna(0)*100

    # #export to csv
    # sector_df.to_csv("canadain_" + sector + ".csv", index=False)
    



def main():
    preprocess_sector_data("Mining and oil and gas extraction [21]","oil_mining_gdp","Real gross domestic product (GDP)")
    preprocess_sector_data("Mining and oil and gas extraction [21]","oil_mining","Labour productivity")
    # preprocess_sector_data("Real estate and rental and leasing [53]","real_estate")
    # preprocess_sector_data("Manufacturing [31-33]","manufacturing")
    # preprocess_sector_data("Construction [23]","construction")
    # preprocess_sector_data("Finance and insurance, and holding companies","finance")

    #preprocess_sector_data("All industries","all_industries","Real gross domestic product (GDP)")

    #multi factor productivity

    #multi_factor_productivity("Mining and oil and gas extraction [21]","oil_mining")
    #multi_factor_productivity("Business sector","business")

    #preprocess_annual_data

    preprocess_anaual_data("All industries","Labour productivity","Canada","all")

    preprocess_anaual_data("Mining and oil and gas extraction [BS21]","Labour productivity","Canada","oil_mining")
    




    


if __name__ == '__main__':
    main()