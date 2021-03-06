import pandas as pd
from matplotlib import pyplot as plt

confirmed_data = pd.read_csv('data/time_series_19-covid-Confirmed.csv')
confirmed_data.replace('Taiwan*', 'China', inplace=True)
columns = confirmed_data.columns
group_by_label = columns[1]
dates = columns[4:]

aggre_data = []
for i, date in enumerate(dates):
    aggre_data.append(confirmed_data.groupby(by=group_by_label)[date].sum())
    if i == 0:
        index = confirmed_data.groupby(by=group_by_label)[date].sum().index.tolist()
confirmed_data = pd.concat(aggre_data, axis=1)
confirmed_data_cn = confirmed_data.loc['China', :]
confirmed_data_rest = confirmed_data.drop(['China'])
confirmed_data_rest = confirmed_data_rest.sum()
confirmed_data_b = pd.concat([confirmed_data_cn, confirmed_data_rest], axis=1)
confirmed_data_b.columns = ['China', 'The rest of the world']

confirmed_data_b.plot(style=['-', '--'], figsize=(6, 4))
plt.xlabel('Date', fontsize=13)
plt.ylabel('Confirmed Cases', fontsize=13)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('png/Confirmed cases.png', dpi=200)
plt.show()

plot_countries = ['Singapore', 'Italy', 'Japan', 'Korea, South']
plot_styles = ['-', '--', '-.', '.']
aggre_data = []
for plot_country in plot_countries:
    s_data = confirmed_data.loc[plot_country, :]
    aggre_data.append(s_data)
confirmed_data_m = pd.concat(aggre_data, axis=1)
confirmed_data_m.columns = plot_countries
confirmed_data_m.iloc[25:, :].plot(style=plot_styles, figsize=(6, 4))
plt.xlabel('Date', fontsize=13)
plt.ylabel('Confirmed Cases', fontsize=13)
plt.tight_layout()
plt.savefig('png/Confirmed Cases of Selected Countries.png', dpi=200)
plt.show()
