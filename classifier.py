def classify(desc):
    if 'valvula' in desc.lower():
        return {'ncm': '8481.80.99', 'confianza': 0.5}
    return {'ncm': '9999.99.99', 'confianza': 0.2}
