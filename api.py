from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Aluno(Resource):
    def post(self):
        aluno = request.form.get('aluno')
        return jsonify({'aluno': aluno})

    def get(self):
        return {
            'name': 'Mateus Oliveira',
            'escola': "IFRN/Par",
            'orientador': "Jurandy",
            'curso': 'Informática',
            'email': 'matews5522@gmail.com',
            'phone': '084998177501',
        }
    
    def put(self):
        aluno = request.get_json()['aluno']
        escola = request.get_json()['escola']      
        return jsonify({
            'aluno': aluno,
            'escola': escola,
        })

    def delete(self):
        cpf = request.query_string
        cpf = str(cpf).split('=')[1].replace("'", "")
        return jsonify({'cpf': cpf})


api.add_resource(Aluno, '/api')


if __name__ == '__main__':
    app.run(debug=True)
