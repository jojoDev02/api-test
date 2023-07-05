from flask import Blueprint, jsonify, request
import requests

via_cep_bp= Blueprint('via-cep', __name__)

@via_cep_bp.route('/consulta-cep/<string:cep>', methods=['GET'])
def consulta_cep(cep):
 
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            cep = data['cep']
            rua = data['logradouro']
            bairro = data['bairro']
            cidade = data['localidade']
            uf = data['uf']
            return jsonify({
                'cep': cep,
                'rua': rua,
                'bairro': bairro,
                'cidade': cidade,
                'estado': uf
            })
        else:
            return jsonify({'error': 'CEP não encontrado'}), 404
    else:
        return jsonify({'error': 'Erro na requisição'}), 500