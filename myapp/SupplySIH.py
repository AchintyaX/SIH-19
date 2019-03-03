def graphgen():
        dataset = pd.read_csv('FinalSheet.csv')

        i = random.randrange(0,6,1)

        height = dataset.iloc[2:,(2*i+1)].values

        H = list(map(int,height))
        bars = dataset.iloc[2:,0].values
        y_pos = np.arange(len(bars))

        status = dataset.iloc[2:,2*i+2].values
        S = list(map(int,status))

        my_color = np.where(dataset.iloc[:,2*i+2].values=='2','red',np.where(dataset.iloc[:,2*i+2].values=='1','yellow','green'))
        plt.bar(y_pos,H,color=my_color)
        plt.xlabel('Months')
        plt.ylabel('Capacity')
        plt.title('Supply Status')  
        plt.xticks(y_pos, bars)
        plt.savefig('templates/myapp/bookss_read.png')
