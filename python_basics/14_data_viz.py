#step-1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#step-2: set a theme
sns.set_theme(style="ticks", color_codes=True)

#step-3 import data set, you can also import your own data
kashti = sns.load_dataset("titanic")
# print(kashti)
#print(kashti.describe)

# #step-4 plot basic graph with 1 variable (count)
# p = sns.countplot(x= "sex", data=kashti) # we don't need y-axis, as 'count' is already there.
# #sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=kashti)
# plt.show()

# #.step-5 plot basic graph with 2 variable (count)
# p = sns.countplot(x= "sex", data=kashti, hue="class") # hue=color
# plt.show()

#.step-6 plot basic graph with 2 variable (count) with title
p = sns.countplot(x= "sex", data=kashti, hue="class") # hue=color
p.set_title("Ammar bhai ka count plot for kashti")
plt.show()
