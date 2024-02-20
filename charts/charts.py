import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ['a','b','c']
    values = [200,150,100]
    print('enter here, tanque puto')
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()