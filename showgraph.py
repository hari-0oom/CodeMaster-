import matplotlib.pyplot as plt
import pandas as pd

def graphUsers():
    df=pd.read_csv("data.csv")
    plt.figure(figsize=(15,10))   # to resize the image just to fit everything
    plt.plot(df["handle"], df["rating"], color="green", marker="o", linewidth=1)
    plt.xlabel('users')
    plt.ylabel('Rating')
    plt.title('CF Rating Graph')
    plt.savefig('graph_users_image.png')
        # no need to Send the graph image just save it main module will call it on its own

def plotRatingChangeForUsers(handles):
    handleslist=handles.split(";")

    df=pd.read_csv("rc_data.csv")
    plt.figure(figsize=(15,10))   # to resize the image just to fit everything
    for i in handleslist:
        df2=df[df.handle == i]
        plt.plot(df2["Time"], df2["newRating"], marker=".",linewidth=1)
    plt.xlabel('users')
    plt.ylabel('Rating')
    plt.title('User Rating Change')
    plt.savefig('graph_user_rating_change.png')
    