from wordcloud import WordCloud
from matplotlib import pyplot as plt
import seaborn as sns


def distribution_plot(data):
    sns.countplot(
        x="label",
        data=data,
    )
    # increase the size of the plot
    plt.rcParams["figure.figsize"] = (10, 7)
    plt.rcParams["font.size"] = 10

    # decrese the x axis label
    plt.xticks(size=10)

    # save the plot
    plt.savefig("./reports/figures/distribution_plot.png")

    plt.show()


def circular_distribution_plot(data):
    data["label"].value_counts().plot.pie(autopct="%1.1f%%")
    plt.title("Distribution of the labels")
    plt.savefig("./reports/figures/circular_distribution_plot.png")
    plt.show()


# # use wordcloud to visualize the most common words in the emails
def wordcloud_plot(data):
    wordcloud = WordCloud(width=800, height=400).generate(" ".join(data["email"]))
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("./reports/figures/wordcloud_plot.png")
    plt.show()
