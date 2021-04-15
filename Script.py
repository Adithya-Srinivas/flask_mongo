from flask import Flask, render_template,url_for, request, redirect
import pymongo

app = Flask(__name__, template_folder='./templates')

client = pymongo.MongoClient(
   'mongodb+srv://Scrap:Scrap123@cluster0.vofcb.mongodb.net/assesments?retryWrites=true&w=majority')
db = client.assesments
collection = db.grant
collection1 = db.case_studies





@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submitform', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        if data['input'].capitalize() == 'Grant':
            grant = collection.find()
            text = []
            def fun():
                for doc in grant:
                    list = doc
                    text.append(list)
                return text

            return render_template("grant.html",
                                             title= fun())
        elif data['input'].capitalize()=='Case studies':
            case_studies = collection1.find()
            text = []
            def fun():
                for id,doc in enumerate(case_studies):
                    title = doc['title']
                    link = doc['link']
                    challenge = doc['Challenge']
                    Solution = doc['Solution']
                    Business = doc['Business']

                    return title,link,challenge,Solution,Business

            return render_template("case_studies.html",
                                   title=fun())
        else:
            return 'wrong input'

    else:

        return 'Oooopps'+'Something went wrong'
