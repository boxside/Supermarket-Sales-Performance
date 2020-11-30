import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)

data = pd.read_csv(r'C:\Users\fikri\Desktop\pyproj\supermarket\data.csv')
print(data.info())
print(data.head())

data['Date'] = pd.to_datetime(data['Date'])
data['month'] = (data['Date']).dt.month
data['day'] = (data['Date']).dt.day
def hour(time):
    return time.split(':')[0]
data['hours'] = data['Time'].apply(lambda x : f"{hour(x)}")

print(data.head())
print(data.info())

plt.rcParams['figure.figsize']=(20, 30)
plt.style.use('dark_background')

sns.countplot(x='Customer type', hue='Gender', data=data,palette = 'viridis')
plt.xlabel('Customer Type', size=18, labelpad=10)
plt.ylabel('Jumlah', size=18, labelpad=10)
plt.xticks(rotation=45, fontsize=12)

plt.show()
sns.catplot(x="Customer type",hue='Gender',kind='count' , col= 'Branch', data =data)
plt.show()
sns.catplot(y="Product line",hue='Gender',kind='count' ,data =data)
plt.show()
sns.catplot(x="Payment",kind='count' ,data =data)
ax = plt.gca()
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='white', ha='center', va='bottom')
plt.show()
sns.catplot(x="Payment",hue='Gender',kind='count' ,data =data)
plt.show()
#RATING ANALYSIS
day_revenue= data.groupby(['month','day'])['Total'].sum().reset_index()
sns.catplot(x="day",kind='count',data =data)
ax = plt.gca()

plt.show()


day_high = data[data['day'] == 15].groupby('Product line')['Total'].sum().reset_index()
sns.catplot(x="Total",y='Product line',kind='bar',data =data)
ax = plt.gca()
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='white', ha='center', va='bottom')
plt.show()


print(day_revenue.info())
sns.boxplot(x='Branch',y='Rating', data=data,palette = 'viridis')
plt.show()

sns.boxenplot(x='Product line',y='Rating', data=data,palette = 'viridis')
plt.show()

sns.swarmplot(x='Branch',y='Rating',hue='Gender', data=data)
plt.show()

#PRODUCT AND EARNING ANALYSIS
revenue_branch = data.groupby('Branch')['Total'].sum().reset_index()
print(revenue_branch)


sns.barplot(x='Branch',y='Total', data=revenue_branch,palette = 'viridis' )
ax = plt.gca()
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='white', ha='center', va='bottom')
plt.show()


#asaasadsdas
revenue_product = data.groupby('Product line')['Total'].sum().reset_index()
revenue_product = revenue_product.sort_values(by='Total', ascending=False)
print(revenue_product.info())


sns.barplot(y='Product line',x='Total', data=revenue_product,palette = 'rocket')
plt.show()

month_data = data.groupby(['month','Branch'])['Total'].sum().reset_index()
print(month_data)

sns.barplot(x='Branch',y='Total',hue='month', data=month_data,palette = 'viridis')
ax = plt.gca()
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='white', ha='center', va='bottom')
plt.show()

sns.catplot(x="Total",  y = 'Product line', col= 'month',kind='bar' , row= 'Branch', data =data)
plt.show()


time_sold = data.groupby('hours')['Quantity'].sum().reset_index()
sns.lineplot(x='hours',y='Quantity', data=time_sold)

plt.show()

sns.relplot(x="hours",  y = 'Quantity', col= 'month' , row= 'Branch', kind="line", data =data)
plt.show()

payment_revenue = data.groupby('Payment')['Total'].sum().reset_index()
payment_revenue = payment_revenue.sort_values(by='Total', ascending=False)
sns.barplot(x='Total',y='Payment', data=payment_revenue,palette = 'viridis')
plt.show()

member_revenue = data.groupby('Customer type')['Total'].sum().reset_index()
member_revenue = member_revenue.sort_values(by='Total', ascending=False)
sns.barplot(y='Total',x='Customer type', data=member_revenue,palette = 'gnuplot')
ax = plt.gca()
for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='white', ha='center', va='bottom')
plt.show()

