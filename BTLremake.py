#Datasets about player & team NBA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_playerdt = pd.read_csv('NBA Data/NBA PLayer Stats(1950 - 2022)', encoding='utf-8', index_col='Tm')
#Information about datasets
df = df_playerdt.info()
#Lenght of datasets
df_1 = len(df_playerdt)
print(df_1)
#Shape of datasets
print('Shape:', df_playerdt.shape)
print(df)
#Total of player(1950-2022)
df_3 = df_playerdt.drop_duplicates(subset=['Player'], keep='first')
#print(df_3)
print('Total of Player(1950-2022):', len(df_3['Player']))
#Total of player(1950)
df_4 = df_playerdt[df_playerdt['Season'] == 1950]
#print(df_4)
print('Total of Player(1950):', len(df_4.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(1951)
df_5 = df_playerdt[df_playerdt['Season'] == 1951]
#print(df_5)
print('Total of Player(1951):', len(df_5.drop_duplicates(subset=['Player'],keep='first')))
#Total of player(1952)
df_6 = df_playerdt[df_playerdt['Season'] == 1952]
#print(df_6)
print('Total of Player(1952):', len(df_6.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(1953)
df_7 = df_playerdt[df_playerdt['Season'] == 1953]
#print(df_7)
print('Total of Player(1953):', len(df_7.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1954)
df_8 = df_playerdt[df_playerdt['Season'] == 1954]
#print(df_8)
print('Total of Player(1954):', len(df_8.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1955)
df_9 = df_playerdt[df_playerdt['Season'] == 1955]

#print(df_9)
print('Total of PLayer(1955):', len(df_9.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1956)
df_10 = df_playerdt[df_playerdt['Season'] == 1956]
#print(df_10)
print('Total of Player(1956):', len(df_10.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1957)
df_11 = df_playerdt[df_playerdt['Season'] == 1957]
#print(df_11)
print('Total of PLayer(1957):', len(df_11.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1958)
df_12 = df_playerdt[df_playerdt['Season'] == 1958]
#print(df_12)
print('Total of PLayer(1958):', len(df_12.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1959)
df_13 = df_playerdt[df_playerdt['Season'] == 1959]
#print(df_13)
print('Total of Player(1959):', len(df_13.drop_duplicates(subset=['Player'], keep='first')))
#Total pff Player(1960)
df_14 = df_playerdt[df_playerdt['Season'] == 1960]
#print(df_14)
print('Total of Player(1960):', len(df_14.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1961)
df_15 = df_playerdt[df_playerdt['Season'] == 1961]
#print(df_15)
print('Total of PLayer(1961):', len(df_15.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1962)
df_16 = df_playerdt[df_playerdt['Season'] == 1962]
#print(df_16)
print('Total of Player(1962):', len(df_16.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1963)
df_17 = df_playerdt[df_playerdt['Season'] == 1963]
#print(df_17)
print('Total of Player(1963):', len(df_17.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1964)
df_18 = df_playerdt[df_playerdt['Season'] == 1964]
#print(df_18)
print('Total of PLayer(1964):', len(df_18.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1965)
df_19 = df_playerdt[df_playerdt['Season'] == 1965]
#print(df_19)
print('Total of Player(1965):', len(df_19.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1966)
df_20 = df_playerdt[df_playerdt['Season'] == 1966]
#print(df_20)
print('Total of Player(1966):',len(df_20.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1967)
df_21 = df_playerdt[df_playerdt['Season'] == 1967]
#print(df_21)
print('Total of PLayer(1967):', len(df_21.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1968)
df_22 = df_playerdt[df_playerdt['Season'] == 1968]
#print(df_22)
print('Total of Player(1968):', len(df_22.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1969)
df_23 = df_playerdt[df_playerdt['Season'] == 1969]
#print(df_23)
print('Total of Player(1969):', len(df_23.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1970)
df_24 = df_playerdt[df_playerdt['Season'] == 1970]
#print(df_24)
print('Total of Player(1970):', len(df_24.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1971)
df_25 = df_playerdt[df_playerdt['Season'] == 1971]
#print(df_25)
print('Total of Player(1971):', len(df_25.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1972)
df_26 = df_playerdt[df_playerdt['Season'] == 1972]
#print(df_26)
print('Total of Player(1972):', len(df_26.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1973)
df_27 = df_playerdt[df_playerdt['Season'] == 1973]
#print(df_27)
print('Total of PLayer(1973):', len(df_27.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(1974)
df_28 = df_playerdt[df_playerdt['Season'] == 1974]
#print(df_28)
print('Total of Player(1974):', len(df_28.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(1975)
df_29 = df_playerdt[df_playerdt['Season'] == 1975]
#print(df_29)
print('Total of Player(1975):', len(df_29.drop_duplicates(subset=['Player'],keep='first')))
#Total of player(1976)
df_30 = df_playerdt[df_playerdt['Season'] == 1976]
#print(df_30)
print('Total of Player(1976):', len(df_30.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(1977)
df_31 = df_playerdt[df_playerdt['Season'] == 1977]
#print(df_31)
print('Total of Player(1977):', len(df_31.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1978)
df_32 = df_playerdt[df_playerdt['Season'] == 1978]
#print(df_32)
print('Total of Player(1978):', len(df_32.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1979)
df_33 = df_playerdt[df_playerdt['Season'] == 1979]
#print(df_33)
print('Total of PLayer(1979):', len(df_33.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1980)
df_34 = df_playerdt[df_playerdt['Season'] == 1980]
#print(df_34)
print('Total of Player(1980):', len(df_34.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1981)
df_35 = df_playerdt[df_playerdt['Season'] == 1981]
#print(df_35)
print('Total of PLayer(1981):', len(df_35.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1982)
df_36 = df_playerdt[df_playerdt['Season'] == 1982]
#print(df_36)
print('Total of PLayer(1982):', len(df_36.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1983)
df_37 = df_playerdt[df_playerdt['Season'] == 1983]
#print(df_37)
print('Total of Player(1983):', len(df_37.drop_duplicates(subset=['Player'], keep='first')))
#Total pff Player(1984)
df_38 = df_playerdt[df_playerdt['Season'] == 1984]
#print(df_38)
print('Total of Player(1984):', len(df_38.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1985)
df_39 = df_playerdt[df_playerdt['Season'] == 1985]
#print(df_39)
print('Total of PLayer(1985):', len(df_39.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1986)
df_40 = df_playerdt[df_playerdt['Season'] == 1986]
#print(df_40)
print('Total of Player(1986):', len(df_40.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1987)
df_41 = df_playerdt[df_playerdt['Season'] == 1987]
#print(df_41)
print('Total of Player(1987):', len(df_41.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1988)
df_42 = df_playerdt[df_playerdt['Season'] == 1988]
#print(df_42)
print('Total of PLayer(1988):', len(df_42.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1989)
df_43 = df_playerdt[df_playerdt['Season'] == 1989]
#print(df_43)
print('Total of Player(1989):', len(df_43.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1990)
df_44 = df_playerdt[df_playerdt['Season'] == 1990]
#print(df_44)
print('Total of Player(1990):', len(df_44.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1991)
df_45 = df_playerdt[df_playerdt['Season'] == 1991]
#print(df_45)
print('Total of PLayer(1991):', len(df_45.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1992)
df_46 = df_playerdt[df_playerdt['Season'] == 1992]
#print(df_46)
print('Total of Player(1992):', len(df_46.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1993)
df_47 = df_playerdt[df_playerdt['Season'] == 1993]
#print(df_47)
print('Total of Player(1993):', len(df_47.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1994)
df_48 = df_playerdt[df_playerdt['Season'] == 1994]
#print(df_48)
print('Total of Player(1994):', len(df_48.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1995)
df_49 = df_playerdt[df_playerdt['Season'] == 1995]
#print(df_49)
print('Total of Player(1995):', len(df_49.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1996)
df_50 = df_playerdt[df_playerdt['Season'] == 1996]
#print(df_50)
print('Total of Player(1996):', len(df_50.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1997)
df_51 = df_playerdt[df_playerdt['Season'] == 1997]
#print(df_51)
print('Total of PLayer(1997):', len(df_51.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(1998)
df_52 = df_playerdt[df_playerdt['Season'] == 1998]
#print(df_52)
print('Total of Player(1998):', len(df_52.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(1999)
df_53 = df_playerdt[df_playerdt['Season'] == 1999]
#print(df_53)
print('Total of Player(1999):', len(df_53.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2000)
df_54 = df_playerdt[df_playerdt['Season'] == 2000]
#print(df_54)
print('Total of Player(2000):', len(df_54.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2001)
df_55 = df_playerdt[df_playerdt['Season'] == 2001]
#print(df_55)
print('Total of PLayer(2001):', len(df_55.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(2002)
df_56 = df_playerdt[df_playerdt['Season'] == 2002]
#print(df_56)
print('Total of Player(2002):', len(df_56.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(2003)
df_57 = df_playerdt[df_playerdt['Season'] == 2003]
#print(df_57)
print('Total of Player(2003):', len(df_57.drop_duplicates(subset=['Player'],keep='first')))
#Total of player(2004)
df_58 = df_playerdt[df_playerdt['Season'] == 2004]
#print(df_58)
print('Total of Player(2004):', len(df_58.drop_duplicates(subset=['Player'], keep='first')))
#Total of player(2005)
df_59 = df_playerdt[df_playerdt['Season'] == 2005]
#print(df_59)
print('Total of Player(2005):', len(df_59.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2006)
df_60 = df_playerdt[df_playerdt['Season'] == 2006]
#print(df_60)
print('Total of Player(2006):', len(df_60.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2007)
df_61 = df_playerdt[df_playerdt['Season'] == 2007]
#print(df_61)
print('Total of PLayer(2007):', len(df_61.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2008)
df_62 = df_playerdt[df_playerdt['Season'] == 2008]
#print(df_62)
print('Total of Player(2008):', len(df_62.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2009)
df_63 = df_playerdt[df_playerdt['Season'] == 2009]
#print(df_63)
print('Total of PLayer(2009):', len(df_63.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(2010)
df_64 = df_playerdt[df_playerdt['Season'] == 2010]
#print(df_64)
print('Total of PLayer(2010):', len(df_64.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2011)
df_65 = df_playerdt[df_playerdt['Season'] == 2011]
#print(df_65)
print('Total of Player(2011):', len(df_65.drop_duplicates(subset=['Player'], keep='first')))
#Total pff Player(2012)
df_66 = df_playerdt[df_playerdt['Season'] == 2012]
#print(df_66)
print('Total of Player(2012):', len(df_66.drop_duplicates(subset=['Player'], keep='first')))
#Total of PLayer(2013)
df_67= df_playerdt[df_playerdt['Season'] == 2013]
#print(df_67)
print('Total of PLayer(2013):', len(df_67.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2014)
df_68 = df_playerdt[df_playerdt['Season'] == 2014]
#print(df_68)
print('Total of Player(2014):', len(df_68.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2015)
df_69 = df_playerdt[df_playerdt['Season'] == 2015]
#print(df_69)
print('Total of Player(2015):', len(df_69.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2016)
df_70 = df_playerdt[df_playerdt['Season'] == 2016]
#print(df_70)
print('Total of PLayer(2016):', len(df_70.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2017)
df_71 = df_playerdt[df_playerdt['Season'] == 2017]
#print(df_71)
print('Total of Player(2017):', len(df_71.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2018)
df_72 = df_playerdt[df_playerdt['Season'] == 2018]
#print(df_72)
print('Total of Player(2018):', len(df_72.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2019)
df_73 = df_playerdt[df_playerdt['Season'] == 2019]
#print(df_73)
print('Total of PLayer(2019):', len(df_73.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2020)
df_74 = df_playerdt[df_playerdt['Season'] == 2020]
#print(df_74)
print('Total of Player(2020):', len(df_74.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2021)
df_75 = df_playerdt[df_playerdt['Season'] == 2021]
#print(df_75)
print('Total of Player(2021):', len(df_75.drop_duplicates(subset=['Player'], keep='first')))
#Total of Player(2022)
df_76 = df_playerdt[df_playerdt['Season'] == 2022]
#print(df_76)
print('Total of Player(2022):', len(df_76.drop_duplicates(subset=['Player'], keep='first')))

#Age

#Age 18
df_77 = df_playerdt[df_playerdt['Age'] == 18.0]
#print(df_77[['Player', 'Age']])
print('Total of Player Age(18):', len(df_77.drop_duplicates(subset=['Player'], keep='first')))
df_001 = len(df_77.drop_duplicates(subset=['Player'], keep='first'))

#Age 19
df_78 = df_playerdt[df_playerdt['Age'] == 19.0]
#print(df_78[['Player', 'Age']])
print('Total of Player Age(19):', len(df_78.drop_duplicates(subset=['Player'], keep='first')))
df_002 = len(df_78.drop_duplicates(subset=['Player'], keep='first'))

#Age 20
df_79 = df_playerdt[df_playerdt['Age'] == 20.0]
#print(df_79[['Player', 'Age']])
print('Total of Player Age(20):', len(df_79.drop_duplicates(subset=['Player'], keep='first')))
df_003 = len(df_79.drop_duplicates(subset=['Player'], keep='first'))

#Age 21
df_80 = df_playerdt[df_playerdt['Age'] == 21.0]
#print(df_80[['Player', 'Age']])
print('Total of Player Age(21):', len(df_80.drop_duplicates(subset=['Player'], keep='first')))
df_004 = len(df_80.drop_duplicates(subset=['Player'], keep='first'))

#Age 22
df_81 = df_playerdt[df_playerdt['Age'] == 22.0]
#print(df_81[['Player', 'Age']])
print('Total of Player Age(22):', len(df_81.drop_duplicates(subset=['Player'], keep='first')))
df_005 = len(df_81.drop_duplicates(subset=['Player'], keep='first'))

#Age 23
df_82 = df_playerdt[df_playerdt['Age'] == 23.0]
#print(df_82[['Player', 'Age']])
print('Total of PLayer Age(23):', len(df_82.drop_duplicates(subset=['Player'], keep='first')))
df_006 = len(df_82.drop_duplicates(subset=['Player'], keep='first'))

#Age 24
df_83 = df_playerdt[df_playerdt['Age'] == 24.0]
#print(df_83[['Player', 'Age']])
print('Total of Player Age(24):', len(df_83.drop_duplicates(subset=['Player'], keep='first')))
df_007 = len(df_83.drop_duplicates(subset=['Player'], keep='first'))

#Age 25
df_84 = df_playerdt[df_playerdt['Age'] == 25.0]
#print(df_84[['Player', 'Age']])
print('Total of Player Age(25):', len(df_84.drop_duplicates(subset=['Player'], keep='first')))
df_008 =  len(df_84.drop_duplicates(subset=['Player'], keep='first'))

#Age 26
df_85 = df_playerdt[df_playerdt['Age'] == 26.0]
#print(df_85[['Player', 'Age']])
print('Total of PLayer Age(26):', len(df_85.drop_duplicates(subset=['Player'], keep='first')))
df_009 = len(df_85.drop_duplicates(subset=['Player'], keep='first'))

#Age 27
df_86 = df_playerdt[df_playerdt['Age'] == 27.0]
#print(df_86[['Player', 'Age']])
print('Total of Player Age(27):', len(df_86.drop_duplicates(subset=['Player'], keep='first')))
df_010 = len(df_86.drop_duplicates(subset=['Player'], keep='first'))

#Age 28
df_87 = df_playerdt[df_playerdt['Age'] == 28.0]
#print(df_87[['Player', 'Age']])
print('Total of Player Age(28):', len(df_87.drop_duplicates(subset=['Player'], keep='first')))
df_011 = len(df_87.drop_duplicates(subset=['Player'], keep='first'))

#Age 29
df_88 = df_playerdt[df_playerdt['Age'] == 29.0]
#print(df_88[['Player', 'Age']])
print('Total of Player Age(29):', len(df_88.drop_duplicates(subset=['Player'], keep='first')))
df_012 = len(df_88.drop_duplicates(subset=['Player'], keep='first'))

#Age 30
df_89 = df_playerdt[df_playerdt['Age'] == 30.0]
#print(df_89[['Player', 'Age']])
print('Total of Player Age(30):', len(df_89.drop_duplicates(subset=['Player'], keep='first')))
df_013 = len(df_89.drop_duplicates(subset=['Player'], keep='first'))

#Age 31
df_90 = df_playerdt[df_playerdt['Age'] == 31.0]
#print(df_90[['Player', 'Age']])
print('Total of Player Age(31):', len(df_90.drop_duplicates(subset=['Player'], keep='first')))
df_014 = len(df_90.drop_duplicates(subset=['Player'], keep='first'))

#Age 32
df_91 = df_playerdt[df_playerdt['Age'] == 32.0]
#print(df_91[['Player', 'Age']])
print('Total of Player Age(32):', len(df_91.drop_duplicates(subset=['Player'], keep='first')))
df_015 = len(df_91.drop_duplicates(subset=['Player'], keep='first'))

#Age 33
df_92 = df_playerdt[df_playerdt['Age'] == 33.0]
#print(df_92[['Player', 'Age']])
print('Total of Player Age(33):', len(df_92.drop_duplicates(subset=['Player'], keep='first')))
df_016 = len(df_92.drop_duplicates(subset=['Player'], keep='first'))

#Age 34
df_93 = df_playerdt[df_playerdt['Age'] == 34.0]
#print(df_93[['Player', 'Age']])
print('Total of Player Age(34):', len(df_93.drop_duplicates(subset=['Player'], keep='first')))
df_017 = len(df_93.drop_duplicates(subset=['Player'], keep='first'))

#Age 35
df_94 = df_playerdt[df_playerdt['Age'] == 35.0]
#print(df_94[['Player', 'Age']])
print('Total of Player Age(35):', len(df_94.drop_duplicates(subset=['Player'], keep='first')))
df_018 = len(df_94.drop_duplicates(subset=['Player'], keep='first'))

#Age 36
df_95 = df_playerdt[df_playerdt['Age'] == 36.0]
#print(df_95[['Player', 'Age']])
print('Total of Player Age(36):', len(df_95.drop_duplicates(subset=['Player'], keep='first')))
df_019 = len(df_95.drop_duplicates(subset=['Player'], keep='first'))

#Age 37
df_96 = df_playerdt[df_playerdt['Age'] == 37.0]
#print(df_96[['Player', 'Age']])
print('Total of Player Age(37):', len(df_96.drop_duplicates(subset=['Player'], keep='first')))
df_020 = len(df_96.drop_duplicates(subset=['Player'], keep='first'))

#Age 38
df_97 = df_playerdt[df_playerdt['Age'] == 38.0]
#print(df_97[['Player', 'Age']])
print('Total of Player Age(38):', len(df_97.drop_duplicates(subset=['Player'], keep='first')))
df_021 = len(df_97.drop_duplicates(subset=['Player'], keep='first'))

#Age 39
df_98 = df_playerdt[df_playerdt['Age'] == 39.0]
#print(df_98[['Player', 'Age']])
print('Total of Player Age(39):', len(df_98.drop_duplicates(subset=['Player'], keep='first')))
df_022 = len(df_98.drop_duplicates(subset=['Player'], keep='first'))

#Age 40
df_99 = df_playerdt[df_playerdt['Age'] == 40.0]
#print(df_99[['Player', 'Age']])
print('Total of Player Age(40):', len(df_99.drop_duplicates(subset=['Player'], keep='first')))
df_023 = len(df_99.drop_duplicates(subset=['Player'], keep='first'))

#Age 41
df_100 = df_playerdt[df_playerdt['Age'] == 41.0]
#print(df_100[['Player', 'Age']])
print('Total of Player Age(41):', len(df_100.drop_duplicates(subset=['Player'], keep='first')))
df_024 = len(df_100.drop_duplicates(subset=['Player'], keep='first'))

#Age 42
df_101 = df_playerdt[df_playerdt['Age'] == 42.0]
#print(df_101[['Player', 'Age']])
print('Total of Player Age(42):', len(df_101.drop_duplicates(subset=['Player'], keep='first')))
df_025 = len(df_101.drop_duplicates(subset=['Player'], keep='first'))

#Age 43
df_102 = df_playerdt[df_playerdt['Age'] == 43.0]
#print(df_102[['Player', 'Age']])
print('Total of Player Age(43):', len(df_102.drop_duplicates(subset=['Player'], keep='first')))
df_026 = len(df_102.drop_duplicates(subset=['Player'], keep='first'))

#Age 44
df_103 = df_playerdt[df_playerdt['Age'] == 44.0]
#print(df_103[['Player', 'Age']])
print('Total of Player Age(44):', len(df_103.drop_duplicates(subset=['Player'], keep='first')))
df_027 = len(df_103.drop_duplicates(subset=['Player'], keep='first'))

df_age18to26 = df_001 + df_002 + df_003 + df_004 + df_005 + df_006 + df_007 + df_008 + df_009
print('Age 18-26:', df_age18to26)
df_age27to35 = df_010 + df_011 + df_012 + df_013 + df_014 + df_015 + df_016 + df_017 + df_018
print('Age 27-35:', df_age27to35)
df_age36to44 = df_019 + df_020 + df_021 + df_022 + df_023 + df_024 + df_025 + df_026 + df_027
print('Age 36-44:', df_age36to44)

df_age18to44 = df_001 + df_002 + df_003 + df_004 + df_005 + df_006 + df_007 + df_008 + df_009 + df_010 + df_011 + df_012 + df_013 + df_014 + df_015 + df_016 + df_017 + df_018 + df_019 + df_020 + df_021 + df_022 + df_023 + df_024 + df_025 + df_026 + df_027
print('Age 18-44:', df_age18to44)


# Input Data For Each  Bar Chart
x1 = np.array([1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960])  # từ 488 đến 501 là dữ liệu đầu vào để tạo ra bảng 
x2 = np.array([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970])
x3 = np.array([1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980])
x4 = np.array([1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990])
x5 = np.array([1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000])
x6 = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010])


y1 = np.array([223, 135, 116, 124, 110, 105, 92, 99, 99, 92, 99])
y2 = np.array([93, 113, 117, 111, 114, 111, 123, 151, 168, 171])
y3 = np.array([217, 216, 214, 221, 235, 238, 295, 285, 279, 286])
y4 = np.array([303, 314, 314, 309, 317, 322, 334, 331, 352, 380])
y5 = np.array([386, 386, 390, 403, 406, 428, 441, 439, 440, 439])
y6 = np.array([441, 440, 428, 442, 464, 458, 458, 450, 444, 442])



# Vẽ biểu đồ cột lên từng trục
plt.subplot(2, 3, 1)
plt.bar(x1, y1, color='plum')
plt.title('Chart Show Total of PLayer(1950-1960)', loc='left')
plt.ylabel('Total of Player')
for i in range(len(x1)):
    plt.text(x1[i], y1[i], str(y1[i]), ha='center', va='top')

plt.subplot(2, 3, 2)
plt.bar(x2, y2, color='khaki')
plt.title('Chart Show Total of PLayer(1961-1970)', loc='center')
for i in range(len(x2)):
    plt.text(x2[i], y2[i], str(y2[i]), ha='center', va='center')

plt.subplot(2, 3, 3)
plt.bar(x3, y3, color='pink')
plt.title('Chart Show Total of PLayer(1971-1980)', loc='right')
for i in range(len(x3)):
    plt.text(x3[i], y3[i], str(y3[i]), ha='center', va='center')

plt.subplot(2, 3, 4)
plt.bar(x4, y4, color='linen')
plt.title('Chart Show Total of PLayer(1981-1990)', loc='left')
plt.xlabel('Year')
plt.ylabel('Total of Player')
for i in range(len(x4)):
    plt.text(x4[i], y4[i], str(y4[i]), ha='center', va='center')

plt.subplot(2, 3, 5)
plt.bar(x5, y5, color='lightblue')
plt.title('Chart Show Total of PLayer(1991-2000)', loc='center')
plt.xlabel('Year')
for i in range(len(x5)):
    plt.text(x5[i], y5[i], str(y5[i]), ha='center', va='center')

plt.subplot(2, 3, 6)   
plt.bar(x6, y6, color='orange')  # chỉnh màu cột 
plt.title('Chart Show Total of PLayer(2001-2010)', loc='right')   # tên biều đồ
plt.xlabel('Year')
plt.suptitle('Total of Player In Each Year(1950-2022)')
for i in range(len(x5)):
    plt.text(x6[i], y6[i], str(y6[i]), ha='center', va='center')   # đây là để hiển thị số liệu ở mỗi cột 




# x = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
# x_001 = np.array([2020, 2021, 2022])
# y = np.array([478, 468, 481, 492, 476, 486, 540, 530, 529])
# y_001 = np.array([529, 540, 605])


# plt.bar(x, y)
# for i in range(len(x)):
#     plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')
# plt.xlabel('Year')
# plt.ylabel('Total of Player')
# plt.bar(x_001, y_001)
# for i in range(len(x_001)):
#     plt.text(x_001[i], y_001[i], str(y_001[i]), ha='center', va='bottom')
plt.xlabel('Year')
plt.ylabel('Total of Player')
plt.suptitle('Total of Player(2011-2022)')
plt.show()

#Input Data For Each Pie Chart Age's Player Play In NBA
sizes = [12829/22974*100, 9636/22974*100, 509/22974*100]
colors = ['yellowgreen', 'gold', 'lightskyblue']
labels = ['Age18-26', 'Age27-35', 'Age36-44']
autopct = '%1.1f%%'
startangle = 90

plt.pie(sizes, colors=colors, labels=labels, autopct=autopct, startangle=startangle, shadow=True)
plt.title('Pie Chart Show Age PLayer Play In NBA')
plt.legend(loc='best', bbox_to_anchor=(1, 0.5))
plt.axis('scaled')
plt.show()

#Input Data For Pyplot Chart Age(18-26)
x_01 = np.array(['A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26'])
y_01 = np.array([13, 159, 408, 741, 1947, 2605, 2572, 2280, 2104])
plt.subplot(1, 3, 1)
plt.plot(x_01, y_01, marker='.', color='pink')
plt.title('Pyplot Chart Age(18-26)')
for i in range(len(x_01)):
    plt.text(x_01[i], y_01[i], str(y_01[i]), ha='center', va='center')

#Input Data For Pyplot Chart Age(27-35)

x_02 = np.array(['A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33', 'A34', 'A35'])
y_02 = np.array([1893, 1640, 1453, 1274, 1056, 865, 663, 473, 319])
plt.subplot(1, 3, 2)
plt.plot(x_02, y_02, marker='.', color='yellow')
plt.title('Pyplot Chart Age(27-35)')
for i in range(len(x_02)):
    plt.text(x_02[i], y_02[i], str(y_02[i]), ha='center', va='center')


#Input Data For Pyplot Chart Age(36-44)
x_03 = np.array(['A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44'])
y_03 = np.array([211, 131, 85, 47, 21, 7, 4, 2, 1])
plt.subplot(1, 3, 3)
plt.plot(x_03, y_03, marker='.', color='sandybrown')
plt.title('Pyplot Chart Age(36-44)')
plt.suptitle('Pyplot Chart Age(18-44)')
for i in range(len(x_03)):
    plt.text(x_03[i], y_03[i], str(y_03[i]), ha='center', va='center')

plt.show()





