import pandas as pd
import json
from flask import Flask, request,render_template
df=pd.read_csv("disase_drugs.csv") 
unique = df['condition'].unique()


app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    result=[]
    data = request.args.to_dict()
    if data is None:
        return render_template('index.html')
    val=data.values()
    req=[]
    Navail=[]
    for x in val:
        if x in unique:
            dat = df.loc[df['condition'] == x]
            length = 5 if len(dat)>5 else len(data)
            dat=dat.sort_values(by ='mean_p', ascending = 0)
            dat=dat.iloc[:,1:][:5]
            dat = dat.to_dict(orient='records')
            dat={x:dat}
            result.append(dat)
        else:
            dat={x:"NO DATA"}
            result.append(dat)

    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)